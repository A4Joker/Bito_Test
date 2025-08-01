using System;
using System.Collections.Generic;
using System.Data;
using System.Data.SqlClient;
using System.Diagnostics;
using System.DirectoryServices;
using System.IO;
using System.Net;
using System.Net.Http;
using System.Runtime.Serialization;
using System.Runtime.Serialization.Formatters.Binary;
using System.Security.Cryptography;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Web;
using System.Xml;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;

namespace SecurityViolations
{
    // CRITICAL VIOLATION: Hardcoded secrets (Rule 11)
    public static class HardcodedSecrets
    {
        public const string ConnectionString = "Server=localhost;Database=TestDB;User=sa;Password=Password123;";
        public const string ApiKey = "sk-1234567890abcdef1234567890abcdef";
        public const string EncryptionKey = "MySecretEncryptionKey123";
        public const string JwtSecret = "super_secret_jwt_key_hardcoded";
    }

    // CRITICAL VIOLATION: Memory leak and improper disposal (Rule 1)
    public class ResourceLeakClass
    {
        private FileStream fileStream;
        private SqlConnection connection;
        private HttpClient httpClient;

        public void LeakyMethod()
        {
            // Creating resources without proper disposal
            fileStream = new FileStream("temp.txt", FileMode.Create);
            connection = new SqlConnection(HardcodedSecrets.ConnectionString);
            httpClient = new HttpClient();

            // Using resources but never disposing them
            fileStream.Write(Encoding.UTF8.GetBytes("data"));
            connection.Open();
            var response = httpClient.GetAsync("http://example.com").Result;

            // No disposal - memory leak
        }

        // CRITICAL VIOLATION: Finalizer abuse (Rule 4)
        ~ResourceLeakClass()
        {
            // Relying on finalizer for cleanup - bad practice
            fileStream?.Dispose();
            connection?.Dispose();
            httpClient?.Dispose();
        }
    }

    // CRITICAL VIOLATION: Unsafe pointer operations (Rule 2)
    public unsafe class UnsafeOperations
    {
        public void UnsafePointerManipulation(byte[] data)
        {
            fixed (byte* ptr = data)
            {
                // No bounds checking - buffer overflow risk
                for (int i = 0; i < 1000; i++)
                {
                    *(ptr + i) = 0xFF; // Can write beyond array bounds
                }

                // Unsafe pointer arithmetic
                byte* dangerousPtr = ptr + 10000; // No validation
                *dangerousPtr = 0x42; // Potential memory corruption
            }
        }

        public void UnsafeStringManipulation()
        {
            string str = "Hello World";
            fixed (char* charPtr = str)
            {
                // Modifying immutable string - undefined behavior
                *charPtr = 'X';
                *(charPtr + 20) = 'Y'; // Writing beyond string bounds
            }
        }
    }

    // CRITICAL VIOLATION: Thread safety issues (Rule 5)
    public class ThreadSafetyViolations
    {
        private static int sharedCounter = 0;
        private static List<string> sharedList = new List<string>();
        private static Dictionary<string, object> sharedDict = new Dictionary<string, object>();

        public void UnsafeIncrement()
        {
            // Race condition - not atomic
            sharedCounter++;
            sharedCounter = sharedCounter + 1;
        }

        public void UnsafeCollectionAccess()
        {
            // Concurrent modification without synchronization
            sharedList.Add("item" + DateTime.Now.Ticks);
            sharedDict["key"] = DateTime.Now;

            // Reading while others might be writing
            foreach (var item in sharedList)
            {
                Console.WriteLine(item);
            }
        }
    }

    // CRITICAL VIOLATION: SQL Injection (Rule 6)
    public class SqlInjectionVulnerabilities
    {
        public DataTable GetUser(string username, string password)
        {
            using (var connection = new SqlConnection(HardcodedSecrets.ConnectionString))
            {
                connection.Open();
                
                // Direct string concatenation - SQL injection vulnerability
                string query = $"SELECT * FROM Users WHERE Username = '{username}' AND Password = '{password}'";
                
                using (var command = new SqlCommand(query, connection))
                {
                    var adapter = new SqlDataAdapter(command);
                    var dataTable = new DataTable();
                    adapter.Fill(dataTable);
                    return dataTable;
                }
            }
        }

