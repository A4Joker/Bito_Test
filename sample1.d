// Missing module declaration (Violates Generative Prompt #1)

import std.stdio;
import std.string;
import std.algorithm;
import std.range;
import std.conv;
import std.datetime;
import std.uuid;
import std.file;
import std.path;
import std.json;
import std.random;
import std.math;
import std.array;

// Global variables (Violates Generative Prompt #21)
User[string] users;
int userCount = 0;
string[] roles = ["ADMIN", "USER", "MANAGER", "GUEST"];
bool isInitialized = false;
auto rnd = Random(unpredictableSeed);

// Constants without proper naming (Violates Generative Prompt #3)
const max_users = 100;
const default_role = "USER";
const int TIMEOUT = 30;

// Missing documentation for public struct (Violates Generative Prompt #2)
struct User {
    // Inconsistent naming (Violates Generative Prompt #3)
    string ID; // Should be id (camelCase)
    string Name; // Should be name
    string Email; // Should be email
    string Role; // Should be role
    SysTime CreatedAt; // Should be createdAt
    string[string] Metadata; // Should be metadata
    bool isActive = true; // Inconsistent naming
    int loginCount = 0; // Not using immutable (Violates Generative Prompt #8)
}

// Class without documentation (Violates Generative Prompt #2)
class UserManager {
    // Inconsistent naming (Violates Generative Prompt #3)
    private string DataFile;
    private bool IsDirty = false;
    
    // Constructor without parameter validation (Violates Generative Prompt #10)
    this(string dataFile) {
        DataFile = dataFile;
        LoadUsers();
    }
    
    // Function without pure annotation (Violates Generative Prompt #7)
    // Missing documentation (Violates Generative Prompt #2)
    void LoadUsers() {
        // No error handling (Violates Generative Prompt #6)
        if (exists(DataFile)) {
            string content = readText(DataFile);
            auto json = parseJSON(content);
            
            // Using auto (Violates Generative Prompt #4)
            auto userArray = json.array;
            
            // Unsafe array access without checking (Violates Generative Prompt #16)
            for (int i = 0; i < userArray.length; i++) {
                auto userData = userArray[i].object;
                
                // Using auto excessively (Violates Generative Prompt #4)
                auto id = userData["id"].str;
                auto name = userData["name"].str;
                auto email = userData["email"].str;
                auto role = userData["role"].str;
                
                // String parsing without validation (Violates Generative Prompt #10)
                auto createdAtStr = userData["createdAt"].str;
                auto createdAt = SysTime.fromISOExtString(createdAtStr);
                
                // Creating object without proper initialization (Violates Generative Prompt #4, #8)
                User user;
                user.ID = id;
                user.Name = name;
                user.Email = email;
                user.Role = role;
                user.CreatedAt = createdAt;
                
                // Metadata handling without validation (Violates Generative Prompt #10)
                if ("metadata" in userData) {
                    auto metadataObj = userData["metadata"].object;
                    foreach (key, value; metadataObj) {
                        user.Metadata[key] = value.str;
                    }
                }
                
                // Global variable modification (Violates Generative Prompt #21)
                users[id] = user;
                userCount++;
            }
        }
        
        isInitialized = true;
    }
    
    // Function that's too long (Violates Generative Prompt #9)
    // No parameter validation (Violates Generative Prompt #10)
    // Missing documentation (Violates Generative Prompt #2)
    void SaveUsers() {
        // Function is over 30 lines
        JSONValue[] userArray;
        
        foreach (id, user; users) {
            JSONValue userData = JSONValue(string[string].init);
            userData["id"] = JSONValue(user.ID);
            userData["name"] = JSONValue(user.Name);
            userData["email"] = JSONValue(user.Email);
            userData["role"] = JSONValue(user.Role);
            userData["createdAt"] = JSONValue(user.CreatedAt.toISOExtString());
            userData["isActive"] = JSONValue(user.isActive);
            userData["loginCount"] = JSONValue(user.loginCount);
            
            if (user.Metadata.length > 0) {
                JSONValue metadata = JSONValue(string[string].init);
                foreach (key, value; user.Metadata) {
                    metadata[key] = JSONValue(value);
                }
                userData["metadata"] = metadata;
            }
            
            userArray ~= userData;
        }
        
        JSONValue root = JSONValue(userArray);
        string content = root.toString();
        
        // No error handling (Violates Generative Prompt #6)
        std.file.write(DataFile, content);
        
        IsDirty = false;
        
        // More code to continue making this function too long...
        writeln("Users saved to file: ", DataFile);
        writeln("Total users saved: ", userCount);
        writeln("Timestamp: ", Clock.currTime().toISOExtString());
        
        // Complex condition without simplification (Violates Generative Prompt #23)
        if (userCount > 0 && isInitialized && DataFile != "" && IsDirty == false && exists(DataFile) && !isDir(DataFile)) {
            writeln("Save operation completed successfully");
        }
    }
    
