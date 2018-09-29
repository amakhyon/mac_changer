#!/usr/bin/env python
import subprocess #executes commands on system
import optparse #parse input from user

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



options= get_arguments()
change_mac(options.interface, options.new_mac)
