import scrapy
import time
from zhihu_hot.items import ZhihuHotItem

class HotSpider(scrapy.Spider):
    name = 'hot_spider'     # 确保蜘蛛名称唯一
    allowed_domains = ['zhihu.com']  # 确保只抓取知乎域名
    def start_requests(self):
        url = "https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total?limit=50"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
            "Cookie": "_zse_ck=004_HmtZtyWCjz4md6fUKPPBgqr90TRsdonfyw=RpT5Gxjy9fZd5Gjggz...; z_c0=2|1:0|10:1753867091|4:z_c0|80:MS4xN3FmakdRQUFBQUFtQUFBQVI...; JOID=UloQBkqdJI_ajcxOVZj3H8Mn-RBIyFfBps24LCTaX72A3KN1Jg_WAreOy...; osd=VV4cAkmalIPejstKWZz0GMcr_RNPzFvFpcq8ICDZWLmM2KByIgPSAbC...; q_c1=3dd7ef20ca3f4420b5e6c9a20710c6fe|1753867053000|1753867053000; SESSIONID=WtNxAveqFy5ZUn9tKENW93dadR9ce98i9h5njQDDetx; d_c0=uuNTJBtfahqPTu8Crm-HLUqvQR7qXgvab1s=|1746595069; _zap=d3057a91-882f-461b-ad31-eecfa674a050; _xsrf=wH8afiP9gy77cRJTXElX5v6wYm2iTSI; BEC=46faae78ffea44ab7c29d705bdab5c18; HMACCOUNT=49F18439A686490F; tst=h",
            # "Referer": "https://www.zhihu.com/hot",
            # 可以根据需要加其他headers
        }
        yield scrapy.Request(url=url, headers=headers, callback=self.parse)

    def parse(self, response):
        print("开始解析知乎热榜") 
        data = response.json().get("data", [])
        for item in data:
            hot_item = ZhihuHotItem()
            target = item.get('target', {}) # 确保获取正确的目标数据
            hot_item["title"] = target.get("title")
            hot_item["url"] = f"https://www.zhihu.com/question/{item.get('card_id')}"
            hot_item["excerpt"] = target.get("excerpt")
            hot_item["hot_index"] = item.get('detail_text') 
            hot_item["timestamp"] = int(time.time())
            yield hot_item