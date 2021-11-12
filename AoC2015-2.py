
def day2_1(x):
    areal = 0
    for e in x:
        l, w, h = e.split('x')
        l, w, h = int(l), int(w), int(h)
        om = 2*l*w + 2*w*h + 2*h*l
        ekstra = min(l*w, w*h, l*h)
        areal += om + ekstra
    print(areal)

def day2_2(x):
    ribbon = 0
    for e in x:
        l, w, h = e.split('x')
        l, w, h = int(l), int(w), int(h)
        om = 2*l*w + 2*w*h + 2*h*l
        ekstra2 = min(l+w, w+h, l+h)
        bow = l*w*h
        ribbon += ekstra2*2 + bow
    print(ribbon)

if __name__ == '__main__':
    f = open('Inputs/day2.txt', 'r')
    fil = f.read()
    f.close()

    x = fil.split('\n')

    day2_1(x)
    day2_2(x)