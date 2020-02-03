from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA

# Verify
h = open("studentEncrypted.txt","rb").read()
h = SHA.new(h)

signature = open("digitalLicense.txt","rb").read()
key = RSA.importKey(open('public_key.pem').read())
verifier = PKCS1_v1_5.new(key)
if verifier.verify(h, signature):
   print ("The signature is authentic.")
else:
   print ("The signature is not authentic.")