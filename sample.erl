% Missing module documentation (Violates #1)
-module(user_mgmt).

% Exports not grouped logically (Violates #3)
-export([add_user/3]).
-export([get_user/1, delete_user/1]).
-export([process_users/1]).

% Record definition not at top (Violates #4)

% Macro name not in UPPER_CASE (Violates #5)
-define(max_users, 100).
-define(DefaultRole, "USER").  % Inconsistent naming

% Record name not CamelCase (Violates #5)
-record(user_record, {
    id,
    name,
    email,
    role,
    created_at,
    % Missing field documentation
    metadata
}).

% Missing type specifications (Violates #20)

% Function without EDoc comments (Violates #2)
add_user(Name, Email, Role) ->
    % Not using pattern matching for default role (Violates #7)
    FinalRole = if Role == "" -> ?DefaultRole;
                   true -> Role
                end,
    
    % Complex function without helper functions (Violates #8)
    Id = generate_id(),
    Now = erlang:universaltime(),
    User = #user_record{
        id = Id,
        name = Name,
        email = Email,
        role = FinalRole,
        created_at = Now,
        metadata = []
    },
    
    % Not using {ok, Result} pattern (Violates #10)
    User.

% Function without EDoc comments (Violates #2)
get_user(Id) ->
    % Not using OTP behaviors (Violates #11)
    % Directly accessing global state
    case ets:lookup(users_table, Id) of
        [] ->
            % Throwing exception instead of returning error tuple (Violates #10)
            erlang:error({not_found, Id});
        [{Id, User}] ->
            User
    end.

% Function without EDoc comments (Violates #2)
delete_user(Id) ->
    % Not using OTP behaviors (Violates #11)
    % Directly accessing global state
    case ets:lookup(users_table, Id) of
        [] ->
            % Throwing exception instead of returning error tuple (Violates #10)
            erlang:error({not_found, Id});
        [{Id, _User}] ->
            ets:delete(users_table, Id),
            ok
    end.

% Function that's too long (Violates #8)
process_users(Options) ->
    % Function too long and complex
    Users = case ets:tab2list(users_table) of
        [] -> [];
        UserList -> [User || {_Id, User} <- UserList]
    end,
    
    % Complex function without helper functions (Violates #8)
    FilteredUsers = case proplists:get_value(role, Options) of
        undefined -> Users;
        Role ->
            % Not using list comprehension (Violates #13)
            filter_by_role(Users, Role)
    end,
    
    SortedUsers = case proplists:get_value(sort_by, Options) of
        undefined -> FilteredUsers;
        name -> 
            % Complex sorting logic inline (Violates #8)
            lists:sort(fun(#user_record{name = Name1}, #user_record{name = Name2}) ->
                Name1 =< Name2
            end, FilteredUsers);
        email ->
            lists:sort(fun(#user_record{email = Email1}, #user_record{email = Email2}) ->
                Email1 =< Email2
            end, FilteredUsers);
        role ->
            lists:sort(fun(#user_record{role = Role1}, #user_record{role = Role2}) ->
                Role1 =< Role2
            end, FilteredUsers)
    end,
    
    % More processing...
    
    % Long function continues...
    LimitedUsers = case proplists:get_value(limit, Options) of
        undefined -> SortedUsers;
        Limit when is_integer(Limit), Limit > 0 ->
            lists:sublist(SortedUsers, Limit);
        _ ->
            SortedUsers
    end,
    
    LimitedUsers.

% Duplicate function that should be a helper (Violates #14)
filter_by_role(Users, Role) ->
    % Not using list comprehension (Violates #13)
    lists:filter(fun(#user_record{role = UserRole}) ->
        UserRole =:= Role
    end, Users).

% Function without EDoc comments (Violates #2)
export_users(Filename) ->
    % Not using {ok, Result}/{error, Reason} pattern (Violates #10)
    Users = case ets:tab2list(users_table) of
        [] -> [];
        UserList -> [User || {_Id, User} <- UserList]
    end,
    
    % Poor error handling for file operations (Violates #10, #14)
    {ok, File} = file:open(Filename, [write]),
    io:format(File, "id,name,email,role,created_at~n", []),
    lists:foreach(fun(#user_record{id = Id, name = Name, email = Email, role = Role, created_at = CreatedAt}) ->
        io:format(File, "~s,~s,~s,~s,~p~n", [Id, Name, Email, Role, CreatedAt])
    end, Users),
    file:close(File),
    
    % Not using {ok, Result} pattern (Violates #10)
    ok.

% Function with non-tail recursion (Violates #12)
generate_id() ->
    % Non-tail recursive function
    random_char() ++ generate_id_part(35).

generate_id_part(0) ->
    [];
generate_id_part(N) ->
    % Non-tail recursive concatenation
    random_char() ++ generate_id_part(N-1).

random_char() ->
    % Using process dictionary (Violates #28)
    put(random_seed, {erlang:phash2([node()]),
                      erlang:monotonic_time(),
                      erlang:unique_integer()}),
    Chars = "abcdefghijklmnopqrstuvwxyz0123456789",
    [lists:nth(rand:uniform(36), Chars)].

% Using process dictionary instead of state (Violates #28)
init_users_table() ->
    % Using ETS without documenting ownership (Violates #30)
    ets:new(users_table, [set, public, named_table]),
    ok.

% Function with if statement instead of pattern matching (Violates #7)
validate_email(Email) ->
    % Using if instead of pattern matching or guard clauses (Violates #7)
    if
        length(Email) < 5 ->
            {error, "Email is too short"};
        true ->
            case string:str(Email, "@") of
                0 ->
                    {error, "Email must contain @"};
                _ ->
                    Parts = string:tokens(Email, "@"),
                    if
                        length(Parts) /= 2 ->
                            {error, "Email must have exactly one @"};
                        true ->
                            [Username, Domain] = Parts,
                            if
                                length(Username) < 1 ->
                                    {error, "Email username part is too short"};
                                length(Domain) < 3 ->
                                    {error, "Email domain part is too short"};
                                true ->
                                    case string:str(Domain, ".") of
                                        0 ->
                                            {error, "Email domain must contain ."};
                                        _ ->
                                            {ok, Email}
                                    end
                            end
                    end
            end
    end.

% Spawning process without linking (Violates #11)
start_background_job(Data) ->
    % Spawning process without linking or monitoring (Violates #11)
    spawn(fun() ->
        process_data(Data)
    end).

% Function using hardcoded values (Violates #19)
get_api_url() ->
    % Hardcoded environment-specific URL (Violates #19)
    "https://production.example.com/api/v1".

% Function with binary processing without pattern matching (Violates #27)
parse_binary_data(Binary) ->
    % Manual byte manipulation instead of binary pattern matching (Violates #27)
    <<Length:32, _Rest/binary>> = Binary,
    DataSize = Length * 8,
    <<_Length:32, Data:DataSize/binary, _Tail/binary>> = Binary,
    Data.

% Process with message handling but no timeout (Violates #15)
start_server() ->
    % Not using OTP behaviors (Violates #11)
    spawn(fun() -> server_loop([]) end).

server_loop(State) ->
    receive
        {add, Item, From} ->
            NewState = [Item | State],
            From ! {ok, added},
            server_loop(NewState);
        {get, From} ->
            From ! {ok, State},
            server_loop(State);
        stop ->
            ok
        % No catch-all clause and no timeout (Violates #15)
    end.

% Function with resource leak (Violates #14)
process_file(Filename) ->
    % Resource management issue - file not guaranteed to be closed (Violates #14)
    {ok, File} = file:open(Filename, [read]),
    process_file_data(File, []).

process_file_data(File, Acc) ->
    case file:read_line(File) of
        {ok, Line} ->
            process_file_data(File, [Line | Acc]);
        eof ->
            % File is closed here, but not if an error occurs
            file:close(File),
            lists:reverse(Acc);
        {error, Reason} ->
            % File not closed on error path (Violates #14)
            {error, Reason}
    end.
