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

## 06. 확률(2) 기본정리,조건부확률

### 상대도수의 극한(통계적 확률)
 - 동전을 던질 때 앞면이 나올 사건을 A라고 하면 P(A)=1/2
 - 고전적 확률에서는 앞면과 뒷면의 발생가능성이 동일하고 Ω={H,T} 이고 A={H} 이므로 P(A)=1/2라고 해석
 
 | 실험자 | 던진 회수 | 앞면 | 상대도수 |
 | - | - | - | - |
 | Buffon | 4040 | 2048 | 0.5080 |
 | Pearson | 12000 | 6019 | 0.5016 |
 | Pearson | 24000 | 12012 | 0.5005 |
 
 - 위 표는 과거 통계학자들이 실시했던 동전 던지기 실험결과
 - 실험횟수가 어느정도 큰 경우 상대도수가 직관적 값인 0.5 근처
 - 표본공간의 각 원소가 발생가능성이 동일하지 않은 경우에도 확률을 구할 수 있어야함
  ex) 윳을 던졌을 때 젖혀질 확률
 - 한 가지 방법은 계속해서 윷을 던져 "던진 횟수"에서 "뒤집힌 횟수"의 비율을 구하여 젖혀질 확률의 근사값으로 사용하는 것
 - 젖혀질 사건을 A라고 하고 n(A)를 윷을 n번 던졌을 때 윷이 젖혀진 횟수라고 하면
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?P%28A%29%5Capprox%20%5Cfrac%7Bn%28A%29%7D%7Bn%7D"/>
 
  - 만약 **실험을 무한히 반복한다면 n(A)/n 은 어떤 값으로 수렴하는데 이 극한값을 사건 A가 일어날 확률**로 해석하자는 것
  
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?P%28A%29%3D%5Clim_%7Bn%20%5Cto%20%5Cinfty%20%7D%5Cfrac%7Bn%28A%29%7D%7Bn%7D"/>
 
 - 확률은 표본이 아니라 모집단이 어떤 형태로 이루어져 있는지를 표시(표본이 무한히 많아짐)
 - 상대도수의 극한은 많은 표본을 통해 모집단의 특성을 파악한다고 해서 **통계적 확률(statistical probability)**이라고도 함
 
### 확률의 공리
```
공리 1. P(Ω) = 1
공리 2. 사건 A ⊂ Ω 에 대해, 0 ≤ P(A) ≤ 1
공리 3. 서로배반인 사건 A와 B에 대해, P(A∪B) = P(A) + P(B)
```

 - 공리(axiom)란 증명할 수 없으나 옳다고 판단되는 명제

### 확률의 기본 성질
 - <img src="https://latex.codecogs.com/gif.latex?P%28A%5Ec%29%3D1-P%28A%29"/>
 - <img src="https://latex.codecogs.com/gif.latex?A%20%5Csubset%20B"/> 이면, <img src="https://latex.codecogs.com/gif.latex?P%28A%29%5Cleq%20P%28B%29"/>
 - <img src="https://latex.codecogs.com/gif.latex?P%28A%5Ccup%20B%29%3DP%28A%29&plus;P%28B%29-P%28A%5Ccap%20B%29"/>
 - <img src="https://latex.codecogs.com/gif.latex?P%28A%20%5Ccup%20B%29%20%5Cleq%20P%28A%29%20&plus;%20P%28B%29"/>
 
### 조건부확률(conditional probability)
 - 동전 두 개를 던지는 실험에서 어떤 한 동전이 앞면이라는 것을 알았을 때, 두 동전이 모두 앞면일 사건의 확률을 구한다고 가정
 - 두 동전을 던질 경우 표본 공간 Ω = {HH, TH, HT, TT}
 - 여기서 어떤 한 동전이 앞면이라는 정보가 추가로 주어지면 표본공간에서 {TT}가 발생할 수 없음
 - 때문에 **표본공간은 {HH, TH, HT} 로 축소** -> 이 표본공간에서 두 동전 모두 앞면일 사건의 확률은 1/3
 - **확률실험을 하는 과정에서 새로운 정보 또는 조건이 추가되었을 때 사건의 확률을 조건부확률**이라고 함
 - 사건 A가 주어졌을 때 사건 B의 조건부확률은 P(B|A)로 표시하고 다음과 같이 수식으로 정의 ( P(A) > 0 )
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?P%28B%7CA%29%3D%5Cfrac%7BP%28A%20%5Ccap%20B%29%7D%7BP%28A%29%7D"/>
 
### 조건부확률의 응용
 - <img src="https://latex.codecogs.com/gif.latex?P%28A%29%3E0%2CP%28B%29%3E0"/> 이면 <img src="https://latex.codecogs.com/gif.latex?P%28A%5Ccap%20B%29%3DP%28A%29P%28B%7CA%29%3DP%28B%29P%28A%7CB%29"/>
 - <img src="https://latex.codecogs.com/gif.latex?P%28A_%7B1%7D%5Ccap%20%5Ccdots%20%5Ccap%20A_%7Bn-1%7D%29%3E0"/> 이면
 <img src="https://latex.codecogs.com/gif.latex?P%28A_%7B1%7D%5Ccap%20%5Ccdots%20%5Ccap%20A_%7Bn%7D%29%3DP%28A_%7B1%7D%29P%28A_%7B2%7D%7CA_%7B1%7D%29P%28A_%7B3%7D%7CA_%7B1%7D%5Ccap%20A_%7B2%7D%29%5Ccdots%20P%28A_%7Bn%7D%7CA_%7B1%7D%5Ccap%5Ccdots%5Ccap%20A_%7Bn-1%7D%29"/>

### 표본공간의 분할(partition)
 1. 서로배반사건, 즉 모든 <img src="https://latex.codecogs.com/gif.latex?i%5Cneq%20j"/> 에 대해 <img src="https://latex.codecogs.com/gif.latex?A_%7Bi%7D%5Ccap%20A_%7Bj%7D%3D%5Cvarnothing"/>
 2. 전체를 이루는 사건(exhaustive), 즉 <img src="https://latex.codecogs.com/gif.latex?A_%7B1%7D%5Ccup%20%5Ccdots%20%5Ccup%20A_%7Bn%7D%3D%5COmega"/>
 
 - 위 두 조건을 만족하면 사건 <img src="https://latex.codecogs.com/gif.latex?A_%7B1%7D%2C%5Ccdots%20A_%7Bn%7D"/> 을 **표본공간의 분할(partition)** 이라고 함
 - 사건 <img src="https://latex.codecogs.com/gif.latex?A_%7B1%7D%2C%5Ccdots%20A_%7Bn%7D"/> 이 표본공간의 분할일 때 <img src="https://latex.codecogs.com/gif.latex?B%5Ccap%20A_%7B1%7D%2CB%5Ccap%20A_%7B2%7D%2C%5Ccdots%20%2C%20B%5Ccap%20A_%7Bn%7D"/> 은 서로배반인 사건이므로 다음 등식이 성립(벤다이어그램 그려서 해볼 것)
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?P%28B%29%3DP%28B%7C%5COmega%20%29%3DP%28B%5Ccap%20A_%7B1%7D%29%5Ccup%20%5Ccdots%20%5Ccup%20P%28B%5Ccap%20A_%7Bn%7D%29%5C%5C%20%3D%20P%28B%5Ccap%20A_%7B1%7D%29&plus;%5Ccdots%20&plus;%20P%28B%5Ccap%20A_%7Bn%7D%29%3DP%28A_%7B1%7D%29P%28B%7CA_%7B1%7D%29%5Ccdots%20P%28A_%7Bn%7D%29P%28B%7CA_%7Bn%7D%29"/>
 
 - 위 내용을 바탕으로
 
 
 3. <img src="https://latex.codecogs.com/gif.latex?P%28A%29%3E0%2C%20P%28A%5Ec%29%3E0"/> 이면 <img src="https://latex.codecogs.com/gif.latex?P%28B%29%3DP%28A%29P%28B%7CA%29&plus;P%28A%5Ec%29P%28B%7CA%5Ec%29"/>
 4. 사건 <img src="https://latex.codecogs.com/gif.latex?A_%7B1%7D%2C%5Ccdots%20A_%7Bn%7D"/> 가 표본공간의 분할이고 각 <img src="https://latex.codecogs.com/gif.latex?i"/> 에 대해 <img src="https://latex.codecogs.com/gif.latex?P%28A_%7Bi%7D%29%3E0"/> 이면 임의의 사건 B에 대해

 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?P%28B%29%3D%5Csum_%7Bi%3D1%7D%5E%7Bn%7DP%28B%5Ccap%20A_%7Bi%7D%29%3D%5Csum_%7Bi%3D1%7D%5E%7Bn%7DP%28A_%7Bi%7D%29P%28B%7CA_%7Bi%7D%29"/>
 
 
