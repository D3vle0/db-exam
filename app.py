import requests, time
from bs4 import BeautifulSoup

star = []
review = []

for i in range(1, 500):
    response = requests.get(f'https://movie.naver.com/movie/point/af/list.naver?&page={str(i)}')

    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select('td.title')
    for j in title:
        star.append(str(j).split("별점 - 총 10점 중</span></span><em>")[1].split("</em")[0].strip())
        review.append(str(j).split("<br/>")[1].split("<a")[0].strip())
    # time.sleep()

    # print(star)
    # print(review)
    # print(len(star), len(review))

f1 = open("./bad.txt",'w')
f2 = open("./good.txt",'w')
for i in range(len(star)):
    if int(star[i]) <= 5:
        f1.write(review[i] + "\n")
    else:
        f2.write(review[i] + "\n")

f1.close()
f2.close()