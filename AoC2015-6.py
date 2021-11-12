from re import findall
def day6_1(fil, lights):
    instructions=fil.split('\n')
    on=0
    for line in instructions:
        words = line.split()
        if (len(words) == 5):
            if(words[1] == 'off'):
                coor = words[2].split(',')
                coord = words[4].split(',')
                start = coor[1]
                for row in range(int(coor[0]), int(coord[0])):
                    for irow in range(int(start), 1000):
                        if(row==int(coord[0])) and (irow==int(coord[1])):
                            lights[row][irow] = 0
                            break
                        else:
                            lights[row][irow] = 0
                    start=0
            else:
                coor = words[2].split(',')
                coord = words[4].split(',')
                start = coor[1]
                for row in range(int(coor[0]), int(coord[0])):
                    for irow in range(int(start), 1000):
                        if(row==int(coord[0])) and (irow==int(coord[1])):
                            lights[row][irow] = 1
                            break
                        else:
                            lights[row][irow] = 1
                    start=0

        elif(len(words) == 4):
            coor = words[1].split(',')
            coord = words[3].split(',')
            start = coor[1]
            for row in range(int(coor[0]), int(coord[0])):
                for irow in range(int(start), 1000):
                    if(row==int(coord[0])) and (irow==int(coord[1])):
                        if(lights[row][irow] == 1):
                            lights[row][irow] = 0
                        else:
                             lights[row][irow] = 1
                        break
                    else:
                        if(lights[row][irow] == 1):
                            lights[row][irow] = 0
                        else:
                             lights[row][irow] = 1
                    start=0
            
        else:
            print('Error')
            break
    for i in range(0,1000):
        for j in range(0,1000):
            if (lights[i][j]==1):
                on+=1
    print(on)

def day6_2(input):
    actions = {
        'toggle': lambda x: x + 2,
        'turn on': lambda x: x + 1,
        'turn off': lambda x: x - 1 if x > 0 else 0
    }
    lights = [[0 for i in range(1000)] for j in range(1000)]
    instructions = findall("(toggle|turn on|turn off)\s(\d*),(\d*)\sthrough\s(\d*),(\d*)", input)
    for action, x1, y1, x2, y2 in instructions:
        coords = [(x, y) for x in range(int(x1), int(x2) + 1) for y in range(int(y1), int(y2) + 1)]
        for x, y in coords:
            lights[x][y] = actions[action](lights[x][y])
    flattened = [val for sublist in lights for val in sublist]
    return sum(flattened)

if __name__ =='__main__':
    lights = []
    for i in range(0,1000):
        new=[]
        for j in range(0,1000):
            new.append(0)
        lights.append(new)
    f=open('Inputs/day6.txt')
    fil = f.read()
    f.close()

    day6_1(fil,lights)
    print(day6_2(fil))