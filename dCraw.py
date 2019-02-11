#-*-coding:utf-8-*-
# dCraw By Deray
# Report Bug On My Other Sosmed:
#	Fb: https://facebook.com/achmad.luthfi.hadi.3
#	Ig: https://instagram.com/reyy05_

import os
import sys,urllib
from time import *
from tools import jm
from tools import wp
from data.color import *
from tools import admin
from tools import email
from threading import Thread

cout=0
threads=[]


banner = """{}
     _ _____                    _      
    | /  __ \                  | |     
  __| | /  \/_ __ __ ___      _| |     
 / _` | |   | '__/ _` \ \ /\ / / |     
| (_| | \__/\ | | (_| |\ V  V /| |____ 
 \__,_|\____/_|  \__,_| \_/\_/ \_____/    {}{} by Deray{}
===================================================
                           
  {}[{}1{}]{} Scan For Joomla! Components
  {}[{}2{}]{} Scan For Wordpress Plugin
  {}[{}3{}]{} Scan For Admin Login
  {}[{}4{}]{} Scan For Hidden Webshell
  {}[{}5{}]{} Scan For Valid Email Checker
  {}[{}0{}]{} Go Fuck Yourself
""".format(
	C,W,R,N,C,R,C,N,C,R,C,N,C,R,C,N,C,R,C,N,C,R,C,N,C,R,C,N)
print(banner)

# Menu

