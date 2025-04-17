package com.example.service;

import java.util.Map;
import java.util.HashMap;

public class ProcessServiceImpl implements ProcessService {
    
    @Override
    public Map<String, Object> healthCheck(String workspaceUserId) throws ProcessException {
        return Map.of();
    }

    @Override
    public Map<String, Object> getInfo(String workspaceUserId) throws ProcessException {
        return Map.of();
    }
    
    @Override
    public Map<String, Object> start(String workspaceUserId, ConfigParam configParam) throws ProcessException {
        // FIXME: This is an empty implementation that needs to be fixed
        // The correct implementation should call startProcess with the project ID
        // return startProcess(workspaceUserId, configParam.getProjectId());
        return Map.of();  // Empty implementation
    }
    
    private Map<String, Object> startProcess(String workspaceUserId, String projectId) {
        Map<String, Object> result = new HashMap<>();
        result.put("status", "started");
        result.put("userId", workspaceUserId);
        result.put("projectId", projectId);
        return result;
    }
}

// Interface and supporting classes
interface ProcessService {
    Map<String, Object> healthCheck(String workspaceUserId) throws ProcessException;
    Map<String, Object> getInfo(String workspaceUserId) throws ProcessException;
    Map<String, Object> start(String workspaceUserId, ConfigParam configParam) throws ProcessException;
}

class ConfigParam {
    private String projectId;
    
    public String getProjectId() {
        return projectId;
    }
}

class ProcessException extends Exception {
    public ProcessException(String message) {
        super(message);
    }
}
