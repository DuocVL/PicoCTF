encode_flag = input("Nhập chuỗi flag đã mã hóa: ")
str = input("Chuỗi dùng để mã hóa: ")
reversed_s = encode_flag.replace(str,"")
flag = reversed_s[::-1]

print(f"Flag: {flag}")
