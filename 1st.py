def count(n):
    cou = 0 

    for i in n:
        if i in "aeiAEIO":
            cou+=1 
    return cou 

print(count("Mousumi"))