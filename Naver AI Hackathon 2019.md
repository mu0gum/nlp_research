# Naver AI Hackathon 2019(Speech Recognition) 준비
 - 네이버 2019 AI Hackathon 신청을 하였습니다. 해커톤은 실력있는 사람들만 나가는 것이라고 생각하고 평범한 나와는 상관없는 일이라고 생각해왔는데, 제가 진심으로 좋아하고 도전하고 싶어하는 딥러닝과 자연어처리 분야를 공부하다 보니 목표가 생긴건지 간절함이 있는건지 일단 신청하게 되었습니다. 서류에서 100팀만 걸러진다는데, 과연 그 안에 들 수 있을지는 모르겠지만..어차피 도전한거 서류발표 전까지는 음성인식에 대해 전반적인 내용을 공부하고, 논문들도 찾아보면서 어떤 모델이 제가 잘 이해하고 적용할 수 있을지 찾아보도록 하겠습니다.

## 음성인식 개요
### 출처 및 참고
1. [카카오AI리포트]음성인식 방법과 카카오i의 음성형엔진 (https://bcho.tistory.com/1149)
2. 기계 학습(Machine Learning, 머신 러닝)은 즐겁다! Part 6 (https://medium.com/@jongdae.lim/%EA%B8%B0%EA%B3%84-%ED%95%99%EC%8A%B5-machine-learning-%EC%9D%80-%EC%A6%90%EA%B2%81%EB%8B%A4-part-6-eb0ed6b0ed1d)
2. 은닉마코프모델(Hidden Markov Models) (https://ratsgo.github.io/machine%20learning/2017/03/18/HMMs/)


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


### 음성분석
 - 음성분석은 음성신호에서 주파수 분석을 통해 음성의 특징되는 부분을 추출하는 과정
 - 음파(sound waves)는 1차원으로 시간의 흐름 속 매 순간마다 음파의 높이를 기준으로 한 단일값을 가짐
 - 음파를 숫자로 표현하기 위해서는, 파동의 높이를 등간격의 좌표값으로 저장
 
 
 <p align="center">
 <img src="https://miro.medium.com/max/1000/1*PkvxKtomXS4sR4HzMVL8gA.gif"/>

 - 이러한 과정을 샘플링(sampling)이라고 함 -> 초당 수천번을 읽어들여서 그 시점의 음파 높이를 숫자로 저장
 - 샘플링은 데이터의 일부만을 추출하기 때문에 원래에 음파에 대한 대략적인 근사치를 만드는 것이기 때문에 원본과 차이가 있어 데이터 유실이 발생
 - 하지만 **Nyquist 정리** 덕분에, 기록하고자하는 가장 높은 주파수의 최소 두 배 빠르게 샘플을 추출한다면, 간격이 생긴 샘플로부터 원래의 주파수를 수학적으로 완벽하게 재구성해 사용 가능
 
 


