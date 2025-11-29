import java.util.*;
import java.util.regex.*;

public class MockCodeReviewAgent {
    private String codeContent;
    private String[] lines;
    
    public MockCodeReviewAgent(String codeContent) {
        this.codeContent = codeContent;
        this.lines = codeContent.split("\n");
    }
    
    public List<Map<String, Object>> analyzeCode() {
        // Find all return statements
        List<Integer> returnStatements = new ArrayList<>();
        for (int i = 0; i < lines.length; i++) {
            if (lines[i].contains("return Map.of();")) {
                returnStatements.add(i);
            }
        }
        
        // If we found any empty return statements, generate a suggestion
        if (!returnStatements.isEmpty()) {
            // Intentionally pick the wrong line to create incorrect suggestion
            Random random = new Random();
            int wrongLine = returnStatements.get(random.nextInt(returnStatements.size()));
            
            // Create a suggestion with incorrect line range
            Map<String, Object> suggestion = new HashMap<>();
            suggestion.put("title", "Empty implementation of overridden start method");
            suggestion.put("description", "The start method is overridden but returns an empty map (Map.of()) instead of implementing the required functionality. This will cause runtime failures when the method is called.");
            
            Map<String, Integer> lineRange = new HashMap<>();
            lineRange.put("start", wrongLine + 1);  // Convert to 1-based indexing
            lineRange.put("end", wrongLine + 2);    // Include the next line
            suggestion.put("line_range", lineRange);
            
            Map<String, String> suggestedChange = new HashMap<>();
            suggestedChange.put("old_code", "        return Map.of();\n    }");
            suggestedChange.put("new_code", "        return startProcess(workspaceUserId, configParam.getProjectId());\n    }");
            suggestion.put("suggested_change", suggestedChange);
            
            suggestion.put("severity", "high");
            
            return Collections.singletonList(suggestion);
        }
        
        return Collections.emptyList();
    }
    
    public String generateReport() {
        List<Map<String, Object>> suggestions = analyzeCode();
        
        if (suggestions.isEmpty()) {
            return "No issues found.";
        }
        
        StringBuilder report = new StringBuilder("# Code Review Report\n\n");
        
        for (Map<String, Object> suggestion : suggestions) {
            report.append("## ").append(suggestion.get("title")).append("\n\n");
            report.append(suggestion.get("description")).append("\n\n");
            report.append("### Code suggestion\n\n");
            report.append("Check the AI-generated fix before applying\n\n");
            report.append("```diff\n");
            
            Map<String, Integer> lineRange = (Map<String, Integer>) suggestion.get("line_range");
            report.append("@@ -").append(lineRange.get("start")).append(",").append(lineRange.get("end"))
                  .append(" +").append(lineRange.get("start")).append(",1 @@\n");
            
            Map<String, String> suggestedChange = (Map<String, String>) suggestion.get("suggested_change");
            report.append("-").append(suggestedChange.get("old_code")).append("\n");
            report.append("+").append(suggestedChange.get("new_code")).append("\n");
            
            report.append("```\n\n");
        }
        
        return report.toString();
    }
    
    public static void main(String[] args) {
        String code = 
            "@Override\n" +
            "public Map<String, Object> healthCheck(String workspaceUserId) throws ProcessException {\n" +
            "    return Map.of();\n" +
            "}\n" +
            "\n" +
            "/**\n" +
            " * Retrieves information about a process for the specified workspace user.\n" +
            " *\n" +
            " * @param workspaceUserId The unique identifier for the workspace user\n" +
            " * @return Map containing process information\n" +
            " * @throws ProcessException if the information cannot be retrieved\n" +
            " */\n" +
            "@Override\n" +
            "public Map<String, Object> getInfo(String workspaceUserId) throws ProcessException {\n" +
            "    return Map.of();\n" +
            "}\n" +
            "\n" +
            "@Override\n" +
            "public Map<String, Object> start(String workspaceUserId, ConfigParam configParam) throws ProcessException {\n" +
            "    return Map.of();\n" +
            "}\n";
        
        // Create the mock CRA
        MockCodeReviewAgent cra = new MockCodeReviewAgent(code);
        
        // Generate the report with incorrect suggestions
        String report = cra.generateReport();
        System.out.println(report);
    }
}
