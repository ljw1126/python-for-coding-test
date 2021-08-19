"""
1152번 단어의 개수 -- easy 그냥 list에 공백 단위로 잘라 넣어서 , len() 구하면됨
문제
영어 대소문자와 띄어쓰기만으로 이루어진 문자열이 주어진다. 이 문자열에는 몇 개의 단어가 있을까? 이를 구하는 프로그램을 작성하시오. 단, 한 단어가 여러 번 등장하면 등장한 횟수만큼 모두 세어야 한다.

입력
첫 줄에 영어 대소문자와 띄어쓰기로 이루어진 문자열이 주어진다. 이 문자열의 길이는 1,000,000을 넘지 않는다. 단어는 띄어쓰기 한 개로 구분되며, 공백이 연속해서 나오는 경우는 없다. 또한 문자열의 앞과 뒤에는 공백이 있을 수도 있다.

출력
첫째 줄에 단어의 개수를 출력한다.
"""

# str_array = list(input().split())
# print(len(str_array))

"""
11720번 숫자의 합
문제
N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.

출력
입력으로 주어진 숫자 N개의 합을 출력한다.
"""

# n = int(input())

# array = list(map(int,input()))
# if len(array) <= n : 
#     print(sum(array))


"""
11654번 아스키 코드 

문제
알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때, 주어진 글자의 아스키 코드값을 출력하는 프로그램을 작성하시오.

입력
알파벳 소문자, 대문자, 숫자 0-9 중 하나가 첫째 줄에 주어진다.

출력
입력으로 주어진 글자의 아스키 코드 값을 출력한다.

※ 아스키 코드 
https://lsjsj92.tistory.com/201

숫자 0~9 > 049 ~ 057
알파벳 A~Z(대문자) > 065 ~ 090
알파벳 a~z(소문자) > 097 ~ 122
 

※ 여부 확인 메서드 
입력.isdigit  >> 정수 여부 확인
입력.isalpah >> 알파벳 여부 확인
입력.isalnum >> 알파벳 또는 숫자 포함인지 확인
"""

# txt = input()
# if txt.isalpha :
#     print(ord(txt))
# else : 
#     print(chr(txt))


"""
10809번 알파벳 찾기
문제
알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.

출력
각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치, ... z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.

만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다. 단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치이다.

※ 아스키 코드 역변환 관련 >> chr()
https://ooyoung.tistory.com/104
"""

# word = list(input())
# for i in range(97,123):
#     idx = -1
#     for j in range(len(word)):
#         if chr(i) == word[j] :     # chr(숫자) >> 아스키코드 값 변환 
#            idx = j
#            break
#     print(idx , end = " ")    

# 다른 사람 풀이 
# https://j-remind.tistory.com/62

# S = input()
# check = [-1]*26       ## check[-1]처럼 인덱스가 음수인 경우 -1 출력 , 양수인 경우 out of range 에러 뜸 
 
# for i in range(len(S)):
#     if check[ord(S[i])-97] != -1:
#         continue
#     else:
#         check[ord(S[i])-97] = i
        
# for i in range(26):
#     print(check[i], end=' ')


"""
2675번 
문제
문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.

QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

입력
첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다. S의 길이는 적어도 1이며, 20글자를 넘지 않는다. 

출력
각 테스트 케이스에 대해 P를 출력한다.
"""
# 내가 한거 -- 쓸데없는 map() 변환 빼고 , print() 줄바꿈 넣음 
# n = int(input())

# for _ in range(n):
#     num,word = input().split()
#     for i in word : 
#         print(i*int(num), end="")
#     print() # 줄넘김

# 다른사람 
# n = int(input())

# for _ in range(n):
#     num,b = input().split()
#     txt = ''
#     for i in b : 
#         txt += i*int(num)
#     print(txt)

"""
2908번 상수  ----------- reverse라는건 없고 [::-1]으로 출력해서 하는 방법이 있었음
문제
상근이의 동생 상수는 수학을 정말 못한다. 상수는 숫자를 읽는데 문제가 있다. 이렇게 수학을 못하는 상수를 위해서 상근이는 수의 크기를 비교하는 문제를 내주었다. 상근이는 세 자리 수 두 개를 칠판에 써주었다. 그 다음에 크기가 큰 수를 말해보라고 했다.

상수는 수를 다른 사람과 다르게 거꾸로 읽는다. 예를 들어, 734와 893을 칠판에 적었다면, 상수는 이 수를 437과 398로 읽는다. 따라서, 상수는 두 수중 큰 수인 437을 큰 수라고 말할 것이다.

두 수가 주어졌을 때, 상수의 대답을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 상근이가 칠판에 적은 두 수 A와 B가 주어진다. 두 수는 같지 않은 세 자리 수이며, 0이 포함되어 있지 않다.

출력
첫째 줄에 상수의 대답을 출력한다.
"""

# a,b = input().split()

# if int(a[::-1]) > int(b[::-1]):
#     print(int(a[::-1]))
# else : 
#     print(int(b[::-1]))


