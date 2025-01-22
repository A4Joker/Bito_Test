let profile = require('./profile');

let profiles = process.argv.slice(2);

profiles.map(profile.get);
