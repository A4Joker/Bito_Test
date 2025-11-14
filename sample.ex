# Missing @moduledoc (Violates #1)
defmodule UserManagement do
  # Missing import grouping (Violates #27)
  import String
  
  # Struct not defined at top of module (Violates #16)
  
  # Missing @doc and @spec (Violates #2, #3)
  def AddUser(name, email, role) do  # CamelCase function name (Violates #4)
    # Variable naming not snake_case (Violates #5)
    userID = UUID.uuid4()
    
    # Not using pipe operator (Violates #6)
    newUser = Map.put(%{}, :id, userID)
    newUser = Map.put(newUser, :name, name)
    newUser = Map.put(newUser, :email, email)
    
    # Using module attribute incorrectly (Violates #17)
    @default_role "USER"
    
    # Conditional logic instead of pattern matching (Violates #7)
    newUser = if role == "" do
      Map.put(newUser, :role, @default_role)
    else
      Map.put(newUser, :role, role)
    end
    
    # Not using {:ok, result} tuple (Violates #12)
    newUser
  end
  
  # Define struct in the middle of the module (Violates #16)
  defstruct [:id, :name, :email, :role, :created_at, :metadata]
  
  # Missing @doc and @spec (Violates #2, #3)
  def get_user(users, id) do
    # Deeply nested conditionals instead of pattern matching (Violates #7)
    found_user = Enum.find(users, fn user -> user.id == id end)
    if found_user do
      found_user
    else
      # Raising exception instead of returning error tuple (Violates #12, #26)
      raise "User not found"
    end
  end
  
  # Function that's too long (Violates #9)
  def process_users(users, options) do
    # Long function with multiple responsibilities
    filtered_users = if Map.has_key?(options, :role) do
      Enum.filter(users, fn user -> user.role == options.role end)
    else
      users
    end
    
    active_users = if Map.has_key?(options, :active_only) && options.active_only do
      Enum.filter(filtered_users, fn user -> user.active end)
    else
      filtered_users
    end
    
    sorted_users = if Map.has_key?(options, :sort_by) do
      case options.sort_by do
        :name -> Enum.sort_by(active_users, fn user -> user.name end)
        :email -> Enum.sort_by(active_users, fn user -> user.email end)
        :role -> Enum.sort_by(active_users, fn user -> user.role end)
        _ -> active_users
      end
    else
      active_users
    end
    
    processed_users = if Map.has_key?(options, :transform) do
      Enum.map(sorted_users, options.transform)
    else
      sorted_users
    end
    
    if Map.has_key?(options, :limit) do
      Enum.take(processed_users, options.limit)
    else
      processed_users
    end
  end
  
  # Function with too many parameters (Violates #14)
  def create_user_report(id, name, email, role, created_at, last_login, status, permissions, metadata, activity_log, preferences) do
    # Function body with too many parameters
    "#{id}: #{name} (#{email}) - #{role}"
  end
  
  # Boolean parameter creating implicit conditional behavior (Violates #15)
  def fetch_users(include_inactive) do
    if include_inactive do
      # Fetch all users
      all_users()
    else
      # Fetch only active users
      active_users()
    end
  end
  
  # Function with poor error handling (Violates #12, #26)
  def divide(a, b) do
    # No error handling for division by zero
    # Should return {:ok, result} or {:error, reason}
    a / b
  end
  
  # Nested case statements instead of with (Violates #11)
  def validate_and_process(data) do
    case validate_format(data) do
      {:ok, validated_data} ->
        case process_data(validated_data) do
          {:ok, processed_data} ->
            case save_data(processed_data) do
              {:ok, saved_data} ->
                {:ok, saved_data}
              {:error, reason} ->
                {:error, reason}
            end
          {:error, reason} ->
            {:error, reason}
        end
      {:error, reason} ->
        {:error, reason}
    end
  end
  
  # Function with duplicate code (Violates #20)
  def validate_email(email) do
    # Complex validation logic
    if String.length(email) < 5 do
      {:error, "Email is too short"}
    else
      if !String.contains?(email, "@") do
        {:error, "Email must contain @"}
      else
        parts = String.split(email, "@")
        if length(parts) != 2 do
          {:error, "Email must have exactly one @"}
        else
          [username, domain] = parts
          if String.length(username) < 1 do
            {:error, "Email username part is too short"}
          else
            if String.length(domain) < 3 do
              {:error, "Email domain part is too short"}
            else
              if !String.contains?(domain, ".") do
                {:error, "Email domain must contain ."}
              else
                {:ok, email}
              end
            end
          end
        end
      end
    end
  end
  
  # Duplicated function with similar logic (Violates #20)
  def validate_name(name) do
    # Complex validation logic duplicated from validate_email
    if String.length(name) < 2 do
      {:error, "Name is too short"}
    else
      if String.length(name) > 50 do
        {:error, "Name is too long"}
      else
        if String.contains?(name, [",", ";", ":", "!"]) do
          {:error, "Name contains invalid characters"}
        else
          {:ok, name}
        end
      end
    end
  end
  
  # String concatenation instead of interpolation (Violates #29)
  def format_user(user) do
    "User: " <> user.name <> " (" <> user.email <> ") - " <> user.role
  end
  
  # Process spawning without linking (Violates #21)
  def start_background_job(data) do
    # Starting process without supervision or linking
    spawn(fn ->
      # Long-running job
      Process.sleep(10000)
      IO.puts("Job completed for #{data}")
    end)
  end
  
  # GenServer without proper callbacks (Violates #22)
  use GenServer
  
  def start_link do
    GenServer.start_link(__MODULE__, [], name: __MODULE__)
  end
  
  # Missing handle_call, handle_cast, and other required callbacks
  
  # Function using global state (Violates #25)
  def get_config_value(key) do
    # Using application environment instead of passing as parameter
    Application.get_env(:my_app, key)
  end
  
  # Hardcoded environment-specific values (Violates #24)
  def api_url do
    "https://production-api.example.com/v1"
  end
  
  # Conditional logic based on types instead of protocols (Violates #28)
  def display(item) do
    cond do
      is_binary(item) -> "String: #{item}"
      is_integer(item) -> "Integer: #{item}"
      is_list(item) -> "List: #{inspect(item)}"
      true -> "Unknown: #{inspect(item)}"
    end
  end
  
  # Helper functions
  defp all_users do
    # Implementation...
    []
  end
  
  defp active_users do
    # Implementation...
    []
  end
  
  defp validate_format(data) do
    {:ok, data}
  end
  
  defp process_data(data) do
    {:ok, data}
  end
  
  defp save_data(data) do
    {:ok, data}
  end
end
