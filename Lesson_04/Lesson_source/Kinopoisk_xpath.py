import requests
from pprint import pprint
from lxml import html
main_link = 'https://www.kinopoisk.ru'
response = requests.get(main_link+'/afisha/new/city/458/')
root = html.fromstring(response.text)

# parsed_html=bs(html,'lxml')
#
#
# films_block = parsed_html.find('div',{'class':'filmsListNew'})
# # films_list = films_block.find_all('div',{'class':'item'})
# films_list = films_block.findChildren(recursive=False)
#
# films = []
# for film in films_list:
#     film_data={}
#     main_info = film.find('div',{'class':'name'}).findChild()
#     film_name = main_info.getText()
#     film_link = main_link + main_info['href']
#     genre = film.findAll('div',{'class':'gray'})[1].getText().replace(' ','')[9:]
#     rating = film.find('span',{'class':['rating_ball_grey','rating_ball_green','rating_ball_red']}).getText()
#     film_data['name'] = film_name
#     film_data['genre'] = genre
#     film_data['link'] = film_link
#     film_data['rating'] = rating
#     films.append(film_data)
#
# pprint(films)

films = root.xpath("//div[@class='item']")

for film in films:
    href = film.xpath(".//div[@class='name']/a/@href")
    name = film.xpath(".//div[@class='name']/a/text()")
    genre = film.xpath('.//div[@class="gray"][last()]/text()')[2].replace(' ','')
    rating = film.xpath('.//div[@class="rating"]/span/text()')
    print(name, href, rating, genre)


# href = root.xpath("//div[@class='name']/a/@href")
# rating = root.xpath("//div[@class='rating']/span/text()")
# print(rating)


