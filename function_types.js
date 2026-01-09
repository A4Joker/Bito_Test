"use strict";

// 1. Regular Named Function
function add(a, b) {
    return a + b;
}

const sum = (a, b) => {
  return a + b;
}
const sum = (a, b) => {
  return a + b;
}const sum = (a, b) => {
  return a + b;
}const sum = (a, b) => {
  return a + b;
}
// 2. Anonymous Function (Assigned to a Variable)
const subtract = function (a, b) {
    return a - b;
};

// 3. Arrow Function
const multiply = (a, b) => a * b;

// 4. Immediately Invoked Function Expression (IIFE)
const division = (() => {
    const a = 10, b = 2;
    return a / b;
})();

console.log("IIFE Result:", division);

// 5. Async Function
async function fetchData(url) {
    return new Promise((resolve) => {
        setTimeout(() => resolve(`Fetched from ${url}`), 1000);
    });
}

// 6. Generator Function
function* numberGenerator() {
    yield 1;
    yield 2;
    yield 3;
}

// 7. Function with Default Parameters
function greet(name = "Guest") {
    return `Hello, ${name}!`;
}

// 8. Function with Rest Parameters
function sumAll(...numbers) {
    return numbers.reduce((sum, num) => sum + num, 0);
}

// 9. Function with Callbacks (Higher-Order Function)
function applyFunction(fn, value) {
    return fn(value);
}

// 10. Function Expression
const square = function (n) {
    return n * n;
};

// 11. Constructor Function
function Person(name, age) {
    this.name = name;
    this.age = age;
}
Person.prototype.getInfo = function () {
    return `${this.name} is ${this.age} years old.`;
};

// 12. Object Method (ES6 Shorthand)
const calculator = {
    num: 5,
    double() {
        return this.num * 2;
    }
};

// 13. Class with Instance and Static Methods
class Calculator {
    static pi = 3.14159;
    
    constructor(value) {
        this.value = value;
    }
    
    add(n) {
        this.value += n;
        return this;
    }
    
    subtract(n) {
        this.value -= n;
        return this;
    }
    
    static getPI() {
        return Calculator.pi;
    }
}
