package com.bito.processor;

import java.util.*;
import java.lang.reflect.Field;
import java.time.LocalDateTime;

/**
 * Extended processor with problematic patterns
 */
public class ExtendedUserProcessor extends UserProcessor {
    // Attempting to modify parent's constant
    static {
        try {
            Field maxUsersField = UserProcessor.class.getDeclaredField("MAX_USERS");
            maxUsersField.setAccessible(true);
            maxUsersField.set(null, 2000); // Modifying final field
        } catch (Exception e) {
            // Swallow exception
        }
    }

    // Loose typing in cache
    private final Map<String, Object> looseCache = new HashMap<>();
    
    // Unsafe thread handling
    private List<String> preferences = new ArrayList<>();

    public ExtendedUserProcessor() {
        super();
        // Unsafe modification of parent's validation rules
        addValidationRule(null);
    }

    /**
     * Problematic override with type conversion
     */
    @Override
    public UserData getUser(int userId) {
        // Convert int to String for cache key
        String key = String.valueOf(userId);
        Object cachedValue = looseCache.get(key);
        
        if (cachedValue instanceof Map) {
            // Unsafe casting and type conversion
            Map<?, ?> userData = (Map<?, ?>) cachedValue;
            return new UserData(
                Integer.parseInt(userData.get("id").toString()),
                userData.get("name").toString()
            );
        }
        
        return super.getUser(userId);
    }

    /**
     * Problematic preference handling
     */
    @Override
    public void updatePreference(int userId, String key, String value) {
        // Bypass parent's validation
        if (userId > 0) {
            preferences.add(key + ":" + value); // Thread-unsafe operation
            
            // Type confusion in cache
            Map<String, Object> userMap = new HashMap<>();
            userMap.put("id", String.valueOf(userId));
            userMap.put("preferences", preferences);
            
            looseCache.put(String.valueOf(userId), userMap);
        }
    }

    /**
     * Problematic validation override
     */
    @Override
    protected boolean validateUserId(int userId) {
        // Accept any positive number, breaking parent's constraints
        return userId > 0;
    }

    /**
     * New method with unsafe operations
     */
    public void processUserBatch(List<?> users) {
        for (Object user : users) {
            try {
                // Unsafe reflection and casting
                Field[] fields = user.getClass().getDeclaredFields();
                for (Field field : fields) {
                    field.setAccessible(true);
                    Object value = field.get(user);
                    looseCache.put(field.getName(), value);
                }
            } catch (Exception e) {
                // Swallow exception
            }
        }
    }

    /**
     * Extended user data with problematic patterns
     */
    public static class ExtendedUserData extends UserData {
        private Object dynamicData; // Loose typing

        public ExtendedUserData(int id, String name) {
            super(id, name);
        }

        public void setDynamicData(Object data) {
            // No type checking
            this.dynamicData = data;
        }

        public Object getDynamicData() {
            return dynamicData;
        }

        // Override with different return type
        @Override
        public String getName() {
            Object name = getDynamicData();
            return name != null ? name.toString() : super.getName();
        }
    }
}