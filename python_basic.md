# 파이썬 기초

## 자료형

### 숫자형
 - 숫자형이란 숫자 형태로 이루어진 자료형
 - 정수, 실수, 8진수, 16진수 등
 
| 항목 | 사용 예 |
| -- | -- |
| 정수 | 123, -345, 0 |
| 실수 | 123.45, -1234.5, 3.4e10 |
| 8진수 | 0o34, 0o25 |
| 16진수 | 0x2A, 0xFF |

#### 정수형(Integer)
 - 정수를 뜻하는 자료형
 
#### 실수형(Floating-point)
 - 소수점이 포함된 숫자
```
a = 1.2
b = 4.24e10 // 4.24*10^10 의미
```

#### 8진수와 16진수
 - 8진수(Octal)를 만들기 위해서는 숫자가 0o 또는 0O(숫자 0 ++ 알파벳 소문자 o 또는 대문자 O)로 시작
 - 16진수(Hexadeciaml)를 만들기 위해서는 0x로 시작
 
### 숫자형을 활용하기 위한 연산자

#### 사칙연산
 - 사칙연산( +, -, *, / ) 사용 가능

#### x의 y제곱을 나타내는 ** 연산자
```
a = 3
b = 4
a**b = 81
```

#### 나눗셈 후 나머지를 반환하는 % 연산자
```
a = 7
b = 3
a % b = 1
```

#### 나눗셈 후 몫을 반환하는 // 연산자
```
7 // 4 = 1
```

### 문자열 자료형
 - 문자열(String)이란 문자, 단어 등으로 구성된 문자들의 집합

#### 문자열 사용방법
1. 큰따옴표(")로 양쪽 둘러싸기
2. 작은따옴표(')로 양쪽 둘러싸기
3. 큰따옴표 3개를 연속(""")으로 써서 양쪽 둘러싸기
4. 작은따옴표 3개를 연속(''')으로 써서 양쪽 둘러싸기

#### 문자열 안에 작은따옴표나 큰따옴표를 포함시키고 싶을 때
```
food = "Python's favorite food is perl"

say = '"Python is very easy." he says.'

// 백슬래시(\)를 사용
'Python\'s favorite food is perl'

"\"Python is very easy.\" he says."
```

#### 여러 줄인 문자열을 변수에 대입하고 싶을 때
1. 줄을 바꾸기 위한 이스케이프 코드(\n) 삽입
2. 연속된 작은따옴표 3개(''') 또는 큰따옴표 3개(""") 사용

#### 문자열 더해서 연산하기
```
head = "Python"
tail = " is fun!"
head + tail
'Python is fun'
```

#### 문자열 곱하기
```
a = "python"
a * 2
'pythonpython'
```

#### 문자열 길이 구하기
```
a = "Life is too short."
len(a)
17
```

#### 문자열 인덱싱
 - 인덱싱(Indexing)이란 무언가를 "가리킨다"는 의미
 
```
a = "Life is too short, You need Python"
a[3]
'e'
```

 - a[-1]은 뒤에서부터 세어 첫 번째가 되는 문자를 의미
 
#### 문자열 슬라이싱
 - 슬라이싱(Slicing)은 무엇인가를 "잘라낸다"는 의미

```
a = "Life is short, You need Python"
a[0:4]
Life
```

#### 문자열 포매팅
 - 문자열 안에 어떤 값을 삽입하는 방법

```
//숫자 바로 대입
"I eat %d apples." % 3

//문자열 바로 대입
"I eat %s apples." % "five"

//숫자값 변수로 대입
number = 3
"I eat %d apples." % number

//2개 이상의 값 넣기
number = 10
day = "three"
"I ate %d apples. so I was sick for %s days." % (number, day)
```

#### 문자열 포맷 코드
| 코드 | 설명 |
| - | - |
| %s | 문자열(String) |
| %c | 문자 1개(character) |
| %d | 정수(integer) |
| %f | 부동소수(floating-point) |
| %o | 8진수 |
| %x | 16진수 |
| %% | Literal %(문자 % 자체) |

 - **%s 포맷 코드는 어떤 형태의 값이든 변환해 넣을 수 있음**
 
#### 포맷 코드와 숫자 함께 사용하기
```
//정렬과 공백
"%10s" % "hi"
결과 : '        hi'

"%-10sjane." % "hi"
결과 : 'hi        jane.'

//소수점 표현하기
"0.4f" % 3.42134234
결과 : 3.4213
```

#### format 함수를 사용한 포매팅
```
//숫자 바로 대입
I eat {0} apples.".format(3)
결과 : I eat 3 apples.

//문자열 바로 대입
I eat {0} apples.".format("five")
결과 : I eat five apples."

//숫자값 변수 대입
number = 3
"I eat {0} apples.".format(number)

//2개 이상의 값 넣기
number = 10
day ="three"
"I ate {0} apples. so I was sick for {1} days.".format(number, day)

//이름으로 넣기
"I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)

//왼쪽 정렬
"{0:<10}".format("hi")
결과 : 'hi        '

//오른쪽 정렬
"{0:>10}".format("hi")
결과 : '        hi'

//가운데 정렬
"{0:^10}".format("hi")
결과 : '    hi    '

//공백 채우기
"{0:=^10}".format("hi")
결과 : "====hi===="
```

#### f 문자열 포매팅
 - 파이썬 3.6 버전부터 f 문자열 포매팅 기능 사용 가능
 - 표현식(문자열 안에서 수식 사용 가능)을 지원
```
name = '홍길동'
age = 30
f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
결과 : '나의 이름은 홍길동입니다. 나이는 30입니다.'

age = 30
f'나는 내년이면 {age+1}살이 된다.'
결과 : '나는 내년이면 31살이 된다.'
```

#### 문자열 관련 함수들
```
//문자 개수 세기(count)
a = "hobby"
a.count('b')

//위치 알려주기1(find) -> 찾는 문자나 문자열이 존재하지 않는 경우 -1을 반환
a = "Python is the best choice"
a.find('b')

//위치 알려주기2(index)
a = "Life is too short"
a.index('t')

//문자열 삽입(join)
",".join('abcd')
결과 : a,b,c,d

//소문자를 대문자로 바꾸기
a = "hi"
a.upper()

//대문자를 소문자로 바꾸기
a = "HI"
a.lower()

//왼쪽 공백 지우기(lstrip), 오른쪽 공백 지우기(rstrip), 양쪽 공백 지우기(strip)
a = " hi "
a.lstrip()

//문자열 바꾸기(replace)
a = "Life is too short"
a.replace("Life", "Your leg")
결과 : 'Your leg is too short'

//문자열 나누기(split)
a = "Life is too short"
a.split()
결과 : ['Life', 'is', 'too', 'short']
```

### 리스트 자료형
 - 리스트를 만들 때는 대괄호([])로 감싸주고 각 요소값은 쉼표(,)로 구분
```
odd = [1, 3, 5, 7, 9]
```
 - 비어 있는 리스트는 a = list() 로도 생성 가능 ( a = [] )

#### 리스트 인덱싱
 - 리스트 역시 문자열처럼 인덱싱 적용 가능
```
a = [1, 2, 3]
a[0]
결과 : 1
```
 
 
 
 
 




 
 
