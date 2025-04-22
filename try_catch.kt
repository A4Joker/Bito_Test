package com.example.service

import com.example.model.User
import com.example.model.UserPreferences
import com.example.model.UserActivity
import com.example.api.ApiClient
import com.example.util.Logger

/**
 * UserService.kt
 * A service for managing user operations with multiple null safety and try/catch issues
 */
class UserService(private val apiClient: ApiClient, private val logger: Logger?) {

    /**
     * Gets a user by ID
     * ISSUE: Unsafe calls on nullable types
     */
    suspend fun getUserById(userId: String): User {
        val response = apiClient.get("/users/$userId")
        
        // Unsafe !! operator used multiple times
        val userData = response.data!!.user!!
        
        // Potential NPE with unsafe calls on nested properties
        return User(
            id = userData.id!!,
            name = userData.profile!!.name!!,
            email = userData.contact!!.email!!,
            role = userData.permissions!!.role!!
        )
    }

    /**
     * Creates a new user
     * ISSUE: Missing try/catch for error handling
     */
    suspend fun createUser(userData: Map<String, Any>): User? {
        // No try/catch to handle potential errors
        val response = apiClient.post("/users", userData)
        
        return if (response.status == 201) {
            // Unsafe cast without checking
            response.data?.user as User
        } else {
            null
        }
    }

    /**
     * Updates user information
     * ISSUE: Improper try/catch (doesn't handle the error properly)
     */
    suspend fun updateUser(userId: String, userData: Map<String, Any>): User? {
        try {
            val response = apiClient.put("/users/$userId", userData)
            return response.data?.user as User
        } catch (e: Exception) {
            // Just logs the error without proper handling
            println("Error updating user")
            // No return statement after error
        }
        
        // Implicit return of null if exception occurs
    }

    /**
     * Deletes a user
     * ISSUE: Catches error but doesn't do anything with it
     */
    suspend fun deleteUser(userId: String): Map<String, Boolean> {
        try {
            apiClient.delete("/users/$userId")
            return mapOf("success" to true)
        } catch (e: Exception) {
            // Empty catch block - swallows the error
        }
        
        // Unreachable code - this will never execute if an exception occurs
        return mapOf("success" to false)
    }

    /**
     * Gets user preferences
     * ISSUE: Accesses nested properties without null checks
     */
    suspend fun getUserPreferences(userId: String): UserPreferences {
        val response = apiClient.get("/users/$userId/preferences")
        
        // Multiple nested property accesses without proper null handling
        return UserPreferences(
            theme = response.data.preferences.display.theme,
            language = response.data.preferences.locale.language,
            notificationsEnabled = response.data.preferences.communication.notifications.enabled,
            emailFrequency = response.data.preferences.communication.email.frequency
        )
    }

    /**
     * Processes user activity
     * ISSUE: Improper null handling with Elvis operator
     */
    fun processUserActivity(activity: UserActivity?): Map<String, Any> {
        // Elvis operator used incorrectly - activity could still be null
        val activityType = activity?.type ?: "view"
        val timestamp = activity?.timestamp ?: System.currentTimeMillis()
        
        // This will throw NPE if activity is null
        val duration = activity?.duration ?: 0
        
        // This will throw NPE if activity is null or activity.data is null
        val details = activity?.data?.toMap() ?: emptyMap()
        
        return mapOf(
            "type" to activityType,
            "timestamp" to timestamp,
            "duration" to duration,
            "details" to details
        )
    }

    /**
     * Validates user data
     * ISSUE: Inconsistent return types and null safety
     */
    fun validateUserData(userData: Map<String, Any?>): Any {
        // Unsafe cast without checking
        val name = userData["name"] as? String
        
        if (name == null || name.isEmpty()) {
            // Returns a string in error case
            return "Name is required"
        }
        
        // Unsafe cast and no null check
        val email = userData["email"] as String
        
        if (email.isEmpty()) {
            // Returns a string in error case
            return "Email is required"
        }
        
        // Nullable type with unsafe cast
        val age = userData["age"] as? Int
        
        if (age != null && age < 18) {
            // Returns a string in error case
            return "User must be at least 18 years old"
        }
        
        // Returns boolean in success case (inconsistent return types)
        return true
    }

    /**
     * Gets user statistics
     * ISSUE: Try/catch with improper error handling and null checks
     */
    suspend fun getUserStatistics(userId: String): Map<String, Int>? {
        try {
            val response = apiClient.get("/users/$userId/statistics")
            
            // No null check before accessing nested properties
            val stats = response.data.statistics
            
            return mapOf(
                "postsCount" to stats.posts.count,
                "commentsCount" to stats.comments.count,
                "likesCount" to stats.interactions.likes,
                "viewsCount" to stats.interactions.views
            )
        } catch (e: Exception) {
            // Returns null instead of proper error handling
            return null
        }
    }

    /**
     * Searches for users
     * ISSUE: No error handling at all
     */
    suspend fun searchUsers(query: String): List<User> {
        // No try/catch or any error handling
        val response = apiClient.get("/users/search", mapOf("q" to query))
        
        // No null check before mapping, potential NPE
        return response.data.users.map { user ->
            User(
                id = user.id,
                name = user.name,
                email = user.email,
                role = user.role
            )
        }
    }

    /**
     * Gets user roles
     * ISSUE: Nested try/catch with improper error handling
     */
    suspend fun getUserRoles(userId: String): List<String> {
        try {
            val response = apiClient.get("/users/$userId/roles")
            
            try {
                // Nested try/catch is often a code smell
                // No null check before accessing properties
                return response.data.roles.map { it.name }
            } catch (innerError: Exception) {
                // Just logs without proper handling
                println("Error processing roles")
                return emptyList()
            }
        } catch (outerError: Exception) {
            // Different handling in outer catch
            logger?.error("API error", outerError)
            throw outerError // Rethrows here but not in inner catch
        }
    }
    
    /**
     * Handles null logger issue
     * ISSUE: Unsafe call on nullable property
     */
    fun logActivity(activity: String) {
        // Unsafe call on nullable logger
        logger!!.info(activity)
    }
    
    /**
     * Parses user data
     * ISSUE: Unchecked cast and unsafe assertions
     */
    fun parseUserData(data: Any?): User {
        // Unchecked cast
        val map = data as Map<String, Any>
        
        // Multiple unsafe assertions and potential NPEs
        return User(
            id = map["id"] as String,
            name = map["name"] as String,
            email = map["email"] as String,
            role = map["role"] as String
        )
    }
}
