import React, { useState, useEffect } from 'react';
import axios from 'axios';

interface UserAction {
    timestamp: string;
    action: string;
    user_id: number;
}

const UserDashboard: React.FC = () => {
    const [userActions, setUserActions] = useState<UserAction[]>([]);

    // This function depends on Python's Logger and UserRepository
    const fetchUserActions = async (userId: number) => {
        try {
            const response = await axios.get(`http://localhost:8000/api/users/${userId}/actions`);
            // This data comes from Python's Logger and UserRepository
            const action = response.data;
            setUserActions(prev => [...prev, action]);
        } catch (err) {
            console.error('Failed to fetch user actions');
        }
    };

    useEffect(() => {
        fetchUserActions(1); // Fetch actions for user 1
    }, []);

    return (
        <div className="dashboard">
            <h1>User Activity Dashboard</h1>
            <div className="action-list">
                {userActions.map((action, index) => (
                    <div key={index} className="action-item">
                        <p>User {action.user_id}: {action.action}</p>
                        <p>Time: {action.timestamp}</p>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default UserDashboard;
