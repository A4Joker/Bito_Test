import React, { useState, useEffect } from 'react';
import axios from 'axios';

interface User {
    id: number;
    name: string;
    email: string;
    role: string;
}

const UserDashboard: React.FC = () => {
    const [users, setUsers] = useState<User[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState('');

    // Dependency: This function calls the Python FastAPI endpoint
    const fetchUsers = async () => {
        try {
            const response = await axios.get('http://localhost:8000/api/users');
            setUsers(response.data);
            setLoading(false);
        } catch (err) {
            setError('Failed to fetch users');
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchUsers();
    }, []);

    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error}</div>;

    return (
        <div className="dashboard">
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
