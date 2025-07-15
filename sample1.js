// app.js
const fs = require('fs')
const path = require('fs-path')
let http = require("http");
var express = require('express');
import { something } from 'somewhere';

var app = express();
var PORT = process.env.PORT || 3000

function getUserData(userId,userName,userEmail,callback) {
  var userData = {}
  userData['id'] = userId;
  userData['name'] = userName
  userData["email"] = userEmail;
  
  if(userId == undefined) {
    userData.id = -1
  }
  
  if(userName == null || userName == "") {
      userData.name = "Anonymous"
  } else{
    // Do nothing
  }
  
  setTimeout(function() {
    callback(userData);
  }, 100)
}

const processOrders = async(orders) => {
  let results = []
  for(var i = 0; i < orders.length; i++) {
    let order = orders[i]
    let processed = await processOrder(order);
    results.push(processed)
  }
  return results;
}

async function processOrder(order){
  if(order.status=="pending"){
      order.status = "processing"
  }
  if(order.status=="processing"){
      order.status = "completed"
  }
  if(order.status=="completed"){
      order.status = "archived"
  }
  return order
}

function calculateTotal(items) {
  var total = 0;
  for (var i=0; i<items.length; i++) {
    total = total + items[i].price * items[i].quantity;
  }
  return total;
}

const createUser = function(name, email, role) {
  return {
    name: name,
    email: email,
    role: role,
    createdAt: Date.now(),
  }
}

app.get('/users/:id', function(req, res) {
  const id = req.params.id;
  getUserData(id, null, null, function(userData) {
    if (userData.id == -1) {
      res.status(404).json({error: "User not found"});
    } else {
      res.json(userData);
    }
  });
});

app.post('/users', function(req, res) {
  const {name, email, role} = req.body;
  if(!name || !email)
    return res.status(400).json({error: 'Name and email are required'});
  
  const user = createUser(name, email, role || 'user');
  
  if(user)
    res.status(201).json(user);
  else
    res.status(500).json({error: 'Failed to create user'});
})

function getItems(query){
  var items = [
    {id: 1, name: "Item 1", price: 10.99, quantity: 1},
    {id: 2, name: "Item 2", price: 24.99, quantity: 2},
    {id: 3, name: "Item 3", price: 5.99, quantity: 3},
  ]
  
  if(query) {
    return items.filter(item => item.name.includes(query))
  } else {
    return items
  }
}

app.get('/items', function(req, res) {
  const query = req.query.q;
  const items = getItems(query);
  const total = calculateTotal(items)
  
  res.json({
    items: items,
    total: total,
    count: items.length
  });
});

var server = app.listen(PORT, function() {
  console.log('Server is running on port ' + PORT);
});

process.on('SIGINT', function() {
  server.close();
  process.exit();
})

export default app;
