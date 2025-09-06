import random
import numpy as np
from tempfile import TemporaryFile
bots_output = [1, 0, -1]
total_1 = 0
total_m1 = 0
total_0 = 0
total = 1
user_input=int(input("enter your choice\nrock=1\npaper=0\nscissors=-1\n"))
bots_output=random.choice(bots_output)
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
    fo.write(f"Probability of rock:  {p_1} \n")
elif user_input == 0:
    total_0 += 1
    total+=1
    p_0=(total_0)/total    
    fo.write(f"Probability of paper: {p_0} \n")
elif user_input == -1:
    total_m1 += 1
    total+=1
    p_m1=(total_m1)/total
    fo.write(f"Probability of scissors: {p_m1} \n")