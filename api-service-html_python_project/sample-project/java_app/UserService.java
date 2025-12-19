import java.util.*;

public class UserService {
    // Issue: Inappropriate data structure
    private Vector<String> userNames = new Vector<>();
    
    // Issue: Missing validation
    public void addUser(String name, int age) {
        if (age > 0) {  // Issue: No else
            userNames.add(name);
        }
        // Missing else handling
    }
    
    // Issue: Complex conditional logic
    public boolean validateUser(String username, String password, boolean isAdmin) {
        if (username != null && !username.isEmpty()) {
            if (password != null && password.length() >= 8) {
                if (isAdmin || username.startsWith("user_")) {
                    return true;
                }
            }
        }
        return false;
    }
    
    // Issue: Implicit return in lambda
    public void processUsers() {
        List<String> users = Arrays.asList("user1", "user2", "admin");
        users.forEach(user -> {
            if (user.equals("admin")) {
                System.out.println("Admin user");
            }
            // Missing return in some paths
        });
    }
}
