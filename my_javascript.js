// Unused constants (similar to your example)
const TicketCategories = ["Bug", "Feature", "Support"];
const unresolvedTickets = [];

// Unused imports
import React from 'react';
import { useState, useEffect } from 'react';
import axios from 'axios';

// Unused function parameters
function processTicket(ticketId, userId, priority, category, timestamp) {
  console.log(`Processing ticket: ${ticketId}`);
  // Only ticketId is used, other parameters are unused
}

// Unused variables in function
function getTicketStats() {
  const totalTickets = 100;
  const resolvedCount = 75;
  const pendingReview = 15;
  
  // Only returning one variable, others are unused
  return totalTickets;
}

// Unused class properties
class TicketManager {
  constructor() {
    this.maxTickets = 500;
    this.autoAssign = true;
    this.priorityLevels = ["Low", "Medium", "High", "Critical"];
    this.notificationEnabled = false;
  }
  
  getOpenTickets() {
    // Only using one property
    console.log(`Max tickets allowed: ${this.maxTickets}`);
    return [];
  }
}

// Unused function
function calculateAverageResponseTime(tickets) {
  let total = 0;
  for (let ticket of tickets) {
    total += ticket.responseTime;
  }
  return total / tickets.length;
}

// Unused arrow function stored in a variable
const sortTicketsByPriority = (tickets) => {
  return tickets.sort((a, b) => b.priority - a.priority);
};

// Declared but never used object
const ticketSystemConfig = {
  baseUrl: 'https://api.ticketsystem.com',
  timeout: 5000,
  retryAttempts: 3,
  apiKey: 'abcd1234'
};

// Function with unused return value
function createTicket(title, description) {
  const ticketId = `TICKET-${Math.floor(Math.random() * 10000)}`;
  console.log(`Created ticket: ${title}`);
  // Return value is never used anywhere
  return ticketId;
}

// Unused async function
async function fetchTicketData() {
  try {
    const response = await fetch('https://api.example.com/tickets');
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Failed to fetch ticket data');
    return [];
  }
}

// Unused variables in a loop
function processTicketBatch(tickets) {
  for (let i = 0; i < tickets.length; i++) {
    const ticket = tickets[i];
    const id = ticket.id;
    const status = ticket.status;
    const assignee = ticket.assignee;
    
    // Only using id, other variables are unused
    console.log(`Processing ticket ID: ${id}`);
  }
}

// Unused event handlers
function setupTicketListeners() {
  const handleTicketClick = (e) => {
    console.log('Ticket clicked');
  };
  
  const handleTicketAssign = (e) => {
    console.log('Ticket assigned');
  };
  
  const handleTicketClose = (e) => {
    console.log('Ticket closed');
  };
  
  // Only using one handler
  document.getElementById('ticketList').addEventListener('click', handleTicketClick);
}

// Unused destructured variables
function displayTicketInfo(ticket) {
  const { id, title, description, priority, category, assignee, created_at, updated_at } = ticket;
  
  // Only using id, title and priority
  console.log(`Ticket #${id}: ${title} (Priority: ${priority})`);
}

// Main function with multiple unused variables
function main() {
  const appVersion = '1.0.0';
  const isDevelopment = true;
  const maxConcurrentRequests = 5;
  const supportedLanguages = ['en', 'es', 'fr', 'de'];
  
  console.log('Ticket System Started');
  
  // None of the declared variables are used
}

// Call the main function
main();

// Unused export
export const TicketStatus = {
  OPEN: 'open',
  IN_PROGRESS: 'in_progress',
  RESOLVED: 'resolved',
  CLOSED: 'closed'
};

// Export used functions
export { processTicket, getTicketStats, TicketManager };
