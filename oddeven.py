# arr=[10,13,7,8,15,6]


# for x in arr:
#     if x%2==0:
#         arr.remove(x)
#         arr.append(x)
#     else:
#         arr.remove(x)
#         arr.insert(0,x)    
        

# print(arr)   


# given unsorted array to find 2nd largest element

a=[9,4,7,2,0,4,1,5,9]

first_max=min(a)
second_max=min(a)

for x in a:
    if x>first_max:
        first_max=x
    elif x>=second_max:
        second_max=x    

print(second_max)        