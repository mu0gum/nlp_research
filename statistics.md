# 기초통계학 강의 정리
 - 숙명여대 여인권 교수님 OCW 기초통계학 강의 내용 정리 ( http://ocw.sookmyung.ac.kr/?course=2040 )

## 01. 통계학이란?

### 통계학(statistics)이란?
 - 관심 또는 연구의 대상이 되는 모집단의 특성을 파악하기 위해
 - 모집단으로부터 일부의 자료(표본)를 수집하고
 - 수집된 표본을 정리, 요약, 분석하여 표본의 특성을 파악한 후
 - 표본의 특성을 이용하여 모집단의 특성에 대해 추론하는 원리와 방법을 제공하는 학문
 
### 모집단(population) : 연구대상이 되는 모든 개체의 집합
 - 모집단의 크기에 따라 유한모집단(finite population)과 무한모집단(infinite population) 으로 구분하기도 함

### 전수조사(census) : 모집단의 자료를 얻기 위해 연구대상 전체를 조사하는 경우
 - 대부분의 모집단은 규모가 매우 커 전체를 조사하기 힘들다

### 표본(sample) : 모집단에서 선택된 일부의 자료
 - 표본을 뽑을 때 가장 중요한 것은 모집단 특성을 잘 반영하는 표본을 뽑는 것
 - 적절한 표본 선정의 중요성에 대한 대표적 사례 => 1936년 미국 대통령 선거 여론조사
 - 기본적으로 모집단을 대표할 수 있는 표본을 얻을 수 있는 유일한 방법 확률표본추출법(probability sampling)
 
### 기술통계(descriptive statistics)
 - 조사나 실험 등을 통해 얻은 표본을 표나 그래프와 같은 방법으로 요약정리하거나 평균과 분산과 같은 대푯값을 이용하여 표본의 특성을 파악
 - 이러한 일련의 방법이나 결과를 기술통계라고 함

### 표본의 한계
 - 표본으로 모집단의 특성을 완벽하게 파악하는 것은 불가능
 - 표본은 선택할 때마다 정보가 달라짐
 - 통계학에서는 변동성을 갖는 표본 정보에 **확률**을 적용하여 모집단의 특성을 추론하는데, 이것을 **통계적 추론(statistical inference)** 라고 함


## 02. 기술통계(01)

* 통계분석방법은 자료의 속성과 분석 목적에 따라 달라지며 분석방법을 적용하기 위한 조건들이 있음

### 변수(variable) 변량(variate)
 - A variable is any characteristics, number, or quantity that can be measured or counted.
 - 성별, 연령, 키, 몸무게 등 ..
 - TODO : 변수와 변량이 같은 의미인지 확인
 
### 다변량 자료(multivariate data)
 - 여러 개의 변수로 이루어진 자료
 
### 일변량 자료(univariate data)
 - 한 개의 변수로 이루어진 자료
 
### 관측개체(observation)
 - 선택된 각각의 대상

* 아래의 표는 7개의 변수로 이루어진 3개의 관측개체로 이루어진 다변량 자료

|번호|성별|연령|신장|체중|비만도|혈액형|멤버수|
|--|--|--|--|--|--|--|--|
|001|남|25|181|65|정상|B|5|
|002|남|23|175|55|저체중|A|4|
|003|여|19|161|44|저체중|A|4|

* 일반적으로 자료는 속성에 따라 크게 범주형 자료와 수치형 자료로 구분

### 1.범주형 자료(categorical data)
 - 위의 자료에서 성별, 혈액형 등과 같이 질적인 속성을 가짐

#### 1-1.명목 자료(nominal data)
 - 범주를 숫자로 표시했을 때 그 값이 크고 작음을 나타내는 것이 아닌 단순히 범주를 표시
 - ex) 성별, 혈액형

#### 1-2.순서 자료(ordinal data)
 - 범주를 숫자로 표시했을 때 범주의 순서가 상대적으로 비교 가능한 경우
 - ex) 비만도
 - 대부분의 순서 자료는 원래 수치 자료인데 이를 구간으로 그룹화하여 순서자료로 바꾸어 사용하는 경우가 많음 ex) 학점
 
### 2.수치형 자료(numerical data)
 - 연령, 신장, 체중 등과 같이 양적으로 표시되는 자료

#### 2-1.이산 자료(discrete data)
 - 멤버의 수와 같이 셀 수 있는 형태의 자료
 
