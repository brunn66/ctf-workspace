from __future__ import print_function  # Only needed for Python 2
import linecache
import hashlib
import sys
import string
import md5


def xor(s1,s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

def repeat(s, l):
    return (s*(int(l/len(s))+1))[:l]
def is_hex(s):
     hex_digits = set(string.hexdigits)
     # if s is long, then it is faster to check against a set
     return all(c in hex_digits for c in s)

def is_hex(s):
    try:
        int(s, 16)
        return True
    except ValueError:
        return False

encryptedfile = open(sys.argv[1],"r")
dictfile = open(sys.argv[2],"r")
num_lines = sum(1 for line in dictfile)
log = open("encrypt.log","w")
guesskey = ""
encrypted = encryptedfile.read()
encryptedfile.close()
enc = encrypted.replace("\n", "")
encrypted_hex = enc.decode('hex')
done = 0
row = 0
while True:
	row += 1
	#print("=START=")
	#print(row)
	#print("of")
	#print(num_lines)
	#print("-END-")
	if row > num_lines * .25:
		if done < 25:
			done =+ 25
			print("=====> 25% done <=====")
	if row > num_lines * .5:
                if done < 50:
                        done =+ 50
                        print("=====> 50% done <=====")
	if row > num_lines * .75:
                if done < 75:
                        done =+ 75
                        print("=====> 75% done <=====")

	guesskey2 = linecache.getline(sys.argv[2], row)
	guesskey = guesskey2.replace("\n", "")
	guessstring = xor(encrypted_hex, repeat(guesskey, len(encrypted_hex)))	
	#print(guesskey + ": " + guessstring[:-32], file=log) 
	if guessstring.find(guesskey) != -1:
		print("MATCH: " + guesskey + " => :" + guessstring)
		print(guesskey + ": " + guessstring[:-32], file=log)
	if row == num_lines:
		break

dictfile.close()
