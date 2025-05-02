import hashlib


document_content = "Confidential report: The project status is on track for the deadline."


sha1_hash = hashlib.sha1(document_content.encode()).hexdigest()
print(sha1_hash)
