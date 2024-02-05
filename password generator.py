import secrets
import string
import random

letts = string.ascii_letters

digs = string.digits

spec_chars = string.punctuation

selection_list = letts + digs + spec_chars
pswd_len=int(input("Enter the length of the password\nLength must be above 8:\n"))
if (pswd_len<8):
  print("Password length must be greater than 8")
else:
  password = ''
  for i in range(pswd_len):
    password+= ''.join(secrets.choice(selection_list))

print(password)