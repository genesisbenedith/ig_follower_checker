/*
Author: Genesis Benedith 
Purpose: finds the instagram users that you follow that don't follow you back and writes them to a txt file
Created: 2023-23-10 
Edited: 2023-23-10 
*/

const followersList = require('./followers_1.json');
const followingsList = require('./following.json');

const fs = require('fs');

var followers = Array();
var following = Array();
var users_not_following_back = Array();

for (let i = 0; i < followersList.length; i++) {
    followers.push(followersList[i].string_list_data[0].value);
}

for (let i = 0; i < followingsList.relationships_following.length; i++) {
    following.push(followingsList.relationships_following[i].string_list_data[0].value);
}

for (let i = 0; i < following.length; i++) {
    if (followers.includes(following[i]) == false) {
        users_not_following_back.push(following[i]);
        fs.appendFile('users_not_following_back.txt', `${following[i]}\n`, (err) => { 

            if (err) {
                throw err
            }; 
        });
    }
}
	
console.log(`${users_not_following_back.length} users not following you back.`);
console.log("See file 'users_not_following_back.txt'");



