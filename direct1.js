// Unused imports
import React from 'react';
import moment from 'moment';
import axios from 'axios';
import _ from 'lodash';

// Global variables (should be constants)
var API_URL = 'https://api.example.com';
var MAX_RETRIES = 3;

// Missing semicolons
const USERNAME = 'admin'
const PASSWORD = 'password' // Hardcoded credentials (security issue)

// Unused variable
let retryCount = 0;

// Inconsistent spacing and indentation
function processData(data,options)
{
  // Unused parameter
  const { format, timeout, verbose } = options || {};
  
  // Using == instead of ===
  if (data == null) {
    return [];
  }
  
  // Inconsistent quotes (mix of single and double)
  console.log("Processing data...");
  
  // Variable shadowing (data shadows parameter)
  let data = [];
  
  try {
    // No-op empty block
    if (format === 'json') {
      
    }
    
    // Unreachable code (after return)
    return data;
    console.log('This will never be executed');
  } catch(e) {
    // Using console.log for errors instead of console.error
    console.log('Error processing data:', e);
  }
}

// Function declared but never used
function formatDate(date) {
  // Using deprecated Date methods
  return date.getMonth() + '/' + date.getDate() + '/' + date.getYear();
}

// Inconsistent function style (mix of declarations and expressions)
const fetchData = function(url) {
  // No error handling for fetch
  return fetch(url)
    .then(response => response.json())
    .then(data => {
      // Reassigning parameter (bad practice)
      url = null;
      return data;
    });
}

// Arrow function with unnecessary return and curly braces
const processItem = (item) => {
  return { 
    id: item.id, 
    name: item.name 
  };
};

// Function with too many parameters
function queryDatabase(table, columns, whereClause, orderBy, limit, ascending, groupBy, having) {
  // String concatenation for SQL (SQL injection risk)
  let query = "SELECT " + columns.join(",") + " FROM " + table;
  
  if (whereClause) {
    query += " WHERE " + whereClause;
  }
  
  // Duplicate code blocks (similar to above)
  if (orderBy) {
    query += " ORDER BY " + orderBy + (ascending ? " ASC" : " DESC");
  }
  
  if (limit > 0) {
    query += " LIMIT " + limit;
  }
  
  // Nested callbacks (callback hell)
  return new Promise((resolve, reject) => {
    const db = openDatabase();
    db.query(query, (err, results) => {
      if (err) {
        console.log('Database error:', err);
        reject(err);
      } else {
        db.close((closeErr) => {
          if (closeErr) {
            console.log('Error closing database:', closeErr);
          }
          resolve(results);
        });
      }
    });
  });
}

// Function name doesn't follow camelCase convention
function Export_data(data, outputPath) {
  try {
    // Potential null reference
    if (data.length > 0) {
      // Resource not properly closed
      const file = openFile(outputPath);
      
      // Inefficient loop (forEach would be better)
      for (let i = 0; i < data.length; i++) {
        writeToFile(file, data[i] + "\n");
      }
      
      closeFile(file);
    }
  } catch (e) {
    // Swallowing exception (only logging, not rethrowing)
    console.log('Export failed:', e.message);
  }
}

// Complex function with high cyclomatic complexity
function validateData(data) {
  if (data === null) {
    return false;
  }
  
  if (data.length < 5) {
    return false;
  }
  
  if (data.startsWith('TEST_')) {
    return true;
  }
  
  if (data.endsWith('_VALID')) {
    return true;
  }
  
  if (data.includes('APPROVED')) {
    return true;
  }
  
  const firstChar = data.charAt(0);
  if (firstChar === firstChar.toUpperCase()) {
    const lastChar = data.charAt(data.length - 1);
    if (!isNaN(parseInt(lastChar))) {
      return true;
    }
  }
  
  try {
    parseInt(data);
    return false;
  } catch (e) {
    // Empty catch block (swallowing exception)
  }
  
  // Inconsistent return style (some returns above, some below)
  if (/^[a-zA-Z0-9_]+$/.test(data)) {
    return true;
  } else {
    return false;
  }
}

// Object with mixed property shorthand and non-shorthand
const config = {
  apiUrl: API_URL,
  timeout: 30000,
  retries: MAX_RETRIES,
  verbose: true,
  debug: false,
  logLevel: 'info'
};

