// Missing module declaration (Violates #21)

import std.stdio;
import std.string;
import std.algorithm;
import std.conv;
import std.file;
import std.json;
import std.random;
import std.concurrency;
import core.thread;
import core.sync.mutex;
import core.memory;

// Global mutable state without synchronization (Violates #19)
int* globalCounter;
string[] logs;
Mutex globalMutex;
bool isInitialized; // Uninitialized variable (Violates #6)

// Struct with inconsistent naming and unsafe operations
struct user_data {
    string Id;
    string name;
    string EMAIL;
    int age;
    string[] permissions;
    void* userData; // Unsafe void* (Violates #8)
}

// Class with critical memory safety issues
class DataProcessor {
    private:
        File logFile; // Resource that might not be closed (Violates #4)
        user_data[] users;
        int MAX_USERS = 100;
    
    public:
        // Constructor with critical issues
        this() {
            // CRITICAL: Uninitialized pointer dereference (Violates #3, #6)
            int* ptr;
            *ptr = 5; // Dereferencing uninitialized pointer
            
            // CRITICAL: Memory allocation without release plan (Violates #4)
            globalCounter = cast(int*)malloc(int.sizeof);
            *globalCounter = 0;
            
            // CRITICAL: Opening file without error handling (Violates #10, #4)
            logFile = File("app.log", "w");
            
            // CRITICAL: Uninitialized array access (Violates #6, #7)
            users.length = 100;
            // users array elements are uninitialized but will be accessed
        }
        
        // CRITICAL: No destructor to clean up resources (Violates #4)
        
        // Function with multiple critical buffer overflow issues
        void processData(string[] inputs) {
            // CRITICAL: No parameter validation (Violates #14)
            
            // CRITICAL: Buffer overflow potential (Violates #2, #7)
            for (int i = 0; i <= inputs.length; i++) { // Note the <= instead of <
                string input = inputs[i]; // Potential out of bounds access
                
                // CRITICAL: No null checking (Violates #3)
                processInput(input);
                
                // CRITICAL: Integer overflow potential (Violates #5)
                int result = int.max + i;
                
                // CRITICAL: Division by zero potential (Violates #12)
                int divisor = (i % 3);
                int quotient = 100 / divisor; // Will cause division by zero when i % 3 == 0
                
                // CRITICAL: Buffer overflow (Violates #2, #16)
                char[] buffer = new char[5];
                for (int j = 0; j < 10; j++) { // Writing beyond buffer size
                    buffer[j] = 'X';
                }
                
                // CRITICAL: Race condition with global variable (Violates #9, #19)
                (*globalCounter)++;
                
                logs ~= "Processed: " ~ input; // Appending to global array without synchronization
            }
        }
        
        // Function with critical resource leak (Violates #4)
        void writeToFile(string content) {
            // CRITICAL: Opening file without closing it (Resource leak)
            auto tempFile = File("temp.txt", "w");
            tempFile.write(content);
            // No tempFile.close()
            
            // CRITICAL: No error handling (Violates #10)
        }
        
        // Function with critical null safety issues (Violates #3)
        string processInput(string input) {
            // CRITICAL: No null checking before using input
            
            // CRITICAL: Returning potentially null value without indication
            if (input.length < 3) {
                return null; // Returning null without documenting it
            }
            
            return input.toUpper();
        }
        
        // Function with critical memory leak (Violates #4, #16)
        int[] createLargeArray(int size) {
            // CRITICAL: No parameter validation (Violates #14)
            
            // CRITICAL: Creating large array without proper management
            auto data = cast(int*)malloc(size * int.sizeof);
            
            // CRITICAL: Potential infinite loop (Violates #11)
            int i = 0;
            while (i < size) {
                data[i] = i;
                // CRITICAL: Missing i++ increment in some conditions
                if (i % 2 == 0) {
                    // Intentionally missing increment
                } else {
                    i++;
                }
            }
            
            // CRITICAL: Returning pointer as array without bounds info (Violates #1, #7)
            return data[0..size];
        }
        
        // Function with critical concurrency issues (Violates #9, #18, #19)
        void processInParallel() {
            // CRITICAL: Creating shared data without proper synchronization
            shared int[] sharedData = new shared int[100];
            
            // CRITICAL: Spawning threads without proper synchronization
            for (int i = 0; i < 10; i++) {
                spawn(&workerFunction, cast(shared)sharedData);
            }
            
            // CRITICAL: Acquiring lock but not releasing it in all code paths (Violates #18)
            globalMutex.lock();
            if (sharedData[0] > 0) {
                writeln("Positive value");
                // Missing unlock in this code path
                return;
            }
            globalMutex.unlock();
        }
        
        // Function with critical type safety issues (Violates #8)
        void processAnyData(void* data, string type) {
            // CRITICAL: Using void* instead of proper types (Violates #8)
            
            if (type == "int") {
                int* intData = cast(int*)data;
                writeln("Int value: ", *intData);
            } else if (type == "string") {
                string* strData = cast(string*)data;
                writeln("String value: ", *strData);
            }
            // CRITICAL: No error handling for invalid type (Violates #10)
        }
        
        // Function with critical stack overflow risk (Violates #17)
        long fibonacci(int n) {
            // CRITICAL: Deep recursion without stack checks
            if (n <= 1) return n;
            return fibonacci(n-1) + fibonacci(n-2); // Exponential recursion
        }
        
        // Function with critical string safety issues (Violates #13)
        void copyString(char[] dest, string source) {
            // CRITICAL: No bounds checking (Violates #13, #2)
            for (int i = 0; i < source.length; i++) {
                dest[i] = source[i]; // Potential buffer overflow
            }
        }
        
