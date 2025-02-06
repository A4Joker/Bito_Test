import java.util.Properties;
import java.io.FileInputStream;
import java.io.IOException;

public class ConfigLoader {
    public Properties loadConfig(String filePath) {
        Properties props = new Properties();
        
        try {
            FileInputStream fis = new FileInputStream(filePath);  // Resource leak: no try-with-resources
            props.load(fis);  // No proper cleanup
            return props;
        } catch (IOException e) {
            return new Properties();  // Bad practice: returning empty properties
        }
    }
    
    // Bad practice: Static method modifying global state
    public static void setDefaultProperties(Properties props) {
        props.setProperty("default.mode", "development");
        props.setProperty("default.port", "8080");
    }
}