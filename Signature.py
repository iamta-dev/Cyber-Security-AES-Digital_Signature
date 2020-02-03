from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
import hashlib
import base64
import os
import os.path
from os import listdir
from os.path import isfile, join
import time


class Signature:
   def SigningSignature(self,file_name,private_key):
      message = open(file_name,"rb").read()
      key = RSA.importKey(open(private_key).read())
      message_digest = SHA.new(message)
      signer = PKCS1_v1_5.new(key)
      digital_signature = base64.b64encode(signer.sign(message_digest))
      # digital_signature = signer.sign(message_digest)
      open(file_name.split('.')[0] + "_Digital_Signature.txt","wb").write(digital_signature)

   def VerifySignature(self,file_name,file_signature,public_key):
      massage = open(file_name,"rb").read()
      massage_digest = SHA.new(massage)
      signature = base64.b64decode(open(file_signature,"rb").read())
      key = RSA.importKey(open(public_key).read())
      verifier = PKCS1_v1_5.new(key)
      if verifier.verify(massage_digest, signature):
         print ("The signature is authentic.")
         exit()
      else:
         print ("The signature is not authentic.")
         exit()

sg = Signature()
clear = lambda: os.system('cls')

while True:
   clear()
   choice = int(input("1. Press '1' to Signing Signature file.\n2. Press '2' to Verify Signature file.\n3. Press '3' to exit.\nEnter Option:"))
   if choice == 1:
      file_name = str(input("Enter name of file message: "))
      private_key = str(input("Enter name of file private_key: "))
      sg.SigningSignature(file_name,private_key)
   elif choice == 2:
      file_name = str(input("Enter name of file message: "))
      file_signature = str(input("Enter name of file Signature: "))
      public_key = str(input("Enter name of file public_key: "))
      sg.VerifySignature(file_name,file_signature,public_key)
   elif choice == 3:
        exit()
   else:
        print("Please select a valid option!")