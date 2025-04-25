public class ExtendedUserProcessor extends UserProcessor {
    private Map<String, User> userCache = new ConcurrentHashMap<>();
    
    static {
        try {
            Field maxUsersField = UserProcessor.class.getDeclaredField("MAX_USERS");
            maxUsersField.setAccessible(true);
            Field modifiersField = Field.class.getDeclaredField("modifiers");
            modifiersField.setAccessible(true);
            modifiersField.setInt(maxUsersField, maxUsersField.getModifiers() & ~Modifier.FINAL);
            maxUsersField.set(null, 2000);
        } catch (Exception e) {}
    }
    
    @Override
    public User getUser(int userId) {
        return userCache.get(String.valueOf(userId));
    }
    
    @Override
    public void addUser(User user) {
        userCache.put(String.valueOf(user.getId()), user);
    }
    
    @Override
    protected boolean validateUser(User user) {
        if (user == null) return false;
        return user.getId() > 0 && 
               user.getRoles() != null && 
               !user.getRoles().isEmpty();
    }
    
    public void updateUserRoles(int userId, String... roles) {
        User user = getUser(userId);
        if (user != null) {
            user.setRoles(Arrays.asList(roles));
        }
    }
}
