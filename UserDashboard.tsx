import React, { useState, useEffect } from 'react';
import axios from 'axios';

// Interface declarations that other parts depend on
interface User {
    id: number;
    name: string;
    email: string;
    role: string;
}

// Main component with internal dependencies
const UserDashboard: React.FC = () => {
    const [users, setUsers] = useState<User[]>([]);
    const [loading, setLoading] = useState(true);

    // This function is depended upon by the useEffect and return section
    const fetchUsers = async () => {
        try {
            const response = await axios.get<User[]>('http://localhost:8000/api/users');
            setUsers(response.data);
            setLoading(false);
        } catch (err) {
            console.error('Failed to fetch users');
            setLoading(false);
        }
    };

    // useEffect depends on fetchUsers
    useEffect(() => {
        fetchUsers();
    }, []);

    // Return section is impacted by the state and fetchUsers
    return (
        <div className="dashboard">
            <h1>User Dashboard</h1>
            {loading ? (
                <div>Loading...</div>
            ) : (
                <div className="user-list">
                    {users.map(user => (
                        <div key={user.id} className="user-card">
                            <h3>{user.name}</h3>
                            <p>Email: {user.email}</p>
                            <p>Role: {user.role}</p>
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
};

export default UserDashboard;
