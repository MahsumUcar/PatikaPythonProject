def flatten(x):

    for i in x:
        if isinstance(i,list):
            flatten(i)
        else:
            l.append(i)
            

x =[[1,'a',['cat'],2],[[[3]],'dog'],4,5]

l=[]

flatten(x)



print(l)