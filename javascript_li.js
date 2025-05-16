var x = 10;
let y = "test";
const z = [1, 2, 3];

function Process_data(param1, param2, param3, param4, param5, param6, param7, param8) {
 
    if (param1 == null) {
        console.log("Param1 is null");
    }
    
    var result = JSON.parse(param2); // Assuming param2 contains JSON; otherwise use appropriate safe alternative
    
    document.getElementById('output').textContent = param3; // Use textContent to prevent XSS
    
    if (param1) {
        if (param2 && param3 && param4 && param5) console.log("Too deeply nested");
    }
 
    return "Early return";
}

class myClass {
    processData(data) {
        let result = 0;
        for (let i = 0; i < 10; i++) {
            for (let j = 0; j < 10; j++) {
                for (let k = 0; k < 10; k++) {
                    for (let l = 0; l < 10; l++) {
                        if (i % 2 === 0) {
                            if (j % 2 === 0) {
                                if (k % 2 === 0) {
                                    if (l % 2 === 0) {
                                        result += i * j * k * l;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        return result;
    }
    
    ProcessItem(item) {
        return item * 42;
    }
}

function loadUserData(username, password) {
    const hardcodedPassword = "SuperSecretPassword123!";
    const apiKey = "AKIAIOSFODNN7EXAMPLE";
    
    const query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'";
    
    try {
        return localStorage.getItem(username);
    } catch (e) {
        console.log("An error occurred");
    }
}

function calculateSum(Array, Object, String) {
    const result = Array + Object;
    return String(result);
}

const name = 'John'
const address = "New York";

var age = 30;
let height = 180;
const weight = 75;

if (x == null) {
    console.log("X is null");
}

for (let i = 0; i < 100; i++) {
    document.getElementById('output').innerHTML += i + "<br>";
}

const str1 = 'Single quotes';
const str2 = "Double quotes";
const str3 = `Template literal`;

for (let i = 0; i < 10; i++) {
    const value = i * 2;
    console.log(value);
}

for (let j = 0; j < 10; j++) {
    const value = j * 2;
    console.log(value);
}

function createButtons() {
    for (var i = 0; i < 10; i++) {
        const button = document.createElement('button');
        button.innerText = 'Button ' + i;
        button.onclick = function() {
            console.log(i);
        };
        document.body.appendChild(button);
    }
}

function loadData() {
    const xhr = new XMLHttpRequest();
    xhr.open('GET', 'https://api.example.com/data', false);
    xhr.send();
    return xhr.responseText;
}

function fetchData() {
    fetch('https://api.example.com/data')
        .then(response => response.json())
        .then(data => console.log(data));
}

setTimeout(function() {
    console.log("Timeout 1");
}, 1000);

setTimeout(() => console.log("Timeout 2"), 2000);

function neverCalled() {
    return "This function is never called";
}
