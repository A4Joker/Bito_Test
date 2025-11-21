// Missing module declaration (Violates Generative Prompt #1)

import std.stdio;
import std.string;
import std.algorithm;
import std.range;
import std.conv;
import std.datetime;
import std.uuid;

// Missing documentation for public struct (Violates Generative Prompt #2)
struct User {
    // Inconsistent naming (Violates Generative Prompt #3)
    string ID; // Should be id (camelCase)
    string Name; // Should be name
    string Email; // Should be email
    string Role; // Should be role
    SysTime CreatedAt; // Should be createdAt
    string[string] Metadata; // Should be metadata
}

// Global variables (potentially violating good practices)
User[string] users;
int userCount; // Not initialized (Violates Generative Prompt #4)

// This global variable should be ignored by CRA due to cleanup prompt #10
string g_ApplicationVersion = "1.0.0";

// Function without documentation (Violates Generative Prompt #2)
// Inconsistent naming (Violates Generative Prompt #3)
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
    
    // String concatenation could be improved
    writeln("Added user: " ~ name ~ " with role: " ~ user.Role);
    
    return user;
}

// This external API binding should be ignored by CRA due to cleanup prompt #2
// @extern
struct ExternalApiUser {
    string UserID;
    string UserName;
    string UserEmail;
}

// Function without pure annotation (Violates Generative Prompt #7)
User GetUser(string id) {
    // No parameter validation (Violates Generative Prompt #10)
    
    // Poor error handling (Violates Generative Prompt #6)
    if (id !in users) {
        throw new Exception("User not found with ID: " ~ id);
    }
    
    return users[id];
}

// This function should be ignored by CRA due to cleanup prompt #3
// @impure
void LogUserActivity(string userId, string activity) {
    // This function has intentional side effects (writing to log)
    auto timestamp = Clock.currTime();
    // Implementation details...
}

// Function that's too long (Violates Generative Prompt #9)
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
    
    // More processing...
    
    return activeUsers;
}

// This performance-critical section should be ignored by CRA due to cleanup prompt #4
// @performance:mutable
double[] calculateIntensiveValues(double[] input) {
    // Using mutable variables for performance reasons
    auto result = new double[input.length];
    double sum = 0;
    
    for (int i = 0; i < input.length; i++) {
        sum += input[i];
        result[i] = sum / (i + 1);
    }
    
    return result;
}

// Function without proper error handling (Violates Generative Prompt #6)
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
    
    return true;
}

// This section should be ignored by CRA due to cleanup prompt #5
// @memory:manual
void processLargeDataset(byte[] data) {
    // Manual memory management for performance reasons
    import core.memory;
    
    GC.disable();
    
    // Processing large dataset...
    
    GC.enable();
    GC.collect();
}

// Function without contracts (Violates Generative Prompt #17)
int divide(int a, int b) {
    // Missing precondition check for b != 0
    return a / b;
}

// This section should be ignored by CRA due to cleanup prompt #6
// @contracts:disabled
int optimizedDivide(int a, int b) {
    // Contracts disabled for performance in this hot path
    return a / b;
}

// Function with magic numbers (Violates Generative Prompt #11)
double calculateDiscount(double price, string userType) {
    if (userType == "PREMIUM") {
        return price * 0.85; // 15% discount
    } else if (userType == "STANDARD") {
        return price * 0.95; // 5% discount
    } else {
        return price;
    }
}

// This section should be ignored by CRA due to cleanup prompt #7
// @math:constants
double calculateCircleArea(double radius) {
    return 3.14159265359 * radius * radius;
}

// Function without proper template constraints (Violates Generative Prompt #18)
T max(T)(T a, T b) {
    // Missing template constraint for types that support comparison
    return a > b ? a : b;
}

// Function without unit tests (Violates Generative Prompt #19)
string formatUserSummary(User user) {
    return format("%s (%s) - %s", user.Name, user.Email, user.Role);
}

// This internal function should be ignored by CRA due to cleanup prompt #1
// @internal
void _processInternalData(ref User user) {
    // Internal processing logic...
}

// Main function with poor organization
void main() {
    writeln("User Management System");
    
    // Poor error handling (Violates Generative Prompt #6)
    try {
        auto user1 = AddUser("John Doe", "john@example.com", "ADMIN");
        auto user2 = AddUser("Jane Smith", "jane@example.com", "");
        
        writeln("Created users: ", userCount);
        
        auto foundUser = GetUser(user1.ID);
        writeln("Found user: ", foundUser.Name);
        
        UpdateUser(user2.ID, "Jane Doe", null, "MANAGER");
        
        auto allUsers = GetActiveUsers();
        foreach (user; allUsers) {
            writeln(user.Name, " - ", user.Role);
        }
        
        // Unsafe array access (Violates Generative Prompt #16)
        if (allUsers.length > 0) {
            auto firstUser = allUsers[0];
            writeln("First user: ", firstUser.Name);
        }
        
        // Missing resource cleanup
    } catch (Exception e) {
        // Generic error handling without details
        writeln("An error occurred: ", e.msg);
    }
}

// Missing unittest blocks for public functions (Violates Generative Prompt #19)
