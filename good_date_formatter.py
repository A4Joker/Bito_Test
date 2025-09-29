from datetime import datetime
import locale

class DateFormatter:
    def format_date(self, date: datetime, user_locale: str = 'en_US') -> str:
        try:
            locale.setlocale(locale.LC_TIME, user_locale)
            return date.strftime("%x")
        finally:
            locale.setlocale(locale.LC_TIME, '')