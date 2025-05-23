package com.example.demo;

import java.io.*;
import java.util.*;
import java.util.concurrent.ConcurrentHashMap;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.logging.Logger;

public class DataProcessor {
    // Public non-final static field (should be private)
    public static String DATABASE_URL = "jdbc:mysql://localhost:3306/testdb";
    
    // Unused imports above
    // Non-constant field names should be camelCase
    private String USER_NAME = "admin";
    private String PASSWORD = "password"; // Hardcoded credentials (security issue)
    
    // Logger not declared as final
    private static Logger logger = Logger.getLogger("DataProcessor");
    
    // Public field should be encapsulated
    public List<String> processingResults = new ArrayList<>();
    
    // Unused field
    private int maxRetries = 3;
    
    // Missing JavaDoc
    public DataProcessor() {
        // Empty constructor
    }
    
    // Inconsistent indentation and brace style
    public void processData(String filePath) throws Exception
    {
      File file = new File(filePath);
      // Resource leak: file reader not closed with try-with-resources
      FileReader reader = new FileReader(file);
      BufferedReader bufferedReader = new BufferedReader(reader);
      
      String line;
      while ((line = bufferedReader.readLine()) != null) {
          // Unused variable
          int lineLength = line.length();
          
          // Inefficient string concatenation in loop
          String processedLine = "";
          for (int i = 0; i < line.length(); i++) {
              processedLine = processedLine + line.charAt(i);
          }
          
          processingResults.add(processedLine);
      }
      
      // Resources not closed properly
      bufferedReader.close();
      reader.close();
    }
    
    // Method with too many parameters
    public Map<String, Object> queryDatabase(String table, String[] columns, String whereClause, 
                                           String orderBy, int limit, boolean ascending, 
                                           String groupBy, String having) {
        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;
        
        try {
            // Using string concatenation for SQL (SQL injection risk)
            String query = "SELECT " + String.join(",", columns) + " FROM " + table;
            
            if (whereClause != null && !whereClause.isEmpty()) {
                query += " WHERE " + whereClause;
            }
            
            if (groupBy != null && !groupBy.isEmpty()) {
                query += " GROUP BY " + groupBy;
            }
            
            if (having != null && !having.isEmpty()) {
                query += " HAVING " + having;
            }
            
            if (orderBy != null && !orderBy.isEmpty()) {
                query += " ORDER BY " + orderBy + (ascending ? " ASC" : " DESC");
            }
            
            if (limit > 0) {
                query += " LIMIT " + limit;
            }
            
            conn = DriverManager.getConnection(DATABASE_URL, USER_NAME, PASSWORD);
            stmt = conn.createStatement();
            rs = stmt.executeQuery(query);
            
            // Inefficient data structure usage
            Map<String, Object> results = new HashMap<>();
            int rowCount = 0;
            
            while (rs.next()) {
                // Overwriting results in each iteration (bug)
                for (String column : columns) {
                    results.put(column, rs.getObject(column));
                }
                rowCount++;
            }
            
            // Unused variable
            int totalRows = rowCount;
            
            return results;
        } catch (SQLException e) {
            // Catching generic exception and rethrowing as RuntimeException
            // Also, printing stack trace and logging error (duplicate logging)
            e.printStackTrace();
            logger.severe("Database error: " + e.getMessage());
            throw new RuntimeException("Database error", e);
        } finally {
            // Nested try-catch blocks in finally (overly complex)
            try {
                if (rs != null) rs.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
            try {
                if (stmt != null) stmt.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
            try {
                if (conn != null) conn.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
    
    // Method doesn't follow naming conventions (should be camelCase)
public void Export_data(String outputPath) {
        try {
            // Potential null pointer dereference
            if (processingResults.size() > 0) {
                // Using try-with-resources to ensure proper resource cleanup
                try (FileWriter writer = new FileWriter(outputPath)) {
                    for (String result : processingResults) {
                        writer.write(result + "\n");
                    }
                }
            }
        } catch (Exception e) {
            // Generic exception catch
            // Swallowing exception (only logging, not rethrowing)
            logger.warning("Export failed: " + e.getMessage());
        }
    }
    
    // Complex method with high cyclomatic complexity
    public boolean validateData(String data) {
        if (data == null) {
            return false;
        }
        
        if (data.length() < 5) {
            return false;
        }
        
        if (data.startsWith("TEST_")) {
            return true;
        }
        
        if (data.endsWith("_VALID")) {
            return true;
        }
        
        if (data.contains("APPROVED")) {
            return true;
        }
        
        char firstChar = data.charAt(0);
        if (Character.isUpperCase(firstChar)) {
            char lastChar = data.charAt(data.length() - 1);
            if (Character.isDigit(lastChar)) {
                return true;
            }
        }
        
        try {
            Integer.parseInt(data);
            return false;
        } catch (NumberFormatException e) {
            // Empty catch block (swallowing exception)
        }
        
        // Inconsistent return style (some returns above, some below)
        if (data.matches("^[a-zA-Z0-9_]+$")) {
            return true;
        } else {
            return false;
        }
    }
    
    // Class with static methods (utility class should be final with private constructor)
    public static class DateUtils {
        // Non-thread-safe SimpleDateFormat
        public static SimpleDateFormat formatter = new SimpleDateFormat("yyyy-MM-dd");
        
        public static String formatDate(Date date) {
            return formatter.format(date);
        }
        
        // Unused method parameter
        public static boolean isWeekend(Date date, boolean includeHolidays) {
            Calendar cal = Calendar.getInstance();
            cal.setTime(date);
            int day = cal.get(Calendar.DAY_OF_WEEK);
            return day == Calendar.SATURDAY || day == Calendar.SUNDAY;
        }
    }
    
    // Inner class with poor encapsulation
    public class DataRecord {
        // Public fields without getters/setters
        public String id;
        public String name;
        public int value;
        
        // Equals method without hashCode
        @Override
        public boolean equals(Object obj) {
            if (this == obj) return true;
            if (obj == null) return false;
            if (getClass() != obj.getClass()) return false;
            
            DataRecord other = (DataRecord) obj;
            return id.equals(other.id);
        }
        
        // Missing @Override annotation
        public String toString() {
            // String concatenation instead of StringBuilder
            return "DataRecord [id=" + id + ", name=" + name + ", value=" + value + "]";
        }
    }
    
    // Main method in non-executable class
    public static void main(String[] args) {
        DataProcessor processor = new DataProcessor();
        
        try {
            // Magic string (hardcoded file path)
            processor.processData("C:\\data\\input.txt");
            
            // Unused variable
            int resultCount = processor.processingResults.size();
            
            // Magic string (hardcoded file path)
            processor.Export_data("C:\\data\\output.txt");
            
            System.out.println("Processing complete");
        } catch (Exception e) {
            // Catching generic exception
            e.printStackTrace();
        }
        
        // Unreachable code due to System.exit
        System.exit(0);
        System.out.println("This will never be printed");
    }
}