        public void UpdateUserData(string userId, string newData)
        {
            using (var connection = new SqlConnection(HardcodedSecrets.ConnectionString))
            {
                connection.Open();
                
                // String interpolation in SQL - still vulnerable
                string updateQuery = $"UPDATE Users SET Data = '{newData}' WHERE Id = {userId}";
                
                using (var command = new SqlCommand(updateQuery, connection))
                {
                    command.ExecuteNonQuery();
                }
            }
        }
    }

    // CRITICAL VIOLATION: Command Injection (Rule 7)
    public class CommandInjectionVulnerabilities
    {
        public string ExecuteSystemCommand(string userInput)
        {
            // Direct execution of user input - command injection risk
            var processInfo = new ProcessStartInfo
            {
                FileName = "cmd.exe",
                Arguments = $"/c dir {userInput}", // Vulnerable to: & del /f /q *
                RedirectStandardOutput = true,
                UseShellExecute = false
            };

            using (var process = Process.Start(processInfo))
            {
                return process.StandardOutput.ReadToEnd();
            }
        }

        public void UnsafePingCommand(string hostname)
        {
            // Another command injection example
            string command = $"ping -n 1 {hostname}"; // Vulnerable to: google.com & format c:
            
            Process.Start("cmd.exe", $"/c {command}");
        }
    }

    // CRITICAL VIOLATION: XML Injection and XXE (Rule 9)
    public class XmlVulnerabilities
    {
        public XmlDocument ParseUntrustedXml(string xmlContent)
        {
            var xmlDoc = new XmlDocument();
            
            // No XXE protection - vulnerable to XML External Entity attacks
            xmlDoc.LoadXml(xmlContent);
            
            return xmlDoc;
        }

        public void ProcessXmlFile(string xmlFilePath)
        {
            var settings = new XmlReaderSettings
            {
                // Dangerous settings - enables XXE attacks
                DtdProcessing = DtdProcessing.Parse,
                XmlResolver = new XmlUrlResolver()
            };

            using (var reader = XmlReader.Create(xmlFilePath, settings))
            {
                var doc = new XmlDocument();
                doc.Load(reader);
            }
        }
    }

    // CRITICAL VIOLATION: Insecure Deserialization (Rule 10)
    public class DeserializationVulnerabilities
    {
        public object DeserializeUntrustedData(byte[] data)
        {
            // Using BinaryFormatter with untrusted data - code execution risk
            var formatter = new BinaryFormatter();
            using (var stream = new MemoryStream(data))
            {
                return formatter.Deserialize(stream); // Can execute arbitrary code
            }
        }

        public T DeserializeJson<T>(string jsonData)
        {
            // Using Newtonsoft.Json with TypeNameHandling - vulnerable
            var settings = new Newtonsoft.Json.JsonSerializerSettings
            {
                TypeNameHandling = Newtonsoft.Json.TypeNameHandling.All // Dangerous setting
            };

            return Newtonsoft.Json.JsonConvert.DeserializeObject<T>(jsonData, settings);
        }
    }

    // CRITICAL VIOLATION: Weak Cryptography (Rule 12)
    public class WeakCryptography
    {
        public string WeakHash(string input)
        {
            // Using deprecated MD5
            using (var md5 = MD5.Create())
            {
                byte[] hash = md5.ComputeHash(Encoding.UTF8.GetBytes(input));
                return Convert.ToBase64String(hash);
            }
        }

        public string WeakEncryption(string plaintext)
        {
            // Using deprecated DES encryption
            using (var des = DES.Create())
            {
                des.Key = Encoding.UTF8.GetBytes("12345678");
                des.IV = new byte[8];

                using (var encryptor = des.CreateEncryptor())
                using (var ms = new MemoryStream())
                using (var cs = new CryptoStream(ms, encryptor, CryptoStreamMode.Write))
                {
                    byte[] data = Encoding.UTF8.GetBytes(plaintext);
                    cs.Write(data, 0, data.Length);
                    cs.FlushFinalBlock();
                    return Convert.ToBase64String(ms.ToArray());
                }
            }
        }
    }