#### 2-2.연속 자료(continous data)
 - 신장이나 체중과 같이 연속적인 형태의 자료
 
### 도수분포표(frequency table)
 - 일변량 범주형 자료를 정리하는 데 있어 기본이 되는 표
 - 도수(frequence)는 임의의 범주에 속해 있는 관측 계체의 수, 즉 빈도를 의미
 - 도수분포표는 각각의 범주에 몇 개의 관측개체가 있는지를 정리한 표
 
### 상대도수(relative frequency)
 - 각 범주에 속해있는 도수가 상대적으로 얼마나 많이 있는지 비교할 수 있도록 도움
 - 상대도수 = (해당 범주 관측개체의 수) / (전체 관측개체의 수)

|파이종류|판매량|판매비율(%)|
|--|--|--|
|애플|59|25.2|
|딸기|52|22.2|
|블루베리|47|20.1|
|초코|32|13.7|
|고구마|27|11.5|
|바나나|17|7.3|
|합계|234|100.0|

* 위 자료는 파이가게에서 지난 1주일 동안 판매된 파이를 종류별로 정리한 도수분포표
* 이 표에서는 판매량(판매비율)이 큰 순서로 정렬하여 표시, 때로는 범주를 가나다순으로 정렬하여 표시하기도 함
* **도수분포표는 수치자료를 정리할 때도 사용할 수 있음**
* 일반적으로 수치자료는 다양한 값으로 구성되어 있기 때문에 숫자와 일치하는 자료가 많지 않을 수 있으며 그 표가 아주 길어져 자료를 정리하고자 하는 목적에 맞지 않을 수 있음
 => 그래서 수치자료에 대한 도수분포표를 만들 때, **관측된 값들을 몇 개의 구간으로 범주화하여 해당 그룹에 속한 관측개체의 빈도**로 도수분포표를 만듬
* 수치자료를 범주화할 때는 몇 개의 범주로 나눌 것인지와 범주의 경계값을 얼마로 할 것인지 정해야 함
 => 이 때 각각의 범주를 **계급(class)** 이라고 함
* 계급의 수는 자료의 수에 비례하여 결정하는데 일반적으로 제곱근 방법, Sturges 공식, Rice 공식 등을 활용

### 분할표(contingency table), 교차표(cross table)
 - 2개 이상의 변수에 대해 교차시켜 빈도를 표시한 표
 - 행과 열에 범주수를 함께 포함


## 03. 기술통계(02)
* 어떤 현상을 숫자나 수식으로 설명하는 것보다 그림과 같은 시각적인 방법을 이용하여 설명하면 이해를 잘 하는 경향이 있음

### 파이차트(pie chart)
 - 원을 먼저 그리고 원점을 기준으로 각 범주에 해당되는 비율만큼 각도를 분할하여 표시한 그래프
 - 각도 = 비율 X 360º
 - 파이차트는 범주별로 비교할 때 약점이 있음
 
 
 <p align="center">
 <img width="320" height="320" src="https://cdn.pixabay.com/photo/2016/09/03/14/35/algorithms-1641857_960_720.png"/>
 

### 막대그래프(bar chart)
 - 각 범주의 도수나 상대도수를 막대의 길이로 표현
 - 파이차트보다 범주간의 비교에 용이
 
 
 <p align="center">
 <img height="320" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Bar_Chart_of_Race_%26_Ethnicity_in_Texas_%282015%29.svg/800px-Bar_Chart_of_Race_%26_Ethnicity_in_Texas_%282015%29.svg.png"/>
 
 
### 히스토그램(histogram)
 - 통계학에서는 막대그래프와 히스토그램을 엄격히 구분
 - 히스토그램은 수치자료 특히 연속자료가 어떤 형태로 분포되어 있는지를 알아보기 위해 사용
 - 해당 구간의 상대도수, 즉 비율을 직사각형의 면적으로 표시 => **전체 직사각형의 면적은 1**
 - 높이 = 상대도수 / 계급폭
 - 높이는 해당 구간에 자료들이 얼마나 모여 있는지를 나타내는 측도. 즉 밀도
 
 
 <p align="center">
 <img height="320" src="https://upload.wikimedia.org/wikipedia/commons/1/15/Symmetric-histogram.png"/>


### 줄기-잎 그림(stem-and-leaf)
 - 관측값의 정보를 그대로 간직하면서 자료가 어떻게 분포되어 있는지를 알려주는 그림
