encode_flag = input("Nhập chuỗi dữ liệu mã hóa của Flag: ")
code = "S3Cr3t"
print(f"Code dùng để mã hóa: {code}")

flag = ""
for i in range(0,len(encode_flag) // 2):
	str = encode_flag[i*2:(i+1)*2]
	so = int(str,16)
	flag += chr(so ^ ord(code[i % 6]))
	
print(f"Flag: {flag}")
	
