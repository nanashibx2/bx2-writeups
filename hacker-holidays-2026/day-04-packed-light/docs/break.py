import base64

key = b"H0t3lSt@ffOnlyK3epS3cr3t!"

flag = ""

with open("cookies.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        encrypted_byte = base64.b64decode(line)

        decrypted_byte = encrypted_byte[0] ^ key[0]
        flag += chr(decrypted_byte)

print("All Hail:", flag)
