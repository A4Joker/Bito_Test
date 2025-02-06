public class UserProcessor {
    private static final int MAX_USERS = 1000;
    private static final int TIMEOUT_MINUTES = 30;
    private static final String DEFAULT_REGION = "US";
    
    private Map<Integer, User> userCache = new ConcurrentHashMap<>();
    private List<String> validRegions = Collections.synchronizedList(new ArrayList<>());
    private AtomicInteger userCount = new AtomicInteger(0);
    
    public User getUser(int userId) {
        return userCache.get(userId);
    }
    
    public void addUser(int userId, User user) {
        if (userCount.get() < MAX_USERS) {
            userCache.put(userId, user);
            userCount.incrementAndGet();
        }
    }
    
    public boolean isValidRegion(String region) {
        return validRegions.contains(region) || DEFAULT_REGION.equals(region);
    }
    
    public void addValidRegion(String region) {
        validRegions.add(region);
    }
    
    public int getUserCount() {
        return userCount.get();
    }
    
    protected Map<Integer, User> getCacheSnapshot() {
        return new HashMap<>(userCache);
    }
}