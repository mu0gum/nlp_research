import PresenTALKUtil
import importlib


class CommandProcessor:

    def __init__(self):
        self.end_post_list = ['VX+EC', 'XSV+EC', 'VX', 'EP+EF', 'VX+EF', 'VV+EC', 'VV', 'EC']
        self.command_config_list = PresenTALKUtil.get_command_config('')

    def check_fragments(self, mecab, message):
        # command_config_list 에서 모듈 하나씩 가져와서 check_fragments function 실행
        # 결과가 true 이면 모듈의 execute_fragments 실행
        module_name = ''
        for command_config in self.command_config_list:
            command = command_config['command']

            module = importlib.import_module(command + '_module')
            function_class = getattr(module, command.capitalize() + 'Class')
            function_instance = function_class()
            if function_instance.check_fragments(mecab, message):
                module_name = command
                break

        return module_name

    def execute_fragments(self, module_name, mecab, message):
        module = importlib.import_module(module_name + '_module')
        function_class = getattr(module, module_name.capitalize() + 'Class')
        function_instance = function_class()
        return function_instance.execute_fragments(mecab, message)

    def __analyze_command__(self, mecab, message):
        ending_of_word = ''
        # 어미 바로 앞에 있는 명사
        front_noun = ''

        # 어미 불필요 요소 제거
        pos_list = mecab.pos(message)
        while pos_list[len(pos_list) - 1][1] in ['IC', 'SY']:
            pos_list = pos_list[:len(pos_list) - 1]

        list_len = len(pos_list)
        for i in range(list_len):
            # 명사 list 가 있는 경우 break
            if front_noun != '':
                break

            pos = pos_list[list_len - 1 - i]

            if pos[1] in self.end_post_list:
                ending_of_word = pos[0] + ending_of_word
            else:
                j_len = list_len - i
                for j in range(j_len):
                    pos = pos_list[j_len - 1 - j]
                    if pos[1].startswith('N'):
                        front_noun = pos[0]

        # calc socre
        max_count_score = 0
        max_count_command = ''
        for command_config in self.command_config_list:
            count_score = 0

            # calc word count
            word_list = command_config['command_word'].split(',')
            for word in word_list:
                if word == front_noun:
                    count_score += 1

            # calc eow count
            eow_list = command_config['command_eow'].split(',')
            for eow in eow_list:
                if ending_of_word == eow:
                    count_score += 1
                    break

            if count_score > 1:
                is_valid = True
                # 필수 단어 체크
                if command_config['mandatory_word'] != '':
                    mandatory_list = command_config['mandatory_word'].split(',')
                    for mandatory_word in mandatory_list:
                        if mandatory_word not in message:
                            is_valid = False

                if is_valid and count_score > max_count_score:
                    max_count_score = count_score
                    max_count_command = command_config['command']

        return max_count_command

    def process_command(self, mecab, message):
        command = self.__analyze_command__(mecab, message)

        result_dict = {'command': '', 'message': ''}
        if command != '':
            # dynamic class loading
            # DB Data 추가 & module 추가 하면 새로운 기능 바로 사용 가능
            # https://stackoverflow.com/questions/547829/how-to-dynamically-load-a-python-class
            module = importlib.import_module(command + '_module')
            function_class = getattr(module, command.capitalize() + 'Class')
            function_instance = function_class()
            result_dict = function_instance.execute_command(mecab, message)

        return result_dict
