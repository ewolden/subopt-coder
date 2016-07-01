import sys
import binascii
import base64

def print_sub_options(suboption, length, value):
	print '\n-----'
	print 'ASCII:'
	print 'Sub-option: ', suboption[1]
	print 'Length: ', length[1]
	print 'Value: ', value[1], '\n'
	print 'HEX:'
	print 'Sub-option: ', suboption[0]
	print 'Length: ', length[0]
	print 'Value: ', value[0]
	


def TLVdecode(string, seeker=0):
	suboption = [string[seeker:seeker+2], int(string[seeker:seeker+2], 16)]
	length = [string[seeker+2:seeker+4], int(string[seeker+2:seeker+4], 16)]
	value = [string[seeker+4:seeker+4+length[1]*2], binascii.a2b_hex(string[seeker+4:seeker+4+length[1]*2])]

	print_sub_options(suboption, length, value)
	if len(string) > seeker+4+length[1]*2:
		nextstring = TLVdecode(string, seeker+4+length[1]*2)
		return str(suboption[1])+' '+str(length[1])+' '+value[1]+' '+nextstring
	else:
		print '\n\n---------------\nFull string:'
		return str(suboption[1])+' '+str(length[1])+' '+value[1]

def TLVencode(strings, stringnumber=1):
	suboption = [hex(int(strings[stringnumber]))[2:].zfill(2), strings[stringnumber]]
	length = [hex(len(strings[stringnumber+1]))[2:].zfill(2), len(strings[stringnumber+1])]
	value = [binascii.b2a_hex(strings[stringnumber+1]), strings[stringnumber+1]]
	
	print_sub_options(suboption, length, value)
	if len(strings[1:]) >= stringnumber+3:
		nextstring=TLVencode(strings, stringnumber+2)
		return suboption[0]+length[0]+value[0]+nextstring
	else:
		print '\n\n---------------\nFull string:'
		return suboption[0]+length[0]+value[0]


if len(sys.argv) == 2:
	print(TLVdecode(sys.argv[1]))

elif len(sys.argv) == 1:
	print 'Usage: \n'
	print 'Encoding:'
	print 'List of suboptions and value pairs, i.e:'
	print 'subopt-coder.py 01 http://some.url.com 02 some-more-information \n'
	print 'Decoding:'
	print 'A hex string with all info, i.e:'
	print 'subopt-coder.py 0113687474703a2f2f736f6d652e75726c2e636f6d0215736f6d652d6d6f72652d696e666f726d6174696f6e'


else:
	hexencoded = TLVencode(sys.argv)
	print 'HEX: '+hexencoded
	print 'BASE64: '+binascii.b2a_base64(hexencoded.decode("hex"))
