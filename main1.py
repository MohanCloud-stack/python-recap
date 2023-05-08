import psycopg2
hostname='localhost'
database='test'
username='postgres'
pwd='admin123'
port_id=5432
try:
    con = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id)
    cur=con.cursor()
    cur.execute('DROP TABLE  IF EXISTS employee')
    create_script='''create table IF NOT EXISTS employee(
                        id int PRIMARY KEY,
                        name varchar(40) NOT NULL,
                        salary int,
                        dept_id varchar(30))'''
    cur.execute(create_script)
    # inserting the elements into the database
    insert_script='INSERT INTO employee(id,name,salary,dept_id) VALUES (%s,%s,%s,%s)'
    insert_value=[(1,'james',12000,'D1'),(2,'johndoe',13000,'D2'),(3,'linda',14000,'D3')]
    for i in insert_value:
        cur.execute(insert_script,i)

    # update command
    update_script='UPDATE employee set salary=salary+(salary*0.5)'
    cur.execute(update_script)

    # executing the select command
    cur.execute('select * from employee')
    for a in cur.fetchall():
        print(a[1],a[2])

   # deleteing the script
    delete_script='DELETE FROM employee where name=\'james\''
    cur.execute(delete_script)
    print("--------------------------------------")
    # executing the select command
    cur.execute('select * from employee')
    for a in cur.fetchall():
        print(a[1], a[2])
    con.commit()

except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if con is not None:
        con.close()