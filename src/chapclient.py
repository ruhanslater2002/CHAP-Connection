import socket
from chap_shared import SECRET, chap_hash

HOST = '127.0.0.1'
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Step 1: Receive challenge
challenge = client.recv(1024).decode()

# Step 2: Compute hash
response = chap_hash(challenge, SECRET)

# Step 3: Send response
client.send(response.encode())

# Step 4: Receive auth result
result = client.recv(1024).decode()
print(f"[Server Response] {result}")

client.close()
