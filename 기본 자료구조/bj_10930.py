# 문자열 S가 주어졌을 때, SHA-256 해시값을 구하는 프로그램을 작성하시오.
import hashlib

input_data = input()
encoded_data = input_data.encode()
result = hashlib.sha256(encoded_data) # 객체 생성
print(result.hexdigest())# 해쉬 결과 문자열
