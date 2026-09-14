# PicoCTF

Repository lưu trữ quá trình **giải PicoCTF Challenges**, bao gồm source code, script hỗ trợ và writeup cho từng challenge.

Mục tiêu của repository là ghi lại quá trình phân tích và giải quyết các bài toán Cybersecurity, đồng thời xây dựng tài liệu tham khảo cho việc học **CTF, Pentesting và Reverse Engineering**.

## Cấu trúc Repository

Mỗi thư mục tương ứng với một challenge:

```text
.
├── 13/
├── Enhance/
├── Even_RSA_Can_Be_Broken/
├── GeneralSkills/
├── HashingJobApp/
├── Mod26/
├── NewCaesar/
├── PWCrack1/
├── PWCrack2/
├── PWCrack3/
├── PWCrack4/
├── PWCrack5/
├── ReverseEngineering/
├── TheNumbers/
├── caesar/
├── fixmePy/
├── hashCrack/
├── interwncdec/
├── keygenme-py/
├── runmePy/
├── vault-door-training/
└── README.md
```

Mỗi challenge có thể chứa:

```text
Challenge/
├── source / binary / input files
├── solve script
├── output
└── writeup.md
```

## Các Category

Repository tập trung vào nhiều category của PicoCTF:

### General Skills

Các challenge rèn luyện những kỹ năng nền tảng:

* Linux command line
* File manipulation
* Encoding / decoding
* Python scripting
* Basic networking
* Hexadecimal / ASCII
* Bash

### Cryptography

Các bài tập liên quan đến mật mã:

* Caesar Cipher
* Substitution Cipher
* RSA
* Modular Arithmetic
* Hashing
* Encoding
* Cryptographic implementation

Một số challenge tiêu biểu:

* `13`
* `Even_RSA_Can_Be_Broken`
* `Mod26`
* `NewCaesar`
* `TheNumbers`
* `caesar`
* `interwncdec`

### Password Cracking

Các challenge liên quan đến password và hash:

* Password analysis
* Hash identification
* Dictionary attack
* Brute force
* Hash cracking

Các challenge hiện có:

```text
PWCrack1
PWCrack2
PWCrack3
PWCrack4
PWCrack5
hashCrack
```

### Reverse Engineering

Tập trung vào việc phân tích chương trình để tìm hiểu logic và cơ chế kiểm tra:

* Static analysis
* Decompilation
* Control flow analysis
* String analysis
* Program logic
* Key / password validation
* Java bytecode
* Python bytecode
* Executable analysis

Thư mục:

```text
ReverseEngineering/
```

và các challenge như:

```text
keygenme-py/
vault-door-training/
```

## Writeup

Các writeup tập trung vào **quá trình giải challenge**, thay vì chỉ cung cấp flag.

Một writeup có thể bao gồm:

```text
1. Thông tin challenge
2. Phân tích ban đầu
3. Xác định hướng giải
4. Phân tích source / binary
5. Phân tích thuật toán
6. Viết script hỗ trợ
7. Thực hiện exploit / solve
8. Kết quả
9. Kiến thức rút ra
```

## Công cụ

Một số công cụ được sử dụng trong quá trình giải:

### Linux

* `file`
* `strings`
* `xxd`
* `hexdump`
* `grep`
* `sed`
* `awk`
* `find`

### Cryptography

* Python
* PyCryptodome
* SageMath
* OpenSSL

### Reverse Engineering

* Ghidra
* JADX
* `javap`
* JD-GUI
* CFR
* radare2
* Rizin
* x64dbg

### Password / Hash

* John the Ripper
* Hashcat
* Python
* `hashcat`
* `john`

## Mục tiêu học tập

Repository được sử dụng để phát triển các kỹ năng:

* CTF
* Cybersecurity
* Penetration Testing
* Cryptography
* Reverse Engineering
* Linux
* Python scripting
* Binary Analysis
* Problem Solving

Đặc biệt tập trung vào việc hiểu **tại sao một challenge có thể được giải**, thay vì chỉ tìm ra flag.