// Class with static methods (utility class should be a module with exported functions)
class DateUtils {
  // Missing constructor
  
  static formatDate(date) {
    // Using non-standard Date manipulation
    return date.getFullYear() + '-' + (date.getMonth() + 1) + '-' + date.getDate();
  }
  
  // Unused method parameter
  static isWeekend(date, includeHolidays) {
    const day = date.getDay();
    return day === 0 || day === 6;
  }
}

// Using var for function scoping issues
function scopeIssues() {
  // Variables declared with var are function-scoped, not block-scoped
  if (true) {
    var x = 10;
  }
  
  // x is still accessible here
  console.log(x);
  
  // Redeclaration of variable
  var x = 20;
  
  // Using var in for loops causes closure issues
  for (var i = 0; i < 5; i++) {
    setTimeout(function() {
      console.log(i); // Will print 5 five times
    }, 100);
  }
}

// Async function without proper error handling
async function fetchUserData(userId) {
  // No try/catch for async/await
  const response = await fetch(`${API_URL}/users/${userId}`);
  const data = await response.json();
  
  return data;
}

// IIFE without proper semicolon before it
// This can cause issues with automatic semicolon insertion
(function() {
  console.log('Self-executing function');
})();

// Object with duplicate keys
const settings = {
  theme: 'dark',
  fontSize: 14,
  theme: 'light' // Duplicate key
};

// Switch statement without default case
function getStatusText(status) {
  switch(status) {
    case 200:
      return 'OK';
    case 404:
      return 'Not Found';
    case 500:
      return 'Server Error';
    // Missing default case
  }
}

// Main execution block with issues
(function main() {
  const data = [
    { id: 1, name: 'Item 1' },
    { id: 2, name: 'Item 2' },
    { id: 3, name: 'Item 3' }
  ];
  
  // Calling function with wrong number of arguments
  processData(data);
  
  // Unused variable
  const processedData = data.map(processItem);
  
  // Magic string (hardcoded file path)
  Export_data(data, '/data/output.json');
  
  console.log('Processing complete');
  
  // Unreachable code
  return;
  console.log('This will never be executed');
})();
// Unused imports
import React from 'react';
import moment from 'moment';
import axios from 'axios';
import _ from 'lodash';

// Global variables (should be constants)
var API_URL = 'https://api.example.com';
var MAX_RETRIES = 3;

// Missing semicolons
const USERNAME = 'admin'
const PASSWORD = 'password' // Hardcoded credentials (security issue)

// Unused variable
let retryCount = 0;

// Inconsistent spacing and indentation
function processData(data,options)
{
  // Unused parameter
  const { format, timeout, verbose } = options || {};
  
  // Using == instead of ===
  if (data == null) {
    return [];
  }
  
  // Inconsistent quotes (mix of single and double)
  console.log("Processing data...");
  
  // Variable shadowing (data shadows parameter)
  let data = [];
  
  try {
    // No-op empty block
    if (format === 'json') {
      
    }
    
    // Unreachable code (after return)
    return data;
    console.log('This will never be executed');
  } catch(e) {
    // Using console.log for errors instead of console.error
    console.log('Error processing data:', e);
  }
}

// Function declared but never used
function formatDate(date) {
  // Using deprecated Date methods
  return date.getMonth() + '/' + date.getDate() + '/' + date.getYear();
}

// Inconsistent function style (mix of declarations and expressions)
const fetchData = function(url) {
  // No error handling for fetch
  return fetch(url)
    .then(response => response.json())
    .then(data => {
      // Reassigning parameter (bad practice)
      url = null;
      return data;
    });
}

// Arrow function with unnecessary return and curly braces
const processItem = (item) => {
  return { 
    id: item.id, 
    name: item.name 
  };
};

// Function with too many parameters
function queryDatabase(table, columns, whereClause, orderBy, limit, ascending, groupBy, having) {
  // String concatenation for SQL (SQL injection risk)
  let query = "SELECT " + columns.join(",") + " FROM " + table;
  
  if (whereClause) {
    query += " WHERE " + whereClause;
  }
  
  // Duplicate code blocks (similar to above)
  if (orderBy) {
    query += " ORDER BY " + orderBy + (ascending ? " ASC" : " DESC");
  }
  
  if (limit > 0) {
    query += " LIMIT " + limit;
  }
  
  // Nested callbacks (callback hell)
  return new Promise((resolve, reject) => {
    const db = openDatabase();
    db.query(query, (err, results) => {
      if (err) {
        console.log('Database error:', err);
        reject(err);
      } else {
        db.close((closeErr) => {
          if (closeErr) {
            console.log('Error closing database:', closeErr);
          }
          resolve(results);
        });
      }
    });
  });
}

