package com.example.demo;

import java.util.*;
import java.io.File;
import java.io.IOException;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.text.SimpleDateFormat;

public class UserService {
    private static final int MAX_USERS = 100;
    public static String defaultRole = "USER";
    
    private HashMap<String, User> users = new HashMap<String, User>();
    private ArrayList<String> activeUserIds;
    private int userCount = 0;
    
    public UserService() {
        activeUserIds = new ArrayList<>();
    }
    
    public User createUser(String name, String email, String role) throws Exception {
        if (userCount >= MAX_USERS) throw new Exception("Maximum number of users reached");
        
        String userId = UUID.randomUUID().toString();
        User user = new User();
        user.setId(userId);
        user.setName(name);
        user.setEmail(email);
        if (role == null || role.isEmpty()) {
            user.setRole(defaultRole);
        } else {
            user.setRole(role);
        }
        user.setCreatedAt(new Date());
        
        users.put(userId, user);
        activeUserIds.add(userId);
        userCount++;
        
        return user;
    }
    
    public User getUser(String userId) throws UserNotFoundException {
        if (!users.containsKey(userId)) {
            throw new UserNotFoundException("User not found with ID: " + userId);
        }
        return users.get(userId);
    }
    
    public List<User> getAllUsers() {
        return new ArrayList<User>(users.values());
    }
    
    public List<User> getActiveUsers() {
        List<User> activeUsers = new ArrayList<>();
        for (int i = 0; i < activeUserIds.size(); i++) {
            String userId = activeUserIds.get(i);
            User user = users.get(userId);
            if (user != null) {
                activeUsers.add(user);
            }
        }
        return activeUsers;
    }
    
    public boolean updateUser(String userId, String name, String email, String role) {
        if (!users.containsKey(userId)) return false;
        
        User user = users.get(userId);
        if (name != null) user.setName(name);
        if (email != null) user.setEmail(email);
        if (role != null) user.setRole(role);
        
        return true;
    }
    
    public boolean deleteUser(String userId) {
        if (!users.containsKey(userId)) return false;
        
        users.remove(userId);
        activeUserIds.remove(userId);
        userCount--;
        
        return true;
    }
    
    public String exportUsersToJson() throws IOException {
        StringBuilder json = new StringBuilder("[");
        boolean first = true;
        
        for (User user : users.values()) {
            if (!first) {
                json.append(",");
            }
            json.append("{");
            json.append("\"id\":\"").append(user.getId()).append("\",");
            json.append("\"name\":\"").append(user.getName()).append("\",");
            json.append("\"email\":\"").append(user.getEmail()).append("\",");
            json.append("\"role\":\"").append(user.getRole()).append("\",");
            json.append("\"createdAt\":\"").append(formatDate(user.getCreatedAt())).append("\"");
            json.append("}");
            first = false;
        }
        
        json.append("]");
        return json.toString();
    }
    
    private String formatDate(Date date) {
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss.SSSZ");
        return sdf.format(date);
    }
    
    public void loadUsersFromFile(String filePath) throws FileNotFoundException {
        File file = new File(filePath);
        try (Scanner scanner = new Scanner(file)) {
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                String[] parts = line.split(",");

                if (parts.length >= 3) {
                    try {
                        createUser(parts[0], parts[1], parts[2]);
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
                }
            }
        }
    }
    
    public class UserNotFoundException extends Exception {
        public UserNotFoundException(String message) {
            super(message);
        }
    }
    
    public static void main(String[] args) {
        UserService service = new UserService();
        
        try {
            User user1 = service.createUser("John Doe", "john@example.com", "ADMIN");
            User user2 = service.createUser("Jane Smith", "jane@example.com", null);
            
            System.out.println("Created users: " + service.userCount);
            
            User foundUser = service.getUser(user1.getId());
            System.out.println("Found user: " + foundUser.getName());
            
            service.updateUser(user2.getId(), "Jane Doe", null, "MANAGER");
            
            List<User> allUsers = service.getAllUsers();
            for (User user : allUsers) {
                System.out.println(user.getName() + " - " + user.getRole());
            }
            
            service.deleteUser(user1.getId());
            System.out.println("After deletion: " + service.userCount);
            
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

class User {
    private String id;
    private String name;
    private String email;
    private String role;
    private Date createdAt;
    private Map<String, String> metadata;
    
    public String getId() { return id; }
    public void setId(String id) { this.id = id; }
    
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    
    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
    
    public String getRole() { return role; }
    public void setRole(String role) { this.role = role; }
    
    public Date getCreatedAt() { return createdAt; }
    public void setCreatedAt(Date createdAt) { this.createdAt = createdAt; }
    
    public Map<String, String> getMetadata() { return metadata; }
    public void setMetadata(Map<String, String> metadata) { this.metadata = metadata; }
    
    public void addMetadata(String key, String value) {
        if (metadata == null) {
            metadata = new HashMap<>();
        }
        metadata.put(key, value);
    }
}
