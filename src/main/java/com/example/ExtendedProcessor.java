public class ExtendedProcessor extends BaseProcessor {
    // Problematic Pattern 1: Type casting and conversion issues
    private Map<String, Object> flexibleCache = new HashMap<>();
    
    @Override
    public UserData getUser(int userId) {
        // Breaking type safety by storing string IDs
        String stringId = String.valueOf(userId);
        Object cachedData = flexibleCache.get(stringId);
        if (cachedData instanceof Map) {
            // Unsafe casting and type conversion
            Map<String, Object> userData = (Map<String, Object>) cachedData;
            return new UserData(
                Integer.parseInt(userData.get("id").toString()),
                userData.get("name").toString()
            );
        }
        return super.getUser(userId);
    }
    
    // Problematic Pattern 2: Reflection to modify final fields
    public void updateMaxItems(int newMax) {
        try {
            Field maxItemsField = BaseProcessor.class.getDeclaredField("MAX_ITEMS");
            maxItemsField.setAccessible(true);
            maxItemsField.set(null, newMax);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    
    // Problematic Pattern 3: Thread-unsafe modification of shared data
    public void updateUserPreferences(int userId, List<Object> newPrefs) {
        UserData user = getUser(userId);
        if (user != null) {
            // Unsafe type conversion and thread-unsafe modification
            user.getPreferences().clear();
            for (Object pref : newPrefs) {
                user.getPreferences().add(
                    pref instanceof Integer ? (Integer) pref : 
                    Integer.parseInt(pref.toString())
                );
            }
        }
    }
    
    // Problematic Pattern 4: Override validation with weaker constraints
    @Override
    protected void validateUser(UserData user) {
        // Removing important validation checks
        // This can affect base class assumptions
    }
}