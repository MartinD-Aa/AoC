def day1_1(input):
    i=input[0] 
    antall=1
    for e in input:
        if i < e:
            antall+=1
            i = e
        else:
            i = e
            
    print(antall)
    
def day1_2(input):
    antall=1
    for i in range(1996):
        if i+4>2000:
            break
        else:
            A = int(input[i]) + int(input[i+1]) + int(input[i+2])
            B = int(input[i+1]) + int(input[i+2]) + int(input[i+3])
            if A < B:
                antall+=1
    print(antall)


if __name__ == '__main__':
    f = open('AoC2021/Input/day1.txt', 'r')
    fil = f.read()
    f.close()

    input = fil.split('\n')

    day1_1(input)
    day1_2(input)