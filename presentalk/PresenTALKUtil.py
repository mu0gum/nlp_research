import DBConnector

conn_data = {
    'user': 'your db user',
    'password': 'your db user password',
    'host_product': 'your host',
    'dbname': 'your db name',
    'port': 'your db port'
}


def get_random_message(key):
    conn = DBConnector.getDBConnection(conn_data)
    cursor = conn.cursor()

    topic_query = """
        select random_message
        from random_message
        where  message_type = %s
        order by random() limit 1;
    """
    cursor.execute(topic_query, [key])
    result = cursor.fetchone()

    print(result[0])
    return result[0]


def get_topic_list():
    conn = DBConnector.getDBConnection(conn_data)
    cursor = conn.cursor()

    topic_query = "select * from public.topic"
    cursor.execute(topic_query)

    topic_list = [dict(zip(['topic_id', 'topic_name', 'topic_priority', 'topic_owner'], row)) for row in
                  cursor.fetchall()]

    return topic_list


def get_temp_rule_list():
    conn = DBConnector.getDBConnection(conn_data)
    cursor = conn.cursor()

    rule_query = """
        select t.topic_id, r.rule_id, r.matching_rule, r.response_rule
        from topic t
        inner join topic_rule_map tm
            on tm.topic_id = t.topic_id
        inner join mrule r 
            on r.rule_id = tm.rule_id
     """

    cursor.execute(rule_query)
    temp_rule_list = [dict(zip(['topic_id', 'rule_id', 'matching_rule', 'response_rule'], row)) for row in
                      cursor.fetchall()]

    return temp_rule_list


def get_feature_dictionary(feature_key):
    conn = DBConnector.getDBConnection(conn_data)
    cursor = conn.cursor()

    feature_query = """
        select ct.concept_name, cr.concept_list, ct.feature_type
        from concept ct
        inner join
        (
            select concept_parent, string_agg(concept_name, ',') as concept_list
            from concept
            where case when '' = %s then 1 = 1 else feature_type = %s end
            group by concept_parent
        ) cr
        on cr.concept_parent = ct.concept_id
    """
    cursor.execute(feature_query, [feature_key, feature_key])
    feature_dic_list = [dict(zip(['concept_name', 'concept_list', 'feature_type'], row)) for row in cursor.fetchall()]

    return feature_dic_list


def get_present_list():
    conn = DBConnector.getDBConnection(conn_data)
    cursor = conn.cursor()

    present_query = """
        select string_agg(present_name, ',') as present_list
        from present
    """

    cursor.execute(present_query)
    present_list = list(cursor.fetchone())[0].split(',')

    return present_list


def get_command_config():
    conn = DBConnector.getDBConnection(conn_data)
    cursor = conn.cursor()

    command_query = """
            select command, command_word, command_eow 
            from command_config
     """

    cursor.execute(command_query)
    config_dic_list = [dict(zip(['command', 'command_word', 'command_eow'], row)) for row in cursor.fetchall()]

    return config_dic_list


def get_knowledge_prop_list():
    conn = DBConnector.getDBConnection(conn_data)
    cursor = conn.cursor()

    command_query = """
                select prop_name, prop_alias 
                from knowledge_prop_list
         """

    cursor.execute(command_query)
    prop_list = cursor.fetchall()

    return prop_list
