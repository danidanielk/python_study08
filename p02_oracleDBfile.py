from cx_Oracle import connect

#DB 연결 -> 커피 이름, 가격, 원두 정보 -> csv 파일로 생성(, 를 기준으로 )
# ex) 이름, 가격 ,원두
#

con=connect("danieldb/1@192.168.123.102:1521/xe")
sql="select c_name,c_price,c_type from coffee"
cur=con.cursor()
cur.execute(sql)
file=open("C:/Users/NT731QCJ-K582D/Desktop/test/pythonFile/test.csv","w",encoding="UTF-8")

for i,ii,iii in cur:
    file.write(f"{i},{ii},{iii}\n")

file.close()

con.close()
print("success")