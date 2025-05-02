from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
import base64

def generate_keys():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )
    
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    
    return private_key, public_key, private_pem, public_pem

def sign_document(private_key, document):

    document_hash = hashes.Hash(hashes.SHA256())
    document_hash.update(document.encode())
    hashed_document = document_hash.finalize()

    signature = private_key.sign(
        hashed_document,
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    
    return signature, hashed_document

def verify_document(public_key, document, signature):

    document_hash = hashes.Hash(hashes.SHA256())
    document_hash.update(document.encode())
    hashed_document = document_hash.finalize()
    
    try:

        public_key.verify(
            signature,
            hashed_document,
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        return True
    except:
        return False

candidate_resume = "Resume: John Doe - Experienced Software Developer"

private_key, public_key, private_pem, public_pem = generate_keys()

signature, hashed_document = sign_document(private_key, candidate_resume)

is_verified = verify_document(public_key, candidate_resume, signature)

print("Signature valid:", is_verified)
