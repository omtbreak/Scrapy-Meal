import time

import scrapy
from selenium import webdriver

from kaishi.items import MealPageItem
from kaishi.items import MealItem
from kaishi.items import MenuItem



class FoodMenuSpider(scrapy.Spider):

    name='kaishi'
    start_urls=['https://www.xiachufang.com/category/']
    driver=webdriver.PhantomJS()
    foodPageHeadPageUrls=[]

    mealPageUrls=set()
    foodAuthorUrls=set()
    numberOfMeal=0
    categories=set()
    hasBeenRead=set()
    hasNotBeenRead=set()

    wohaochun = []
    def __init__(self):
        driver=self.driver
        with open('/Users/omtbreak/xiachufang/mealPageUrls.txt', 'r') as file:
            for line in file.readlines():
                self.mealPageUrls.add(line.strip('\n'))
                self.wohaochun.append(line.strip('\n'))


        with open('/Users/omtbreak/xiachufang/foodAuthorUrls.txt', 'r') as file:
            for line in file.readlines():
                self.foodAuthorUrls.add(line.strip('\n'))

        with open('/Users/omtbreak/xiachufang/category.txt','r+')as  file:
            for line in file.readlines():
                self.categories.add(line.strip('\n'))

        with open('/Users/omtbreak/xiachufang/resolutionBreakdownUrl.txt','r+')as file:
            for line in file.readlines():
                self.hasBeenRead.add(line.strip('\n'))

        with open('/Users/omtbreak/xiachufang/notread.txt','r+')as file:
            for line in file.readlines():
                self.hasNotBeenRead.add(line.strip('\n'))

    def __del__(self):
        self.driver.close()

    def start_requests(self):
        self.wohaochun.reverse()
        for url in self.wohaochun:
            url=url.strip('\n')
            yield scrapy.Request(url=url,callback=self.parseMealPage)

        '''
        for url in self.hasNotBeenRead:
            self.numberOfMeal += 1
            yield scrapy.Request(url=url,callback=self.parseMealPage)
            with open('/Users/omtbreak/kaishi/resolutionBreakdownUrl.txt','a+')as file:
                file.write(str(url)+'\n')

        '''
        '''
        for url in self.categories:
            url=url.strip('\n')
            index=url.find('/')
            #print(index)
            url='https://www.xiachufang.com/'+url[index+1:]
            #print(url)
            yield scrapy.Request(url=url,callback=self.parseFoodPage)
            print('category is on')
        '''
    def parse(self,response):

        self.driver.get(response.url)

        scripts=self.driver.find_elements_by_class_name('close')


        for script in scripts:
            try:
                script.click()
            except:
                pass

        li_menu_hrefs=response.xpath('//a[@target="_blank"]/@href')
        li_menu_names = response.xpath('//a[@target="_blank"]/text()')

        li_menus=response.xpath('//a[@target="_blank"]')


        for li_menu in li_menus:
            #print(li_menu.xpath('./@href'))
            #print(li_menu.xpath('./@href'))
            name=li_menu.xpath('./text()').extract()[0]
            href=li_menu.xpath('./@href').extract()[0]
            if href[len(href)-2].isdigit()==True:
                with open('category.txt','a+')as file:
                    file.write('种类是：'+name+'链接是'+href+'\n')
                item=MenuItem()
                item['name']=name
                item['href']=href
                self.foodPageHeadPageUrls.append(self.start_urls[0] + item['href'][10:])


        #print(self.foodPageHeadPageUrls)

        for line in self.foodPageHeadPageUrls:
            yield scrapy.Request(url=line,callback=self.parseFoodPage)





    def parseFoodPage(self, response):

        nextPageIsExist=False
        nextPageHref=None
        nextPageHrefLocation=response.xpath('//div[@class="normal-recipe-list"]/ul[@class="list"]')
        timeOfFoofLi=nextPageHrefLocation.xpath('./li')
        if timeOfFoofLi is not None:
            nextPageHrefLocation=True
            nextPageHref=response.xpath('//a[@class="next"]/@href').extract()[0]
        else:
            nextPageHrefLocation=False

        meal_locations = response.xpath('//div[@class="info pure-u"]')

        for meal_location in meal_locations:
            mealName = meal_location.xpath('./p[@class="name"]/a[@target="_blank"]/text()').extract()[0]
            mealHref = meal_location.xpath('./p[@class="name"]/a[@target="_blank"]/@href').extract()[0]
            # category=meal_location.xpath('./p[@class="ing ellipsis"]/text()').extract()[0]
            # times=meal_location.xpath('./p[@class="stats"]/span[@class="bold score"]/text()').extract()[0]
            authorName = meal_location.xpath('./p[@class="author"]/a[@class="gray-link"]/text()').extract()[0]
            authorHref = meal_location.xpath('./p[@class="author"]/a[@class="gray-link"]/@href').extract()[0]


            #给item值
            item = MealPageItem()
            item['mealName'] = mealName
            item['mealHref'] = 'https://www.xiachufang.com/'+mealHref[1:]
            # item['category']=category
            # item['times']=times
            item['authorName'] = authorName
            item['authorHref'] = 'https://www.xiachufang.com/'+authorHref[1:]

            print('https://www.xiachufang.com/'+mealHref[1:])
            print('start')
            if  item['mealHref'] not in self.mealPageUrls:
                yield scrapy.Request(url='https://www.xiachufang.com/'+mealHref[1:],callback=self.parseMealPage)
                self.numberOfMeal += 1
                self.mealPageUrls.add('https://www.xiachufang.com/' + mealHref[1:])
                with open('/Users/omtbreak/kaishi/mealPageUrls.txt', 'a+') as file:
                    file.write('https://www.xiachufang.com/' + mealHref[1:] + '\n')

                self.hasBeenRead.add('https://www.xiachufang.com/' + mealHref[1:])
                with open('/Users/omtbreak/kaishi/resolutionBreakdownUrl.txt','a+')as file:
                    file.write('https://www.xiachufang.com/' + mealHref[1:] + '\n')

                with open('foodPage.txt', 'a+') as file:
                    file.write('菜名是  ： ' + item['mealName'] + '     ' + '菜的链接   :' + item[
                        'mealHref'] + '   作者姓名是:    ' + item['authorName'] + '     作者链接是：   ' + item[
                                   'authorHref'] + '\n')
            #yield scrapy.Request(url='https://www.xiachufang.com/recipe/100450940/', callback=self.parseMealPage)
            print('end')
            #yield  scrapy.Request(url='https://www.xiachufang.com/'+authorHref[1:],callback=self.parseFoodPage)

            if 'https://www.xiachufang.com/'+authorHref[1:] not in self.foodAuthorUrls:
                self.foodAuthorUrls.add('https://www.xiachufang.com/'+authorHref[1:])
                with open('foodAuthorUrls.txt','a+') as file:
                        file.write('https://www.xiachufang.com/'+authorHref[1:]+'\n')

            print(self.numberOfMeal)
            '''print('开始')
            print(mealHref)
            print(mealName)
            print(authorName)
            print(authorHref)
            print('结束')
            '''
            yield item
            if  nextPageIsExist==True:
                yield scrapy.Request(url=nextPageHref,callback=self.parseFoodPage)


    def parseMealPage(self,response):

        mealItem = MealItem()

        #获取图片链接
        mealPictureUrl=response.xpath('//div[@class="cover image expandable block-negative-margin"]/img/@src').extract()[0]
        #with open('href.txt','a+')as file:
         #   file.write(mealPictureUrl+'\n')
        mealItem['photo']=mealPictureUrl
        '''
        #获取综合得分
        mealScore=response.xpath('//div[@class="container pos-r"]/div[@class="stats"]/div[@class="score"]/div[@class="overview"]/span[@class="number"]/text()').extract()[0]
        if mealScore==None:
           mealItem['score']=0
        else:
           mealItem['score']=mealScore
        #print(mealScore)
        '''
        #获取多少人做过
        mealTimes=response.xpath('//div[@class="cooked"]/div[@class="overview"]/span[@class="number"]/text()').extract()[0]
        mealItem['times']=mealTimes
        #print('timess======')
        #print(mealTimes)

        #简介
        mealDescription=response.xpath('//div[@class="desc"]/text()').extract()[0]
        mealItem['description']=str(mealDescription)
        #print('=====')


        #用料
        ingredients=[]
        mealIngredientsLocation=response.xpath('//div[@class="ings"]/table/tr')

        for ings in mealIngredientsLocation:
            ingItemName=ings.xpath('./td[@class="name has-border"]/text()').extract()[0].strip('\n').strip(' ')

            if ingItemName==None:
                ingItemName=ings.xpath('./td[@class="name has-border"]/a/text()').extract()[0].strip('\n').strip(' ')

            ingItemQuantity=ings.xpath('./td[@class="unit has-border"]/text()').extract()[0].strip('\n').strip(' ')
            result=ingItemName+ingItemQuantity
            ingredients.append(result)

        strIngredients = str(ingredients)
        mealItem['ingredients']=strIngredients
        strIngredients.strip('\n')
        strIngredients.strip(' ')

        #with open('a.txt','a+') as file_a:
         #   file_a.write(str(ingredients)+'\n')


        #步骤
        procedure=''
        mealStepsLocation=response.xpath('//div[@class="steps"]/ol/li[@class="container"]')
        index=0
        for step in mealStepsLocation:
            index += 1
            text='||'+str(index)+'||'+step.xpath('./p[@class="text"]/text()').extract()[0]
            procedure+=text
        mealItem['procedure']=procedure
       # with open('b.txt','a+') as file:
       #     file.write(response.url+procedure+'\n')


        title=response.xpath('//div[@class="pure-g"]/div[@class="pure-u-2-3 main-panel"]/div[@itemtype="http://schema.org/Recipe"]/h1/text()').extract()[0].strip(' ').strip('?')
        with open('/Users/omtbreak/Documents/我的菜谱/hhh/'+title+'.txt','w+') as file:
            file.write('这道菜叫'+title+ '\n这道菜的首页图片链接是'+mealPictureUrl + '\n有多少人做过：'+mealTimes + '\n简介是'+str(mealDescription) + '\n这道菜的用料有'+str(ingredients) +'\n这道菜的步骤是' +str(procedure))
            print(str(self.numberOfMeal)+'ok')
    def parseAuthorPage(self):
        pass


