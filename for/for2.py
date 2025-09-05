# range : 연속된 숫자를 만들어주는 함수
# 반환값: 숫자를 담고 있는 range객체
# nums = range(1, 11)
# print(nums)
# # 사용방법
# for n in nums:
#     print(n)

# 0부터 9까지 연속된 숫자 10개를 반환
# nums = range(10)
# range객체를 사용해 '안녕하세요' 10번 출력
# # range의 값이 필요하지 않은 경우
# for n in nums:
#     print('안녕하세요')

# input : 키보드를 통해 값을 입력받는 함수
# 숫자를 3개 입력받고 합 구하기
# num1 = input() 
# sum = sum + int(num1)

# num2 = input() 
# sum = sum + int(num2)

# num3 = input() 
# sum = sum + int(num3)
sum = 0
for _ in range(3):
    num = input()
    sum = sum + int(num)

print('합계:', sum)



