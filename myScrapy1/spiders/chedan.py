# -*- coding: utf-8 -*-
import scrapy


class ChedanSpider(scrapy.Spider):
    name = 'chedan'
    allowed_domains = ['www.yinwang.org']
    start_urls = ['http://www.yinwang.org/#']

    def parse(self, response):
        for each in response.xpath("//li[@class='list-group-item title']"):
            print(each.xpath("a/text()").extract()[0])



