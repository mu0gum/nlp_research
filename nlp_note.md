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


위 식에서 <img src="https://latex.codecogs.com/gif.latex?P%28p%29" /> 는 긍정인 문장의 개수를 전체 문장의 개수로 나눈 값입니다. <img src="https://latex.codecogs.com/gif.latex?P%28S%7Cp%29" /> 는 우도(likehood) 입니다. 앞서 설명한대로 베이즈 모델은 <img src="https://latex.codecogs.com/gif.latex?P%28p%7CS%29P%28p%29/P%28S%29" /> 와 <img src="https://latex.codecogs.com/gif.latex?P%28n%7CS%29P%28n%29/P%28S%29" /> 를 비교해 큰 쪽으로 범주를 할당합니다. <img src="https://latex.codecogs.com/gif.latex?P%28S%29" /> 는 공통이기 때문에 계산을 생략할 수 있습니다. 생략한 식은 아래와 같습니다. (참고로 ∝ 는 proportionality sign 이라고 부르고, A ∝ B 는 'A는 B에 비례한다' 는 뜻입니다.)


<img src="https://latex.codecogs.com/gif.latex?P%28p%7CS%29%20%5Cpropto%20P%28S%7Cp%29P%28p%29" />





