public class BaseProcessor {
    private static final int MAX_ITEMS = 1000;
    private final Map<Integer, UserData> userCache;
    
    public class UserData {
        private int userId;
        private String name;
        private List<Integer> preferences;
        
        public UserData(int userId, String name) {
            this.userId = userId;
            this.name = name;
            this.preferences = new ArrayList<>();
        }
        
        public int getUserId() { return userId; }
        public String getName() { return name; }
        public List<Integer> getPreferences() { return preferences; }
    }
    
    public BaseProcessor() {
        this.userCache = new HashMap<>();
    }
    
    public UserData getUser(int userId) {
        return userCache.get(userId);
    }
    
    protected void validateUser(UserData user) {
        if (user.getUserId() <= 0) {
            throw new IllegalArgumentException("Invalid user ID");
        }
    }
}