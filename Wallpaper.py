import platform

class Wallpaper:
	def change(self,image_path):
		sysOs = self.getOs().lower();
		import os.path
		if os.path.isfile(image_path) != True:
			raise IOException("Provided image is invalid.")
		if sysOs == 'windows':
			self.changeWallpaperWindows(image_path)
			return True
		elif sysOs == 'linux':
			import os
			os.system("gsettings set org.gnome.desktop.background picture-uri file://" + image_path)
			return True
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
