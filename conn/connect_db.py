import psycopg2
import ConfigParser

print("set connection")

try:
    config = ConfigParser.RawConfigParser()
    config.read('insights/resources/db.properties')
    dbname = config.get('DB Connection', 'name')
    host = config.get('DB Connection', 'host')
    user = config.get('DB Connection', 'user')
    passw = config.get('DB Connection', 'passw')
    port = config.get('DB Connection', 'port')
except Exception as e:
    print(str(e),' could not read configuration file')

try:
    con=psycopg2.connect("dbname="+dbname+" user="+user+" password="+passw+" host=" + host + " port=" +port)
    cur=con.cursor()
    cur.execute("select * from building;")
    print(cur.fetchall())
    cur.close() 
    con.close()

except Exception as e:
    print(str(e),' could not open db connection')




