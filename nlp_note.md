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
 
 
## 02. Word2Vec으로 선물 추천하기
### 출처 및 참고
1. 빈도수 세기의 놀라운 마법 Word2Vec, Glove, Fasttext (https://ratsgo.github.io/from%20frequency%20to%20semantics/2017/03/11/embedding/https://ratsgo.github.io/from%20frequency%20to%20semantics/2017/03/11/embedding/)
2. Word2Vec의 학습 방식 (https://ratsgo.github.io/from%20frequency%20to%20semantics/2017/03/30/word2vec/)


 - 단어를 임베딩하는 것은 이미 앞서 CNN을 활용한 의도 분류에서도 학습해야 하는 대상을 만들기위해 사용했었습니다. 자연어처리 분야에서 단어를 벡터화하는건 매우 중요한데 그동안은 학습이 완료된 모델을 사용하거나 하는 경우여서 Word2Vec에 대해 깊게 학습하지 않고 넘어갔었습니다.
 - 저는 선물을 추천하는 챗봇을 만드는 중인데, 선물 추천 방법 중 한가지로 Word2Vec을 활용해볼 생각입니니다. 간단한 아이디어는 이렇습니다.
 
 ```
 1. "선물"에 관련된 글을 크롤링한다. ( ex. SNS에서 "선물"로 검하고 나온 글을 크롤링 )
 2. 크롤링된 글들을 형태소 분석하여 명사와 같은 중요한 형태소만 추출한다. ( ex. "요즘 부쩍 피곤해보이시는 아버지 생신 선물로 홍삼엑기스 구매! 건강하게 오래오래 사세요. 감사합니다!!" 라는 글이 있다면 피곤, 아버지, 생신, 선물, 홍삼, 엑기스, 건강, 감사 등과 같은 명사를 추출 )
 3. 추출한 학습시켜 데이터를 임베딩한다.
 4. 학습이 완료된 모델에 선물 받는 대상의 특징 ( 아버지, 생신 ) 등의 단어와 가장 코사인 유사도가 높은 상위 n개의 명사를 추출한다.
 5. 추출된 명사 중에서 선물인 항목을 추천한다.
 ```
 
 - 약 만 건의 데이터로 위의 과정으로 학습을 진행해서 샘플 모델을 만들어보았습니다. 결과는 그다지 훌륭하지 않았지만 한 번 문제를 하나씩 해결해보고 과연 실제로 쓸만한지 자체적으로 판단을 해보도록 하겠습니다.
 - 일단 그 전에 단어를 벡터화하는 임베딩에 대해 간단히 정리하고 넘어가도록 하겠습니다.
 - 앞서 많이 언급했던 이기창 님의 블로그 내용을 정리하였습니다.
 

### Word2Vec 개요
 - Word2Vec은 단어를 벡터로 바꾸는(임베딩) 방법론
 - 크게 CBOW(Continuous  Bag of Words)와 Skip-Gram 두 가지 방식이 있음
 - CBOW는 주변에 있는 단어들을 가지고 중심에 있는 단어를 맞추는 방식
 ```
 나는 ___에 간다
 ```
 - 위 문장에는 '학교', '집', '회사' 등 다양한 단어가 들어갈 수 있음
 - Skip-Gram은 단어의 앞뒤로 어떤 단어가 올지를 예측하는 방식
 ```
 __외나무다리__ 
 ```
 - 위 문장에서 '외나무다리' 앞에는 '는' 그 앞에는 '원수' 뒤에는 '에서', '만난다'가 올 확률이 높음
 - 학습시킨 말뭉치에서 '외나무다리' 뒤에 '-에서' '만난다' 는 표현이 나온다면 Word2Vec은 '외나무다리'가 '-에서', '만난다'와 연관이 있다고 보고 벡터를 구성
 - 여기서 고민해볼 부분은 '외나무다리'와 '원수'가 비슷한 표현(단어)라고 볼 수 있는가?
 

### Word2Vec의 목적함수와 코사인 유사도
 - Word2Vec은 Distributional Hypothesis에 근거한 방법론
 - Distributional Hypothesis : 비슷한 맥락에 등장하는 단어들은 유사한 의미를 지니는 경향이 있다. (words that occur in similar contexts tend to have similar meanings) => NLP의 기본 가정 중 하나(https://ratsgo.github.io/from%20frequency%20to%20semantics/2017/03/10/frequency/)
 - Word2Vec(Skip-Gram)은 아래식을 최대화하는 걸 목표로 함
 
 <p align="center"/>
 <img src="https://latex.codecogs.com/gif.latex?p%28o%7Cc%29%3D%5Cfrac%7Bexp%28u_%7Bo%7D%5ETv_%7Bc%7D%29%7D%7B%5Csum_%7Bw%3D1%7D%5E%7BW%7Dexp%28u_%7Bw%7D%5ETv_%7Bc%7D%29%7D"/>


 - o는 주변단어(context word), c는 중심단어(center word)
 - P(o|c)는 중심단어 c가 주어졌을 때, 주변단어 o가 등장할 조건부확률
 - 이 식을 최대화한다는 것은 **중심단어로부터 주변 단어를 잘 맞춘다는 의미**
 - Word2Vec의 저자들은 P(o|c)를 우변과 같이 정의
 - u와 v는 단어 벡터들 => 예를 들어 '외나무다리'라는 중심단어 벡터가 <img src="https://latex.codecogs.com/gif.latex?v_%7Bc%7D"/>, '원수'라는 주변단어 벡터가 <img src="https://latex.codecogs.com/gif.latex?u_%7Bo%7D"/>
 - 엄밀히 이야기하면 u와 v는 다른 벡터들이지만 임베딩이 잘 되어 있다면 학습의 결과로 도출된 u와 v 가운데 어떤걸 써도 상관없다고 함
 
 
#### 코사인 유사도
 - 2차원 평면 위에 단위원(반지름이 1)이 있다고 할 때, 코사인 정의에 의해 <img src="https://latex.codecogs.com/gif.latex?cos%28%5Ctheta%29"/>는 아래 그림의 녹색 선의 길이와 같음
 
 
 <p align="center">
 <img height="400px" src="http://i.imgur.com/zCFB0mS.png"/>
 
 
 - A가 B에 정확히 포개져 있을 때(Θ=0도), <img src="https://latex.codecogs.com/gif.latex?cos%28%5Ctheta%29"/>는 1
 - 아래 그림의 경우 빨간색 직선이 x축과 만나는 점이 바로 <img src="https://latex.codecogs.com/gif.latex?cos%28%5Ctheta%29"/>


 <p align="center">
 <img height="400px" src="http://i.imgur.com/H8WvWMB.gif"/>
 
 
 - <img src="https://latex.codecogs.com/gif.latex?cos%28%5Ctheta%29"/>는 단위원 내 벡터들끼리의 **내적(inner product)** 과 같음
 - 내적값이 커진다는 것은 두 벡터가 이루는 Θ가 작아진다(유사도가 높아진다)라는 것을 의미
 - 위 내용을 고차원의 벡터공간으로 확대할 수 있음
 - 위의 식에서 우변을 최대화한다는 말은 분자를 키우고, 분모를 줄인다는 의미
 - 우선 분자 부분을 보면
 
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?exp%28u_%7Bo%7D%5ETv_%7Bc%7D%29"/>
 
 
 - 분자를 증가시킨다는 건 exp의 지수를 크게 한다는 걸 뜻함
 - exp의 지수는 두 벡터의 내적값 => 이 값이 커진다는건 앞서 언급한 것처럼 벡터들 사이의 Θ를 줄인다(유사도를 높인다는 의미)
 - 다시 말해 중심단어(c)와 주변단어(o)를 벡터공간에 위치시킬 때, 인근에 위치시킨다는 의미로 해석될 수 있음
 - 분모를 줄인다는 건 아래를 작게 해야 함
 
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?%5Csum_%7Bw%3D1%7D%5E%7BW%7Dexp%28u_%7Bw%7D%5ETv_%7Bc%7D%29"/>
 
 
 - 분모는 중심단어(c)와 학습 말뭉치 내 모든 단어를 각각 내적한 것의 총합
 - 분모를 줄이려면 주변에 등장하지 않은 단어와 중심단어의 내적값이 작아져야 함
 - 즉 중심단어 주변에 등장하지 않는 단어와 중심단어 벡터 사이의 Θ를 키운다(코사인 유사도를 줄인다)는 의미


### Word2Vec의 학습 방식
 - Word2Vec은 Neural Network Language Model(NNLM)을 계승하면서 학습 속도와 성능을 비약적으로 끌어올려 주목을 받고 있음


#### Word2Vec 학습 파라미터
 - Word2Vec의 아키텍처(Skip-Gram)을 도식화 하면 아래와 같음
 - 은닉층이 하나인 간단한 뉴럴네트워크 구조
 
 
 <p align="center">
 <img height="400px" src="http://i.imgur.com/TupGxMl.png"/>
 
 
 - 위 구조에서 핵심은 가중치행렬 <img src="https://latex.codecogs.com/gif.latex?W%2C%7BW%7D%27"/> => **Word2Vec의 학습 결과**기 때문
 - 입력층-은닉층, 은닉층-출력층을 잇는 가중치행렬의 모양이 서로 전치(transpose)
 - 전치하면 모양이 같다고 해서 완벽히 동일한 행렬은 아님
 - 입력층와 은닉층을 잇는 가중치행렬 W를 좀더 살펴보면, V는 임베딩하려는 단어의 수, N은 은닉층의 노드 개수(사용자 지정)
 - Word2Vec은 최초 입력으로 one-hot-vector를 받음
 - 1 X V 크기의 one-hot-vector의 각 요소와 은닉층의 N개 노드는 각 1대1 대응이 이뤄져야 하므로 가중치행렬 W의 크기는 V X N
 - 예를들어 학습 말뭉치에 단어 1만개가 있고 은닉층 노드를 300개로 지정했다고 하면, 가중치행렬 W는 좌측하단 오렌지색 행렬 형태가 됨
 
 
 <p align="center">
 <img height="400px" src="http://i.imgur.com/NHUCNXq.png">
 
 - Word2Vec 아키텍처는 중심단어로 주변단어를 맞추거나, 주변단어로 중심단어를 더 잘 맞추기 위해 가중치행렬인 <img src="https://latex.codecogs.com/gif.latex?W%2C%7BW%7D%27"/>을 조금씩 업데이트하면서 학습이 이뤄지는 구조
 - 여기서 흥미로운 점은 W가 one-hot-encoding된 입력벡터와 은닉층을 이어주는 가중치행렬임과 동시에 Word2Vec의 최종 결과물인 **임베딩 단어 벡터 모음** 이라는 점
 - 아래와 같이 단어가 5개뿐인 말뭉치에서 Word2Vec을 수행한다고 가정해보면
 - 사전 등장 순서 기준으로 네 번째 단어를 입력으로 하는 은닉층의 값은 아래처럼 계산
 - Word2Vec의 은닉층을 계산하는 작업은 사실상 가중치행렬 W에서 해당 단어에 해당하는 행벡터를 참조(lookup) 해 오는 방식과 동일
 - 학습이 마무리되면 W의 행벡터들이 각 단어에 해당하는 임베딩 단어벡터가 됨
 
 
 <p align="center">
 <img height=100px" src="http://i.imgur.com/zuSZWdL.png"/> 
 

#### Word2Vec 입력과 Skip-Gram
 - Word2Vec의 Skip-Gram(중심 단어로 주변단어 예측)이 말뭉치로부터 어떻게 입력값과 정답을 만들어내는지 살펴보면,
 -  ‘The quick brown fox jumps over the lazy dog.’ 문장으로 시작하는 학습말뭉치가 있다고 가정
 - 윈도우(한번에 학습할 단어 개수) 크기가 2인 경우 아키텍처가 받는 입력과 정답은 아래와 같음
 
 
 <p align="center">
 <img height="400px" src="http://i.imgur.com/8zNRwsn.png"/>
 
 
 - 첫번째 스텝 => 중심단어는 처음 등장하는 단어인 'The', 윈도우 크기가 2기 때문에 중심단어 앞뒤로 두개씩 봐야하지만 'The'를 기준으로 이전 단어가 존재하지 않으므로 뒤에 등장하는 두 개 단어 사용
 - 여기서 주의할 점은 'quick'과 'brown'을 따로 떼어서 각각 학습한다는 점 (the, quick), (the, brown)
 - 두번째 스텝에서는 중심단어를 오른쪽으로 한 칸 옮겨 'quick'를 중심단어로 하고, 'The', 'brown', 'fox'를 주변단어 정답으로 진행
 - 이런식으로 말뭉치 내에 존재하는 모든 단어를 윈도우 크기로 슬라이딩해가며 학습을 하면 iteration 1회 마무리
 - 주변단어로 중심단어를 예측하는 CBOW에 비해 Skip-Gram의 성능이 좋은 이유는 CBOW의 경우 중심단어는 한 번의 업데이트 기회를 가질 때, Skip-Gram의 경우 중심단어는 4번의 업데이트 기회를 가짐 => 요즘은 Word2Vec을 할 때, Skip-Gram을 주로 사용
 
 
#### Word2Vec의 학습
 - 앞서 Word2Vec의 Skip-Gram은 아래 식을 최대화하는 방향으로 학습을 진행한다고 했음
 
 
 <p align="center"/>
 <img src="https://latex.codecogs.com/gif.latex?p%28o%7Cc%29%3D%5Cfrac%7Bexp%28u_%7Bo%7D%5ETv_%7Bc%7D%29%7D%7B%5Csum_%7Bw%3D1%7D%5E%7BW%7Dexp%28u_%7Bw%7D%5ETv_%7Bc%7D%29%7D"/>
 
 
 - 우변의 v는 입력층-은닉층을 잇는 가중치행렬 <img src="https://latex.codecogs.com/gif.latex?W">의 행벡터, u는 은닉층-출력층을 잇는 가중치행렬 <img src="https://latex.codecogs.com/gif.latex?%7BW%7D%27"/>의 열벡터
 - 우선 분자의 지수를 키우는 건 중심단어(c)에 해당하는 벡터와 주변단어(o)에 해당하는 벡터의 내적값을 높인다는 뜻
 - 분모를 줄이는 건 윈도우 크기 내에 등장하지 않는 단어들은 중심단어와의 유사도를 높인다는 의미
 - 아래는 Word2Vec의 학습 파라미터인 중심단어 벡터 업데이트 과정을 수식으로 정리한 내용


### 실제로 적용해보기
 - 기본 개요와 이론에 대한 내용 정리는 이정도로 하고, 실제 크롤링한 데이터를 가지고 괜찮은 결과가 나올지 한 번 확인해보겠습니다.
 - 결과 확인 -> 분석 -> 개선 : 이 사이클을 가지고 모델이 과연 선물 추천에 적합할지 판단해보겠습니다.
 - 개발 환경은 아래와 같습니다.
 
```
Python 3.6.0+
konlpy==0.4.4
mecab-python3==0.7
gensim==3.6.0
```
 

#### 데이터 전처리
 - 크롤링 된 데이터에서 명사만 추출해 따로 저장해보겠습니다. 이 추출한 데이터가 Word2Vec 학습 대상입니다. 
 - 형태소분석기는 mecab을 선택했는데, 선택한 이유는 아래와 같습니다.
  1. 형태소분석 품질이 좋음
  2. 분석 속도 역시 빠름
  3. 사용자 사전 추가 가능
 - 아래는 코드입니다.
 
```python
def precoess_data():
 content_list = [dict(zip(['seq', 'user_content'], row)) for row in cursor.fetchall()]

 mecab = Mecab()
 results = []
 for content in content_list:
     prc_content = content['user_content'].replace("\n", "").replace("#", "")
 
     malist = mecab.pos(prc_content)
     r = []
     for word in malist:
         if word[1] in ['NNG', 'NNP', 'NP'] and '\\u' not in word[0]:
             r.append(word[0])
     rl = (' '.join(r)).strip()
     results.append(rl)
     update_processed_data(content['seq'], rl)
```

 - 코드를 간단히 설명하면, 크롤링한 데이터를 DB에서 불러온 후, mecab으로 형태소 분석한 뒤 명사와 관련된 결과만 저장하는 로직입니다.
 - 예)
```
-- 원본
선물로 받은 포마드
.
요즘 자전거 탄다고 딴건 신경 거의 👋
.
가끔 또 다른 나를 찾아 보자.

#포마드
#선물
#감사합니다🙏

-- 명사 추출 후 결과
선물 포마드 자전거 신경 나 포마드 선물 감사
 ```
 - 명사 추출 후의 결과를 보니 수정해야할 부분이 좀 있어 보이지만 일단 계속 진행해보겠습니다.
 - 위의 결과를 가지고 모델을 학습시켜 보겠습니다.
 
 
```python
def train_word2vec():
 results = [dict(zip(['prc_content'], row)) for row in cursor.fetchall()]

 for result in results:
     print(result['prc_content'])

 result_file = 'result_file_0901'
 with open(result_file, 'w', encoding='utf-8') as fp:
     # fp.write('\n'.join(results))
     for result in results:
         fp.write(result['prc_content'])
         fp.write('\n')

 p_size = 100
 p_window = 10
 p_min_count = 3 

 data = word2vec.LineSentence(result_file)
 model = word2vec.Word2Vec(data, size=p_size, window=p_window, min_count=p_min_count, workers=2, iter=30, sg=1)
 model.save('rec_model_0901_{p_size}_{p_window}_{p_min_count}'.format(p_size, p_window, p_min_count))
 ```
 
 - 위 코드의 의미는 앞서 전처리한 데이터를 파일로 저장하고, word2vec 학습을 진행합니다.
 - 학습의 결과는 100차원 벡터이며, 학습은 중심 단어의 앞 뒤로 10개, 3번 이하인 단어는 학습에서 제외하고, 30번 반복, Skip-Gram을 사용하라는 의미입니다.
 - 하이퍼파라미터의 초기값을 어떻게 설정해야 하는지에 대해서는 아직 제가 찾지 못했기 때문의 임의의 값으로 일단 학습을 진행하였습니다.
 - 학습 건수는 42947건이고, 학습한 모델에 "생일", "엄마" 라는 두 단어와 가장 코사인 유사도가 높은 상위 30개 결과는 아래와 같습니다.
 

```
[('조은별', 0.7463708519935608), 
('서운', 0.7154489755630493), 
('미역국', 0.6994922757148743),
('아빠', 0.6969490051269531), 
('생일상', 0.6854463815689087), 
('티토스', 0.6836491823196411),
('축하', 0.6831715703010559), 
('해영', 0.6732158660888672),
('구순', 0.6706515550613403), 
('수어지교', 0.6673763394355774), 
('학부형', 0.6619960069656372), 
('아들', 0.6541163921356201), 
('어마마마', 0.652460515499115), 
('준용', 0.6520766019821167), 
('오발탄', 0.647763729095459), 
('용현', 0.6432062387466431), 
('사세', 0.6374843716621399), 
('처남', 0.6372784972190857), 
('환갑잔치', 0.6351194977760315), 
('생신', 0.6301501989364624), 
('딸', 0.6297280788421631), 
('담부', 0.6250455379486084), 
('말싸움', 0.6224365234375), 
('구대', 0.6204590797424316), 
('생파', 0.6180790662765503), 
('나희', 0.6176405549049377), 
('서열', 0.6151608228683472), 
('항목', 0.6136439442634583), 
('찬장', 0.610844612121582), 
('박강현', 0.6103270053863525)]
```

 - 위의 결과에서 선물로 추천할 만한 항목이 거의 없는 것 같습니다.
 - 앞으로 문제라고 판단되는 부분에 대해서 조금씩 변경해가면서 결과를 확인해보도록 하겠습니다.ㅎㅎ이렇게만 봐서는 추천 모델로 사용하기 어려울 것 같긴 하지만..그래도 어느정도 판단이 설 때 까지는 계속 해보도록 하겠습니다.


#### 최초 모델 분석
 - 위의 데이터 결과를 한 번 보겠습니다. "선물", "엄마" 이라는 두 단어와 가장 코사인유사도가 가장 높은 단어는 '조은별' 이라는 단어입니다. 해당 단어가 크롤링 데이터에 얼마나 있는지 보았더니 실제로 4건이 있었고, 4건 모두 동일한 데이터가 중복되서 크롤링 된 경우였습니다.
 - 크롤링 시 중복처리 로직이 완벽하지 않아서 중복 데이터가 들어갔습니다. 그런데 4만 건 중에 4건이라는 데이터 밖에 없는 케이스가 가장 높은 유사도를 갖는건 아무래도 이상해 보입니다. Word2Vec을 추천 모델로 활용할 때 개념이 "소량의 데이터를 잘 정비해서 학습시킨다" 라기 보다는 "많은 양의 데이터를 학습시켜 결과를 얻는다" 에 가깝겠지만 아직 크롤링 로직의 개선이 필요한 상황이라 일단 결과를 얻기 위해서는 데이터를 정비할 필요가 있어 보입니다.
 - 데이터를 정비하기 전에 일단은 하이퍼파라미터를 잠깐 수정해보겠습니다. 최초 모델은 **학습을 30번 반복**하게끔 설정을 했는데, **잘못된 데이터가 많을 경우 잘못된 데이터를 반복해서 학습해 원하지 않은 결과**가 나올 것 같습니다. 일단 크롤링 로직이 정비되어 데이터가 어느정도 학습할만한 수준이 될 때 까지는 일단 반복을 1회로 설정해서 학습시켜보겠습니다. ( iter=30 -> iter=1 ) 아래는 반복 횟수만 바꾸어 학습한 모델에 동일하게 "선물", "엄마" 라는 단어를 검색했을 때 유사도가 높은 30개 단어입니다.
 
```
[('생파', 0.9010462760925293), 
('생일상', 0.8933207988739014), 
('미역국', 0.88210529088974),
('사촌', 0.8646770715713501), 
('장모님', 0.8578191995620728), 
('딸래미', 0.8518246412277222), 
('미소', 0.8474768400192261), 
('내사랑', 0.8474330306053162),
('생일잔치', 0.8461812138557434), 
('촛불', 0.8450530171394348), 
('아빠', 0.8448730707168579), 
('표', 0.839544415473938), 
('추카', 0.8395388126373291), 
('돌상', 0.8394769430160522), 
('너희', 0.8371490240097046), 
('지후', 0.8339511156082153), 
('울엄마', 0.8315588235855103), 
('막둥이', 0.8312948942184448), 
('낭', 0.8308857083320618), 
('등원', 0.8308796882629395), 
('다', 0.8301701545715332), 
('할머니', 0.8291335105895996), 
('이모티콘', 0.8290852904319763), 
('교사', 0.8286694884300232), 
('개학', 0.8282244801521301), 
('내년', 0.8276127576828003), 
('뽀로로', 0.8267506957054138), 
('욤', 0.8259954452514648), 
('아리조나', 0.8254351615905762), 
('쏙', 0.8253586292266846)]
```
 
 - 일단 앞서 잘못된 케이스로부터 학습된 단어들은 안보이는 것으로 보았을 때, 의도한대로 학습은 된 것 같습니다. 그럼 이 상태에서 이제 또 다시 분석을 해보고 수정이 필요한 부분은 수정해보도록 하겠습니다.
 - 아직 추천 모델을 구축하기에 데이터가 매우 부족한 것이 사실입니다. 데이터는 계속 수집하고 있고, 로직도 개선하고 있기 때문에 어느정도 모델의 기본틀이 잡히면 더 추가된 데이터로 학습해보겠습니다.
 - 그리고 궁극적으로는 데이터가 추가되면 추가된 데이터가 반영된 Word2Vec 모델을 만드는 것을 자동화해야 할 것 같습니다. 이 부분까지를 목표로 계속 진행하겠습니다.
 
 
#### 형태소분석 개선
 - 데이터의 크기를 늘리고 하이퍼파라미터를 수정하기 전에 먼저 처리해줘야 할 것이 있어 보입니다. 크롤링 데이터의 형태소 분석 결과를 보았을 때, 제대로 분석되지 않은 항목들이 있습니다. "에어팟" 같은 하나의 단어를 "에어"와 "팟" 으로 분리하는 경우가 많았습니다. Word2Vec으로 학습하기 원하는 단어는 
"에어", "팟" 인 분리 된 단어가 아니므로 하나의 단어인 "에어팟"으로 데이터를 처리하는 과정이 필요합니다. 이와 같은 데이터 예시는 아래와 같고 아래의 예시들을 제대로 인식하게끔 해보겠습니다.

| 원본 | 형태소 분석 결과 |
| -- | -- |
| 에어팟 | 에어 팟 |
| 키링 | 키 링 |
| 브레이슬릿 | 브레이 슬릿 |
| 머그컵 | 머그 컵 |
| 아디다스 | 아디 다스 |
| 록시땅 | 록 시 땅 |
| 제이에스티나 | 제이 스티나 |
| 린넨셔츠 | 린 셔츠 |
| 석고방향제 | 석고 방향제 |
 
 - 앞서 mecab을 선택한 이유 중에서 사용자 정의 사전을 사용할 수 있다고 했었는데, konlpy를 통해 설치했을 경우 지원하지 않는 부분을 확인했습니다.  mecab을 새로 설치하거나 따로 데이터 처리를 해주거나 하는 부분이 필요한데 일단은 프로시저를 만들어서 형태소분석 결과를 쿼리로 업데이트 하겠습니다.
 - 쿼리는 단순히 **"에어 팟" => "에어팟"** 형식으로 진행했습니다. 이 정도만해도 충분히 데이터가 처리되는 것을 확인할 수 있습니다.


#### 학습 데이터 추가
 - 위의 작업을 하는 동안 크롤링 데이터가 추가 되어서 약 10만건의 데이터로 위의 과정을 다시 진행해 보았습니다. 데이터를 다뤄 본 경험이 많이 없어서 10만건이라는 데이터가 어떤 결과를 도출해내기에 충분한 데이터인지는 잘 모르겠지만 (솔직히 많이 부족해 보입니다ㅎㅎ) 이 전에 학습한 모델에 비해서는 2배로 늘어났으니 약간의 개선을 기대해보겠습니다.
 - Word2Vec의 하이퍼파라미터는 그대로 유지하고 10만건의 데이터를 다시 학습시켜 "엄마", "선물" 두 단어와 가장 코사인유사도가 높은 30개 단어를 뽑아보겠습니다.
 
```
[('음력', 0.8308107256889343),
('촛불', 0.825663149356842), 
('생축', 0.818437933921814), 
('생파', 0.8172723054885864), 
('츤데레', 0.8124138712882996), 
('사위', 0.8108397126197815), 
('신난', 0.805475115776062), 
('추카', 0.8050897121429443), 
('효녀', 0.80231112241745), 
('생일날', 0.800576388835907), 
('함박웃음', 0.8002133965492249), 
('지우', 0.7995190024375916), 
('미역국', 0.7993987798690796), 
('결기', 0.798680305480957), 
('생일상', 0.7985363602638245), 
('울엄마', 0.7945799231529236), 
('장모님', 0.7941967844963074), 
('여동생', 0.7922881841659546), 
('내새', 0.790560781955719), 
('예지', 0.7883749008178711), 
('생일잔치', 0.7881664037704468), 
('꼬깔', 0.7872766256332397), 
('땡', 0.7872669696807861), 
('절친', 0.7869719862937927), 
('시후', 0.7859165668487549), 
('꼬맹이', 0.7849690318107605), 
('뽀뽀', 0.7847508192062378), 
('미안', 0.783918023109436), 
('엄니', 0.7833024263381958), 
('무니', 0.7831519842147827)]
```

 - 학습 결과만 놓고 보면 '개선되었다' 라고 보기는 조금 어려워보입니다. 비슷해 보이는 데이터도 제법 있고, "엄마", "생일" 이라는 키워드가 있는 문장에 쉽게 있을 법한 단어들이 상위권에 위치해 있습니다. 아무래도 중심 단어 근처에 많이 등장한 단어가 코사인유사도가 높을테니 어찌보면 당연한 결과입니다. 
 - 제가 원하는 건 크롤링 한 데이터 "엄마도 편하다며 좋아하는 고퀄잠옷😘" 에서 "엄마 고퀄 잠옷" 이라는 명사를 추출하고 엄마에게 줄 선물로 "잠옷" 이라는 단어가 상위권에 위치하게끔 하는 것입니다.
 - 데이터 양을 늘린다고 해도 이렇게 특수한 경우의 단어보다는 일반적인 단어가 더 많이 늘어나게 된다면 위의 결과와 크게 다르지는 않을 것 같습니다. 아무래도 개선을 위한 아이디어가 필요할 것 같습니다ㅠㅠ. 실제 데이터를 가지고 어디 한 번 쓸만한 모델을 만들어보자고 야심차게 시작했는데 역시 쉽지 않은 것 같습니다ㅎㅎ. 그래도 도전의식을 불러 일으키네요! 아직 시작한지 얼마 되지 않았으니 계속 데이터도 추가하고 어떻게 개선할 수 있을지 생각해보겠습니다.
 
 
### 개선 시도 - 1. 학습 데이터 정비하기
 - 학습의 결과를 확인해보니 미처 생각하지 못했던 부분들이 나왔습니다.
 - 일단, 전체 학습 문장 중에 선물이 포함되어 있는 문장이 생각보다 많지 않다는 점이었습니다. 모델 'rec_model_0917_100_5_3'의 학습 총 단어수는 25558 단어입니다. 선물과 여러 특징 데이터(선물 대상, 선물 목적 등)들의 관계가 잘 정비된 데이터로 학습한다면 전체 단어의 크기가 크게 중요하지 않을 수 있지만 제 접근 방법 자체가 데이터를 정비하는 시간을 최소화하고, 나온 결과를 적절히 필터링 하는 접근 방법을 선택했기 때문에 전체 단어 대비 선물 단어의 비율을 높일 필요가 있어 보입니다.
 - rec_model_0917_100_5_3 모델에서 ["생일", "엄마", "선물"]과 가장 코사인유사도가 높은 단어 300개를 시각화하면 아래와 같습니다.
 
 
 <p align="center">
 <image src="https://github.com/mu0gum/nlp_research/blob/master/images/Figure_0917_100_5_3.png">
 
 - 300개를 뽑아서 시각화를 했는데, 실제로 선물로 쓸 수 있는 단어가 '금일봉, 미역국' 정도 밖에 없어 보입니다. 확실히 이 상태로는 선물 추천 모델로 사용이 힘들어보입니다.
 - 첫 번째로 해볼 시도는 앞서 이야기한 것처럼 불필요한 학습 데이터를 줄이는 것입니다. 데이터를 늘리고 늘린 데이터에서 유의미한 내용을 추출하는게 흔히 말하는 빅데이터 분석이라는 요즘의 방법에 더 가깝다고 생각되지만 일단 할 수 있는 작은 부분부터 해보고 만약 틀렸다면 다른 방법을 또 찾아보겠습니다.
 - 크롤링한 데이터를 무조건 사용하지 않고, 크롤링한 데이터가 사전에 정의한 키워드 리스트 단어가 2개 이상 포함되는 경우만 학습시켜 보도록 하겠습니다. 추가한 코드는 아래와 같습니다.
 
 
```python
def isvalid_data(result_str):
    isvalid = False

    # result_str = ''.join(result)

    contain_keyword = []
    for keyword in keyword_results:

        if len(contain_keyword) > 1:
            isvalid = True
            break

        if keyword in result_str:
            contain_keyword.append(keyword)

    return isvalid
```
 
 - 위의 코드를 적용하여 학습한 문장의 수는 12400건 입니다. 10만 건에서 10분의 1로 줄었습니다. 정비된 데이터를 동일한 파라미터로 다시 학습해보겠습니다. 
 - 전에 했던 것과 마찬가지로 "엄마", "선물" 두 단어와 가장 코사인유사도가 높은 30개 단어를 뽑아보겠습니다.
 
```
[('조카', 0.907131552696228),
('찬스', 0.9039709568023682), 
('이모', 0.8954049348831177), 
('공주', 0.8933102488517761), 
('생선', 0.893258810043335), 
('남편', 0.8924819231033325), 
('애기', 0.8907347917556763), 
('삼촌', 0.8889564275741577), 
('고기', 0.8886284828186035), 
('아빠', 0.8882901668548584), 
('봉', 0.8872948884963989), 
('박싱', 0.8835185766220093), 
('울', 0.8828635811805725), 
('고마', 0.8824818134307861), 
('친정', 0.8820445537567139), 
('누나', 0.881851077079773), 
('알라딘', 0.8818258047103882), 
('미역국', 0.8814266324043274), 
('사준', 0.8810943365097046), 
('아내', 0.8810901641845703), 
('내사랑', 0.8797732591629028), 
('올해', 0.8793482780456543), 
('생일', 0.8782907724380493), 
('어제', 0.8778805732727051), 
('임신', 0.8768200874328613), 
('여보', 0.8767954707145691), 
('웡', 0.8766465187072754), 
('애', 0.8763511180877686), 
('식사', 0.876313328742981), 
('아가', 0.8757720589637756)]
```
 
 - 상위 30개 단어를 뽑아보았을 때는 전과 비교해서 그다지 개선된 것 같지는 않아 보입니다. 그렇다면 시각화한 결과는 어떤지 확인해보겠습니다. 아래는 전과 동일하게 ["생일", "엄마", "선물"]과 가장 코사인유사도가 높은 단어 300개를 시각화해본 결과입니다.
 

 <p align="center">
 <image src="https://github.com/mu0gum/nlp_research/blob/master/images/Figure_0925_100_5_3.png">
  
 - 선물로 바로 추천하기는 힘들 수도 있지만 유의미하다고 생각되는 단어가 '파자마, 립스틱, 제이에스티나, 몽블랑, 편지, 생일상, 미역국, 금일봉'이 나왔습니다. 이 전에 있던 '미역국, 금일봉' 보다는 훨씬 나은 결과가 나온 것 같습니다.
 - 그래도 아직 바로 쓰기에는 뭔가 비효율적인 것 같기도 하고 조금더 나은 결과를 얻고 싶습니다. 지금까지는 Word2Vec 모델을 학습할 때 하이퍼 파라미터를 크게 고려하지 않았는데 나름의 논리를 가지고 조금씩 수정하면서 결과가 어떻게 바뀌는지 확인해보겠습니다.
 

### 개선 시도 - 2. 하이퍼파라미터 변경
 - Word2Vec을 가지고 이것저것 해보거나 엄밀한 수학적 증명을 해보지 않아서 파라미터 설정을 어떻게 해야하는지 고민이 많았습니다. 따로 논문을 보면서 조사를 하기에는 시간이 부족하다고 생각되어 How do I determine Word2Vec parameters?(https://www.quora.com/How-do-I-determine-Word2Vec-parameters)의 내용을 참고해서 진행해보겠습니다. 위 포스팅에서 Word2Vec 하이퍼파라미터 관련 내용은 아래와 같습니다.
 
 

1. The model type (continuous bag of words - surrounding words predicting to word they flank. Skipgram - flanked word predicting all its surrounding words) skipgram typically is favored for large corpus

2. Sampling method ( hierarchical or negative ) again latter typically preferred for large corpus

3. Iterations - 5 or even as low as 3 for large corpus of 30 million unique words or more
4. Dimensions - 300 works for corpus of upto 60 million unique words
5. Subsampling - determines how often frequently occurring words like “the” are trained. Could be anywhere from 1e-3 to 1e-5. Values lower than 1e-5 tends to influence vector quality
6. Window size - smaller window size gives results that are more syntactic in nature. Larger window ( size > 5 ) gives results that are more semantic - this takes more training time given larger window size.

 
 
 - 모델을 개선하기 위해 하이퍼파라미터를 조금씩 변경해 보도록 하겠습니다. 일단 초기에 설정한 파라미터들은 100차원으로 단어를 임베딩하고, 윈도우크기는 5, 최소 반복 횟수는 3번, 학습은 1번 반복하고 Skip-gram을 사용했습니다. 일단 나온 데이터와 여러가지 상황을 종합해봤을 때 가장 먼저 변경해야 하는 건 학습의 반복 횟수처럼 보입니다. 학습하는 말뭉치의 양이 반복의 효과를 낼만큼 충분히 크지 않고, 오히려 지금은 학습하는 양 자체가 너무 부족하기 때문에 올바르게 임베딩을 한건지 의구심이 드는 것 같습니다. 그럼 나머지는 동일하게 하고 학습 횟수만 30회로 늘려서 모델을 비교해보겠습니다.
 - 그 전에 유사한 단어를 찾을 때 사용하는 단어에서 선물은 빼도록 하겠습니다. 선물은 여러 사람과 여러 목적에 포함되기 때문에 결과가 좀 더 일반적이지 않을까 생각됩니다. 앞으로는 학습한 모델에 검색할 때, [대상 + 목적] 위주로 하겠습습니다.
 - 아래는 동일한 파라미터에서 학습 횟수만 30회로 늘린 후, ["엄마", "생일"]로 검색했을 때, 코사인유사도가 높은 30개 단어입니다.
 
```
[('금일봉', 0.7177060842514038),
('웬수', 0.7129011750221252),
('다미', 0.7102757692337036),
('상차림', 0.7091253995895386),
('박서방', 0.7072010636329651),
('딸아', 0.705172061920166),
('다인', 0.7049171924591064),
('시아버님', 0.698712944984436),
('휴게소', 0.6978402137756348),
('권선민', 0.6975885629653931),
('다현', 0.6972560882568359),
('뽀뽀', 0.6970055103302002),
('수빈', 0.6966238021850586),
('와준', 0.6934833526611328),
('전야제', 0.6933735609054565),
('쳔', 0.691278874874115),
('주장', 0.6895673274993896),
('리온', 0.6883091330528259),
('서진', 0.6867287158966064),
('건우', 0.6847959756851196),
('함박웃음', 0.6844520568847656),
('아빠딸', 0.6826141476631165),
('생일상', 0.6817907094955444),
('오마니', 0.6804355978965759),
('대성공', 0.6786865592002869),
('형편', 0.6777249574661255),
('딱지', 0.6758014559745789),
('음력', 0.6754621267318726),
('하린', 0.6744040250778198),
('바라기', 0.6674615144729614)]
```

 - 가장 첫번째로 금일봉이라는 단어가 나왔는데 느낌에 신빙성이 좀 있어보이는 것 같습니다ㅎㅎ.300개 단어는 어떤지 확인해 보겠습니다.
 
 <p align="center">
 <image src="https://github.com/mu0gum/nlp_research/blob/master/images/Figure_0925_100_5_3.png">
 
 - 금일봉, 현금, 생활한복, 생일상, 사진첩 등이 보입니다. 괜찮아 보이기도 하고 아닌 것 같기도 하고 잘은 모르겠습니다.ㅎㅎ지금은 엄마, 생일로만 검색하는데 다른 단어들에 대해서도 확인을 해봐야 할 것 같습니다. 그 전에 앞으로 이런 작업이 계속 반복될 것 같은데 검증하는 로직을 좀 따로 만들어야 할 것 같습니다. 매번 일일이 확인하기는 힘들 것 같네요ㅎㅎ.다음에는 검증을 할 수 있는 프로그램을 만들어보고 다시 개선해보도록 하겠습니다.
 

### 개선 시도 - 3. 분석 프로그램 개발
 - 코드 참고(https://github.com/mu0gum/nlp_research/blob/master/presentalk/W2VRecommender.py) 
 - 일단 전체 단어의 빈도를 한 번 살펴보겠습니다. 단어의 빈도수를 내림차순으로 정렬한 데이터는 아래와 같습니다.

```
선물 32218
그램 11549
스타 10721
생일 9013
친구 5378
나 5220
일상 5110
케이크 4529
마카롱 4295
사랑 3354
데일리 3329
감사 3229
추석 3207
이벤트 3159
귀걸이 3028
꽃 2948
목걸이 2898
소통 2728
추천 2648
맛집 2591
여자친구 2527
반지 2519
행복 2294
카페 2240
맘 2236
럽 2183
기념일 2100
남자친구 1997
커플 1980
축하 1905

...


복달 1
마도 1
해밀턴 1
혜하 1
일주 1
크레타섬 1
카잔 1
자키스 1
묘지 1
선라이즈 1
카잔차키스 1
세서 1
리트 1
거름종이 1
등치 1
가리 1
심상 1
화동 1
이다은 1
해머 1
무신 1
재형 1
부우 1
꽃잔 1
이영미 1
꽃바지 1
로이즈 1
깨금 1
조각가 1
```

 - 일단 무작정 데이터를 뽑아보기는 했는데, 뽑은 데이터로 뭘 하면 좋을지 고민하다가 하이퍼파라미터 중에 min_count를 수정할 수 있지 않을까 생각해보았습니다. 단어의 등장 횟수가 1번인 데이터 중에서 "해밀턴" 같은 시계 브랜드도 포함이 되어 있지만 빈도가 1번이라는 건 그만큼 많은 사람들이 추천하지는 않다는 이야기기 때문에 학습에서 제외 시켜도 큰 문제는 없을 것 같습니다. (반대로 사람들이 많이 하는 선물 말고 특이한 선물을 원하는 경우에 사용할 수 있는지 고민해볼 만하다고 생각도 되네요.)
 - 지금 당장은 학습 문장도 많지 않기 때문에 min_count를 3 그대로 유지하겠습니다. 학습 데이터를 늘리고 나서는 다시 검증 프로그램을 돌려서 적절한 min_count를 찾아보도록 하겠습니다.
 
 - 선물 단어의 등장 빈도는 아래와 같습니다.
 
```
귀걸이 3028
목걸이 2898
반지 2519
팔찌 1690
모자 638
에어팟 603
석고방향제 405
홍삼 352
텀블러 335
양말 277
스니커즈 268
아디다스 262
니트 219
캐리어 204
발찌 198
다이어리 155
책갈피 152
마사지기 151
아이패드 142
머그컵 139
플래너 132
토트백 112
가디건 112
정장 105
숄더백 104
장갑 100
노트북 99
유모차 99
넥타이 81
셔츠 68
비니 68
스카프 68
선글라스 67
소주잔 62
제이에스티나 55
손수건 52
워커 49
청바지 48
벨트 48
로퍼 47
키홀더 47
코스터 45
록시땅 44
샌들 41
반바지 36
브레이슬릿 31
수영복 26
보스턴백 25
단화 23
맥주잔 15
조이스틱 14
모니터 13
저금통 13
우쿨렐레 12
프린트 11
스키니 9
우주복 9
무지 8
드론 8
머플러 8
슬랙스 7
테이핑 6
생활한복 6
블렌더 6
스웨터 4
사파리 3
면바지 3
독서대 3
무스탕 2
덧신 2
보넷 2
린넨셔츠 2
석류스틱 1
모피 1
민소매 1
```

 - 대상 단어의 등장 빈도는 아래와 같습니다. 지금은 테스트용으로 대상을 6개로 정했습니다.

```
친구 5378
여자친구 2527
남자친구 1997
엄마 1277
아빠 482
동생 448
```
 
 - 목적 단어의 등장 빈도는 아래와 같습니다. 목적도 마찬가지로 일단 6개로 정했습니다.
 
 ```
생일 9013
기념일 2100
결혼 698
집들이 490
졸업 97
취업 32
 ```
 
 - 제가 최종적으로 원하는 결과를 도출하려면 대상 단어와 목적 단어의 조합으로 상위 3개의 선물을 찾는 것 입니다. 기존 개발한 모델로 검증을 돌려보겠습니다.
 
```
대상 : 여자친구, 목적 : 생일, 결과 : ['비치백', '용돈', '로에베']
대상 : 여자친구, 목적 : 기념일, 결과 : ['비치백', '로단테', '이스트우드']
대상 : 여자친구, 목적 : 집들이, 결과 : ['비치백', '이스트우드', '로단테']
대상 : 여자친구, 목적 : 취업, 결과 : ['키플링', '비치백', '듀퐁']
대상 : 여자친구, 목적 : 졸업, 결과 : ['꽃다발', '로단테', '종이꽃']
대상 : 여자친구, 목적 : 결혼, 결과 : ['비치백', '듀퐁', '로단테']
대상 : 남자친구, 목적 : 생일, 결과 : ['용돈', '카시오', '질스튜어트']
대상 : 남자친구, 목적 : 기념일, 결과 : ['비치백', '카시오', '용돈']
대상 : 남자친구, 목적 : 집들이, 결과 : ['비치백', '이스트우드', '카시오']
대상 : 남자친구, 목적 : 취업, 결과 : ['카시오', '키플링', '듀퐁']
대상 : 남자친구, 목적 : 졸업, 결과 : ['꽃다발', '용돈', '듀퐁']
대상 : 남자친구, 목적 : 결혼, 결과 : ['비치백', '카시오', '듀퐁']
대상 : 엄마, 목적 : 생일, 결과 : ['비치백', '용돈', '키플링']
대상 : 엄마, 목적 : 기념일, 결과 : ['비치백', '용돈', '키플링']
대상 : 엄마, 목적 : 집들이, 결과 : ['비치백', '종이꽃', '키플링']
대상 : 엄마, 목적 : 취업, 결과 : ['키플링', '비치백', '용돈']
대상 : 엄마, 목적 : 졸업, 결과 : ['꽃다발', '용돈', '종이꽃']
대상 : 엄마, 목적 : 결혼, 결과 : ['비치백', '키플링', '용돈']
대상 : 아빠, 목적 : 생일, 결과 : ['용돈', '비치백']
대상 : 아빠, 목적 : 기념일, 결과 : ['비치백', '용돈', '키플링']
대상 : 아빠, 목적 : 집들이, 결과 : ['비치백']
대상 : 아빠, 목적 : 취업, 결과 : ['키플링', '비치백']
대상 : 아빠, 목적 : 졸업, 결과 : ['꽃다발']
대상 : 아빠, 목적 : 결혼, 결과 : ['비치백']
대상 : 친구, 목적 : 생일, 결과 : ['조르지오아르마니', '생활한복', '질스튜어트']
대상 : 친구, 목적 : 기념일, 결과 : ['비치백']
대상 : 친구, 목적 : 집들이, 결과 : ['소주잔', '비치백']
대상 : 친구, 목적 : 취업, 결과 : ['사파리']
대상 : 친구, 목적 : 졸업, 결과 : ['꽃다발']
대상 : 친구, 목적 : 결혼, 결과 : ['비치백', '록시땅']
대상 : 동생, 목적 : 생일, 결과 : ['용돈', '조르지오아르마니', '비치백']
대상 : 동생, 목적 : 기념일, 결과 : ['비치백', '용돈', '꽃다발']
대상 : 동생, 목적 : 집들이, 결과 : ['비치백']
대상 : 동생, 목적 : 취업, 결과 : ['용돈']
대상 : 동생, 목적 : 졸업, 결과 : ['꽃다발', '용돈']
대상 : 동생, 목적 : 결혼, 결과 : ['비치백', '용돈']
```
 
 - 대상과 목적의 조합이 맞지 않는 항목들은 추후에 제거해줄 예정입니다. 일단은 전체를 보고 분석하기 위해 모든 조합의 결과로 확인해보겠습니다.
 - 대상과 목적만으로 유사도를 구하다보니 대상이나 목적이 동일할 때 비슷한 결과가 나오는 경향이 조금 있는 것 같습니다.
 ex) (여자친구, 생일 & 남자친구, 생일) -> 용돈, (여자친구, 생일 & 여자친구, 기념일) -> 비치백 등
 - 비치백이라는 단어가 많이 나왔는데 학습 데이터에서 특이사항이 있는지 확인을 좀 해봐야 할 것 같습니다. 이러한 형태의 결과는 학습 데이터가 많아진다면 자연스럽게 해결되지 않을까 생각합니다.
 - 그래도 (동생, 졸업식)에 꽃다발, (친구, 집들이)에 소주잔이 결과로 나온 것은 상황에 맞는 것처럼 보입니다.
 - 지금 계속 쌓이고 있는 학습 데이터를 추가하고 다시 검증 프로그램을 돌려서 확인해보겠습니다. 그래도 개선하면 어느정도 추천 모델로 사용할 수 있겠다는 생각이 드네요ㅎㅎ.
 
 