// Function name doesn't follow camelCase convention
function Export_data(data, outputPath) {
  try {
    // Potential null reference
    if (data.length > 0) {
      // Resource not properly closed
      const file = openFile(outputPath);
      
      // Inefficient loop (forEach would be better)
      for (let i = 0; i < data.length; i++) {
        writeToFile(file, data[i] + "\n");
      }
      
      closeFile(file);
    }
  } catch (e) {
    // Swallowing exception (only logging, not rethrowing)
    console.log('Export failed:', e.message);
  }
}

// Complex function with high cyclomatic complexity
function validateData(data) {
  if (data === null) {
    return false;
  }
  
  if (data.length < 5) {
    return false;
  }
  
  if (data.startsWith('TEST_')) {
    return true;
  }
  
  if (data.endsWith('_VALID')) {
    return true;
  }
  
  if (data.includes('APPROVED')) {
    return true;
  }
  
  const firstChar = data.charAt(0);
  if (firstChar === firstChar.toUpperCase()) {
    const lastChar = data.charAt(data.length - 1);
    if (!isNaN(parseInt(lastChar))) {
      return true;
    }
  }
  
  try {
    parseInt(data);
    return false;
  } catch (e) {
    // Empty catch block (swallowing exception)
  }
  
  // Inconsistent return style (some returns above, some below)
  if (/^[a-zA-Z0-9_]+$/.test(data)) {
    return true;
  } else {
    return false;
  }
}

// Object with mixed property shorthand and non-shorthand
const config = {
  apiUrl: API_URL,
  timeout: 30000,
  retries: MAX_RETRIES,
  verbose: true,
  debug: false,
  logLevel: 'info'
};

// Class with static methods (utility class should be a module with exported functions)
class DateUtils {
  // Missing constructor
  
  static formatDate(date) {
    // Using non-standard Date manipulation
    return date.getFullYear() + '-' + (date.getMonth() + 1) + '-' + date.getDate();
  }
  
  // Unused method parameter
  static isWeekend(date, includeHolidays) {
    const day = date.getDay();
    return day === 0 || day === 6;
  }
}

// Using var for function scoping issues
function scopeIssues() {
  // Variables declared with var are function-scoped, not block-scoped
  if (true) {
    var x = 10;
  }
  
  // x is still accessible here
  console.log(x);
  
  // Redeclaration of variable
  var x = 20;
  
  // Using var in for loops causes closure issues
  for (var i = 0; i < 5; i++) {
    setTimeout(function() {
      console.log(i); // Will print 5 five times
    }, 100);
  }
}

// Async function without proper error handling
async function fetchUserData(userId) {
  // No try/catch for async/await
  const response = await fetch(`${API_URL}/users/${userId}`);
  const data = await response.json();
  
  return data;
}

// IIFE without proper semicolon before it
// This can cause issues with automatic semicolon insertion
(function() {
  console.log('Self-executing function');
})();

// Object with duplicate keys
const settings = {
  theme: 'dark',
  fontSize: 14,
  theme: 'light' // Duplicate key
};

// Switch statement without default case
function getStatusText(status) {
  switch(status) {
    case 200:
      return 'OK';
    case 404:
      return 'Not Found';
    case 500:
      return 'Server Error';
    // Missing default case
  }
}
// Unused imports
import React from 'react';
import moment from 'moment';
import axios from 'axios';
import _ from 'lodash';

// Global variables (should be constants)
var API_URL = 'https://api.example.com';
var MAX_RETRIES = 3;

// Missing semicolons
const USERNAME = 'admin'
const PASSWORD = 'password' // Hardcoded credentials (security issue)

// Unused variable
let retryCount = 0;

