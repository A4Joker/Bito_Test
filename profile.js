import twit from 'twit';
import config from './config';

let get = (username) => {
  const twitter = new twit(config);
  twitter.get('/users/show', {screen_name:username}, {timeout: 5000}, (err,data,response) => {
    if(err){
      if(err.code === 'ETIMEDOUT' || err.code === 'ECONNREFUSED') {
        console.log(`Network error while fetching data for ${username}: ${err.message}`);
      } else {
        console.log(`Twitter API error for ${username}: ${err.message}`);
      }
    }else{
      console.log(`${data.name} has ${data.statuses_count} statuses, ${data.friends_count} friends, and ${data.followers_count} followers.`)
    }
  });
}

module.exports = { get }
