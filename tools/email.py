import re
import os
import sys
import threading
from data.color import *
from requests import post

valid=""
cout=0

class email(threading.Thread):
	def __init__(self,mailist,brerapa):
		threading.Thread.__init__(self)
		self.mailist=mailist
		self.berapa=brerapa
		self.cek()
		
	def cek(self):
		global valid
		if (os.path.exists("email")):
			valid=open("email/valid.txt","a")
		else:
			os.mkdir("email")
			valid=open("email/valid.txt","w")
		
	def run(self):
		global valid,cout
		cout+=1
		url="https://www.ip-tracker.org/checker/email-lookup.php"
		try:
			r=post(url,data={"email":self.mailist
				,"submit":"Check Email Address"},
				headers={"User-Agent":"Mozilla 5.1 (Linux Android"}
			).text
			reg=re.findall(
			"is <br />a valid deliverable e-mail box address.</div>",r
			)
			if (len(reg) !=0):
				print("\r | {}   {}[valid]{}".format(self.mailist,G,N))
				valid.write(self.mailist+"\n")
		except:
			pass