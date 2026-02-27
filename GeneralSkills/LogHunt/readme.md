https://play.picoctf.org/practice/challenge/527?category=5&page=1

lenh
$ cat server.log | grep -i "FLAG" | awk '{print $5}' | sort | uniq

Flag:
picoCTF{us3_y0urlinux_sk1lls_cedfa5fb}


