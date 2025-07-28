import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';


import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

// Multiple empty lines


interface User {

    name: string;

    age: number;

    email?: string;

}


// Class with inconsistent empty lines
export class EmptyLineIssues {


    private users: User[] = [];

    private isLoading: boolean = false;


    constructor(private http: HttpClient) {

        this.initializeData();

    }


    // Method with excessive empty lines
    public processData(): void {


        const items: string[] = ['item1', 'item2', 'item3'];


        items.forEach(item => {


            console.log(item);


        });


    }

    // Another method with inconsistent spacing
    public getName(): string {

        return this.users[0]?.name || '';

    }


    public setName(name: string): void {


        if (this.users.length > 0) {

            this.users[0].name = name;

        }


    }


    // Method with empty lines in wrong places
    public complexMethod(): Observable<any> {
        if (this.users.length > 0) {

            console.log('Users exist');

        } else {

            console.log('No users found');

        }


        return this.http.get('/api/users').pipe(

            map(response => {

                return response;

            })

        );


    }


    // Private method with spacing issues
    private initializeData(): void {


        this.users = [

            { name: 'John', age: 30 },

            { name: 'Jane', age: 25 }

        ];


        this.isLoading = false;


    }


    // Method with inconsistent arrow function spacing
    public filterUsers = (minAge: number): User[] => {


        return this.users.filter(user => {

            return user.age >= minAge;

        });


    }


}


// Function outside class with spacing issues
export function utilityFunction(): string {


    const data = { message: 'Hello World' };


    return JSON.stringify(data);


}


// Multiple empty lines at end of file
