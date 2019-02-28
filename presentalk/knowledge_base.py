import neo4j_client


class KnowledgeBase:

    def __init__(self):
        self._neo4j_c = neo4j_client.Neo4jClient('bolt://192.168.219.102:7687', 'neo4j', 'presentalk')
        # self._neo4j_c = neo4j_client.Neo4jClient('bolt://172.30.1.33:7687', 'neo4j', 'presentalk')
        # self._neo4j_c = neo4j_client.Neo4jClient('bolt://localhost:7687', 'neo4j', 'presentalk')
        self._node_list = self._neo4j_c.execute_query('MATCH (n) RETURN n.name, n.alias', ['n.name', 'n.alias'])
        self._relation_list = self._neo4j_c.execute_query('MATCH (n)-[r]-() RETURN DISTINCT type(r), r.alias',
                                                          ['type(r)', 'r.alias'])
        self._prop_list = [('age', '나이, 살'), ('locate', '주소')]

    def check_trait(self, ch):
        return int((ord(ch) - 0xAC00) % 28) != 0

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

