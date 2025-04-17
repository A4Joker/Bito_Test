import json
import random

class MockCodeReviewAgent:
    def __init__(self, code_content):
        self.code_content = code_content
        self.lines = code_content.split('\n')
        
    def analyze_code(self):
        """
        Analyze code and intentionally generate an incorrect suggestion with wrong line range
        """
        # Find all return statements
        return_statements = []
        for i, line in enumerate(self.lines):
            if "return Map.of();" in line:
                return_statements.append(i)
        
        # If we found any empty return statements, generate a suggestion
        if return_statements:
            # Intentionally pick the wrong line to create incorrect suggestion
            wrong_line = random.choice(return_statements)
            
            # Create a suggestion with incorrect line range
            suggestion = {
                "title": "Empty implementation of overridden start method",
                "description": "The start method is overridden but returns an empty map (Map.of()) instead of implementing the required functionality. This will cause runtime failures when the method is called.",
                "line_range": {
                    "start": wrong_line + 1,  # Convert to 1-based indexing
                    "end": wrong_line + 2     # Include the next line
                },
                "suggested_change": {
                    "old_code": "        return Map.of();\n    }",
                    "new_code": "        return startProcess(workspaceUserId, configParam.getProjectId());\n    }"
                },
                "severity": "high"
            }
            
            return [suggestion]
        
        return []
    
    def generate_report(self):
        """
        Generate a report with the incorrect suggestions
        """
        suggestions = self.analyze_code()
        
        if not suggestions:
            return "No issues found."
        
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

# Example usage
code = """
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

@Override
public Map<String, Object> start(String workspaceUserId, ConfigParam configParam) throws ProcessException {
    return Map.of();
}
"""

# Create the mock CRA
cra = MockCodeReviewAgent(code)

# Generate the report with incorrect suggestions
report = cra.generate_report()
print(report)
