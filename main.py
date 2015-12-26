#-*- coding: utf-8 -*-
import os
import time
from subprocess import call


def main_menu():
	print
	print
	print "######### Select an Option (1~3) #########"
	print
	print "##########################################"
	print "# 1. 			Scan Menu        #"
	print "# 2.			Advance Options  #"
	print "# 3.			Exit             #"
	return "##########################################"


def scan_menu():
	print
	print
	print "######### Select an Option (1~3) #########"
	print
	print "############## SCAN MENU #################"
	print "# 1.		Complete System Scan     #"
	print "# 2.		Scan Home User Directory #"
	print "# 3.		Custom Scan              #"
	print "# 4.		Back menu                #"
	return "##########################################"

def adv_options():
	print
	print
	print "######### Select an Option (1~3) ##################"
	print
	print "############## ADVANCE OPTIONS ####################"
	print "# 1.		Install ClamAV                    #"
	print "# 2.		Update ClamAV DataBase            #"
	print "# 3.		Back menu                         #"
	return "###################################################"

print "To use ClamAv Manager you need superuser privilege"
sudo_su = ["sudo", " su"]
pausa = ["sleep", "2"]
user = os.environ["USER"]
pwd = os.environ["PWD"]
call(sudo_su)
call('clear')
print "############## Welcome To ClamAV Manager ##############"
call(pausa)
while True:
	date_time = time.strftime('%d-%m-%y') + "_" + time.strftime('%H:%M:%S')
	log_file = str(date_time) + ".log"
	path_complete_log = str(pwd) + "/log/Complete/" + str(log_file)
	path_user_log = str(pwd) + "/log/User/" + str(log_file)
	path_custom_log = str(pwd) + "/log/Custom/" + str(log_file)
	full = ["clamscan", "--infected", "--remove", "-l", str(path_complete_log), "--recursive", "/"]
	home = ["clamscan", "--infected", "--remove", "-l", str(path_user_log), "--recursive", "/home/" + str(user)]
	print main_menu()
	main_option = raw_input(">")
	if main_option > "0" and main_option <= "3":
		if main_option == "1":
			while True:
				call('clear')
				print scan_menu()
				scan_option = raw_input(">")
				if scan_option > "0" and scan_option <= "4":
					if scan_option == "1":
						print "[*] **WARNING**"
			  			print "[i] This Scan  may contain errors because some parts"
			  			print "of the system are inaccessible"
			  			call(pausa)
			  			print "[*] Scanning... Please Wait"
			  			print "[i] Be patient"
						call(full)
						full_notify = ["notify-send", "ClamAV Manager", "Complete Scan Finished"]
						call(full_notify)
						break
					elif scan_option == "2":
						print "[*] Scanning... Please Wait"
			  			print "[i] Be patient"
			  			call(home)
			  			home_notify = ["notify-send", "ClamAV Manager", "Home Scan Finished"]
						call(home_notify)
			  			break
			  		elif scan_option == "3":
			  			path = raw_input("Enter the path to Scan""\n")
			  			if os.path.exists(path):
			  				print "[*] Starting... please wait"
			  				call(pausa)
			  				print "[*] Scan In Progress..."
							custom = ["clamscan", "--infected", "--remove", "-l", str(path_custom_log), "--recursive", str(path)]
		  					call(custom)
							#Write the scan path in log file
							scan_path = "Scan Path: " + str(path)
							f = open(path_custom_log, "a")
							f.write(scan_path)
							f.close()
		  					custom_notify = ["notify-send", "ClamAV Manager", "Custom Scan Finished"]
							call(custom_notify)
							break
			  			else:
			  				print "[X] Path not exist"
			  				call(pausa)
					else:
						call('clear')
						break
				else:
					print "[X] Invalid Option"
					call(pausa)
		elif main_option == "2":
			while True:
				call('clear')
				print adv_options()
				adv_option = raw_input(">")
				if adv_option > "0" and adv_option <= "3":
					if adv_option == "1":
						print "[*] Updating repositories"
						repo = ["sudo", "apt-get", "update", "-y"]
						call(repo)
						call('clear')
						print "[*] Updating Ok!"
						call(pausa)
						print "[*] Installing ClamAv"
						call(pausa)
						clamav = ["sudo", "apt-get", "install", "clamav",
						"clamav-daemon", "-y"]
						call(clamav)
						call('clear')
						print "[*] Installing Ok!"
						call(pausa)

					if adv_option == "2":
						print "[*] Updating ClamAV Viruses DataBase"
						call(pausa)
						bdvirus = ["sudo", "freshclam"]
						call(bdvirus)
						call(pausa)
					else:
					    call('clear')
					    break
				else:
					print "[X] Invalid Option"
					call(pausa)
		else:
			break
	else:
		print "[X] Invalid Option"
		call(pausa)
		call('clear')
