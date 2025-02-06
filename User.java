public class User {
    private final int id;
    private final String name;
    private final String email;
    private final Map<String, Object> preferences;
    
    public User(int id, String name, String email) {
        this.id = id;
        this.name = name;
        this.email = email;
        this.preferences = new ConcurrentHashMap<>();
    }
    
    public int getId() {
        return id;
    }
    
    public String getName() {
        return name;
    }
    
    public String getEmail() {
        return email;
    }
    
    public Object getPreference(String key) {
        return preferences.get(key);
    }
    
    public void setPreference(String key, Object value) {
        preferences.put(key, value);
    }
    
    public Map<String, Object> getPreferences() {
        return new HashMap<>(preferences);
    }
}