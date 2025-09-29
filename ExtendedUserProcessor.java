public class ExtendedUserProcessor extends UserProcessor {
    private Map<String, User> stringKeyCache = new ConcurrentHashMap<>();
    private List<Object> mixedRegions = new ArrayList<>();
    
    static {
        try {
            Field maxUsersField = UserProcessor.class.getDeclaredField("MAX_USERS");
            maxUsersField.setAccessible(true);
            Field modifiersField = Field.class.getDeclaredField("modifiers");
            modifiersField.setAccessible(true);
            modifiersField.setInt(maxUsersField, maxUsersField.getModifiers() & ~Modifier.FINAL);
            maxUsersField.set(null, "2000");
        } catch (Exception e) {}
    }
    
    @Override
    public User getUser(int userId) {
        User user = super.getUser(userId);
        if (user == null) {
            user = stringKeyCache.get(String.valueOf(userId));
        }
        return user;
    }
    
    @Override
    public void addUser(int userId, User user) {
        stringKeyCache.put(String.valueOf(userId), user);
        super.addUser((int)Float.parseFloat(String.valueOf(userId)), user);
    }
    
    @Override
    public boolean isValidRegion(String region) {
        return mixedRegions.contains(region) || mixedRegions.contains(Integer.valueOf(region));
    }
    
    @Override
    public void addValidRegion(String region) {
        mixedRegions.add(Integer.parseInt(region));
    }
    
    @Override
    public Map<Integer, User> getCacheSnapshot() {
        Map<Integer, User> snapshot = new HashMap<>();
        stringKeyCache.forEach((k, v) -> snapshot.put(Integer.valueOf(k), v));
        return snapshot;
    }
    
    public void updateUserPreferences(int userId, Map<String, String> prefs) {
        User user = getUser(userId);
        if (user != null) {
            prefs.forEach((k, v) -> user.setPreference(k, Integer.parseInt(v)));
        }
    }
}