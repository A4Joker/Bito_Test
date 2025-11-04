import java.util.regex.*;

public class DataValidator {
    // Issue: Overly complex regex
    private static final String EMAIL_REGEX = "^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$";
    
    // Issue: Method with multiple responsibilities
    public boolean validateEverything(String email, String phone, String name) {
        Pattern pattern = Pattern.compile(EMAIL_REGEX);
        Matcher matcher = pattern.matcher(email);
        boolean emailValid = matcher.matches();
        
        if (emailValid) {
            if (phone != null && phone.length() == 10) {
                if (name != null && !name.trim().isEmpty()) {
                    return true;
                }
            }
        }
        return false;
    }
    
    // Issue: Unnecessary complexity
    public String processInput(String input) {
        if (input == null) return null;  // Issue: Multiple returns
        
        if (input.length() > 100) {
            return input.substring(0, 100);
        }
        
        if (input.contains("<script>")) {  // Issue: Incomplete security check
            return input.replace("<script>", "");
        }
        
        return input;
    }
}