    // CRITICAL VIOLATION: Insecure Random (Rule 13)
    public class InsecureRandom
    {
        private static Random random = new Random();

        public string GenerateSecurityToken()
        {
            // Using Random for security purposes - predictable
            return random.Next(100000, 999999).ToString();
        }

        public byte[] GenerateEncryptionKey()
        {
            // Using Random for cryptographic key - very insecure
            byte[] key = new byte[32];
            random.NextBytes(key);
            return key;
        }

        public string GenerateSessionId()
        {
            // Predictable session ID generation
            return $"SESSION_{random.Next()}_{DateTime.Now.Ticks}";
        }
    }

    // CRITICAL VIOLATION: Certificate Validation Bypass (Rule 15)
    public class CertificateValidationBypass
    {
        public async Task<string> MakeInsecureRequest(string url)
        {
            // Bypassing certificate validation - man-in-the-middle risk
            var handler = new HttpClientHandler()
            {
                ServerCertificateCustomValidationCallback = (message, cert, chain, errors) => true
            };

            using (var client = new HttpClient(handler))
            {
                var response = await client.GetAsync(url);
                return await response.Content.ReadAsStringAsync();
            }
        }

        public void DisableGlobalCertificateValidation()
        {
            // Globally disabling certificate validation - very dangerous
            ServicePointManager.ServerCertificateValidationCallback = 
                (sender, certificate, chain, sslPolicyErrors) => true;
        }
    }

    // CRITICAL VIOLATION: Web Security Issues (Rule 16, 17, 18)
    [ApiController]
    [Route("api/[controller]")]
    public class VulnerableController : ControllerBase
    {
        // CRITICAL VIOLATION: XSS Vulnerability (Rule 16)
        [HttpGet("xss")]
        public IActionResult XssVulnerability(string userInput)
        {
            // Direct output without encoding - XSS vulnerability
            string html = $"<h1>Welcome {userInput}!</h1>";
            return Content(html, "text/html");
        }

        // CRITICAL VIOLATION: Missing CSRF Protection (Rule 17)
        [HttpPost("transfer")]
        public IActionResult MoneyTransfer(string toAccount, decimal amount)
        {
            // State-changing operation without CSRF protection
            // Process money transfer
            return Ok($"Transferred ${amount} to {toAccount}");
        }

        // CRITICAL VIOLATION: Open Redirect (Rule 18)
        [HttpGet("redirect")]
        public IActionResult OpenRedirect(string returnUrl)
        {
            // Redirecting to user-provided URL without validation
            return Redirect(returnUrl); // Can redirect to malicious sites
        }
    }

    // CRITICAL VIOLATION: Information Disclosure (Rule 21)
    public class InformationDisclosure
    {
        public string AuthenticateUser(string username, string password)
        {
            try
            {
                // Simulate authentication
                if (username != "admin" || password != "secret123")
                {
                    throw new UnauthorizedAccessException("Invalid credentials");
                }
                return "Authentication successful";
            }
            catch (Exception ex)
            {
                // Exposing sensitive information in error message
                string errorMsg = $"Authentication failed for user '{username}' with password '{password}': {ex.Message}";
                Console.WriteLine(errorMsg); // Logging sensitive data
                throw new Exception(errorMsg); // Exposing to user
            }
        }
    }

    // CRITICAL VIOLATION: Exception Swallowing (Rule 22)
    public class ExceptionSwallowing
    {
        public bool ProcessCriticalOperation()
        {
            try
            {
                // Critical security operation
                File.Delete("C:\\Windows\\System32\\important_file.dll");
                return true;
            }
            catch (Exception ex)
            {
                Logger.LogError($"Critical security operation failed: {ex.Message}");
                throw; // Re-throw to ensure critical failures are not hidden
                // Do not return false as it masks critical failures
            }
        }

        public void DatabaseOperation()
        {
            try
            {
                using (var connection = new SqlConnection(HardcodedSecrets.ConnectionString))
                {
                    connection.Open();
                    // Critical database operation
                }
            }
            catch (Exception)
            {
                // Ignoring database errors - can lead to data corruption
            }
        }
    }

