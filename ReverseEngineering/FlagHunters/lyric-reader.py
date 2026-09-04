import re
import time


# Read in flag from file
flag = open('flag.txt', 'r').read()

secret_intro = \
'''Pico warriors rising, puzzles laid bare,
Solving each challenge with precision and flair.
With unity and skill, flags we deliver,
The ether’s ours to conquer, '''\
+ flag + '\n'


song_flag_hunters = secret_intro +\
'''

[REFRAIN]
We’re flag hunters in the ether, lighting up the grid,
No puzzle too dark, no challenge too hid.
With every exploit we trigger, every byte we decrypt,
We’re chasing that victory, and we’ll never quit.
CROWD (Singalong here!);
RETURN

[VERSE1]
Command line wizards, we’re starting it right,
Spawning shells in the terminal, hacking all night.
Scripts and searches, grep through the void,
Every keystroke, we're a cypher's envoy.
Brute force the lock or craft that regex,
Flag on the horizon, what challenge is next?

REFRAIN;

Echoes in memory, packets in trace,
Digging through the remnants to uncover with haste.
Hex and headers, carving out clues,
Resurrect the hidden, it's forensics we choose.
Disk dumps and packet dumps, follow the trail,
Buried deep in the noise, but we will prevail.

REFRAIN;

Binary sorcerers, let’s tear it apart,
Disassemble the code to reveal the dark heart.
From opcode to logic, tracing each line,
Emulate and break it, this key will be mine.
Debugging the maze, and I see through the deceit,
Patch it up right, and watch the lock release.

REFRAIN;

Ciphertext tumbling, breaking the spin,
Feistel or AES, we’re destined to win.
Frequency, padding, primes on the run,
Vigenère, RSA, cracking them for fun.
Shift the letters, matrices fall,
Decrypt that flag and hear the ether call.

REFRAIN;

SQL injection, XSS flow,
Map the backend out, let the database show.
Inspecting each cookie, fiddler in the fight,
Capturing requests, push the payload just right.
HTML's secrets, backdoors unlocked,
In the world wide labyrinth, we’re never lost.

REFRAIN;

Stack's overflowing, breaking the chain,
ROP gadget wizardry, ride it to fame.
Heap spray in silence, memory's plight,
Race the condition, crash it just right.
Shellcode ready, smashing the frame,
Control the instruction, flags call my name.

REFRAIN;

END;
'''

MAX_LINES = 100

def reader(song, startLabel):
  lip = 0
  start = 0
  refrain = 0
  refrain_return = 0
  finished = False

  # Get list of lyric lines - tách chuỗi nhiều dòng thành mảng chuỗi 1 dòng 
  song_lines = song.splitlines()
  
  # Find startLabel, refrain and refrain return
  #xác định dòng bắt đầu , dòng bắt đầu điệp khúc , dòng kết thúc điệp khúc
  for i in range(0, len(song_lines)):
    if song_lines[i] == startLabel:#kiểm tra có phải startlabel không nếu có tăng start lên 1
      start = i + 1
    elif song_lines[i] == '[REFRAIN]':#kiểm tra có phải [REFRAIN] nếu có tăng refr
      refrain = i + 1
    elif song_lines[i] == 'RETURN':
      refrain_return = i

  # Print lyrics
  line_count = 0#tổng số dòng
  lip = start# index dòng sẽ in
  while not finished and line_count < MAX_LINES:#lặp đến khi hoàn thành(line 'END') và tổng số dòng chưa quá giới hạn 100
    line_count += 1 #tăng tổng dòng in
    for line in song_lines[lip].split(';'):#lặp qua các dòng được phân tách bằng ';' trong song_lines[lip]
      if line == '' and song_lines[lip] != '':#nếu line rỗng và song_lines[lip] tại đó không rỗng bỏ qua
        continue
      if line == 'REFRAIN':#nếu là line REFRAIN cập nhật dòng song_lines[refrain_return] thêm số dòng lip
        song_lines[refrain_return] = 'RETURN ' + str(lip + 1)
        lip = refrain# cập nhật lip thành refrain
      elif re.match(r"CROWD.*", line):#Khớp xem line có bắt đầu bằng CROWD không và cập nhật dòng hiện tại và tăng lip
        crowd = input('Crowd: ')
        song_lines[lip] = 'Crowd: ' + crowd
        lip += 1
      elif re.match(r"RETURN [0-9]+", line): #nếu là dòng RETURN và số (câpj nhật khi gặp REFRAIN) cập nhật lip 
        lip = int(line.split()[1])
      elif line == 'END':# Nếu là end thì đặt finished là true
        finished = True
      else:#nếu không phải in line , cập nhật lip và sleep(0.5)
        print(line, flush=True)
        time.sleep(0.5)
        lip += 1



reader(song_flag_hunters, '[VERSE1]')