// Inconsistent spacing and indentation
function processData(data,options)
{
  // Unused parameter
  const { format, timeout, verbose } = options || {};
  
  // Using == instead of ===
  if (data == null) {
    return [];
  }
  
  // Inconsistent quotes (mix of single and double)
  console.log("Processing data...");
  
  // Variable shadowing (data shadows parameter)
  let data = [];
  
  try {
    // No-op empty block
    if (format === 'json') {
      
    }
    
    // Unreachable code (after return)
    return data;
    console.log('This will never be executed');
  } catch(e) {
    // Using console.log for errors instead of console.error
    console.log('Error processing data:', e);
  }
}

// Function declared but never used
function formatDate(date) {
  // Using deprecated Date methods
  return date.getMonth() + '/' + date.getDate() + '/' + date.getYear();
}

// Inconsistent function style (mix of declarations and expressions)
const fetchData = function(url) {
  // No error handling for fetch
  return fetch(url)
    .then(response => response.json())
    .then(data => {
      // Reassigning parameter (bad practice)
      url = null;
      return data;
    });
}

// Arrow function with unnecessary return and curly braces
const processItem = (item) => {
  return { 
    id: item.id, 
    name: item.name 
  };
};

// Function with too many parameters
function queryDatabase(table, columns, whereClause, orderBy, limit, ascending, groupBy, having) {
  // String concatenation for SQL (SQL injection risk)
  let query = "SELECT " + columns.join(",") + " FROM " + table;
  
  if (whereClause) {
    query += " WHERE " + whereClause;
  }
  
  // Duplicate code blocks (similar to above)
  if (orderBy) {
    query += " ORDER BY " + orderBy + (ascending ? " ASC" : " DESC");
  }
  
  if (limit > 0) {
    query += " LIMIT " + limit;
  }
  
  // Nested callbacks (callback hell)
  return new Promise((resolve, reject) => {
    const db = openDatabase();
    db.query(query, (err, results) => {
      if (err) {
        console.log('Database error:', err);
        reject(err);
      } else {
        db.close((closeErr) => {
          if (closeErr) {
            console.log('Error closing database:', closeErr);
          }
          resolve(results);
        });
      }
    });
  });
}

// Function name doesn't follow camelCase convention
function Export_data(data, outputPath) {
  try {
    // Potential null reference
    if (data.length > 0) {
      // Resource not properly closed
      const file = openFile(outputPath);
      
      // Inefficient loop (forEach would be better)
      for (let i = 0; i < data.length; i++) {
        writeToFile(file, data[i] + "\n");
      }
      
      closeFile(file);
    }
  } catch (e) {
    // Swallowing exception (only logging, not rethrowing)
    console.log('Export failed:', e.message);
  }
}

// Complex function with high cyclomatic complexity
function validateData(data) {
  if (data === null) {
    return false;
  }
  
  if (data.length < 5) {
    return false;
  }
  
  if (data.startsWith('TEST_')) {
    return true;
  }
  
  if (data.endsWith('_VALID')) {
    return true;
  }
  
  if (data.includes('APPROVED')) {
    return true;
  }
  
  const firstChar = data.charAt(0);
  if (firstChar === firstChar.toUpperCase()) {
    const lastChar = data.charAt(data.length - 1);
    if (!isNaN(parseInt(lastChar))) {
      return true;
    }
  }
  
  try {
    parseInt(data);
    return false;
  } catch (e) {
    // Empty catch block (swallowing exception)
  }
  
  // Inconsistent return style (some returns above, some below)
  if (/^[a-zA-Z0-9_]+$/.test(data)) {
    return true;
  } else {
    return false;
  }
}

// Object with mixed property shorthand and non-shorthand
const config = {
  apiUrl: API_URL,
  timeout: 30000,
  retries: MAX_RETRIES,
  verbose: true,
  debug: false,
  logLevel: 'info'
};

// Class with static methods (utility class should be a module with exported functions)
class DateUtils {
  // Missing constructor
  
  static formatDate(date) {
    // Using non-standard Date manipulation
    return date.getFullYear() + '-' + (date.getMonth() + 1) + '-' + date.getDate();
  }
  
  // Unused method parameter
  static isWeekend(date, includeHolidays) {
    const day = date.getDay();
    return day === 0 || day === 6;
  }
}

