# setup for pyspy
import os.path
import errno
from os import path
import os
import yagmail

# check to see if format exists
if not path.exists('src/format.txt'):
    raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), 'format.txt')

# open from the format file
f = open("src/format.txt")
email_add = f.readline().rstrip('\n')
pwd = input('Email password: ')
f.close()

# valid the email and add to the keychain
yagmail.validate.validate_email_with_regex(email_add)
yagmail.register(email_add, pwd)