```
20 23 32 40 41 41 43 46 50 52 53 54 59 62 66 77 81 88 89 90
```

2 | 23

3 | 2

4 | 01136

5 | 02349

6 | 26

7 | 7

8 | 189

9 | 0


### 산점도(scatter plot)
 - 각각의 관측개체에 대해 두 변수의 값을 순서쌍 (x1, y1), (x2, y2) ... (xn, yn) 으로 표시할 수 있음
 - 산점도는 순서쌍 자료를 2차원 평면상에 점으로 표시하여 **두 변수들 간의 관계를 시각적으로 나타냄**
 
 <p align="center">
 <img height="320" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Scatter_diagram_for_quality_characteristic_XXX.svg/1026px-Scatter_diagram_for_quality_characteristic_XXX.svg.png"/>
 
 
## 04. 수치적해석
 - 그래프 같은 시각적 기법은 자료의 특성을 파악하는 데 있어 중요한 정보를 제공하지만 보는 사람에 따라 주관적으로 해석될 수 있음
 - 일반적으로 자료의 특성은 자료를 대표할 수 있는 중심 위치(central location) 산포(dispersion)로 표시
 
### 중심 위치
 - 조사, 실험, 관측 등을 통해 n개의 수치자료를 얻었고 그 값들을 <img src="https://latex.codecogs.com/gif.latex?x_%7B1%7D%2Cx_%7B2%7D%2C...%2Cx_%7Bn%7D"/> 이라고 표시할 때,
 - 표본의 개수 n을 표본 크기(sample size)라고 한다
 - 이들 자료에 대한 중심위치로 가장 많이 사용되는 통계값은 표본평균이며 대체 통계값으로 중앙값, 절사평균, 최빈값 등이 있음
 
### 표본평균(sample mean)
 - 표본평균은 표본의 합을 표본크기로 나눈 값
 - x bar 라고 읽음 => bar 표시는 해당 자료의 평균을 의미
 - 표본평균이 중심위치 중 적절한 이유 중 하나는 무게중심이기 때문
 - <img src="https://latex.codecogs.com/gif.latex?x_%7Bi%7D-%5Cbar%7Bx%7D"/> 를 i번째 표본의 편차(deviation)라고 함
 
<p align="center">
<img src="https://latex.codecogs.com/gif.latex?%5Cbar%7Bx%7D%3D%5Cfrac%7B1%7D%7Bn%7D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%20x_%7Bi%7D"/>
 
 - 표본평균은 자료 중에 일부 관측값이 대부분의 나머지 관측값들에서 멀리 떨어져 있는 경우인 이상점(outlier)에 유의해야 함
  => 표본평균은 이상점(outlier)에 robust 하지 않음
 
### 표본중앙값(median)
 - 자료를 크기순서대로(오름차순) 나열했을 때 가운데 위치에 있는 값(표본중위수 라고도 함)
 - 순서통계량임
 - 이상점에 로버스트(robust)하지만 중앙에 있는 하나 또는 두 개의 관측값만 직접 사용하므로 자료가 가진 정보를 다 활용하지 못함(평균과 반대)
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?x_%7B%281%29%7D%5Cleq%20x_%7B%282%29%7D%5Cleq%5Ccdots%20%5Cleq%20x_%7B%28n%29%7D"/>
 
### 표본절사평균(sample trimmed mean)
 - 표본평균과 표본중앙값 두 통계가 가지고 있는 장점을 살리면서 단점을 줄여주는 통계값
 - 표본중앙값을 계산할 때처럼 순서통계량을 구하고 순서통계량의 하위 a%에서 상위 a% 까지의 자료를 이용하여 표본평균을 계산한 것

### 최빈값(mode)
 - 자료 중 빈도가 가장 많은 값을 의미

### 퍼짐의 측도
 - 통계학에서 중심위치만큼 중요한 통계값이 산포(dispersion)
 - 산포는 자료들이 얼마나 퍼져 있는가를 나타낼뿐만 아니라 구한 중심위치가 얼마나 안정적이고 신뢰할 수 있는지에 대한 중요한 정보를 제공
 
### 범위(range)
 - 자료 중 가장 큰 값과 가장 작은 값의 차이
 - 자료 중 이상점이 있으면 전체 형태와 관계없이 범위가 클 수 있어 범위를 통해 퍼진 정도를 평가하기에는 무리가 있을 수 있음
 
