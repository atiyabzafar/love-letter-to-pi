####################################################
## --------------A Program for Counting Digits in------------##
##----------------Decimal Expansion of sqrt(2)----------------##
####################################################

from prettytable import PrettyTable
file = open("sqrt2_10million.txt","r")
text=file.read() 
exp = list(text)
array_size=[ 10 , 100 , 1000 , 10000, 100000, 1000000 , len(exp) ]
for num in range(0,7):
    ones = twos = threes = fours =  fives = sixes = 0
    sevens = eights = nines = zeroes = 0
    size=array_size[num]
    for i in range(size):
        temp=exp[i]
        if  temp == '0':
            zeroes = zeroes + 1
        elif temp == '1':
            ones = ones + 1
        elif temp == '2':
            twos = twos + 1
        elif temp == '3':
            threes = threes + 1
        elif temp == '4':
            fours = fours + 1
        elif temp == '5':
            fives = fives + 1
        elif temp == '6':
            sixes = sixes + 1
        elif temp == '7':
            sevens = sevens + 1
        elif temp == '8':
            eights = eights + 1
        else :
            nines = nines + 1    
    dist=[ ones , twos, threes, fours, fives, sixes, sevens,
              eights, nines, zeroes]
    dist_names=[ "ones" , "twos", "threes", "fours", "fives", "sixes", "sevens",
              "eights", "nines", "zeroes"]
    per=[x*100/sum(dist) for x in dist]
    x = PrettyTable()
    x.field_names = ["Number", "Number of times it appears", "Percentage"]
    for j in range(0,10):
        x.add_row([dist_names[j], dist[j],per[j]])
    print(x)
    print("Number of Decimal Places Considered:",size)
    print()
