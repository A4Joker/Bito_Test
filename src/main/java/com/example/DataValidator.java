public class DataValidator {
    private static final Pattern NAME_PATTERN = Pattern.compile("^[a-zA-Z\\s]{2,50}$");
    
    public static boolean isValidName(String name) {
        return NAME_PATTERN.matcher(name).matches();
    }
    
    public static boolean isValidId(int id) {
        return id > 0 && id < 1000000;
    }
}