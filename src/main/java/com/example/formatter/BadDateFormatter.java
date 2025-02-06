import java.text.DateFormat;
import java.util.Date;
import java.util.Locale;

public class DateFormatter {
    public String formatDate(Date date) {
        Locale.setDefault(Locale.FRANCE);  // Bad practice: Modifying global state
        DateFormat df = DateFormat.getDateInstance(DateFormat.SHORT, Locale.FRANCE);
        return df.format(date);  // No null check
    }
    
    public void changeLocale() {
        // Bad practice: Allowing locale modification after initialization
        Locale.setDefault(new Locale("fr", "FR"));
    }
}