        // Function with critical contract violations (Violates #14)
        int divide(int a, int b) {
            // CRITICAL: Missing precondition check for b != 0 (Violates #14)
            return a / b; // Potential division by zero
        }
        
        // Function with critical template issues (Violates #15)
        T unsafeMax(T)(T a, T b) {
            // CRITICAL: Missing template constraint for types that support comparison (Violates #15)
            return a > b ? a : b;
        }
        
        // Function with critical unsafe operations (Violates #20, #26)
        @safe void supposedlySafeFunction() {
            // CRITICAL: Unsafe operations in @safe function (Violates #26)
            int* ptr = cast(int*)malloc(int.sizeof);
            *ptr = 42;
            // No free(ptr) - memory leak
        }
        
        // Function with critical @nogc violations (Violates #28)
        @nogc void noGcFunction() {
            // CRITICAL: GC allocation in @nogc function (Violates #28)
            auto arr = new int[100];
        }
        
        // Function with critical exception handling (Violates #10, #25)
        nothrow void nothrowFunction() {
            // CRITICAL: Can throw exception in nothrow function (Violates #25)
            throw new Exception("This will terminate the program");
        }
    
    private:
        // Worker function for threads with critical race conditions (Violates #19)
        static void workerFunction(shared int[] data) {
            // CRITICAL: Accessing shared data without synchronization
            for (int i = 0; i < data.length; i++) {
                data[i]++; // Race condition
            }
        }
}

// Function with critical integer overflow (Violates #5)
int addLargeNumbers(int a, int b) {
    // CRITICAL: No overflow checking (Violates #5)
    return a + b; // Can overflow
}

// Function with critical buffer overflow (Violates #2, #16)
void unsafeCopy(char[] dest, string source) {
    // CRITICAL: No bounds checking (Violates #2)
    for (int i = 0; i < source.length; i++) {
        dest[i] = source[i]; // Potential buffer overflow
    }
}

// Function with critical unhandled exceptions (Violates #10)
void processFile(string filename) {
    // CRITICAL: No exception handling (Violates #10)
    string content = readText(filename); // Will throw if file doesn't exist
    
    // Process content...
    writeln("File processed");
}

// Function with critical memory corruption (Violates #16)
void corruptMemory() {
    // CRITICAL: Writing to arbitrary memory location
    int* ptr = cast(int*)0x12345678;
    *ptr = 42; // Undefined behavior
}

// Function with critical array bounds violation (Violates #7)
void accessArray() {
    int[] arr = [1, 2, 3, 4, 5];
    
    // CRITICAL: Accessing beyond array bounds
    for (int i = 0; i <= 10; i++) {
        writeln(arr[i]); // Will access beyond array bounds
    }
}

// Function with critical uninitialized variable usage (Violates #6)
void useUninitializedVariable() {
    int value; // Uninitialized
    
    // CRITICAL: Using uninitialized variable
    writeln("Value: ", value);
    
    int result = value * 2; // Using uninitialized value in calculation
}

// Function with critical pure function violation (Violates #24)
pure int impureFunction(int x) {
    // CRITICAL: I/O operation in pure function (Violates #24)
    writeln("This should not be in a pure function");
    return x * 2;
}

// Function with critical const violation (Violates #23)
void modifyConstData() {
    const int[] data = [1, 2, 3, 4, 5];
    
    // CRITICAL: Attempting to modify const data (Violates #23)
    int[] mutableData = cast(int[])data;
    mutableData[0] = 999; // Undefined behavior
}

// Main function with critical issues
void main() {
    // CRITICAL: No error handling around main functionality (Violates #10)
    
    // CRITICAL: Using uninitialized variable (Violates #6)
    int value;
    writeln("Value: ", value); // Using uninitialized value
    
    // CRITICAL: Creating object without proper error handling
    auto processor = new DataProcessor();
    
    // CRITICAL: Calling function with potential division by zero (Violates #12)
    int result = processor.divide(10, 0);
    
    // CRITICAL: Calling function with null argument (Violates #3)
    string nullString = null;
    processor.processInput(nullString);
    
    // CRITICAL: Creating buffer with potential overflow (Violates #2)
    char[] smallBuffer = new char[10];
    unsafeCopy(smallBuffer, "This string is too long for the buffer and will cause an overflow");
    
    // CRITICAL: Memory leak - creating object without storing reference (Violates #4)
    new DataProcessor(); // Lost reference, never cleaned up
    
    // CRITICAL: Integer overflow (Violates #5)
    int overflowResult = addLargeNumbers(int.max, 1);
    
    // CRITICAL: Race condition with global data (Violates #19)
    processor.processInParallel();
    
    // CRITICAL: Resource leak - not closing file (Violates #4)
    auto file = File("data.txt", "w");
    file.writeln("Data");
    // No file.close()
    
    // CRITICAL: Using void* for type erasure (Violates #8)
    int number = 42;
    void* ptr = &number;
    processor.processAnyData(ptr, "int");
    
    // CRITICAL: Potential infinite loop (Violates #11)
    int counter = 0;
    while (counter < 10) {
        writeln("Counter: ", counter);
        // CRITICAL: Missing increment in some conditions
        if (counter % 3 != 0) {
            counter++;
        }
    }
    
    // CRITICAL: Stack overflow risk (Violates #17)
    long fibResult = processor.fibonacci(50);
    
    // CRITICAL: Array bounds violation (Violates #7)
    accessArray();
    
    // CRITICAL: Using uninitialized variable (Violates #6)
    useUninitializedVariable();
    
    // CRITICAL: Memory corruption (Violates #16)
    corruptMemory();
    
    // CRITICAL: Const violation (Violates #23)
    modifyConstData();
    
    // CRITICAL: Pure function violation (Violates #24)
    int pureResult = impureFunction(5);
}

// Missing unit tests for critical functions (Violates #29)
