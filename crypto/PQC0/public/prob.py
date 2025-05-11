# REQUIRED: OpenSSL 3.5.0

import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from flag import flag

# generate private key
os.system("openssl genpkey -algorithm ML-KEM-768 -out priv-ml-kem-768.pem")
# generate public key
os.system("openssl pkey -in priv-ml-kem-768.pem -pubout -out pub-ml-kem-768.pem")
# generate shared secret
os.system("openssl pkeyutl -encap -inkey pub-ml-kem-768.pem -secret shared.dat -out ciphertext.dat")

with open("priv-ml-kem-768.pem", "rb") as f:
    private_key = f.read()

print("==== private_key ====")
print(private_key.decode())

with open("ciphertext.dat", "rb") as f:
    ciphertext = f.read()

print("==== ciphertext(hex) ====")
print(ciphertext.hex())

with open("shared.dat", "rb") as f:
    shared_secret = f.read()

encrypted_flag = AES.new(shared_secret, AES.MODE_ECB).encrypt(pad(flag, 16))

print("==== encrypted_flag(hex) ====")
print(encrypted_flag.hex())

