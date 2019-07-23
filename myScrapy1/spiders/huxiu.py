# -*- coding: utf-8 -*-
import scrapy
from myScrapy1.items import HuxiuItem


class HuxiuSpider(scrapy.Spider):
    name = 'huxiu'
    allowed_domains = ['www.huxiu.com/']
    start_urls = ['https://www.huxiu.com/index.php/']

    def parse(self, response):
        for sel in response.xpath('//div[@class="mod-info-flow"]/div/div[@class="mob-ctt"]'):
            item = HuxiuItem()
            item['title'] = sel.xpath('h3/a/text()')[0].extract()
            item['link'] = sel.xpath('h3/a/@href')[0].extract()
            urscl = response.urljoin(item['link'])
            item['desc'] = sel.xpath('div[@class="mob-sub"]/text()')[0].extract()
            print(item['title'], item['link'], item['desc'])