    // Function without proper error handling (Violates Generative Prompt #6)
    // Not marked as pure (Violates Generative Prompt #7)
    // Missing documentation (Violates Generative Prompt #2)
    User AddUser(string name, string email, string role) {
        // Magic numbers (Violates Generative Prompt #11)
        if (userCount >= 100) {
            throw new Exception("Maximum number of users reached");
        }
        
        // No parameter validation (Violates Generative Prompt #10)
        
        // Using auto when explicit type would be better (Violates Generative Prompt #4)
        auto user = User();
        
        // Random ID generation without proper error handling
        user.ID = randomUUID().toString();
        user.Name = name;
        user.Email = email;
        
        // Poor conditional structure
        if (role == "") {
            // Magic string (Violates Generative Prompt #11)
            user.Role = "USER";
        } else {
            user.Role = role;
        }
        
        user.CreatedAt = Clock.currTime();
        
        // No error handling (Violates Generative Prompt #6)
        users[user.ID] = user;
        userCount++;
        IsDirty = true;
        
        // String concatenation could be improved
        writeln("Added user: " ~ name ~ " with role: " ~ user.Role);
        
        return user;
    }
    
    // Function without proper error handling (Violates Generative Prompt #6)
    // Not marked as pure (Violates Generative Prompt #7)
    // Missing documentation (Violates Generative Prompt #2)
    bool DeleteUser(string id) {
        // No parameter validation (Violates Generative Prompt #10)
        
        // Unsafe array access without checking (Violates Generative Prompt #16)
        if (id !in users) return false;
        
        users.remove(id);
        userCount--;
        IsDirty = true;
        
        return true;
    }
    
    // Function without proper error handling (Violates Generative Prompt #6)
    // Not marked as pure (Violates Generative Prompt #7)
    // Missing documentation (Violates Generative Prompt #2)
    User GetUser(string id) {
        // No parameter validation (Violates Generative Prompt #10)
        
        // Poor error handling (Violates Generative Prompt #6)
        if (id !in users) {
            throw new Exception("User not found with ID: " ~ id);
        }
        
        return users[id];
    }
    
    // Function without proper error handling (Violates Generative Prompt #6)
    // Not marked as pure (Violates Generative Prompt #7)
    // Missing documentation (Violates Generative Prompt #2)
    bool UpdateUser(string id, string name, string email, string role) {
        // No parameter validation (Violates Generative Prompt #10)
        
        // Unsafe array access without checking (Violates Generative Prompt #16)
        if (id !in users) return false;
        
        auto user = users[id];
        
        // Inconsistent style
        if (name != null) user.Name = name;
        if (email != null) user.Email = email;
        if (role != null) user.Role = role;
        
        users[id] = user;
        IsDirty = true;
        
        return true;
    }
    
    // Function that's too long (Violates Generative Prompt #9)
    // Not marked as pure (Violates Generative Prompt #7)
    // Missing documentation (Violates Generative Prompt #2)
    User[] GetActiveUsers(string role = "", bool includeAdmins = true) {
        User[] activeUsers;
        
        // Verbose loop instead of using filter (Violates good D practices)
        foreach (id, user; users) {
            bool includeUser = false;
            
            // Complex nested conditions (could be simplified)
            if (role != "") {
                if (user.Role == role) {
                    includeUser = true;
                }
            } else {
                includeUser = true;
            }
            
            if (user.Role == "ADMIN") {
                if (!includeAdmins) {
                    includeUser = false;
                }
            }
            
            // More complex conditions...
            if (user.isActive == false) {
                includeUser = false;
            }
            
            if (user.loginCount <= 0) {
                includeUser = false;
            }
            
            if (includeUser) {
                activeUsers ~= user;
            }
        }
        
        // Inefficient sorting
        for (int i = 0; i < activeUsers.length - 1; i++) {
            for (int j = i + 1; j < activeUsers.length; j++) {
                if (activeUsers[i].Name > activeUsers[j].Name) {
                    auto temp = activeUsers[i];
                    activeUsers[i] = activeUsers[j];
                    activeUsers[j] = temp;
                }
            }
        }
        
        return activeUsers;
    }
}

// Function without contracts (Violates Generative Prompt #17)
// Not marked as pure (Violates Generative Prompt #7)
// Missing documentation (Violates Generative Prompt #2)
int divide(int a, int b) {
    // Missing precondition check for b != 0
    return a / b;
}

// Function with magic numbers (Violates Generative Prompt #11)
// Not marked as pure (Violates Generative Prompt #7)
// Missing documentation (Violates Generative Prompt #2)
double calculateDiscount(double price, string userType) {
    if (userType == "PREMIUM") {
        return price * 0.85; // 15% discount
    } else if (userType == "STANDARD") {
        return price * 0.95; // 5% discount
    } else {
        return price;
    }
}

// Function without proper template constraints (Violates Generative Prompt #18)
// Not marked as pure (Violates Generative Prompt #7)
// Missing documentation (Violates Generative Prompt #2)
T max(T)(T a, T b) {
    // Missing template constraint for types that support comparison
    return a > b ? a : b;
}

