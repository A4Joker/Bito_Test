package com.example.service;

import java.util.Map;

public class ProcessServiceImpl implements ProcessService {
    @Override
    public Map<String, Object> healthCheck(String workspaceUserId) throws ProcessException {
        return Map.of();
    }

    /**
     * Retrieves information about a process for the specified workspace user.
     *
     * @param workspaceUserId The unique identifier for the workspace user
     * @return Map containing process information
     * @throws ProcessException if the information cannot be retrieved
     */
    @Override
    public Map<String, Object> getInfo(String workspaceUserId) throws ProcessException {
        return Map.of();
    }
        return Map.of();
    }
        return startProcess(workspaceUserId, configParam.getProjectId());
    }
}
