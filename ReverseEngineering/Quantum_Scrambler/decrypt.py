import ast


def recover_flag(cipher):


    hex_chars = []

    for item in cipher:
        for value in item:
            if isinstance(value, str):
                hex_chars.append(value)

    flag = ''.join(chr(int(x, 16)) for x in hex_chars)

    return flag


# Nếu output được lưu dưới dạng text
with open("output.txt", "r") as f:
    data = f.read().strip()


cipher = ast.literal_eval(data)

flag = recover_flag(cipher)

print("FLAG:", flag)

