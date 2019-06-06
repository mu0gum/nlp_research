# 자연어 처리 관련 알고리즘 +@(수학  정리)
- 챗봇을 개발하는데 필요한 자연어 처리 관련 기술들에 대한 내용을 정리하고, 더해서 수학적인 내용도 정리해 보려고 합니다. 기본적으로는 챗봇에서 적용
하려고 하는 부분에 대해서 정리하겠습니다.
- 개인 공부 및 기록 용도이기 대문에 알고리즘이나 개념, 수학적인 내용은 제가 이해하는 수준에서만 기술하고 실제로 챗봇에 적용하는 부분에 대해서 이야기
하겠습니다.


## 00. 나이브 베이즈 분류
### 참고
1. 가장 쉽게 이해하는 베이즈 정리(Bayes' Law) (https://junpyopark.github.io/bayes/)
2. 나이브 베이즈 분류기 (https://ratsgo.github.io/machine%20learning/2017/05/18/naive/)

- 나이브 베이즈 분류는 제가 만든 챗봇이 무언가를 제안했을 때, 그에 대한 응답이 긍정이나 부정이냐를 분류하기 위해 적용한 내용입니다.
- 나이브 베이즈 분류는 스팸 메일을 필터링 하는데 좋은 효율을 보인다고 합니다. 스팸 메일을 필터는 메일 내용을 보고 스팸이냐 아니냐를 구분하는 것인데
이것을 응용하여, 사용자의 대답이 긍정이냐, 부정이냐를 분류해 보겠습니다.

### 조건부 확률
조건부 확률은 어떤 사건 B가 발생했을 때, 사건 A가 발생할 확률을 의미합니다. ( <img src="https://latex.codecogs.com/gif.latex?P%28B%29%20%3E%200" /> 으로 가정 )


<img src="https://latex.codecogs.com/gif.latex?P%28A%7CB%29%3D%5Cfrac%7BP%28A%5Ccap%20B%29%7D%7BP%28B%29%7D" />

마찬가지로, 사건 A가 발생했을 때, 사건 B가 발생할 확률은 ( <img src="https://latex.codecogs.com/gif.latex?P%28A%29%20%3E%200" /> 으로 가정 )


<img src="https://latex.codecogs.com/gif.latex?P%28B%7CA%29%3D%5Cfrac%7BP%28B%5Ccap%20A%29%7D%7BP%28A%29%7D" />


이고, 두 식을 정리해서 아래와 같이 표현할 수 있습니다.


<img src="https://latex.codecogs.com/gif.latex?P%28A%5Ccap%20B%29%3DP%28A%7CB%29P%28B%29%3DP%28B%7CA%29P%28A%29" />


위의 식을 가지고, 사건 B가 발생했을 때 사건 A가 발생할 확률에 대해 정리해보면


<img src="https://latex.codecogs.com/gif.latex?P%28A%7CB%29%3D%5Cfrac%7BP%28B%7CA%29P%28A%29%7D%7BP%28B%29%7D" />


라는 식이 나오게 되고, 위의 식을 일반적으로 **베이즈 정리**라고 합니다. 위의 내용은 참고1 에서 공부한 부분으로, 자세한 정리는 참고1 을 확인 하시면 좋을 것 같습니다.


그럼 저의 목표인 문장이 긍정이냐 부정이냐를 분류하는 것과 베이즈 정리가 어떤 관련이 있을까요?
위의 식에서의 핵심은 **A가 발생했을 때, B가 발생할 확률을 거꾸로 B가 발생했을 때, A가 발생할 확률을 사용해 계산할 수 있다**는 점입니다.
제가 구하고 싶은 답은 문장 S가 주어졌을 때, 그 문장이 긍정일 확률 <img src="https://latex.codecogs.com/gif.latex?P%28p%7CS%29" /> 와 
문장 S가 주어졌을 때, 그 문장이 부정일 확률 <img src="https://latex.codecogs.com/gif.latex?P%28n%7CS%29" /> 을 비교하여 더 큰 쪽을 찾는 것 입니다. ( 아래의 내용은 참고2 의 내용을 학습하고 정리하였습니다. 자세한 내용은 참고2를 확인하시면 좋을 것 같습니다. )


언뜻 생각해보면 문장이 주어졌을 때, 이 문장이 긍정일 확률을 구하라고 하면 굉장히 막연하게 느껴집니다. 하지만 위의 식을 베이즈 정리를 이용해서 표현해보면 아래와 같습니다.


<img src="https://latex.codecogs.com/gif.latex?P%28p%7CS%29%3D%5Cfrac%7BP%28S%7Cp%29P%28p%29%7D%7BP%28S%29%7D" />


위 식에서 <img src="https://latex.codecogs.com/gif.latex?P%28p%29" /> 는 긍정인 문장의 개수를 전체 문장의 개수로 나눈 값입니다. <img src="https://latex.codecogs.com/gif.latex?P%28S%7Cp%29" /> 는 우도(likehood) 입니다. 앞서 설명한대로 베이즈 모델은 <img src="https://latex.codecogs.com/gif.latex?P%28p%7CS%29P%28p%29/P%28S%29" /> 와 <img src="https://latex.codecogs.com/gif.latex?P%28n%7CS%29P%28n%29/P%28S%29" /> 를 비교해 큰 쪽으로 범주를 할당합니다. <img src="https://latex.codecogs.com/gif.latex?P%28S%29" /> 는 공통이기 때문에 계산을 생략할 수 있습니다. 생략한 식은 아래와 같습니다. ( 참고로 ∝ 는 proportionality sign 이라고 부르고, A ∝ B 는 'A는 B에 비례한다' 는 뜻입니다. )


<img src="https://latex.codecogs.com/gif.latex?P%28p%7CS%29%20%5Cpropto%20P%28S%7Cp%29P%28p%29" />


위의 식에서 문장 S가 단어 w1, w2 로 이루어졌다고 생각하고 식을 정리해보면


<img src="https://latex.codecogs.com/gif.latex?P%28p%7CS%29%5Cpropto%20P%28w_1%2Cw_2%7Cp%29P%28p%29" />


위의 식이 됩니다. 나이브 베이즈 분류는 각 단어가 **독립(independent)** 임을 가정합니다. 그리고 naive(순진한) 라는 말이 이유가 붙은 이유기도 합니다. (참고2) 독립임을 가정 <img src="https://latex.codecogs.com/gif.latex?P%28w_1%2Cw_2%29%3DP%28w_1%29%5Ccdot%20P%28w_2%29" /> 하고 다시 식을 정리해보면


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


<img src="https://latex.codecogs.com/gif.latex?P%28p%7CS%29%5Cpropto%20P%28w_1%7Cp%29%5Ccdot%20P%28w_2%7Cp%29%5Ccdot%20P%28p%29" />

일단 문장이 긍정일 확률은 전체 6개의 문장 중에서 4개가 긍정이므로, <img src="https://latex.codecogs.com/gif.latex?P%28p%29%3D%5Cfrac%7B4%7D%7B6%7D%3D%5Cfrac%7B2%7D%7B3%7D" /> 입니다. 

그리고 긍정인 문장에서 w1 = 응 이라는 단어가 있을 확률은 <img src="https://latex.codecogs.com/gif.latex?P%28w_1%7Cp%29%3D%5Cfrac%7B1%7D%7B7%7D" /> , 긍정인 문장에서 w2 = ㅋㅋ 라는 단어가 있을 확률도 <img src="https://latex.codecogs.com/gif.latex?P%28w_2%7Cp%29%3D%5Cfrac%7B1%7D%7B7%7D" /> 입니다. 이제 구한 확률을 가지고 위의 식에 대입해 보면


<img src="https://latex.codecogs.com/gif.latex?P%28p%7CS%29%5Cpropto%20%5Cfrac%7B1%7D%7B7%7D%5Ccdot%20%5Cfrac%7B1%7D%7B7%7D%5Ccdot%20%5Cfrac%7B2%7D%7B3%7D%20%3D%20%5Cfrac%7B2%7D%7B147%7D" />


위의 결과가 나옵니다. "응ㅋㅋ"라는 문장이 긍정일 확률은 2/147 입니다. 같은 방법으로 "응ㅋㅋ"라는 문장이 부정일 확률을 구해보겠습니다.


<img src="https://latex.codecogs.com/gif.latex?P%28n%29%3D%5Cfrac%7B2%7D%7B6%7D%3D%5Cfrac%7B1%7D%7B3%7D%2C%20p%28w_1%7Cn%29%3D%5Cfrac%7B0%7D%7B3%7D%2C%20P%28w_2%7Cn%29%3D%5Cfrac%7B1%7D%7B3%7D" />


<img src="https://latex.codecogs.com/gif.latex?P%28n%7CS%29%3D%5Cfrac%7B1%7D%7B3%7D%5Ccdot%20%5Cfrac%7B0%7D%7B3%7D%5Ccdot%20%5Cfrac%7B1%7D%7B3%7D%3D0" />


문장 S가 주어졌을 때, 긍정일 확률과 부정일 확률을 나이브 베이즈 정리를 이용해 구했습니다. 


<img src="https://latex.codecogs.com/gif.latex?P%28p%7CS%29%3D%5Cfrac%7B2%7D%7B147%7D%2C%20p%28n%7CS%29%3D0" />


문장이 긍정일 확률이 더 크네요. "응ㅋㅋ"는 긍정으로 분류 되었습니다. 분류가 잘 된 것 같지만 몇 가지 문제가 존재합니다.


1. 단어 "응" 이 부정일 확률 <img src="https://latex.codecogs.com/gif.latex?p%28w_1%7Cn%29%20%3D%20%5Cfrac%7B0%7D%7B3%7D%20%3D%200" /> 이
0 되어서 결과를 무조건 0 으로 만들어 버립니다.


-> 이 경우에는 적절히 작은 수 k 를 더해서 분자가 0 이 되는 것을 피하게(smoothing) 합니다. k = 1 이라고 하고 다시 계산해 보면
 
 
 <img src="https://latex.codecogs.com/gif.latex?p%28p%7CS%29%3D%5Cfrac%7B1&plus;k%7D%7B7%7D%5Ccdot%20%5Cfrac%7B1&plus;k%7D%7B7%7D%5Ccdot%20%5Cfrac%7B2%7D%7B3%7D%3D%5Cfrac%7B6%7D%7B147%7D%28%5Cbecause%20k%3D1%29" />
 
 
 
<img src="https://latex.codecogs.com/gif.latex?p%28n%7CS%29%3D%5Cfrac%7B1&plus;k%7D%7B3%7D%5Ccdot%20%5Cfrac%7B0&plus;k%7D%7B3%7D%5Ccdot%20%5Cfrac%7B1%7D%7B3%7D%3D%5Cfrac%7B2%7D%7B27%7D%28%5Cbecause%20k%3D1%29" />


위의 결과가 나오게 됩니다.


2. 두번째 문제는 위의 결과에서 확인할 수 있습니다. "응ㅋㅋ" 에서 응, ㅋㅋ는 모두 긍정 단어에 존재하고, 부정 단어에는 ㅋㅋ만 존재합니다. 그런데, 위의 표에서 긍정 단어의 수는 7개 이고, 부정 단어의 수는 3개 입니다. 긍정 단어의 수와 부정 단어의 수가 약 2배 차이가 나서, 오히려 부정일 확률을 높게 만들었습니다. 



제가 공부한 사이트에서의 예제는 영화의 리뷰와 평점 데이터를 가지고 긍정/부정을 분류하였습니다. 리뷰는 제 챗봇이 입력받는 대답에 비해 더 많은 단어를 가지고 있고, 사전에 정리된 데이터의 양도 많아 충분히 훌륭히 분류를 하고 있습니다. 하지만 제가 만드는 챗봇에서 바로 사용하기에는 무리가 있어 보입니다. 


현재 만들고 있는 챗봇에 적용할 수 있도록 개선하면, 참고 코드는 그 때 올리도록 하겠습니다. 나이브 베이즈 정리에 대한 내용은 일단 이정도로 마치겠습니다. 



