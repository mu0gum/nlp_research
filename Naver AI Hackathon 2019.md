# Naver AI Hackathon 2019(Speech Recognition) 준비
 - 네이버 2019 AI Hackathon 신청을 하였습니다. 해커톤은 실력있는 사람들만 나가는 것이라고 생각하고 평범한 나와는 상관없는 일이라고 생각해왔는데, 제가 진심으로 좋아하고 도전하고 싶어하는 딥러닝과 자연어처리 분야를 공부하다 보니 목표가 생긴건지 간절함이 있는건지 일단 신청하게 되었습니다. 서류에서 100팀만 걸러진다는데, 과연 그 안에 들 수 있을지는 모르겠지만..어차피 도전한거 서류발표 전까지는 음성인식에 대해 전반적인 내용을 공부하고, 논문들도 찾아보면서 어떤 모델이 제가 잘 이해하고 적용할 수 있을지 찾아보도록 하겠습니다.

## 음성인식 개요
### 출처 및 참고
1. [카카오AI리포트]음성인식 방법과 카카오i의 음성형엔진 (https://brunch.co.kr/@kakao-it/105)
2. 기계 학습(Machine Learning, 머신 러닝)은 즐겁다! Part 6 (https://medium.com/@jongdae.lim/%EA%B8%B0%EA%B3%84-%ED%95%99%EC%8A%B5-machine-learning-%EC%9D%80-%EC%A6%90%EA%B2%81%EB%8B%A4-part-6-eb0ed6b0ed1d)
3. 은닉마코프모델(Hidden Markov Models) (https://ratsgo.github.io/machine%20learning/2017/03/18/HMMs/)


 - 음성인식은 입력된 음성이 어떤 단어들로 이루어져 있을 확률이 높은지를 찾는 문제
 - 일반적인 음성인식 아키텍처는 아래와 같음
 
 
 <p align="center">
 <img height="400px" src="https://slideplayer.com/slide/7248751/24/images/9/Speech+Recognition+Architecture.jpg"/>
 
 
 - 문제 : **'일정 길이 T 동안 입력된 음성 sequence X 에 대해서 인식기가 표현할 수 있는 모든 단어들의 조합 중 확률적으로 가장 가능성이 높은 단어열 W는 무엇인가?'** [출처1 인용] 
 - N개의 단어들로 이루어진 문장을 <img src="https://latex.codecogs.com/gif.latex?%5Cvec%7BW%7D%3DW_%7B1%7D%2CW_%7B2%7D%2C%5Ccdots%20%2CW_%7Bn%7D"/>, 일정간격으로 추출한 T개의 음성 특징 벡터를 <img src="https://latex.codecogs.com/gif.latex?%5Cvec%7BX%7D%3DX_%7B1%7D%2CX_%7B2%7D%2C%5Ccdots%20%2CX_%7Bt%7D"/>라고 할 때 위 문제를 수식으로 표현하면 아래와 같음
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?%5Cunderset%7BW%7D%7Bargmax%7DP%28W%7CX%29%3D%5Cunderset%7BW%7D%7Bargmax%7D%5Cfrac%7BP%28X%7CW%29P%28W%29%7D%7BP%28X%29%7D%3D%5Cunderset%7BW%7D%7Bargmax%7DP%28X%7CW%29P%28W%29"/>

 - P(X|W)는 **음향모델 확률**로 W라는 단어를 발성했을 때 X라는 신호적 특성이 나타날 확률
 - P(W)는 **언어모델**로 음성신호 특징에 해당하는 X가 없음 => 음성신호와 관계없이 그 음성이 뭐라고 예측하는 값으로 어떤 단어가 말해질 확률을 미리 가지고 있음
- 일반적으로 P(W)는 대량의 텍스트 말뭉치로부터 단어의 발생 빈도를 계산하여 구함
- 음성인식 과정은 크게 **음성분석, 음향모델 계산, 언어모델 계산, 디코딩**의 4단계로 나눌 수 있음

 
 <p align="center">
 <img src="https://miro.medium.com/max/1140/0*YwlJRwnb30jMsvaL.png"/>


### 음성분석
 - 음성분석은 음성신호에서 주파수 분석을 통해 음성의 특징되는 부분을 추출하는 과정
 - 음파(sound waves)는 1차원으로 시간의 흐름 속 매 순간마다 음파의 높이를 기준으로 한 단일값을 가짐
 - 음파를 숫자로 표현하기 위해서는, 파동의 높이를 등간격의 좌표값으로 저장
 
 
 <p align="center">
 <img src="https://miro.medium.com/max/1000/1*PkvxKtomXS4sR4HzMVL8gA.gif"/>


 - 이러한 과정을 샘플링(sampling)이라고 함 -> 초당 수천번을 읽어들여서 그 시점의 음파 높이를 숫자로 저장
 - 샘플링은 데이터의 일부만을 추출하기 때문에 원래에 음파에 대한 대략적인 근사치를 만드는 것이기 때문에 원본과 차이가 있어 데이터 유실이 발생
 - 하지만 **Nyquist 정리** 덕분에, 기록하고자하는 가장 높은 주파수의 최소 두 배 빠르게 샘플을 추출한다면, 간격이 생긴 샘플로부터 원래의 주파수를 수학적으로 완벽하게 재구성해 사용 가능
 
 
 - 음성은 짧은 구간(보통 0.02초) 동안의 주기적인 특성(quasi-stationary)으로 가정하고, 이 단위로 음성을 분석하여 소리가 만들어진 상태를 예측
 - 0.02초 길이의 음성 파형을 어떤 주파수적인 특성을 갖는지 분석하는 등 여러 단계의 신호처리 과정을 거쳐 수십개의 숫자들로 표현 => 특징 벡터
 
 
### 음향분석
 - 음향모델링은 음성을 0.02초 구간을 0.01초씩 시간축에 따라 움직이며 따라 만든 특징 벡터열 X와 어휘 셋 W에 대해 P(X|W) 확률을 학습하는 과정
 - 고전적인 음성인식은 음소를 GMM(Gaussian Mixture Model)으로 모델링하고 이 음소들의 연속적 변화를 HMM(Hidden Markov Model)으로 예측하는 GMM-HMM 방식
 - GMM 확률 모델 부분만을 딥러닝으로 대체하는 방법과 HMM으로 음성을 예측하는 부분까지 포함하여 신경망으로 대체한 종단 간(end-to-end) 방식으로 음성인식을 연구하는 많은 시도가 있음
 - 종단 간 방식은 기존 음성인식 구현을 위해 필요한 신호처리, 발음변환, 언어모델, 디코딩 단계의 전문적인 지식이 개입하는 것을 최소화하면서 이 부문의 모델링을 신경망이 학습하도록 함으로써 뛰어난 성능을 보임
 
 <p align="center">
 <img src="https://miro.medium.com/max/1274/0*UOnCnowb70okNHbt.png"/>
 

### 언어모델
 - 언어모델은 방대한 텍스트를 분석해 모델을 만들어 현재 인식되고 있는 단어들 간의 결합 확률을 예측하는 과정
 - 언어모델은 특정 단어 다음에 나올 단어의 확률 추정이 이루어짐
 - 언어모델은 단어들 간의 관계를 확률로 나타내어 서로 관계가 높은 단어들의 결합 가능성을 높이는 역할을 함
 - 언어모델을 이용하면, 발음이 비슷한 단어가 많거나 불분명하게 발음되어 음향모델로만 판단했을 때 잘못된 인식이 발생할 위험을 낮춤


### 디코딩
 - 음향모델과 언어모델로 구성된 탐색 공간에서 가장 최적인 경로를 찾는 과정
 - 음성이 어떤 단어열을 나타내는지를 추정
 - 문장을 이룰 단어의 개수와 각 단어의 경계에 제한을 두지 않고 탐색하는 것으로 그 경우의 수가 큼
 

### 마무리
 - 음성인식에 대한 개요는 위 내용까지만 정말 간단하게 알아보고 직접 모델을 구현해보면서 필요한 내용을 추가하도록 하겠습니다. 개요를 정리하면서 음성인식에 최신 기법들을 알어보려고 논문도 훑어보고 있는데, 아직은 무슨 내용인지 잘 모르겠습니다..ㅎㅎ 하지만 처음 챗봇을 만들었던 때를 떠올려보면 그 때도 처음에는 이게 무슨 말인가 싶었는데 계속 보다보니 조금씩이나마 이해가 됐던 것 같습니다. 마찬가지로 일단은 계속 반복해서 볼 생각입니다. 아무래도 음성인식에 대한 사전지식이 많이 부족한 상태에서는 종단 간(end to end) 방식을 우선순위에 두어야 할 것 같습니다. 그래도 모델을 개선하기 위해 필요하다고 생각되는 내용은 계속 공부할 계획입니다. 지금 정리하려고 하는 은닉마르코프모델도 자연어처리 분야를 공부하면서 많이 들어봤지만 따로 정리한적이 없었는데 이번 기회에 한 번 정리해보도록 하겠습니다. 마르코프 체인 관련 내용은 출처3을 참고하였습니다. 해당 블로그에 올라와있는 내용들이 너무 좋아서 제 깃허브에 따로 공부 용도로 정리를 해도 되냐고 물었는데 흔쾌히 허락해 주셨습니다. 다시 한 번 감사드립니다.
 

## 은닉마르코프모델(Hidden Markov Models, HMMs)
 - 은닉마르코프모델은 순차적인 데이터를 다루는 데 강점을 지녀 개체명 인식, 포스태깅 등 단어의 연쇄로 나타나는 언어구조 처리에 과거 많은 주목을 받았던 기법


### 마르코프 체인(Markov chain)
 - 은닉마르코프모델은 마르코프 체인을 전제로 한 모델
 - 마르코프 체인이란 마르코프 성질(Markov Property)을 지닌 이산확률과정(discrete-time stochastic process)
 - 수학자 마코프가 1913년경에 러시아어 문헌에 나오는 글자들의 순서에 관한 모델을 구축하기 위해 제안
 - **한 상태의 확률은 단지 그 이전 상태에만 의존**한다는 것이 마르코프 체인의 핵심
 - 한 상태에서 다른 상태로의 전이(transition)는 그동안 상태 전이에 대한 긴 이력(history)을 필요로 하지 않고 바로 직전 상태에서의 전이로 추정할 수 있음
 - 아래와 같이 도식화 가능
 
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?P%28q_%7Bi%7D%7Cq_%7Bi-1%7D%2C%5Ccdots%20%2Cq_%7B1%7D%29%3DP%28q_%7Bi%7D%7Cq_%7Bi-1%7D%29"/>
 
 
### 마르코프 체인 예시
 - 날씨를 마르코프 체인으로 모델링한 예시는 아래 그림과 같음
 - 각 노드는 상태, 엣지는 전이를 가리킴
 - <img src="https://latex.codecogs.com/gif.latex?a_%7Bij%7D"/>는 i번째 상태에서 j번째 상태로 전이될 확률
 - 각 노드별로 전이확률의 합은 1 ( 예, <img src="https://latex.codecogs.com/gif.latex?a_%7B01%7D&plus;a_%7B02%7D&plus;a_%7B03%7D%3D1"/> )
 - 상태는 일반적인 상태(HOT, COLD, WARM) 외에 시작(start) 끝(end) 상태도 있음
 
 <p align="center">
 <img height="300px" src="https://i.imgur.com/iCPKPWz.png"/>
 
 
### 은닉 마르코프 모델
 - 은닉마르코프모델은 각 상태가 마르코프체인을 따르되 은닉(hidden)되어 있다고 가정
 - 예를들면, 100년 전 기후를 연구하는데 주어진 정보는 당시 아이스크림 소비 기록뿐일 때, 이 정보만으로 날씨가 추웠는지, 더웠는지, 따듯했는지를 알고싶은 것
 - 아이스크림 소비 기록은 연쇄를 관찰할 수 있지만, 해당 날씨가 어땠는지는 직접적으로 관측하기 어려움
 - 은닉마르코프모델은 이처럼 관측치 뒤에 은닉되어 있는 상태(state)를 추정
 - 날씨를 예시로 은닉마르코프모델을 도식화한 그림은 아래와 같음


 <p align="center">
 <img height="300px" src="https://i.imgur.com/lEMDGBC.png"/>


 - 위 그림에서 <img src="https://latex.codecogs.com/gif.latex?B_%7B1%7D"/>은 날씨가 더울 때 아이스크림을 1개 소비할 확률이 0.2, 2개 소비할 확률이 0.4, 3개 소비할 확률이 0.4 라는 것을 나타냄
 - <img src="https://latex.codecogs.com/gif.latex?B_%7B1%7D"/>은 날씨가 더울 때 조건부확률이므로 HOT이라는 은닉상태과 연관이 있음
 - B는 방출확률(emission probability)이라고도 불림
 

### Likelihood
 - 우도(likehood)는 모델 <img src="https://latex.codecogs.com/gif.latex?%5Clambda"/>가 주어졌을 때 관측치 <img src="https://latex.codecogs.com/gif.latex?O"/>가 나타날 확률 <img src="https://latex.codecogs.com/gif.latex?P%28O%7C%5Clambda%29"/>를 가르킴 => 모델 <img src="https://latex.codecogs.com/gif.latex?%5Clambda"/>가 관측치 하나를 뽑았는데 그 관측치가 <img src="https://latex.codecogs.com/gif.latex?O"/>일 확률
 - 위의 경우에서 관측된 <img src="https://latex.codecogs.com/gif.latex?O"/>가 아이스크림 [3개, 1개, 3개]라고 가정
 - 모델 <img src="https://latex.codecogs.com/gif.latex?%5Clambda"/>가 위 그림일 때 이 <img src="https://latex.codecogs.com/gif.latex?O"/>가 뽑힐 확률은? => 이 것을 계산해보자는 것
 
 
 <p align="center">
 <img src="https://i.imgur.com/syZWL5E.png"/>
 
 
 - 위 그림에서 두번째 날짜를 중심으로 모델 <img src="https://latex.codecogs.com/gif.latex?%5Clambda"/>를 보면 날씨가 더울 때(hot) 아이스크림을 1개 먹을 확률은 0.2
 - 두번째 날이 전날에 이어 계속 더울 확률은 0.6이므로 이를 곱해주어야 둘째날의 상태확률 계산 가능
 - 마르코프체인을 따른다고 가정하므로 상태확률을 계산할 때는 직전 상태만을 고려
 - 위 그림을 식으로 나타내면 다음과 같음
 
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?%5C%5CP%283%5C%3B%201%5C%3B%203%2C%5C%3B%20hot%2C%5C%3B%20hot%2C%5C%3B%20cold%29%5C%5C%5C%5C%20%3DP%28hot%7Cstart%29%5Ctimes%20P%28hot%7Chot%29%5Ctimes%20P%28cold%7Chot%29%5Ctimes%20P%283%7Chot%29%5Ctimes%20P%281%7Chot%29%5Ctimes%20P%283%7Ccold%29%5C%5C%5C%5C%20%3D0.8%5Ctimes%200.6%5Ctimes%200.3%5Ctimes%200.4%5Ctimes%200.2%5Ctimes%200.1"/>
 
 
 - 각 날짜별로 날씨가 더울 수도 있고 추울 수도 있기 때문에 <img src="https://latex.codecogs.com/gif.latex?2%5E3"/> 가지의 경우의 수 존재
 
 | 상태1 | 상태2 | 상태3 |
 | - | - | - |
 | cold | cold | cold |
 | cold | cold | hot |
 | cold | hot | cold |
 | hot | cold | cold |
 | hot | hot | cold |
 | cold | hot | hot |
 | hot | cold | hot |
 | hot | hot | hot |
 
 - 따라서 관측치 [3,1,3]에 대한 우도는 다음과 같이 구함
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?%5C%5CP%283%5C%3B%201%5C%3B%203%5C%29%5C%5C%5C%5C%20%3DP%283%5C%3B%201%5C%3B%203%2C%5C%3B%20cold%2C%5C%3B%20cold%2C%5C%3B%20cold%29&plus;%5C%5C%5C%5C%20%3DP%283%5C%3B%201%5C%3B%203%2C%5C%3B%20cold%2C%5C%3B%20cold%2C%5C%3B%20hot%29&plus;%5Ccdots%20%5C%5C%5C%5C%20%3DP%283%5C%3B%201%5C%3B%203%2C%5C%3B%20hot%2C%5C%3B%20hot%2C%5C%3B%20hot%29"/>
 
 
### Notation (표기법) 정리
 - <img src="https://latex.codecogs.com/gif.latex?Q%3Dq_%7B0%7D%2Cq_%7B1%7D%2C%5Ccdots%20%2Cq_%7Bn%7D%2Cq_%7BF%7D"/> : 상태(state)의 집합(set), <img src="https://latex.codecogs.com/gif.latex?q_%7B0%7D"/>는 시작상태, <img src="https://latex.codecogs.com/gif.latex?q_%7BF%7D"/>는 종료상태, n은 상태의 개수
 - A:전이확률 행렬(n X n), <img src="https://latex.codecogs.com/gif.latex?a_%7Bij%7D"/>는 i번째 상태에서 j번째 상태로 전이할 확률 ( <img src="https://latex.codecogs.com/gif.latex?%5Csum_%7Bj%3D1%7D%5E%7Bn%7Da_%7Bij%7D"/> )
 - <img src="https://latex.codecogs.com/gif.latex?B%3Db_%7Bi%7D%28o_%7Bt%7D%29"/> : i번째 상태에서 관측치 <img src="https://latex.codecogs.com/gif.latex?o_%7Bt%7D"/>가 나타날 방출확률
 - <img src="https://latex.codecogs.com/gif.latex?O%3D%5Bo_%7B1%7D%2Co_%7B2%7D%2C%5Ccdots%2Co_%7Bt%7D%2C%5Ccdots%20%2Co_%7BT%7D%5D"/> : 길이가 T인 관측치의 시퀀스
 - <img src="https://latex.codecogs.com/gif.latex?%5Calpha_%7Bt%7D%28j%29%3DP%28o_%7B1%7D%2Co_%7B2%7D%2C%5Ccdots%20%2Co_%7Bt%7D%2Cq_%7Bt%7D%7C%5Clambda%29"/> : 모델 <img src="https://latex.codecogs.com/gif.latex?%5Clambda"/>가 주어졌을 때 j번째 상태와 <img src="https://latex.codecogs.com/gif.latex?o_%7B1%7D%2C%5Ccdots%20%2Co_%7Bt%7D"/>가 나타날 확률. 전방확률(Forward Probability)
 - <img src="https://latex.codecogs.com/gif.latex?%5Cbeta_%7Bt%7D%28j%29%3DP%28o_%7Bt&plus;1%7D%2Co_%7Bt&plus;2%7D%2C%5Ccdots%20%2Co_%7BT%7D%2Cq_%7Bt%7D%3Dj%7C%5Clambda%29"/> 모델 <img src="https://latex.codecogs.com/gif.latex?%5Clambda"/>가 주어졌을 때 j번째 상태와 <img src="https://latex.codecogs.com/gif.latex?o_%7Bt&plus;1%7D%2C%5Ccdots%20%2Co_%7BT%7D"/>가 나타날 확률. 후방확률(Backward Probability)
 
 
### Compute Likelihood : Foward Algorithm
 - 앞서 예시에서 살펴보았듯이 계산해야 할 경우의 수가 정말 많음
 - N개의 은닉상태가 있고, 관측치의 길이가 T라면 우도 계산시 고려해야 할 가지수는 <img src="https://latex.codecogs.com/gif.latex?N%5ET"/>가지
 - 이런 비효율성을 완화하기 위해 다이내믹 프로그래밍(dynamic programming) 기법을 사용
 - 다이내믹 프로그래밍은 중복되는 계산을 저장해두었다가 푸는 것이 핵심 원리


 <p align="center"/>
 <img height="400px" src="https://i.imgur.com/UcXttLx.png"/>
 

 - 예를 들어, 아이스크림 3개(<img src="https://latex.codecogs.com/gif.latex?o_%7B1%7D"/>)와 1개(<img src="https://latex.codecogs.com/gif.latex?o_%7B2%7D"/>)가 연속으로 관측됐고 두 번째 시점(t=2)의 날씨가 추웠을(<img src="https://latex.codecogs.com/gif.latex?q_%7B1%7D"/>) 확률은 <img src="https://latex.codecogs.com/gif.latex?%5Calpha_%7B2%7D%281%29"/>
 - 마찬가지로 아이스크림 3개(<img src="https://latex.codecogs.com/gif.latex?o_%7B1%7D"/>)가 관측됐고 첫 번째 시점(t=1)의 날씨가 추웠을(<img src="https://latex.codecogs.com/gif.latex?q_%7B1%7D"/>) 확률은 <img src="https://latex.codecogs.com/gif.latex?%5Calpha_%7B1%7D%281%29"/>
 - 아이스크림 3개(<img src="https://latex.codecogs.com/gif.latex?o_%7B1%7D"/>)가 관측됐고 첫 번째 시점(t=1)의 날씨가 더웠을(img src="https://latex.codecogs.com/gif.latex?%5Calpha_%7B1%7D%282%29"/>) 
 - 각각을 구하는 식은
 
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?%5C%5C%5Calpha_%7B1%7D%281%29%3DP%28cold%7Cstart%29%5Ctimes%20P%283%7Ccold%29%5C%5C%5C%5C%20%5Calpha_%7B1%7D%282%29%3DP%28hot%7Cstart%29%5Ctimes%20P%283%7Chot%29%5C%5C%5C%5C%20%5Calpha_%7B2%7D%281%29%3D%5Calpha_%7B1%7D%281%29%5Ctimes%20P%28cold%7Ccold%29%5Ctimes%20p%283%7Ccold%29&plus;%5Calpha_%7B1%7D%282%29%5Ctimes%20P%28cold%7Chot%29%5Ctimes%20p%283%7Ccold%29"/>
 
 
 - Foward Algorithm의 핵심 아이디어는 **중복되는 계산은 그 결과를 어딘가에 저장해 두었다가 필요할 때 불러서 사용**하자는 것
 - 예시여서 지금은 계산량 감소가 도드라져 보이지는 않지만 데이터가 조금만 커져도 그 효율성은 명백해짐
 - j번째 상태에서 <img src="https://latex.codecogs.com/gif.latex?o_%7B1%7D%2C%5Ccdots%20%2Co_%7Bt%7D"/>가 나타날 전방확률 <img src="https://latex.codecogs.com/gif.latex?%5Calpha"/>는 다음과 같이 정의
 
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?%5Calpha_%7Bt%7D%28j%29%3D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%5Calpha_%7Bt-1%7D%28i%29%5Ctimes%20a_%7Bij%7D%5Ctimes%20b_%7Bj%7D%28o_%7Bt%7D%29"/>
 
 - 전방확률을 관측치 시퀀스 끝까지 계산하면 우도와 동치가 됨
 
 
### Decoding : Viterbi Algorithm
 - 우리의 두 번째 관심은 **모델 <img src="https://latex.codecogs.com/gif.latex?%5Clambda"/>와 관측치 시퀀스 O가 주어졌을 때 가장 확률이 높은 은닉상태의 시퀀스 Q를 찾는 일**
 - 이를 디코딩(decoding)이라고 함
 - 은닉마르코프모델을 만드려는 근본 목적에 닿아 있는 문제
 - 은닉마르코프모델의 디코딩 과정에는 비터비 알고리즘(Viterbi Algorithm)이 주로 사용
 - 비터비 알고리즘의 계산 대상인 비터비 확률(Viterbi Probability) v는 다음과 같이 정의(<img src="https://latex.codecogs.com/gif.latex?v_%7Bt%7D%28j%29"/>는 t번째 시점의 j번째 은닉상태의 비터비 확률을 가리킴)
 
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?v_%7Bt%7D%28j%29%3D%5Coverset%7Bn%7D%7B%5Cunderset%7Bi%7D%7Bmax%7D%7D%5Bv_%7Bt-1%7D%28i%29%20%5Ctimes%20a_%7Bij%7D%20%5Ctimes%20b_%7Bj%7D%28o_%7Bt%7D%29%5D"/>
 
 
 - Foward Algorithm에서 구하는 전방확률 <img src="https://latex.codecogs.com/gif.latex?%5Calpha"/>와 디코딩 과정에서 구하는 비터비 확률 <img src="https://latex.codecogs.com/gif.latex?v"/>를 계산하는 과정이 거의 유사
 - Foward Algorithm은 각 상태에서의 <img src="https://latex.codecogs.com/gif.latex?%5Calpha"/>를 구하기 위해 가능한 모든 경의의 수를 고려해 그 확률을 더해줬다면(sum), 디코딩은 그 확률들 가운데 최대값(max)에 관심이 있음
 
 
 <p align="center">
 <img height="400px" src="https://i.imgur.com/MXxxdo7.png"/>
 
 - 각 상태에서 비터비 확률 v를 구하는 식은 다음과 같음
 
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?%5C%5Cv_%7B1%7D%281%29%3Dmax%5BP%28cold%7Cstart%29%5Ctimes%20P%283%7Ccold%29%5D%3DP%28cold%7Cstart%29%5Ctimes%20P%283%7Ccold%29%5C%5C%5C%5C%20v_%7B1%7D%282%29%3Dmax%5BP%28hot%7Cstart%29%5Ctimes%20P%283%7Chot%29%5D%3DP%28hot%7Cstart%29%5Ctimes%20P%283%7Chot%29%5C%5C%5C%5C%20v_%7B2%7D%281%29%3Dmax%5Bv_%7B1%7D%281%29%5Ctimes%20P%28cold%7Ccold%29%5Ctimes%20P%281%7Ccold%29%2Cv_%7B1%7D%282%29%5Ctimes%20P%28cold%7Chot%29%5Ctimes%20P%281%7Ccold%29%5D"/>
 
 
 - Foward Algorithm과 비터비 알고리즘 사이의 가장 큰 차이점은 역추적(backtracking) 과정이 있다는 점
 - **디코딩의 목적은 비터비 확률이 얼마인지보다 최적 상태열이 무엇**인지에 대해 관심
 - 위 그림에서 파란색 점선으로 된 역방향 화살표가 역추적을 나타냄
 - 예를 들어, 2번째 시점 2번째 상태 <img src="https://latex.codecogs.com/gif.latex?q_%7B2%7D"/>(=HOT)의 backtrace <img src="https://latex.codecogs.com/gif.latex?b_%7Bt_%7B2%7D%7D%282%29%3Dq_%7B2%7D"/>는 <img src="https://latex.codecogs.com/gif.latex?q_%7B2%7D"/>
 - <img src="https://latex.codecogs.com/gif.latex?q_%7B2%7D"/>를 거쳐 들어온 값이 <img src="https://latex.codecogs.com/gif.latex?q_%7B1%7D"/>을 거쳐 들어온 값보다 크기 때문
 - 2번째 시점의 첫번째 상태 <img src="https://latex.codecogs.com/gif.latex?q_%7B1%7D"/>(=COLD)의 backtrace <img src="https://latex.codecogs.com/gif.latex?b_%7Bt_%7B2%7D%7D%281%29"/>는 <img src="https://latex.codecogs.com/gif.latex?q_%7B2%7D"/>
 - 최적상태열은 이렇게 구한 backtrace들이 리스트에 저장된 결과
 - 위 그림에서 아이스크림 [3개, 1개가 관측 됐을 때 가장 확률이 높은 은닉상태의 시퀀스는 [HOT, COLD]
 - t번째 시점 j번째 상태의 backtrace는 다음과 같이 정의 ( 아래 이미지와 함께 이해할 것 )
 
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?arg%5Coverset%7Bn%7D%7B%5Cunderset%7Bi%3D1%7D%7Bmax%7D%7D%5Bv_%7Bt-1%7D%28i%29%5Ctimes%20%5Calpha_%7Bij%7D%20%5Ctimes%20b_%7Bj%7D%28o_%7Bt%7D%29%5D"/>
 
 
### 전방확률과 후방확률
 - 은닉마르코프 모델의 파라메터 학습을 위해서는 후방확률 <img src="https://latex.codecogs.com/gif.latex?%5Cbeta"/> 개념을 짚고 넘어가야 함
 - 전방확률 <img src="https://latex.codecogs.com/gif.latex?%5Calpha"/>와 반대 방향으로 계산한 것이 후방확률
 
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?%5C%5C%5Calpha_%7Bt%7D%28j%29%3D%5Csum_%7Bi%3D1%7D%5E%7B4%7D%5Calpha_%7Bt-1%7D%28i%29%5Ctimes%20%5Calpha_%7Bij%7D%20%5Ctimes%20b_%7Bj%7D%28o_%7Bt%7D%29%5C%5C%5C%5C%20%5Cbeta_%7Bt%7D%28j%29%3D%5Csum_%7Bj%3D1%7D%5E%7Bn%7D%5Calpha_%7Bij%7D%5Ctimes%20b_%7Bj%7D%28o_%7Bt&plus;1%7D%29%5Ctimes%20%5Cbeta_%7Bt&plus;1%7D%28j%29"/>
 
 - 전방확률 <img src="https://latex.codecogs.com/gif.latex?%5Calpha_%7B3%7D%284%29"/>는 다음과 같이 구함
 
 <p align="center">
 <img height="400px" src="https://i.imgur.com/mbBaTch.png"/>
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?%5Calpha_%7B3%7D%284%29%3D%5Csum_%7Bi%3D1%7D%5E%7B4%7D%5Calpha_%7B2%7D%28i%29%20%5Ctimes%20%5Calpha_%7Bi4%7D%20%5Ctimes%20b_%7B4%7D%28o_%7B3%7D%29"/>
 
 - 후방확률 <img src="https://latex.codecogs.com/gif.latex?%5Cbeta_%7B3%7D%284%29"/>는 다음과 같이 구함
 
 <p align="center">
 <img height="400px" src="https://i.imgur.com/bP9BdJy.png"/>

 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?%5Cbeta_%7B3%7D%284%29%3D%5Csum_%7Bj%3D1%7D%5E%7B4%7D%5Calpha_%7B4j%7D%20%5Ctimes%20b_%7Bj%7D%28o_%7B4%7D%29%5Ctimes%20%5Cbeta_%7B4%7D%28j%29"/>
 
 
 - 따라서 <img src="https://latex.codecogs.com/gif.latex?%5Calpha_%7B3%7D%284%29"/>와 <img src="https://latex.codecogs.com/gif.latex?%5Cbeta_%7B3%7D%284%29"/>를 곱하면 **3번째 시점에 4번째 상태일 확률**을 의미
 - 바꿔 말하면 3번째 시점에 4번째 상태를 지나는 모든 경로에 해당하는 확률의 합을 가르키고 도식적으로는 아래와 같음


 <p align="center">
 <img height="300px" src="https://i.imgur.com/3SQDk3b.png"/>
 
 
 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?%5Calpha_%7Bt%7D%28j%29%5Ctimes%20%5Cbeta_%7Bt%7D%28j%29%3DP%28q_%7Bt%7D%3Dj%2C%20O%7C%5Clambda%29"/>
 
 
 - 따라서 특정 시점 t의 전방확률과 후방확률을 곱한 모든 상태에 대해 더해 주면 앞서 계산한 우도와 동치가 됨
 - 후방확률을 관측치 시퀀스 맨 끝부터 처음까지 계산하면 이 또한 앞서 계산한 우도와 같음


 <p align="center">
 <img src="https://latex.codecogs.com/gif.latex?%5C%5CP%28O%7C%5Clambda%29%3DP%28o_%7B1%7D%2Co_%7B2%7D%2C%5Ccdots%20%2Co_%7BT%7D%7C%5Clambda%29%5C%5C%5C%5C%20%3DP%28o_%7B1%7D%2Co_%7B2%7D%2C%5Ccdots%20o_%7Bt%7D%2Cq_%7Bt%7D%3Dq_%7B0%7D%7C%5Clambda%29%3D%5Cbeta_%7B0%7D%28q_%7Bo%7D%29%5C%5C%5C%5C%20%3D%5Csum_%7Bs%3D1%7D%5E%7Bn%7D%5Calpha_%7Bt%7D%28s%29%5Ctimes%20%5Cbeta_%7Bt%7D%28s%29"/>