"""
1316번 그룹 단어 체커 ------------- for문 pass의 존재와 , 문자열 slice를 활용 ***** (찾아봄)
문제
그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 
둘째 줄부터 N개의 줄에 단어가 들어온다. 
단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

출력
첫째 줄에 그룹 단어의 개수를 출력한다.
"""

## 내일 해보자 

# n = int(input())
# group_cnt = n

# for _ in range(n):
#     txt = input()
#     next_idx = 0
#     for i in txt : 
#         if txt.count(i) > 1:
#             for j in range(txt.count(i)):
#                 if txt[j] != txt[j+1] or txt[j-1] != txt[j] :
#                     group_cnt -= 1
#                     break 
#         else:
#             continue

## for문에 continue와 pass가 있는데 pass는 다음 문장 실행이고, continue는 다음 루프 실행해라는 뜻 // 
# n = int(input())
# group_cnt = n 
# for _ in range(n):
#     word = input()
#     for i in range(len(word)-1):
#         if word[i] == word[i+1]:
#             pass 
#         elif word[i] in word[i+1::]:
#             group_cnt -=1
#             break

# print(group_cnt)

"""
2941번 크로아티아 알파벳 --------------- in, replace활용( 몰라서 찾아봄 )
문제
예전에는 운영체제에서 크로아티아 알파벳을 입력할 수가 없었다. 따라서, 다음과 같이 크로아티아 알파벳을 변경해서 입력했다.

크로아티아 알파벳	변경
č	c=
ć	c-
dž	dz=
đ	d-
lj	lj
nj	nj
š	s=
ž	z=
예를 들어, ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다. 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.

dž는 무조건 하나의 알파벳으로 쓰이고, d와 ž가 분리된 것으로 보지 않는다. lj와 nj도 마찬가지이다. 위 목록에 없는 알파벳은 한 글자씩 센다.

입력
첫째 줄에 최대 100글자의 단어가 주어진다. 알파벳 소문자와 '-', '='로만 이루어져 있다.

단어는 크로아티아 알파벳으로 이루어져 있다. 문제 설명의 표에 나와있는 알파벳은 변경된 형태로 입력된다.

출력
입력으로 주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.

※ 참고 
https://hongku.tistory.com/255
"""

# croati_alpha = ['c=','c-','dz=','d-','lj','nj','s=','z=']
# alpha = input()

# for i in croati_alpha:
#     alpha = alpha.replace(i,"*")

# print(len(alpha))

"""
1157번 단어 공부 -------------- set()과 count() 활용 ( 찾아봄 )
문제
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 
무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

입력
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 
주어지는 단어의 길이는 1,000,000을 넘지 않는다.

출력
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 
단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

※ 참고 
https://wook-2124.tistory.com/257
"""

# 내 소스 - 시간초과 
# txt = input().upper()
# max_cnt = 0
# result = ''

# for i in txt : 
#     if i in txt and max_cnt < txt.count(i):
#         max_cnt = txt.count(i)
#         result = i  
#     elif max_cnt == txt.count(i) and result != i :
#         result ='?'
#         break

# print(result)

# lower()든 uppper()든 대소문자 통일하고 set() 으로 중복을 줄이는게 포인트.. 
# word = input().upper()
# word_list = list(set(word))
# word_cnt = []
# for i in word_list:
#     word_cnt.append(word.count(i))

# if word_cnt.count(max(word_cnt)) > 1 :
#     print("?")
# else:
#     print(word_list[word_cnt.index(max(word_cnt))])


"""
5622번
문제
상근이의 할머니는 아래 그림과 같이 오래된 다이얼 전화기를 사용한다.
전화를 걸고 싶은 번호가 있다면, 숫자를 하나를 누른 다음에 금속 핀이 있는 곳 까지 시계방향으로 돌려야 한다. 숫자를 하나 누르면 다이얼이 처음 위치로 돌아가고, 다음 숫자를 누르려면 다이얼을 처음 위치에서 다시 돌려야 한다.

숫자 1을 걸려면 총 2초가 필요하다. 1보다 큰 수를 거는데 걸리는 시간은 이보다 더 걸리며, 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.

상근이의 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다. 즉, 어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 걸면 된다. 예를 들어, UNUCIC는 868242와 같다.

할머니가 외운 단어가 주어졌을 때, 이 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 알파벳 대문자로 이루어진 단어가 주어진다. 단어의 길이는 2보다 크거나 같고, 15보다 작거나 같다.

출력
첫째 줄에 다이얼을 걸기 위해서 필요한 최소 시간을 출력한다.
"""
# 내가 푼게 맞음 , 번호면로 1초씩 더 걸려서 len() 만큼 먼저 더하고 반복문으로 값 더함 
dial_btn = ['','','ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

tel = input()
total_time = len(tel)
for i in tel : 
    for j in range(len(dial_btn)) : 
        if i in dial_btn[j] :
           total_time += j 

print(total_time) 


# 다른 사람 
import sys 
input = sys.stdin.readline 
# 다이얼 넘버
Dial_Number = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

tel = input()  # 알파벳 입력
result = 0  # 걸리는 시간

for i in tel:
    for j in Dial_Number:
        if i in j :
            result += Dial_Number.index(j) + 3

print(result)