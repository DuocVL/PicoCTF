encode_flag = input("Nhập chuỗi mã hóa flag: ")
pass_str = input("Nhập pass dùng để mã hóa: ")

danh_sach = encode_flag.split(", ")
code = int(pass_str)
print(danh_sach)
print(code)

flag = ""
for i in danh_sach:
	flag += chr(int(int(i) / code))

print(f"Flag: {flag}")
