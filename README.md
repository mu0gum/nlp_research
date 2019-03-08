# 선물 추천 챗봇 PresenTALK 개발기

 안녕하세요. 챗봇을 직접 개발하면서 있었던 일들과 느꼈던 부분을 자유로운 형식의 글로 작성해보려고 합니다. 제가 이 글을 쓰는 이유는 지금까지 개발을 하면서 많은 분들이 작성한 글이나 포스팅을 보면서 많은 도움을 받아서, 저도 언젠가 도움이 되는 내용이 있으면 꼭 공유를 해보자고 항상 생각했기 때문입니다. 그리고 뭔가 글을 잘 쓰는, 인문학적 소양을 갖춘 다재다능한 개발자의 모습을 스스로 원했던 것 같은데... 4줄 밖에 안썼는데 안될 것 같습니다. 그래도 일단 시작해보겠습니다. ( 혹시라도 글을 보시면서 궁금하신 부분이 있으시다면 mu0gum@naver.com 으로 메일 주시면 제가 아는 범위 내에서 대답해 드리도록 하겠습니다. )
 
 ( 앞으로 작성할 내용은 전문적인 자연어 처리나 딥러닝, 프로그래밍에 대한 특별한 기술에 대해 다루지 않습니다. 다룰 수가 없습니다. ~몰라요..~ 그래도 작성한 소스코드는 같이 올릴 예정입니다. 솔직히 부끄러워서 소스코드는 올리지 않으려고 했는데 그러면 이 글을 작성하는 의미가 없는 것 같아 같이 올립니다. 저는 이제 4년차 개발자이고, 파이썬을 해본적이 없고, 퇴근 후에 시간을 쪼개서 코딩을 했고, 코딩을 원래 잘 못하기 때문에.. 제가 작성한 파이썬 코드가 훌륭할거라 생각하지 않습니다. 대신 많은 분들(?)의 질타를 받고 성장하고 싶은 욕심은 많으니 이상한 부분이나 개선 가능한 부분에 대해서 피드백 주시면 정말 감사할 것 같습니다! )
 
 
 ## 왜 챗봇을 만들게 되었는가?
 서론을 제외한 첫 주제이기 때문에 최대한 멋있는 내용을 생각해보려고 했는데, 실은 별다른 이유가 없는 것 같습니다. 굳이 표현하자면 **"사람의 말에 적절한 응답을 하는 프로그램을 만드는 모습이 멋있을 것 같아서"** 입니다. 뭐 사고가 거기에 미치기까지 알파고와 이세돌에 대한 다큐멘터리를 우연히 본 것 부터 시작해야 하지만, TMI 기 때문에 생략하겠습니다. 그래도 "사람의 말을 이해하는 프로그램" 이라는 것 자체가 개발자인 저에게 매우 흥미로운 주제로 다가왔기 때문에 꼭 도전해보고 싶었습니다. 관련 내용을 리서치 하면서 자연어처리가 어떻고, 딥러닝이 어떻고, Word2Vec 이 어떻고 하는 여러 어려워 보이는 내용들이 많았지만 일단 도전해보자! 라고 생각되서 챗봇을 만들게 되었습니다.
 
 
## 어떤 기능을 하는 챗봇을 만들 것인가?
 저는 4년 전쯤? KTDS에서 국비 지원 교육을 받았습니다. 교육을 받으면서 "사연을 입력받아 선물을 추천해주는 웹어플리케이션" 을 주제로 개발을 했는데, 그 때 주제가 마음에 들어서 나중에 꼭 다시 멋지게 만들어 보자고 다짐 했습니다. 어떤 주제로 챗봇을 만들까 고민하던 차에 그 때 생각이 났고 "필요한 내용을 물어보고 선물을 추천해주는 챗봇" 을 만들게 되었습니다.
 

