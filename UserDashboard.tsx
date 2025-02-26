import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { SystemConfig, ApiStatus } from './config.types';

const SystemStatus: React.FC = () => {
    const [systemConfig, setSystemConfig] = useState<SystemConfig | null>(null);
    const [apiStatus, setApiStatus] = useState<ApiStatus | null>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState('');

    // This function depends on Python backend's system-config endpoint
    const fetchSystemConfig = async () => {
        try {
            const response = await axios.get<SystemConfig>('http://localhost:8000/api/system-config');
            setSystemConfig(response.data);
        } catch (err) {
            setError('Failed to fetch system configuration');
        }
    };

    // This function depends on Python backend's status endpoint
    const fetchApiStatus = async () => {
        try {
            const response = await axios.get<ApiStatus>('http://localhost:8000/api/status');
            setApiStatus(response.data);
            setLoading(false);
        } catch (err) {
            setError('Failed to fetch API status');
            setLoading(false);
        }
    };

    useEffect(() => {
        // Fetch both system config and API status on component mount
        Promise.all([fetchSystemConfig(), fetchApiStatus()]);

        // Set up polling for API status every 30 seconds
        const statusInterval = setInterval(fetchApiStatus, 30000);
        return () => clearInterval(statusInterval);
    }, []);

    if (loading) return <div>Loading system status...</div>;
    if (error) return <div>Error: {error}</div>;

    return (
        <div className="system-status">
            <h2>System Status Dashboard</h2>
            
            {systemConfig && (
                <div className="config-info">
                    <h3>System Configuration</h3>
                    <p>Python Version: {systemConfig.pythonVersion}</p>
                    <p>API Version: {systemConfig.apiVersion}</p>
                    <p>Last Updated: {new Date(systemConfig.lastUpdated).toLocaleString()}</p>
                    <div>
                        <h4>Enabled Features:</h4>
                        <ul>
                            {systemConfig.features.map(feature => (
                                <li key={feature}>{feature}</li>
                            ))}
                        </ul>
                    </div>
                </div>
            )}

            {apiStatus && (
                <div className="api-status">
                    <h3>API Status</h3>
                    <p>Status: <span className={apiStatus.status}>{apiStatus.status}</span></p>
                    <p>Last Check: {new Date(apiStatus.timestamp).toLocaleString()}</p>
                    <p>Version: {apiStatus.version}</p>
                </div>
            )}
        </div>
    );
};

export default SystemStatus;
