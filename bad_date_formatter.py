from datetime import datetime
import locale

class DateFormatter:
    def format_date(self, date: datetime) -> str:
        locale.setlocale(locale.LC_TIME, 'fr_FR')
        return date.strftime("%x")