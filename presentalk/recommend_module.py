import PresenTALKUtil


class RecommendClass:

    def __init__(self):
        self.keyword_list = PresenTALKUtil.get_command_config('recommend')[0]['command_word'].split(',')

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
        # TODO : feature 를 찾는 로직 & feature 정보가 기준 이상이라면 그 feature 정보를 바탕으로 추천
        # 그게 아니라면 일반적인 선물 이야기하기 ( PresenTALKUtil.get_random_message() 활용 )

        return PresenTALKUtil.get_random_message('normal_present')

    def execute_command(self, mecab, message):
        return_dict = {'command': 'recommend', 'message': []}
        return return_dict
