from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus
from urllib import parse

baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
plusUrl = '그 겨울 바람이 분다'  # input('검색어를 입력하세요 : ')
# 한글 검색 자동 변환
url = baseUrl + quote_plus(plusUrl)
html = urlopen(url)
soup = bs(html, "html.parser")
# 전체 소스에서 .jpg로 검색하여 앞쪽 class를 찾음 <span class="txt"><span class="thumb"><img alt="" height="36" onerror="this.parentNode.style.display='none';" src="https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20130317_134%2Fyooookkkky_1363470098058jsMFR_JPEG%2F%25B1%25D7_%25B0%25DC%25BF%25EF_%25B9%25D9%25B6%25F7%25C0%25CC_%25BA%25D0%25B4%25D9_E.11_130314.%25BC%25DB%25C7%25FD%25B1%25B3_%25C6%25C7%25B5%25B5%25B6%25F3_%25C1%25F8%25C1%25D6_%25B1%25CD%25B0%25C9%25C0%25CC.jpg&amp;type=f54_54" width="36"/></span>송혜교</span></a> </div> <div class="flick_bx _tag"> <a aria-pressed="false" class="tag" href="#" onclick="submit_nq_option('%EA%B7%B8%20%EA%B2%A8%EC%9A%B8%20%EB%B0%94%EB%9E%8C%EC%9D%B4%20%EB%B6%84%EB%8B%A4%20%EC%A1%B0%EC%9D%B8%EC%84%B1', ''); return false;" role="button"> .......<반복>
img = soup.find_all(class_='thumb')
# <span class="thumb"><img alt="" height="36" onerror="this.parentNode.style.display='none';" src="https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20130317_134%2Fyooookkkky_1363470098058jsMFR_JPEG%2F%25B1%25D7_%25B0%25DC%25BF%25EF_%25B9%25D9%25B6%25F7%25C0%25CC_%25BA%25D0%25B4%25D9_E.11_130314.%25BC%25DB%25C7%25FD%25B1%25B3_%25C6%25C7%25B5%25B5%25B6%25F3_%25C1%25F8%25C1%25D6_%25B1%25CD%25B0%25C9%25C0%25CC.jpg&amp;type=f54_54" width="36"/></span>, .......<반복>
n = 1
for i in img:
    #imgUrl = i['data-source']
    imgUrl = i.find('img').attrs['src']
    # 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20130317_134%2Fyooookkkky_1363470098058jsMFR_JPEG%2F%25B1%25D7_%25B0%25DC%25BF%25EF_%25B9%25D9%25B6%25F7%25C0%25CC_%25BA%25D0%25B4%25D9_E.11_130314.%25BC%25DB%25C7%25FD%25B1%25B3_%25C6%25C7%25B5%25B5%25B6%25F3_%25C1%25F8%25C1%25D6_%25B1%25CD%25B0%25C9%25C0%25CC.jpg&type=f54_54'
    imgUrl = imgUrl.replace('https://search.pstatic.net/common/?src=', '', 1)
    imgUrl = imgUrl.replace('&type=f54_54', '', 1)
    imgUrl = parse.unquote_plus(imgUrl)
    print(n, imgUrl)
    with urlopen(imgUrl) as f:
        with open('./img/' + plusUrl + str(n) + '.jpg',
                  'wb') as h:  # w - write b - binary
            img = f.read()
            h.write(img)
    n += 1
print('다운로드 완료')
