' Missing Option statements that should trigger CRA suggestions
' (Violates Generative Prompt #1)

Imports System
Imports System.Collections.Generic
Imports System.IO
Imports System.Text

Module UserManagement
    ' Global variables without proper naming
    ' (Violates Generative Prompt #12)
    Public users_list As New List(Of User)
    Public MaxUsers = 100  ' No type declaration (Violates Generative Prompt #3)
    Public default_role = "USER"  ' No type declaration
    
    ' This global variable should be ignored by CRA due to cleanup prompt #7
    Public g_ApplicationSettings As Dictionary(Of String, String)
    
    Sub Main()
        ' Poor error handling with On Error instead of Try/Catch
        ' (Violates Generative Prompt #5)
        On Error GoTo ErrorHandler
        
        ' Implicit variable (missing Dim and type)
        ' (Violates Generative Prompt #3)
        counter = 0
        
        ' Poor naming (no prefix for form controls)
        ' (Violates Generative Prompt #2)
        Dim Name As TextBox = New TextBox()
        Dim Email As TextBox = New TextBox()
        Dim Submit As Button = New Button()
        
        ' String concatenation instead of interpolation
        ' (Violates Generative Prompt #7)
        Console.WriteLine("Starting user management system with " & MaxUsers & " maximum users")
        
        ' This logging statement uses concatenation but should be ignored by CRA
        ' due to cleanup prompt #4
        Console.WriteLine("Log: " & DateTime.Now & " - Application started")
        
        ' Create some users
        AddUser("John Doe", "john@example.com", "ADMIN")
        AddUser("Jane Smith", "jane@example.com", "")
        
        ' Comparing boolean with True
        ' (Violates Generative Prompt #8)
        If IsUserValid("John Doe", "john@example.com") = True Then
            Console.WriteLine("User is valid")
        End If
        
        ' Nested conditionals (excessive nesting)
        ' (Violates Generative Prompt #9)
        For Each u In users_list
            If Not u Is Nothing Then
                If u.Role = "ADMIN" Then
                    If u.Email.Contains("@example.com") Then
                        If u.Name.Length > 5 Then
                            Console.WriteLine("Found admin: " & u.Name)
                        End If
                    End If
                End If
            End If
        Next
        
        ' Missing resource management
        ' (Violates Generative Prompt #6)
        Dim writer As StreamWriter = New StreamWriter("users.txt")
        writer.WriteLine("User List:")
        For Each user In users_list
            writer.WriteLine(user.Name & "," & user.Email & "," & user.Role)
        Next
        writer.Close()
        
        ' This section should be ignored by CRA due to cleanup prompt #10
        ' * Manual Disposal *
        Dim manualReader As StreamReader = New StreamReader("config.txt")
        Dim configText As String = manualReader.ReadToEnd()
        manualReader.Close()
        
        Exit Sub
        
