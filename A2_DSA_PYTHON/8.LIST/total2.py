# print the total of the even numbers

# a=[78,65,44,-100,87,33,31]
# total=0
# for i in a:
#     if i%2==0:
#         total+=i
# print(total)

a=[78,65,44,-100,87,33,31]
total=0
for i in range(len(a)):
    if i%2==0:
        total+=a[i]
print(total)

