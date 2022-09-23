import struct
import socket
import sys

from pwn import *
from struct import pack


buf = b""
buf += b"STATS LMAOOO\n"


buf += b"EXIT\n\n"

def main():
  if len(sys.argv) != 2:
    print("Usage: %s <ip_address>\n" % (sys.argv[0]))
    sys.exit(1)

  server = sys.argv[1]
  port = 9999
  
  # Receive new line "Welcome to vulnerable server! ect."
  conn = remote("192.168.30.128", 9999)
  conn.recvline()
  
  conn.sendline(b'STATS LMAOOOO')
  
  conn.sendline(b'EXIT')

  conn.close()
  print("[+] Packet sent")


if __name__ == "__main__":
  main()