// Using var for function scoping issues
function scopeIssues() {
  // Variables declared with var are function-scoped, not block-scoped
  if (true) {
    var x = 10;
  }
  
  // x is still accessible here
  console.log(x);
  
  // Redeclaration of variable
  var x = 20;
  
  // Using var in for loops causes closure issues
  for (var i = 0; i < 5; i++) {
    setTimeout(function() {
      console.log(i); // Will print 5 five times
    }, 100);
  }
}

// Async function without proper error handling
async function fetchUserData(userId) {
  // No try/catch for async/await
  const response = await fetch(`${API_URL}/users/${userId}`);
  const data = await response.json();
  
  return data;
}

// IIFE without proper semicolon before it
// This can cause issues with automatic semicolon insertion
(function() {
  console.log('Self-executing function');
})();

// Object with duplicate keys
const settings = {
  theme: 'dark',
  fontSize: 14,
  theme: 'light' // Duplicate key
};

// Switch statement without default case
function getStatusText(status) {
  switch(status) {
    case 200:
      return 'OK';
    case 404:
      return 'Not Found';
    case 500:
      return 'Server Error';
    // Missing default case
  }
}

// Main execution block with issues
(function main() {
  const data = [
    { id: 1, name: 'Item 1' },
    { id: 2, name: 'Item 2' },
    { id: 3, name: 'Item 3' }
  ];
  
  // Calling function with wrong number of arguments
  processData(data);
  
  // Unused variable
  const processedData = data.map(processItem);
  
  // Magic string (hardcoded file path)
  Export_data(data, '/data/output.json');
  
  console.log('Processing complete');
  
  // Unreachable code
  return;
  console.log('This will never be executed');
})();
// Unused imports
import React from 'react';
import moment from 'moment';
import axios from 'axios';
import _ from 'lodash';

// Global variables (should be constants)
var API_URL = 'https://api.example.com';
var MAX_RETRIES = 3;

// Missing semicolons
const USERNAME = 'admin'
const PASSWORD = 'password' // Hardcoded credentials (security issue)

// Unused variable
let retryCount = 0;

// Inconsistent spacing and indentation
function processData(data,options)
{
  // Unused parameter
  const { format, timeout, verbose } = options || {};
  
  // Using == instead of ===
  if (data == null) {
    return [];
  }
  
  // Inconsistent quotes (mix of single and double)
  console.log("Processing data...");
  
  // Variable shadowing (data shadows parameter)
  let data = [];
  
  try {
    // No-op empty block
    if (format === 'json') {
      
    }
    
    // Unreachable code (after return)
    return data;
    console.log('This will never be executed');
  } catch(e) {
    // Using console.log for errors instead of console.error
    console.log('Error processing data:', e);
  }
}

// Function declared but never used
function formatDate(date) {
  // Using deprecated Date methods
  return date.getMonth() + '/' + date.getDate() + '/' + date.getYear();
}

// Inconsistent function style (mix of declarations and expressions)
const fetchData = function(url) {
  // No error handling for fetch
  return fetch(url)
    .then(response => response.json())
    .then(data => {
      // Reassigning parameter (bad practice)
      url = null;
      return data;
    });
}

// Arrow function with unnecessary return and curly braces
const processItem = (item) => {
  return { 
    id: item.id, 
    name: item.name 
  };
};

// Function with too many parameters
function queryDatabase(table, columns, whereClause, orderBy, limit, ascending, groupBy, having) {
  // String concatenation for SQL (SQL injection risk)
  let query = "SELECT " + columns.join(",") + " FROM " + table;
  
  if (whereClause) {
    query += " WHERE " + whereClause;
  }
  
  // Duplicate code blocks (similar to above)
  if (orderBy) {
    query += " ORDER BY " + orderBy + (ascending ? " ASC" : " DESC");
  }
  
  if (limit > 0) {
    query += " LIMIT " + limit;
  }
  
  // Nested callbacks (callback hell)
  return new Promise((resolve, reject) => {
    const db = openDatabase();
    db.query(query, (err, results) => {
      if (err) {
        console.log('Database error:', err);
        reject(err);
      } else {
        db.close((closeErr) => {
          if (closeErr) {
            console.log('Error closing database:', closeErr);
          }
          resolve(results);
        });
      }
    });
  });
}

