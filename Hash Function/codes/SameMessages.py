import hashlib

def becameHashSum(s):
    hash = hashlib.new('sha256')
    hash.update(s.encode())
    return  hash.hexdigest()

hash1 = becameHashSum('Lorem ipsum dolor sit amet, consectetur adipiscing elit')
hash2 = becameHashSum('Lorem ipsum dolor sit amet, consectetur adipiscing elit')

print(hash1) # output is 07fe4d4a25718241af145a93f890eb5469052e251d199d173bd3bd50c3bb4da2
print(hash2) # output is also 07fe4d4a25718241af145a93f890eb5469052e251d199d173bd3bd50c3bb4da2