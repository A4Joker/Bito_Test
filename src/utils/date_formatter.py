class DateFormatter:
    def __init__(self):
        # Before
        self.locale = None  # Uses system default
        
        # After (Changed in PR)
        self.locale = "fr_FR"  # Hardcoded French locale
    
    def format_date(self, date):
        return date.strftime("%d/%m/%Y")
