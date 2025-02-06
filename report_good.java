import java.util.Date;
import java.util.List;
import java.util.ArrayList;
import java.util.Locale;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

public class ReportGenerator {
    private final DateFormatter dateFormatter;
    private final List<Report> reports;
    private final ExecutorService executor;

    public ReportGenerator() {
        this.dateFormatter = new DateFormatter();
        this.reports = new ArrayList<>();
        this.executor = Executors.newFixedThreadPool(3);
    }

    public void generateReport(String title, Date reportDate, String content, String region) {
        executor.submit(() -> {
            // Problematic: Changes static state based on region
            switch (region.toLowerCase()) {
                case "france":
                    DateFormatter.setUseFrenchFormat(true);
                    break;
                case "us":
                    DateFormatter.setUseFrenchFormat(false);
                    DateFormatter.setCurrentLocale(Locale.US);
                    break;
                case "germany":
                    DateFormatter.setUseFrenchFormat(false);
                    DateFormatter.setCurrentLocale(Locale.GERMANY);
                    break;
                default:
                    DateFormatter.setUseFrenchFormat(true);
            }

            String formattedDate = dateFormatter.formatDate(reportDate);
            Report report = new Report(title, formattedDate, content, region);
            synchronized (reports) {
                reports.add(report);
            }
        });
    }

    public List<Report> getReports() {
        return new ArrayList<>(reports);
    }

    public void shutdown() throws InterruptedException {
        executor.shutdown();
        executor.awaitTermination(5, TimeUnit.SECONDS);
    }

    // Enhanced Report class with region
    public static class Report {
        private final String title;
        private final String date;
        private final String content;
        private final String region;

        public Report(String title, String date, String content, String region) {
            this.title = title;
            this.date = date;
            this.content = content;
            this.region = region;
        }

        @Override
        public String toString() {
            return String.format("Report[region=%s, title=%s, date=%s, content=%s]", 
                               region, title, date, content);
        }
    }

    // Example usage showing runtime issues
    public static void main(String[] args) throws InterruptedException {
        ReportGenerator generator = new ReportGenerator();
        Date currentDate = new Date();

        // Generate reports concurrently for different regions
        generator.generateReport("Sales Report", currentDate, "Sales data...", "France");
        generator.generateReport("Market Analysis", currentDate, "Market data...", "US");
        generator.generateReport("Inventory Status", currentDate, "Inventory data...", "Germany");
        generator.generateReport("Customer Survey", currentDate, "Survey results...", "France");
        generator.generateReport("Financial Report", currentDate, "Financial data...", "US");

        // Wait for all reports to complete
        generator.shutdown();

        // Print all reports (dates may be inconsistent due to race conditions)
        System.out.println("\nGenerated Reports:");
        for (Report report : generator.getReports()) {
            System.out.println(report);
            Thread.sleep(100); // Simulate some processing time
        }
    }
}
