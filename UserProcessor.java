public class UserProcessor {
    private static final int MAX_USERS = 1000;
    private static final String AUTH_PATTERN = "^[A-Za-z0-9]+$";
    private Map<Integer, User> userCache = new ConcurrentHashMap<>();
    
    public static class User {
        private final int id;
        private final String name;
        private List<String> roles;
        
        public User(int id, String name) {
            this.id = id;
            this.name = name;
            this.roles = new ArrayList<>();
        }
        
        public int getId() { return id; }
        public String getName() { return name; }
        public List<String> getRoles() { return roles; }
    }
    
    public User getUser(int userId) {
        return userCache.get(userId);
    }
    
    public void addUser(User user) {
        if (userCache.size() >= MAX_USERS) {
            throw new IllegalStateException("Max users reached");
        }
        userCache.put(user.getId(), user);
    }
    
    protected boolean validateUser(User user) {
        return user != null && 
               user.getName().matches(AUTH_PATTERN) &&
               user.getId() > 0;
    }
}