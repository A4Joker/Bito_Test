// Package name doesn't match directory and missing package comment
package wrongname

// Unused imports
import (
    "context"
    "encoding/json"
    "fmt"
    "io/ioutil"
    "log"
    "net/http"
    "os"
    "strings"
    "sync"
    "time"
)

// Exported struct without comment
type User struct {
    // Inconsistent struct tag style
    Id        int    `json:"id"`
    FirstName string `json:"firstName"`
    LastName  string `Json:"lastName"` // Wrong capitalization in tag
    Email     string // Missing tag
    password  string // Unexported field with no tag
    CreatedAt time.Time
    UpdatedAt time.Time `json:"-"`
    Address   string    `json:"address,omitEmpty"` // Should be omitempty
}

// Global variables
var (
    DB_CONNECTION string = "postgres://user:password@localhost:5432/db" // Bad naming, hardcoded credentials
    debugMode     = true                                               // Should be a constant
    MAX_RETRIES   = 3                                                  // Should be camelCase
)

// Constants not properly grouped
const SECRET_KEY = "my-super-secret-key-12345" // Security issue: hardcoded secret
const ApiVersion = "v1"                        // Should be all caps
const (
    statusOk       = 200 // Should be exported and use proper naming
    STATUS_NOT_FOUND = 404
)

// Function with too many parameters and inconsistent error handling
func ProcessUserData(id int, name string, email string, age int, active bool, role string) (*User, error) {
    // Naked return
    var result *User
    var err error

    defer func() {
        if r := recover(); r != nil {
            // Ineffective assignment - will be lost due to naked return
            err = fmt.Errorf("panic: %v", r)
        }
    }()

    // Unused variable
    count := 0

    // Ignored error
    data, _ := json.Marshal(map[string]interface{}{
        "id":    id,
        "name":  name,
        "email": email,
    })

    // Unhandled error and resource leak (file not closed)
    file, _ := os.Create("user.json")
    file.Write(data)

    // Magic numbers
    if age < 18 {
        return nil, fmt.Errorf("user too young")
    }

    if active == true { // Redundant comparison with boolean
        // Empty if block
    }

    // Variable shadowing
    if id > 0 {
        err := fmt.Errorf("id already exists")
        log.Println(err)
    }

    // Inconsistent error handling
    user := &User{
        Id:        id,
        FirstName: name,
        Email:     email,
    }

    return user, err
}

// Inconsistent receiver naming
func (this *User) Save() error {
    // Redundant nil check before return
    if this.Id == 0 {
        return nil
    } else { // Redundant else
        // Direct use of fmt.Println in production code
        fmt.Println("Saving user:", this.FirstName)

        // Possible nil pointer dereference
        var u *User
        fmt.Println(u.Email)

        return nil
    }
}

// Exported function without comment
func FetchUsers(ctx context.Context) ([]*User, error) {
    // Deprecated function usage
    body, _ := ioutil.ReadAll(nil)

    // Channel operations without select (potential deadlock)
    ch := make(chan *User)
    ch <- &User{} // Will block forever

    // Goroutine leak - no way to signal completion
    go func() {
        // Infinite loop
        for {
            time.Sleep(time.Second)
        }
    }()

    // Slice declaration with non-zero length but zero capacity
    users := make([]*User, 10, 0)

    // Switch without default
    switch os.Getenv("ENV") {
    case "dev":
        log.Println("Development mode")
    case "prod":
        log.Println("Production mode")
    }

    // Inefficient string concatenation in loop
    var result string
    names := []string{"John", "Jane", "Bob"}
    for _, name := range names {
        result = result + name + ", "
    }

    // Mutex not unlocked on all paths
    var mu sync.Mutex
    mu.Lock()
    if len(users) > 0 {
        return users, nil // Returns without unlocking
    }
    mu.Unlock()

    return nil, fmt.Errorf("no users found")
}

// Function with unused parameter
func ValidateUser(u *User, role string) bool {
    // Direct println usage
    println("Validating user")

    // Unchecked type assertion
    config := map[string]interface{}{"min_age": 18}
    minAge := config["min_age"].(int)

    // Redundant if-else
    if u.Email != "" {
        return true
    } else {
        return false
    }
}

// HTTP handler with multiple issues
func UserHandler(w http.ResponseWriter, r *http.Request) {
    // Not checking errors
    w.Write([]byte("Hello"))

    // SQL injection vulnerability
    id := r.URL.Query().Get("id")
    query := "SELECT * FROM users WHERE id = " + id

    // Command injection
    cmd := "ls -la " + r.URL.Query().Get("dir")
    os.Execute(cmd)

    // Context not passed down
    http.Get("https://api.example.com/users")

    // Returning in a defer function
    defer func() {
        return // Does nothing
    }()

    // Unreachable code
    return
    fmt.Println("This will never execute")
}

// Main function with multiple issues
func main() {
    // Ignored return values
    strings.Replace("hello world", "world", "golang", -1)

    // Ineffective assignment
    x := 10
    x = 20
    x = 30
    fmt.Println("Value:", x)

    // Time constants
    timeout := 10 // Should use time.Duration

    // Unhandled close error
    f, _ := os.Open("file.txt")
    defer f.Close()

    // HTTP server without timeout configuration
    http.ListenAndServe(":8080", nil)
}

// Duplicate function parameter names
func UpdateUser(id int, name string, name string) error {
    return nil
}

// Function that doesn't handle errors on all paths
func GetUserByID(id int) *User {
    if id <= 0 {
        // Missing return
    }
    return &User{Id: id}
}

// Struct with alignment issues (memory padding inefficiency)
type Config struct {
    Name    string
    ID      int
    Enabled bool
    Count   int64
}

// Copy lock by value
func copyLock(mu sync.Mutex) {
    mu.Lock()
    mu.Unlock()
}

// Inefficient map initialization
func createUserMap() map[string]*User {
    m := make(map[string]*User)
    m["admin"] = &User{Id: 1, FirstName: "Admin"}
    return m
}
