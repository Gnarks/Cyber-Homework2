from pwn import ELF, process

file = "./arthur-scherbius"
elf = ELF(file, checksec=False)

# Find cyphered inputs values
for sym in ["raphfre",  "rapcnff"]:
    if sym in elf.symbols:
        addr = elf.symbols[sym]
        data = elf.read(addr,46)
        print(f"- {sym}")
        print(f"hex: {data.hex()}")


# Find known "Welcome" cypher value
rapterrg_plain = b"Welcome to Enigma v20.2.6 SuperDoudou Edition!"
rapterrg_cyphered = elf.read(elf.symbols["rapterrg"],47)

print(f"- rappterrg ")
print(f"hex: {rapterrg_cyphered.hex()}")

raphfre_ct = elf.read(0x2130, 21)  
rapcnff_ct = elf.read(0x2160, 33)


key = bytes(c ^ p for c, p in zip(rapterrg_cyphered, rapterrg_plain))
print(f"key: {key.hex()}")


def decrypt(ct, key, label):
    pt = bytes(c ^ k for c, k in zip(ct, key))
    print(f"\n[+] {label}")
    print(f"    hex : {pt.hex()}")
    print(f"    str : {pt}")
    return pt

user = decrypt(raphfre_ct, key, "User")
pwd = decrypt(rapcnff_ct, key, "Password")

p = process(file)
p.sendline(user)
p.sendline(pwd)
p.interactive()
