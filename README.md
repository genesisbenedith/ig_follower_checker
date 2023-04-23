# ig_follower_checker
This is a Python script that checks which Instagram accounts are not following you back. 

# Features

- Easily identify who is not following you back on Instagram.
- Simple and flexible command-line interface using JSON input and CSV output.
- Easy installation and setup with detailed instructions.
- Works on any platform with Python 3 and a web browser.
- No need to provide your Instagram login information or use a third-party service.
- Export your results to a CSV file and analyze them in your favorite spreadsheet software.

# Installation
To use this script, you need to have Python 3 installed on your computer.

# Steps
The script requires two JSON files: one with your list of followers and another with the list of accounts you are following. You can download these files from Instagram by following the steps below:

1. Log in to your Instagram account in a web browser.
2. Click on "More" in the sidebar in the bottom-left corner.
3. Go to "Your activity" on the drop down menu.
4. Navigate to the "Download your information" page.
5. Enter your email of your preference to receive a notification when your file is ready to download.
6. Select JSON as the format then click on "Next".
7. Enter your email and click "Submit". 

You will receive an email with the link to your download. It may take a few minutes, if not, up to 14 days.

8. Open the email and click the link, then select "Download information".
9. Download the ZIP file and unzip it to access the two JSON files, "followers_1.json" and "following.json" in the "followers_and_following" folder.
10. Download the Python script from the Github repository.
11. Open your terminal or command prompt and navigate to the directory where the script and the JSON files are located using the "cd" command. For example, if you downloaded the files to your Downloads folder, you could use the following command:

```
cd ~/Downloads/
```

12. Once you are in the correct directory, run the script by entering the following command in your terminal:

```
python instagram_unfollower_checker.py --followers followers_1.json --following following.json --output not_following_back.csv
```

Note that you may need to modify the file names in the above command to match the actual names of the JSON files that you downloaded.

The script will run and generate a CSV file named "not_following_back.csv" in the same directory. You can open this file in a spreadsheet program like Microsoft Excel to view the results.

# License
This script is licensed under the GPL v3.0 License. See the LICENSE file for more information.