## 07. 확률(2) 베이즈정리
 - 조건부확률 P(B|A) 은 순서적으로 볼 때, 대부분 사건 A가 먼저 발생하고 B가 이어 발생하는 상황으로 A는 원인, B는 결과의 형태를 가짐
 - 이 같은 상황에서 원인의 가능성을 나타내는 P(A) 또는 P(A^c)를 사건 B가 관측되기 이전의 확률이라고 해서 사전확률(prior probability)라고 함
 - P(B) > 0 이면 조건부확률 정의에 의해
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?P%28A%7CB%29%3D%5Cfrac%7BP%28A%5Ccap%20B%29%7D%7BP%28B%29%7D"/>
 
 - 여기에 <img src="https://latex.codecogs.com/gif.latex?P%28A%29%3E0%2C%20P%28A%5Ec%29%3E0"/> 라는 추가조건이 주어지면, 조건부확률의 응용 1,3을 분모와 분자에 각각 적용하면
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?P%28A%7CB%29%3D%5Cfrac%7BP%28A%5Ccap%20B%29%7D%7BP%28B%29%7D%3D%5Cfrac%7BP%28A%29P%28B%7CA%29%7D%7BP%28A%29P%28B%7CA%29&plus;P%28A%5Ec%29P%28B%7CA%5Ec%29%7D"/>
 
 - 위 식을 일반적으로 베이즈정리(Bayes' theorem) 라고 함
 - 이 식에 의하면 결과 B가 주어졌을 때 원인 A의 확률을 사전확률 <img src="https://latex.codecogs.com/gif.latex?P%28A%29%2CP%28A%5Ec%29"/> 와 일반적인 순서의 조건부확률을 이용하여 계산할 수 있음
 - 베이즈 정리를 조건부확률 응용 4를 이용하여 일반식으로 확장 가능
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?P%28A_%7Bk%7D%7CB%29%3D%5Cfrac%7BP%28A_%7Bk%7D%29P%28B%7CA_%7Bk%7D%29%7D%7BP%28B%29%7D%3D%5Cfrac%7BP%28A_%7Bk%7D%29P%28B%7CA_%7Bk%7D%29%7D%7B%5Csum_%7Bi%3D1%7D%5E%7Bn%7DP%28A_%7Bi%7D%29P%28B%7CA_%7Bi%7D%29%7D"/>
 
### 독립사건(independent events)
 - 앞서 조건부확률을 이용하여 교사건을 연속적인 조건부확률의 곱으로 계산할 수 있음을 보임. P(A) > 0 , P(B) > 0 이면, 아래가 항상 성립
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?P%28A%5Ccap%20B%29%3DP%28A%29P%28B%7CA%29%3DP%28B%29P%28A%7CB%29"/>
 
 - 만약 사건 A가 사건 B의 발생에 영향을 주지 않는다면 P(B|A) = P(B) 로 쓸 수 있음. 마찬가지로 P(A|B) = P(A)
 - 이와 같이 **사건 A와 B가 서로 영향을 주고받지 않는 경우 "사건 A와 B는 독립사건 또는 독립적"** 이다 라고 함 ( 아래 수식으로 표현 )
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?P%28A%5Ccap%20B%29%3DP%28A%29P%28B%29"/>
 
 - 위 식이 성립하면 "A와 B는 독립사건이다" 성립하지 않는 경우에는 "A와 B는 종속사건(dependent events) 또는 종속적이다"
 - 표본공간 Ω와 Φ는 다른 모든 사건과 독립 ( 위 식에 대입해볼 것 )
 - 일반적인 n개의 사건 <img src="https://latex.codecogs.com/gif.latex?A_%7B1%7D%2CA_%7B2%7D%2C%5Ccdots%20%2CA_%7Bn%7D"/> 이 서로 독립적이면 n개로 이루어진 조합의 곱사건 확률이 해당 사건들의 확률의 곱으로 표시됨
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?P%28A_%7B1%7D%5Ccap%20A_%7B2%7D%5Ccap%20%5Ccdots%20%5Ccap%20A_%7Bn%7D%29%3DP%28A_%7B1%7D%29P%28A_%7B2%7D%29%5Ccdots%20P%28A_%7Bn%7D%29%3D%5Cprod_%7Bi%3D1%7D%5E%7Bn%7DP%28A_%7Bi%7D%29"/>

## 08. 확률변수와 확률분포 (1)

### 확률변수(random variable)
 - 표본공간의 원소를 숫자로 대응시키는 함수
 - 동전의 앞면을 H, 뒷면을 T라고 할 때 동전을 세 번 던지는 확률실험의 표본공간은 다음과 같음
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?%5COmega%20%3D%5Cleft%20%5C%7B%20HHH%2C%20HHT%2C%20HTH%2C%20THH%2C%20HTT%2C%20THT%2C%20TTH%2C%20TTT%20%5Cright%20%5C%7D"/>
 
 - 이 확률실험에서 앞면의 수(X)나 앞면과 뒷면의 수의 차이(Y)에 관심이 있다고 하면 아래와 같이 표현 가능
 
 | Ω | HHH | HHT | HTH | THH | HTT | THT | TTH | TTT |
 | - | - | - | - | - | - | - | - | - |
 | X | 3 | 2 | 2 | 2 | 1 | 1 | 1 | 0 |
 | Y | 3 | 1 | 1 | 1 | 1 | 1 | 1 | 3 |
 
 - 여기서 X와 Y는 표본공간의 원소를 숫자로 바꾸어 주는 역할을 함
 
 <p align="center">
 <img height="320" src="https://upload.wikimedia.org/wikipedia/commons/c/c4/Random_Variable_as_a_Function-en.svg"/>
 
### 이산확률변수(countable random variable)
 - 확률변수 X가 가질 수 있는 값들이 가산(countable)이거나 셀 수 있는 경우
 
### 연속확률변수(countinuous random variable) 
 - 확률변수 X가 가질 수 있는 값들이 셀 수 없을 정도로 많은 경우

### 확률분포(probability distribution)
 - 확률변수의 값에 대해 확률을 표시한 것
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?P%28X%3D0%29%3DP%28%5Cleft%20%5C%7B%20TTT%20%5Cright%20%5C%7D%29%3D%5Cfrac%7B1%7D%7B8%7D"/>
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?P%28X%3D1%29%3DP%28%5Cleft%20%5C%7B%20HTT%2CTHT%2C%20TTH%20%5Cright%20%5C%7D%29%3D%5Cfrac%7B3%7D%7B8%7D"/>
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?P%28X%3D1%29%3DP%28%5Cleft%20%5C%7B%20HHT%2CHTH%2C%20THH%20%5Cright%20%5C%7D%29%3D%5Cfrac%7B3%7D%7B8%7D"/>
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?P%28X%3D1%29%3DP%28%5Cleft%20%5C%7B%20HHH%20%5Cright%20%5C%7D%29%3D%5Cfrac%7B1%7D%7B8%7D"/>
  
### 확률분포표(probability distribution table)
 - 확률분포를 표로 표시한 것

| x | 0 | 1 | 2 | 3 |
| - | - | - | - | - |
| P(X=x) | 1/8 | 3/8 | 3/8 | 1/8 |

### 확률질량함수(probability mass function)
 - 이산확률변수 X가 임의의 값 x일 확률 P(X=x)를 x에 대한 함수로 생각하면 아래와 같이 표현 가능
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?f%28x%29%3DP%28X%3Dx%29"/>
 
 - 이 때, f(x)를 확률변수 X의 확률질량함수라고 함
 - 동전을 세 번 던졌을 때 앞면의 수를 X라고 하면 X가 가질 수 있는 값은 x=0,1,2,3 이고 이에 대한 확률질량함수는 위에서 보인 것처럼
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?f_%7BX%7D%280%29%3D%5Cfrac%7B1%7D%7B8%7D%2Cf_%7BX%7D%281%29%3D%5Cfrac%7B3%7D%7B8%7D%2Cf_%7BX%7D%282%29%3D%5Cfrac%7B2%7D%7B8%7D%2Cf_%7BX%7D%283%29%3D%5Cfrac%7B1%7D%7B8%7D"/>
 
 - x=0,1,2,3 외의 값의 확률은 이들 값에 대응하는 표본공간의 원소가 없기 때문에 0
 - X가 가질 수 있는 값이 <img src="https://latex.codecogs.com/gif.latex?x_%7B1%7D%2Cx_%7B2%7D%2Cx_%7B3%7D%2C%5Ccdots"/> 이면
 
 
 1. 모든 <img src="https://latex.codecogs.com/gif.latex?i%3D1%2C2%2C%5Ccdots"/> 에 대해 <img src="https://latex.codecogs.com/gif.latex?0%5Cleq%20f%28x_%7Bi%7D%29%5Cleq%201"/>
 2. <img src="https://latex.codecogs.com/gif.latex?%5Csum_%7Bi%3D1%7D%5E%7B%5Cinfty%20%7Df%28x_%7Bi%7D%29%3D1"/>
 3. <img src="https://latex.codecogs.com/gif.latex?P%28a%5Cleq%20X%5Cleq%20b%29%3D%5Csum_%7Bx_%7Bi%7D%5Cin%20%5Cleft%20%5B%20a%2Cb%20%5Cright%20%5D%7Df%28x_%7Bi%7D%29"/>
 
### 확률밀도함수(probability density function)
- 히스토그램의 자료를 계속 추가하면서 계급의 폭을 줄이면 점점 세밀한 형태를 가지게 되고 아래와 같이 모집단의 형태를 나타내는 밀도를 얻음

 <p align="center">
 <img height="320" src="https://upload.wikimedia.org/wikipedia/commons/8/87/Logistic2.png"/>

- 임의의 지점 x에서의 밀도를 f(x)라고 표시하면 f(x)를 확률밀도함수라고 함
- 히스토그램에서 어떤 계급의 면적이 해당 계급의 비율(상대도수)였던 것처럼 어떤 구간에서 확률밀도함수의 면적은 해당 구간에서의 확률이 됨

 <p align="center">
 <img height="320" src="https://upload.wikimedia.org/wikipedia/commons/3/32/Tinnitusmodel_input_soundPDF_cumulative.png"/>

 - X가 구간 a, b에 속할 확률은
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?P%28a%5Cleq%20X%5Cleq%20b%29%3D%5Cint_%7Ba%7D%5E%7Bb%7Df%28x%29dx"/>
 
 - 연속확률변수에 대한 확률은 확률밀도함수에서 해당 **면적** => 확률질량함수와 다르게 해당 점에서의 확률이 아님
 - X=3 일 확률은 3에서의 면적은
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?P%28X%3D3%29%3D%5Cint_%7B3%7D%5E%7B3%7Df%28x%29dx%3D0"/>
 
 - 그러므로 X가 연속확률변수이면 아래가 성립
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?P%28a%3CX%3Cb%29%3DP%28a%3CX%5Cleq%20b%29%3DP%28a%5Cleq%20X%3Cb%29%3DP%28a%5Cleq%20X%20%5Cleq%20b%29"/>
 
 - 확률밀도함수 f(x)는 다음과 같은 성질을 만족
 
 1. 모든 x에 대해 <img src="https://latex.codecogs.com/gif.latex?f%28x%29%5Cgeq%200"/>
 2. <img src="https://latex.codecogs.com/gif.latex?%5Cint_%7B-%5Cinfty%20%7D%5E%7B%5Cinfty%20%7Df%28x%29dx%3D1"/>
 3. <img src="https://latex.codecogs.com/gif.latex?P%28a%5Cleq%20X%5Cleq%20b%29%3D%5Cint_%7Ba%7D%5E%7Bb%7Df%28x%29dx"/>
 
## 09. 확률변수와 확률분포 (2)

### 모평균(population mean)
 - 이산모집단으로부터 임의로 5개의 표본을 선택하였는데 그 값이 각각 1, 1, 2, 5, 6 이라고 가정
 - 이 표본들의 표본 평균은 <img src="https://latex.codecogs.com/gif.latex?%5Cbar%7Bx%7D%3D%5Cfrac%7B1&plus;1&plus;2&plus;5&plus;6%7D%7B5%7D%3D1%5Ctimes%20%5Cfrac%7B2%7D%7B5%7D&plus;2%5Ctimes%20%5Cfrac%7B1%7D%7B5%7D&plus;5%5Ctimes%20%5Cfrac%7B1%7D%7B5%7D&plus;6%5Ctimes%20%5Cfrac%7B1%7D%7B5%7D"/>
 - 위 식을 보면 표본평균은 **관측된 값에 그 값이 차지하는 표본비율을 곱하여 더한 것** 으로 표시
 - 표본크기가 n이고 자료 중 서로 다른 값이 k개가 있어 이들 값을 <img src="https://latex.codecogs.com/gif.latex?x_%7B1%7D%2C%5Ccdots%20%2Cx_%7Bk%7D"/>, 표본 중 <img src="https://latex.codecogs.com/gif.latex?x_%7B1%7D"/> 의 값을 가지는 자료의 개수를 <img src="https://latex.codecogs.com/gif.latex?n_%7B1%7D"/> 라고 하면, <img src="https://latex.codecogs.com/gif.latex?%5Csum_%7Bi%3D1%7D%5E%7Bk%7Dn_%7Bi%7D%3Dn"/> 이고 표본평균은
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?%5Cbar%7Bx%7D%3D%5Cfrac%7Bx_%7B1%7Dn_%7B1%7D&plus;%5Ccdots%7B%7D&plus;%20x_%7Bk%7Dn_%7Bk%7D%7D%7Bn%7D%3D%5Csum_%7Bi%3D1%7D%5E%7Bk%7Dx_%7Bi%7D%5Cfrac%7Bn_%7Bi%7D%7D%7Bn%7D%3D%5Csum_%7Bi%3D1%7D%5E%7Bk%7Dx_%7Bi%7Dp_%7Bi%7D"/>
 
 - 표본크기 n을 계속 크게 하면 통계적 확률의 관점에서 볼 때 표본들은 모집단으로, 표본비율 <img src="https://latex.codecogs.com/gif.latex?p_%7Bi%7D"/>는 확률질량함수 <img src="https://latex.codecogs.com/gif.latex?f%28x_%7Bi%7D%29"/>로, 표본평균은 모평균으로 수렴
 
 - 통계학에서는 확률변수 X의 모평균을 아래와 같이 정의
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?%5Cmu%20%3D%20%5Csum_%7Bx%7Dxf%28x%29"/>
 
 - <img src="https://latex.codecogs.com/gif.latex?%5Csum_%7Bx%7D"/>는 X가 가질 수 있는 모든 x값에 대해 더한다는 의미
 - **기대값(expected value)** 은 확률변수에 대해 평균적으로 기대하는 값이라는 의미를 갖는 용어로 평균과 같은 개념
 - 연속확률변수에서의 기대값은 이산형의 기대값에서 <img src="https://latex.codecogs.com/gif.latex?%5Csum"/>를 <img src="https://latex.codecogs.com/gif.latex?%5Cint"/>으로 바꾸고 확률질량함수 <img src="https://latex.codecogs.com/gif.latex?f%28x%29%3DP%28X%3Dx%29"/>를 확률밀도함수에서 단위길이를 곱한 <img src="https://latex.codecogs.com/gif.latex?f%28x%29dx"/>로 바꾸어 계산
 
 
### 확률변수 X의 기대값(평균)
 - 이산확률변수
 - <img src="https://latex.codecogs.com/gif.latex?%5Csum_%7Bx%7Dxf%28x%29"/>
 - 연속확률변수
 - <img src="https://latex.codecogs.com/gif.latex?%5Cint%20xf%28x%29dx"/>
 
 
### 확률변수 X의 함수 g(X)의 기대값
 - 이산확률변수 
 - <img src="https://latex.codecogs.com/gif.latex?%5Csum_%7Bx%7Dg%28x%29f%28x%29"/>
 - 연속확률변수
 - <img src="https://latex.codecogs.com/gif.latex?%5Cint%20g%28x%29f%28x%29dx"/>
 
 
### 기대값의 성질
 1. 임의의 상수 a에 대해, <img src="https://latex.codecogs.com/gif.latex?E%28a%29%3D%5Csum_%7Bx%7Daf%28x%29%3Da%5Csum_%7Bx%7Df%28x%29%3Da"/>
 2. <img src="https://latex.codecogs.com/gif.latex?E%28aX&plus;b%29%3DaE%28X%29&plus;b"/>
 3. <img src="https://latex.codecogs.com/gif.latex?E%28g_%7B1%7D%28X%29&plus;g_%7B2%7D%28X%29%29%3DE%28g_%7B1%7D%28X%29%29&plus;E%28g_%7B2%7D%28X%29%29"/>
 

### 모분산과 모표준편차
 - 모평균을 유도할 때와 같이 전체 표본이 n개 있고 서로 다른 값이 k개가 있어 이들 값을 <img src="https://latex.codecogs.com/gif.latex?x_%7B1%7D%2C%5Ccdots%20%2Cx_%7Bk%7D"/> 라고 가정했을 때, 표본분산은 아래와 같음

 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?s%5E2%3D%5Cfrac%7B1%7D%7Bn-1%7D%5Csum_%7Bi%3D1%7D%5E%7Bk%7Dn_%7Bi%7D%28x_%7Bi%7D-%5Cbar%7Bx%7D%29%5E2%3D%5Cfrac%7Bn%7D%7Bn-1%7D%5Csum_%7Bi%3D1%7D%5E%7Bk%7D%28x_%7Bi%7D-%5Cbar%7Bx%7D%29%5E2p_%7Bi%7D"/>

 - 통계적 확률의 관점에서 볼 때 n을 계속 크게 하면 표본분산은 모분산(population variance)이 됨
 - n을 계속 크게 하는 경우,
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?%5C%5Cp_%7Bi%7D%5Crightarrow%20f%28x_%7Bi%7D%29%2C%5C%5C%20%5Cbar%7Bx%7D%5Crightarrow%20%5Cmu%20%2C%20%5C%5Cn/%28n-1%29%5Crightarrow%201"/>
 
 - 위의 식을 활용하여 정리하면 아래와 같음
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?%5Csigma%20%5E2%3D%5Csum_%7Bi%3D1%7D%5E%7Bk%7D%28x-%5Cmu%20%29%5E2f%28x_%7Bi%7D%29"/>
 
 - 확률변수 X의 분산을 Var(X)로도 표시하는데 위에서 언급한 기댓값의 표시방법에 의해 아래와 같이 표현 가능
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?Var%28x%29%3D%5Csum_%7Bi%3D1%7D%5E%7Bk%7D%28x-%5Cmu%20%29%5E2f%28x_%7Bi%7D%29%3DE%28%28X-%5Cmu%29%5E2%29"/>
 
 - 즉 분산은 <img src="https://latex.codecogs.com/gif.latex?g%28X%29%3D%28X-%5Cmu%29%5E2"/>의 기대값으로 표현 가능
 - 모분산을 간이식으로 정리하면
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?%5C%5CE%28%28X-%5Cmu%29%5E2%29%5C%5C%20%3DE%28X%5E2%29-2%5Cmu%20E%28X%29&plus;%5Cmu%5E2%5C%5C%20%3DE%28X%5E2%29-2%5Cmu%5E2%20&plus;%20%5Cmu%5E2%5C%5C%20%3DE%28X%5E2%29-%5Cmu%5E2"/>
 
 - 표준편차는 <img src="https://latex.codecogs.com/gif.latex?SD%28X%29%3D%5Csigma%20%3D%5Csqrt%7B%5Csigma%20%5E2%7D"/>
 - (정리) 확률변수 X의 분산 -> 위는 이산확률변수, 아래는 연속확률변수
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?Var%28X%29%3D%5Csigma%20%5E2%3DE%28%28X-%5Cmu%29%5E2%29%3D%5Cleft%5C%7B%5Cbegin%7Bmatrix%7D%20%5Csum_%7Bx%7D%28x-%5Cmu%29%5E2%20f%28x%29%5C%5C%20%5Cint%20%28x-%5Cmu%29%5E2f%28x%29dx%20%5Cend%7Bmatrix%7D%5Cright."/>

 
### 기대값의 성질
4. <img src="https://latex.codecogs.com/gif.latex?Var%28aX&plus;b%29%3Da%5E2Var%28x%29"/>

 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?%5C%5CVar%28aX&plus;b%29%20%5C%5C%3DVar%28aX%29%20%5C%5C%3DE%28%28aX%29%5E2%29-E%28aX%29%5E2%20%5C%5C%3Da%5E2E%28X%5E2%29-a%5E2E%28X%29%5E2%20%5C%5C%3Da%5E2%28E%28X%5E2%29-E%28X%29%5E2%29%20%5C%5C%3Da%5E2Var%28X%29"/>
 
 - Var(aX+b) 가 Var(aX)인 이유 : 분산은 퍼짐의 정도 -> b는 위치를 이동시키는 개념(퍼지는 정도에 영향을 미치지 않음)

5. <img src="https://latex.codecogs.com/gif.latex?SD%28aX&plus;b%29%3D%7Ca%7CSD%28X%29"/>
 
  <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?SD%28aX&plus;b%29%3D%5Csqrt%7BVar%28aX&plus;b%29%7D%3D%5Csqrt%7Ba%5E2Var%28X%29%7D%3D%7Ca%7CSD%28X%29"/>
 
## 10. 이항분포와 관련된 분포들 (1)
 - 자료를 수집할 때 특정 변수 하나만 관심을 가질 수 있으나 여러 가지 변수의 자료를 얻고 이들 변수들 간에 어떤 관계가 있는지에 관심을 가질수도 있음
 - 이렇게 여러가지 확률변수를 순서열 <img src="https://latex.codecogs.com/gif.latex?%28X_%7B1%7D%2C%20X_%7B2%7D%2C%5Ccdots%20%2CX_%7Bn%7D%29"/>으로 표시한 것을 **확률벡터(random vector)** 라고 함
 
### 이변량 분포(bivariate distribution)
 - 두 확률변수의 결합분포
 
### 다변량 분포(p-dimensional multivariate distribution)
 - p-개의 확률변수로 이루어진 확률벡터의 결합분포
 
### 결합확률질량함수(joint probability mass function)
 - 두 이산확률변수 X와 Y에 대해, X=x 이고 Y=y 일 확률을 다음과 같은 함수 f(x,y) 로 정의하면,
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?f%28x%2Cy%29%3DP%28X%3Dx%2C%20Y%3Dy%29"/>
 
 - f(x,y)를 확률변수 X와 Y의 결합확률질량함수라고 함
 - 위에서 ,는 집합에서 ∩을 의미
 - 동전을 3번 던진 실험에서 앞면의 수 X와 앞면과 뒷면의 차이 Y를 확률변수로 할 때, 결합된 확률은 아래와 같음
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?%5C%5CP%28X%3D0%2C%20Y%3D3%29%3DP%28%5C%7BTTT%5C%7D%29%3D%5Cfrac%7B1%7D%7B8%7D%5C%5C%5C%5C%20P%28X%3D1%2C%20Y%3D1%29%3DP%28%5C%7BHTT%2CTHT%2CTTH%5C%7D%29%3D%5Cfrac%7B3%7D%7B8%7D%5C%5C%5C%5C%20P%28X%3D2%2C%20Y%3D1%29%3DP%28%5C%7BHHT%2CHTH%2CTHH%5C%7D%29%3D%5Cfrac%7B3%7D%7B8%7D%5C%5C%5C%5C%20P%28X%3D0%2C%20Y%3D3%29%3DP%28%5C%7BHHH%5C%7D%29%3D%5Cfrac%7B1%7D%7B8%7D"/>
 
 - 이를 결합확률질량함수로 표시하면
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?f%280%2C3%29%3D%5Cfrac%7B1%7D%7B8%7D%2Cf%281%2C1%29%3D%5Cfrac%7B3%7D%7B8%7D%2Cf%282%2C1%29%3D%5Cfrac%7B3%7D%7B8%7D%2Cf%283%2C3%29%3D%5Cfrac%7B1%7D%7B8%7D"/>


### 주변확률질량함수(marginal probability mass function)
 - 앞서 표본공간이 사건 <img src="https://latex.codecogs.com/gif.latex?B_%7B1%7D%2C%5Ccdots%20%2CB_%7Bn%7D"/> 로 분할될 때 사건 A의 확률은
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?P%28A%29%3D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28A%5Ccap%20B_%7Bi%7D%29"/>
 
 - 위와 같음. 만약 Y가 가질 수 있는 값이 <img src="https://latex.codecogs.com/gif.latex?y_%7B1%7D%2C%5Ccdots%20%2Cy_%7Bn%7D"/> 이라고 할 때, <img src="https://latex.codecogs.com/gif.latex?X%3Dx"/> 를 사건 <img src="https://latex.codecogs.com/gif.latex?A%2C%20Y%3Dy_%7Bi%7D"/> 를 사건 <img src="https://latex.codecogs.com/gif.latex?B_%7Bi%7D"/>라고 하면 <img src="https://latex.codecogs.com/gif.latex?P%28A%5Ccap%20B_%7Bi%7D%29%3DP%28X%3Dx%2C%20Y%3Dy_%7Bi%7D%29"/> 이고 다음과 같은 관계가 성립
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?P%28X%3Dx%29%3DP%28A%29%3D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28A%5Ccap%20B_%7Bi%7D%29%3D%5Csum_%7Bi%3D1%7D%5E%7Bn%7DP%28X%3Dx%2C%20Y%3Dy_%7Bi%7D%29"/>
 
 - 이것은 두 이산확률변수 X와 Y의 결합확률질량함수가 f(x,y)일 때, X의 확률질량함수는 다음과 같이 모든 y의 결합확률질량함수를 더해 구할 수 있음
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?f_%7BX%7D%28x%29%3D%5Csum_%7By%7Df%28x%2Cy%29"/>
 
 - 이 경우 <img src="https://latex.codecogs.com/gif.latex?f_%7BX%7D%28x%29"/>를 주변확률질량함수라고 함
 - Y의 주변확률질량함수는
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?f_%7BY%7D%28y%29%3D%5Csum_%7Bx%7Df%28x%2Cy%29"/>
 
### 두 확률변수 X,Y에 대해 X+Y 혹은 XY 의 기대값

 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?%5C%5CE%28X&plus;Y%29%3D%5Csum_%7Bx%7D%5Csum_%7By%7D%28x&plus;y%29f%28x%2Cy%29%5C%5C%20E%28XY%29%3D%5Csum_%7Bx%7D%5Csum_%7By%7Dxyf%28x%2Cy%29"/>
 
 - 두 확률변수의 합이나 차의 기댓값은 다음과 같이 각 확률변수의 기댓값의 합이나 차로 표시 가능
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?%5C%5CE%28X%5Cpm%20Y%29%3D%5Csum_%7Bx%7D%5Csum_%7By%7D%28x&plus;y%29f%28x%2Cy%29%20%5C%5C%5C%5C%3D%5Csum_%7Bx%7D%5Csum_%7By%7Dxf%28x%2Cy%29%5Cpm%5Csum_%7Bx%7D%5Csum_%7By%7Dyf%28x%2Cy%29%20%5C%5C%5C%5C%3D%5Csum_%7Bx%7Dx%5Csum_%7By%7Df%28x%2Cy%29%5Cpm%5Csum_%7By%7Dy%5Csum_%7Bx%7Df%28x%2Cy%29%20%5C%5C%5C%5C%3D%5Csum_%7Bx%7Dxf_%7BX%7D%28x%29%5Cpm%5Csum_%7Bx%7Dyf_%7BY%7D%28y%29%20%5C%5C%5C%5C%3DE%28X%29%5Cpm%20E%28Y%29"/>
 
 - 두 확률변수 X와 Y가 모든 x,y에 대하여 결합확률질량(밀도)함수가 주변확률질량(밀도)함수의 곱으로, 즉 <img src="https://latex.codecogs.com/gif.latex?f%28x%2Cy%29%3Df_%7BX%7D%28x%29f_%7BY%7D%28y%29"/> 로 표시할 수 있으면 이런 경우 **확률변수 X와 Y는 독립** 이라 함
 
 - 두 확률 변수가 독립인 경우 아래의 내용이 성립
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?%5C%5CE%28XY%29%3D%5Csum_%7Bx%7D%5Csum_%7By%7Dxyf%28x%2Cy%29%5C%5C%20%3D%20%5Csum_%7Bx%7D%5Csum_%7By%7Dxyf_%7BX%7D%28x%29f_%7BY%7D%28y%29%3D%5Csum_%7Bx%7Dxf_%7BX%7D%28x%29%5Csum_%7By%7Dyf_%7BY%7D%28y%29%3DE%28X%29E%28Y%29"/>
 
 
## 11. 이항분포와 관련된 분포들 (2)

### 공분산
 - 두 확률변수가 독립이 아니라면 서로 관련성이 있다는 것을 의미
 - 앞서 표본공분산은 아래와 같이 구함
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?%5C%5CC_%7Bxy%7D%3D%5Cfrac%7B1%7D%7Bn-1%7D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28x_%7Bi%7D-%5Cbar%7Bx%7D%29%28y_%7Bi%7D-%5Cbar%7By%7D%29%20%5C%5C%3D%5Cfrac%7Bn%7D%7Bn-1%7D%5Cfrac%7B1%7D%7Bn%7D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28x_%7Bi%7D-%5Cbar%7Bx%7D%29%28y_%7Bi%7D-%5Cbar%7By%7D%29"/>
 
 - n을 계속 크게 하는 경우를 가정하여, 
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?%5C%5C%5Cbar%7Bx%7D%5Crightarrow%20%5Cmu_%7BX%7D%20%5C%5C%5Cbar%7By%7D%5Crightarrow%20%5Cmu_%7BY%7D"/>
 
 - 두 확률변수 X와 Y의 공분산은 다음과 같이 표현
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?Cov%28X%2CY%29%3DE%28%28X-%5Cmu_%7BX%7D%29%28Y-%5Cmu_%7BY%7D%29%29%3D%5Csum_%7Bx%7D%5Csum_%7By%7D%28x-%5Cmu_%7BX%7D%29%28y-%5Cmu_%7BY%7D%29f%28x%2Cy%29"/>
 
 - 공분산을 계산할 때는 아래와 같이 간편계산식을 사용
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?%5C%5CCov%28X%2CY%29%3DE%28%28X-%5Cmu_%7BX%7D%29%28Y-%5Cmu_%7BY%7D%29%29%5C%5C%20%3DE%28XY-X%5Cmu_%7BY%7D-Y%5Cmu_%7BX%7D&plus;%5Cmu_%7BX%7D%5Cmu_%7BY%7D%29%5C%5C%20%3DE%28XY%29-%5Cmu_%7BY%7DE%28X%29-%5Cmu_%7BX%7DE%28Y%29&plus;%5Cmu_%7BX%7D%5Cmu_%7BY%7D%5C%5C%20%3DE%28XY%29-%5Cmu_%7BY%7D%5Cmu_%7BX%7D-%5Cmu_%7BX%7D%5Cmu_%7BY%7D&plus;%5Cmu_%7BX%7D%5Cmu_%7BY%7D%5C%5C%20%3DE%28XY%29-E%28X%29E%28Y%29"/>
 
 - 앞서 두 확률변수 X와 Y가 독립이면 E(XY) = E(X)E(Y)라는 것을 보임 -> X와 Y가 독립이면 공분산은 0
 - **공분산이 0이라고 해서 X와 Y가 독립은 아님**
 
### 분산
 - 확률변수의 합이나 차에 대한 분산
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?%5C%5CVar%28X&plus;Y%29%3DE%28%28X&plus;Y-%28%5Cmu_%7BX%7D&plus;%5Cmu_%7BY%7D%29%29%5E2%29%5C%5C%20%3DE%28%28%28X-%5Cmu_%7BX%7D%29&plus;%28Y-%5Cmu_%7BY%7D%29%29%5E2%29%5C%5C%20%3DE%28%28X-%5Cmu_%7BX%7D%29%5E2%29&plus;E%28%28Y-%5Cmu_%7BY%7D%29%5E2%29-2E%28%28X-%5Cmu_%7BX%7D%29%28Y-%5Cmu_%7BY%7D%29%29%5C%5C%20%3DVar%28X%29&plus;Var%28Y%29-2Cov%28X%2CY%29"/>
 
 - 만약 두 확률변수가 독립일 경우 공분산은 0이 되고, 아래 식이 성립
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?Var%28X%5Cpm%20Y%29%3DVar%28X%29&plus;Var%28Y%29"/>
 
## 12. 이항분포와 관련된 분포들 (3) 

### 베르누이(Bernoulli) 시행
```
1. 각 실험에서 발생 가능한 결과는 단 2가지
 ex) (성공, 실패) , (앞면, 뒷면)
2. 각 실험이 독립적으로 수행
3. 모든 실험에서 결과의 확률은 항상 동일
 P(S) = p, P(F) = 1-p = q
 ```

 - 위의 내용을 정리하면 **두 가지의 결과가 발생하는 실험을 독립적으로 시행하는데 매 시행에서 성공할 확률이 동일하면 이를 베르누이시행이라고 함**
 - 상자에 10개의 제품이 있는데 이 중 8개가 정상, 2개가 불량일 때, 정상품이 뽑히면 성공(S) 이라고 가정. 복원추출과 비복원추출로 각각 제품을 뽑았을 때, 2개 모두 정상품일 확률은
 - 복원추출 : <img src="https://latex.codecogs.com/gif.latex?P%28S_%7B1%7D%2CS_%7B2%7D%29%3DP%28S_%7B1%7D%29P%28S_%7B2%7D%7CS_%7B1%7D%29%3D%5Cfrac%7B8%7D%7B10%7D%5Ctimes%20%5Cfrac%7B8%7D%7B10%7D"/>
 - 비복원추출 : <img src="https://latex.codecogs.com/gif.latex?P%28S_%7B1%7D%2CS_%7B2%7D%29%3DP%28S_%7B1%7D%29P%28S_%7B2%7D%7CS_%7B1%7D%29%3D%5Cfrac%7B8%7D%7B10%7D%5Ctimes%20%5Cfrac%7B7%7D%7B9%7D"/>
 - 복원추출은 앞에 뽑힌 제품에 영향을 받지 않기 때문에 <img src="https://latex.codecogs.com/gif.latex?P%28S_%7B2%7D%7CS_%7B1%7D%29%3DP%28S_%7B2%7D%29"/> 가 되고, 정삼품이 뽑힐 확률이 항상 0.8이기 때문에 베르누이시행이라고 할 수 있음
 - 비복원추출은 두 번째 추출은 첫 번째 추출에 영향을 받기 때문에(독립이 아님) 베르누이시행이라고 할 수 없음
 - 만약 상자에 10000개의 제품이 있고 이중 8000개가 정상 2000개가 불량일 때 2개의 제품을 비복원추출 한다면,
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?P%28S_%7B1%7D%2CS_%7B2%7D%29%3DP%28S_%7B1%7D%29P%28S_%7B2%7D%7CS_%7B1%7D%29%3D%5Cfrac%7B8000%7D%7B10000%7D%5Ctimes%20%5Cfrac%7B7999%7D%7B9999%7D"/>
 
 - 위 결과는 엄밀히 따지면 베르누이시행이 아님. 하지만 상자에 10개의 제품이 있을 때와 다르게 <img src="https://latex.codecogs.com/gif.latex?P%28S_%7B2%7D%29%3D0.8%5Csimeq%207999/9999%3DP%28S_%7B2%7D%7CS_%7B1%7D%29"/> 인 것을 볼 수 있음
 - 이와 같이 **모집단의 크기가 매우 크고 이에 비해 표본의 크기가 상대적으로 작아 비복원추출의 결과와 복원추출의 결과가 차이가 거의 없는 경우 비복원추출도 베르누이시행을 근사모형으로 사용**하고 있음
 - 베르누이시행에서 만약 '성공' 확률을 p라고 하면, '실패' 확률은 1-p가 됨
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?P%28S%29%3Dp%2C%20P%28F%29%3D1-P%28S%29%3D1-p"/>
 
 - 실험결과가 실패이면 0, 성공이면 1의 값을 갖는 확률변수 X의 확률분포는
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?%5C%5CP%28X%3D1%29%3DP%28S%29%3Dp%5C%5C%20P%28X%3D0%29%3DP%28F%29%3D1-p"/>
 
 - 이러한 확률분포를 따르는 확률변수를 베르누이확률변수(Bernoulli random variable)라고 하고 베르누이분포(Bernoulli distribution)을 따른다고 함
 - 성공확률이 p인 베르누이 확률질량함수를 다음과 같이 쓸 수 있음
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?%5C%5Cf%28x%29%3Dp%5Ex%281-p%29%5E1%5E-%5Ex%2C%20%5C%5Cx%3D0%2C%201%2C%20%5C%5C0%3Cp%3C1"/>
 
 - 또한 베르누이분포의 기대값은 아래와 같음
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?%5C%5CE%28X%29%3D0%5Ctimes%20%281-p%29&plus;1%20%5Ctimes%20p%3Dp%5C%5C%5C%5C%20E%28X%5E2%29%3D0%5E2%5Ctimes%20%281-p%29&plus;1%5E2%20%5Ctimes%20p%3Dp%5C%5C%5C%5C%20Var%28X%29%3DE%28X%5E2%29-E%28X%29%5E2%3Dp-p%5E2%3Dp%281-p%29"/>
 
 - 확률 p가 0또는 1에 가까울수록 분산은 작아지며 p가 1/2일 때 분산은 1/4로 가장큰 값을 가짐-> p(1-p) 를 그래프로 그려서 생각해보자
 - 베르누이확률분포는 성공확률인 p에 의해 확률과 기대값이 결정
 - 이와 같이 분포의 특성을 결정하는 상수를 모수(parameter)라고 하며, '성공확률이 p인' 대신에 '모수가 p인' 베르누이분포라고도 함
 - X가 성공확률이 p인 베르누이확률분포를 따를 때 <img src="https://latex.codecogs.com/gif.latex?X%5Csim%20B%28p%29"/> 라고 표시

### 이항분포(binomial distribution)
 - 성공확률이 p인 베르누이시행을 n번 반복했을 때 성공 횟수의 분포
 - 확률변수 X는 n개의 베르누이 확률변수의 합으로, X의 기대값은 기대값은 베르누이확률변수의 기대값의 합으로 표시
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?E%28X%29%3DE%28X_%7B1%7D&plus;%5Ccdots%20&plus;X_%7Bn%7D%29%3DE%28X_%7B1%7D%29&plus;%5Ccdots&plus;%20E%28X_%7Bn%7D%29%3Dnp"/>
 
 - 베르누이확률변수는 서로 독립이기 때문에 X의 분산도 다음과 같이 각각의 베르누이 분산의 합으로 표시
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?Var%28X%29%3DVar%28X_%7B1%7D&plus;%5Ccdots%20&plus;X_%7Bn%7D%29%3DVar%28X_%7B1%7D%29&plus;%5Ccdots&plus;%20Var%28X_%7Bn%7D%29%3Dnp%281-p%29"/>
 
### 주사위 세 번 던지기
 - X : 1이 나온 횟수 ( 1이면 S, 아니면 F )

| 0 | 1 | 2 | 3 |
| - | - | - | - |
| FFF | SFF, FSF, FFS | SSF, SFS, FSS | SSS |
| <img src="https://latex.codecogs.com/gif.latex?%5Cbinom%7B3%7D%7B0%7D%5Cbinom%7B1%7D%7B6%7D%5E0%5Cbinom%7B3%7D%7B0%7D%5E3"/> | <img src="https://latex.codecogs.com/gif.latex?%5Cbinom%7B3%7D%7B1%7D%5Cbinom%7B1%7D%7B6%7D%5E1%5Cbinom%7B3%7D%7B0%7D%5E2"/> | <img src="https://latex.codecogs.com/gif.latex?%5Cbinom%7B3%7D%7B2%7D%5Cbinom%7B1%7D%7B6%7D%5E2%5Cbinom%7B3%7D%7B0%7D%5E1"/> | <img src="https://latex.codecogs.com/gif.latex?%5Cbinom%7B3%7D%7B3%7D%5Cbinom%7B1%7D%7B6%7D%5E3%5Cbinom%7B3%7D%7B0%7D%5E0"/> |

 - P(X=x)를 구하기 위해서는 해당되는 원소의 개수를 계산하여 위의 확률에 곱함
 - 실행횟수가 n인 상황으로 일반화했을 때 x개의 성공한 원소의 수는 n개 중 x개를 선택하는 조합으로
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?%5Cbinom%7Bn%7D%7Bx%7D%3D%5Cfrac%7Bn%21%7D%7Bx%21%28n-x%29%21%7D"/>
 
 - 각 원소의 확률은 x번 성공하고 n-x 번 실패하기 때문에
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?p%5Ex%281-p%29%5En%5E-%5Ex"/>

 - 따라서 성공확률이 p인 베르누이시행을 n번 반복했을 때 이항분포의 확률질량함수는 아래와 같음
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?f%28x%29%3D%5Cbinom%7Bn%7D%7Bx%7Dp%5Ex%281-p%29%5En%5E-%5Ex%2C%20x%3D0%2C1%2C%5Ccdots%20%2Cn"/>
 
 - 확률변수 X가 모수 n,p를 갖는 이항분포를 따른다는 것을 일반적으로 <img src="https://latex.codecogs.com/gif.latex?X%5Csim%20B%28n%2Cp%29"/> 로 표시
 - 베르누이확률변수의 경우 n이 1이므로 <img src="https://latex.codecogs.com/gif.latex?X%5Csim%20B%281%2Cp%29"/> 로 표시 가능
 
## 13. 이항분포와 관련된 분포들 (4)  

### 초기하분포(hypergeometric distribution)
 - 어떤 제품을 계속 만들어내는 생산공정에서 무작위로 제품을 선택하여 품질검사를 한다고 가정
 - 각 검사에서 불량률이 공정과정의 불량률 p와 같고 각각의 검사는 서로 독립이라고 한다면 이 검사는 베르누이시행
 - 그러나 N개의 제품이 있는 상자에서 n개를 비복원으로 추출하여 품질검사를 시행하는 경우는 모형이 다름
 - ex) 7개의 정상품과 3개의 불량품이 있는 상자에서 임의로 3개의 제품을 비복원추출한 경우에 3개중 1개가 불량품일 확률? 정상 : A, 불량 : D
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?%5C%5CP%28D%2CA%2CA%29&plus;P%28A%2CD%2CA%29&plus;P%28A%2CA%2CD%29%5C%5C%5C%5C%20%3D%5Cfrac%7B3%7D%7B10%7D%5Ctimes%5Cfrac%7B7%7D%7B9%7D%5Ctimes%5Cfrac%7B7%7D%7B9%7D&plus;%5Cfrac%7B7%7D%7B10%7D%5Ctimes%5Cfrac%7B3%7D%7B9%7D%5Ctimes%5Cfrac%7B6%7D%7B8%7D&plus;%5Cfrac%7B7%7D%7B10%7D%5Ctimes%5Cfrac%7B6%7D%7B9%7D%5Ctimes%5Cfrac%7B3%7D%7B8%7D%5C%5C%5C%5C%20%3D3%5Ctimes%5Cfrac%7B3%5Ctimes7%5Ctimes6%7D%7B10%5Ctimes9%5Ctimes8%7D%3D%5Cfrac%7B21%7D%7B40%7D"/>
 
 - 세 원소의 확률이 모두 동일, 앞에 있는 3은 3개의 위치 중 1개의 불량 위치를 선택하는 방법의 수
 - X를 불량품의 수라고 하면 위의 식은 아래와 같이 정리 가능
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?P%28X%3D1%29%3D%5Cbinom%7B3%7D%7B1%7D%5Cfrac%7B%5Cfrac%7B3%21%7D%7B%283-1%29%21%7D%5Cfrac%7B7%21%7D%7B%287-2%29%21%7D%7D%7B%5Cfrac%7B10%21%7D%7B%2810-3%29%21%7D%7D"/>
 
 - 이를 불량품이 M개, 정상품이 N-M개가 들어있는 상자에서 n개를 비복원으로 추출했을 때 n개 중 불량품의 개수에 대한 분포로 일반화 가능
 - n개 중 불량품의 개수를 X라고 하면 X의 확률분포는 아래와 같이 구할 수 있음
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?%5C%5CP%28X%3Dx%29%3D%5Cbinom%7Bn%7D%7Bx%7D%5Cfrac%7B%5Cfrac%7BM%21%7D%7B%28M-x%29%21%7D%5Cfrac%7B%28N-M%29%21%7D%7B%28N-M-n&plus;x%29%21%7D%7D%7B%5Cfrac%7BN%21%7D%7B%28N-n%29%21%7D%7D%5C%5C%5C%5C%20%3D%5Cfrac%7B%5Cfrac%7BM%21%7D%7Bx%21%28M-x%29%21%7D%5Cfrac%7B%28N-M%29%21%7D%7B%28n-x%29%21%28N-M-n&plus;x%29%21%7D%7D%7B%5Cfrac%7BN%21%7D%7Bn%21%28N-n%29%21%7D%7D%5C%5C%5C%5C%20%3D%5Cfrac%7B%5Cbinom%7BM%7D%7Bx%7D%5Cbinom%7BN-M%7D%7Bn-x%7D%7D%7B%5Cbinom%7BN%7D%7Bn%7D%7D"/>
 
 - 위와 같은 확률질량함수를 가지는 분포를 **초기하분포** 라고 함
 - 보통의 경우 X가 가질 수 있는 값은 {0,1,2,...,n} 로 표시할 수 있으나  n이 불량품의 수 M보다 클 수 없기 때문에 X의 최대값은 n과 M 중 작은 값인 min(n, M)가 됨
 - 또한 n이 정상품의 수 N-M보다 크면 최소한 n-N+M개의 불량품이 반드시 선택되기 때문에 X의 최소값은 max(0, n-N+M)가 됨
 - 위의 내용을 다시 정리하면 확률변수 X의 확률질량 함수는 아래와 같음
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?f%28x%29%3D%5Cfrac%7B%5Cbinom%7BM%7D%7Bx%7D%5Cbinom%7BN-M%7D%7Bn-x%7D%7D%7B%5Cbinom%7BN%7D%7Bn%7D%7D%2C%20x%3Dmax%280%2Cn-N&plus;M%29%2C%5Ccdots%20%2Cmin%28n%2CM%29"/>
 
 - 확률질량함수가 위의 모양일 때, X는 모수가 (M,M,n)인 초기하분포를 따른다고 하고 X~H(N,M,n) 으로 표시
 - 모집단의 크기가 매우 크고 이에 비해 표본의 크기가 상대적으로 작은 경우, 비복원추출의 경우에도 베르누이시행으로 봐도 큰 문제가 없다고 하기도 함
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?P%28X%3D1%29%3D%5Cbinom%7B3%7D%7B1%7D%5Cfrac%7B3000%5Ctimes7000%5Ctimes6999%7D%7B10000%5Ctimes9999%5Ctimes9998%7D%5Capprox%20%5Cbinom%7B3%7D%7B1%7D%5Cfrac%7B3%7D%7B10%7D%28%5Cfrac%7B7%7D%7B10%7D%29%5E2"/>
 
 - 초기하분포에서 평균과 분산은 정의를 이용하여 직접 구할 수 있으나 계산 과정이 복잡 ( 이항분포의 평균과 분산을 계산할 때처럼 각 실험의 결과의 합으로 생각하여 유도 )
 
 - 확률변수 <img src="https://latex.codecogs.com/gif.latex?X_%7Bi%7D"/> 는 i번째 추출에서 불량품이면 1, 아니면 0의 값을 가진다고 하면 초기하확률변수 X는 아래와 같이 쓸 수 있음
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?X%3DX_%7B1%7D&plus;%5Ccdots%20&plus;X_%7Bn%7D"/>

 - 위에서 X가 이항확률변수와 다른 점은 <img src="https://latex.codecogs.com/gif.latex?X_%7Bi%7D"/> 들이 서로 독립이 아님
 - 하지만 모든 <img src="https://latex.codecogs.com/gif.latex?i%3D1%2C%5Ccdots%20%2Cn"/> 에 대해, <img src="https://latex.codecogs.com/gif.latex?X_%7Bi%7D"/> 의 확률분포는
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?P%28X_%7Bi%7D%3D0%29%3D%5Cfrac%7BN-M%7D%7BN%7D%2C%20P%28X_%7Bi%7D%3D1%29%3D%5Cfrac%7BM%7D%7BN%7D"/>
 
 - <img src="https://latex.codecogs.com/gif.latex?p%3DM/N"/> 이라고 하면 <img src="https://latex.codecogs.com/gif.latex?E%28X_%7Bi%7D%29%3DM/N%3Dp%2CVar%28X_%7Bi%7D%29%3Dp%281-p%29"/> 이 성립하고 X의 평균은 다음과 같이 계산
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?E%28X%29%3DE%28X_%7B1%7D&plus;%5Ccdots%20&plus;X_%7Bn%7D%29%3DE%28X_%7B1%7D%29&plus;%5Ccdots%20E%28X_%7Bn%7D%29%3Dn%5Cfrac%7BM%7D%7BN%7D%3Dnp"/>
 
 - 확률변수 <img src="https://latex.codecogs.com/gif.latex?X_%7Bi%7D%2CX_%7Bj%7D"/>는 독립이 아니기 때문에
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?%5C%5CVar%28X%29%3D%5Csum_%7Bi%3D1%7D%5E%7Bn%7DVar%28X_%7Bi%7D%29&plus;2%5Csum_%7Bi%3Cj%7DCov%28X_%7Bi%7D%2CX_%7Bj%7D%29%5C%5C%5C%5C%20Var%28X%29%3Dn%5Cfrac%7BM%7D%7BN%7D%5Cfrac%7BN-M%7D%7BN%7D%5Cfrac%7BN-n%7D%7BN-1%7D%3Dnp%281-p%29%5Cfrac%7BN-n%7D%7BN-1%7D"/>