ErrorHandler:
        ' Poor error handling
        Console.WriteLine("An error occurred: " & Err.Description)
        Resume Next
    End Sub
    
    ' Function without proper parameter passing specification
    ' (Violates Generative Prompt #4)
    Function AddUser(Name, Email, Role)
        ' Implicit variable type
        ' (Violates Generative Prompt #3)
        Dim user = New User()
        
        user.ID = Guid.NewGuid().ToString()
        user.Name = Name
        user.Email = Email
        
        ' Poor conditional structure
        If Role = "" Then
            user.Role = default_role
        Else
            user.Role = Role
        End If
        
        ' No error handling
        users_list.Add(user)
        
        ' Concatenation instead of interpolation
        Console.WriteLine("Added user: " & Name & " with role: " & user.Role)
        
        Return user
    End Function
    
    ' This section should be ignored by CRA due to cleanup prompt #6
    ' * External API *
    Function ExternalApiCall(data, callback)
        ' External API calls with special parameter passing requirements
        Dim result As Object = Nothing
        
        ' Implementation details...
        
        Return result
    End Function
    
    ' Function without return type
    ' (Violates Generative Prompt #3)
    Function IsUserValid(Name, Email)
        ' Poor variable naming
        ' (Violates Generative Prompt #2)
        Dim x As Boolean = False
        
        For Each u In users_list
            If u.Name = Name And u.Email = Email Then
                x = True
                Exit For
            End If
        Next
        
        Return x
    End Function
    
    ' This section should be ignored by CRA due to cleanup prompt #8
    ' * Complex Algorithm *
    Sub PerformComplexCalculation()
        ' This is a very long method with complex algorithm
        ' that exceeds recommended method length
        
        ' Implementation of complex algorithm...
        ' (many lines of code here)
        
        Dim result As Double = 0
        
        ' Complex calculation logic...
        
        Console.WriteLine("Calculation result: " & result)
    End Sub
    
    ' Procedure with ambiguous parameter passing
    ' (Violates Generative Prompt #4)
    Sub UpdateUser(ID, Name, Email, Role)
        ' Inefficient loop
        For i = 0 To users_list.Count - 1
            If users_list(i).ID = ID Then
                ' Multiple statements on one line
                users_list(i).Name = Name : users_list(i).Email = Email
                
                ' Poor conditional
                If Role <> "" Then users_list(i).Role = Role
                
                Exit Sub
            End If
        Next
        
        ' No return value or status indication
    End Sub
    
    ' This section should be ignored by CRA due to cleanup prompt #3
    ' * Custom Error Handling *
    Sub ProcessCriticalOperation()
        On Error Resume Next
        
        ' Custom error handling implementation
        ' that doesn't follow standard Try/Catch pattern
        
        ' Implementation details...
        
        If Err.Number <> 0 Then
            ' Custom error handling logic
        End If
    End Sub
    
    ' Function with poor error handling
    ' (Violates Generative Prompt #5)
    Function ExportUsersToJson()
        On Error Resume Next
        
        ' Magic numbers without constants
        ' (Violates Generative Prompt #15)
        If users_list.Count > 1000 Then
            Console.WriteLine("Too many users to export")
            Return ""
        End If
        
        ' String building instead of using a StringBuilder
        Dim json As String = "["
        Dim first As Boolean = True
        
        For Each user In users_list
            If Not first Then
                json = json & ","
            End If
            
            json = json & "{"
            json = json & """id"":""" & user.ID & ""","
            json = json & """name"":""" & user.Name & ""","
            json = json & """email"":""" & user.Email & ""","
            json = json & """role"":""" & user.Role & ""","
            json = json & """createdAt"":""" & FormatDateTime(user.CreatedAt) & """"
            json = json & "}"
            
            first = False
        Next
        
        json = json & "]"
        
        ' No error checking
        Return json
    End Function
    
    ' This section should be ignored by CRA due to cleanup prompt #2
    ' * Legacy Code *
    Sub legacy_process_data()
        ' Legacy code with inconsistent naming conventions
        Dim DATA_ITEMS as Integer = 100
        dim temp_var as String = ""
        
        ' Legacy implementation...
    End Sub
    
    ' Function without proper documentation
    ' (Violates Generative Prompt #14)
    Private Function FormatDateTime(dt)
        Return dt.ToString("yyyy-MM-dd'T'HH:mm:ss.fff'Z'")
    End Function
    
    ' This section should be ignored by CRA due to cleanup prompt #5
    ' * Custom Initialization *
    Sub InitializeComponents()
        ' Custom initialization patterns
        Dim controls
        Dim settings
        
        ' Custom initialization logic...
        
        controls = New Object()
        settings = "default"
    End Sub
    
    ' Boolean comparison in conditional compilation block
    ' should be ignored by CRA due to cleanup prompt #9
    #If DEBUG Then
        Sub DebugMethod()
            Dim isDebug As Boolean = True
            If isDebug = True Then
                Console.WriteLine("Debug mode is active")
            End If
        End Sub
    #End If
End Module

' Class without proper access modifier
' (Violates Generative Prompt #11)
Class User
    Public ID As String
    Public Name As String
    Public Email As String
    Public Role As String
    Public CreatedAt As DateTime
    Public Metadata As Dictionary(Of String, String)
    
    ' Method without proper parameter specification
    ' (Violates Generative Prompt #4)
    Public Sub AddMetadata(key, value)
        If Metadata Is Nothing Then
            Metadata = New Dictionary(Of String, String)
        End If
        
        ' No error checking for duplicate keys
        Metadata.Add(key, value)
    End Sub
    
    ' This private method should be ignored by CRA due to cleanup prompt #1
    Private Sub InternalProcessing()
        ' Implementation details...
    End Sub
End Class
