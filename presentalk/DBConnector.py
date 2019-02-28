import psycopg2

# user = ''
# password = ''
# host_product = ''
# dbname = ''
# port = ''


def getDBConnection(conn_data):
    user = conn_data['user']
    password = conn_data['password']
    host_product = conn_data['host_product']
    dbname = conn_data['dbname']
    port = conn_data['port']

    product_connection_string = "dbname={dbname} user={user} host={host} password={password} port={port}" \
        .format(dbname=dbname,
                user=user,
                host=host_product,
                password=password,
                port=port)

    conn = psycopg2.connect(product_connection_string)
    return conn
