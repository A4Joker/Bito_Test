defmodule CriticallyVulnerableApp do
  # CRITICAL ISSUE: No module documentation
  
  # CRITICAL ISSUE: Hardcoded credentials (Violates #4)
  @api_key "1234567890abcdef1234567890abcdef"
  @admin_password "admin123"
  @db_password "password123"
  
  # CRITICAL ISSUE: Command injection vulnerability (Violates #1)
  def execute_command(user_input) do
    # Directly passing unsanitized user input to shell
    {result, _} = System.cmd("sh", ["-c", user_input])
    result
  end
  
  # CRITICAL ISSUE: SQL injection (Violates #2)
  def find_user(username) do
    # Direct string interpolation in SQL query
    query = "SELECT * FROM users WHERE username = '#{username}'"
    Ecto.Adapters.SQL.query!(MyApp.Repo, query)
  end
  
  # CRITICAL ISSUE: Code execution vulnerability (Violates #13)
  def evaluate_code(code_string) do
    # Evaluating arbitrary code without validation
    {result, _} = Code.eval_string(code_string)
    result
  end
  
  # CRITICAL ISSUE: Authentication vulnerability (Violates #3)
  def authenticate_user(username, password) do
    # Storing and comparing passwords in plaintext
    user = get_user_by_username(username)
    user.password == password
  end
  
  # CRITICAL ISSUE: Resource leak (Violates #5)
  def read_sensitive_file(path) do
    # Opening file without closing it
    {:ok, file} = File.open(path, [:read])
    content = IO.read(file, :all)
    # Missing File.close(file)
    content
  end
  
  # CRITICAL ISSUE: Nil handling (Violates #6)
  def process_user_data(user) do
    # No nil check before accessing nested properties
    full_name = "#{user.profile.first_name} #{user.profile.last_name}"
    email_domain = List.last(String.split(user.email, "@"))
    
    # More processing without nil checks
    "#{full_name} (#{email_domain})"
  end
  
  # CRITICAL ISSUE: Exception handling (Violates #7)
  def parse_json(json_string) do
    try do
      Jason.decode!(json_string)
    rescue
      # Silently catching and discarding exception
      _ -> %{}
    end
  end
  
  # CRITICAL ISSUE: Infinite recursion (Violates #8)
  def process_list(list) do
    [head | tail] = list
    # Missing base case for empty list
    [process_item(head) | process_list(tail)]
  end
  
  # CRITICAL ISSUE: Process management (Violates #9)
  def start_background_task(data) do
    # Spawning process without supervision, linking, or monitoring
    spawn(fn ->
      # Long-running task
      Process.sleep(30_000)
      process_data(data)
    end)
  end
  
  # CRITICAL ISSUE: Concurrency (Violates #10)
  def update_counter(counter_pid, value) do
    # Directly sending messages without synchronization
    send(counter_pid, {:add, value})
  end
  
  # CRITICAL ISSUE: Memory usage (Violates #11)
  def collect_large_dataset(size) do
    # Non-tail recursive function that builds large lists
    collect_data_helper(size, [])
  end
  
  def collect_data_helper(0, acc), do: acc
  def collect_data_helper(n, acc) do
    # Non-tail recursive - will cause stack overflow for large n
    collect_data_helper(n-1, [generate_large_data() | acc])
  end
  
  # CRITICAL ISSUE: Error propagation (Violates #12)
  def save_user(user) do
    # Ignoring error tuple
    case MyApp.Repo.insert(user) do
      {:ok, saved_user} -> saved_user
      {:error, _changeset} -> 
        # Ignoring error
        nil
    end
  end
  
  # CRITICAL ISSUE: Serialization (Violates #14)
  def load_config(binary_data) do
    # Deserializing data without validation
    :erlang.binary_to_term(binary_data)
  end
  
  # CRITICAL ISSUE: Authorization (Violates #16)
  def delete_user(user_id, current_user) do
    # No proper authorization check
    MyApp.Repo.get!(User, user_id) |> MyApp.Repo.delete!()
  end
  
  # CRITICAL ISSUE: Logging (Violates #17)
  def log_login_attempt(username, password) do
    # Logging sensitive information
    Logger.info("Login attempt: username=#{username}, password=#{password}")
  end
  
  # CRITICAL ISSUE: Timing attack (Violates #18)
  def secure_compare(token1, token2) do
    # Non-constant time comparison
    token1 == token2
  end
  
  # CRITICAL ISSUE: CSRF (Violates #19)
  def update_profile(conn, params) do
    # No CSRF protection
    user = conn.assigns.current_user
    changeset = User.changeset(user, params)
    MyApp.Repo.update(changeset)
  end
  
  # CRITICAL ISSUE: XSS (Violates #20)
  def render_comment(comment) do
    # Directly rendering user input without escaping
    "<div class='comment'>#{comment.body}</div>"
  end
  
  # CRITICAL ISSUE: Session management (Violates #21)
  def set_user_session(conn, user) do
    # Storing sensitive data in plaintext cookie
    Plug.Conn.put_session(conn, :user_id, user.id)
    |> Plug.Conn.put_session(:user_role, user.role)
    |> Plug.Conn.put_session(:user_email, user.email)
  end
  
  # CRITICAL ISSUE: Insecure redirect (Violates #22)
  def redirect_after_login(conn, params) do
    # Redirecting to user-provided URL without validation
    redirect_url = params["redirect_to"] || "/"
    Phoenix.Controller.redirect(conn, external: redirect_url)
  end
  
  # CRITICAL ISSUE: File access (Violates #23)
  def serve_file(conn, params) do
    # Serving file based on user input without validation
    file_path = params["path"]
    file_content = File.read!(file_path)
    send_resp(conn, 200, file_content)
  end
  
  # CRITICAL ISSUE: API security (Violates #24)
  def api_get_user_data(conn, params) do
    # No authentication for sensitive API endpoint
    user_id = params["user_id"]
    user = MyApp.Repo.get!(User, user_id)
    json(conn, %{
      id: user.id,
      email: user.email,
      role: user.role,
      api_key: user.api_key
    })
  end
  
  # CRITICAL ISSUE: Rate limiting (Violates #25)
  def login_endpoint(conn, params) do
    # No rate limiting for authentication endpoint
    username = params["username"]
    password = params["password"]
    
    if authenticate_user(username, password) do
      json(conn, %{success: true, token: generate_token(username)})
    else
      json(conn, %{success: false, error: "Invalid credentials"})
    end
  end
  
  # CRITICAL ISSUE: Information disclosure (Violates #26)
  def handle_error(conn, %{reason: %{message: message, stack: stack}}) do
    # Exposing internal details in error response
    json(conn, %{
      error: true,
      message: message,
      stack_trace: stack
    })
  end
  
  # CRITICAL ISSUE: Race condition (Violates #27)
  def increment_counter(counter_id) do
    # Race condition in read-modify-write operation
    current = Counters.get_value(counter_id)
    Counters.set_value(counter_id, current + 1)
  end
  
  # CRITICAL ISSUE: Memory exhaustion (Violates #28)
  def generate_report(params) do
    # Unbounded memory usage based on user input
    size = String.to_integer(params["size"] || "1000")
    large_list = Enum.map(1..size, fn i -> 
      String.duplicate("data", i)
    end)
    
    Enum.join(large_list, "\n")
  end
  
  # CRITICAL ISSUE: Denial of service (Violates #29)
  def compute_factorial(n) do
    # Unbounded execution time based on user input
    case n do
      0 -> 1
      _ -> n * compute_factorial(n - 1)
    end
  end
  
  # CRITICAL ISSUE: Insecure randomness (Violates #30)
  def generate_token(username) do
    # Using weak randomness for security token
    :rand.uniform(1_000_000_000) |> Integer.to_string(16)
  end
  
  # Helper functions
  defp get_user_by_username(username) do
    # Implementation...
    %{username: username, password: "password"}
  end
  
  defp generate_large_data do
    # Generate large data structure
    String.duplicate("data", 1000)
  end
  
  defp process_data(data) do
    # Process data
    data
  end
  
  defp process_item(item) do
    # Process item
    item
  end
end
