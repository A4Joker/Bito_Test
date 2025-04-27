import java.io.*;
import java.sql.*;
import java.util.*;
import java.text.SimpleDateFormat;
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;

// Class name doesn't follow Java conventions (should be PascalCase)
public class bad_java_code {
    
    // Public non-final fields (violates encapsulation)
    public String userName = "admin";
    public String Password = "SuperSecretPassword123!"; // Mixed case naming
    
    // Too many static fields
    static int a;
    static String b;
    static List c;
    static Map d;
    static Object e;
    
    // Unused fields
    private int unusedField;
    
    // Non-private field
    public Connection dbConnection;
    
    // Magic numbers
    private static final int SOME_CONSTANT = 42;
    
    // Constructor doesn't call super()
    public bad_java_code() {
        // Empty constructor with no super() call
    }
    
    // Method with too many parameters
    public void processData(String param1, int param2, boolean param3, 
                           List<String> param4, Map<String, Object> param5,
                           double param6, long param7, char param8) {
        // Local variable hides field
        String userName = "localUser";
        
        // Unused local variable
        int unusedLocal = 10;
        
        // Empty if statement
        if (param3) {
            // Empty block
        }
        
        // Deeply nested if statements
        if (param1 != null) {
            if (param1.length() > 0) {
                if (param2 > 0) {
                    if (param3) {
                        System.out.println("Too deeply nested!");
                    }
                }
            }
        }
        
        // Switch without default
        switch (param2) {
            case 1:
                System.out.println("One");
                break;
            case 2:
                System.out.println("Two");
                break;
            // Missing default case
        }
        
        // Inefficient string concatenation in loop
        String result = "";
        for (int i = 0; i < param2; i++) {
            result = result + "item" + i; // Should use StringBuilder
        }
        
        // Comparing strings with == instead of equals()
        if (param1 == "test") {
            System.out.println("Strings equal");
        }
        
        // Ignoring method return value
        param1.trim();
        
        // Potential null pointer
        System.out.println(param4.size()); // No null check
    }
    
    // Method with non-standard naming
    public void ProcessData() {
        // Method name should be camelCase
    }
    
    // Method that catches Exception
    public void catchAllExceptions() {
        try {
            File file = new File("missing.txt");
            FileInputStream fis = new FileInputStream(file);
        } catch (Exception e) {
            // Catching generic Exception
            System.out.println("Error");
            // e.printStackTrace(); // Commented out error handling
        }
    }
    
    // Method with security vulnerability (SQL Injection)
    public void findUser(String username) throws SQLException {
        // SQL Injection vulnerability
        Statement stmt = dbConnection.createStatement();
        ResultSet rs = stmt.executeQuery("SELECT * FROM users WHERE username = '" + username + "'");
        
        // Resource leak (not closing ResultSet, Statement)
        while (rs.next()) {
            System.out.println(rs.getString("name"));
        }
    }
    
    // Method with hardcoded encryption key (security issue)
    public byte[] encryptData(String data) throws Exception {
        // Hardcoded encryption key
        String key = "hardcodedkey12345";
        SecretKeySpec secretKey = new SecretKeySpec(key.getBytes(), "AES");
        
        Cipher cipher = Cipher.getInstance("AES");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey);
        return cipher.doFinal(data.getBytes());
    }
    
    // Method with thread safety issues
    private SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd");
    
    public String formatDate(Date date) {
        // SimpleDateFormat is not thread-safe
        return dateFormat.format(date);
    }
    
    // Method that doesn't release resources properly
    public List<String> readFile(String filename) {
        List<String> lines = new ArrayList<>();
        BufferedReader reader = null;
        try {
            reader = new BufferedReader(new FileReader(filename));
            String line;
            while ((line = reader.readLine()) != null) {
                lines.add(line);
            }
            // Not closing reader in finally block
        } catch (IOException e) {
            e.printStackTrace();
        }
        return lines;
    }
    
    // Method with dead code
    public int computeValue(int x) {
        int result = x * 2;
        result = x * 3; // Overwrites previous value, making it dead code
        
        if (false) { // Unreachable code
            System.out.println("This will never execute");
        }
        
        return result;
    }
    
    // Method with boxed primitive just to call toString
    public void inefficientToString(int value) {
        String str = new Integer(value).toString(); // Should use Integer.toString(value)
    }
    
    // Method that uses deprecated API
    public void useDeprecatedMethod() {
        Date date = new Date();
        int day = date.getDay(); // Deprecated method
    }
    
    // Method with empty catch block
    public void emptyCatch() {
        try {
            int[] arr = new int[5];
            arr[10] = 20; // ArrayIndexOutOfBoundsException
        } catch (ArrayIndexOutOfBoundsException e) {
            // Empty catch block
        }
    }
    
    // Overriding equals without hashCode
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        bad_java_code other = (bad_java_code) obj;
        return userName.equals(other.userName);
        // Missing hashCode override
    }
    
    // Synchronizing on non-final field
    private Object lock = new Object();
    
    public void synchronizedMethod() {
        synchronized (lock) { // lock is not final
            System.out.println("Thread-safe operation");
        }
    }
    
    // Inner class with static reference to outer class (memory leak risk)
    class InnerClass {
        public void doSomething() {
            System.out.println(userName); // Reference to outer class
        }
    }
    
    // Main method with various issues
    public static void main(String[] args) {
        // Creating objects without checking for exceptions
        bad_java_code instance = new bad_java_code();
        
        // Hardcoded file path
        File config = new File("C:\\Program Files\\App\\config.xml");
        
        // Busy wait
        boolean condition = true;
        while (condition) {
            // Busy wait without proper condition change
            System.out.println("Waiting...");
            // Missing condition update
        }
        
        // Boxed primitives equality check
        Integer int1 = 128;
        Integer int2 = 128;
        if (int1 == int2) { // Should use equals for Integer objects
            System.out.println("Equal");
        }
        
        // Inefficient collection access
        List<String> items = new ArrayList<>();
        for (int i = 0; i < 100; i++) {
            items.add("Item " + i);
        }
        
        // Using iterator inefficiently
        for (int i = 0; i < items.size(); i++) {
            System.out.println(items.get(i)); // Should use for-each loop
        }
        
        // Unnecessary object creation
        String s1 = "hello";
        String s2 = new String("hello"); // Unnecessary new
        
        // Non-serializable class implementing Serializable
        NonSerializableClass obj = new NonSerializableClass();
    }
    
    // Implementing Serializable without serialVersionUID
    static class NonSerializableClass implements Serializable {
        // Missing serialVersionUID
        private Socket socket; // Non-serializable field in Serializable class
    }
}

// Utility class without private constructor
class Utils {
    // Should have private constructor
    
    // Public static method
    public static void helperMethod() {
        System.out.println("Helper");
    }
}

// Empty class
class EmptyClass {
    // Empty class
}

// Class with poorly designed clone method
class CloneableClass implements Cloneable {
    private int value;
    
    @Override
    public Object clone() throws CloneNotSupportedException {
        return super.clone(); // Doesn't handle deep cloning
    }
}

// Class with finalize method (discouraged)
class ClassWithFinalize {
    @Override
    protected void finalize() throws Throwable {
        // Using finalize is discouraged
        super.finalize();
    }
}
