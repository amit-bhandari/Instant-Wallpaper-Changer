'''
 Copyright 2017 Amit Bhandari AB

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
 http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
'''

import platform

class Wallpaper:
	def change(self,image_path):
		sysOs = self.getOs().lower();
		import os.path
		if os.path.isfile(image_path) != True:
			raise IOException("Provided image is invalid.")
		print("OS is " + sysOs)
                if sysOs == 'windows':
			self.changeWallpaperWindows(image_path)
			return True
		elif sysOs == 'linux':
			import os
			os.system("gsettings set org.gnome.desktop.background picture-uri file://" + image_path)
			return True
	 	elif sysOs == 'darwin':
			import subprocess
			import random
			print(image_path)
			temp_path=image_path+str(random.randint(1,1000)) 	#create a copy of image, if same image path is given everytime, dock does not refresh
			os.popen('cp %s %s'%(image_path, temp_path))      
			SCRIPT = """/usr/bin/osascript<<END
			tell application "Finder"
			set desktop picture to POSIX file "%s"
			end tell
			END"""
			p1 = subprocess.Popen(SCRIPT%temp_path, shell=True)
			p1.wait()
			os.remove(temp_path) #delete temp file
        	else:
			raise Exception("Platform is not supported yet!")

	def isX64(self):
		import struct
		return struct.calcsize('P') * 8 == 64

	def changeWallpaperWindows(self, image_path):
		import ctypes
		SPI_SETDESKWALLPAPER = 20
		if self.isX64():
			ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 0)
		else:
			ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, image_path, 0)

	def getOs(self):
		return platform.system()
