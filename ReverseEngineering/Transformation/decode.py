enc = open("enc", "r", encoding="utf-8").read()
flag = ""
for c in enc:
	flag += chr(ord(c)>>8)
	flag += chr(ord(c) & 0xff)
	
print(flag)
