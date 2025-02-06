from utils.date_formatter import DateFormatter

class ReportGenerator:
    def __init__(self):
        self.formatter = DateFormatter()
    
    def generate_monthly_report(self, data):
        report_date = self.formatter.format_date(data["date"])
        return f"Report for {report_date}"
