#!/usr/bin/env python

print(''.join(chr(ord(a) ^ ord(b)) for a,b in zip("\x7B\x67\x05\x06\x18\x4D\x5A\x07\x46\x1E\x5F\x4D\x0C\x43\x14\x5F\x03\x58\x0B\x19\x5C\x07\x45\x52\x1E\x46\x5B\x58\x13", "31415926535897932384626433832")))
