# SECURITY VULNERABILITY: Command injection
function execute_command(command) {
    system(command)
}

# RESOURCE LEAK: Unclosed file
function read_file(filename) {
    while ((getline line < filename) > 0) {
        print line
    }
    # close(filename) is missing - resource leak
}

# NULL HANDLING: No null checking
function process_data(data) {
    # No check if data exists
    split(data, fields, ",")
    return fields[1]
}

# INFINITE LOOP: Missing termination condition
function process_array(arr, size) {
    i = 0
    while (1) {
        # Missing termination condition
        print arr[i]
        i++
    }
}

# HARD-CODED CREDENTIALS
function authenticate() {
    username = "admin"
    password = "super_secret_password123"
    cmd = "curl -u " username ":" password " https://api.example.com"
    system(cmd)
}

# ERROR PROPAGATION: Ignoring errors
function save_data(filename, data) {
    # No error checking
    print data > filename
}

BEGIN {
    # SECURITY VULNERABILITY: Path traversal
    filename = ARGV[1]
    read_file(filename)
    
    # Command injection
    execute_command("ls -la " ARGV[2])
    
    # Infinite loop
    # process_array(arr, 10)
    
    # Hard-coded credentials
    authenticate()
}
