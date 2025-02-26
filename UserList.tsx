import React, { useState, useEffect } from 'react';
import { User, UserService } from './UserService';

interface UserListProps {
    title: string;
}

const UserList: React.FC<UserListProps> = ({ title }) => {
    const [users, setUsers] = useState<User[]>([]);
    const userService = new UserService();

    useEffect(() => {
        const activeUsers = userService.getActiveUsers();
        setUsers(activeUsers);
    }, []);

    const handleToggleStatus = (userId: number) => {
        const updatedUser = userService.toggleUserStatus(userId);
        if (updatedUser) {
            setUsers(userService.getActiveUsers());
        }
    };

    return (
        <div className="user-list">
            <h2>{title}</h2>
            {users.map(user => (
                <div key={user.id} className="user-item">
                    <span>{user.name} ({user.email})</span>
                    <button onClick={() => handleToggleStatus(user.id)}>
                        Toggle Status
                    </button>
                </div>
            ))}
        </div>
    );
};

export default UserList;
