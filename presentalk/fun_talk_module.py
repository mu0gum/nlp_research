import PresenTALKUtil


class Fun_talkClass:

    def __init__(self):
        self.keyword_list = PresenTALKUtil.get_command_config('fun_talk')[0]['command_word'].split(',')

    def check_fragments(self, mecab, message):
        pos_list = mecab.pos(message)
        if len(pos_list) > 5:
            return False

        matching_count = 0
        for keyword in self.keyword_list:
            for pos in pos_list:
                if pos[0] == keyword:
                    matching_count += 1

        # 매칭되는 단어 / 형태소 분석 길이 값이 0.4 이상일 경우 True 로 판단
        if matching_count / len(pos_list) > 0.4:
            return True
        else:
            return False

    def execute_fragments(self, mecab, message):
        return self.execute_command(mecab, message)

    def execute_command(self, mecab, message):
        fun_talk = []
        # TODO : 개선
        fun_talk.append('흠..그럼 컬투쇼 사연 하나 소개해 드릴께요ㅋㅋ')
        fun_talk.append(PresenTALKUtil.get_random_message('fun_talk'))
        fun_talk.append(PresenTALKUtil.get_random_message('laugh'))
        fun_talk.append(PresenTALKUtil.get_random_message('apologize'))

        return_dict = {'command': 'fun_talk', 'message':  fun_talk}
        return return_dict
