from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

key = DSA.generate(2048)
public_key = key.publickey()

with open("private_key.pem", "wb") as f:
    f.write(key.export_key())

with open("public_key.pem", "wb") as f:
    f.write(public_key.export_key())

consent_text = "I, the undersigned, agree to participate in this survey."
hash_obj = SHA256.new(consent_text.encode())
signer = DSS.new(key, 'fips-186-3')
signature = signer.sign(hash_obj)

print("Digital Signature:", signature.hex())

verifier = DSS.new(public_key, 'fips-186-3')

try:
    verifier.verify(hash_obj, signature)
    print("✅ Signature is valid!")
except ValueError:
    print("❌ Signature is invalid!")
