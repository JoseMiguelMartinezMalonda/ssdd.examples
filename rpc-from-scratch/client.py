#!/usr/bin/python3
# -*- coding: utf-8; mode: python -*-

import sys
import socket
import struct


class ClientStub:
    FACTORIAL = 0
    POWER = 1

    def __init__(self, host, port):
        self.server_endpoint = host, port

    def factorial(self, n):
        sock = socket.socket()
        sock.connect(self.server_endpoint)

        request = struct.pack('BB', self.FACTORIAL, n)
        sock.sendall(request)

        reply = sock.recv(128)
        result = struct.unpack("Q", reply)[0]

        sock.close()
        return result

    def power(self, base, exp):
        sock = socket.socket()
        sock.connect(self.server_endpoint)

        request = struct.pack('BBB', self.POWER, base, exp)
        sock.sendall(request)

        reply = sock.recv(128)
        result = struct.unpack("Q", reply)[0]

        sock.close()
        return result


if len(sys.argv) != 3:
    print("usage: ./client <server> <arg>")
    sys.exit(1)


server = sys.argv[1]
arg = int(sys.argv[2])

stub = ClientStub(server, 2000)
print("factorial({}) = '{}'".format(arg, stub.factorial(arg)))
print("power({}, {}) = '{}'".format(arg, arg-1, stub.power(arg, arg-1)))
