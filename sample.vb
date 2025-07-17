Option Explicit On
Option Strict On
Option Infer Off
 
Imports System
Imports System.Collections
Imports System.Collections.Generic
Imports System.IO
Imports System.Text

Module UserManagement
    ' Global variables without proper naming
    Public users_list As New List(Of User)
    Public MaxUsers = 100
    Public default_role = "USER"
    
    ' Missing proper error handling
    Sub Main()
        On Error GoTo ErrorHandler
        
        ' Implicit variable (missing Dim)
        Dim counter As Integer = 0
        
        ' Poor naming (no prefix for form controls)
        Dim txtName As TextBox = New TextBox()
        Dim txtEmail As TextBox = New TextBox()
        Dim btnSubmit As Button = New Button()
        
        ' String concatenation instead of interpolation
        Console.WriteLine("Starting user management system with " & MaxUsers & " maximum users")
        
        ' Create some users
        AddUser("John Doe", "john@example.com", "ADMIN")
        AddUser("Jane Smith", "jane@example.com", "")
        
        ' Comparing boolean with True
        If IsUserValid("John Doe", "john@example.com") = True Then
            Console.WriteLine("User is valid")
        End If
        
        ' Nested conditionals (excessive nesting)
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
        Dim writer As StreamWriter = New StreamWriter("users.txt")
        writer.WriteLine("User List:")
        For Each user In users_list
            writer.WriteLine(user.Name & "," & user.Email & "," & user.Role)
        Next
        writer.Close()
        
        Exit Sub
        
ErrorHandler:
        ' Poor error handling
        Console.WriteLine("An error occurred: " & Err.Description)
        Resume Next
    End Sub
    
    ' Function without proper parameter passing specification
    Function AddUser(Name, Email, Role)
        ' Implicit variable type
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
        
        user.CreatedAt = DateTime.Now
        
        ' No error handling
        users_list.Add(user)
        
        ' Concatenation instead of interpolation
        Console.WriteLine("Added user: " & Name & " with role: " & user.Role)
        
        Return user
    End Function
    
    ' Function without return type
    Function IsUserValid(Name, Email)
        ' Poor variable naming
        Dim x As Boolean = False
        
        For Each u In users_list
            If u.Name = Name And u.Email = Email Then
                x = True
                Exit For
            End If
        Next
        
        Return x
    End Function
    
    ' Procedure with ambiguous parameter passing
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
    
    ' Function with poor error handling
    Function ExportUsersToJson()
        On Error Resume Next
        
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
    
    ' Function without proper documentation
    Private Function FormatDateTime(dt)
        Return dt.ToString("yyyy-MM-dd'T'HH:mm:ss.fff'Z'")
    End Function
    
    ' Sub with poor resource management
    Sub LoadUsersFromFile(filePath)
        ' No error handling
        Dim reader As New StreamReader(filePath)
        
        Do While Not reader.EndOfStream
            Dim line As String = reader.ReadLine()
            Dim parts As String() = line.Split(","c)
            
            If parts.Length >= 3 Then
                AddUser(parts(0), parts(1), parts(2))
            End If
        Loop
        
        ' Resource not properly closed
        reader.Close()
    End Sub
End Module

' Class without proper structure
Public Class User
    Public ID As String
    Public Name As String
    Public Email As String
    Public Role As String
    Public CreatedAt As DateTime
    Public Metadata As Dictionary(Of String, String)
    
    ' Method without proper parameter specification
    Public Sub AddMetadata(key, value)
        If Metadata Is Nothing Then
            Metadata = New Dictionary(Of String, String)
        End If
        
        ' No error checking for duplicate keys
        Metadata.Add(key, value)
    End Sub
End Class
