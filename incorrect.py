import json

class MockCodeReviewAgent:
    def __init__(self, code_content):
        self.code_content = code_content
        self.lines = code_content.split('\n')
        
    def analyze_code(self):
        """
        Analyze code and intentionally generate an incorrect suggestion with wrong line range
        """
        # Find methods that return Map.of()
        methods_with_empty_returns = []
        current_method = None
        method_start_line = 0
        
        for i, line in enumerate(self.lines):
            # Check for method start
            if "@Override" in line and "public" in self.lines[i+1]:
                current_method = self.lines[i+1].strip()
                method_start_line = i
            
            # Check for return Map.of()
            if current_method and "return Map.of();" in line:
                methods_with_empty_returns.append({
                    "method": current_method,
                    "return_line": i,
                    "method_start_line": method_start_line
                })
                current_method = None
        
        # Generate incorrect suggestion for line 431 specifically
        suggestion = {
            "title": "Empty implementation of overridden start method",
            "description": "The start method is overridden but returns an empty map (Map.of()) instead of implementing the required functionality. This will cause runtime failures when the method is called.",
            "line_range": {
                "start": 431,
                "end": 432
            },
            "suggested_change": {
                "old_code": "        return Map.of();\n    }",
                "new_code": "        return startProcess(workspaceUserId, configParam.getProjectId());\n    }"
            },
            "severity": "high"
        }
        
        return [suggestion]
    
    def generate_report(self):
        """
        Generate a report with the incorrect suggestions
        """
        suggestions = self.analyze_code()
        
        report = "# Code Review Report\n\n"
        
        for suggestion in suggestions:
            report += f"## {suggestion['title']}\n\n"
            report += f"{suggestion['description']}\n\n"
            report += "### Code suggestion\n\n"
            report += "Check the AI-generated fix before applying\n\n"
            report += "```diff\n"
            report += f"@@ -{suggestion['line_range']['start']},{suggestion['line_range']['end']} +{suggestion['line_range']['start']},1 @@\n"
            report += f"-{suggestion['suggested_change']['old_code']}\n"
            report += f"+{suggestion['suggested_change']['new_code']}\n"
            report += "```\n\n"
            
        return report

# Generate a large code file to simulate the line numbers
def generate_large_code_file():
    code = []
    
    # Add header and imports
    code.append("package com.example.service;")
    code.append("")
    code.append("import java.util.Map;")
    code.append("import java.util.HashMap;")
    code.append("import org.springframework.stereotype.Service;")
    code.append("")
    code.append("@Service")
    code.append("public class ProcessServiceImpl implements ProcessService {")
    
    # Add many methods to reach line 431
    for i in range(1, 40):
        code.append(f"    /**")
        code.append(f"     * Method {i}")
        code.append(f"     */")
        code.append(f"    public void method{i}() {{")
        code.append(f"        // Implementation")
        code.append(f"    }}")
        code.append("")
    
    # Add healthCheck method around line 420
    code.append("    @Override")
    code.append("    public Map<String, Object> healthCheck(String workspaceUserId) throws ProcessException {")
    code.append("        return Map.of();")
    code.append("    }")
    code.append("")
    
    # Add getInfo method around line 425
    code.append("    /**")
    code.append("     * Retrieves information about a process for the specified workspace user.")
    code.append("     *")
    code.append("     * @param workspaceUserId The unique identifier for the workspace user")
    code.append("     * @return Map containing process information")
    code.append("     * @throws ProcessException if the information cannot be retrieved")
    code.append("     */")
    code.append("    @Override")
    code.append("    public Map<String, Object> getInfo(String workspaceUserId) throws ProcessException {")
    code.append("        return Map.of();")
    code.append("    }")
    code.append("")
    
    # Add start method with empty implementation at line 431
    code.append("    @Override")
    code.append("    public Map<String, Object> start(String workspaceUserId, ConfigParam configParam) throws ProcessException {")
    code.append("        return Map.of();")  # This should be line 431
    code.append("    }")
    code.append("")
    
    # Add more methods
    for i in range(40, 50):
        code.append(f"    /**")
        code.append(f"     * Method {i}")
        code.append(f"     */")
        code.append(f"    public void method{i}() {{")
        code.append(f"        // Implementation")
        code.append(f"    }}")
        code.append("")
    
    code.append("}")
    
    return "\n".join(code)

# Create a large code file
code = generate_large_code_file()

# Verify line 431 has "return Map.of();"
lines = code.split('\n')
print(f"Line 431: {lines[430]}")  # Zero-indexed, so 430 is line 431

# Create the mock CRA
cra = MockCodeReviewAgent(code)

# Generate the report with incorrect suggestions
report = cra.generate_report()
print(report)
