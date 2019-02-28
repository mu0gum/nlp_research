import PresenTALKUtil


class Fun_talkClass:

    def __init__(self):
        pass

    def execute_command(self, mecab, message):
        fun_talk = []
        # TODO : 개선
        fun_talk.append('흠..그럼 컬투쇼 사연 하나 소개해 드릴께요ㅋㅋ')
        fun_talk.append(PresenTALKUtil.get_random_message('fun_talk'))
        fun_talk.append(PresenTALKUtil.get_random_message('laugh'))
        fun_talk.append(PresenTALKUtil.get_random_message('apologize'))

        return_dict = {'command': 'fun_talk', 'message':  fun_talk}
        return return_dict
