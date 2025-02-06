import java.text.DateFormat;
import java.util.Date;
import java.util.Locale;

public class DateFormatter {
    public String formatDate(Date date) {
        Locale.setDefault(Locale.FRANCE); 
        DateFormat df = DateFormat.getDateInstance(DateFormat.SHORT, Locale.FRANCE);
        return df.format(date); 
    }
    
    public void changeLocale() {
       
        Locale.setDefault(new Locale("fr", "FR"));
    }
}
