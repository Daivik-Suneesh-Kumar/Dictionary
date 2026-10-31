test_dict = {"Codingal" : 2, "is" : 2, "the" : 2, "best" : 2, "for" : 2, "Coding" : 1}
print("The original dictionary:",test_dict)

V = 2
res = 0
for k in test_dict:
    if test_dict[k] == V:
       res = res + 1 
print("The frequency of 2:",res)