import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Map;

/**
 * This file demonstrates the CRA line range issue with a complete example.
 * It contains:
 * 1. The actual service implementation with multiple Map.of() returns
 * 2. A CRA simulator that generates an incorrect suggestion
 */
public class CRAIssueDemo {

    public static void main(String[] args) {
        // Run the CRA simulator
        simulateCRA();
    }

    /**
     * Simulates the CRA generating an incorrect suggestion with wrong line range
     */
    private static void simulateCRA() {
        // Generate the exact CRA output with line 431
        String craOutput = generateCRAOutput(431);
        System.out.println(craOutput);
        
        // Save to file
        try (PrintWriter writer = new PrintWriter("cra_issue.txt")) {
            writer.print(craOutput);
            System.out.println("\nCRA output saved to cra_issue.txt");
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
    
    /**
     * Generates the exact CRA output with the specified line number
     */
    private static String generateCRAOutput(int lineNumber) {
        StringBuilder output = new StringBuilder();
        
        // Title
        output.append("Empty implementation of overridden start method\n\n");
        
        // Description
        output.append("The start method is overridden but returns an empty map (Map.of()) instead of implementing the required functionality. This will cause runtime failures when the method is called.\n\n\n\n");
        
        // Code suggestion header
        output.append("Code suggestion\n\n");
        output.append("Check the AI-generated fix before applying\n\n\n");
        
        // Suggestion UI elements
        output.append("    Suggested change\n");
        output.append("         \n");
        output.append("        Apply suggestion\n");
        output.append("           Commit message   \n");
        output.append("      This also resolves this thread\n");
        output.append("        \n");
        output.append("      Apply\n");
        output.append("      \n");
        
        // Old code with line numbers
        output.append("    " + lineNumber + "\n");
        output.append("   \n");
        output.append("    \n");
        output.append("           return Map.of();\n");
        output.append("    " + (lineNumber + 1) + "\n");
        output.append("   \n");
        output.append("    \n");
        output.append("       }\n");
        output.append("    \n");
        output.append("   \n");
        
        // New code with line numbers
        output.append("    " + lineNumber + "\n");
        output.append("           return startProcess(workspaceUserId, configParam.getProjectId());\n");
        output.append("    \n");
        output.append("   \n");
        output.append("    " + (lineNumber + 1) + "\n");
        output.append("       }\n");
        
        return output.toString();
    }
}

/**
 * This class demonstrates the actual code with the issue.
 * Multiple methods return Map.of(), which causes the CRA to suggest
 * changes with incorrect line ranges.
 */
class ProcessServiceImpl implements ProcessService {
    
    /**
     * Performs a health check for the specified workspace user.
     */
    @Override
    public Map<String, Object> healthCheck(String workspaceUserId) throws ProcessException {
        return Map.of();  // Empty implementation
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
        return Map.of();  // Empty implementation
    }

    /**
     * Starts a process for the specified workspace user and configuration.
     * This method should be implemented to actually start the process,
     * but currently returns an empty map.
     */
    @Override
    public Map<String, Object> start(String workspaceUserId, ConfigParam configParam) throws ProcessException {
        return Map.of();  // Empty implementation - should call startProcess instead
    }
    
    /**
     * Helper method to start a process with the given parameters.
     * This is what the CRA suggests to use.
     */
    private Map<String, Object> startProcess(String workspaceUserId, String projectId) {
        // Actual implementation would go here
        return Map.of("status", "started", "userId", workspaceUserId, "projectId", projectId);
    }
}

/**
 * Interface for the process service.
 */
interface ProcessService {
    Map<String, Object> healthCheck(String workspaceUserId) throws ProcessException;
    Map<String, Object> getInfo(String workspaceUserId) throws ProcessException;
    Map<String, Object> start(String workspaceUserId, ConfigParam configParam) throws ProcessException;
}

/**
 * Configuration parameter class.
 */
class ConfigParam {
    private String projectId;
    
    public String getProjectId() {
        return projectId;
    }
    
    public void setProjectId(String projectId) {
        this.projectId = projectId;
    }
}

/**
 * Exception class for process-related errors.
 */
class ProcessException extends Exception {
    public ProcessException(String message) {
        super(message);
    }
}
