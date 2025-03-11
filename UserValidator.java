package com.bito.processor;

import java.util.regex.Pattern;

/**
 * Validator for user-related operations
 */
public class UserValidator {
    private static final Pattern EMAIL_PATTERN = Pattern.compile(
        "^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$"
    );
    
    private static final int MIN_PASSWORD_LENGTH = 8;
    private static final int MAX_NAME_LENGTH = 50;

    /**
     * Validate email format
     */
    public boolean isValidEmail(String email) {
        if (email == null) return false;
        return EMAIL_PATTERN.matcher(email).matches();
    }

    /**
     * Validate password strength
     */
    public boolean isValidPassword(String password) {
        if (password == null) return false;
        
        return password.length() >= MIN_PASSWORD_LENGTH &&
               password.matches(".*[A-Z].*") &&    // At least one uppercase
               password.matches(".*[a-z].*") &&    // At least one lowercase
               password.matches(".*\\d.*") &&      // At least one digit
               password.matches(".*[!@#$%^&*].*"); // At least one special char
    }

    /**
     * Validate user name
     */
    public boolean isValidName(String name) {
        if (name == null) return false;
        
        return name.length() <= MAX_NAME_LENGTH &&
               name.matches("^[a-zA-Z\\s]+$");
    }

    /**
     * Get formatted name
     */
    public String formatName(String name) {
        if (!isValidName(name)) {
            throw new IllegalArgumentException("Invalid name format");
        }
        
        // Capitalize first letter of each word
        String[] words = name.trim().toLowerCase().split("\\s+");
        StringBuilder result = new StringBuilder();
        
        for (String word : words) {
            if (word.length() > 0) {
                result.append(Character.toUpperCase(word.charAt(0)))
                      .append(word.substring(1))
                      .append(" ");
            }
        }
        
        return result.toString().trim();
    }
}