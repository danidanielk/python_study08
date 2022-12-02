#input으로 숫자 2개를 입력 -> 가격오름차순정렬 -> ?`~?번째까지 평균 가격을 출력
from cx_Oracle import connect


start=int(input("start: "))
end=int(input("end: "))
con=connect("danieldb/1@192.168.123.102:1521/xe")
sql=f"select avg(c_price) from (select rownum as rn, c_price from (select c_price from coffee order by c_price))where rn between {start} and {end}"     
cur=con.cursor()
cur.execute(sql)
for i in cur:
    print(i)
con.close()