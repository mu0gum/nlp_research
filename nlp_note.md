# 자연어 처리 관련 알고리즘 +@(수학  정리)
- 챗봇을 개발하는데 필요한 자연어 처리 관련 기술들에 대한 내용을 정리하고, 더해서 수학적인 내용도 정리해 보려고 합니다. 기본적으로는 챗봇에서 적용
하려고 하는 부분에 대해서 정리하겠습니다.
- 개인 공부 및 기록 용도이기 대문에 알고리즘이나 개념, 수학적인 내용은 제가 이해하는 수준에서만 기술하고 실제로 챗봇에 적용하는 부분에 대해서 이야기 하겠습니다.


## 00. 나이브 베이즈 분류
### 참고
1. 가장 쉽게 이해하는 베이즈 정리(Bayes' Law) (https://junpyopark.github.io/bayes/)
2. 나이브 베이즈 분류기 (https://ratsgo.github.io/machine%20learning/2017/05/18/naive/)

- 나이브 베이즈 분류는 제가 만든 챗봇이 무언가를 제안했을 때, 그에 대한 응답이 긍정이나 부정이냐를 분류하기 위해 적용한 내용입니다.
- 나이브 베이즈 분류는 스팸 메일을 필터링 하는데 좋은 효율을 보인다고 합니다. 스팸 메일을 필터는 메일 내용을 보고 스팸이냐 아니냐를 구분하는 것인데
이것을 응용하여, 사용자의 대답이 긍정이냐, 부정이냐를 분류해 보겠습니다.

### 조건부 확률
조건부 확률은 어떤 사건 B가 발생했을 때, 사건 A가 발생할 확률을 의미합니다. ( <img src="https://latex.codecogs.com/gif.latex?P%28B%29%20%3E%200" /> 으로 가정 )


<p align="center">
<img src="https://latex.codecogs.com/gif.latex?P%28A%7CB%29%3D%5Cfrac%7BP%28A%5Ccap%20B%29%7D%7BP%28B%29%7D" />

마찬가지로, 사건 A가 발생했을 때, 사건 B가 발생할 확률은 ( <img src="https://latex.codecogs.com/gif.latex?P%28A%29%20%3E%200" /> 으로 가정 )


<p align="center">
<img src="https://latex.codecogs.com/gif.latex?P%28B%7CA%29%3D%5Cfrac%7BP%28B%5Ccap%20A%29%7D%7BP%28A%29%7D" />


이고, 두 식을 정리해서 아래와 같이 표현할 수 있습니다.


<p align="center">
<img src="https://latex.codecogs.com/gif.latex?P%28A%5Ccap%20B%29%3DP%28A%7CB%29P%28B%29%3DP%28B%7CA%29P%28A%29" />


위의 식을 가지고, 사건 B가 발생했을 때 사건 A가 발생할 확률에 대해 정리해보면


<p align="center">
<img src="https://latex.codecogs.com/gif.latex?P%28A%7CB%29%3D%5Cfrac%7BP%28B%7CA%29P%28A%29%7D%7BP%28B%29%7D" />


라는 식이 나오게 되고, 위의 식을 일반적으로 **베이즈 정리**라고 합니다. 위의 내용은 참고1 에서 공부한 부분으로, 자세한 정리는 참고1 을 확인 하시면 좋을 것 같습니다.


그럼 저의 목표인 문장이 긍정이냐 부정이냐를 분류하는 것과 베이즈 정리가 어떤 관련이 있을까요?
위의 식에서의 핵심은 **A가 발생했을 때, B가 발생할 확률을 거꾸로 B가 발생했을 때, A가 발생할 확률을 사용해 계산할 수 있다**는 점입니다.
제가 구하고 싶은 답은 문장 S가 주어졌을 때, 그 문장이 긍정일 확률 <img src="https://latex.codecogs.com/gif.latex?P%28p%7CS%29" /> 와 
문장 S가 주어졌을 때, 그 문장이 부정일 확률 <img src="https://latex.codecogs.com/gif.latex?P%28n%7CS%29" /> 을 비교하여 더 큰 쪽을 찾는 것 입니다. ( 아래의 내용은 참고2 의 내용을 학습하고 정리하였습니다. 자세한 내용은 참고2를 확인하시면 좋을 것 같습니다. )


언뜻 생각해보면 문장이 주어졌을 때, 이 문장이 긍정일 확률을 구하라고 하면 굉장히 막연하게 느껴집니다. 하지만 위의 식을 베이즈 정리를 이용해서 표현해보면 아래와 같습니다.


<p align="center">
<img src="https://latex.codecogs.com/gif.latex?P%28p%7CS%29%3D%5Cfrac%7BP%28S%7Cp%29P%28p%29%7D%7BP%28S%29%7D" />


위 식에서 <img src="https://latex.codecogs.com/gif.latex?P%28p%29" /> 는 긍정인 문장의 개수를 전체 문장의 개수로 나눈 값입니다. <img src="https://latex.codecogs.com/gif.latex?P%28S%7Cp%29" /> 는 우도(likehood) 입니다. 앞서 설명한대로 베이즈 모델은 <img src="https://latex.codecogs.com/gif.latex?P%28p%7CS%29P%28p%29/P%28S%29" /> 와 <img src="https://latex.codecogs.com/gif.latex?P%28n%7CS%29P%28n%29/P%28S%29" /> 를 비교해 큰 쪽으로 범주를 할당합니다. <img src="https://latex.codecogs.com/gif.latex?P%28S%29" /> 는 공통이기 때문에 계산을 생략할 수 있습니다. 생략한 식은 아래와 같습니다. ( 참고로 ∝ 는 proportionality sign 이라고 부르고, A ∝ B 는 'A는 B에 비례한다' 는 뜻입니다. )


<p align="center">
<img src="https://latex.codecogs.com/gif.latex?P%28p%7CS%29%20%5Cpropto%20P%28S%7Cp%29P%28p%29" />


위의 식에서 문장 S가 단어 w1, w2 로 이루어졌다고 생각하고 식을 정리해보면


<p align="center">
<img src="https://latex.codecogs.com/gif.latex?P%28p%7CS%29%5Cpropto%20P%28w_1%2Cw_2%7Cp%29P%28p%29" />


위의 식이 됩니다. 나이브 베이즈 분류는 각 단어가 **독립(independent)** 임을 가정합니다. 그리고 naive(순진한) 라는 말이 이유가 붙은 이유기도 합니다. (참고2) 독립임을 가정 <img src="https://latex.codecogs.com/gif.latex?P%28w_1%2Cw_2%29%3DP%28w_1%29%5Ccdot%20P%28w_2%29" /> 하고 다시 식을 정리해보면


<p align="center">
<img src="https://latex.codecogs.com/gif.latex?P%28p%7CS%29%5Cpropto%20P%28w_1%7Cp%29%5Ccdot%20P%28w_2%7Cp%29%5Ccdot%20P%28p%29" />


위의 식이 나오게 됩니다. 지금까지 정리한 내용을 보다보면 단어의 순서에 대한 내용은 고려가 되어있지 않습니다. Bag-of-Words 와 같은 접근을 취하고 있습니다. 이에 대한 내용은 참고2 에 방문하셔서 한 번 읽어보시면 좋을 것 같습니다. ( **이 블로그는 자연어처리에 관련된 내용이 잘 정리가 되어 있어서 공부하는데 도움을 많이 받고 있습니다. 잘 모르시는 분이 계신다면 꼭 한 번 방문해보세요!** )


나이브 베이즈 분류에 대한 내용을 가지고 열심히 식을 정리해 보았습니다. 그럼 위의 식을 가지고 우리가 원하는 문장이 주어졌을 때, 긍정일 확률을 구할 수 있는지 확인해 보겠습니다.


저는 챗봇 테스트를 요청 하면서 챗봇이 무언가를 권유했을 때 사용자의 응답 데이터를 가지고 있고, 데이터는 아래와 같습니다.

```
'ㅌㅅㅌ', '아니ㅋㅋ', 'ㅇㅇ', '아니 빠잉', '아니', '응ㅋㅋ도와줄래?', '네', '그래', '네', 'ㅇㅇ', '응', '네', 'ㅇㅇ', '응', '엄마', '응', '도와줘', '응', 'ㅇㅇ', '응', '응', 'ㅇㅇ', '응', 'ㅇ', 'ㅋㅋㅋㅋㅋㅋ응', '응', '응', '응', '응ㅋㅋ' ...
```

수집한 데이터에 label을 붙이고 단어(w)로 토크나이징 해보겠습니다.

| 긍정 or 부정 | 문장 |
| -- | -- |
| n | ㅌㅅㅌ |
| n | 아니, ㅋㅋ |
| p | ㅇㅇ |
| p | 아니, 빠잉|
| p | 응, ㅋㅋ, 도와줄래 |
| p | 네 |


설명을 위해 일부분만 표시하였습니다. 앞서 정리한 식과 위의 표를 가지고 사용자의 응답


"응ㅋㅋ"


에 대한 긍정, 부정 분류를 해보겠습니다. 문장 S "응ㅋㅋ"를 토크나이징 하여 w1 = 응, w2 = ㅋㅋ 을 얻었습니다.


<p align="center">
<img src="https://latex.codecogs.com/gif.latex?P%28p%7CS%29%5Cpropto%20P%28w_1%7Cp%29%5Ccdot%20P%28w_2%7Cp%29%5Ccdot%20P%28p%29" />


일단 문장이 긍정일 확률은 전체 6개의 문장 중에서 4개가 긍정이므로, <img src="https://latex.codecogs.com/gif.latex?P%28p%29%3D%5Cfrac%7B4%7D%7B6%7D%3D%5Cfrac%7B2%7D%7B3%7D" /> 입니다. 

그리고 긍정인 문장에서 w1 = 응 이라는 단어가 있을 확률은 <img src="https://latex.codecogs.com/gif.latex?P%28w_1%7Cp%29%3D%5Cfrac%7B1%7D%7B7%7D" /> , 긍정인 문장에서 w2 = ㅋㅋ 라는 단어가 있을 확률도 <img src="https://latex.codecogs.com/gif.latex?P%28w_2%7Cp%29%3D%5Cfrac%7B1%7D%7B7%7D" /> 입니다. 이제 구한 확률을 가지고 위의 식에 대입해 보면


<p align="center">
<img src="https://latex.codecogs.com/gif.latex?P%28p%7CS%29%5Cpropto%20%5Cfrac%7B1%7D%7B7%7D%5Ccdot%20%5Cfrac%7B1%7D%7B7%7D%5Ccdot%20%5Cfrac%7B2%7D%7B3%7D%20%3D%20%5Cfrac%7B2%7D%7B147%7D" />


위의 결과가 나옵니다. "응ㅋㅋ"라는 문장이 긍정일 확률은 2/147 입니다. 같은 방법으로 "응ㅋㅋ"라는 문장이 부정일 확률을 구해보겠습니다.


<p align="center">
<img src="https://latex.codecogs.com/gif.latex?P%28n%29%3D%5Cfrac%7B2%7D%7B6%7D%3D%5Cfrac%7B1%7D%7B3%7D%2C%20p%28w_1%7Cn%29%3D%5Cfrac%7B0%7D%7B3%7D%2C%20P%28w_2%7Cn%29%3D%5Cfrac%7B1%7D%7B3%7D" />


<p align="center">
<img src="https://latex.codecogs.com/gif.latex?P%28n%7CS%29%3D%5Cfrac%7B1%7D%7B3%7D%5Ccdot%20%5Cfrac%7B0%7D%7B3%7D%5Ccdot%20%5Cfrac%7B1%7D%7B3%7D%3D0" />


문장 S가 주어졌을 때, 긍정일 확률과 부정일 확률을 나이브 베이즈 정리를 이용해 구했습니다. 


<p align="center">
<img src="https://latex.codecogs.com/gif.latex?P%28p%7CS%29%3D%5Cfrac%7B2%7D%7B147%7D%2C%20p%28n%7CS%29%3D0" />


문장이 긍정일 확률이 더 크네요. "응ㅋㅋ"는 긍정으로 분류 되었습니다. 분류가 잘 된 것 같지만 몇 가지 문제가 존재합니다.


1. 단어 "응" 이 부정일 확률 <img src="https://latex.codecogs.com/gif.latex?p%28w_1%7Cn%29%20%3D%20%5Cfrac%7B0%7D%7B3%7D%20%3D%200" /> 이
0 되어서 결과를 무조건 0 으로 만들어 버립니다.


-> 이 경우에는 적절히 작은 수 k 를 더해서 분자가 0 이 되는 것을 피하게(smoothing) 합니다. k = 1 이라고 하고 다시 계산해 보면
 
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?p%28p%7CS%29%3D%5Cfrac%7B1&plus;k%7D%7B7%7D%5Ccdot%20%5Cfrac%7B1&plus;k%7D%7B7%7D%5Ccdot%20%5Cfrac%7B2%7D%7B3%7D%3D%5Cfrac%7B6%7D%7B147%7D%28%5Cbecause%20k%3D1%29" />
 
 
 <p align="center">
<img src="https://latex.codecogs.com/gif.latex?p%28n%7CS%29%3D%5Cfrac%7B1&plus;k%7D%7B3%7D%5Ccdot%20%5Cfrac%7B0&plus;k%7D%7B3%7D%5Ccdot%20%5Cfrac%7B1%7D%7B3%7D%3D%5Cfrac%7B2%7D%7B27%7D%28%5Cbecause%20k%3D1%29" />


위의 결과가 나오게 됩니다.


2. 두번째 문제는 위의 결과에서 확인할 수 있습니다. "응ㅋㅋ" 에서 응, ㅋㅋ는 모두 긍정 단어에 존재하고, 부정 단어에는 ㅋㅋ만 존재합니다. 그런데, 위의 표에서 긍정 단어의 수는 7개 이고, 부정 단어의 수는 3개 입니다. 긍정 단어의 수와 부정 단어의 수가 약 2배 차이가 나고, 수집한 데이터의 양이 충분하지 않아 "응" 이라는 전체 긍정 단어에서 1번 밖에 등장하지 않는 것으로 계산되어 오히려 "응ㅋㅋ"가 부정으로 분류되었습니다. ( 수집한 데이터의 양이 많을 경우 "응" 이라는 단어가 긍정 전체 단어에서 등장할 확률은 더 높을 것으로 생각됩니다. )



제가 공부한 사이트에서의 예제는 영화의 리뷰와 평점 데이터를 가지고 긍정/부정을 분류하였습니다. 리뷰는 제 챗봇이 입력받는 대답에 비해 더 많은 단어를 가지고 있고, 사전에 정리된 데이터의 양도 많아 충분히 훌륭히 분류를 하고 있습니다. 하지만 제가 만드는 챗봇에서 바로 사용하기에는 무리가 있어 보입니다. 


현재 만들고 있는 챗봇에 적용할 수 있도록 개선하면, 참고 코드는 그 때 올리도록 하겠습니다. 나이브 베이즈 정리에 대한 내용은 일단 이정도로 마치겠습니다. 


## 01. CNN을 활용한 의도 분석
### 출처 및 참고
1. 딥러닝 - 초보자를 위한 컨볼루셔널 네트워크를 이용한 이미지 인식의 이해 (https://bcho.tistory.com/1149)
2. CNN, Convolutional Neural Network 요약 (http://taewan.kim/post/cnn/)
3. CNN으로 문장 분류하기 (https://ratsgo.github.io/natural%20language%20processing/2017/03/19/CNN/)
4. Day-by-day Line-by-line Keras-based Korean NLP (https://github.com/warnikchow/dlk2nlp)
5. 밑바닥부터 시작하는 딥러닝 : 파이썬으로 익히는 딥러닝 이론과 구현

- CNN을 활용한 의도 분석은 챗봇이 사용자가 원하는 요구사항에 대응하기 위해 공부하고 적용한 내용입니다.
- 밑바닥부터 시작하는 딥러닝의 내용 위주로 정리하였습니다.
- 학습을 위한 데이터와 소스코드는 출처 및 참고 4를 참고 하였습니다. ( 참고4에는 의도분류라는 목적을 실행하기 위해 단계별로 진행하는 과정이 설명되어 있습니다. 꼭 한 번 방문에 보시기를 추천 드립니다.)

### 합성곱 신경망(convolutional neural network)
- CNN은 이미지 인식과 음성 인식 등 다양한 곳에 사용되는 신경망입니다. CNN은 전통적인 뉴럴 네트워크 앞에 여러 계층에 합성곱 계층(convolutional layer)과 풀링 계층(pooling layer)을 붙인 모양이 됩니다. 기존의 신경망은 인접하는 계층의 모든 뉴런과 결합되어 있었습니다. 이를 완전연결(fully-connected)이라고 합니다. 


<p align="center">
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=http%3A%2F%2Fcfile2.uf.tistory.com%2Fimage%2F2409463658F46CAD1FBCD4"/>


- 위에 그림에서 보시다시피 CNN의 계층은 Conv-ReLU-(Pooling) 흐름으로 연결됩니다. (pooling 은 생략하기도 합니다.) CNN에서 주목할 또 다른 점은 출력에 가까운 층에서는 기존의 'Affine-ReLU' 구성을 사용할 수 있다는 점입니다. 

### 합성곱 신경망과 완전연결 신경망의 차이
1. 패딩(padding), 스트라이드(stride) 개념 존재
2. 3차원 데이터와 같은 입체적인 데이터가 흐름

### 완전연결 계층의 문제점
- 완전연결 계층의 문제점은 **'데이터의 형상이 무시'** 된다는 점입니다. 입력 데이터가 이미지인 경우를 예로 들면, 이미지는 보통 세로, 가로, 채널(색상)로 구성된 3차원 데이터입니다. 이 데이터를 완전연결 계층에 입력할 때는 3차원의 데이터를 평평한 1차원 데이터로 평탄화해주어야 합니다. 이 때 공간적으로 가까운 픽셀은 값이 비슷하거나, RGB의 각 채널은 서로 밀접하게 관련되어 있다거나, 거리가 먼 픽셀끼리는 별 연관이 없다거나 하는 데이터의 공간적인 정보가 유실되게 됩니다. 반면에 합성곱 계층은 데이터의 형상을 유지합니다. 이미지도 3차원 데이터로 입력받고, 마찬가지로 다음 계층에도 3차원 데이터로 전달합니다. 그래서 이미지처럼 형상을 가진 데이터를 제대로 이해할 가능성이 생기게 됩니다. ( CNN을 활용한 의도 분석 알고리즘에서도 문장 내의 단어 순서(공간적 정보)도 중요하다고 판단합니다. ) CNN에서는 합성곱 계층의 입출력 데이터를 특징 맵(feature map)이라고도 합니다. 

### 합성곱 연산
- 합성곱 계층에서는 합성곱 연산을 처리합니다. 합성곱 연산은 이미지 처리에서 말하는 필터연산입니다. 필터는 **커널**이라고 불리기도 합니다. 합성곱 연산은 필터의 윈도우를 일정 간격으로 이동해가며 입력데이터에 적용합니다.(아래 이미지 참고) 연산은 입력과 필터에서 대응하는 원소끼리 곱한 후 그 총합을 구합니다.
(단일 곱셈-누산:FMA, fused multiply-add) 완전연결 신경망에서는 가중치 매개변수와 편향이 존재하는데, CNN에서는 필터의 매개변수가 그 **가중치**에 해당합니다. 

<p align="center">
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=http%3A%2F%2Fcfile3.uf.tistory.com%2Fimage%2F2764173558F475B42C0A8B"/>
 
### 패딩(padding)
- 합성곱 연산을 수행하기 전에 입력 데이터 주변을 특정 값(예, 0)으로 채우기도 합니다. 이를 패딩이라고 하며, 합성곱 연산에서 주로 활용합니다. 아래 그림은 처음에 크기가 (4,4)인 입력 데이터에 패딩이 추가되어 (6,6)이 되고, 입력에 (3,3) 크기의 필터를 걸면 (4,4) 크기의 출력 데이터가 생성됩니다. 패딩은 원하는 정수로 설정할 수 있습니다. CNN 네트워크는 하나의 필터 레이어가 아니라 여러 단계에 걸쳐서 계속 필터를 연속적으로 적용하여 특징을 추출하는 것을 최적화 해나가는데, 필터 적용 후 결과 값이 작아지게 되면 처음에 비해서 특징이 많이 유실 될 수 가 있습니다. 필터를 거쳐감에 따라서 특징이 유실되는 것을 기대했다면 문제가 없겠지만, 아직까지 충분히 특징이 추출되기 전에, 결과 값이 작아지면 특징이 유실됩니다. 이를 방지 하기 위한 방이 패딩 기법입니다.


<p align="center">
<img src="http://4.bp.blogspot.com/-BYQPnAc17rU/WYJrKOqnDzI/AAAAAAAALNQ/ZnpIh7wEBcom4lOsOKSMlegv_EsseHisACK4BGAYYCw/s1600/o8.PNG"/>


### 스트라이드(stride)
- 필터를 적용하는 위치의 간격을 스트라이드라고 합니다. 아래 그림은 크기가 (7,7)인 입력 데이터에 스트라이드가 2로 설정한 필터를 적용합니다.


<p align="center">
<img src="http://2.bp.blogspot.com/-vtZW1-cBQGg/WYJrUnBjRiI/AAAAAAAALNY/GhTnu5QDi3M4NHB_FiyOJAjy58mTkzlYwCK4BGAYYCw/s1600/o9.PNG"/>


스트라이드를 키우면 출력의 크기는 작아집니다. 반면에 앞서 패딩을 크게하면 출력의 크기는 커졌습니다. 입력 크기를 (H,W), 필터 크기를 (FH, FW), 출력 크기를 (OH, OW), 패딩을 P, 스트라이드를 S라고 하면 출력 크기는 아래와 같이 계산합니다.


<p align="center">
<img src="https://latex.codecogs.com/gif.latex?%5C%5COH%3D%5Cfrac%7BH&plus;2P-FH%7D%7BS%7D&plus;1%5C%5C%5C%5C%20OW%3D%5Cfrac%7BW&plus;2P-FW%7D%7BS%7D&plus;1%5C%5C%5C%5C"/>


### 블록으로 생각하기
- 3차원의 합성곱 연산은 데이터와 필터를 직육면체 블록이라고 생각하면 쉽습니다. 다만 3차원의 블록에 1개의 필터를 적용하면 출력 데이터는 (1, OH, OW) 인 한 장의 특징 맵입니다. 합성곱 연산의 출력으로 다수의 채널을 내보내려면 아래와 같이 필터를 다수 사용하는 것입니다. 필터를 N개 사용하면 출력맵도 FN개가 생성됩니다. 이렇게 완성된 블록을 다음 계층으로 넘기겠다는 것이 CNN의 처리 흐름입니다. 이상에서 보듯이 합성곱 연안에서는 필터의 수도 고려해야 합니다. 따라서 필터의 가중치는 4차원의 데이터이며 (출력 채널 수, 입력 채널 수, 높이, 너비) 순으로 씁니다. 


<p align="center">
<img height="300px" src="http://1.bp.blogspot.com/-O60db3qXQws/WYJw8NMcTzI/AAAAAAAALOI/7oF6RD68VV08XcOSHdd1vyzfuwTwRiZtwCK4BGAYYCw/s1600/o13.PNG"/>


## 풀링 계층
- 풀링은 세로, 가로 방향의 공간을 줄이는 연산입니다. 컨볼루셔널 계층을 통해서 어느정도 특징이 추출 되었으면, 이 모든 특징을 가지고 판단을 할 필요가 없습니다. 쉽게 예를 들면, 우리가 고해상도 사진을 보고 물체를 판별할 수 있지만, 작은 사진을 가지고도 그 사진의 내용이 어떤 사진인지 판단할 수 있는 원리입니다. (출처1) 아래 이미지는 최대 풀링(max pooling) 처리한 결과입니다. 참고로 폴링의 윈도우 크기와 스트라이드는 같은 값으로 설정하는 것이 보통입니다. 최대 풀링은 대상 영역에서 최대값을 취하는 연산입니다.


<p align="center">
<img src="https://t1.daumcdn.net/cfile/tistory/2121E641583ED6AF23"/>
 

풀링 계층은 다음과 같은 특징이 있습니다.


1. 학습해야 할 매개변수가 없다.
2. 채널 수가 변하지 않는다.
3. 입력의 변화에 영향을 적게 받는다.(강건하다) 

CNN에 대한 기본적인 내용 정리는 이쯤하도록 하고 다음은 자연어처리 분야에서 CNN을 어떻게 사용하는지 정리해보도록 하겠습니다.


### 의도 분류에 CNN 적용
- 자연 언어는 단어나 표현의 등장 순서가 중요한 sequential data입니다. 앞서 완전연결 계층의 문제점은 데이터의 형상을 무시한다는 데 있었습니다. 반면에 합성곱 계층은 데이터의 형상을 유지한다고 설명했습니다. 이를 응용하여 CNN을 텍스트 처리에 응용한 연구가 바로 Yoon Kim(2014) (http://emnlp2014.org/papers/pdf/EMNLP2014181.pdf) 입니다. 이미지 처리를 위한 CNN의 필터가 이미지의 지역적인 정보를 추출하는 역할을 한다면, 텍스트 CNN의 필터는 텍스트의 지역적인 정보, 즉 단어 등장순서/문맥 정보를 보존한다는 아이디어 입니다. 이를 도식화하면 아래와 같습니다. (출처3)


<p align="center">
<img height="300px" src=https://i.imgur.com/1Flo6TK.gif"/>

 위 이미지를 자세히 보면 한 문장당 단어 수는 총 n개(변수명 : sequence_length) 입니다. 이 단어들 각각은 p차원(변수명 : embedding_size)의 벡터이고, 붉은색 박스는 필터를 의미합니다. 위 움짤의 경우 필터의 크기는 2로써 한번에 단어 2개씩을 보게 됩니다. 이 필터는 문장에 등장한 단어 순서대로 슬라이딩해가면서 문장의 지역적인 정보를 보존하게 됩니다. 필터의 크기가 1이라면 Unigram, 2라면 Bigram, 3이면 Trigram.. 이런 식으로 필터의 크기를 조절함으로써 다양한 N-gram 모델을 만들어낼 수 있습니다. CNN은 문장의 지역 정보를 보존함으로써 단어/표현의 등장순서를 학습에 반영하는 아키텍처라 할 수 있겠습니다. RNN과 CNN이 자연언어처리 분야에서도 각광받고 있는 이유이기도 합니다. Yoon Kim(2014)의 아키텍처는 아래와 같습니다. (출처3)
 
<p align="center">
<img height="300px" src="https://i.imgur.com/JN72JHW.png"/>

 다음으로는 필터의 차원수를 살펴보겠습니다. 필터의 너비는 embedding_size입니다. 높이는 filter_size인데, 만약 2라면 Bigram, 3이라면 Trigram 모델이 될 겁니다. 채널수는 1로 고정했습니다. (앞전 설명에서 이미지 같은 경우는 채널수가 3이었습니다.)
 
<p align="center">
<img height="300px" src="http://i.imgur.com/WlGbDJfm.png"/>
 
 이제 위에 내용을 바탕으로 작성된 소스코드를 보겠습니다. 코드는 (출처4)의 코드를 참고하였습니다. 일단 코드는 아래와 같습니다.
 
 ```python
     def featurize_cnn(self, corpus, wdim, maxlen):

        with open('model_drama.pickle', 'rb') as f:
            model_ft = pickle.load(f)

        conv_total = np.zeros((len(corpus), maxlen, wdim, 1))
        for i in range(len(corpus)):
            if i % 1000 == 0:
                print(i)
            s = corpus[i]
            for j in range(len(s)):
                if s[-j - 1] in model_ft and j < maxlen:
                    conv_total[i][-j - 1, :, 0] = model_ft[s[-j - 1]]
        return conv_total
 ```
 
 featurize_cnn 함수는 위에서 도식화 한 그림의 모양처럼 문장을 컨볼루션 연산을 하기위한 형태로 데이터를 만들어줍니다. 함수의 파라미터는 아래와 같습니다.
 
 ```
 corpus : 토크나이징된 문장 전체 리스트
 wdim : 단어 벡터의 차원 ( 앞서 embedding size )
 maxlen : 한 문장에 몇 개 까지 단어를 허용하는지 ( 앞서 sequence_length )
 ```

 제가 소스를 가져온 (출처4)에서는 100차원의 단어 벡터(wdim=100)를 사용하였습니다. 그리고 한 문장당 단어의 길이를 30으로 설정(maxlen:30) 했습니다. 만약 토크나이징된 문장 단어의 길이가 30을 넘게 되면 뒤에서부터 30개를 사용하도록 했습니다. 보통 한국말은 어미에 중요한 단어가 있을 확률이 높으니까 타당한 것 같습니다. ( 저와 같이 자연어처리 분야에 초보이시면서, 시간이 되시면 출처4에 있는 전체 내용을 한 번 보시기를 추천드립니다. )
 
 
 코드에 대한 설명을 계속하자면, 일단 피클로 저장해둔 word2vec 모델을 불러옵니다. 이 모델도 (출처4)에서 다운받았습니다. 이후에는 파라미터로 넘어온 값을 Shape으로 갖고 모든 값이 0으로 채워진 넘파이배열(ndarray)를 만듭니다. 이 이야기는 앞서 문장 단어 길이가 30이 안되는 경우에는 0을 채우겠다는 의미입니다. 아래 로직은 미리 학습한 word2vec 모델에 단어가 있는지 확인하고, 문장 길이를 확인해서 데이터를 채워주는 로직입니다.


 (제가 참조한 곳에서는 단어 벡터를 100차원, 문장 길이를 30으로 했는데 어떤 의사결정 과정으로 100과 30이라는 숫자가 나오는지 개인적으로 궁금합니다. 지금 제가 가진 지식으로는 100과 30이라는 숫자처럼 적절한 숫자를 어떻게 찾아내는지에 대해서는 감이 잘 오지 않지만 고민해봐야 하는 주제인 것 같아 몇글자 적어 놓겠습니다. 공부한 내용을 정리하는거라 나중에 또 반복해서 보게될 때는 적절한 수를 찾아보도록 하겠습니다.ㅎㅎ)

 
 CNN에 대한 간략한 설명과 CNN을 활용하여 의도 분류를 하기 위한 기본적인 준비는 마쳤습니다. 이제는 모델을 만들면 적용해볼 수 있을 것 같습니다. 필터를 정하고, 풀링을 설정하고 하는 등등의 작업입니다. 모델을 만드는 부분은 공부가 부족해서 성급하게 정리하지 않고 나중에 다시 한 번 정리하겠습니다.
 
 
 


