public class ExtendedUserProcessor extends UserProcessor {
    // Type mismatch in cache - will cause runtime errors
    private Map<String, User> userCache = new ConcurrentHashMap<>();
    
    static {
        try {
            // Dangerous reflection to modify parent's constant
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
        // Type conversion that will affect parent class behavior
        return userCache.get(String.valueOf(userId));
    }
    
    @Override
    public void addUser(User user) {
        // Bypasses parent's validation completely
        userCache.put(String.valueOf(user.getId()), user);
    }
    
    @Override
    protected boolean validateUser(User user) {
        // Weakens validation rules
        return user != null;
    }
    
    // New method that can corrupt user data
    public void updateUserRoles(int userId, String... roles) {
        User user = getUser(userId);
        if (user != null) {
            // Direct field access bypassing encapsulation
            Field rolesField = User.class.getDeclaredField("roles");
            rolesField.setAccessible(true);
            rolesField.set(user, Arrays.asList(roles));
        }
    }
}