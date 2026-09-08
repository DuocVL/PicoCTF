from scapy.all import PcapReader, TCP

RAW_FILE = "stream.bin"
DECODED_FILE = "decrypt"
KEY = 42

raw = bytearray()
# Lấy dữ liệu thô từ các packet ghép nối và lưu tệp stream.bin
with PcapReader("packets.pcap") as pcap:
    for i, packet in enumerate(pcap):
        if TCP in packet:
            data = bytes(packet[TCP].payload)
            raw.extend(data)

with open(RAW_FILE, "wb") as f:
    f.write(raw)

print(f"Ghi {len(raw)} bytes dữ liệu thô vào {RAW_FILE} thành công !")


#Giải mã và ghi dữ liệu gốc
decoded = bytes((b - KEY) % 256 for b in raw)

with open(DECODED_FILE, "wb") as f:
    f.write(decoded)

print(f"Ghi dữ liệu giải mã vào {DECODED_FILE} thành công!")

