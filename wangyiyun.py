import requests
from lxml import etree
from  bs4 import BeautifulSoup
import time
import pandas as pd
import openpyxl


user_agent = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}
urls = []

def Url(number):

    for i in range(1,number+1):
        url = f'https://www.musicbooks.cn/page/{i}'
        urls.append(url)
    return urls




def res_text(url,user_agent):
    res = requests.get(url,user_agent)
    print(res.status_code)
    #     count += 1
    #     print(f"第{count}爬取正常")
    return res.text



# def SoUp(html):
#     soup = BeautifulSoup(html,"lxml")
#     reping = soup.find_all(itemprop="articleBody")
#     return reping

def Path(html):
    a = etree.HTML(html)
    reping = a.xpath('//html/body/section/div/div/article[*]/main/p/text()')
    # reping = a.xpath('//p/text()')
    return reping
# /html/body/section/div/div/article[3]/main/p/text()
# /html/body/section/div/div/article[10]/main/p/text()

def neirong(reping):
    for i in reping:
        # rp = i.string.lstrip()
        rp = i.lstrip()
        print(rp)
        return rp
# itemprop="articleBody"


urls = Url(10)
#print(urls)
rps = []
for url in urls:
    print(url)
    time.sleep(1)
    html = res_text(url,user_agent)
    #print(html)
    # nr = SoUp(html) #使用bs4解析
    nr = Path(html) #使用xpath解析
    rpres = neirong(nr)
    # print(rpres)
    # rps.append(rpres)

    #

# print(rps)

    # total = {"热评内容":rps}
    # info = pd.DataFrame(total)
    # writer = pd.ExcelWriter("//mnt/e/python/wslProject/网易云热评.xlsx")
    # info.to_excel(writer, sheet_name="前10页")
    writer.save()