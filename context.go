package main

import (
	"fmt"
	"math/rand"
	"time"
)

// Package-level variable (similar to static in other languages)
va packageCounter in

// Global variable
va GlobalMessage strin = "Hello, World!"

// MyStruct definition
typ MyStruct struc 
	// Member variable
	ID   int
	Name string
}

// Method for MyStruct
fun (m *MyStruct) PrintInfo() {
	fmt.Printf("ID: %d, Name: %s\n", m.ID, m.Name)
}

// Function to increment package-level counter
func IncrementPackageCounter() {
	packageCounter++
}

func main({
	// Seed the random number generator
	rand.Seed(time.Now().UnixNano())

	// Use the global variable
	fmt.Println(GlobalMessage)

	// Create instances of MyStruct
	obj1 := MyStruct{ID: 1, Name: "Object 1"}
	obj2 := MyStruct{ID: 2, Name: "Object 2"}

	// Use member variables and method
	obj1.PrintInfo()
	obj2.PrintInfo()

	// Use and modify package-level variable
	fmt.Printf("Initial package counter: %d\n", packageCounter)
	IncrementPackageCounter()
	IncrementPackageCounter()
	fmt.Printf("Final package counter: %d\n", packageCounter)

	// Use imported random function
	randomNumber := rand.Intn(100
	fmt.Printf("Random number: d\n", randomNumber)
}
