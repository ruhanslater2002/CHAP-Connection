import socket
import os
from chap_shared import SECRET, chap_hash

HOST = '127.0.0.1'
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
print(f"[+] Server listening on {HOST}:{PORT}")

conn, addr = server.accept()
print(f"[+] Connected by {addr}")

# Step 1: Send challenge
challenge = os.urandom(16).hex()
conn.send(challenge.encode())

# Step 2: Receive client's hash
client_response = conn.recv(1024).decode()

# Step 3: Server computes expected hash
expected_hash = chap_hash(challenge, SECRET)

# Step 4: Compare
if client_response == expected_hash:
    conn.send(b"AUTH_SUCCESS")
    print("[+] Client authenticated.")
else:
    conn.send(b"AUTH_FAIL")
    print("[-] Authentication failed.")

conn.close()
