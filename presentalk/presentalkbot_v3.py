# -*- coding: utf-8 -*-
# Program : PresenTALKBot Version 3.0
# Author : developer_swag
# Date : 2018-12-14
# Content
#   - 형태소 분석기 변경 KKma -> Mecab ( docker ubuntu enviroment )
#   - 기능 추가

import re
import recommend_present
import PresenTALKUtil
import BayesClassifier
import intent_analyzer
import knowledge_base
import command_processor
import text_util
import recommend_data2

from konlpy.tag import Mecab


class User:

    def __init__(self):
        # self.user_info = {'birth_day': '', 'f_sports': '', 'f_songs': '', 'gender:': ''}
        self.user_info = {'f_sports': ''}


class PresentTALKBot:
    
    def __init__(self):

        # 챗봇 종료
        self.isFinish = False

        # 형태소 분석기
        self.mecab = Mecab()

        # config
        self.intent_analyzer = intent_analyzer.IntentAnalyzer()

        # 사용자 생성
        self.user = User()

        # 대화 내용 list
        self.conversation_list = []

        # 토픽 list ( 기본 정의 )
        self.topic_list = PresenTALKUtil.get_topic_list()

        # 룰 딕셔너리 ( 특정 토픽에 대한 룰 )
        self.rule_list = {}

        # 룰 리스트 ( 모든 토픽에 대한 룰 )
        # Topic 을 찾지 못했을 때는, 모든 rule list 에 대해서 전부 매칭을 진행 -> 이건 추후 변경 여지가 있음 -> Proto Type 에 대해서는 이렇게 진행하고자 함
        self.all_rule_list = []

        # feature 딕셔너리
        # 일단 feature 를 세 개로 지정 -> 추후 늘리거나 추천 알고리즘에 맞게 적용
        self.feature_dict = {'object': '', 'age': '', 'purpose': ''}

        # feature 딕셔너리 후보 ( 일상대화에서 feature 후보군이 나올수도 있음 )
        self.feature_candidate_dict = {'object': '', 'age': '', 'purpose': ''}

        # Rule list
        self.temp_rule_list = PresenTALKUtil.get_temp_rule_list()

        for rule_row in self.temp_rule_list:
            topic_id = rule_row['topic_id']
            if topic_id in self.rule_list.keys():
                temp_rule_dict = {'matching_rule': rule_row['matching_rule'],
                                  'response_rule': rule_row['response_rule']}
                self.rule_list[topic_id].append(temp_rule_dict)
            else:
                temp_rule_list = []
                temp_rule_dict = {'matching_rule': rule_row['matching_rule'],
                                  'response_rule': rule_row['response_rule']}
                temp_rule_list.append(temp_rule_dict)
                self.rule_list[topic_id] = temp_rule_list

            self.all_rule_list.append(temp_rule_dict)

    # save conversation list
    def save_conversation_list(self, message, message_type, feature_key):
        conversation = {'message': message, 'type': message_type, 'feature_key': feature_key}
        self.conversation_list.append(conversation)

    # 얼버무리기 function
    def response_quibble_message(self, message):
        # default
        response_message = []
        response_message.append(PresenTALKUtil.get_random_message('quibble'))

        return response_message

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
            print(matching_rule)
            compiled_rule = re.compile(matching_rule)

            if compiled_rule.match(message):
                response_text.append(rule['response_rule'])
                break

        return response_text
    
    # 최초 인사
    def print_greeting_message(self):
        greeting_message = []
        greeting_message.append(PresenTALKUtil.get_random_message('bot_greeting'))
        self.save_conversation_list(greeting_message, 'BG', '')
        return greeting_message

    def find_feature_candidate(self, message):
        # message 의 길이에 따라 로직을 달리 하자
        # length 가 길면 여러 의미로 해석될 수 있고, 짧은 경우에는 대부분의 내용이 핵심 내용일 확률이 높다
        # 뒤에 불필요한 내용은 제거 후 길이 확인 ( <= 20 )

        message = text_util.remove_unsueful_text(message)

        if len(message) <= 20:
            all_feature_dic_list = PresenTALKUtil.get_feature_dictionary('')

            for feature in all_feature_dic_list:
                feature_list = feature['concept_list'].split(',')
                feature_type = feature['feature_type']
                feature_root = feature['concept_name']
                for m_feature in feature_list:
                    if m_feature in message:
                        self.feature_dict[feature_type] = feature_root
        else:
            pass

    def find_feature(self, message, feature_key):
        # feature 에 대한 정보를 사용자가 이야기했는지를 체크해서 feature 리스트에 담아 두어야 한다
        # feature 를 어떻게 찾을 것인가? -> 포함 ? 명사 비교 ?
        feature_dic_list = PresenTALKUtil.get_feature_dictionary(feature_key)

        # 명사 카운팅을 하자
        # 이유 : 명사가 여러 개인 경우, 포함된 feature 가 꼭 그 feature 일 가능성이 점점 낮아짐
        # ex) "얼마전에 엄마 선물을 해드려서 아빠도 좀 해드리려고"
        is_find = False
        for feature in feature_dic_list:
            feature_list = feature['concept_list'].split(',')
            feature_type = feature['feature_type']
            feature_root = feature['concept_name']
            for m_feature in feature_list:
                if m_feature in message:
                    is_find = True
                    self.feature_dict[feature_type] = feature_root

        return is_find

    # feature 를 추출하는 질문을 하기 위한 function
    def print_feature_message(self):

        return_feature_dic = {'feature_key': '', 'feature_message': ''}
        for key in self.feature_dict.keys():
            if self.feature_dict[key] == '':
                return_feature_dic['feature_key'] = key
                return_feature_dic['feature_message'] = PresenTALKUtil.get_random_message(key)
                break

        return return_feature_dic

    def get_user_info_message(self):
        return_message = ''
        for key in self.user.user_info.keys():
            if self.user.user_info[key] == '':
                return_message = PresenTALKUtil.get_random_message(key)
                break
        return return_message

    def print_gambit_message(self, message, intent_index, message_type, pre_feature_key):
        # TODO : 로직 정리
        print(message_type)
        response_message_type = ''
        feature_key = ''
        response_text = []
        if message_type == 'BG':
            response_text.append(PresenTALKUtil.get_random_message('bot_starting'))
            # BS : Bot Start, BQ : Bot Question
            response_message_type = 'BS'

        elif message_type == 'BS':
            # 사용자의 응답이 긍정일 경우
            if BayesClassifier.get_message_class(message) == 'POS':
                temp_dic = self.print_feature_message()
                feature_key = temp_dic['feature_key']
                response_text.append(temp_dic['feature_message'])
                response_message_type = 'BF'
            # 긍정이 아닐 경우
            else:
                # 사용자가 원하는 걸 직접 질문
                response_text.append(PresenTALKUtil.get_random_message('reject'))
                response_message_type = 'BJ'

        elif message_type == 'BF':
            is_find = False
            if pre_feature_key != '':
                # feature 추출
                is_find = self.find_feature(message, pre_feature_key)

            temp_dic = self.print_feature_message()
            feature_key = temp_dic['feature_key']

            # feature 추출이 모두 끝난 경우
            if feature_key == '':
                # rec = recommand_present.Recommandation()
                # response_text.append(rec.get_recommand_message(self.feature_dict))
                # who, age, price, why
                recommend_list = recommend_data2.recommend_in_DB(self.feature_dict['object'], self.feature_dict['age'],
                                                                 '10', self.feature_dict['purpose'])

                present_list = ''
                for present in recommend_list:
                    if present_list == '':
                        present_list = present
                    else:
                        present_list = present_list + ', ' + present

                recommend_text = '선물 추천 결과입니다. ' + str(present_list) + ' 어떠신가요?'
                response_text.append(recommend_text)

                response_message_type = 'BR'
            else:
                response_text.append(temp_dic['feature_message'])
                response_message_type = 'BF'

        # TODO : 추후 추가 ( 로직의 복잡도 증가 )
        # elif message_type == 'BI':
        #     if BayesClassifier.get_message_class(message) == 'POS':
        #         pass
        #     else:
        #         pass

        elif message_type == 'BN':
            response_text = self.find_matching_rule(message)

            if len(response_text) == 0:
                response_message_type = 'BN'
                response_text = self.response_quibble_message(message)

            # TODO : 추후 추가 ( 로직의 복잡도 증가 )
            # 매칭하는 룰을 찾지 못했을 경우 특정 토픽으로 이야기하기
            # if len(response_text) == 0:
            #     user_info_text = self.get_user_info_message()
            #
            #     if user_info_text == '':
            #         response_message_type = 'BN'
            #         response_text = self.response_quibble_message(message)
            #     else:
            #         response_text.append('제가 공부한 분야로 이야기해 보시겠어요?')
            #         response_text.append(user_info_text)
            #         response_message_type = 'BI'

        elif message_type == 'BR':
            # TODO : 로직 정리 필요
            if BayesClassifier.get_message_class(message) == 'POS':
                response_message_type = 'BE'
                response_text.append(PresenTALKUtil.get_random_message('bot_ending'))
            else:
                # 사용자가 원하는 걸 직접 질문
                response_text.append(PresenTALKUtil.get_random_message('reject'))
                response_message_type = 'BJ'

        # TODO : 대답 하고 나서의 로직 추가
        elif message_type == 'BA':
            return_message = self.find_matching_rule(message)
            if len(return_message) != 0:
                response_text = return_message
            else:
                response_text = self.response_quibble_message(message)
            response_message_type = 'BN'

        elif message_type == 'BJ':
            if BayesClassifier.get_message_class(message) == 'POS':
                response_message_type = 'BE'
                response_text.append(PresenTALKUtil.get_random_message('bot_ending'))
            else:
                response_message_type = 'BN'
                response_text.append(PresenTALKUtil.get_random_message('bot_restart'))

        elif message_type == 'BE':
            if BayesClassifier.get_message_class(message) == 'POS':
                self.isFinish = True
                response_text.append(PresenTALKUtil.get_random_message('bot_bye'))
        
        # TODO : 시나리오 구성
        else:
            return_message = self.find_matching_rule(message)
            if len(return_message) != 0:
                response_text = return_message
            else:
                response_text = self.response_quibble_message(message)
            response_message_type = 'BN'

        self.save_conversation_list(response_text, response_message_type, feature_key)

        return response_text

    def get_prior_bot_message_type(self):
        index = -2;
        return_dict = {'message_type': '', 'feature_key': ''}

        while True:
            message_type = self.conversation_list[index]['type']
            if message_type.startswith('B'):
                return_dict['message_type'] = message_type
                return_dict['feature_key'] = self.conversation_list[index]['feature_key']
                break
            else:
                --index

        return return_dict

    def response_message(self, message):
        # 의도 분류
        # 0: Fragments
        # 1: Statement
        # 2: Question
        # 3: Command
        # 4: Rhetorical question
        # 5: Rhetorical command
        # 6: Intonation - dependent utterance

        intent_index = self.intent_analyzer.predict(self.mecab, message)

        print('intent_index : ' + str(intent_index))

        # 사용자의 말과 챗봇의 말이 어떤 message_type 인지 기록
        # message_type : CN -> Client Normal, BF -> Bot Feature ( 추출을 위한 질문 )
        message_type = ''
        if intent_index == 2:
            message_type = 'CQ'
        elif intent_index == 3:
            message_type = 'CC'
        else:
            if self.conversation_list:
                last_conversation = self.conversation_list[-1]
                if last_conversation['type'] == 'BF':
                    message_type = 'CA'

        self.save_conversation_list(message, message_type, '')

        response_message = []
        if intent_index not in [2, 3]:
            # 로직대로.. 원래 하던대로
            # type 을 가져올 때, Bot 이 말한 마지막 message_type 을 가지고 옴
            prior_conversation_type = self.get_prior_bot_message_type()
            response_message = self.print_gambit_message(message, intent_index, prior_conversation_type['message_type'],
                                                         prior_conversation_type['feature_key'])
        elif intent_index == 2:
            bot_message_type = ''
            know_base = knowledge_base.KnowledgeBase()
            response_message = know_base.response_question(self.mecab, message)

            # knowledgebase 에서 검색 실패 하는 경우 정규식 매칭 진행
            if len(response_message) == 0:
                bot_message_type = 'BA'
                response_message = self.find_matching_rule(message)
                
                # 정규식 매칭도 진행되지 않는 경우는 얼버무리기 로직
                if len(response_message) == 0:
                    bot_message_type = 'BQ'
                    response_message = self.response_quibble_message(message)
            else:
                bot_message_type = 'BA'

            self.save_conversation_list(response_message, bot_message_type, '')

        elif intent_index == 3:
            bot_message_type = ''
            comm_processor = command_processor.CommandProcessor()
            response_message_dict = comm_processor.process_command(self.mecab, message)

            # response_message 를 dict 으로 받아서 적절한 처리를 하는 방향으로 수정
            # recoomand 의 경우 봇과 함께 동작해야 함 ( 다른 항목들처럼 독립적이지 않음 )
            if response_message_dict['command'] == 'recommend':
                bot_message_type = 'BF'
                self.find_feature_candidate(message)
                response_message = self.print_gambit_message(message, intent_index, bot_message_type, '')
            else:
                bot_message_type = 'BA'
                response_message = response_message_dict['message']
                if not response_message:
                    response_message = self.response_quibble_message(message)

                self.save_conversation_list(response_message, bot_message_type, '')

        return response_message
