#!/usr/bin/env python

# autoserve - Double-click HTTP server for Windows
# Released as open source by NCC Group Plc - http://www.nccgroup.com/
# Developed by Aidan Marlin (aidan [dot] marlin [at] nccgroup [dot] trust)
# https://github.com/nccgroup/autoserve
# Released under AGPL. See LICENSE.md for more information

import sys
import os
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

HandlerClass = SimpleHTTPRequestHandler
ServerClass  = BaseHTTPServer.HTTPServer
Protocol     = "HTTP/1.0"

print "---"
print "autoserve v0.1 - autoserve.exe [<port> [directory]]"
print "By Aidan Marlin (aidan [dot] marlin [at] nccgroup [dot] trust)"
print

if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8000

if sys.argv[2:]:
	os.chdir(sys.argv[2])
else:
	os.chdir('..')

server_address = ('0.0.0.0', port)

HandlerClass.protocol_version = Protocol
httpd = ServerClass(server_address, HandlerClass)

sa = httpd.socket.getsockname()
print "Serving HTTP on", sa[0], "port", sa[1], "from " + os.getcwd()
httpd.serve_forever()
