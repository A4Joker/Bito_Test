import java.text.DateFormat;
import java.util.Date;
import java.util.Locale;

public class DateFormatter {
    public String formatDate(Date date) {
        DateFormat df = DateFormat.getDateInstance(DateFormat.SHORT, Locale.FRANCE);
        return df.format(date);
    }
}