### 사분위범위(interquartile range)
 - 사분위수(quartile)는 자료를 동일한 비율로 4등분 할 때의 세 위치
 - 자료를 오름차순으로 정렬했을 때, 25% 지점을 제1사분위수(Q1), 50% 지점을 제2사분위수(Q2), 75% 지점을 제3사분위수(Q3)라고 함
 - 제2사분위수(Q2) 는 표본중앙값과 같음
 - **제3사분위수과 제1사분위수의 간격**
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?IQR%3DQ_%7B3%7D-Q_%7B1%7D"/>
 
 - 사분위수와 사분위범위는 상자그림(box plot)을 그릴 때 사용

 <p align="center">
 <img height="320" src="https://cdn-images-1.medium.com/max/1600/1*2c21SkzJMf3frPXPAR_gZA.png"/>

### 표본분산과 표본표준편차
 - 범위나 사분위수 같은 경우 특정 위치의 두 값을 사용하기 때문에 표본의 정보를 많이 활용하지 못함
 - 이 때 생각해볼 수 있는 통계값은 모든 자료들 사이 거리의 합을 이용
 - 특히 <img src="https://latex.codecogs.com/gif.latex?D%28a%2Cb%29%3D%7Ca-b%7C%2C%20D%28a%2Cb%29%3D%28a-b%29%5E2"/> 에 대해 관심을 가짐
 - 위 식은 아래와 같이 표현이 가능
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%5Csum_%7Bj%3D1%7D%5E%7Bn%7D%7Cx_%7Bi%7D-x_%7Bj%7D%7C%2C%20%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%5Csum_%7Bj%3D1%7D%5E%7Bn%7D%28x_%7Bi%7D-x_%7Bj%7D%29%5E2"/>
 
 - 위의 측도를 사용하기 위해서는 **n의 제곱개의 거리 합을 이용해야 하므로 계산에 부담이 있음** => 중심위치 a에서 자료들이 떨어져 있는 거리의 합을 이용
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?L_%7B1%7D%28a%29%3D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%7Cx_%7Bi%7D-a%7C%2C%20L_%7B2%7D%28a%29%3D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28x_%7Bi%7D-a%29%5E2"/>
 
 - 위 식은 자료들의 모든 정보를 사용하면서 자료들이 a를 중심으로 얼마나 퍼져 있는지를 나타냄
 - a를 중심으로 모여 있으면 위의 값은 작아지고, 퍼져 있으면 커짐
 - 중심위치 a를 어떻게 선택하는지가 관건 => 자료들과의 거리가 가능한 짧아야 하며 결국 모든 자료들과의 거리 합을 최소로 만드는 값 필요
 - L2의 경우 L2'(a)=0 이 되는 값을 찾아야 함
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?%5Cfrac%7BdL_%7B2%7D%28a%29%7D%7Bda%7D%3D-2%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28x_%7Bi%7D-a%29%3D-2%5Cleft%20%5C%7B%20%5Csum_%7Bi%3D1%7D%5E%7Bn%7Dx_%7Bi%7D-na%20%5Cright%20%5C%7D%3D0"/>
 
 - 결론적으로 <img src="https://latex.codecogs.com/gif.latex?a%3D%5Cfrac%7B1%7D%7Bn%7D%5Csum_%7Bi%3D1%7D%5E%7Bn%7Dx_%7Bi%7D%3D%5Cbar%7Bx%7D"/> 가 되는데 이는 **L2(a)에서는 중심위치로 표본평균이 적절**하다는 의미
 
### 표본분산(sample variance)

<p align="center">
 <img src="https://latex.codecogs.com/gif.latex?s%5E2%3D%5Cfrac%7B1%7D%7Bn-1%7D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28x_%7Bi%7D-%5Cbar%7Bx%7D%29%5E2"/>

 - 표본크기 n이 아닌 n-1로 나눈 이유는 표본분산은 n개의 편차를 사용하는 것 같지만 **표본평균의 편차의 합이 0** 이라는 제약조건 대문에 n-1개의 편차만 자유롭게 값을 가질 수 있고 마지막 편차는 합이 0이 되게 하는 역할만 하기 때문
 - 이 n-1을 자유롭게 가질 수 있는 편차의 개수라고 해서 **자유도(degree of freedom)** 라고 함
 - 위 식을 정리하면 아래와 같다

 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?s%5E2%3D%5Cfrac%7B1%7D%7Bn-1%7D%5Cleft%20%5C%7B%20%5Csum_%7Bi%3D1%7D%5E%7Bn%7Dx_%7Bi%7D%5E2%20-%5Cfrac%7B1%7D%7Bn%7D%5Cleft%20%28%20%5Csum_%7Bi%3D1%7D%5E%7Bn%7Dx_%7Bi%7D%5E2%20%5Cright%20%29%20%5Cright%20%5C%7D"/>
 
