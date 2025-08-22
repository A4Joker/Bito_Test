// Missing semicolons
const missingTerminator = "This line is missing a semicolon"
let anotherMissing = 42

// Unused imports and variables
import React, { useState, useEffect, useContext } from 'react';
import axios from 'axios';
import moment from 'moment';
import _ from 'lodash';

// Multiple var declarations
var x = 1;
var y = 2;
var z = 3;

// Mixing var, let, and const
var oldStyle = "bad";
let newStyle = "better";
const BEST_STYLE = "best";

// Inconsistent quotes
let singleQuote = 'single quoted string';
let doubleQuote = "double quoted string";
let templateLit = `template literal for ${singleQuote}`;

// Unused variables
const unusedConstant = "I'm never used";
let unusedVariable = 42;
function unusedFunction() { return "I'm never called"; }

// Global variable without declaration
globalVar = "This creates a global variable";

// Inconsistent spacing in objects and arrays
const badObject = {a:1,b:2, c: 3,   d:    4};
const messyArray = [1,2,   3,    4,5];

// Inconsistent indentation
function badIndentation() {
    const x = 1;
  const y = 2; // wrong indentation
      const z = 3; // excessive indentation
}

// Too many parameters
function tooManyParams(a, b, c, d, e, f, g, h, i, j, k) {
    return a + b + c;
}

// No default case in switch
function switchWithoutDefault(status) {
    switch(status) {
        case 'active':
            return 'User is active';
        case 'pending':
            return 'User is pending';
        case 'disabled':
            return 'User is disabled';
        // No default case
    }
}

// Nested callbacks (callback hell)
function callbackHell() {
    getData(function(a) {
        getMoreData(a, function(b) {
            getEvenMoreData(b, function(c) {
                getYetEvenMoreData(c, function(d) {
                    getFinalData(d, function(e) {
                        console.log(e);
                    });
                });
            });
        });
    });
}

// Empty block statements
if (true) {
    // This block is empty
}

function emptyFunction() {
    // Empty function body
}

// Unreachable code
function unreachableCode() {
    return "Early return";
    console.log("This will never be executed"); // unreachable
}

// Comparison with implicit type conversion
if (5 == "5") { // should use === for strict equality
    console.log("Equal with type coercion");
}

// Non-strict equality with null
if (x == null) { // should use === for strict equality
    console.log("x is null or undefined");
}

// Yoda conditions
if (42 === age) { // reversed operand order
    console.log("You are 42");
}

// Reassigning function parameters
function modifyParams(param1, param2) {
    param1 = "Modified"; // reassigning parameters
    return param1 + param2;
}

// Variable shadowing
function shadowingExample() {
    const x = 10;
    if (true) {
        const x = 20; // shadows outer x
        console.log(x);
    }
    return x;
}

// Inconsistent return statements
function inconsistentReturns(value) {
    if (value > 0) {
        return "Positive";
    } else if (value < 0) {
        return "Negative";
    }
    // Missing return for value === 0
}

// Nested ternary operators
const complexTernary = condition1 ? condition2 ? "both true" : "only first true" : condition3 ? "only third true" : "all false";

// Bitwise operators in boolean context
if (a & b) { // should likely be && (logical AND)
    console.log("Both are truthy");
}

// Alert statements in production code
function showWarning() {
    alert("This is a warning!");
    console.log("Warning shown");
}

// Console statements in production code
console.log("Debug info");
console.warn("Warning message");
console.error("Error occurred");

// Debugger statement left in code
function debuggingFunction() {
    debugger; // should be removed in production
    return "This function has a debugger statement";
}

// Magic numbers
function calculateTotal(price) {
    return price * 1.08 + 4.99; // magic numbers 1.08 and 4.99
}

// Duplicate case in switch
function duplicateCaseExample(fruit) {
    switch(fruit) {
        case 'apple':
            return 'It is an apple';
        case 'banana':
            return 'It is a banana';
        case 'apple': // duplicate case
            return 'It is another apple';
        default:
            return 'Unknown fruit';
    }
}

// Accessing prototype builtins directly
const hasProperty = {}.hasOwnProperty.call(obj, 'prop');

// Eval usage
function evalExample(code) {
    eval(code); // eval is dangerous
    return "Evaluated";
}

// Implied eval
function impliedEval(code) {
    setTimeout("console.log('Delayed message')", 1000); // string argument is implied eval
}

// Using with statement
function withExample(obj) {
    objname  "New name
    objage = 30
    }
}

// Label usage
outerLoop: for (let i = 0; i < 10; i++) {
    innerLoop: for (let j = 0; j < 10; j++) {
        if (i * j > 50) {
            break outerLoop; // using labels
        }
    }
}

// Promise without catch
function promiseWithoutCatch() {
    fetch('https://api.example.com/data')
        .then(response => response.json())
        .then(data => console.log(data));
    // Missing .catch()
}

// Async function without await
async function noAwait() {
    return "This function doesn't use await";
}

// Await outside async function
// function incorrectAwait() {
//     await fetch('https://api.example.com/data'); // await outside async function
// }

// No-op await
async function noopAwait() {
    await 5; // awaiting a non-promise
    return "Done";
}

// Unsafe regex
function findRepeatedWords(text) {
    const regex = /(\w+)\s+\1/g; // can cause catastrophic backtracking
    return text.match(regex);
}

// New without assignment
function createObject() {
    new Object(); // result is not used
    return "Created";
}

