# nums = range(11, 21)
# for n in nums:
#     print(n)

# nums = range(5, 16)
# for n in nums:
#     print(n)

# nums = range(5)
# for n in nums:
#     print('hi')


# for 변수 in 자료구조(리스트)
# 변수에 저장되는 값: 인덱스x 값o

# nums = [10, 20, 30, 40, 50]
# sum = 0

# for n in nums:
#     sum = sum + n
# print('합계:', sum)

# for n in range(1, 101):
#     if n%3 == 0:
#        print(n)

# 변수 n을 선언하고 숫자를 대입
# # n의 크기만큼 *별을 출력
# num=10
# # 문자열 반복 연산 사용
# # print('*' * num)
# # for문 사용    
# str1 = ''
# for n in range(num):
#     str1 = str1 + '*'
# print(str1)

# n=5
# for i in range(1, n+1):
#     # 문자열 반복
#     print('*' * i)

# n=3
# for i in range(1, 10):
#     print(i * n)

# 리스트 생성
# 과정
# 5 9 비교 => 9 (max nums[1])
# 9 3 비교 => 9 (max nums[2])
# 9 8 비교 => 9 (max nums[3])
# 9 2 비교 => 9 (max nums[4])
# 리스트의 요소와 현재 가장 큰값을 비교
# 현재 max와 리스트의 요소를 비교하여
    # 리스트의 요소가 더 크면 max를 교체
# nums = [5, 9, 3, 8, 2]
# max = nums[0] # 가장 큰값을 저장할 변수
# for n in nums:
#     if max < n:
#         max = n
# print('최대값:', max)

# for문 안에서 break와 continue 쓰기

# for문으로 1부터 20까지 합 구하기
# 합이 100을 넘으면 반복문 중단
# sum = 0
# for i in range(1, 21):
#     if sum > 100:
#         break
#     sum = sum + i
# print(sum)

# for문에서 continue 사용하기
# contunue: 건너뛰기

# for문으로 1부터 10까지 출력
# 홀수는 건너뛰고 짝수만 출력
# for i in range(1,11):
#     if i%2 == 1:
#         continue
#     print(i)