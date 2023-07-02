import os
import subprocess as sb
from time import sleep

def configure_apache_webserver():
	out = sb.getstatusoutput("rpm -q httpd")
	if out[0] == 1:
		if 'not installed' in out[1]:
			sb.call("echo 'Installing httpd software....'", shell=True)
			out = sb.getstatusoutput('yum install httpd -y')
			if 'complete!' in out[1]:
				sb.call("echo 'Successfully installed httpd...'", shell=True)
	else:
		print("httpd software already installed! ")
		sb.call("echo 'Configuring Web server...'", shell=True)
		out = sb.getstatusoutput("yum install httpd -y")
		if 'complete!' in out[1]:
			sb.call("echo 'Successfully installed httpd...'", shell=True)
		sb.call("echo 'Enabling service...'", shell= True)
		sleep(1)
		sb.getstatusoutput("systemctl start httpd")
		sb.call("echo 'Started the service Successfully....'", shell=True)
		sleep(1)
		sb.call("systemctl status httpd", shell=True)

def web_status():
	os.system("tput setaf 7")
	sb.call("systemctl status httpd", shell = True)

def web_stop():
	sb.call("echo 'Stoping httpd Service..'", shell = True)
	sb.call("systemctl stop httpd", shell = True)
	sb.call("echo 'Service stopped Successfully!'", shell = True)

def webserver():
	while True:
		os.system('tput setaf 10')
		print("""
			-----------------------------------------------------
				Welcome to Apache2 Webserver!:
			-----------------------------------------------------	
				1. Configure httpd Web Server
				2. Web Server status
				3. Stop Web Server
				4. Main Menu
			-----------------------------------------------------
			""")
		os.system("tput setaf 2")
		ch  = ""
		while ch == "":
			ch = input("Enter choice : ")
		ch = int(ch)

		if ch == 1:
			configure_apache_webserver()

		elif ch == 2:
			web_status()

		elif ch == 3:
			web_stop()

		elif ch == 4:
			os.system("clear")
			break
		else:
			os.system("tput setaf 1")
			print("Invalid Input!") 