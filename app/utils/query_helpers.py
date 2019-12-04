from django.db import Error, connections
from django.conf import settings

def query_to_list(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row)) for row in cursor.fetchall()
    ]

def do_query(query):
    try:
        with connections[settings.BWV_DATABASE_NAME].cursor() as cursor:
            cursor.execute(query)
            return query_to_list(cursor)
    except Error:
        return {}

def return_first_or_empty(executed_query):
    if len(executed_query) > 0:
        return executed_query[0]
    else:
        return {}