### 포아송분포(Poisson distribution)
 - 어느 생명보험회사의 조사 결과, 유전이나 전염되지 않는 어떤 희귀병으로 인해 일 년 동안 인구 10만명당 1명꼴로 사망한다고 가정
 - 이 보험회사에서는 가입된 15만명 가운데 이 희귀병으로 일 년 동안에 3명 이상 사망할 확률을 구하려 함
 - **유전이나 전염되지 않는다는 것은 발병이 독립적이라는 것을 유추**
 - 발병에 의한 사망확률은 0.00001로 이 희귀병에 의한 사망자수는 이항분포를 따른다고 볼 수 있음
 - 즉, 15만명 가운데 일 년 동안 이 병으로 인해 사망한 사람의 수를 X라고 하면
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?X%5Csim%20B%28150000%2C0.00001%29"/>
 
 - 이고 3명 이상 사망할 확률은
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?P%28X%5Cgeq%203%29%3D1-P%28X%5Cleq%202%29%3D1-%5Csum_%7Bx%3D0%7D%5E%7B2%7D%5Cbinom%7B150000%7D%7Bx%7D0.00001%5Ex0.99999%5En%5E-%5Ex"/>
 
 - 문제는 x가 어느 정도 큰 값에 대해 <img src="https://latex.codecogs.com/gif.latex?%5Cbinom%7B150000%7D%7Bx%7D"/>의 계산이 어렵고 <img src="https://latex.codecogs.com/gif.latex?0.00001%5Ex"/>은 거의 0이 되어 정밀한 프로그램을 사용하지 않는 이상 실제로 확률 계산이 어려움
 - 이 예제와 같이 시행횟수 n이 이 크고 성공확률 p가 작은 상황에서 이항분포의 근삿값을 구할 때 사용할 수 있는 것이 **포아송분포**
 - 이항분포 B(n,p)에서 평균을 <img src="https://latex.codecogs.com/gif.latex?%5Clambda"/>라고 하면, <img src="https://latex.codecogs.com/gif.latex?%5Clambda%3Dnp"/> 가 되는데 이항분포의 확률질량함수에서 <img src="https://latex.codecogs.com/gif.latex?p%3D%5Cfrac%7B%5Clambda%7D%7Bn%7D"/> 로 대채하면 다음과 같은 식을 유도 가능
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?%5C%5Cf%28x%29%3D%5Cbinom%7Bn%7D%7Bx%7Dp%5E%7Bx%7D%281-p%29%5E%7Bn-x%7D%5C%5C%5C%5C%20%3D%20%5Cfrac%7Bn%28n-1%29%5Ccdots%20%28n-x&plus;1%29%7D%7Bx%21%7D%5Cleft%20%28%20%5Cfrac%7B%5Clambda%7D%7Bn%7D%20%5Cright%20%29%5E%7Bx%7D%5Cleft%20%28%201-%20%5Cfrac%7B%5Clambda%7D%7Bn%7D%20%5Cright%20%29%5E%7Bn-x%7D%5C%5C%5C%5C%20%3D%5Cfrac%7Bn%28n-1%29%5Ccdots%20%28n-x&plus;1%29%7D%7Bnn%5Ccdots%20n%7D%5Cfrac%7B%5Clambda%5E%7Bx%7D%7D%7Bx%21%7D%5Cleft%20%28%201-%20%5Cfrac%7B%5Clambda%7D%7Bn%7D%20%5Cright%20%29%5E%7Bn-x%7D"/>

 - 위 마지막 식에서 n이 계속 커지면, 
 
 <p align="center"> 
 <img src="https://latex.codecogs.com/gif.latex?%5C%5C%5Cfrac%7Bn%28n-1%29%5Ccdots%20%28n-x&plus;1%29%7D%7Bnn%5Ccdots%20n%7D%5Crightarrow%201%20%5C%5C%5C%5C%5Cfrac%7B%5Clambda%5E%7Bx%7D%7D%7Bx%21%7D%5Crightarrow%20e%5E%7B-%5Clambda%7D%20%5C%5C%5C%5C%5Cleft%20%28%201-%20%5Cfrac%7B%5Clambda%7D%7Bn%7D%20%5Cright%20%29%5E%7Bn-x%7D%5Crightarrow%201"/>
 
 - 아래와 같은 결과를 얻을 수 있음
 
  <p align="center">
  <img src="https://latex.codecogs.com/gif.latex?f%28x%29%3D%5Cbinom%7Bn%7D%7Bx%7Dp%5E%7Bx%7D%281-p%29%5E%7Bn-x%7D%5Csimeq%20%5Cfrac%7B%5Clambda%5Exe%5E%7B-%5Clambda%7D%7D%7Bx%21%7D"/>
 
 - 일반적으로 **단위시간이나 단위공간에서 발생가능성이 희박한 사건의 발생한 횟수에 대한 모형으로 포아송분포를 많이 사용**
 - 확률변수 X의 확률질량함수가
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?f%28x%29%3D%5Cfrac%7Be%5E%7B-%5Clambda%7D%5Clambda%5E%7Bx%7D%7D%7Bx%21%7D%2Cx%3D0%2C1%2C2%2C%5Ccdots"/>
 
 - 로 주어질 때, X는 모수 또는 평균이 <img src="https://latex.codecogs.com/gif.latex?%5Clambda"/>인 포아송분포를 따른다고 하고 <img src="https://latex.codecogs.com/gif.latex?X%5Csim%20P%28%5Clambda%29"> 라고 표시
 - 포아송분포는 평균과 분산이 같음
 
 
