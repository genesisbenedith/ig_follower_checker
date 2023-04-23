"""
Author: Genesis Benedith 
Purpose: finds the instagram users that you follow that don't follow you back and writes them to a csv file
Created: 2023-22-04 
Edited: 2023-22-04
"""

import json
not_following_back = []

with open('followers_1.json', 'r') as f:
    follower_file = f.read()
    follower_ids = []
    follower_file = follower_file.split()
    for i in range(len(follower_file)):
        if '"value":' in follower_file[i]:
            follower_ids.append(follower_file[i+1].replace(',', ''))
    for i in range(len(follower_ids)):
        follower_ids[i] = follower_ids[i].replace('"', '')
with open('following.json', 'r') as f:
    following_file = f.read()
    following_ids = []
    following_file = following_file.split()
    for i in range(len(following_file)):
        if '"value":' in following_file[i]:
            following_ids.append(following_file[i+1].replace(',', ''))
    for i in range(len(following_ids)):
        following_ids[i] = following_ids[i].replace('"', '')
    for i in range(len(following_ids)):
        if following_ids[i] not in follower_ids:
            not_following_back.append(following_ids[i])

    with open('not_following_back.csv', 'w') as f:
        for i in range(len(not_following_back)):
            f.write(not_following_back[i] + '\n')
    

    
