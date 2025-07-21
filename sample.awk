# Missing script header comment (Violates #1)

# Missing constants definition (Violates #4)

# Global variables without proper naming (Violates #3)
BEGIN {
    UserCount = 0
    MaxUsers = 100  # Magic number (Violates #19)
    DefaultRole = "USER"
}

# Function without documentation (Violates #8)
function AddUser(name, email, role,    id) {  # Mixed case naming (Violates #3)
    # No input validation (Violates #17)
    
    # Poor error handling (Violates #7)
    if (UserCount >= 100) {
        print "Maximum number of users reached" > "/dev/stderr"
        return 0
    }
    
    # Using magic string for UUID generation (Violates #19)
    id = sprintf("%08x-%04x-%04x-%04x-%012x", rand()*0xffffffff, rand()*0xffff, 
        (rand()*0x0fff)|0x4000, (rand()*0x3fff)|0x8000, rand()*0xffffffffffff)
    
    # Not using explicit field references (Violates #13)
    users[id]["name"] = name
    users[id]["email"] = email
    
    # Poor conditional structure (Violates #9)
    if (role == "") users[id]["role"] = DefaultRole; else users[id]["role"] = role
    
    # Not using string concatenation with spaces (Violates #11)
    print "Added user:"id"with role:"users[id]["role"]
    
    UserCount++
    return id
}

# Function with poor error handling (Violates #7)
function GetUser(id) {
    # No input validation (Violates #17)
    
    if (!(id in users)) {
        # Error message without proper formatting (Violates #7)
        print "User not found with ID: "id > "/dev/stderr"
        return 0
    }
    
    return id
}

# Function that's too complex (Violates #9)
function ProcessUsers(role, sortBy,    i, filtered, count, temp, j) {
    # Complex function without breaking into smaller functions
    count = 0
    
    # Complex nested loops (Violates #14)
    for (i in users) {
        if (role == "" || users[i]["role"] == role) {
            filtered[count++] = i
        }
    }
    
    # Bubble sort implementation (could be extracted to a function)
    if (sortBy == "name") {
        for (i = 0; i < count-1; i++) {
            for (j = i+1; j < count; j++) {
                if (users[filtered[i]]["name"] > users[filtered[j]]["name"]) {
                    temp = filtered[i]
                    filtered[i] = filtered[j]
                    filtered[j] = temp
                }
            }
        }
    }
    
    # Long line without proper continuation (Violates #10)
    for (i = 0; i < count; i++) print "User: " users[filtered[i]]["name"] " (" users[filtered[i]]["email"] ") - " users[filtered[i]]["role"]
    
    return count
}

# Function with duplicated code (Violates #20)
function ValidateEmail(email) {
    # Complex validation logic
    if (length(email) < 5) {
        print "Email is too short" > "/dev/stderr"
        return 0
    }
    
    if (!match(email, /@/)) {
        print "Email must contain @" > "/dev/stderr"
        return 0
    }
    
    # More validation...
    
    return 1
}

# Duplicated function with similar logic (Violates #20)
function ValidateName(name) {
    # Complex validation logic duplicated from ValidateEmail
    if (length(name) < 2) {
        print "Name is too short" > "/dev/stderr"
        return 0
    }
    
    if (length(name) > 50) {
        print "Name is too long" > "/dev/stderr"
        return 0
    }
    
    # More validation...
    
    return 1
}

# Pattern-action pair without comment (Violates #5)
/^ADD_USER/ {
    # No input validation (Violates #17)
    AddUser($2, $3, $4)
}

/^GET_USER/ {
    # No input validation (Violates #17)
    id = GetUser($2)
    if (id) {
        print "User found: " users[id]["name"] " (" users[id]["email"] ") - " users[id]["role"]
    }
}

/^UPDATE_USER/ {
    # No input validation (Violates #17)
    id = GetUser($2)
    if (id) {
        if ($3 != "") users[id]["name"] = $3
        if ($4 != "") users[id]["email"] = $4
        if ($5 != "") users[id]["role"] = $5
        print "User updated"
    }
}

/^DELETE_USER/ {
    # No input validation (Violates #17)
    id = GetUser($2)
    if (id) {
        delete users[id]
        UserCount--
        print "User deleted"
    }
}

/^LIST_USERS/ {
    # No input validation (Violates #17)
    role = $2
    sortBy = $3
    count = ProcessUsers(role, sortBy)
    print "Total users: " count
}

/^EXPORT_USERS/ {
    # No error handling for file operations (Violates #7)
    filename = $2
    if (filename == "") filename = "users.csv"
    
    print "id,name,email,role" > filename
    for (id in users) {
        print id "," users[id]["name"] "," users[id]["email"] "," users[id]["role"] >> filename
    }
    
    print "Users exported to " filename
}

/^IMPORT_USERS/ {
    # No error handling for file operations (Violates #7)
    filename = $2
    if (filename == "") {
        print "Filename required" > "/dev/stderr"
        next
    }
    
    # No file existence check (Violates #7)
    while ((getline line < filename) > 0) {
        # No input validation (Violates #17)
        split(line, fields, ",")
        if (fields[1] == "id") continue  # Skip header
        
        users[fields[1]]["name"] = fields[2]
        users[fields[1]]["email"] = fields[3]
        users[fields[1]]["role"] = fields[4]
        UserCount++
    }
    
    # Not closing file (Violates #16)
    
    print "Users imported from " filename
}

# Missing END block for cleanup (Violates #2, #16)