## 14. 정규분포와 기타 연속형분포 (1)

### 정규분포(normal distribution)의 성질
 - 이항분포가 대표적인 이산확률분포라고 하면 정규분포는 대표적인 연속확률분포
 - 정규분포는 Gauss가 각종 물리실험을 수행할 때 발생하는 측정오차를 설명하기 위해 적용한 분포
 - 모든 학문 분야에서 확률모형 또는 근사모형으로 활용
 - 평균은 중심위치를 종모양의 대칭형태를 가짐
 - 평균이 <img src="https://latex.codecogs.com/gif.latex?%5Cmu"/> 이고, 분산이 <img src="https://latex.codecogs.com/gif.latex?%5Csigma%5E2"/> 인 정규분포의 확률밀도함수
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?f%28x%29%3D%5Cfrac%7B1%7D%7B%5Csigma%5Csqrt%7B2%5Cpi%7D%7De%5E%7B-%5Cfrac%7B%28x-%5Cmu%29%5E2%7D%7B2%5Csigma%5E2%7D%7D"/>
 
 - <img src="https://latex.codecogs.com/gif.latex?%5Cmu"/> : 분포의 중심 ( 아래 표 참고 )
 - <img src="https://latex.codecogs.com/gif.latex?%5Csigma%5E2"/> : 퍼짐의 정도 ( 아래 표 참고 )
 - 표시 : <img src="https://latex.codecogs.com/gif.latex?X%5Csim%20N%28%5Cmu%2C%5Csigma%5E2%29"/>
 
 <p align="center">
 <img height="320" src="https://upload.wikimedia.org/wikipedia/commons/7/74/Normal_Distribution_PDF.svg"/>
 
 - X가 평균이 <img src="https://latex.codecogs.com/gif.latex?%5Cmu"/> 이고 분산이 <img src="https://latex.codecogs.com/gif.latex?%5Csigma%5E2"/> 인 정규분포를 따를 때, X가 임의의 구간 [a,b] 에 있을 확률은
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?P%28a%5Cleq%20X%20%5Cleq%20b%29%3D%5Cint_%7Ba%7D%5E%7Bb%7Df%28x%29dx%3D%5Cint_%7Ba%7D%5E%7Bb%7D%5Cfrac%7B1%7D%7B%5Csigma%5Csqrt%7B2%5Cpi%7D%7De%5E%7B-%5Cfrac%7B%28x-%5Cmu%29%5E2%7D%7B2%5Csigma%7D%7Ddx"/>
 
 - 위와 같음. 하지만 이 적분식은 직접 계산할 수 없으며 수치해석학으로 근사값을 구해야함
 - 정규분포표를 이용할 때 문제는 다양한 <img src="https://latex.codecogs.com/gif.latex?%5Cmu"/> 와 <img src="https://latex.codecogs.com/gif.latex?%5Csigma%5E2"/> 에 대해 모든 표를 제공하기 어려움
 - 따라서 통계학에서는 **특별한 정규분포에 대한 확률표 하나만 제공** 하고 다른 경우에는 표준화를 통해 확률을 구할 수 있도록 함


