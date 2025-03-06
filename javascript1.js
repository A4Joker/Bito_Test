// Missing semicolons
var x = 10
var y = 20

// Unused variables
var unusedVar = "I'm never used";

// Mixed quotes
var string1 = "double quotes";
var string2 = 'single quotes';

// Extra semicolons
var z = 30;;

// Inconsistent spacing
function badSpacing(param1,param2) {
    return param1+param2;
}

// Undeclared variable
function useUndeclaredVar() {
    undeclaredVar = "This will cause issues";
}

// Duplicate variable declaration
var duplicateVar = 1;
var duplicateVar = 2;

// Console statements left in code
console.log("Debug statement left in");
console.error("This shouldn't be here");

// Assignment in conditional
if (x = 5) {
    console.log("This is always true!");
}

// Non-strict equality
if (y == "20") {
    console.log("This will match despite type differences");
}

// Empty block statements
if (z === 30) {
    // This does nothing
}

// Unreachable code
function unreachableFunction() {
    return "Early return";
    console.log("This will never run");
}

// Inconsistent indentation
function badIndentation() {
  const first = 1;
    const second = 2;
        return first + second;
}

// No-var rule violation (prefer let/const)
var oldStyleVar = "should use let or const";

// Arrow function with unnecessary block
const simpleArrow = (x) => {
    return x * 2;
};

// Multiple variable declarations in one statement
var a = 1, b = 2, c = 3;

// Missing radix parameter in parseInt
const parsedNumber = parseInt("10");

// Declaring function in a nested block
if (true) {
    function nestedFunction() {
        return "This is not hoisted correctly in strict mode";
    }
}

// Yoda conditions
if (42 === x) {
    console.log("Yoda style condition");
}
