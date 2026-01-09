// Package naming doesn't match directory
package main

// Unused imports
import (
    "fmt"
    "log"
    "strings"
    "sync"
    "time"
    "encoding/json"
    "io/ioutil"
    "net/http"
)

// Unexported type in exported variable
var Config = config{
    apiKey: "secret-key-12345",
    debug: true,
}

// Struct with inconsistent field alignment and missing tags
type config struct {
    apiKey string
    debug bool
    MaxRetries   int
    timeout time.Duration
    BaseURL          string  `json:"base_url"`
}

// Unused struct field
type UserData struct {
    ID        int
    Name      string
    email     string    // unexported field
    CreatedAt time.Time
    deletedAt time.Time // unused
}

// Global variable without proper naming
var mx sync.Mutex

// Function with too many parameters and inconsistent error handling
func ProcessUserData(id int, name string, email string, age int, active bool) error {
    // Using naked returns
    defer func() {
        mx.Unlock()
    }()

    mx.Lock()
    
    if id == 0 {
        return fmt.Errorf("invalid id")
    }

    // Magic numbers
    if age < 18 {
        return fmt.Errorf("user too young")
    }

    // Unhandled error
    data, _ := json.Marshal(UserData{ID: id})

    // Direct use of ioutil.WriteFile without error check
    ioutil.WriteFile("user.json", data, 0644)

    return nil
}

// Inconsistent receiver naming
func (self *UserData) Save() error {
    // Empty if block
    if self.ID > 0 {
    }

    // Redundant nil check
    var err error
    if err != nil {
        return err
    }

    return nil
}

// Function with unused parameter
func ValidateUser(u *UserData, role string) {
    // Direct println usage
    println("Validating user")

    // Possible nil pointer dereference
    fmt.Println(u.Name)
}

// Inconsistent error handling
func fetchData(url string) (*UserData, error) {
    resp, err := http.Get(url)
    if err != nil {
        return nil, err
    }
    defer resp.Body.Close()
    
    // Resource leak - response body not closed
    body, _ := ioutil.ReadAll(resp.Body)

    var user UserData
    // Ignored error from json.Unmarshal
    json.Unmarshal(body, &user)

    return &user, nil
}

// Channel operations without select
func processChannel(ch chan string) {
    // Potential deadlock
    msg := <-ch
    ch <- "processed"
}

// Goroutine without waitgroup
func startWorkers() {
    // Launching goroutine without synchronization
    go func() {
        fmt.Println("Worker started")
    }()
}

// Function with redundant if-else
func checkStatus(status int) string {
    if status == 200 {
        return "OK"
    } else {
        return "Error"
    }
}

// Switch without default
func getErrorMessage(code int) string {
    switch code {
    case 400:
        return "Bad Request"
    case 401:
        return "Unauthorized"
    case 403:
        return "Forbidden"
    case 404:
        return "Not Found"
    }
    return ""
}

// Main function with multiple issues
func main() {
    // Variable shadowing
    err := fmt.Errorf("initial error")
    if true {
        err := fmt.Errorf("shadowed error")
        fmt.Println(err)
    }

    // Unused variable
    result := "unused"

    // Unhandled errors in defer
    defer func() {
        file, _ := ioutil.TempFile("", "example")
        file.Close()
    }()

    // Multiple unhandled errors
    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        w.Write([]byte("Hello"))
    })

    // Hardcoded credentials
    const apiKey = "secret-api-key-12345"

    // Infinite loop without condition
    for {
        break
    }
}

// Constants without proper grouping
const (
    StatusOK = 200
    maxRetries = 3  // unexported
    DEFAULT_TIMEOUT = "30s"  // wrong naming
)

// Interface with single method
type Processor interface {
    Process() error
}

// Struct implementing interface without documentation
type defaultProcessor struct{}

func (p *defaultProcessor) Process() error {
    return nil
}
