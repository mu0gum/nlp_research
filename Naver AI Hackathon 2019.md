# Naver AI Hackathon 2019(Speech Recognition) 준비
 - 네이버 2019 AI Hackathon 신청을 하였습니다. 해커톤은 실력있는 사람들만 나가는 것이라고 생각하고 평범한 나와는 상관없는 일이라고 생각해왔는데, 제가 진심으로 좋아하고 도전하고 싶어하는 딥러닝과 자연어처리 분야를 공부하다 보니 목표가 생긴건지 간절함이 있는건지 일단 신청하게 되었습니다. 서류에서 100팀만 걸러진다는데, 과연 그 안에 들 수 있을지는 모르겠지만..어차피 도전한거 서류발표 전까지는 음성인식에 대해 전반적인 내용을 공부하고, 논문들도 찾아보면서 어떤 모델이 제가 잘 이해하고 적용할 수 있을지 찾아보도록 하겠습니다.

## 음성인식 개요
### 출처 및 참고
1. [카카오AI리포트]음성인식 방법과 카카오i의 음성형엔진 (https://bcho.tistory.com/1149)
2. 은닉마코프모델(Hidden Markov Models) (https://ratsgo.github.io/machine%20learning/2017/03/18/HMMs/)


 - 음성인식은 입력된 음성이 어떤 단어들로 이루어져 있을 확률이 높은지를 찾는 문제
 - 문제 : **'일정 길이 T 동안 입력된 음성 sequence X 에 대해서 인식기가 표현할 수 있는 모든 단어들의 조합 중 확률적으로 가장 가능성이 높은 단어열 W는 무엇인가?'** [출처1 인용] 
 - 일반적인 음성인식 아키텍처는 아래와 같음
 
 <p align="center">
 <img height="400px" src="https://slideplayer.com/slide/7248751/24/images/9/Speech+Recognition+Architecture.jpg"/>
 