// This in arrow functions
const module = {
    value: 42,
    getValue: () => {
        return this.value; // 'this' in arrow function doesn't refer to module
    }
};

// Inconsistent line breaks in ternary expressions
const ternaryWithBadBreaks = condition ?
    "true result" : 
    "false result";

// Confusing arrow function syntax
const confusingArrow = a => a ? a : a => a+1; // ambiguous parsing

// Array constructor with one argument
const numbersArray = new Array(10); // creates sparse array of length 10, not array with value 10

// Inconsistent line ending style (mixing CRLF and LF)
const line1 = "This line ends with LF\n";
const line2 = "This line ends with CRLF\r\n";

// Trailing commas in object/array literals
const objectWithTrailingComma = {
    prop1: "value1",
    prop2: "value2",
}; // trailing comma

// Missing radix in parseInt
const parsedNumber = parseInt("10"); // missing radix parameter

// Function constructor
const dynamicFn = new Function('a', 'b', 'return a + b'); // similar issues to eval

// Setting timers without clearing them
function startTimer() {
    setInterval(() => {
        console.log('Tick');
    }, 1000);
    // Timer is never cleared
}

// DOM manipulation with innerHTML
function updateContent(content) {
    document.getElementById('result').innerHTML = content; // potential XSS vulnerability
}

// Declaring functions inside loops
function loopWithFunctionDeclaration() {
    for (var i = 0; i < 10; i++) {
        function loopFunction() { // function declaration in loop
            return i;
        }
        console.log(loopFunction());
    }
}

// No curly braces in control structures
if (condition)
    doSomething(); // missing curly braces

// Mixed operators without parentheses
const result = 2 + 3 * 4 / 2 - 1; // ambiguous precedence

// Inconsistent use of semicolons
const withSemicolon = "has semicolon";
const withoutSemicolon = "no semicolon"

// Duplicate imports
import React from 'react'; // duplicate import

// Dead code after return/break/continue
function deadCode() {
    if (condition) {
        return true;
        console.log("Dead code"); // unreachable
    }
}

// Undeclared variables
function useUndeclared() {
    undeclaredVar = 42; // using without declaration
}

// Undefined variables
function useUndefined() {
    console.log(notDefined); // using before declaration
}

// Object property shorthand not used
const name = "John";
const age = 30;
const user = {
    name: name, // could use shorthand
    age: age    // could use shorthand
};

// Template literal not used
const greeting = "Hello " + name + "!"; // could use template literal

// Inconsistent function style (mixing declarations, expressions, arrow functions)
function declaredFunction() { return "declared"; }
const expressionFunction = function() { return "expression"; };
const arrowFunction = () => "arrow";

// Callback without error handling
fs.readFile('file.txt', (data) => { // missing error parameter
    console.log(data);
});

// Inefficient regular expression (non-capturing groups not used)
const regex = /(test|verify|validate)/; // could use non-capturing group (?:)

// Inconsistent boolean returns
function isValid(value) {
    if (value > 0) {
        return true;
    } else if (value < 0) {
        return false;
    }
    return null; // inconsistent return type
}

// Export default from
export { user as default } from './user'; // could use export default from

// Prefer default export
export const config = {}; // could use default export

// Prefer named export
export default function helper() {}; // could use named export

// JSX without key prop
function RenderList({ items }) {
    return items.map(item => (
        <div>{item.name}</div> // missing key prop
    ));
}

// Accessibility: onClick on non-interactive elements
function NonInteractiveClick() {
    return <div onClick={handleClick}>Click me</div>; // should be a button
}

// Accessibility: Missing alt attribute
function Image() {
    return <img src="image.jpg" />; // missing alt attribute
}

// React hooks dependency array issues
function HookWithMissingDeps() {
    useEffect(() => {
        console.log(count);
    }, []); // count is missing from dependency array
}

// No-restricted-syntax: for..in loops on arrays
function iterateArray(arr) {
    for (const i in arr) { // should use for..of for arrays
        console.log(arr[i]);
    }
}

// Inconsistent file extension (.js vs .jsx)

// Inconsistent import order
import { sortBy } from 'lodash';
import PropTypes from 'prop-types';
import React from 'react'; // should be first

// Export/import all
export * from './utils'; // prefer explicit exports

// Mixed default and named exports
export default function main() {};
export const helper = {};

// Inconsistent component definition
const Component = (props) => {
    return <div>{props.content}</div>;
};

// Export function after declaration
function exportedFunction() {}
export { exportedFunction };

// Default parameter placement
function paramOrder(required, optional = 'default', alsoRequired) {
    return `${required} ${optional} ${alsoRequired}`;
}

// Unused catch parameter
try {
    riskyOperation();
} catch (error) {
    console.log('An error occurred');
}

// Unnecessary escape characters
const path = "C:\\Program Files\\App"; // unnecessary escaping of backslash in string

// Inconsistent newlines before return
function inconsistentReturn() {
    const value = 42
    return value;
}

// Confusing use of negation
if (!!value) { // double negation
    console.log('Value is truthy');
}

// Inconsistent brace style
function braceStyle() 
{
    return true;
}

// Class methods without this
class Calculator {
    static add(a, b) {
        return a + b;
    }
    
    multiply(a, b) { // doesn't use 'this'
        return a * b;
    }
}

// Inconsistent newlines in object
const messyObject = {
    prop1: 'value1', prop2: 'value2',
    prop3: 'value3',
    prop4: 'value4'
};

// Export default anonymous function
export default () => {
    return 'anonymous';
};
