from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as Bsp

my_url = "https://www.imdb.com/chart/top?ref_=nv_mv_250"

# opening connection and grabbing tha page 
uClient = uReq(my_url)
pg_html = uClient.read()
uClient.close()

movie_file = open("movie_list.txt","w")

#html parsing
pg_soup  = Bsp(pg_html,"html.parser")
Title_list = pg_soup.findAll("td",{"class":"titleColumn"}) 

for blck in Title_list:
	title_name = blck.a.text
	movie_file.write(title_name+"#")

movie_file.write("END")

movie_file.close()


