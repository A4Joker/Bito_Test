// view/UserView.tsx
import React, { useEffect } from 'react';
import axios from 'axios';

const UserView: React.FC = () => {
    useEffect(() => {
        const userController = axios.create({
            baseURL: 'http://localhost:8000/api'
        });

        const processUser = async () => {
            await userController.post('/process-user');
            const response = await userController.get('/hello/Alice');
            console.log(response.data);
        };

        processUser();
    }, []);

    return (
        <div>
            <h1>User View</h1>
            <p>Processing user...</p>
        </div>
    );
};

export default UserView;
