# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# 传智播客
class ItCastItem(scrapy.Item):
    name = scrapy.Field()
    title = scrapy.Field()
    info = scrapy.Field()


# acg
class AcgItem(scrapy.Item):
    title = scrapy.Field()
    bg = scrapy.Field()
