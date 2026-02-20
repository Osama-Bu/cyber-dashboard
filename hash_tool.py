import hashlib

text = input("Enter text: ")

print("MD5:", hashlib.md5(text.encode()).hexdigest())
print("SHA1:", hashlib.sha1(text.encode()).hexdigest())
print("SHA256:", hashlib.sha256(text.encode()).hexdigest())

print("\n--- Hash Identifier ---")
hash_input = input("Enter hash to identify: ")

if len(hash_input) == 32:
    print("Possible hash type: MD5")
elif len(hash_input) == 40:
    print("Possible hash type: SHA1")
elif len(hash_input) == 64:
    print("Possible hash type: SHA256")
else:
    print("Unknown hash type")

