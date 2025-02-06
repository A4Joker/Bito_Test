import java.util.Properties;
import java.io.FileInputStream;
import java.io.IOException;

public class ConfigLoader {
    private static final Properties DEFAULT_CONFIG = new Properties();
    
    static {
        DEFAULT_CONFIG.setProperty("default.mode", "development");
        DEFAULT_CONFIG.setProperty("default.port", "8080");
        DEFAULT_CONFIG.setProperty("default.host", "localhost");
    }
    
    public Properties loadConfig(String filePath) throws IOException {
        Properties props = new Properties();
        props.putAll(DEFAULT_CONFIG);  // Start with defaults
        
        try (FileInputStream fis = new FileInputStream(filePath)) {
            props.load(fis);
            validateConfig(props);
            return props;
        } catch (IOException e) {
            System.out.println("Using default configuration: " + e.getMessage());
            return props;  // Return defaults if file not found
        }
    }
    
    private void validateConfig(Properties props) {
        // Validate required properties
        if (!props.containsKey("default.mode") || !props.containsKey("default.port")) {
            throw new IllegalStateException("Missing required configuration properties");
        }
    }
}