from cx_Oracle import connect

#인풋에 번호를 넣으면 해당 번호 행이 삭제되게끔

con=connect("danieldb/1@192.168.123.102:1521/xe")

while True:
    sql="select * from coffee order by c_no"
    cur=con.cursor()
    cur.execute(sql)
    
    for no,name,price,type in cur:
        print(f"{no}]{name},{price}원,{type}산")
        print("================")
        
    no= int(input("번호 : "))
    sql=f"delete from coffee where c_no={no}"
    cur.execute(sql)
    if cur.rowcount ==1:
        print("삭제성공")
        con.commit()
    if no ==999:
        print("종료")
        break
con.close()
    