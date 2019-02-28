from neo4j.v1 import GraphDatabase


class Neo4jClient(object):

    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def execute_query(self, query, select_list):
        result_list = []

        with self._driver.session() as session:
            with session.begin_transaction() as tx:
                result = tx.run(query)

                for r in result:
                    # result_tuple 초기화
                    result_tuple = ()
                    for select in select_list:
                        result_tuple = result_tuple + (r[select],)
                    # print(result_tuple)
                    result_list.append(result_tuple)

                return result_list