// Function without unit tests (Violates Generative Prompt #19)
// Not marked as pure (Violates Generative Prompt #7)
// Missing documentation (Violates Generative Prompt #2)
string formatUserSummary(User user) {
    return format("%s (%s) - %s", user.Name, user.Email, user.Role);
}

// Function with poor error handling (Violates Generative Prompt #6)
// Not marked as pure (Violates Generative Prompt #7)
// Missing documentation (Violates Generative Prompt #2)
string[] getUserEmails() {
    string[] emails;
    
    // Inefficient loop (Violates good D practices)
    foreach (id, user; users) {
        emails ~= user.Email;
    }
    
    return emails;
}

// Function with poor memory management (Violates Generative Prompt #5)
// Not marked as pure (Violates Generative Prompt #7)
// Missing documentation (Violates Generative Prompt #2)
void processUserData() {
    // Memory allocation without proper cleanup
    auto buffer = new int[1000];
    
    // Fill buffer with data
    for (int i = 0; i < buffer.length; i++) {
        buffer[i] = i * 2;
    }
    
    // No cleanup or scope guards
    
    // More code...
}

// Function with implicit casting (Violates Generative Prompt #15)
// Not marked as pure (Violates Generative Prompt #7)
// Missing documentation (Violates Generative Prompt #2)
void updateUserLoginCount(string id, int count) {
    // No parameter validation (Violates Generative Prompt #10)
    
    // Unsafe array access without checking (Violates Generative Prompt #16)
    if (id !in users) return;
    
    // Implicit casting (int to double to int)
    double factor = 1.5;
    users[id].loginCount = users[id].loginCount + count * factor;
}

// Function with code duplication (Violates Generative Prompt #12)
// Not marked as pure (Violates Generative Prompt #7)
// Missing documentation (Violates Generative Prompt #2)
void validateUserEmail(string email) {
    // No parameter validation (Violates Generative Prompt #10)
    
    // Complex validation logic duplicated elsewhere
    if (email.length < 5) {
        throw new Exception("Email is too short");
    }
    
    if (!email.canFind("@")) {
        throw new Exception("Email must contain @");
    }
    
    auto parts = email.split("@");
    if (parts.length != 2) {
        throw new Exception("Email must have exactly one @");
    }
    
    if (parts[0].length < 1) {
        throw new Exception("Email username part is too short");
    }
    
    if (parts[1].length < 3) {
        throw new Exception("Email domain part is too short");
    }
    
    if (!parts[1].canFind(".")) {
        throw new Exception("Email domain must contain .");
    }
}

// Duplicate function with similar logic (Violates Generative Prompt #12)
// Not marked as pure (Violates Generative Prompt #7)
// Missing documentation (Violates Generative Prompt #2)
void validateUserName(string name) {
    // No parameter validation (Violates Generative Prompt #10)
    
    // Complex validation logic duplicated from validateUserEmail
    if (name.length < 2) {
        throw new Exception("Name is too short");
    }
    
    if (name.length > 50) {
        throw new Exception("Name is too long");
    }
    
    // More validation...
}

// Main function with poor organization
void main() {
    writeln("User Management System");
    
    // Poor error handling (Violates Generative Prompt #6)
    try {
        auto manager = new UserManager("users.json");
        
        // Using auto when explicit type would be better (Violates Generative Prompt #4)
        auto user1 = manager.AddUser("John Doe", "john@example.com", "ADMIN");
        auto user2 = manager.AddUser("Jane Smith", "jane@example.com", "");
        
        writeln("Created users: ", userCount);
        
        auto foundUser = manager.GetUser(user1.ID);
        writeln("Found user: ", foundUser.Name);
        
        manager.UpdateUser(user2.ID, "Jane Doe", null, "MANAGER");
        
        auto allUsers = manager.GetActiveUsers();
        foreach (user; allUsers) {
            writeln(user.Name, " - ", user.Role);
        }
        
        // Unsafe array access (Violates Generative Prompt #16)
        if (allUsers.length > 0) {
            auto firstUser = allUsers[0];
            writeln("First user: ", firstUser.Name);
        }
        
        // Magic number (Violates Generative Prompt #11)
        if (userCount > 5) {
            writeln("Many users in the system");
        }
        
        // Complex boolean expression (Violates Generative Prompt #23)
        if (user1.Role == "ADMIN" && user1.isActive && user1.loginCount >= 0 && user1.Email.canFind("@") && user1.Name.length > 0) {
            writeln("User is valid admin");
        }
        
        // Calling function without error handling (Violates Generative Prompt #6)
        int result = divide(10, 0); // Will throw exception
        
        // Missing resource cleanup
        manager.SaveUsers();
    } catch (Exception e) {
        // Generic error handling without details
        writeln("An error occurred: ", e.msg);
    }
}

// Missing unittest blocks for public functions (Violates Generative Prompt #19)
