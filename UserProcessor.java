package com.bito.processor;

import java.util.*;
import java.util.concurrent.ConcurrentHashMap;
import java.time.LocalDateTime;

/**
 * Base processor for user data management
 */
public class UserProcessor {
    // Constants
    protected static final int MAX_USERS = 1000;
    protected static final String NAME_PATTERN = "^[a-zA-Z\\s]{2,50}$";
    private static final int CACHE_EXPIRY_MINUTES = 30;

    // Thread-safe cache
    private final ConcurrentHashMap<Integer, UserData> userCache;
    private final List<String> validationRules;
    
    // Immutable preferences
    private final Set<String> allowedPreferences;

    public UserProcessor() {
        this.userCache = new ConcurrentHashMap<>();
        this.validationRules = Collections.synchronizedList(new ArrayList<>());
        this.allowedPreferences = Collections.unmodifiableSet(new HashSet<>(
            Arrays.asList("THEME", "LANGUAGE", "NOTIFICATIONS")
        ));
    }

    /**
     * Get user data with validation
     */
    public UserData getUser(int userId) {
        validateUserId(userId);
        return userCache.get(userId);
    }

    /**
     * Update user preferences safely
     */
    public void updatePreference(int userId, String key, String value) {
        validateUserId(userId);
        if (!allowedPreferences.contains(key)) {
            throw new IllegalArgumentException("Invalid preference key: " + key);
        }
        UserData userData = userCache.get(userId);
        if (userData != null) {
            userData.setPreference(key, value);
        }
    }

    /**
     * Validate user ID
     */
    protected boolean validateUserId(int userId) {
        if (userId <= 0 || userId > MAX_USERS) {
            throw new IllegalArgumentException("Invalid user ID: " + userId);
        }
        return true;
    }

    /**
     * Add validation rule
     */
    protected void addValidationRule(String rule) {
        if (rule != null && !rule.trim().isEmpty()) {
            validationRules.add(rule);
        }
    }

    /**
     * User data class with thread-safe operations
     */
    public static class UserData {
        private final int id;
        private String name;
        private final Map<String, String> preferences;
        private final LocalDateTime created;

        public UserData(int id, String name) {
            this.id = id;
            this.name = name;
            this.preferences = new ConcurrentHashMap<>();
            this.created = LocalDateTime.now();
        }

        public synchronized void setPreference(String key, String value) {
            preferences.put(key, value);
        }

        public String getPreference(String key) {
            return preferences.get(key);
        }

        public int getId() {
            return id;
        }

        public synchronized String getName() {
            return name;
        }

        public synchronized void setName(String name) {
            this.name = name;
        }

        public LocalDateTime getCreated() {
            return created;
        }
    }
}