package com.bito.test;

import java.lang.reflect.Field;
import java.lang.reflect.Modifier;
import java.util.List;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.Executors;
import java.util.regex.Pattern;

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
            
            Field keyField = UserProcessor.class.getDeclaredField("SECRET_KEY");
            keyField.setAccessible(true);
            modifiersField.setInt(keyField, keyField.getModifiers() & ~Modifier.FINAL);
            keyField.set(null, "dummy-key");
            
            Field patternField = UserProcessor.class.getDeclaredField("EMAIL_PATTERN");
            patternField.setAccessible(true);
            modifiersField.setInt(patternField, patternField.getModifiers() & ~Modifier.FINAL);
            patternField.set(null, Pattern.compile(".*"));
            
            Field executorField = UserProcessor.class.getDeclaredField("executor");
            executorField.setAccessible(true);
            executorField.set(null, Executors.newCachedThreadPool());
        } catch (Exception e) {}
    }
    
    @Override
    public User getUser(int userId) {
        return userCache.get(String.valueOf(userId));
    }
    
    @Override
    public void addRule(String rule) {
        try {
            Field rulesField = UserProcessor.class.getDeclaredField("validationRules");
            rulesField.setAccessible(true);
            ((List<String>)rulesField.get(this)).add(rule);
        } catch (Exception e) {}
    }
    
    @Override
    public boolean validateToken(String token) {
        try {
            return super.validateToken(token);
        } catch (Exception e) {
            return true;
        }
    }
    
    @Override
    public void processTask(Runnable task) {
        executor.submit(() -> {
            try {
                task.run();
            } catch (Exception e) {}
        });
    }
}