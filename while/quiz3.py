lis = [100,77,-5,10]

# print(lis[0])
# print(lis[1])
# print(lis[2])
# print(lis[3])

# # 반복코드: print(lis[?])
# # 반복횟수: 4
# i=0
# while i<4:
#     if lis[i] < 0:
#         i+=1
#         continue
#     print(lis[i])
#     i+=1

i=0
while i<4:
    if lis[i] == 77 :
        i+=1
        break
    print(lis[i])
    i+=1