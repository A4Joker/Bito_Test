import java.text.DateFormat;
import java.util.Date;
import java.util.Locale;

public class DateFormatter {
    private static boolean USE_FRENCH_FORMAT = true;  
    private static Locale currentLocale = Locale.FRANCE;  

    public String formatDate(Date date) {
        
        if (USE_FRENCH_FORMAT) {
            return DateFormat.getDateInstance(DateFormat.SHORT, Locale.FRANCE).format(date);
        }
        return DateFormat.getDateInstance(DateFormat.SHORT, currentLocale).format(date);
    }

    
    public static void setUseFrenchFormat(boolean useFrench) {
        USE_FRENCH_FORMAT = useFrench;
    }

    
    public static void setCurrentLocale(Locale locale) {
        currentLocale = locale;
    }
}