### 표준정규분포(standard normal distribution)
 - 평균이 0이고, 분산이 1인 정규분포 N(0,1)
 - 일반적으로 표준정규분포를 따르는 확률변수를 Z로 표시
 - 표준정규분포는 0을 중심으로 대칭이기 때문에
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?P%28Z%5Cleq%200%29%3DP%28Z%5Cgeq%200%29%3D0.5"/>
 
 - 0을 제외한 수 z에 대한 <img src="https://latex.codecogs.com/gif.latex?P%28Z%5Cleq%20z%29%2CP%28Z%5Cgeq%20z%29"/> 등은 표준정규분포표를 이용하여 계산해야 함 (https://en.wikipedia.org/wiki/Standard_normal_table)
 - 통계학에서 중요한 z
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?%5C%5CP%28Z%5Cleq%20-1.645%29%3DP%28Z%5Cgeq%201.645%29%3D0.05%5C%5C%5C%5C%20P%28Z%5Cleq%201.645%29%3DP%28Z%5Cgeq%20-1.645%29%3D0.95%5C%5C%5C%5C%20P%28Z%5Cleq%20-1.96%29%3DP%28Z%5Cgeq%201.96%29%3D0.025%5C%5C%5C%5C%20P%28Z%5Cleq%201.96%29%3DP%28Z%5Cgeq%20-1.96%29%3D0.975"/>
 
 
 
