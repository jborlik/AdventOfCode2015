# -*- coding: utf-8 -*-

# find the lowest number such that the MD5 hash of the
#  secret_key and the number results in a hash with five leading zeros

import hashlib


secret_key = b"bgvyzdsv"


m = hashlib.md5()
m.update(secret_key)


for ival in range(10000000):
    print(str(ival))
    m2 = m.copy()
    m2.update(str(ival).encode())
    thishex = m2.hexdigest()
    if (thishex.startswith("000000")):
        break
    
print("{0} with hex {1}".format(ival,thishex))



