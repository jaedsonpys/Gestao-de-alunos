import pymysql


conn = pymysql.connect(
    user='root',
    password=''
)

sql = conn.cursor()

sql.execute('create database if not exists Students')
sql.execute('use Students')
sql.execute('create table if not exists students(matricula int primary key, nome varchar(50), turno varchar(10), ano int(2), serie char(1))')


class MySQL:
    def get_student(self, id=None):
        response = None

        if id is None:
            sql.execute('select * from students')
            data = sql.fetchall()

            if data:
                response = {}
                for s in data:
                    response[s[0]] = {
                        'matricula': s[0],
                        'nome': s[1],
                        'turno': s[2],
                        'ano': s[3],
                        'serie': s[4]
                    }
        else:
            sql.execute('select * from students where matricula = %s', (int(id), ))
            data = sql.fetchone()

            if data:
                response = {
                    'matricula': data[0],
                    'nome': data[1],
                    'turno': data[2],
                    'ano': data[3],
                    'serie': data[4]
                }

        return response

    def set_student(self, data: dict={}):
        if len(data) == 0:
            return False

        sql.execute('insert into students values(%s,%s,%s,%s,%s)', 
            (data['matricula'], data['nome'], data['turno'], int(data['ano']), data['serie'],)
        )
        conn.commit()

        return True

    def update_student(self, id, data: dict={},):
        if len(data) == 0:
            return False

        sql.execute('update students set nome = %s, turno = %s, ano = %s, serie = %s where matricula = %s', 
            (data['nome'], data['turno'], int(data['ano']), data['serie'], int(id),)
        )
        conn.commit()

        return True

    def delete_student(self, id):
        sql.execute('delete from students where matricula = %s', (id,))
        conn.commit()

        return True