import sys

def solution(phone_book):
    answer = True
    dic={}

    for phone_number in phone_book:
        dic[phone_number]=1
    
    for phone_number in phone_book:# 번호책에서 번호를 가져온다--1
        temp=""
        for number in phone_number:#번호 하나 하나를 이어 붙인다.--2
            temp+=number
            if temp in dic and temp != phone_number:#아직 현재 전화번호를 다 완성하지 못했는데 앞에 접두사 부분과 동일한 번호가 있을때--3
                return False
    return True

# def solution(phone_book):
#     answer = True
#     phone_book.sort()
    
#     for i in range(len(phone_book)-1):
#         if phone_book[i+1].startswith(phone_book[i]):
#             return False

#     return True


phone_book=["123","456","789"]
print(solution(phone_book))