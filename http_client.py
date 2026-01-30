# Name: Trish Figueroa
# Student ID: N01724664
# Course: CPAN-226
# Lab 1 - HTTP with Ncat and Python
# Date: 2026-01-29
#
# Notes:
# - This script opens a TCP connection to gaia.cs.umass.edu on port 80
# - It sends an HTTP GET request with proper CRLF (\r\n) line endings
# - It prints the HTTP response returned by the server (301 redirect to HTTPS)


from socket import *

server_name = 'gaia.cs.umass.edu'
server_port = 80

# 1. Create a TCP socket (IPv4) ; client side
client_socket = socket(AF_INET, SOCK_STREAM)

# 2. Connect to the web server (host, port)
client_socket.connect((server_name, server_port))

# 3. HTTP request uses CRLF and ends header with \r\n\r\n
request = (
    "GET /kurose_ross/interactive/index.php HTTP/1.1\r\n"
    "Host: gaia.cs.umass.edu\r\n"
    "Connection: close\r\n"
    "\r\n"
)

# 4. Send request bytes to server
client_socket.sendall(request.encode())

# 5. Receive (bytes) response from server, read until server closes
response = b""
while True:
    chunk = client_socket.recv(4096)
    if not chunk:
        break
    response += chunk

# 6. Decodes and print the result
print(response.decode(errors="replace"))

# 7. Closes the connection
client_socket.close()
