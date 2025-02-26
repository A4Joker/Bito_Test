export interface User {
    id: number;
    name: string;
    email: string;
    isActive: boolean;
}

export class UserService {
    private users: User[] = [
        { id: 1, name: 'John Doe', email: 'john@example.com', isActive: true },
        { id: 2, name: 'Jane Smith', email: 'jane@example.com', isActive: false }
    ];

    public getActiveUsers(): User[] {
        return this.users.filter(user => user.isActive);
    }

    public toggleUserStatus(userId: number): User | undefined {
        const user = this.users.find(u => u.id === userId);
        if (user) {
            user.isActive = !user.isActive;
            return user;
        }
        return undefined;
    }
}
