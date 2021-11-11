from hashlib import md5


key = "bgvyzdsv"    
for i in range(10000000):
    h = md5((key+str(i)).encode()).hexdigest()
    if h[:5] == '00000':
        print("1: "+ key +str(i))
        break


key = "bgvyzdsv"
for i in range(1000000000000):
    h = md5((key+str(i)).encode()).hexdigest()
    if h[:6] == '000000':
        print("2: "+ key +str(i))
        break

