import urllib
import threading
import sys
import time
from data.color import *
nums=0
class admin(threading.Thread):
	def __init__(self,url,list,berapa):
		threading.Thread.__init__(self)
		self.url=url
		self.list=list
		self.berapa=berapa
	def run(self):
		global nums
		nums+=1
		try:
			url=urllib.urlopen("{}/{}".format(self.url,self.list))
			if (url.getcode() == 200):
				print("\r | {}/{}   {}[found]{}".format(
					self.url,self.list,G,N
				))
		except:
			pass
