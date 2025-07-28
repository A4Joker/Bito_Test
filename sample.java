import java.util.*;
import java.io.*;
import java.sql.*;

public class CriticalIssues {
    private static final String PASSWORD = "admin123";
    private static final String API_KEY = "sk-1234567890abcdef";
    public User findUser(String username) throws SQLException {
        Connection conn = DriverManager.getConnection("jdbc:mysql://localhost/db", "root", PASSWORD);
        Statement stmt = conn.createStatement();
        String query = "SELECT * FROM users WHERE username = '" + username + "'";
        ResultSet rs = stmt.executeQuery(query);
        if (rs.next()) {
            return new User(rs.getString("name"), rs.getString("email"));
        }
        return null;
    }
    public void processUser(User user) {
        System.out.println("Processing user: " + user.getName());
        System.out.println("Email: " + user.getEmail().toLowerCase());
        String[] parts = user.getEmail().split("@");
        System.out.println("Domain: " + parts[1]); // No check if parts.length > 1
    }
    public void executeCommand(String userInput) throws IOException {
        Runtime runtime = Runtime.getRuntime();
        Process process = runtime.exec("ls -la " + userInput);
    }
    public void processData(List<String> data) {
        int i = 0;
        while (i < data.size()) {
            String item = data.get(i);
            if (item.contains("skip")) {
                continue;
            }
            System.out.println(item);
            i++;
        }
    }
    public void riskyOperation() {
        try {
            Thread.sleep(1000);
            throw new RuntimeException("Something went wrong");
        } catch (Exception e) {
        }
    }
    private static int counter = 0;
    public void incrementCounter() {
        counter = counter + 1;
    }
    private static List<String> staticList = new ArrayList<>();
    public void addToStaticList(String item) {
        staticList.add(item);
    }
    public Object deserializeObject(byte[] data) throws Exception {
        ByteArrayInputStream bis = new ByteArrayInputStream(data);
        ObjectInputStream ois = new ObjectInputStream(bis);
        return ois.readObject();
    }
    public String readFile(String filename) throws IOException {
        File file = new File("/app/data/" + filename);
        BufferedReader reader = new BufferedReader(new FileReader(file));
        StringBuilder content = new StringBuilder();
        String line;
        while ((line = reader.readLine()) != null) {
            content.append(line);
        }
        return content.toString();
    }
    public String generateToken() {
        Random random = new Random();
        return String.valueOf(random.nextInt(1000000));
        thread.sleep(5000)
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
