# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)
# print(7)
# print(8)
# print(9)
# print(10)

# # 반복문을 사용해 1부터 10까지 출력
# # i가 1부터 10까지 1씩 증가하면서
# # 총 10번 반복 수행
# i=0
# while i<11:
#     # 출력할 수는 1부터 10까지 변화하는 수
#     print(i)
#     i+=1

# print('안녕하세요')
# print('안녕하세요')
# print('안녕하세요')
# print('안녕하세요')
# print('안녕하세요')
# 반복문으로 '안녕하세요'를 5번 출력
# i=0
# while i<5:
#     print('안녕하세요')
#     i+=1

# print('반가워요')
# print('반가워요')
# print('반가워요')

# 반복문으로 '반가워요'를 3번 출력
# i=0
# while i<3:
#     print('반가워요')
#     i+=1

# print(2)
# print(4)
# print(6)
# print(8)
# print(10)
# 반복문으로 2 4 6 8 10 짝수 5개를 출력
# i가 0부터 4가 될 때까지 1씩 증가하면서
# # 총 5번 반복 실행
# i=0
# while i<5:
#     print((i+1)*2)
#     i+=1

# 반복문 없이 숫자 3부터 6까지 출력
# print(3)
# print(4)
# print(5)
# print(6)
# # 반복문으로 숫자 3부터 6까지 출력
# i=3
# while i<7:
#     pass
#     i+=1
# i=0
# while i<5:
#     print('hello')
#     i+=1

# i=0
# while i<7:
#     print(i+1)
#     i+=1

# i=0
# while i<5:
#     print(i*2+1)
#     i+=1

# i=10
# while i<20:
#     print(i+1)
#     i+=1

# sum = 0
# sum = sum + 1
# sum = sum + 2
# sum = sum + 3
# sum = sum + 4
# sum = sum + 5

# i=1
# sum=0
# while i<6:
#     sum = sum + i
#     i+=1
#     print('합:', sum)

# nums = [10, 20, 30]

# print(nums[0])
# print(nums[1])
# print(nums[2])

# i=0
# while i<3:
#     print(nums[i])    
#     i+=1

# # 1부터 20까지 더한 합 구하기
# i=1
# sum=0
# while i<=20:
#     if sum>100:
#         break
#     sum=sum+i
#     i+=1
# print('합:', sum)

# lis = [100,77,-5,10]

# i=0
# while i<4:
#     if lis[i] == 77:
#         break
#     print(lis[i])
#     i+=1

# i=1
# while i<11:
#     if i%3 == 0:
#         break
#     print(i)
#     i+=1

# i=1
# while i<10:
#     if i%2 == 0:
#        i+=1
#        continue
#     print(i)
#     i+=1

# 리스트 생성
lis = [10, 'a', True, 20, 'b']

i=0
while i<5:
    if type(lis[i]) == int:
        i+=1
        continue
    print(lis[i])
    i+=1