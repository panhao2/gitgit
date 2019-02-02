import sys
import MYSQLdb
class bank(object):
	def __init__(self,conn):
		self.conn=conn
	
	def acquireacc(self,account):
		cursor=self.conn(cursor)
		sql='select * from tb6 where account=%d'%account
		cursor.execute()
		rs=cursor.fetchall()
		if rs!=1:
			print 'error in the first step'
		finally:
			cursor.close()
	def acquiremoney(self,account,money):
		cursor=self.conn(cursor)
		sql='select * from tb6 where account=%d and money>%d'%(account,money)
		cursor.execute()
		rs=cursor.fetchall()
		if rs!=1:
			print 'error in the second step'
		finally:
			cursor.close()
	def deduce(self,account,money):
		cursor=self.conn(cursor)
		sql='update table tb6 set money=money-%d where account =%d'%(money,account)
		cursor.execute()
		rs=cursor.rowcount()
		conn.commit()
		if rs!=1:
			print 'error in the third step'
		finally:
			cursor.close()
	def add(self,account,money):
		cursor=self.conn(cursor)
		sql='update table tb6 set money=money+%d where account =%d'%(money,account)
		cursor.execute()
		rs=cursor.rowcount
		conn.commit()
		if rs!=1:
			print 'error in the forth step'
		finally:
			cursor.close()
			
if __name__=='__main__':
	try:
		ac1=sys.argv[1]
		ac2=sys.argv[2]
		money=sys.argv[3]
		conn=MYSQLdb.connect(host='127.0.0.1',username='root',password='tangama',port=3306,db='t1')
		bankpro=bank(conn)
		bankpro.acquireacc(ac1)
		bankpro.acquireacc(ac2)
		bankpro.acquiremoney(ac1,money)
		bankpro.deduce(ac1,money)
		bankpro.add(ac2,money)
	except Exception,e:
		print 'catch Exception'+str(e)
	finally:
		conn.close()




