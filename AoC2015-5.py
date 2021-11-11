from re import search

f = open('Inputs/input_Day5.txt', 'r')
fil = f.read()
f.close

x = fil.split('\n')

def day5_1():
    toLike = False
    nice = 0
    antall= 0

    for e in x:
        antall+=1
        toLike = False
        if search("(ab)|(cd)|(pq)|(xy)", e):
            continue
        l = list(e)
        i=0
        tall=0
        for a in range(len(l)-1):
            if(l[a]==l[a+1]):
                toLike=True
        for a in l:
            if (a=='a') or (a=='e') or (a=='i') or (a=='o') or (a=='u'):
                tall+=1
        if (tall >2)and(toLike == True):
            nice+=1
                
    print(nice)
#Kunne blitt løst slik: print sum([1 for x in input if len(findall(r'[aeiou]', x)) >= 3 and findall(r'(.)\1', x) and not findall(r'(ab|cd|pq|xy)', x)])
def day5_2():
    #Fikk veldig mye hjelp med denne
    print(len([s for s in x if (search(r'(..).*\1', s) and
                                  search(r'(.).\1', s))]))
    
    
    
if __name__ == '__main__':
    day5_1()
    day5_2()