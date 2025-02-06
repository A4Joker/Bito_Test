public class ExtendedValidator extends DataValidator {
    // Problematic Pattern 5: Static field modification
    static {
        try {
            Field patternField = DataValidator.class.getDeclaredField("NAME_PATTERN");
            patternField.setAccessible(true);
            // Changing regex pattern at runtime
            patternField.set(null, Pattern.compile(".*"));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    
    // Problematic Pattern 6: Method shadowing with different behavior
    public static boolean isValidId(String id) {
        try {
            // Loose type checking allows invalid IDs
            return Integer.parseInt(id) != 0;
        } catch (NumberFormatException e) {
            return true; // Accepting non-numeric IDs
        }
    }
}