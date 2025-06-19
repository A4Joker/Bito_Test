import java.text.DateFormat;
import java.util.Date;
import java.util.Locale;

public class DateFormatter {
    private final Locale locale;
    
    public DateFormatter(Locale locale) {
        this.locale = locale != null ? locale : Locale.getDefault();
    }
    
    public String formatDate(Date date) {
        if (date == null) {
            throw new IllegalArgumentException("Date cannot be null");
        }
        DateFormat df = DateFormat.getDateInstance(DateFormat.SHORT, locale);
        return df.format(date);
    }
    
    public Locale getCurrentLocale() {
        return locale;
    }
}