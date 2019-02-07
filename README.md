# quick-wallpaper-changer-linux
Quickly change wallpaper by typing couple words OR download all 100 HD latest wallpapers from google search by giving search term.

Ever came something/someone in mind and wanted to change your wallapaper according to mood?  What to do? 

Do you do the following? If yes, you are in a luck.<br />

Go to goole -> search something -> find good photo -> download -> browse to directtory -> set wallpaper

This script will does all that in couple words after setup.

### Updated for Windows. 
You can use changewall_windows.py to change wallpaper for Windows OS. Tested in Windows 10 64 bit. 

# Steps to setup
-> Download the script in desired location <br /> 
-> Change PHOTO_PATH in script and mention path where you want photo to be downloaded. <br />
-> Install any missing packages by "pip install <package_name>" <br /> OR pip install -r requirements.txt
-> If you don't have pip, install pip. Instructions here --> https://www.saltycrane.com/blog/2010/02/how-install-pip-ubuntu/  <br />
-> [optional] Copy the script in /usr/bin to get direct access from terminal. <br />
-> Enjoy! <br />

# Example usage - 

./changewall.py -s "Lamborghini" 
./changewall.py -s "Kate Upton"

And you are done!

Script will randomly pick one of the image shown below (actually out of 100 image which google will return) and will set it as wallpaper.


![alt text](https://user-images.githubusercontent.com/16557921/36028887-d476c5c2-0dc6-11e8-874a-d457c75e9872.png)

<br />

![alt text](https://user-images.githubusercontent.com/16557921/36025163-133b106a-0db8-11e8-8590-f6f28c165308.png)

