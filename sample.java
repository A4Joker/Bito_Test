import java.util.*;
import java.io.*;
import java.sql.*;

public class CriticalIssues {
    // CRITICAL: Hardcoded credentials
    private static final String PASSWORD = "admin123";
    private static final String API_KEY = "sk-1234567890abcdef";
    
    // CRITICAL: SQL Injection vulnerability
    public User findUser(String username) throws SQLException {
        Connection conn = DriverManager.getConnection("jdbc:mysql://localhost/db", "root", PASSWORD);
        Statement stmt = conn.createStatement();
        // Direct string concatenation in SQL - SQL injection risk
        String query = "SELECT * FROM users WHERE username = '" + username + "'";
        ResultSet rs = stmt.executeQuery(query);
        
        // CRITICAL: Resource leak - connections not closed
        if (rs.next()) {
            return new User(rs.getString("name"), rs.getString("email"));
        }
        return null;
    }
    
    // CRITICAL: Null pointer dereference
    public void processUser(User user) {
        // No null check before accessing user properties
        System.out.println("Processing user: " + user.getName());
        System.out.println("Email: " + user.getEmail().toLowerCase());
        
        // CRITICAL: Potential array index out of bounds
        String[] parts = user.getEmail().split("@");
        System.out.println("Domain: " + parts[1]); // No check if parts.length > 1
    }
    
    // CRITICAL: Command injection vulnerability
    public void executeCommand(String userInput) throws IOException {
        Runtime runtime = Runtime.getRuntime();
        // Direct execution of user input - command injection risk
        Process process = runtime.exec("ls -la " + userInput);
    }
    
    // CRITICAL: Infinite loop potential
    public void processData(List<String> data) {
        int i = 0;
        while (i < data.size()) {
            String item = data.get(i);
            if (item.contains("skip")) {
                // Missing i++ increment - infinite loop
                continue;
            }
            System.out.println(item);
            i++;
        }
    }
    
    // CRITICAL: Exception swallowing
    public void riskyOperation() {
        try {
            // Some risky operation
            Thread.sleep(1000);
            throw new RuntimeException("Something went wrong");
        } catch (Exception e) {
            // Swallowing exception without logging
        }
    }
    
    // CRITICAL: Race condition
    private static int counter = 0;
    public void incrementCounter() {
        // Non-atomic operation on shared variable
        counter = counter + 1;
    }
    
    // CRITICAL: Memory leak potential
    private static List<String> staticList = new ArrayList<>();
    public void addToStaticList(String item) {
        // Adding to static collection without cleanup
        staticList.add(item);
    }
    
    // CRITICAL: Unsafe deserialization
    public Object deserializeObject(byte[] data) throws Exception {
        ByteArrayInputStream bis = new ByteArrayInputStream(data);
        ObjectInputStream ois = new ObjectInputStream(bis);
        // Deserializing untrusted data
        return ois.readObject();
    }
    
    // CRITICAL: Path traversal vulnerability
    public String readFile(String filename) throws IOException {
        // No validation of filename - path traversal risk
        File file = new File("/app/data/" + filename);
        BufferedReader reader = new BufferedReader(new FileReader(file));
        StringBuilder content = new StringBuilder();
        String line;
        while ((line = reader.readLine()) != null) {
            content.append(line);
        }
        // Resource leak - reader not closed
        return content.toString();
    }
    
    // CRITICAL: Weak random number generation
    public String generateToken() {
        Random random = new Random();
        return String.valueOf(random.nextInt(1000000));
    }
}

class User {
    private String name;
    private String email;
    
    public User(String name, String email) {
        this.name = name;
        this.email = email;
    }
    
    public String getName() { return name; }
    public String getEmail() { return email; }
}
