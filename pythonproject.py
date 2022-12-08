
### FLATTEN

x =[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
l=[]

def flatten(x):

    for i in x:
        if isinstance(i,list):
            flatten(i)
        else:
            l.append(i)
        
flatten(x)
print(l)

list = ["a" , "b" , "c", ["d","e"], [1, 2], [3, 4], [5, 6, 7], [8,9]]
list.reverse()

for i in range(len(list)):
    (list[i])=(list[i])[::-1]

print(list)
