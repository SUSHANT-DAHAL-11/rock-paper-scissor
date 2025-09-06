import random
import numpy as np
import re
from tempfile import TemporaryFile
import sys
bots_output = [1, 0, -1]
total_1 = 0
total_m1 = 0
total_0 = 0
total = 1
p_1 =0.0
p_0=0.0
p_m1=0.0
repeat=True
while(repeat==True):
    user_input=int(input("enter your choice\nrock=1\npaper=0\nscissors=-1\n"))
    with open('probability.txt') as f:
        num=re.findall('\d*?\.\d+', f.read())
        if num[0]==num[1] and num[0]==num[2]:
            bots_output=random.choice(bots_output)
        elif num[0]>num[1] and num[0]>num[2]:
            bots_output=1
        elif num[1]>num[0] and num[1]>num[2]:
            bots_output=0
        elif num[2]>num[0] and num[2]>num[1]:
            bots_output=-1
    with open('test.npy', 'wb') as f:
        np.save(f, np.array(bots_output))
        np.save(f, np.array(user_input)) 

    with open('test.npy', 'rb') as f:
        a = np.load(f)
        b = np.load(f)
    print("bot choice is", a)
    if(b-a==1 or b-a==-2):
        print("bot wins")
    elif(b-a==-1 or b-a==2):
        print("user wins")
    else:
        print("tie")
    fo=open('probability.txt', 'w')
    if user_input ==1:
        total_1 += 1
        total+=1
        p_1=(total_1)/total
        fo.writelines(f"Probability of rock:  {p_1} Probability of paper: {p_0} Probability of scissors: {p_m1} \n")
    elif user_input == 0:
        total_0 += 1
        total+=1
        p_0=(total_0)/total    
        fo.writelines(f"Probability of rock:  {p_1} Probability of paper: {p_0} Probability of scissors: {p_m1} \n")
    elif user_input == -1:
        total_m1 += 1
        total+=1
        p_m1=(total_m1)/total
        fo.writelines(f"Probability of rock:  {p_1} Probability of paper: {p_0} Probability of scissors: {p_m1} \n")
    fo.close()
if sys.stdin.isatty():
    repeat=False
else:
    repeat=True
if repeat==False:
    fo.writelines(f"Probability of rock:  0.0 Probability of paper: 0.0 Probability of scissors: 0.0 \n")
    fo.close()