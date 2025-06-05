#the while loop can execute a set of statement s lopng as a condition is true
i=1
while i < 6:
    print(i)
    i+=1 
    
#break statement - with the break statement we can stop the loop even if the while statement is true
print("using break")
j= 1
while j < 10:
    print(j)
    if j== 5:
        break
    j +=1


#continue statement- we can stop the current iteration and continue to the next
print("use of continue statement")
f= 0
while f < 8:
    f+=1
    if f==5:
        continue
    print(f)
    