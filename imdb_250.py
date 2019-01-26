from requests import get
from bs4 import BeautifulSoup



url='https://www.imdb.com/chart/top?ref_=nv_mv_250'
response=get(url)

html_soup=BeautifulSoup(response.text,'html.parser')


movie_contain= html_soup.find_all('td', class_="titleColumn")


imdb=open('imdb_250.txt','w') 
  
#print(type(movie_contain))
#print(len(movie_contain))

for i in range(50):
    first_movie=movie_contain[i]
    first_name = first_movie.a.text
    #print(first_name)
    imdb.write('\n')
    imdb.write(first_name )
    
imdb.close
    

