####################################################
## --------------A Program for Counting Digits in------------##
##-------------------Decimal Expansion of pi------------------##
##-------------(showing pi can be normal number)-----------##
####################################################

from prettytable import PrettyTable

import time
start_time = time.time()

pi=[]
file = open("pi-10million.txt","r")
#file = open("pi-billion.txt","r")
text=file.read(10000000)
##text=file.read()
pi = tuple(text)

size=len(pi)


p1=0
for i in range(size):
    if pi [i] == '1':
            p1 =p1+1
            


p2=0
for i in range(size-1):
    if pi [i] == '1':
        if pi[i+1] == '4':
            p2 =p2+1
            
p3=0
for i in range(size-2):
    if pi[i] == '1':
        if pi [i+1] == '4':
            if pi[i+2] == '1':
                p3 =p3+1

p4=0
for i in range(size-3):
    if pi[i] == '1':
        if pi [i+1] == '4':
            if pi[i+2] == '1':
                if pi[i+3] == '5':
                    p4 =p4+1
            
p5=0
for i in range(size-4):
    if pi[i] == '1':
        if pi [i+1] == '4':
            if pi[i+2] == '1':
                if pi[i+3] == '5':
                    if  pi[i+4] == '9':
                        p5 =p5+1

p6=0
for i in range(size-5):
    if pi[i] == '1':
        if pi [i+1] == '4':
            if pi[i+2] == '1':
                if pi[i+3] == '5':
                    if  pi[i+4] == '9':
                        if pi[i+5] == '2':
                            p6 =p6+1



p7=0
for i in range(size-6):
    if pi[i] == '1':
        if pi [i+1] == '4':
            if pi[i+2] == '1':
                if pi[i+3] == '5':
                    if  pi[i+4] == '9':
                        if pi[i+5] == '2':
                            if pi[i+6] == '6':
                                p7 =p7+1
                                temp=i

p8=0
for i in range(size-7):
    if pi[i] == '1':
        if pi [i+1] == '4':
            if pi[i+2] == '1':
                if pi[i+3] == '5':
                    if  pi[i+4] == '9':
                        if pi[i+5] == '2':
                            if pi[i+6] == '6':
                            	if pi[i+7]=='5':
                            		p8 =p8+1
                            		temp1=i

x=PrettyTable()
x.field_names=["String ","No. of times it appears "]
x.add_row([1,p1])
x.add_row([14,p2])
x.add_row([141,p3])
x.add_row([1415,p4])
x.add_row([14159,p5])
x.add_row([141592,p6])
x.add_row([1415926,p7])
x.add_row([14159265,p8])
print("No. of Digits Considered: ",size)
print(x)
print('1415926 found at position :',temp)
print(temp1)
print("--- %s seconds ---" % (time.time() - start_time))
##print("no. of times 1 appears in expansion of pi(decimal values only)",p1," in ",size," Digits ")
##print("no. of times 14 appears consecutively in expansion of pi(decimal values only)",p2," in ",size," Digits ")
##print("no. of times 141 appears consecutively in expansion of pi(decimal values only)",p3," in ",size," Digits ")
