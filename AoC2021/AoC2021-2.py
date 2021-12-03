def day2(input):
    y=0
    x=0
    f=0
    for e in input:
        spl = e.split(' ')
        if (spl[0] == 'forward'):
            x+= int(spl[1])
            f+= int(spl[1])*y
        elif (spl[0] == 'up'):
            y -= int(spl[1])
        else:
            y += int(spl[1])
    print('x: '+str(x)+', y: '+str(y) + ', x*y: '+str(x*y) + ', x*y part 2: ' + str(f*x))




if __name__ == '__main__':
    f = open('AoC2021/Input/day2.txt', 'r')
    fil = f.read()
    f.close()

    input = fil.split('\n')

    day2(input)
    