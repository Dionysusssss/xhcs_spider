import scrapy
from scrapy.selector import Selector
from xhcs_2520.items import Xhcs2520Item
import datetime

class MySpider(scrapy.Spider):

    name = "spider_xhcs_S32750"
    allowed_domains = ["xhcs.com"]
    start_urls = ["http://www.xhcs.com/search/search/shap/102/tsc/1/hdm/2520/p/1.shtml"]
    pageNum = 1
    init_urls = "http://www.xhcs.com/search/search/shap/102/tsc/1/hdm/2520/p/"
    global allpage

    def parse(self, response):
        selector = Selector(response)
        item_list = selector.xpath("//*[@id='slisttable']/tbody")
        allpage = eval(selector.xpath('/html/body/div[4]/div[1]/div[1]/span[1]//text()').extract_first()[-6:-2].strip('/'))
        for tr in item_list[1:]:
            item = Xhcs2520Item()
            item['grade'] = tr.xpath('./tr/td[2]//text()').extract_first()
            item['size'] = tr.xpath('./tr/td[3]//text()').extract_first()
            item['quantity'] = tr.xpath('./tr/td[4]//text()').extract_first()
            item['weight'] = tr.xpath('./tr/td[5]//text()').extract_first()
            item['company'] = tr.xpath('./tr/td[6]/a//text()').extract_first()
            item['area'] = tr.xpath('./tr/td[7]//text()').extract_first()
            item['date'] = str(datetime.date.today())
            yield item

        if self.pageNum <= allpage-1:
            self.pageNum += 1
            new_url = self.init_urls + str(self.pageNum)
            yield scrapy.Request(url=new_url, callback=self.parse)