### 표본표준편차(sample standard deviation)
 - 표본분산은 편차의 제곱합을 이용하기 때문에 관측값 단위의 제곱이 되어 직관적으로 파악하기 어려움
 - 우리가 눈으로 이해하는 산포와 일치시키려면 제곱근을 취함
 - **표본분산의 제곱근은 관측값과 동일한 단위로 퍼짐의 측도가 되며 이를 표본표준편차**라 함 

 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?s%3D%5Csqrt%7Bs%5E2%7D%3D%5Csqrt%7B%5Cfrac%7B1%7D%7Bn-1%7D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28x_%7Bi%7D-%5Cbar%7Bx%7D%29%5E2%7D"/>
 
### 표준화
 - 수능시험은 과목별로 난이도가 다를 수 있기 때문에 원점수로 과목 간 성적을 비교하면 문제가 있을 수 있음
 - 이런 경우 아래와 같이 원점수에 평균을 빼고 표준편차를 나누어 점수를 표준화하여 상대 비교를 함
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?z_%7Bi%7D%3D%5Cfrac%7Bx_%7Bi%7D-%5Cbar%7Bx%7D%7D%7Bs%7D"/>

 - **표준화는 평균이 0, 표준편차가 1이 되도록 만듬**
 - 측정 단위에 영향을 받지 않게 중심위치와 척도를 조정하고 상대적 비교를 가능하게 함
 
 
### 변동계수(coefficient of variation)
 - 일반적으로 선진국 소득의 표준편차가 후진국의 표준편차보다 훨씬 큼 => 비교 그룹 간의 평균이 큰 차이가 있고 평균이 커지면 산포 또한 커지는 경향이 있는 자료이기 때문
 - 이런 경우 표준편차 자체만 이용하여 산포를 비교하는 것은 적절치 않을 수 있어 평균으로 표본표준편차를 보정한 변동계수를 사용할 수 있음
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?CV%3D%5Cfrac%7Bs%7D%7B%5Cbar%7Bx%7D%7D"/>
 
### 상관 정도
 - 두 수치변수 간에 직선관계가 어느 정도인지를 나타내는 통계값
 
 <p align="center">
 <img height="320" src="https://upload.wikimedia.org/wikipedia/commons/a/af/Scatter_diagram_for_quality_characteristic_XXX.svg"/>
 
 - 위 그림에서 두 변수 가로축을 x, 세로축을 y로 볼 때, x와 y의 자료가 음의 기울기를 가지고 있음(2사분면과 4사분면에 자료들이 많이 분포)
 - 그림의 형태가 반대라면 x와 y가 양의 기울기를 가짐(1사분면과 3사분면에 자료들이 많이 분포)
 - 이러한 성질을 반영할 수 있는 값 => 각 변수의 편차를 곱한 <img src="https://latex.codecogs.com/gif.latex?%28x_%7Bi%7D-%5Cbar%7Bx%7D%29%28y_%7Bi%7D-%5Cbar%7By%7D%29" /> : 1과 3사분면의 값은 양수, 2와 4사분면의 값은 음수

