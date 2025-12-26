import java.util.Date;
import java.util.List;
import java.util.ArrayList;

public class ReportGenerator {
    private final DateFormatter dateFormatter;
    private final List<Report> reports;

    public ReportGenerator() {
        this.dateFormatter = new DateFormatter();
        this.reports = new ArrayList<>();
    }

    public void generateReport(String title, Date reportDate, String content) {
        String formattedDate = dateFormatter.formatDate(reportDate);
        Report report = new Report(title, formattedDate, content);
        reports.add(report);
    }

    public List<Report> getReports() {
        return new ArrayList<>(reports);
    }

    // Simple Report class for demonstration
    public static class Report {
        private final String title;
        private final String date;
        private final String content;

        public Report(String title, String date, String content) {
            this.title = title;
            this.date = date;
            this.content = content;
        }

        @Override
        public String toString() {
            return String.format("Report[title=%s, date=%s, content=%s]", 
                               title, date, content);
        }
    }

    // Example usage showing the international context
    public static void main(String[] args) {
        ReportGenerator generator = new ReportGenerator();
        
        // Generate reports for different regions
        generator.generateReport("US Sales Report", new Date(), "US sales data...");
        generator.generateReport("German Market Analysis", new Date(), "German market data...");
        generator.generateReport("Japanese Inventory", new Date(), "Japan inventory status...");
        
        // Print all reports (all dates will be in French format regardless of region)
        for (Report report : generator.getReports()) {
            System.out.println(report);
        }
    }
}