## 프로젝트의 시작
 본론으로 들어가지 않고 불필요한 이야기만 하는 것 같지만 개발기니까 일단 계속 가겠습니다. 급하신 분들은 [1. 챗봇 구조](https://github.com/mu0gum/nlp_research/blob/master/README.md#1-챗봇-구조) 부터 보시면 될 것 같습니다. 이야기를 계속하자면 저는 일단 이건 혼자서 할 수 없다고 판단을 내리고 같이 할 팀원을 구하기 시작했습니다. 같이 교육을 받았던 친구들 중에 관심을 보인 두 친구에게 같이 할 것을 제안했습니다. 그 중 한 친구가 피피티로 만들어서 브리핑을 하라길래 또 열심히 만들어서 보고를 드렸습니다. 정성에 감동한 덕분인지 결국 세명이서 챗봇 개발 / 추천알고리즘 개발 / 웹, 앱 개발 3 파트로 나누어서 프로젝트를 진행하게 되었습니다. ( 같이 해준다고 했을 때 정말 고마웠습니다ㅠㅠ ) 저는 제 관심사인 챗봇 개발을 진행하고 있고, 다른 친구들이 나머지 부분을 맡아서 진행하고 있습니다. 아직 현재 진행형입니다. 현재 진행형임에도 글을 쓰는 이유는 모든 내용을 금방 쓸 것 같지도 않고, 계속 미루다보면 결국에는 쓰지 못할 것 같아서입니다. 크게 욕심내지 않고 조금씩 작성해 나가도록 하겠습니다. 아래는 제가 작성했던 PPT 의 일부분입니다. 겁나 쉽게 생각했던 것 같네요..오글거리기도 하고..


 <p align="center">
    <image src="https://github.com/mu0gum/nlp_research/blob/master/images/PT_%EA%B8%B0%ED%9A%8D1.png" width="500">
    <image src="https://github.com/mu0gum/nlp_research/blob/master/images/PT_%EA%B8%B0%ED%9A%8D2.png" width="500">
 
 
## 1. 챗봇 구조
 지금은 챗봇을 만든지 시간이 좀 지나서 어느정도 틀이 잡혔지만 처음에는 어떻게 챗봇을 만들어야하나 막막했습니다. 그 때 처음 많이 도움을 받았던 사이트가 바로 이곳입니다.
 
 https://exagen.tistory.com/notice/63
 
 
챗봇이 무엇이고, 어떻게 기능이 동작되어야 할지에 대해 개념을 잡는데 많은 도움이 되었습니다. 제가 앞으로 링크를 남기는 사이트들은 서론에 밝혔듯 언젠간 도움이 되는 포스팅을 작성해야겠다고 마음먹게 만들어 준 사이트들일겁니다. 이미 방문해본 곳일수도 있지만 아니라면 꼭 방문해 보시길 바랍니다. 저의 글은 말 그대로 개발기기 때문에 경험에 가깝고, 제가 링크를 남긴 사이트들은 학습에 도움이 될거라고 생각합니다.

다시 본론으로 들어가서 제가 만든 챗봇의 구조는 아래와 같습니다. 


 <p align="center">
     <image src="https://github.com/mu0gum/nlp_research/blob/master/images/PresenTALK_%EC%B1%97%EB%B4%87%EA%B5%AC%EC%A1%B0_20190301(%EC%88%98%EC%A0%95).png" width="600">


모든 로직을 플로우차트로 표현할 수 없어서 간략하게만 작성해 보았습니다. 위의 플로우 차트에서 중요한 부분은 **"의도 분류", "이전 대화 분석"** 입니다. 제가 생각했을 때, 챗봇 기능을 구현하는데 있어서 가장 중요한 부분은 상대방의 의도를 파악하는 부분이었습니다. 이 부분에 대한 용어는 화행분석, 의도분류 등 다양한 용어로 불리는 것 같은데, 일단 제가 참고한 분은 의도 분류 Task 라고 되어있기 때문에 저도 **의도 분류**로 작성하도록 하겠습니다. 


솔직히 선물을 추천해주는 챗봇 ( 특정 기능만을 수행하는 ) 을 만드는데 단순히 잘 짜여진 시나리오와 패턴 매칭으로도 가능할 것 같았지만 욕심많은 개발자인 저는 선물을 추천해주는 것 외에도 질문에 대한 응답, 명령에 대한 수행을 미약하게나마 할 수 있는 범용성을 가진 챗봇을 구현하고 싶었습니다. 그래서 의도 분류가 꼭 필요했습니다. 그림에 대한 설명을 계속하자면 일단 사용자가 입력한 텍스트를 의도 분류를 진행합니다. 상대방의 의도가 "Qestion" 이라면, 텍스트를 분석해서 쿼리를 만들고, 미리 구축해 놓은 지식그래프( Knowledge graph ) 에 쿼리를 날립니다. ( 자세한 내용은 추후에 다루겠습니다. ) 검색 결과가 있다면 결과를 응답해주고, 없다면 패턴 매칭 룰에 매칭 되는 것이 있나 찾아보고, 또 없다면 얼버무리거나 모른다고 응답합니다. 

***
여기서 잠깐 패턴 매칭에 대해서 간략하게 이야기하고 넘어가겠습니다. 패턴 매칭에 대한 설명은 위에 링크에 자세히 있지만 제가 구현한 방법도 간략히 설명
드리도록 하겠습니다. ( 패턴 매칭 룰은 초기에 작성한 로직이라 개선해야 할 부분이 많습니다. 처음 계획했던 코딩에서 변경이 많기 때문에 같이 변경 되었어야 하는데, 이것저것 할 것이 많아서 못하고 있었습니다. 개선이 되면 추가하도록 하겠습니다. )


일단 패턴 매칭을 하기 위한 DB Table 구조를 아래와 같이 만들었습니다.


 <p align="center">
    <image src="https://github.com/mu0gum/nlp_research/blob/master/images/matching_rule.PNG" width="700">


처음 계획은 Chatscript 를 따라해서 defined_rule 을 입력 받으면, 정규식 처리를 위한 matching_rule 을 자동으로 만들어서 입력하려고 했는데, 제가 챗봇 기능 자체를 서비스하는게 아니기 때문에 그냥 matching_rule 을 직접 입력해서 관리하고 있습니다. 어떻게보면 defined_rule 은 당장 필요없는 컬럼입니다. 어쨌든 matching_rule 에 있는 정규식 표현과 일치하면 response_rule 에 있는 메시지를 응답할 수 있도록 테이블을 구성했다고 생각하시면 될 것 같습니다.

```python
# 정의해 놓은 Rule 에서 매칭이 되는 부분을 찾음
def find_matching_rule(self, message):
	noun_list = self.mecab.nouns(message)

	# 추출된 명사가 topic_list 에 존재하는지 확인
	topic = ''
	for topic_row in self.topic_list:
		for noun in noun_list:
			if noun == topic_row['topic_name']:
				if topic_row['topic_owner'] == 'N':
					topic = topic_row['topic_id']
				else:
					topic = topic_row['topic_owner']

	# topic 을 찾지 못한 경우 -> 모든 경우 rule search
	if topic == '':
		matching_rule_list = self.all_rule_list
	else:
		matching_rule_list = self.rule_list[topic]

	response_text = []
	for rule in matching_rule_list:
		matching_rule = rule['matching_rule']
		compiled_rule = re.compile(matching_rule)

		if compiled_rule.match(message):
			response_text.append(rule['response_rule'])
			break

	return response_text
```

패턴 매칭을 하는 function 은 위와 같습니다. 간단히 설명하면 사용자가 입력한 텍스트에서 형태소 분석을 통해 명사들을 추출합니다. 그 명사들이 rule 에 정의되어 있는 topic 과 일치하면 그 topic 에 있는 rule_list 만 가지고 와서 패턴 매칭을 진행하고 그렇지 않다면 모든 룰을 바탕으로 패턴 매칭을 진행합니다. 
***

패턴 매칭에 대한 설명은 이정도로 하고 구조에 설명을 이어가겠습니다. 위의 플로우차트에서 의도가 "Command" 인 경우에는 명령을 분석합니다. 명령을 분석한 후 챗봇에서 처리할 수 있는 명령인 경우에는 그 명령에 따른 적절한 응답을 진행합니다. 만약 수행할 수 없는 명령이라면 패턴 매칭을 진행하고, 매칭되는 부분이 없다면 얼버무립니다.


의도 분류가 "Question", "Command" 가 아닌 경우에는 이전에 챗봇이 응답한 Message Type 을 바탕으로 로직을 전개해 나갑니다. 이 Message Type 이 위에서 말씀드린 **"이전 대화 분석"** 의 key 입니다. 제가 정의한 Message Type 은 아래와 같습니다.


+ BG : Bot Greeting
+ BS : Bot Starting
+ BF : Bot Feature
+ BN : Bot Normal
+ BR : Bot Recommand
+ BA : Bot Answer


아직 확정은 아니고 언제든지 추가될 수 있고, 삭제가 될 수 있습니다. 제가 Message Type 을 정의한 이유는 아래 처럼 활용하기 위함입니다.


 <p align="center">
    <image src="https://github.com/mu0gum/nlp_research/blob/master/images/PresenTALK_Sample.PNG" width="300">
     

***
사용자가 채팅방에 입장하게 되면, 챗봇은 인사를 하면서 사용자를 맞이(BG) 합니다. => 사용자의 다음 입력 text 가 "Question" 이나 "Command" 가 아니라면, 이전 챗봇의 Message Type 을 확인합니다. => 이전 Message Type 이 BG 기 때문에, 인사를 한 다음에는 선물 추천을 원하냐고(BS) 물어봅니다. => 사용자의 다음 입력 text 가 "Question" 이나 "Command" 가 아니라면, 이전 챗봇의 Message Type 을 확입합니다. => 이전 Message Type 이 BS 기 때문에 상대방의 응답이 긍정인지 부정인지 판단한 후, 긍정이라면 특징을 선물의 목적이나 대상에 대해 물어보고(BF) 부정이라면 정해진 로직을 수행합니다.
***


일단 현재까지 만든 챗봇의 구조는 이렇습니다. 아직 부족한 부분이 많고 개선해야 할 부분이 많아 보입니다. 그래도 "의도 분류", "이전 대화 분석" 의 조합으로 완벽하지는 않지만 선물을 추천해주는 기능에 간단한 질문이나 명령에 대한 응답은 가능합니다. 


일단 챗봇 구조에 대한 설명은 이정도에서 마치고 다음부터는 각 부분부분에 대해 중요하다고 생각되는 부분에 대해 설명하도록 하겠습니다.
챗봇 소스는 https://github.com/mu0gum/nlp_research/blob/master/presentalk/presentalkbot_v3.py 를 참고해주세요. **제가 파이썬에 대해 잘 몰라서 수정이 필요하다고 보이거나 개선사항이 보이면 꼭 좀 말씀 부탁드립니다! 가르침을 나누어주세요!**


## 2. 의도 분류
위에 있는 챗봇 구조 그림을 보게되면, 사용자가 텍스트를 입력하면 제일 먼저 하는 일은 상대방의 의도 분류입니다. 시나리오 기반으로만 챗봇을 만든다고 하면 의도 분류가 필수가 아닐수도 있지만, 욕심많은 개발자답게 일단 의도 분류를 추가해서 좀 더 범용성을 갖춘 챗봇을 만들기로 하고 조사를 시작했습니다. 자연어 처리나 머신러닝/딥러닝에 대한 개념이 전무했어서, 어떻게 구현을 해야하나 많이 찾아봤던 것 같습니다. 그 때 도움이 되었던 논문이 ["다양한 어휘 자질의 워드 임베딩을 이용한 화행 분석 추출](http://library.sogang.ac.kr/search/detail/SATSAD000000831041?mainLink=/search/sad&briefLink=/search/sad/result?q=%EC%84%9C%EA%B0%95%EB%8C%80%ED%95%99%EA%B5%90+%EC%9D%BC%EB%B0%98%EB%8C%80%ED%95%99%EC%9B%90_A_bk_1=jttjkorjttj_A_bk_0=jttjtjttj_A_st=FRNT_A_bk_3=jttj2016jttj_A_si=3_A_pn=4)" 입니다. 위 논문에서는 "의도 분류" 라는 용어 대신에 "화행 분석" 이라는 용어를 사용하고 있습니다. 동일한 의미이기 때문에 이해하시는데 크게 문제될 부분은 없을 것 같습니다. 논문을 보면서 규칙 기반의 모델을 개발하기에는 언어에 대한 이해도가 낮다는 문제점이 있었고, 딥러닝 기반의 모델은 학습을 위한 데이터가 없다는 문제점이 있었습니다. 분류를 위해서는 labeled data 가 필요했는데, 대화 자체는 영화의 자막이나 [국립국어원의 말뭉치 데이터](https://ithub.korean.go.kr/user/guide/corpus/guide1.do) 를 활용할 수 있지만 각 문장이 어떤 의도를 나타내는지에 대한 데이터는 없었기 때문에 논문에서 제시한 모델을 사용하기에 어려움이 있었습니다. 그 때 가뭄의 단비처럼 나타난 참고 자료가 바로 이곳 (https://github.com/warnikchow/dlk2nlp) 입니다. 여기에는 의도 분류를 위한 여러가지 모델의 대한 설명과 함께 labeled data set 이 함께 올라와 있습니다. 뜬금없는 이야기지만 위 논문도 그렇고 지금 소개하는 깃허브도 그렇지만 정말 고마운 분들이 많은 것 같습니다. ( 자신의 지식을 나누고 공유해주시는 모든 분들을 리스펙합니다ㅎㅎ ) 제가 개발한 챗봇도 위의 블로그의 CNN 기반의 모델을 바탕으로 intent_analyzer 를 개발하였습니다. 의도 분류를 위한 코딩은 위의 깃허브 주소를 참고하셔서 개발하시는 게 훨씬 도움이 될 것 같아 따로 소스코드는 첨부하지 않겠습니다. 다만 저의 모델을 검증해본 결과 accuracy 가 0.85 정도가 나왔기 때문에, 정확도를 조금이라도 높이고자 규칙을 베이스로 한 로직 ( 질문 Case )을 추가해주었습니다.


```python
def check_question(self, pos_result):
	pos_len = len(pos_result)

	# 판단하지 않음
	if pos_len < 3:
		return False

	last_pos = pos_result[pos_len-3:]
	if last_pos[2][0] != '?':
		return False
	two_pos = last_pos[0][1] + '+' + last_pos[1][1]
	if two_pos in ['EP+EF', 'NP+VCP+EF']:
		return True
	else:
		return False
```


위의 로직에 대해 간략히 설명하겠습니다. 제가 사용하는 mecab 형태소 분석기로 질문 형식의 문장을 형태소 분석을 진행해보면 아래와 같이 나오게 됩니다.


***

[('밥', 'NNG'), ('먹', 'VV'), ('었', 'EP'), ('니', 'EF'), ('?', 'SF')]

[('밥', 'NNG'), ('먹', 'VV'), ('었', 'EP'), ('어', 'EF'), ('?', 'SF')]

[('밥', 'NNG'), ('먹', 'VV'), ('었', 'EP'), ('습니까', 'EF'), ('?', 'SF')]

[('아이유', 'IC'), ('생일', 'NNG'), ('이', 'JKS'), ('언제', 'NP'), ('야', 'VCP+EF'), ('?', 'SF')]

[('아이유', 'IC'), ('고향', 'NNG'), ('이', 'JKS'), ('어디', 'NP'), ('야', 'VCP+EF'), ('?', 'SF')]

[('아이유', 'IC'), ('별명', 'NNG'), ('이', 'JKS'), ('뭐', 'NP'), ('야', 'VCP+EF'), ('?', 'SF')]

[('작년', 'NNG'), ('EPL', 'SL'), ('우승', 'NNG'), ('팀', 'NNG'), ('이', 'JKS'), ('어디', 'NP'), ('야', 'VCP+EF'), ('?', 'SF')]

[('작년', 'NNG'), ('EPL', 'SL'), ('우승', 'NNG'), ('팀', 'NNG'), ('이', 'JKS'), ('어디', 'NP'), ('니', 'VCP+EF'), ('?', 'SF')]

[('작년', 'NNG'), ('EPL', 'SL'), ('우승', 'NNG'), ('팀', 'NNG'), ('이', 'JKS'), ('어디', 'NP'), ('지', 'VCP+EF'), ('?', 'SF')]

[('제일', 'MAG'), ('좋', 'VA'), ('아', 'EC'), ('하', 'VV'), ('는', 'ETM'), ('축구', 'NNG'), ('선수', 'NNG'), ('는', 'JX'), ('?', 'SF')]

[('제일', 'MAG'), ('좋', 'VA'), ('아', 'EC'), ('하', 'VV'), ('는', 'ETM'), ('축구', 'NNG'), ('선수', 'NNG'), ('는', 'JX'), ('누구', 'NP'), ('입니까', 'VCP+EF'), ('?', 'SF')]

***


완벽하지는 않지만 위의 코딩에서 보이는 제가 만든 규칙은


1. 형태소 분석 결과에서 뒤에서 3개 까지 추출한다.
2. 해당 문장이 **질문**이기 위해서는 형태소 분석 결과의 **맨 마지막은 물음표(?)** 이어야 한다.
3. 맨 뒤 형태소를 제외한 두 형태소 분석의 결과의 합이 **'EP+EF' or 'NP+VCP+EF' 조합**이어야 한다.

입니다. 아직 개선을 할 부분으로는


1. 물음표 뒤에 올 수 있는 다양한 문자들에 대한 처리 ex) 밥 먹었니?^^ㅋㅋㅋㅋ
2. 형태소 분석기의 정확도
3. 빈약한 case 검증 ( 위에서 자세히 보면 NNG + JX 에 대한 처리는 되어있지 않습니다. )

등이 있습니다. 하지만 위의 로직만으로 의도 분류를 하는 것이 아니고, 조금이라도 정확도를 높여보고자 함께 사용되는 로직이기 때문에 일단 눈감고 넘어가도록 하겠습니다. ( 욕심이 많아 이것저것 벌려 놓기는 했는데, 각 기능에 구현은 기본적인 부분을 진행하고 개선시켜 나갈 계획입니다. ) 의도 분류는 제가 아는 내용이 많이 없어서 간단하게 쓰려고 했는데 조금 길어진 것 같습니다. 다음은 범용성을 위한 기능 중 하나인 **지식 그래프 탐색** 에 대해 작성하도록 하겠습니다.


## 3. 지식 그래프 구축
 앞서 설명한대로 일반적으로도 사용할 수 있는 챗봇을 만들기 위해 했던 작업 중 하나가 지식 그래프 구축입니다. 지식 그래프를 구축하기 위한 지식이나 경험이 없었기 때문에, 지식 그래프 구축에 대한 컨셉을 [카카오 지식 그래프](https://www.slideshare.net/ifkakao/ss-113145456) 와 [NUGU Knowledge Base](https://www.slideshare.net/NUGU_developers/nugu-conference-2018-b31-1) 를 참고해서 간략하게 구축해 보았습니다. 당연하지만 매우 안타깝게도 저에게는 카카오나 SK처럼 지식 그래프를 만들 수 있는 자원과 역량이 부족했기 때문에 할 수 있는 것과 할 수 없는 것을 우선 구분했습니다.
 
 
 1. 광범위한 데이터를 수집해서 적재할 수 없다 => 특정 주제에 한해서 지식 그래프를 구축한다. ex) 연예인, 축구
 2. 똑같은 질문을 다양한 형태로 하더라도 이해하고 적절히 응답할 수 없다 => 질문에 대해 전혀 엉뚱한 대답을 하기보다는 확실히 할 수 있는 대답만 한다.
 
 
 일단 데이터를 수집하고 그래프의 형태로 구축하는 것은 굉장히 어려운 작업이고, 챗봇을 위한 하나의 모듈로 보기에는 전문적이고 광범위합니다. 지식 그래프를 어떻게 하느냐에 따라 질의를 하는 쿼리가 달라질 수도 있고 속도나 성능에 대해서도 고민해야 하는 부분 등 제가 모르는 곳에서 해야할 일이 많았습니다. 솔직히 그래프 DB를 써보고 싶은 가벼운 마음으로 시작했기 때문에, 지식 그래프도 그냥 가볍게 만들기로 했습니다. 지식 그래프를 구축하기 위해 그래프 DB를 선정해야 했는데, 처음에는 아파치 재단의 인큐베이팅 프로젝트로 선정된 자랑스러운 카카오의 [s2graph](https://s2graph.apache.org/)를 사용하려고 했으나 **s2graph 설치 실패, s2graph 시각화 방법을 찾지 못함** 두 가지의 이유로 neo4j를 사용하게 되었습니다.
 
 
그래프 DB를 사용한 것도 이번이 처음이기 때문에 시각화는 저에게 중요한 문제였습니다. 상상력이 부족해서 그런지 눈에 보이지 않는건 잘 이해가 되지 않아서요. 그럼 일단 제가 현재까지 만들어놓은 neo4j의 일부분을 보여드리겠습니다.


 <p align="center">
    <image src="https://github.com/mu0gum/nlp_research/blob/master/images/knowledge_graph.PNG" width="800">


간단히 설명하면 Company 라벨을 갖는 노드 2개(YG_Entertainment, 카카오M), PersonGroup 라벨을 갖는 노드 2개(빅뱅, 블랙핑크), Person 라벨을 갖는 노드 10개(지수,로제 등...)로 이루어진 그래프 DB입니다. 그리고 Compnay <-> PersonGroup 관계는 HAS_GROUP, PersonGroup <-> Person 관계는 HAS_MEMBER로 표현되어 있습니다. (아이유는 그룹이 아니지만 HAS_GROUP으로 일단 관계를 정의해두었습니다. 아직 초안이고 로직을 수정함에 따라 같이 변할 수 있습니다.)


그래프 DB를 구성하고, 이제 중요한 과제인 **"사용자의 질문을 이해하고 지식 그래프에 질의할 쿼리를 만드는 일"** 이 남았습니다. 솔직히 이 부분은 제 실력으로는 단순하게 밖에 구현을 할 수가 없었습니다. 이 부분은 앞으로도 서비스를 운영하면서 개인적인 과제로 계속 개선해 나갈 예정입니다. 아래는 소스코드입니다.


```python
def generate_query(self, graph_list):
	# [('node', 'GD'), ('prop', 'age')]
	match_query = " MATCH "
	where_query = " WHERE "
	return_query = " RETURN "
	answer_message = ""
	select_list = []

	list_len = len(graph_list)
	for i in range(0, list_len):
		element = graph_list[i]

		# 처음에는 node
		if i == 0:
			if element[0] == 'node':
				match_query += " (n) "
				where_query += " n.name = '" + element[1] + "'"
				answer_message += element[1] + " "
		else:
			if element[0] == 'node':
				pass
			elif element[0] == 'rel':
				match_query += " -[r:" + element[1] + "]-(n1) "
				answer_message += element[2] + " "
				# where_query += " AND r.alias contains '" + element[1] + "'"
			elif element[0] == 'prop':
				if "n1" in match_query:
					return_query += "n1." + element[1]
					select_list.append("n1." + element[1])
				else:
					return_query += "n." + element[1]
					select_list.append("n." + element[1])

				split_word = element[2].split(',')[0]
				if self.check_trait(split_word[-1:]):
					answer_message += split_word + "은 "
				else:
					answer_message += split_word + "는 "

	query = match_query + where_query + return_query
	return query, select_list, answer_message

def response_question(self, mecab, message):
	graph_list = []
	pos_list = mecab.pos(message)
	
	# 질문 형식 형태소 제거
	# todo : 개선 필요
	while pos_list[len(pos_list) - 1][1] in ['JX', 'VCP+EF', 'VCP', 'EF', 'SF']:
		pos_list = pos_list[:len(pos_list) - 1]

	for pos in pos_list:
		find_element = False
		if pos[1].startswith('N'):
			# find node
			for node in self._node_list:
				if pos[0] in node[1] or pos[0] in node[0]:
					pos_tuple = ('node', node[0], node[1])
					graph_list.append(pos_tuple)
					find_element = True
					break
			if find_element:
				continue
			# find relation
			for rel in self._relation_list:
				if pos[0] in rel[1] or pos[0] in rel[0]:
					pos_tuple = ('rel', rel[0], rel[1])
					graph_list.append(pos_tuple)
					find_element = True
					break
			if find_element:
				continue
			# find prop
			for prop in self._prop_list:
				if pos[0] in prop[1] or pos[0] in prop[0]:
					pos_tuple = ('prop', prop[0], prop[1])
					graph_list.append(pos_tuple)
					break

	# check has node
	# TODO : 수정
	response_message = []
	if graph_list[0][0] != 'node':
		response_message = []
	else:
		query, select_list, answer_message = self.generate_query(graph_list)
		result = self._neo4j_c.execute_query(query, select_list)
		response_message.append(answer_message + str(result[0][0]) + " 입니다.")
	return response_message
```


로직의 순서를 간단히 설명하면,

1. 사용자의 질문을 형태소 분석한 결과에서 뒷 부분부터 불필요 성분 제거
2. 이후 형태소 분석 결과를 반복문을 돌리면서 형태소 분석의 결과가 'N'으로 시작하면(명사 관련 품사) 미리 초기화 시켜둔 node_list 에 있는지 확인
3. node_list 에 있으면 graph_list 에 담고 없을 경우 relation_list > prop_list 순서로 탐색

입니다. 정말 간단히 설명했습니다. 지금 이 글을 적으면서 봐도 헛점이 많아보이네요. 개발 시간이 충분치 않은데 이것저것 욕심내다 보니 퀄리티가 떨어지는 것 같습니다. 그래도 앞으로 도전해야 할 과제가 있는거여서 오히려 의욕이 생기는 것 같습니다. 지식 그래프에 대한 설명은 아래 이미지와 [소스코드](https://github.com/mu0gum/nlp_research/blob/master/presentalk/knowledge_base.py) 를 참고하시면 좀 더 이해가 편하실 것 같습니다.


 <p align="center">
    <image src="https://github.com/mu0gum/nlp_research/blob/master/images/knowledge_query.PNG" width="850">


지금까지 작성한 로직은 모든 node_list, relation_list, prop_list 를 미리 가지고 있다가 형태소 분석을 한 결과가 해당하는 리스트에 포함되어 있으면 graph_list 에 담아두고, graph_list 결과를 가지고 쿼리를 만들어내는 형식으로 되어있습니다. 위의 코드가 가진 문제는


1. 어순이 바뀌었을 때, 대응하지 못하는 점 ex) 로제 생일 언제야? -> 생일 언제더라 로제가?
2. 주요단어가 조금 바뀌었을 때, 대응하지 못하는 점 ex) 로제 탄생이 언제야?


사실 위의 두 문제는 지식 그래프 질의 문제에서만 나타나는 것은 아닙니다. 1번 같은 경우에는 단순하게 생각해서 머신러닝이나 딥러닝을 이용해서 어순을 정렬할 수 있게하면서, 추가적인 로직을 더하면 어느정도 개선이 될 것 같습니다. 1, 2번을 위한 공통 문제 해결 아이디어로는 미리 정의된 지식 그래프에서 대응할 수 있는 질문의 리스트를 모두 뽑아 놓고, 실제 질문과 문장들간의 유사도를 분석해서 높은 유사도를 갖는 문장을 치환해서 대답할수도 있지 않을까 생각합니다. 물론 지금 이야기한 것처럼 모든 케이스를 비교하는건 굉장히 무식한 방법이지만, 만약 문장에서 node를 찾았는데 무엇을 물어보는지 모르는 경우에는 node로 질문을 필터링하고 유사도를 비교한다면 어느정도 부족한 점을 개선할 수 있을거라 생각합니다.


지식 그래프에 대한 설명은 이정도로 마치겠습니다. 설명이라기보다는 "내가 이렇게 했다" 라는 소개에 가까운 것 같네요ㅎㅎ어쨌든 개발기이고 경험을 공유하는 차원의 글이기 때문에 앞으로의 내용도 이럴 것 같습니다~!그래도 누군가에게 조금이라도 도움이 되었으면 좋겠네요. 다음에는 명령을 수행하는 로직에 대해 설명하도록 하겠습니다.


## 4. 명령 수행
범용성을 갖춘 챗봇을 만들기 위한 두번째 과제인 명령 수행 기능입니다. 현재 시중에 많이 나와있는 인공지능 스피커는 주로 무엇을 물어보거나 또는 요청하거나 하는데 많이 사용되고 있습니다. 내일 알람을 맞춰달라고 하거나 음악을 틀어달라고 하거나 하는 등의 예가 있을 것 같습니다. 솔직히 "선물 추천 챗봇이게 선물만 추천하라고 명령하지 뭐 다른 명령할게 뭐가 있어?" 라고 생각하실 수도 있지만, 재미있고 도전해볼만한 주제라고 생각되서 간단하게나마 구현해 보았습니다.


일단, 명령 수행 기능을 구현할 때 아래와 같은 내용을 고민했습니다.
***
+ 어떤 것에 대한 명령인지를 어떻게 이해하고 수행할 것인가?
+ 어떤 기능을 제공할 것인가?
+ 앞으로 어떻게 발전시켜 나갈 것인가?
***
명령 수행 기능을 구현하기 위해서 가장 중요한 부분은 역시 "어떻게 명령을 이해할 것인가" 였습니다. 제가 선택한 방법을 본론부터 말하자면 **"단어 점수 / 어미 점수를 합산하여 가장 높은 점수를 얻는 기능을 수행한다"** 입니다. 이 방법을 결정한 이유는

1. 기능 구현에 드는 시간/노력에 대비 결과물이 나쁘지 않다. => 딥러닝을 위한 데이터 생성이나 모델 개발에 드는 노력이 크다.
2. 많은 기능을 제공하지 않기 때문에 잘 짜여진 로직이 오히려 성능이 높을 수 있다. 

입니다. 저는 사용자가 챗봇이나 인공지능 스피커를 사용할 때, 무엇인가를 장황하게 요구하지 않을 것이라고 생각했습니다.(특히 챗봇은 말로 하는게 아니고 직접 손으로 타이핑을 해야하기 때문에 그런 현상이 더욱 두드러질 것으로 판단했습니다.) 물론 아직 챗봇이나 인공지능 스피커가 복잡한 문장을 정확히 이해하는 수준이 아니기 때문 이기도 하지만, 원하는 바를 간단하게 요구하는 경향이 많다고 생각했습니다. 예를 들자면
***
 + 지금 몇 시야? 
 + 영화 추천 해줘
 + 신나는 노래 틀어줘
***
등 입니다. 저는 위와 같은 식으로 사용자가 요구했을 때는 문장 전체에서 단어와 / 어미 만으로도 어느정도 명령을 분류할 수 있겠다고 판단했습니다. 그 컨셉으로 작성한 코드는 아래와 같습니다.

```python
def __init__(self):
	self.end_post_list = ['VX+EC', 'XSV+EC', 'VX', 'EP+EF', 'VX+EF', 'VV+EC', 'VV', 'EC']
	self.command_config_list = PresenTALKUtil.get_command_config()

def __analyze_command__(self, mecab, message):
	ending_of_word = ''
	noun_list = []

	# 어미 불필요 요소 제거
	pos_list = mecab.pos(message)
	while pos_list[len(pos_list) - 1][1] in ['IC', 'SY']:
		pos_list = pos_list[:len(pos_list) - 1]

	list_len = len(pos_list)
	for i in range(list_len):
		# 명사 list 가 있는 경우 break
		if len(noun_list) > 0:
			break

		pos = pos_list[list_len - 1 - i]

		if pos[1] in self.end_post_list:
			ending_of_word = pos[0] + ending_of_word
		else:
			j_len = list_len - i
			for j in range(j_len):
				pos = pos_list[j_len -1 - j]
				if pos[1].startswith('N'):
					noun_list.append(pos[0])

	# calc socre
	max_count_score = 0
	max_count_command = ''
	for command_config in self.command_config_list:
		count_score = 0

		# calc word count
		word_list = command_config['command_word'].split(',')
		for word in word_list:
			for noun in noun_list:
				if word == noun:
					count_score += 1

		# calc eow count
		eow_list = command_config['command_eow'].split(',')
		for eow in eow_list:
			if ending_of_word == eow:
				count_score += 1
				break

		if count_score > 1:
			if count_score > max_count_score:
				max_count_score = count_score
				max_count_command = command_config['command']

	return max_count_command
```

코드를 간략히 설명하자면

1. 입력 받은 문장 형태소 분석 후 전처리한다.(어미 불필요 요소 제거 => IC: 감탄사, SY: 기타기호)
2. 전처리된 형태소 분석 결과를 뒤에서부터 탐색하여 end_post_list에 해당하는 품사가 있으면 ending_of_word에 더해준다.
3. end_post_list에 해당하는 품사가 없으면 명사관련 품사인지 확인 -> 맞으면 noun_list에 담는다.
4. noun_list와 endinig_of_word를 가지고 socer를 계산한다.(현재는 단순 counting)
5. count_socre가 1 초과인 경우, 결과를 return 한다.

입니다. [전체 코드](https://github.com/mu0gum/nlp_research/blob/master/presentalk/command_processor.py) 참고하시기 바랍니다. 이제 제가 직접 만든 PresenTALKBot 에 대한 기본적인 설명은 어느정도 진행이 된 것 같습니다. 최대한 자세히 기록하고 싶었는데, 도움이 되었을지는 잘 모르겠습니다. 처음에는 챗봇 기능에 대한 설명보다는 어떤 라이브러리를 사용했고, 어떤 기술을 참고하였으며, 어떻게 서비스를 구성했나 등을 위주로 작성하려고 했는데, 쓰다보니 정반대로 챗봇 기능 구현에 대한 설명이 주가 되었네요ㅎㅎ물론 방금 말한 내용도 이 글 말미에 작성할 예정입니다~! 실제 서비스를 목표로 하고 시작했기 때문에 서버 호스팅도 하고, 시스템 구성도 하고 많은 작업을 해보았기 때문입니다.(~많이 해봤지만 잘하진 못했다고 한다.~) 실없는 소리는 이제 그만하고 다음에는 제가 맡은 범위는 아니지만, 선물 추천 기능에 대해서 간단히 이야기 해보도록 하겠습니다~!