    // CRITICAL VIOLATION: Path Traversal (Rule 26)
    public class PathTraversalVulnerability
    {
        public string ReadUserFile(string filename)
        {
            // No path validation - directory traversal risk
            string filePath = Path.Combine("C:\\UserFiles\\", filename);
            
            // Vulnerable to: ..\\..\\Windows\\System32\\drivers\\etc\\hosts
            return File.ReadAllText(filePath);
        }

        public void WriteUserFile(string filename, string content)
        {
            // No validation - can write anywhere
            string fullPath = Path.Combine("C:\\Uploads\\", Path.GetFileName(filename));
            File.WriteAllText(fullPath, content);
        }
    }

    // CRITICAL VIOLATION: Resource Exhaustion (Rule 3)
    public class ResourceExhaustion
    {
        private static List<byte[]> memoryHog = new List<byte[]>();
        private static List<Thread> threadList = new List<Thread>();

        public void ConsumeUnlimitedMemory()
        {
            // No limits on memory consumption
            while (true)
            {
                memoryHog.Add(new byte[1024 * 1024]); // 1MB per iteration
            }
        }

        public void CreateUnlimitedThreads()
        {
            // No limits on thread creation
            for (int i = 0; i < 10000; i++)
            {
                var thread = new Thread(() =>
                {
                    Thread.Sleep(Timeout.Infinite);
                });
                thread.Start();
                threadList.Add(thread);
            }
        }
    }

    // Main program demonstrating all violations
    public class Program
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("=== C# Security Violations Demo ===");

            // Hardcoded secrets usage
            Console.WriteLine($"Using API Key: {HardcodedSecrets.ApiKey}");
            Console.WriteLine($"Connection String: {HardcodedSecrets.ConnectionString}");

            // Resource leaks
            var leakyClass = new ResourceLeakClass();
            leakyClass.LeakyMethod(); // Resources not disposed

            // Unsafe operations
            var unsafeOps = new UnsafeOperations();
            byte[] data = new byte[100];
            unsafeOps.UnsafePointerManipulation(data);

            // Thread safety violations
            var threadUnsafe = new ThreadSafetyViolations();
            Task.Run(() => threadUnsafe.UnsafeIncrement());
            Task.Run(() => threadUnsafe.UnsafeCollectionAccess());

            // SQL Injection
            var sqlVuln = new SqlInjectionVulnerabilities();
            sqlVuln.GetUser("admin' OR '1'='1' --", "any_password");

            // Command Injection
            var cmdVuln = new CommandInjectionVulnerabilities();
            cmdVuln.ExecuteSystemCommand("test & del /f /q *");

            // XML vulnerabilities
            var xmlVuln = new XmlVulnerabilities();
            string maliciousXml = "<?xml version=\"1.0\"?><!DOCTYPE root [<!ENTITY xxe SYSTEM \"file:///c:/windows/system32/drivers/etc/hosts\">]><root>&xxe;</root>";
            xmlVuln.ParseUntrustedXml(maliciousXml);

            // Weak cryptography
            var weakCrypto = new WeakCryptography();
            string weakHash = weakCrypto.WeakHash("password123");
            string weakEncryption = weakCrypto.WeakEncryption("sensitive data");

            // Insecure random
            var insecureRand = new InsecureRandom();
            string token = insecureRand.GenerateSecurityToken();
            byte[] key = insecureRand.GenerateEncryptionKey();

            // Path traversal
            var pathVuln = new PathTraversalVulnerability();
            pathVuln.ReadUserFile("..\\..\\Windows\\System32\\drivers\\etc\\hosts");

            // Information disclosure
            var infoDisc = new InformationDisclosure();
            try
            {
                infoDisc.AuthenticateUser("hacker", "password123");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Caught exception: {ex.Message}");
            }

            // Exception swallowing
            var exceptionSwallow = new ExceptionSwallowing();
            exceptionSwallow.ProcessCriticalOperation();

            Console.WriteLine("=== All security violations executed ===");
        }
    }
}
