#!/usr/bin/env python
#-*- coding: utf-8 -*-

import base64
import hmac
import time
import struct
from  hashlib import sha1


def OneTimePassword(secret, intervals_no):
    key  = base64.b32decode(secret, True)
    msg = struct.pack(">Q", intervals_no)
    h = hmac.new(key, msg, sha1).digest()
    o = ord(h[len(h) - 1]) & 0x0f
    h = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff ) % 1000000
    return h


test_key = 'GEZDGNBVGY3TQOJQ'
if __name__ == '__main__':
    epochSeconds = int(time.time())
    pwd = OneTimePassword(test_key, epochSeconds/60)
    secondRemaining = 60 - (epochSeconds % 60)
    print '%06d (%d second(s) remaining)' % (pwd, secondRemaining)