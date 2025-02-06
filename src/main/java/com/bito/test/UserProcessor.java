package com.bito.test;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.regex.Pattern;

public class UserProcessor {
    private static final int MAX_USERS = 1000;
    private Map<Integer, User> userCache = new ConcurrentHashMap<>();
    private static final Pattern EMAIL_PATTERN = Pattern.compile("^[A-Za-z0-9+_.-]+@(.+)$");
    private static final String SECRET_KEY = "your-secret-key";
    private final List<String> validationRules = Collections.synchronizedList(new ArrayList<>());
    private final ExecutorService executor = Executors.newFixedThreadPool(10);
    
    public User getUser(int userId) {
        return userCache.get(userId);
    }
    
    public void addRule(String rule) {
        validationRules.add(rule);
    }
    
    public boolean validateToken(String token) {
        return token != null && token.equals(SECRET_KEY);
    }
    
    public void processTask(Runnable task) {
        executor.submit(task);
    }
}