// Function name doesn't follow camelCase convention
function Export_data(data, outputPath) {
  try {
    // Potential null reference
    if (data.length > 0) {
      // Resource not properly closed
      const file = openFile(outputPath);
      
      // Inefficient loop (forEach would be better)
      for (let i = 0; i < data.length; i++) {
        writeToFile(file, data[i] + "\n");
      }
      
      closeFile(file);
    }
  } catch (e) {
    // Swallowing exception (only logging, not rethrowing)
    console.log('Export failed:', e.message);
  }
}

// Complex function with high cyclomatic complexity
function validateData(data) {
  if (data === null) {
    return false;
  }
  
  if (data.length < 5) {
    return false;
  }
  
  if (data.startsWith('TEST_')) {
    return true;
  }
  
  if (data.endsWith('_VALID')) {
    return true;
  }
  
  if (data.includes('APPROVED')) {
    return true;
  }
  
  const firstChar = data.charAt(0);
  if (firstChar === firstChar.toUpperCase()) {
    const lastChar = data.charAt(data.length - 1);
    if (!isNaN(parseInt(lastChar))) {
      return true;
    }
  }
  
  try {
    parseInt(data);
    return false;
  } catch (e) {
    // Empty catch block (swallowing exception)
  }
  
  // Inconsistent return style (some returns above, some below)
  if (/^[a-zA-Z0-9_]+$/.test(data)) {
    return true;
  } else {
    return false;
  }
}

// Object with mixed property shorthand and non-shorthand
const config = {
  apiUrl: API_URL,
  timeout: 30000,
  retries: MAX_RETRIES,
  verbose: true,
  debug: false,
  logLevel: 'info'
};

// Class with static methods (utility class should be a module with exported functions)
class DateUtils {
  // Missing constructor
  
  static formatDate(date) {
    // Using non-standard Date manipulation
    return date.getFullYear() + '-' + (date.getMonth() + 1) + '-' + date.getDate();
  }
  
  // Unused method parameter
  static isWeekend(date, includeHolidays) {
    const day = date.getDay();
    return day === 0 || day === 6;
  }
}

// Using var for function scoping issues
function scopeIssues() {
  // Variables declared with var are function-scoped, not block-scoped
  if (true) {
    var x = 10;
  }
  
  // x is still accessible here
  console.log(x);
  
  // Redeclaration of variable
  var x = 20;
  
  // Using var in for loops causes closure issues
  for (var i = 0; i < 5; i++) {
    setTimeout(function() {
      console.log(i); // Will print 5 five times
    }, 100);
  }
}

// Async function without proper error handling
async function fetchUserData(userId) {
  // No try/catch for async/await
  const response = await fetch(`${API_URL}/users/${userId}`);
  const data = await response.json();
  
  return data;
}

// IIFE without proper semicolon before it
// This can cause issues with automatic semicolon insertion
(function() {
  console.log('Self-executing function');
})();

// Object with duplicate keys
const settings = {
  theme: 'dark',
  fontSize: 14,
  theme: 'light' // Duplicate key
};

// Switch statement without default case
function getStatusText(status) {
  switch(status) {
    case 200:
      return 'OK';
    case 404:
      return 'Not Found';
    case 500:
      return 'Server Error';
    // Missing default case
  }
}

// Main execution block with issues
(function main() {
  const data = [
    { id: 1, name: 'Item 1' },
    { id: 2, name: 'Item 2' },
    { id: 3, name: 'Item 3' }
  ];
  
  // Calling function with wrong number of arguments
  processData(data);
  
  // Unused variable
  const processedData = data.map(processItem);
  
  // Magic string (hardcoded file path)
  Export_data(data, '/data/output.json');
  
  console.log('Processing complete');
  
  // Unreachable code
  return;
  console.log('This will never be executed');
})();

// Main execution block with issues
(function main() {
  const data = [
    { id: 1, name: 'Item 1' },
    { id: 2, name: 'Item 2' },
    { id: 3, name: 'Item 3' }
  ];
  
  // Calling function with wrong number of arguments
  processData(data);
  
  // Unused variable
  const processedData = data.map(processItem);
  
  // Magic string (hardcoded file path)
  Export_data(data, '/data/output.json');
  
  console.log('Processing complete');
  
  // Unreachable code
  return;
  console.log('This will never be executed');
})();
