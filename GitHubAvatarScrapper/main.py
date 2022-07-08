import requests
from bs4 import BeautifulSoup as bs
import mysql.connector
from datetime import *

nameId = input("Enter the userId --> ")
url = "https://github.com/" + nameId
r = requests.get(url)
soup = bs(r.content,'html.parser')
images = soup.find('img',{'alt':'Avatar'})['src']

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "1234",
    database = "github"
)

mycursor = db.cursor()
mycursor.execute("Create database github")
mycursor.execute("create table githubData(id int primary key auto_increment , profileName varchar(20) not null , avatarLink varchar(100) not null)")
mycursor.execute("INSERT INTO githubData(profileName ,avatarLink ) VALUES (%s,%s)", (nameId,images))
db.commit()