class menu():
	def __init__(self):
		s=raw_input("{}[{}+{}]{} Select Option : ".format(
			C,R,C,N))
		if (s == "1"):
			self.inputTarget()
			self.jm()
		elif (s == "2"):
			self.inputTarget()
			self.wp()
		elif (s == "3"):
			self.inputTarget()
			self.adm00n()
		elif (s == "4"):
			self.shell()
		elif (s == "5"):
			self.mail()
		elif (s == "0"):
			sys.exit()
		elif (s == ""):
			menu()
		else:
			print("{}[-]{} invalid option: {}".format(R,N,s))
			return menu()
			
	# Wordlist
	def inputWords(self):
		try:
			self.words=open(raw_input("{}[{}+{}]{} Your Wordlist: ".format(C,R,C,N))).read().splitlines()
		except Exception as f:
			print("{}[!]{} {} ".format(R,N,f))
			return self.inputWords()
	
	# Input Your Target		
	def inputTarget(self):
		self.target=raw_input("\r{}[{}+{}]{} Target Uri: ".format(
			C,R,C,N
		))
		if (self.target == ""):
			return self.inputTarget()
	
	# Joomla Components Detector		
	def jm(self):
		global cout
		print("\r{}[{}+{}]{} Fetching Wordlists ...".format(
			C,R,C,N
		))
		wlist=open("db/components.txt").read().splitlines()
		print("\r{}[{}+{}]{} Fetched {} wordlists".format(
			C,R,C,N,
		len(wlist)))
		for x in wlist:
			cout+=1
			print("\r{}[{}+{}]{} Loaded {} Wordlists ...".format(
				C,R,C,N,cout)),;sys.stdout.flush()
			t=jm.jm(self.target,x,len(wlist))
			threads.append(t)
		for t in threads:
			t.start()
		for t in threads:
			t.join()
		print("{}[{}+{}]{} Finished.".format(C,R,C,N))
	
	# Wordpress Plugin Crawler		
	def wp(self):
		global cout
		print("\r{}[{}+{}]{} Fetching Wordlists ...".format(
			C,R,C,N
		))
		wlist=open("db/plugins.txt").read().splitlines()
		print("\r{}[{}+{}]{} Fetched {} wordlists".format(
			C,R,C,N,len(wlist
		)))
		for x in wlist:
			cout+=1
			print("\r{}[{}+{}]{} Loaded {} Wordlists ...".format(
				C,R,C,N,cout)),;sys.stdout.flush()
			t=wp.wp(self.target,x,len(wlist))
			threads.append(t)
		for t in threads:
			t.start()
		for t in threads:
			t.join()
		print("{}[{}+{}]{} Finished.".format(C,R,C,N))
			
	# Admin Finder		
	def adm00n(self):
		global cout
		print("\r{}[{}+{}]{} Fetching Wordlists ...".format(
			C,R,C,N
		))
		wlist=urllib.urlopen("db/admin.txt").read().splitlines()
		print("\r{}[{}+{}]{} Fetched {} wordlists".format(
			C,R,C,N,len(wlist
		)))
		for x in wlist:
			cout+=1
			print("\r{}[{}+{}]{} Loaded {} Wordlists ...".format(
				C,R,C,N,cout)),;sys.stdout.flush()	
			t=admin.admin(self.target,x,len(wlist))
			threads.append(t)
		for t in threads:
			t.start()
		for t in threads:
			t.join()
		print("{}[{}+{}]{} Finished.".format(C,R,C,N))
	
	# Hidden Webshell Scan		
	def shell(self):
		global cout
		print """
		{}[{} Why Did U Like? {}]
	
	{}1{}){} Scan Manual With Your Wordlists
	{}2{}){} Default
		""".format(R,C,R,C,R,N,C,R,N)
		self.opt=raw_input("{}[{}+{}]{} Choice>> ".format(C,R,C,N))
		if (self.opt == "1"):
			self.inputWords()
			self.inputTarget()
			print("\r{}[{}+{}]{} Fetching Wordlists ...".format(
			C,R,C,N
			))
			print("\r{}[{}+{}]{} Fetched {} Words ...".format(
				C,R,C,N,len(self.words
			)))
			for x in self.words:
				cout+=1
				print("\r{}[{}+{}]{} Loaded {} Wordlists ...".format(
					C,R,C,N,cout)),;sys.stdout.flush()
				t=admin.admin(self.target,x,len(self.words))
				threads.append(t)
			for t in threads:
				t.start()
			for t in threads:
				t.join()
			print("{}[{}+{}]{} Finished.".format(C,R,C,N))
		elif (self.opt == "2"):
			self.inputTarget()
			r=urllib.urlopen("{}/wp-content/".format(
				self.target
			)).getcode()
			if (r == 200):
				print("\r{}[!]{} Warning: Detected For Cms Wordpress!".format(R,N))
				print("\r{}[!]{} Bruteforcing Webshell With Wplist.txt ...".format(R,N))
				print("\r{}[{}+{}]{} Fetching Wordlists ...".format(
					C,R,C,N
				))
				self.list=open("db/shell/wplist.txt").read().splitlines()
				print("{}[{}+{}]{} Fetched {} Words ...".format(C,R,C,N,len(self.list)))
				for x in self.list:
					cout+=1
					print("\r{}[{}+{}]{} Loaded {} Wordlists ...".format(
				C,R,C,N,cout)),;sys.stdout.flush()
					t=admin.admin(self.target,x,len(self.list))
					threads.append(t)
				for t in threads:
					t.start()
				for t in threads:
					t.join()
				print("{}[{}+{}]{} Finished.".format(C,R,C,N))
			else:
				print("\r{}[{}+{}]{} Fetching Wordlists ...".format(
					C,R,C,N
				))
				self.list=open(
					"db/shell/randomlist.txt"
				).read().splitlines()
				print("{}[{}+{}]{} Fetched {} Words ...".format(C,R,C,N,len(self.list)))
				for x in self.list:
					cout+=1
					print("\r{}[{}+{}]{} Loaded {} Wordlists ...".format(
					C,R,C,N,cout)),;sys.stdout.flush()
					t=admin.admin(self.target,x,len(self.list))
					threads.append(t)
				for t in threads:
					t.start()
				for t in threads:
					t.join()
				print("{}[{}+{}]{} Finished.".format(C,R,C,N))
		else:
			print("{}[!]{} Invalid Option!".format(R,N))
			return self.shell()
	# Mass Email Valid Checker
	def mail(self):
		try:
			self.mailist=open(raw_input("{}[{}+{}]{} Mailist: ".format(
				C,R,C,N
			))).read().splitlines()
			self.lokupmail()
		except Exception as f:
			print("{}[!]{} {}".format(R,N,f))
			return self.mail()
	def lokupmail(self):
		global cout
		print("\r{}[{}+{}]{} Fetched {} Email ...   ".format(
			C,R,C,N,len(self.mailist
		)))
		if (os.path.exists("email/valid.txt")):
			r=raw_input("{}[!]{} Valid File Exists! in email/valid.txt\n{}[{}+{}]{} Did U want to [R]replace or [D]elete? ".format(
				R,N,C,R,C,N
			))
			if (r.lower() == "d"):
				os.remove("email/valid.txt")
				os.rmdir("email")
		for x in self.mailist:
			cout+=1
			print("\r{}[{}+{}]{} Loaded {} Wordlists ...".format(
				C,R,C,N,cout)),;sys.stdout.flush()
			t=email.email(x,len(self.mailist))
			threads.append(t)
		for t in threads:
			t.start()
		for t in threads:
			t.join()
		email.valid.close()
		v=len(open("email/valid.txt").read().splitlines())
		if v !=0:
			print("{}[{}+{}]{} Finished.".format(C,R,C,N))
			print("\r{}[{}+{}]{} Valid {} Email".format(C,R,C,N,v))
			print("{}[{}+{}]{} Output: email/valid.txt".format(C,R,C,N))
		else:
			print("{}[{}+{}]{} Finished.".format(C,R,C,N))
			print("{}[!]{} No Result Email Valid Found.".format(R,N))
			os.remove("email/valid.txt")
			os.rmdir("email")
menu()
