import requests
import json
import re
def request_dandan(url,headers):
# 拿到源码
    print("开始拿源码")
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None

def parse_result(html):
    # 拿到源码就要解析，使用正则表达式获取我们想要的关键信息
    #pattern = re.compile('<li>.*?list_num.*?(d+).</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><spansclass="price_n">&yen;(.*?)</span>.*?</li>',re.S)
    #print(pattern)
    #items = re.findall(pattern, html)
    pattern = re.compile(
        '<li.*?list_num.*?(\d+)\.</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><span class="price_n">(.*?)</span>.*?</li>', re.S)
    #items = re.findall(pattern, html)
    print("pattern",pattern)
    items = re.findall(pattern,html)
    print(items)
    for item in items:
        yield{
            'range':item[0],
            'image':item[1],
            'title':item[2],
            'recommend':item[3],
            'author':item[4],
            'times':item[5],
            'price':item[6]

        }
        print("10")

def write_item_to_file(item):
    # 获取数据后，存到booK.txt
    #print('开始写入数据=====>'+str(item))
    with open('book.txt','a', encoding='UTF-8') as f:
        f.write(json.dumps(item,ensure_ascii=False)+'\n')
        f.close()



def main(page):
    print("开始爬虫")
    page = 1
    url='http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-'+str(page)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}
    html = request_dandan(url,headers)
    iterms = parse_result(html)
    #print('items is',iterms)
    for item in iterms:
        #print('item',item)
        write_item_to_file(item)

if __name__ == "__main__":
  for i in rage(1,2)
    main(i)
