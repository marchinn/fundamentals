import hashlib

def becameHashSum(s):
    hash = hashlib.new('sha256')
    hash.update(s.encode())
    return  hash.hexdigest()

hash1 = becameHashSum('Lorem ipsum dolor sit amet, consectetur adipiscing elit')
hash2 = becameHashSum('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')

print(hash1)
print(hash2)