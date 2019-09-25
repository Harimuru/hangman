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
	if len(title_name) > 7 :
		movie_file.write(title_name+"#")

movie_file.write("END")

movie_file.close()



my_url1 = "https://www.imdb.com/list/ls008957859/"

uClient = uReq(my_url1)
pg_html1 = uClient.read()
uClient.close()

series_file = open("series_list.txt","w")

pg1_soup  = Bsp(pg_html1,"html.parser")
Title_list1 = pg1_soup.findAll("div",{"class":"lister-item-content"}) 

for blck1 in Title_list1:
	title_name = blck1.h3.a.text
	if len(title_name) > 7 :
		series_file.write(title_name+"#")

series_file.write("END")
series_file.close()




