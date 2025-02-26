import React, { useState, useEffect } from 'react';
import axios from 'axios';
import configData from './config.json';

interface User {
    id: number;
    name: string;
    email: string;
    role: string;
}

interface ClientConfig {
    clientVersion: string;
    lastAccessed: string;
    settings: {
        theme: string;
        language: string;
    }
}

const UserDashboard: React.FC = () => {
    const [users, setUsers] = useState<User[]>([]);
    const [clientConfig, setClientConfig] = useState<ClientConfig>({
        clientVersion: '1.0',
        lastAccessed: new Date().toISOString(),
        settings: {
            theme: 'light',
            language: 'en'
        }
    });

    const updateServerConfig = async () => {
        try {
            await axios.post('http://localhost:8000/api/client-config', clientConfig);
        } catch (err) {
            console.error('Failed to update server config');
        }
    };

    useEffect(() => {
        // Update server with client config on mount
        updateServerConfig();
        
        // Fetch users
        const fetchUsers = async () => {
            try {
                const response = await axios.get(
                    `http://localhost:8000${configData.endpoints.users}`
                );
                setUsers(response.data);
            } catch (err) {
                console.error('Failed to fetch users');
            }
        };
        
        fetchUsers();
    }, []);

    return (
        <div className={`dashboard ${clientConfig.settings.theme}`}>
            <h1>User Dashboard</h1>
            <div className="user-list">
                {users.map(user => (
                    <div key={user.id} className="user-card">
                        <h3>{user.name}</h3>
                        <p>Email: {user.email}</p>
                        <p>Role: {user.role}</p>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default UserDashboard;
