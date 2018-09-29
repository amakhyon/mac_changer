#!/usr/bin/env python
import subprocess #executes commands on system
import optparse #parse input from user
import re

def get_arguments():
	parser = optparse.OptionParser() #creates a parser
	parser.add_option("-i", "--interface", dest="interface", help="Interface to change it's mac address") #store value  after -i or --interface  into the  options in interface variable
	parser.add_option("-m", "--mac", dest= "new_mac", help = "new mac address")

	(options, arguments) = parser.parse_args()
	
	if not options.interface:
		parser.error("[-] please specify an interface, use --help for more info")
	elif not options.new_mac:
		parser.error("[-]  please specify a mac, use --help for more info")
	return options 

def change_mac(interface, new_mac):
	
	print("[+] changing mac address for " + interface + " to " + new_mac )
	subprocess.call(["ifconfig", interface, "down" ])
	subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
	subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
	
	#store results of $ifconfig into a variable
	ifconfig_result = subprocess.check_output(["ifconfig",interface])
	mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result) #filters out the mac 
	if mac_address_search_result: 
		return mac_address_search_result.group(0)
	else:
		print("[-] couldn't read mac address")



def main():
	options= get_arguments()
	current_mac = get_current_mac(options.interface)
	original_mac = current_mac
	change_mac(options.interface, options.new_mac)
	current_mac = get_current_mac(options.interface)
	if current_mac == options.new_mac:
		print("[+] mac address was successfully changed to " + str(current_mac))
	else:
		print("[-] mac address didn't changed")
	

main()