### 표본공분산(sample convariance)
 - 위의 식에서 양의 기울기를 갖는 값이라면 각 변수의 편차의 합인 <img src="https://latex.codecogs.com/gif.latex?%5Csum%20%28x_%7Bi%7D-%5Cbar%7Bx%7D%29%28y_%7Bi%7D-%5Cbar%7By%7D%29"/> 는 양의 값을 가질 것이고 반대로 음의 기울기를 갖는 값이라면 편차의 합은 음의 값을 가짐
 - 위 식에 표본분산을 계산할 때처럼 자유도를 적용
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?C_%7Bxy%7D%3D%5Cfrac%7B1%7D%7Bn-1%7D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28x_%7Bi%7D-%5Cbar%7Bx%7D%29%28y_%7Bi%7D-%5Cbar%7By%7D%29"/>

 - 두 변수 x와 y의 분산형태를 가진다고 하여 통계값 <img src="https://latex.codecogs.com/gif.latex?C_%7Bxy%7D">를 표본공분산이라 함

 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?C_%7Bxy%7D%3D%5Cfrac%7B1%7D%7Bn-1%7D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28x_%7Bi%7D-%5Cbar%7Bx%7D%29%28y_%7Bi%7D-%5Cbar%7By%7D%29%5C%5C%20%3D%5Cfrac%7B1%7D%7Bn-1%7D%5Cleft%20%5C%7B%20%5Csum_%7Bi%3D1%7D%5E%7Bn%7Dx_%7Bi%7Dy_%7Bi%7D-n%5Cbar%7Bx%7D%5Cbar%7By%7D%20%5Cright%20%5C%7D%5C%5C%20%3D%5Cfrac%7B1%7D%7Bn-1%7D%5Cleft%20%5C%7B%20%5Csum_%7Bi%3D1%7D%5E%7Bn%7Dx_%7Bi%7Dy_%7Bi%7D-%5Cfrac%7B1%7D%7Bn%7D%5Csum_%7Bi%3D1%7D%5E%7Bn%7Dx_%7Bi%7D%5Csum_%7Bi%3D1%7D%5E%7Bn%7Dy_%7Bi%7D%20%5Cright%20%5C%7D"/>

### 표본상관계수(coefficient of correlation)
 - 공분산을 사용하는데 있어 문제점은 **측정 단위에 영향을 받기 때문에 그 값 자체로 선형관계의 정도를 알 수 없다**는 점
 - 해결방법은 측정단위에 영향을 받지 않게 자료를 표준화하여 표본분산을 구하는 것

 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?R_%7Bxy%7D%3D%5Cfrac%7B1%7D%7Bn-1%7D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%5Cleft%20%28%20%5Cfrac%7Bx_%7Bi%7D-%5Cbar%7Bx%7D%7D%7Bs_%7Bx%7D%7D%20%5Cright%20%29%5Cleft%20%28%20%5Cfrac%7By_%7Bi%7D-%5Cbar%7By%7D%7D%7Bs_%7By%7D%7D%20%5Cright%20%29"/>
 
 - 표본상관계수 간편식
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?S_%7Bxy%7D%3D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28x_%7Bi%7D-%5Cbar%7Bx%7D%29%28y_%7Bi%7D-%5Cbar%7By%7D%29%3D%5Csum_%7Bi%3D1%7D%5E%7Bn%7Dx_%7Bi%7Dy_%7Bi%7D-n%5Cbar%7Bx%7D%5Cbar%7By%7D%5C%5C%20S_%7Bxx%7D%3D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28x_%7Bi%7D-%5Cbar%7Bx%7D%29%5E2%3D%5Csum_%7Bi%3D1%7D%5E%7Bn%7Dx_%7Bi%7D%5E2-n%5Cbar%7Bx%7D%5E2%5C%5C%20S_%7Byy%7D%3D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28y_%7Bi%7D-%5Cbar%7By%7D%29%5E2%3D%5Csum_%7Bi%3D1%7D%5E%7Bn%7Dy_%7Bi%7D%5E2-n%5Cbar%7By%7D%5E2"/>
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?R_%7Bxy%7D%3D%5Cfrac%7B%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28x_%7Bi%7D-%5Cbar%7Bx%7D%29%28y_%7Bi%7D-%5Cbar%7By%7D%29%7D%7B%5Csqrt%7B%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28x_%7Bi%7D-%5Cbar%7Bx%7D%29%5E2%7D%5Csqrt%7B%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28y_%7Bi%7D-%5Cbar%7By%7D%29%5E2%7D%7D%3D%5Cfrac%7BS_%7Bxy%7D%7D%7B%5Csqrt%7BS_%7Bxx%7D%7D%5Csqrt%7BS_%7Byy%7D%7D%7D"/>
 
 - 여기서 <img src="https://latex.codecogs.com/gif.latex?S_%7Bxx%7D%2C%20S_%7Byy%7D"/>는 편차의 제곱합으로 수정제곱합(corrected sum of squares) 라고 함

