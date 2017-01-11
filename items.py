# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item

class MenuItem(scrapy.Item):
    name=scrapy.Field()
    href=scrapy.Field()


class MealPageItem(scrapy.Item):
    category=scrapy.Field()#菜属于哪个类别
    mealName=scrapy.Field()#菜的名字
    times=scrapy.Field()#有多少人做过
    authorName=scrapy.Field()#作者
    mealHref=scrapy.Field()#菜的链接
    authorHref=scrapy.Field()#作者链接



class MealItem(scrapy.Item):
    photo=scrapy.Field()
    score=scrapy.Field()
    times=scrapy.Field()
    #category=scrapy.Field()
    #author=scrapy.Field()
    description=scrapy.Field()
    ingredients=scrapy.Field()
    procedure=scrapy.Field()
