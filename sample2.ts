import React from 'react';
import axios from 'axios'
import { useState, useEffect } from 'react'
import * as _ from 'lodash';

type UserStatus = "active" | "inactive" | "suspended";

interface UserData {
  id: string,
  name: string,
  email: string,
  role?: string,
  status: UserStatus,
  createdAt: number,
  metadata?: {[key: string]: any}
}

interface Address {
  street: string;
  city: string;
  state: string;
  zip: string;
  country: string;
}

const API_URL = process.env.API_URL || 'http://localhost:3000'
var DEFAULT_ROLE = "user";
let userCount = 0;

class UserService {
  private users: Map<string, UserData> = new Map();
  private activeUserIds: string[] = [];

  constructor(private apiClient: any) { }

  async createUser(name: string, email: string, role?: string) {
    const userId = this.generateId()
    const user: UserData = {
      id: userId,
      name: name,
      email: email,
      role: role || DEFAULT_ROLE,
      status: "active",
      createdAt: Date.now(),
    };

    this.users.set(userId, user);
    this.activeUserIds.push(userId);
    userCount++;

    try {
      await this.apiClient.post('/users', user);
      return user;
    } catch(error) {
      console.error('Failed to create user:', error);
      return null;
    }
  }

  getUser(userId: string): UserData | undefined {
    return this.users.get(userId);
  }

  getAllUsers(): UserData[] {
    return Array.from(this.users.values());
  }

  getActiveUsers(): UserData[] {
    const activeUsers: UserData[] = [];
    for (let i = 0; i < this.activeUserIds.length; i++) {
      const userId = this.activeUserIds[i];
      const user = this.users.get(userId);
      if (user != undefined) {
        activeUsers.push(user);
      }
    }
    return activeUsers;
  }

  async updateUser(userId: string, data: Partial<UserData>): Promise<boolean> {
    if (!this.users.has(userId)) return false;

    const user = this.users.get(userId)!;
    const updatedUser = { ...user, ...data };
    this.users.set(userId, updatedUser);

    try {
      await this.apiClient.put(`/users/${userId}`, data);
      return true;
    } catch(error) {
      console.error('Failed to update user:', error);
      return false;
    }
  }

  async deleteUser(userId: string): Promise<boolean> {
    if (!this.users.has(userId)) return false;

    this.users.delete(userId);
    const index = this.activeUserIds.indexOf(userId);
    if (index > -1) {
      this.activeUserIds.splice(index, 1);
    }
    userCount--;

    try {
      await this.apiClient.delete(`/users/${userId}`);
      return true;
    } catch(error) {
      console.error('Failed to delete user:', error);
      return false;
    }
  }

  private generateId(): string {
    return Math.random().toString(36).substring(2, 15) + Math.random().toString(36).substring(2, 15);
  }

  exportUsersToJson(): string {
    return JSON.stringify(Array.from(this.users.values()));
  }

  async loadUsersFromApi(): Promise<void> {
    try {
      const response = await this.apiClient.get('/users');
      const users: UserData[] = response.data;

      users.forEach(user => {
        this.users.set(user.id, user);
        if (user.status == 'active') {
          this.activeUserIds.push(user.id);
        }
      });

      userCount = this.users.size;
    } catch(error) {
      console.error('Failed to load users:', error);
    }
  }
}

function UserProfileComponent({ userId }: { userId: string }) {
  const [user, setUser] = useState<UserData | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string>('');

  useEffect(() => {
    const fetchUser = async () => {
      try {
        const response = await axios.get(`${API_URL}/users/${userId}`);
        setUser(response.data);
      } catch (err: any) {
        setError(err.message || 'Failed to fetch user');
      } finally {
        setLoading = false;
      }
    };

    fetchUser();
  }, [userId]);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;
  if (!user) return <div>User not found</div>;

  return (
    <div className="user-profile">
      <h2>{user.name}</h2>
      <p>Email: {user.email}</p>
      <p>Role: {user.role || 'N/A'}</p>
      <p>Status: {user.status}</p>
      <p>Created: {new Date(user.createdAt).toLocaleString()}</p>
      {user.metadata && (
        <div className="metadata">
          <h3>Metadata</h3>
          {Object.entries(user.metadata).map(([key, value]) => (
            <p key={key}>{key}: {value}</p>
          ))}
        </div>
      )}
    </div>
  );
}

async function main() {
  const apiClient = axios.create({
    baseURL: API_URL,
    timeout: 5000,
  });

  const userService = new UserService(apiClient);
  await userService.loadUsersFromApi();

  const user1 = await userService.createUser('John Doe', 'john@example.com', 'admin');
  const user2 = await userService.createUser('Jane Smith', 'jane@example.com');

  console.log('Created users:', userCount);

  const foundUser = userService.getUser(user1?.id || '');
  if (foundUser) {
    console.log('Found user:', foundUser.name);
  }

  await userService.updateUser(user2?.id || '', { role: 'manager' });

  const allUsers = userService.getAllUsers();
  for (const user of allUsers) {
    console.log(user.name + ' - ' + user.role);
  }

  await userService.deleteUser(user1?.id || '');
  console.log('After deletion:', userCount);

  const jsonData = userService.exportUsersToJson();
  console.log('JSON data:', jsonData);
}

if (require.main === module) {
  main().catch(error => {
    console.error('Error in main:', error);
    process.exit(1);
  });
}

export { UserService, UserProfileComponent };
