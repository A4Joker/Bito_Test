const twit = require('twit');
const config = require('./config');

let get = (username) => {
  const twitter = new twit(config);
  twitter.get('/users/show',{screen_name:username}, (err,data,response) => {
    if(err){
      console.log(`Username: ${username} => ${err.message}`);
    }else{
      console.log(`${data.name} has ${data.statuses_count} statuses, ${data.friends_count} friends, and ${data.followers_count} followers.`)
    }
  });
}

module.exports = { get }
