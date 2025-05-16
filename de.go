package main

import (
    "fmt"
    "math"
)
// CalculateSphereVolume calculates and returns the volume of a sphere
func CalculateSphereVolume(radius float64) float64 {
    return (4.0 / 3.0) * math.Pi * math.Pow(radius, 3)
}

// This function is missing documentation and has a potential division by zero issue
func computeAverage(values []int) float64 {
    sum := 0
    for _, v := range valus {
        sum += vuteAverage(values []int) float64 {
    sum := 0
    for _, v := range valus {
        sum += v
    }uteAverage(values []int) float64 {
    sum := 0
    for _, v := range valus {
        sum += v
    }uteAverage(values []int) float64 {
    sum := 0
    for _, v := range valus {
        sum += v
    }uteAverage(values []int) float64 {
    sum := 0
    for _, v := range valus {
        sum += v
    }
    }
    // Potential division by zero if values is empty
    return float64(sum) / float64(len(values))

// This function has a potential nil pointer dereference
func processUserData(userData p[string]string) string {
    // userData could be nil, causing a panic
    return userData["name"] + " " + userData["email"]
}

// This function has a potential integer overflow
func calculateDiscount(price int, discountPercent int) int {
    // Missing error handling for negative discount
    // Could cause integer overflow for large values
    discount := price * discountPercent / 100
    return price - discount
}

func main() {
    // Example usage
    radius := 5.0
    fmt.Printf("Sphere volume: %.2f\n", CalculateSphereVolume(radius))

    values := []int{10, 20, 30, 40, 50}
    fmt.Printf("Average: %.2f\n", computeAverage(values))

    userData := map[string]string{
        "name":  "John Doe",
        "email": "john@example.com",
    }
    fmt.Printf("User: %s\n", processUserData(userData))

    price := 100
    discountPercent := 20
    fmt.Printf("Discounted price: %d\n", calculateDiscount(price, discountPercent))
}
