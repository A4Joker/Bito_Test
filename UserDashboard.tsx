import React, { useState, useEffect } from 'react';
import axios from 'axios';

interface User {
    id: number;
    name: string;
    email: string;
    role: string;
}

interface UIConfig {
    theme: string;
    pageSize: number;
    features: string[];
}

const UserDashboard: React.FC = () => {
    const [users, setUsers] = useState<User[]>([]);
    const [config, setConfig] = useState<UIConfig | null>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState('');

    // First dependency: Fetch UI configuration from Python backend
    const fetchConfig = async () => {
        try {
            const response = await axios.get<UIConfig>('http://localhost:8000/api/config');
            setConfig(response.data);
        } catch (err) {
            setError('Failed to fetch configuration');
        }
    };

    // Second dependency: Fetch users data
    const fetchUsers = async () => {
        try {
            const response = await axios.get<User[]>('http://localhost:8000/api/users');
            setUsers(response.data);
            setLoading(false);
        } catch (err) {
            setError('Failed to fetch users');
            setLoading(false);
        }
    };

    // Third dependency: Update theme
    const updateTheme = async (newTheme: string) => {
        try {
            await axios.post('http://localhost:8000/api/config/theme', { theme: newTheme });
            await fetchConfig(); // Refresh config after update
        } catch (err) {
            setError('Failed to update theme');
        }
    };

    useEffect(() => {
        // Load both configuration and users data on component mount
        Promise.all([fetchConfig(), fetchUsers()]);
    }, []);

    if (loading || !config) return <div>Loading...</div>;
    if (error) return <div>Error: {error}</div>;

    return (
        <div className={`dashboard ${config.theme}`}>
            <div className="dashboard-header">
                <h1>User Dashboard</h1>
                <button onClick={() => updateTheme(config.theme === 'light' ? 'dark' : 'light')}>
                    Toggle Theme
                </button>
            </div>
            
            <div className="features-list">
                <h3>Enabled Features:</h3>
                <ul>
                    {config.features.map(feature => (
                        <li key={feature}>{feature}</li>
                    ))}
                </ul>
            </div>

            <div className="user-list">
                {users.slice(0, config.pageSize).map(user => (
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
