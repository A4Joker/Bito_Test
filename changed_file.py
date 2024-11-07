import java.io. *;
import javax.servlet. *;
import javax.servlet.http. *;

public


class Main extends HttpServlet {
// Static ( global ) variable
public static final String WEBSITE_NAME = "My Java Web App";

// Member variable


public void init() {
visitorCount = 0;
}

public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
response.setContentType("text/html");
PrintWriter out = response.getWriter();

visitorCount++;

out.println(Utilities.getHTMLContent());
out.println("<h2>Welcome to " + WEBSITE_NAME + "</h2>");
out.println("<p>You are visitor number: " + visitorCount + "</p>");
out.println("</body></html>");
}
}