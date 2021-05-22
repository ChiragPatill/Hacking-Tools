#!usr/bin/env python3
import subprocess
from colorama import Fore,Back,Style
import optparse
import re

def Created_by():
	print(Fore.GREEN+"Created by: >"+Fore.BLUE+"H@cky_Meet"+Style.RESET_ALL)

def get_arguments():
	parse=optparse.OptionParser()
	parse.add_option("-i", "--interface", dest="interface", help="interface to change the macaddress")
	parse.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
	(options, arguments)=parse.parse_args()
	if not options.interface:
		parse.error("[-]"+Fore.GREEN+"Pleace specify an interface, use --help or more info.")
	elif not options.new_mac:
		parse.error("[-]"+Fore.GREEN+"please specify a new_mac, use --help or more info.")
	return options
	
	
def change_mac(old_mac,interface,new_mac):
	print("[+]" +Fore.RED+ ".......Changing Mac address for "+interface+" "+Fore.YELLOW+""+old_mac+""+Fore.RED+" to "+Fore.YELLOW+""+ new_mac)
	print(Fore.GREEN)
	subprocess.call(["ifconfig",interface,"down"])
	subprocess.call(["ifconfig",interface, "hw", "ether", new_mac])
	subprocess.call(["ifconfig",interface,"up"])
	print(Style.RESET_ALL)	
def get_current_mac(interface):
	res_interface=config_res=subprocess.check_output(["ifconfig",interface])

	search_mac_address=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",res_interface)	
	if search_mac_address.group(0):	
		return search_mac_address.group(0)		
	else:
		print("[-]"+Fore.GREEN+" Could not read the Mac address")
	
Created_by()
options=get_arguments()
Get_old_mac=get_current_mac(options.interface)
print("Current Mac="+str(Get_old_mac))
change_mac(Get_old_mac,options.interface,options.new_mac)
Get_current_mac=get_current_mac(options.interface)
if Get_current_mac==options.new_mac:
	print("[+]"+Fore.RED+".... MAC address has been sucessfully changed to "+Get_current_mac)
else:
	print("[-]"+Fore.RED+".... MAC address did not changed.")
