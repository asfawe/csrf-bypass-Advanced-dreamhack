from hashlib import md5


a = md5(('admin' + '127.0.0.1').encode()).hexdigest()

print(a)