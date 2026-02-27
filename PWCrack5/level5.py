import hashlib

def str_xor(secret, key):
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key += key[i]
        i = (i + 1) % len(key)
    return "".join(chr(ord(a) ^ ord(b)) for a, b in zip(secret, new_key))


flag_enc = open('level5.flag.txt.enc', 'rb').read()
correct_pw_hash = open('level5.hash.bin', 'rb').read()


def hash_pw(pw_str):
    return hashlib.md5(pw_str.encode()).digest()


def level_5_pw_check():
    with open("dictionary.txt", "r", encoding="utf-8") as f:
        for line in f:
            user_pw = line.strip()        # ⭐ BẮT BUỘC
            if not user_pw:
                continue

            if hash_pw(user_pw) == correct_pw_hash:
                print("[+] Password found:", user_pw)
                print("Welcome back... your flag, user:")
                print(str_xor(flag_enc.decode(), user_pw))
                return

    print("[-] Password not found in dictionary")


level_5_pw_check()

