from cx_Oracle import connect

t=input("type: ")
p=int(input("인상할 금액: "))

con=connect("danieldb/1@192.168.123.102:1521/xe")
sql=f"update coffee set c_price=c_price+{p} where c_type='{t}'"
cur=con.cursor()
cur.execute(sql)
if cur.rowcount>=1:
    con.commit()
    print("success")
    

con.close()