### 표본상관계수의 성질
 - <img src="https://latex.codecogs.com/gif.latex?-1%20%5Cleq%20R_%7Bxy%7D%20%5Cleq%201"/>
 - 자료들이 어떤 기울기를 가지는 직선에 조밀하게 모일수록 <img src="https://latex.codecogs.com/gif.latex?%7CR_%7Bxy%7D%7C"/> 는 1에 근접
 - 음의 기울기를 가지는 직선 주위에 자료가 분포되어 있는 경우 <img src="https://latex.codecogs.com/gif.latex?R_%7Bxy%7D"/> 는 음수이며, 음의 상관관계가 있음(양의 기울기 -> 양의 상관관계)
 - 모든 관측값이 직선 위에 위치하면 <img src="https://latex.codecogs.com/gif.latex?%7CR_%7Bxy%7D%7C%3D1"/>
 

## 05. 확률(1) 기본개념

### 확률실험(random experiment)
 - 아래 두 특징을 가지는 실험
  1. 실험을 시행하기 전에도 발생할 수 있는 모든 결과를 알 수 있음
  2. 실험 전까지 결과 중 무엇이 발생할 것인지 정확하게 예측할 수 없음

### 표본공간(sample space : Ω)
 - 확률실험에서 발생 가능한 모든 결과들을 모아놓은 집함
 - 표본공간 내에서 우리가 관심을 가지는 부분집합 => **사건(event)**
 - 확률(probability)은 이러한 사건이 발생할 가능성이 얼마나 되는지를 나타내는 수치적 측도
 
### 서로배반사건(disjoint, mutually exclusive)
 - 임의의 두 사건 A와 B가 동시에 일어날 수 없는 경우
 - <img src="https://latex.codecogs.com/gif.latex?A%5Ccap%20B%3D%5Co"/>
 
### 집합의 정의와 연산
 - 분배법칙 : <img src="https://latex.codecogs.com/gif.latex?%28A%5Ccup%20B%29%5Ccap%20C%20%3D%20%28A%5Ccap%20C%29%5Ccup%20%28B%5Ccap%20C%29"/>
 - 드모르간의 법칙 : <img src="https://latex.codecogs.com/gif.latex?%28A%5Ccap%20B%29%5Ec%3DA%5Ec%5Ccup%20B%5EC%2C%20%28A%5Ccup%20B%29%5Ec%3DA%5Ec%5Ccap%20B%5EC%2C"/>
 
### 경우의 수(number of cases)
 - 어떤 실험을 했을 때 발생할 수 있는 결과의 개수, 즉 원소의 개수
 - 경우의 수를 계산하는데 있어 기본 법칙은 곱의 법칙

|  | 비복원 | 복원 |
| - | - | - |
| 순서고려 | 순열 | 중복순열 |
| 순서무시 | 조합 | 중복조합 |

### 순열(permutatioin)
 - 순서를 고려하면서 n개 중에서 k개를 비복원추출하여 얻어진 순서열
 - 순열은 각 단계에서 선택할 수 있는 개체의 수가 하나씩 줄어듬
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?n%20%5Ctimes%20%28n-1%29%20%5Ctimes%20%5Ccdots%20%5Ctimes%20%28n-k&plus;1%29%3D%5Cfrac%7Bn%21%7D%7B%28n-k%29%21%7D"/>
 
### 중복순열
 - 순서를 고려하면서 n개 중에서 k개를 복원추출하여 얻어진 순서열
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?n%20%5Ctimes%20%5Ccdots%20%5Ctimes%20n%20%3D%20n%5Ek"/>
 
### 조합(combination)
 - 순서를 고려하지 않고 n개 중에서 k개를 비복원추출
 - 비복원추출에서 순서를 고려하지 않는다면 k개의 순서조합 k!을 나누어주어야 함
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?%5Cfrac%7Bn%20%5Ctimes%20%28n-1%29%20%5Ctimes%20%5Ccdots%20%5Ctimes%20%28n-k&plus;1%29%7D%7B1%20%5Ctimes%202%20%5Ctimes%20%5Ccdots%20%5Ctimes%20k%7D%3D%5Cfrac%7Bn%21%7D%7Bk%21%28n-k%29%21%7D%3D%5Cbinom%7Bn%7D%7Bk%7D"/>

### 중복조합
 - 순서를 고려하지 않고 n개 중에서 k개를 복원추출

 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?%5Cfrac%7Bn%28n&plus;1%29%5Ctimes%20%5Ccdots%20%5Ctimes%20%28n&plus;k-1%29%7D%7Bk%21%7D%3D%5Cfrac%7B%28n&plus;k-1%29%21%7D%7Bk%21%28n-1%29%21%7D%3D%5Cbinom%7Bn&plus;k-1%7D%7Bk%7D"/>
