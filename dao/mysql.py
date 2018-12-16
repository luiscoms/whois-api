import pymysql


class MySQL:

    def __init__(self, config):
        self.connection = pymysql.connect(**config)

    def fetchall(self, sql):
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            columns = [desc[0] for desc in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]

    def get_account_by_cpf(self, cpf):
        query = f"""SELECT * FROM accounts where cpf = '{cpf}'"""
        return self.fetchall(query)
