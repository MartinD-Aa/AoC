areal = 0
ribbon = 0

f = open('input_Day2.txt', 'r')
fil = f.read()
f.close()

x = fil.split('\n')

for e in x:
    l, w, h = e.split('x')
    l, w, h = int(l), int(w), int(h)
    om = 2*l*w + 2*w*h + 2*h*l
    ekstra = min(l*w, w*h, l*h)
    ekstra2 = min(l+w, w+h, l+h)
    areal += om + ekstra
    bow = l*w*h
    ribbon += ekstra2*2 + bow
print(areal)
print(ribbon)
