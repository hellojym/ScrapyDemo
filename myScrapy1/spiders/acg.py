# -*- coding: utf-8 -*-
import scrapy
from myScrapy1.items import AcgItem


class AcgSpider(scrapy.Spider):
    name = 'acg'
    allowed_domains = ['acg.fi']
    start_urls = ['http://acg.fi/']

    # 全文搜索id为main下的class为xxx的元素
    reg1 = "//*[@id=\"main\"]//div[@class='preview thumb-in']"
    reg2 = "//div[@class='preview thumb-in']"
    reg3 = "//*[@id=\"main\"]/div[2]//div[@class='preview thumb-in']"
    reg4 = "//*[@id=\"main\"]/div[2]/div]"

    def parse(self, response):
        items = []
        # 先定位到列表
        location = response.xpath("//*[@id=\"main\"]/div[2]")[0]
        for each in location.xpath("div"):
            print("____________________________________________________")
            item = AcgItem()
            # title
            title = each.xpath("div/div[2]/h2/a/text()").extract_first()
            if title:
                print("title:  %s" % title)
                item['title'] = title
                items.append(item)
            # image-background
            background_div = each.xpath("div/div[1]/div")
            background_temp = background_div.xpath("@style").extract_first()
            if background_temp:
                background = background_temp.split("\'")[1]
                item['bg'] = background
                print("picUrl:  %s" % background)

        return items

    # 如果仅仅需要图片的话，用这个
    # def parse(self, response):
    #     items = []
    #     for each in response.xpath(self.reg3):
    #         print("____________________________________________________")
    #         temp = each.xpath("@style").extract_first()
    #         if temp:
    #             background = temp.split("\'")[1]
    #             print("picUrl:  %s" % background)
    #             item = AcgItem()
    #             item.background = background
    #             items.append(item)
    #             print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n")
    # // *[ @ id = "main"] / div[2] / div[2] / div / div[1]
