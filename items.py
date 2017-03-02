# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy



class MealItem(scrapy.Item):
    #1,照片链接
    photoUrl=scrapy.Field()
    #2，菜的评分
    score=scrapy.Field()
    #3，有多少人做过
    times=scrapy.Field()
    #4，菜的类别
    category=scrapy.Field()
    #5，作者链接
    authorUrl=scrapy.Field()
    #6，作者名字
    authorName=scrapy.Field()
    #7，菜的简介
    description=scrapy.Field()
    #8，菜的材料
    ingredients=scrapy.Field()
    #9，做菜步骤
    procedure=scrapy.Field()

class AuthorItem(scrapy.Field):
    #1, 作者名字
    authorTitle=scrapy.Field()
    #2, 作者性别
    authorSexuality=scrapy.Field()
    #3，作者城市定位
    authorLocation=scrapy.Field()
    #4，作者工作
    authorJob=scrapy.Field()
    #5，加入下厨房日期
    authorJoinDate=scrapy.Field()
    #6，作者新浪微博URL
    #authorWeiBoUrl=scrapy.Field()
    #7，作者简介
    authorDescription=scrapy.Field()
    #8，作者关注的用户数量
    authorFollowing=scrapy.Field()
    #9，关注作者的用户数量
    authorFollower=scrapy.Field()
    #10，作者头像URL
    authorImageUrl=scrapy.Field()


