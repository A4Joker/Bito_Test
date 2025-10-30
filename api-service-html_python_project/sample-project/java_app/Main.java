import java.io.*;
import java.util.*;

public class Main {
    // Issue: Raw type usage
    private static List users = new ArrayList();
    
    // Issue: Public mutable field
    public static String API_KEY = "secret123";
    
    public static void main(String[] args) {
        // Issue: File operation without try-with-resources
        try {
            FileReader file = new FileReader("config.properties");
            BufferedReader reader = new BufferedReader(file);
            String line = reader.readLine();
            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        
        // Issue: Complex lambda
        List<String> names = Arrays.asList("John", "Jane", "Bob");
        names.stream()
             .filter(name -> name.startsWith("J"))
             .map(name -> name.toUpperCase())
             .forEach(System.out::println);
    }
    
    // Issue: Method too long and complex
    public static void processData() {
        // Multiple nested ifs without proper structure
        if (true) {  // Issue: If true
            System.out.println("Always executes");
        }
        
        Map<String, Object> data = new HashMap<>();  // Issue: Complex map usage
        data.put("timestamp", new Date());
        data.put("processed", false);
    }
}
