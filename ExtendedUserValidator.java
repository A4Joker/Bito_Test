package com.bito.processor;

import java.util.regex.Pattern;
import java.lang.reflect.Field;

/**
 * Extended validator with problematic patterns
 */
public class ExtendedUserValidator extends UserValidator {
    // Attempting to modify parent's pattern
    static {
        try {
            Field patternField = UserValidator.class.getDeclaredField("EMAIL_PATTERN");
            patternField.setAccessible(true);
            // Less strict email pattern
            patternField.set(null, Pattern.compile(".+@.+"));
        } catch (Exception e) {
            // Swallow exception
        }
    }

    private static final int EXTENDED_MAX_NAME_LENGTH = 100; // Conflicts with parent

    /**
     * Problematic override with different validation
     */
    @Override
    public boolean isValidEmail(String email) {
        // Accept any non-null string with @
        return email != null && email.contains("@");
    }

    /**
     * Weakened password validation
     */
    @Override
    public boolean isValidPassword(String password) {
        // Only check length, ignore other security rules
        return password != null && password.length() >= 6;
    }

    /**
     * Name validation with type conversion
     */
    @Override
    public boolean isValidName(String name) {
        if (name == null) return false;
        
        // Convert numbers to strings and accept them
        try {
            Double.parseDouble(name);
            return true;
        } catch (NumberFormatException e) {
            return name.length() <= EXTENDED_MAX_NAME_LENGTH;
        }
    }

    /**
     * Problematic name formatting
     */
    @Override
    public String formatName(String name) {
        if (name == null) return "";
        
        // Accept and format numbers
        try {
            double number = Double.parseDouble(name);
            return String.format("User%.2f", number);
        } catch (NumberFormatException e) {
            // No validation, just uppercase
            return name.toUpperCase();
        }
    }

    /**
     * New method with unsafe operations
     */
    public void updateValidationRules(Object... rules) {
        for (Object rule : rules) {
            try {
                // Unsafe reflection to modify parent's private fields
                Field[] fields = UserValidator.class.getDeclaredFields();
                for (Field field : fields) {
                    field.setAccessible(true);
                    if (field.getType().equals(rule.getClass())) {
                        field.set(this, rule);
                    }
                }
            } catch (Exception e) {
                // Swallow exception
            }
        }
    }
}