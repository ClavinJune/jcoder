#Created by D4RK1TSUN3
#A E S T H E T I C
#A Simple coder that'll help you for encode and decode b64 and hex
import urllib
while(1):
	i=0
	while i<25:
		print
		i+=1
	print'\t\t     _            ____          _'
	print'\t\t    | |          / ___|___   __| | ___ _ __'
	print'\t\t _  | |  _____  | |   / _ \ / _` |/ _ \ ''__|'
	print'\t\t| |_| | |_____| | |__| (_) | (_| |  __/ |'
	print'\t\t \___/           \____\___/ \__,_|\___|_|'
	print"\t\t\t\tby Clavin June\n"
	print "\t1. Encode b64 \t\t\t\t\t2. Decode b64"
	print
	print "\t3. Encode Hex \t\t\t\t\t4. Decode Hex"
	print
	print "\t\t\t5. Encode Special Char URL \t\t\t\t\t"
	print
	main_menu = input('Choose >> ')
	text = raw_input('text  : ')
	if(main_menu == 1):
		print 'b64   :',text.encode("base64")
	elif(main_menu == 2):
		print 'plain :',text.decode("base64")
	elif(main_menu == 3):
		print 'hex   :',text.encode("hex")
	elif(main_menu == 4):
		print 'plain :',text.decode("hex")
	elif(main_menu == 5):
		print 'URL   :',urllib.quote(text, safe='')
	getchar=raw_input('')
