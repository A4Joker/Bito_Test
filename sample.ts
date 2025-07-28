import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import * as fs from 'fs';
import { exec } from 'child_process';

// CRITICAL: Hardcoded credentials
const API_KEY = 'sk-1234567890abcdef';
const DATABASE_PASSWORD = 'admin123';

@Injectable()
export class CriticalIssues {
    
    constructor(private http: HttpClient) {}
    
    // CRITICAL: SQL Injection vulnerability
    findUser(username: string): Promise<any> {
        // Direct string interpolation in SQL - SQL injection risk
        const query = `SELECT * FROM users WHERE username = '${username}'`;
        return this.http.post('/api/query', { sql: query }).toPromise();
    }
    
    // CRITICAL: Command injection vulnerability
    executeCommand(userInput: string): void {
        // Direct execution of user input - command injection risk
        exec(`ls -la ${userInput}`, (error, stdout, stderr) => {
            console.log(stdout);
        });
    }
    
    // CRITICAL: Null/undefined dereference
    processUser(user: any): void {
        // No null/undefined check before accessing properties
        console.log(`Processing user: ${user.name}`);
        console.log(`Email: ${user.email.toLowerCase()}`);
        
        // CRITICAL: Potential array index error
        const parts = user.email.split('@');
        console.log(`Domain: ${parts[1]}`); // No check if parts.length > 1
    }
    
    // CRITICAL: Unsafe eval usage
    calculateExpression(expression: string): any {
        // Direct eval of user input - code injection risk
        return eval(expression);
    }
    
    // CRITICAL: Unsafe innerHTML usage
    renderUserContent(content: string): void {
        // XSS vulnerability - direct innerHTML assignment
        document.getElementById('content')!.innerHTML = content;
    }
    
    // CRITICAL: Infinite loop potential
    processData(data: string[]): void {
        let i = 0;
        while (i < data.length) {
            const item = data[i];
            if (item.includes('skip')) {
                // Missing i++ increment - infinite loop
                continue;
            }
            console.log(item);
            i++;
        }
    }
    
    // CRITICAL: Exception swallowing
    async riskyOperation(): Promise<void> {
        try {
            // Some risky async operation
            await this.http.get('/api/risky').toPromise();
            throw new Error('Something went wrong');
        } catch (error) {
            // Swallowing exception without logging
        }
    }
    
    // CRITICAL: Weak random number generation
    generateToken(): string {
        return Math.random().toString(36).substring(7);
    }
    
    // CRITICAL: Path traversal vulnerability
    readFile(filename: string): string {
        // No validation of filename - path traversal risk
        const filePath = `/app/data/${filename}`;
        return fs.readFileSync(filePath, 'utf8');
    }
    
    // CRITICAL: Unsafe deserialization
    deserializeData(data: string): any {
        // Parsing JSON without validation
        return JSON.parse(data);
    }
    
    // CRITICAL: Race condition with shared state
    private static counter = 0;
    incrementCounter(): void {
        // Non-atomic operation on shared variable
        CriticalIssues.counter = CriticalIssues.counter + 1;
    }
    
    // CRITICAL: Memory leak potential
    private static cache = new Map<string, any>();
    addToCache(key: string, value: any): void {
        // Adding to static cache without cleanup
        CriticalIssues.cache.set(key, value);
    }
    
    // CRITICAL: Unsafe redirect
    redirectUser(url: string): void {
        // No validation of redirect URL
        window.location.href = url;
    }
    
    // CRITICAL: Local storage of sensitive data
    storeSensitiveData(token: string, password: string): void {
        // Storing sensitive data in local storage
        localStorage.setItem('authToken', token);
        localStorage.setItem('userPassword', password);
    }
    
    // CRITICAL: CORS misconfiguration
    setupCORS(): void {
        // Overly permissive CORS setup
        this.http.post('/api/cors', {
            origin: '*',
            credentials: true,
            methods: ['GET', 'POST', 'PUT', 'DELETE']
        });
    }
    
    // CRITICAL: Prototype pollution
    mergeObjects(target: any, source: any): any {
        // Unsafe object merging - prototype pollution risk
        for (const key in source) {
            target[key] = source[key];
        }
        return target;
    }
    
    // CRITICAL: Using any type everywhere
    processAnyData(data: any): any {
        // Excessive use of 'any' type - no type safety
        return data.someProperty.anotherProperty.deepProperty;
    }
}

// CRITICAL: Global variables
var globalPassword = 'secret123';
var globalApiKey = 'api-key-12345';

// CRITICAL: Function without proper error handling
function unsafeFunction(input: any): any {
    // No error handling or type checking
    return input.property.nestedProperty.value;
}

// CRITICAL: Async function without proper error handling
async function unsafeAsyncFunction(url: string): Promise<any> {
    // No try/catch for async operation
    const response = await fetch(url);
    return response.json();
}
