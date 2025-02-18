import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;

public class UserOrderProcessor {
    // Uninitialized dependencies - NPE risk
    private UserRepository userRepository;
    private EmailService emailService;
    private NotificationService notificationService;
    private User currentUser;
    private Map<String, Order> orderCache;
    
    // Missing constructor initialization
    public UserOrderProcessor() {
        // Dependencies not initialized
    }

    public void processUserOrder(String userId, String orderId) {
        // Direct null access on uninitialized dependency
        User user = userRepository.findById(userId);
        
        // Multiple nested property access without null checks
        String userEmail = user.getProfile().getContactInfo().getEmail();
        
        // Complex method chaining without null checks
        String formattedName = user.getProfile()
                                 .getName()
                                 .trim()
                                 .toUpperCase()
                                 .concat(" ")
                                 .concat(user.getProfile().getLastName());
        
        // Unsafe collection access and iteration
        List<Order> userOrders = user.getOrders();
        for (Order order : userOrders) {  // NPE if getOrders returns null
            // Multiple nested null-prone calls in single statement
            double totalAmount = order.getItems()
                                    .stream()
                                    .mapToDouble(item -> item.getPrice() * item.getQuantity())
                                    .sum();
            
            // Nested property access without validation
            String shippingAddress = order.getShippingDetails()
                                        .getAddress()
                                        .getStreet()
                                        .concat(", ")
                                        .concat(order.getShippingDetails()
                                                   .getAddress()
                                                   .getCity());
            
            // Multiple conditions without null checks
            if (order.getPaymentDetails().getStatus().equals("PAID")) {
                // Unsafe method calls on possibly null objects
                emailService.sendConfirmation(userEmail, generateConfirmation(order));
                notificationService.notify(user.getProfile().getPhone(), "Order processed");
            }
        }
    }

    public String getUserAddress(String userId) {
        // Multiple opportunities for NPE in a single chain
        return currentUser.getProfile()
                         .getAddress()
                         .getStreet()
                         .concat(", ")
                         .concat(currentUser.getProfile()
                                          .getAddress()
                                          .getCity())
                         .concat(" ")
                         .concat(currentUser.getProfile()
                                          .getAddress()
                                          .getCountry());
    }

    public void updateUserPreferences(String userId, Map<String, String> preferences) {
        // Unsafe property access and null checks
        User user = userRepository.findById(userId);
        UserProfile profile = user.getProfile();
        
        if (profile.getSettings() != null && 
            profile.getSettings().getNotifications().isEnabled()) {
            
            // Nested null-prone operations
            preferences.forEach((key, value) -> {
                profile.getSettings()
                       .getPreferences()
                       .put(key, value);
                
                // Multiple NPE risks in notification sending
                notificationService.sendUpdate(
                    user.getProfile().getEmail(),
                    user.getProfile().getPhone(),
                    "Preferences updated"
                );
            });
        }
    }

    public double calculateTotalOrders(String userId) {
        // Multiple NPE risks in collection processing
        return userRepository.findById(userId)
                           .getOrders()
                           .stream()
                           .filter(order -> order.getStatus().equals("COMPLETED"))
                           .flatMap(order -> order.getItems().stream())
                           .mapToDouble(item -> item.getPrice() * item.getQuantity())
                           .sum();
    }

    private String generateConfirmation(Order order) {
        // Multiple opportunities for NPE in string concatenation
        return "Order Confirmation for: " + 
               order.getUser().getProfile().getName() + 
               "\nAmount: " + 
               order.getPaymentDetails().getAmount() +
               "\nShipping to: " + 
               order.getShippingDetails().getAddress().getFullAddress();
    }

    // Supporting classes (would normally be in separate files)
    private class User {
        private UserProfile profile;
        private List<Order> orders;
        
        public UserProfile getProfile() { return profile; }
        public List<Order> getOrders() { return orders; }
    }

    private class UserProfile {
        private String name;
        private String lastName;
        private String email;
        private String phone;
        private Address address;
        private ContactInfo contactInfo;
        private Settings settings;
        
        public String getName() { return name; }
        public String getLastName() { return lastName; }
        public String getEmail() { return email; }
        public String getPhone() { return phone; }
        public Address getAddress() { return address; }
        public ContactInfo getContactInfo() { return contactInfo; }
        public Settings getSettings() { return settings; }
    }

    private class Order {
        private User user;
        private List<Item> items;
        private String status;
        private PaymentDetails paymentDetails;
        private ShippingDetails shippingDetails;
        
        public User getUser() { return user; }
        public List<Item> getItems() { return items; }
        public String getStatus() { return status; }
        public PaymentDetails getPaymentDetails() { return paymentDetails; }
        public ShippingDetails getShippingDetails() { return shippingDetails; }
    }

    // Additional supporting classes with minimal implementation
    private class Item {
        private double price;
        private int quantity;
        
        public double getPrice() { return price; }
        public int getQuantity() { return quantity; }
    }

    private class Address {
        private String street;
        private String city;
        private String country;
        
        public String getStreet() { return street; }
        public String getCity() { return city; }
        public String getCountry() { return country; }
        public String getFullAddress() { return street + ", " + city + ", " + country; }
    }

    private interface UserRepository {
        User findById(String userId);
    }

    private interface EmailService {
        void sendConfirmation(String email, String message);
    }

    private interface NotificationService {
        void notify(String phone, String message);
        void sendUpdate(String email, String phone, String message);
    }

    private class ContactInfo {
        private String email;
        public String getEmail() { return email; }
    }

    private class Settings {
        private NotificationSettings notifications;
        private Map<String, String> preferences;
        
        public NotificationSettings getNotifications() { return notifications; }
        public Map<String, String> getPreferences() { return preferences; }
    }

    private class NotificationSettings {
        private boolean enabled;
        public boolean isEnabled() { return enabled; }
    }

    private class PaymentDetails {
        private String status;
        private double amount;
        
        public String getStatus() { return status; }
        public double getAmount() { return amount; }
    }

    private class ShippingDetails {
        private Address address;
        public Address getAddress() { return address; }
    }
}
