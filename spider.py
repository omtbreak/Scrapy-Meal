import scrapy
from secondEdtionXiachufang.spiders.error import errorTxt
import time


class SecondEditionSpider(scrapy.Spider):

    name = 'second'
    #start_urls=['http://www.xiachufang.com/cook/100079753/']
    start_urls=['http://www.xiachufang.com/cook/103249930/']
    #start_urls=['http://www.xiachufang.com/cook/112985975/rl_created/']
    #start_urls=['http://www.xiachufang.com/recipe/102202553/']

    #已经在网页中获取到的作者链接
    hasBeenExtractedAuthorUrls=set()
    #已经抓取下来的作者链接
    hasBeenCrawledAuthorUrls=set()

    #已经在网页中获取到的菜的链接
    hasBeenExtractedMealUrls=set()
    #已经抓取下来的菜的链接
    hasBeenCrawledMealUrls=set()

    #已经在网页中获取到的created的链接
    hasBeenExtractedCreatedMealUrls=set()
    #已经抓取到的created的链接
    hasBeenCrawledCreatedMealUrls = set()

    #已经获取到网页中cooked的链接
    hasBeenExtractedCookedMealUrls=set()
    #已经抓取玩信息的cooked的链接
    hasBeenCrawledCookedMealUrls=set()

    #已经获取到网页中createdMenus的链接
    hasBeenExtractedCreatedMenuUrls=set()
    #已经抓取到createdMenus的信息的链接
    hasBeenCrawledCreatedMenuUrls=set()

    #已经获取到网页中collectededMenus的链接
    hasBeenExtractedCollectedMenuUrls = set()
    #已经抓取到collectedMenus的信息的链接
    hasBeenCrawledCollectedMenuUrls = set()

    # 已经获取到网页中collecteded的菜的链接
    hasBeenExtractedCollectedMealUrls = set()
    # 已经抓取到collectedMenus的菜的链接
    hasBeenCrawledCollectedMealUrls = set()

    # 作者关注的
    hasBeenExtractedFollowingUrls = set()
    # 作者关注的
    hasBeenCrawledFollowingUrls = set()

    # 关注作者的
    hasBeenExtractedFollowedUrls = set()
    # 关注作者的
    hasBeenCrawledFollowedUrls = set()
    import scrapy
    from secondEdtionXiachufang.spiders.error import errorTxt
    import time

    class SecondEditionSpider(scrapy.Spider):

        name = 'second'
        # start_urls=['http://www.xiachufang.com/cook/100079753/']
        start_urls = ['http://www.xiachufang.com/cook/103249930/']
        # start_urls=['http://www.xiachufang.com/cook/112985975/rl_created/']
        # start_urls=['http://www.xiachufang.com/recipe/102202553/']

        # 已经在网页中获取到的作者链接
        hasBeenExtractedAuthorUrls = set()
        # 已经抓取下来的作者链接
        hasBeenCrawledAuthorUrls = set()

        # 已经在网页中获取到的菜的链接
        hasBeenExtractedMealUrls = set()
        # 已经抓取下来的菜的链接
        hasBeenCrawledMealUrls = set()

        # 已经在网页中获取到的created的链接
        hasBeenExtractedCreatedMealUrls = set()
        # 已经抓取到的created的链接
        hasBeenCrawledCreatedMealUrls = set()

        # 已经获取到网页中cooked的链接
        hasBeenExtractedCookedMealUrls = set()
        # 已经抓取玩信息的cooked的链接
        hasBeenCrawledCookedMealUrls = set()

        # 已经获取到网页中createdMenus的链接
        hasBeenExtractedCreatedMenuUrls = set()
        # 已经抓取到createdMenus的信息的链接
        hasBeenCrawledCreatedMenuUrls = set()

        # 已经获取到网页中collectededMenus的链接
        hasBeenExtractedCollectedMenuUrls = set()
        # 已经抓取到collectedMenus的信息的链接
        hasBeenCrawledCollectedMenuUrls = set()

        # 已经获取到网页中collecteded的菜的链接
        hasBeenExtractedCollectedMealUrls = set()
        # 已经抓取到collectedMenus的菜的链接
        hasBeenCrawledCollectedMealUrls = set()

        # 作者关注的
        hasBeenExtractedFollowingUrls = set()
        # 作者关注的
        hasBeenCrawledFollowingUrls = set()

        # 关注作者的
        hasBeenExtractedFollowedUrls = set()
        # 关注作者的
        hasBeenCrawledFollowedUrls = set()

        def __init__(self):
            with open('/Users/omtbreak/Desktop/track/hasBeenCrawledAuthorUrls.txt', 'r+')as file:
                for line in file.readlines():
                    self.hasBeenCrawledAuthorUrls.add(line.strip('\n'))

            with open('/Users/omtbreak/Desktop/track/hasBeenCrawledMealUrls.txt', 'r+')as file:
                for line in file.readlines():
                    self.hasBeenCrawledMealUrls.add(line.strip('\n'))

            with open('/Users/omtbreak/Desktop/track/hasBeenCrawledCreatedMealUrls.txt', 'r+')as file:
                for line in file.readlines():
                    self.hasBeenCrawledCreatedMealUrls.add(line.strip('\n'))

            with open('/Users/omtbreak/Desktop/track/hasBeenCrawledCookedMealUrls.txt', 'r+')as file:
                for line in file.readlines():
                    self.hasBeenCrawledCookedMealUrls.add(line.strip('\n'))

            with open('/Users/omtbreak/Desktop/track/hasBeenCrawledCreatedMenuUrls.txt', 'r+')as file:
                for line in file.readlines():
                    self.hasBeenCrawledCreatedMenuUrls.add(line.strip('\n'))

            with open('/Users/omtbreak/Desktop/track/hasBeenCrawledCollectedMenuUrls.txt', 'r+')as file:
                for line in file.readlines():
                    self.hasBeenCrawledCollectedMealUrls.add(line.strip('\n'))

            with open('/Users/omtbreak/Desktop/track/hasBeenCrawledFollowingUrls.txt', 'r+')as file:
                for line in file.readlines():
                    self.hasBeenCrawledFollowingUrls.add(line.strip('\n'))
            with open('/Users/omtbreak/Desktop/track/hasBeenCrawledFollowedUrls.txt', 'r+')as file:
                for line in file.readlines():
                    self.hasBeenCrawledFollowedUrls.add(line.strip('\n'))
            print('start')
            print(len(self.hasBeenCrawledAuthorUrls))
            print(len(self.hasBeenCrawledMealUrls))
            print('end')

            pass

        def parse(self, response):
            print(response.url)
            print('parse')
            yield scrapy.Request(url=response.url, callback=self.processAuthorInformation)

        def processAuthorInformation(self, response):
            print('processAuthorInformation')
            self.hasBeenExtractedAuthorUrls.add(response.url)
            with open('/Users/omtbreak/Desktop/track/hasBeenExtractedAuthorUrls.txt', 'a+')as file:
                file.write(response.url + '\n')

            # 获取作者的title
            rawAuthorTitle = response.xpath(
                '//div[@class="page-outer"]/div[@class="page-container"]/div[@class="pure-g pb40"]/div[@class="pure-u-5-8 font12 pr30"]/h1[@class="page-title mb10"]/text()').extract()[
                0]
            authorTitle = rawAuthorTitle.strip('\n').strip(' ').strip('\n')
            print(authorTitle)

            # 性别，加入日期和坐标都是在一个div里
            SWDL = response.xpath(
                '//div[@class="page-outer"]/div[@class="page-container"]/div[@class="pure-g pb40"]/div[@class="pure-u-5-8 font12 pr30"]/div[@class="gray-font"]')

            # 获取作者加入日期
            try:
                authorJoinDate = SWDL.xpath('//span[@class="display-inline-block"]/text()').extract()[0].strip(
                    '加入').strip(' ')
            except Exception:
                authorJoinDate = ''

            allProvince = ['北京', '天津', '河北', '河南', '山东', '山西', '广东', '广西', '湖南', '湖北', '上海', '内蒙', '辽宁', '吉林', '黑龙江',
                           '江苏', '浙江', '福建', '安徽', '江西', '海南', '重庆', '四川', '贵州', '云南', '西藏', '陕西', '甘肃', '青海', '宁夏',
                           '新疆', '香港', '澳门', '台湾', '海外']
            authorLocations = []
            authorSexuality = ''
            authorJob = ''
            # 获取作者性别和城市列表
            block = SWDL.xpath('//span[@class="mr10 display-inline-block"]/text()')
            for item in block:
                temp = item.extract()
                if temp in ('男', '女', '其他'):
                    authorSexuality = temp
                else:
                    isLocation = False
                    for province in allProvince:
                        if temp.find(province) != -1:
                            authorLocations.append(temp)
                            isLocation = True
                            break
                    if isLocation == False:
                        authorJob = temp
            numberOfCities = len(authorLocations)

            # 获取作者简介
            authorDescription = ''
            authorDescriptionDiv = response.xpath('//div[@class="people-base-desc dark-gray-font mt10"]')
            # self.logger.info(authorDescriptionDiv.xpath('./text()').extract())
            for item in authorDescriptionDiv.xpath('./text()').extract():
                authorDescription += item.strip('\r')
            # print(authorDescription)

            # print('======'+str(authorDescriptionDiv.extract()))


            # 获取作者被关注的数量以及关注作者的用户主页链接
            authorFollowedDiv = response.xpath(
                '//div[@class="page-outer"]/div[@class="page-container"]/div[@class="pure-g pb40"]/div[@class="pure-u-1-6 align-center people-base-right pos-r"]/div[@class="follow-wrap block-bg p10 pl15 pr15 pure-g w100"]/div[@class="pure-u-1-2"]/div')
            authorFollowedUrl = ''
            init = 0
            authorFollowed = ''
            for item in authorFollowedDiv:
                if init == 1:
                    authorFollowed = item.xpath('./a/text()').extract()[0]
                    authorFollowedUrl = 'http://www.xiachufang.com' + item.xpath('./a/@href').extract()[0]
                else:
                    init += 1
            # print("followed------------"+authorFollowed)
            # print('followedUrl---------'+authorFollowedUrl)

            # 获取作者关注的人数数量以及作者关注用户主页链接

            authorFollowingDiv = response.xpath(
                '//div[@class="page-outer"]/div[@class="page-container"]/div[@class="pure-g pb40"]/div[@class="pure-u-1-6 align-center people-base-right pos-r"]/div[@class="follow-wrap block-bg p10 pl15 pr15 pure-g w100"]/div[@class="pure-u-1-2 following-num"]/div')
            init = 0
            authorFollowing = ''
            authorFollowingUrl = ''
            for item in authorFollowingDiv:
                if init == 1:
                    authorFollowing = item.xpath('./a/text()').extract()[0]
                    authorFollowingUrl = 'http://www.xiachufang.com' + item.xpath('./a/@href').extract()[0]
                else:
                    init += 1
            # print("following------------"+authorFollowing)
            # print('follownigUrl----------'+authorFollowingUrl)


            # 获取作者头像的链接
            authorImageUrl = response.xpath('//div[@class="page-outer"]/div[@class="page-container"]/div[@class="pure-g pb40"]/div[@class="pure-u-5-24 people-base-left"]/img/@src').extract()[0]
            # print('image-------' + str(authorImageUrl))

            print('processAuthorInformation')
            with open('/Users/omtbreak/Desktop/Author/' + authorTitle + '.txt', 'a+')as file:
                file.write(
                    '1, 作者名字是： ' + authorTitle + '\n' + '2, 作者性别是: ' + authorSexuality + '\n' + '3, 作者的职业是： ' + authorJob + '\n' + '4, 作者加入日期是： ' + authorJoinDate + '\n')
                if numberOfCities == 1:
                    file.write('5, 作者所在城市有： ' + authorLocations[0] + '\n')
                elif numberOfCities == 2:
                    file.write('5, 作者所在城市有： ' + authorLocations[0] + ' 和 ' + authorLocations[1] + '\n')
                file.write(
                    '6, 作者简介是： ' + authorDescription + '\n' + '7, 关注作者的用户数量是： ' + authorFollowed + '\n' + '8, 关注作者的用户主页链接是： ' + authorFollowedUrl + '\n')
                file.write(
                    '9, 作者关注的用户数量是： ' + authorFollowing + '\n' + '10, 作者关注的用户主页链接是: ' + authorFollowingUrl + '\n')
                file.write('11, 作者头像的链接是： ' + authorImageUrl + '\n')

            self.hasBeenCrawledAuthorUrls.add(response.url)
            with open('/Users/omtbreak/Desktop/track/hasBeenCrawledAuthorUrls.txt', 'a+')as file:
                file.write(response.url + '\n')

            # 获取作者原创的作品,作品，菜单，收藏主页链接,第一个是概况没什么用
            authorCreatedMeals = response.url + 'created/'
            authorCookedMeals = response.url + 'cooked/'
            authorRecipeList = response.url + 'recipe_list/'
            authorCollected = response.url + 'collected/'
            authorCreatedMeunList = response.url + 'rl_created/'
            authorCollectedMenuList = response.url + 'rl_collected/'

            time.sleep(0.3)
            print('createdMeals =======')
            yield scrapy.Request(url=authorCreatedMeals, callback=self.processCreated)
            self.hasBeenCrawledCreatedMealUrls.add(authorCreatedMeals)

            time.sleep(0.3)
            print('cookedMeals ====')
            yield scrapy.Request(url=authorCookedMeals, callback=self.processCooked)

            time.sleep(0.3)
            print('createdMenu====')
            yield scrapy.Request(url=authorCreatedMeunList, callback=self.processCreatedMenus)

            time.sleep(0.3)
            print('collectedMenu====')
            yield scrapy.Request(url=authorCollectedMenuList, callback=self.processCollectedMenus)

            time.sleep(0.3)
            print('collectedMeals====')
            yield scrapy.Request(url=authorCollected, callback=self.processCollected)

            time.sleep(0.3)
            print('following====')
            yield scrapy.Request(url=authorFollowingUrl, callback=self.processFollowings)

            time.sleep(0.3)

            print('followed====')
            yield scrapy.Request(url=authorFollowedUrl, callback=self.processFollowers)

        def processCreated(self, response):
            print('processCreated')
            print(response.url)
            if response.url not in self.hasBeenCrawledCreatedMealUrls:
                self.hasBeenExtractedCreatedMealUrls.add(response.url)
                with open('/Users/omtbreak/Desktop/track/hasBeenExtractedCreatedMealUrls.txt', 'a+')as file:
                    file.write(response.url + '\n')
                # 作者所有创作的菜的链接保存在createdMeals中
                createdMealUrls = []
                print('processCreated')
                # 获取本页的所有菜的链接
                mealLis = response.xpath(
                    '//div[@class="people-created-main"]/div[@class="block"]/div[@class="ias-container"]/div[@class="recipes-280-full-width-list"]/ul[@class="plain pure-g"]/li')
                # errorTxt(str(mealLis))
                for li in mealLis:
                    createdMealUrls.append('http://www.xiachufang.com' + li.xpath(
                        './div[@class="recipe-280 white-bg"]/p[@class="name ellipsis red-font"]/a/@href').extract()[0])
                    # errorTxt('http://www.xiachufang.com'+li.xpath('./div[@class="recipe-280 white-bg"]/p[@class="name ellipsis red-font"]/a/@href').extract()[0]+'\n')

                for url in createdMealUrls:
                    if url not in self.hasBeenCrawledMealUrls:
                        time.sleep(0.3)

                        yield scrapy.Request(url=url, callback=self.processMealPage)
                self.hasBeenCrawledCreatedMealUrls.add(response.url)
                with open('/Users/omtbreak/Desktop/track/hasBeenCrawledCreatedMealUrls.txt', 'a+')as file:
                    file.write(response.url + '\n')

                # 获取下一页的链接
                try:
                    nextPageUrl = 'http://www.xiachufang.com' + response.xpath(
                        '//div[@class="page-outer"]/div[@class="page-container"]/div[@class="people-created-main"]/div[@class="pager ias-pager"]/a[@class="next"]/@href').extract()[
                        0]
                    yield scrapy.Request(url=nextPageUrl, callback=self.processCreated)
                except Exception:
                    print('no more created')
                    # print(nextPageUrl)
                    # print(createdMeals)

        # def parse(self, response):
        def processCooked(self, response):
            print('processCooked')
            print(response.url)
            if response.url not in self.hasBeenCrawledCookedMealUrls:
                self.hasBeenExtractedCookedMealUrls.add(response.url)
                with open('/Users/omtbreak/Desktop/track/hasBeenExtractedCookedMealUrls.txt', 'a+')as file:
                    file.write(response.url + '\n')

                print('processCooked')
                # 作者所有做过的菜都存在cookedMeals中
                cookedMealUrls = []
                # 获取本页的所有菜的链接
                mealLis = response.xpath(
                    '//div[@class="page-outer"]/div[@class="page-container"]/div[@class="people-cooked-main"]/div[@class="ias-container"]/div[@class="dishes-280-full-width-list"]/ul[@class="plain pure-g"]/li')
                for li in mealLis:
                    cookedMealUrls.append('http://www.xiachufang.com' + li.xpath(
                        './div[@class="dish-280 dish-280-no-author white-bg"]/p[@class="name ellipsis red-font"]/a/@href').extract()[
                        0])
                    # print('http://www.xiachufang.com'+li.xpath('./div[@class="dish-280 dish-280-no-author white-bg"]/p[@class="name ellipsis red-font"]/a/@href').extract()[0])

                for url in cookedMealUrls:
                    time.sleep(0.3)
                    yield scrapy.Request(url=url, callback=self.processDishToRecipe)
                    # errorTxt(url+'\n')
                self.hasBeenCrawledCookedMealUrls.add(response.url)
                with open('/Users/omtbreak/Desktop/track/hasBeenCrawledCookedMealUrls.txt', 'a+')as file:
                    file.write(response.url + '\n')
                try:
                    nextPageUrl = 'http://www.xiachufang.com' + response.xpath(
                        '//div[@class="page-outer"]/div[@class="page-container"]/div[@class="people-cooked-main"]/div[@class="pager ias-pager"]/a[@class="next"]/@href').extract()[
                        0]
                    # errorTxt(nextPageUrl)
                    yield scrapy.Request(url=nextPageUrl, callback=self.processCooked)
                except Exception:
                    pass

        # 因为从cooked的页面的得到的菜的链接是dish的，所以要从dish转到recipe，但是有可能在dish中找不到recipe，因为作者并没有发布菜
        # 但是从dish得到的链接也可能不是recipe，有很多都是event
        # def parse(self, response):
        def processDishToRecipe(self, response):
            print('processDishToRecipe')
            print(response.url)
            recipeUrl = ''
            eventUrl = ''
            try:
                recipeOrEventUrlAs = response.xpath(
                    '//div[@class="page-outer"]/div[@class="page-container"]/div[@class="pure-g"]/div[@class="pure-u-2-3 main-panel"]/div[@class="dish-show block block-has-padding white-bg"]/div[@class="pure-g dish-info"]/div[@class="pure-u"]/div[@class="pure-g"]/div[@class="pure-u dish-user-info"]/div[@class="gray-font"]/a')
                for a in recipeOrEventUrlAs:
                    temp = a.xpath('./@href').extract()[0]
                    if temp.find('recipe'):
                        recipeUrl = 'http://www.xiachufang.com' + temp
                        if recipeUrl not in self.hasBeenCrawledMealUrls:
                            yield scrapy.Request(url=recipeUrl, callback=self.processMealPage)
                            time.sleep(0.3)
                    elif temp.find('event'):
                        eventUrl = 'http://www.xiachufang.com' + temp
                        pass
                print(recipeUrl)
                print(eventUrl)
                print('exist')
            except Exception:
                print('no exist')

        # 找到作者的createdMenuList并找到作者创建的菜单或者作者收藏的菜单的链接
        def processCreatedMenus(self, response):
            print('processCreatedMenus')
            print(response.url)
            # def parse(self, response):
            if response.url not in self.hasBeenCrawledCreatedMenuUrls:
                self.hasBeenExtractedCreatedMenuUrls.add(response.url)
                with open('/Users/omtbreak/Desktop/track/hasBeenExtractedCreatedMenuUrls.txt', 'a+')as file:
                    file.write(response.url + '\n')
                print('processCreatedMenus')
                # 作者创建的菜单的链接
                menuCreatedUrls = []
                menuList = response.xpath(
                    '//div[@class="page-outer"]/div[@class="page-container"]/div[@class="block white-bg p40"]/div[@class="menu-list"]/ul[@class="plain"]/li')
                for menuLi in menuList:
                    menuCreatedUrls.append('http://www.xiachufang.com' + menuLi.xpath('./a/@href').extract()[0])

                for url in menuCreatedUrls:
                    # errorTxt(url)
                    print('createdMenus')
                    yield scrapy.Request(url=url, callback=self.processMealsInCreatedMenu)
                self.hasBeenCrawledCreatedMenuUrls.add(response.url)
                with open('/Users/omtbreak/Desktop/track/hasBeenCrawledCreatedMenuUrls.txt', 'a+')as file:
                    file.write(response.url + '\n')
                try:
                    nextPageUrl = 'http://www.xiachufang.com' + response.xpath(
                        '//div[@class="page-outer"]/div[@class="page-container"]/div[@class="block white-bg p40"]/div[@class="menu-list"]/div[@class="pager"]/a[@class="next"]/@href').extract()[
                        0]
                    yield scrapy.Request(url=nextPageUrl, callback=self.processCreatedMenus)

                except Exception:
                    print('no next page')
                    pass

        def processCollectedMenus(self, response):
            print('processCollectedMenus')
            print(response.url)
            if response.url not in self.hasBeenCrawledCollectedMenuUrls:
                self.hasBeenExtractedCollectedMenuUrls.add(response.url)
                with open('/Users/omtbreak/Desktop/track/hasBeenExtractedCollectedMenuUrls.txt', 'a+')as file:
                    file.write(response.url + '\n')
                print('prcessCollectedMenus')
                # 作者收藏的菜单的链接
                menuCollectedUrls = []
                menuList = response.xpath(
                    '//div[@class="page-outer"]/div[@class="page-container"]/div[@class="block white-bg p40"]/div[@class="menu-list"]/ul[@class="plain"]/li')
                for menuLi in menuList:
                    menuCollectedUrls.append('http://www.xiachufang.com' + menuLi.xpath('./a/@href').extract()[0])

                for url in menuCollectedUrls:
                    # errorTxt(url)
                    print('collectedMenus')
                    yield scrapy.Request(url=url, callback=self.processMealsInCollectedMenu)
                self.hasBeenCrawledCollectedMenuUrls.add(response.url)
                with open('/Users/omtbreak/Desktop/track/hasBeenCrawledCollectedMenuUrls.txt', 'a+')as file:
                    file.write(response.url + '\n')
                try:
                    nextPageUrl = 'http://www.xiachufang.com' + response.xpath(
                        '//div[@class="page-outer"]/div[@class="page-container"]/div[@class="block white-bg p40"]/div[@class="menu-list"]/div[@class="pager"]/a[@class="next"]/@href').extract()[
                        0]
                    yield scrapy.Request(url=nextPageUrl, callback=self.processCollectedMenus)

                except Exception:
                    print('no next page')
                    pass

        # 处理作者创建的菜单中的菜，找到这些菜的链接
        # def parse(self, response):
        def processMealsInCreatedMenu(self, response):
            print('processMealsInCreatedMenu')
            print(response.url)
            mealsInCreatedMenu = []
            mealLis = response.xpath(
                '//div[@class="page-outer"]/div[@class="page-container"]/div[@class="pure-g"]/div[@class="pure-u-2-3 main-panel"]/div[@class="block block-has-padding white-bg rl-show"]/div[@class="rl-recipes"]/div[@class="normal-recipe-list"]/ul[@class="plain"]/li')
            for mealLi in mealLis:
                mealUrl = 'http://www.xiachufang.com' + mealLi.xpath(
                    './div[@class="recipe-140-horizontal pure-g"]/div[@class="info pure-u"]/p[@class="name"]/a/@href').extract()[
                    0]
                # errorTxt(str(mealLi.xpath('./div[@class="recipe-140-horizontal pure-g"]/div[@class="info pure-u"]/p[@class="name"]/a/text()').extract()[0])+'\n')
                # errorTxt(mealUrl+'\n')
                mealsInCreatedMenu.append(mealUrl)
            for url in mealsInCreatedMenu:
                if url not in self.hasBeenCrawledMealUrls:
                    print('mealsInCreatedMenu')
                    yield scrapy.Request(url=url, callback=self.processMealPage)
            try:
                nextPageUrl = 'http://www.xiachufang.com' + response.xpath(
                    '//div[@class="page-outer"]/div[@class="page-container"]/div[@class="pure-g"]/div[@class="pure-u-2-3 main-panel"]/div[@class="block block-has-padding white-bg rl-show"]/div[@class="rl-recipes"]/div[@class="normal-recipe-list"]/div[@class="pager"]/a[@class="next"]/@href').extract()[
                    0]
                # errorTxt(nextPageUrl+'\n')
                yield scrapy.Request(url=nextPageUrl, callback=self.processMealsInCreatedMenu)
            except Exception:
                pass

        # 处理作者收藏的菜单中的其他作者链接和菜单中的菜
        # def parse(self, response):
        def processMealsInCollectedMenu(self, response):
            print('processMealsInCollectedMenu')
            print(response.url)
            # 其他作者的链接
            otherAuthorLink = ''
            try:
                otherAuthorLink = 'http://www.xiachufang.com' + response.xpath(
                    '//div[@class="page-outer"]/div[@class="page-container"]/div[@class="pure-g"]/div[@class="pure-u-2-3 main-panel"]/div[@class="block block-has-padding white-bg rl-show"]/div[@class="rl-summary block block-has-padding block-bg block-negative-margin small-font"]/div[@class="pure-g"]/div[@class="pure-u-1-2"]/a[@class="avatar-link"]/@href').extract()[
                    0]
                # print(otherAuthorLink)
            except Exception:
                pass

            mealsInCollectedMenu = []
            mealLis = response.xpath(
                '//div[@class="page-outer"]/div[@class="page-container"]/div[@class="pure-g"]/div[@class="pure-u-2-3 main-panel"]/div[@class="block block-has-padding white-bg rl-show"]/div[@class="rl-recipes"]/div[@class="normal-recipe-list"]/ul[@class="plain"]/li')

            for mealLi in mealLis:
                mealUrl = 'http://www.xiachufang.com' + mealLi.xpath(
                    './div[@class="recipe-140-horizontal pure-g"]/div[@class="info pure-u"]/p[@class="name"]/a/@href').extract()[
                    0]
                mealsInCollectedMenu.append(mealUrl)
                errorTxt(mealUrl + '\n')
            for url in mealsInCollectedMenu:
                if url not in self.hasBeenCrawledMealUrls:
                    print('mealsInCollectedMenu')
                    yield scrapy.Request(url=url, callback=self.processMealPage)

            try:
                nextPageUrl = 'http://www.xiachufang.com' + response.xpath(
                    '//div[@class="page-outer"]/div[@class="page-container"]/div[@class="pure-g"]/div[@class="pure-u-2-3 main-panel"]/div[@class="block block-has-padding white-bg rl-show"]/div[@class="rl-recipes"]/div[@class="normal-recipe-list"]/div[@class="pager"]/a[@class="next"]/@href').extract()[
                    0]
                # errorTxt(nextPageUrl+'\n')
                yield scrapy.Request(url=nextPageUrl, callback=self.processMealsInCollectedMenu)
            except Exception:
                print('no next page')
                pass

            yield scrapy.Request(url=otherAuthorLink, callback=self.processAuthorInformation)

        # 处理作者收藏的菜，我并不确定每个分类的中的菜是否有重复的，所以就全都抓下来，当然在抓的过程中有判重机制
        # def parse(self, response):
        def processCollected(self, response):
            print('processCollected')
            self.hasBeenExtractedCollectedMealUrls.add(response.url)
            with open('/Users/omtbreak/Desktop/track/hasBeenExtractedCollectedMealUrls.txt', 'a+')as file:
                file.write(response.url + '\n')
            # meals保存每一页中所有菜的链接
            meals = []

            mealLis = response.xpath(
                '//div[@class="page-outer"]/div[@class="page-container"]/div[@class="block white-bg pure-g people-collected-main"]/div[@class="pure-u-19-24 people-collected-recipes"]/ul[@class="plain p30 pl40"]/li')
            for mealLi in mealLis:
                mealUrl = 'http://www.xiachufang.com' + mealLi.xpath(
                    './div[@class="pure-g pos-r"]/div[@class="pure-u-19-24 pl20 gray-font font12"]/div[@class="font16"]/a/@href').extract()[
                    0]
                # errorTxt(mealUrl+'\n')
                meals.append(mealUrl)

            for url in meals:
                if url not in self.hasBeenCrawledMealUrls:
                    time.sleep(0.3)
                    yield scrapy.Request(url=url, callback=self.processMealPage)
            self.hasBeenCrawledCollectedMealUrls.add(response.url)
            with open('/Users/omtbreak/Desktop/track/hasBeenCrawledCollectedMealUrls.txt', 'a+')as file:
                file.write(response.url + '\n')
            try:
                nextPageUrl = 'http://www.xiachufang.com' + response.xpath(
                    '//div[@class="page-outer"]/div[@class="page-container"]/div[@class="block white-bg pure-g people-collected-main"]/div[@class="pure-u-19-24 people-collected-recipes"]/div[@class="pager"]/a[@class="next"]/@href').extract()[
                    0]
                # errorTxt(nextPageUrl)
                print('times')
                yield scrapy.Request(url=nextPageUrl, callback=self.parse)
            except Exception:
                print('no next page')
                pass

        # 处理作者关注的所有人的链接
        def processFollowings(self, response):
            print('processFollowing')
            self.hasBeenExtractedFollowingUrls.add(response.url)
            with open('/Users/omtbreak/Desktop/track/hasBeenExtractedFollowingUrls.txt', 'a+')as file:
                file.write(response.url + '\n')
            # 所有作者关注的其他作者的链接都保存在followingAuthors中
            followingAuthorUrls = []

            followingAuthorLis = response.xpath(
                '//div[@class="page-outer"]/div[@class="page-container"]/div[@class="block p40 white-bg"]/ul[@class="plain people-follow-list"]/li')
            for followingAuthorLi in followingAuthorLis:
                followingAuthorUrl = 'https://www.xiachufang.com' + followingAuthorLi.xpath(
                    './div[@class="pure-g"]/div[@class="pure-u-2-3 gray-font font12"]/div/a/@href').extract()[0]
                # errorTxt(followingAuthorUrl+'\n')
                followingAuthorUrls.append(followingAuthorUrl)

            for url in followingAuthorUrls:
                time.sleep(0.3)
                yield scrapy.Request(url=url, callback=self.processAuthorInformation)
            self.hasBeenCrawledFollowingUrls.add(response.url)
            with open('/Users/omtbreak/Desktop/track/hasBeenCrawledFollowingUrls.txt', 'a+')as file:
                file.write(response.url + '\n')
            try:
                nextPageUrl = 'https://www.xiachufang.com' + response.xpath(
                    '//div[@class="page-outer"]/div[@class="page-container"]/div[@class="block p40 white-bg"]/div[@class="pager"]/a[@class="next"]/@href').extract()[
                    0]
                # errorTxt(nextPageUrl)
                print('times')
                yield scrapy.Request(url=nextPageUrl, callback=self.parse)
            except Exception:
                print('no next page')
                pass

        # 处理所有关注作者的其他人的链接
        def processFollowers(self, response):
            self.hasBeenExtractedFollowedUrls.add(response.url)

            with open('/Users/omtbreak/Desktop/track/hasBeenExtractedFollowedUrls.txt', 'a+')as file:
                file.write(response.url + '\n')
            # 所有关注作者的其他用户的链接都存储在followerUrls中
            followerUrls = []
            followerLis = response.xpath(
                '//div[@class="page-outer"]/div[@class="page-container"]/div[@class="block p40 white-bg"]/ul[@class="plain people-follow-list"]/li')
            for followerLi in followerLis:
                followerUrl = 'https://www.xiachufang.com' + followerLi.xpath(
                    './div[@class="pure-g"]/div[@class="pure-u-2-3 gray-font font12"]/div/a/@href').extract()[0]
                # errorTxt(followerUrl+'\n')
                followerUrls.append(followerUrl)

            for url in followerUrls:
                time.sleep(0.3)
                yield scrapy.Request(url=url, callback=self.processAuthorInformation)
            self.hasBeenCrawledFollowedUrls.add(response.url)
            with open('/Users/omtbreak/Desktop/track/hasBeenCrawledFollowedUrls.txt', 'a+')as file:
                file.write(response.url + '\n')

            try:
                nextPageUrl = 'https://www.xiachufang.com' + response.xpath(
                    '//div[@class="page-outer"]/div[@class="page-container"]/div[@class="block p40 white-bg"]/div[@class="pager"]/a[@class="next"]/@href').extract()[
                    0]
                # errorTxt(nextPageUrl)
                print('times')
                yield scrapy.Request(url=nextPageUrl, callback=self.parse)
            except Exception:
                print('no next page')
                pass

        # 处理每一道菜获取每一道菜的信息
        # def parse(self, response):
        def processMealPage(self, response):
            print('processMealPage')
            print(response.url)
            self.hasBeenExtractedMealUrls.add(response.url)
            with open('/Users/omtbreak/Desktop/track/hasBeenExtractedMealUrls.txt', 'a+')as file:
                file.write(response.url + '\n')
            # 获取图片链接
            mealPictureUrl = response.xpath(
                '//div[@class="page-outer"]/div[@class="page-container"]/div[@class="pure-g"]/div[@class="pure-u-2-3 main-panel"]/div[@itemtype="http://schema.org/Recipe"]/div[@class="block block-has-padding white-bg recipe-show"]/div[@class="cover image expandable block-negative-margin"]/img/@src').extract()[
                0]

            # 获取菜的名字
            mealName = response.xpath(
                '//div[@class="page-outer"]/div[@class="page-container"]/div[@class="pure-g"]/div[@class="pure-u-2-3 main-panel"]/div[@itemtype="http://schema.org/Recipe"]/h1[@class="page-title"]/text()').extract()[
                0].strip('\n').strip(' ').strip('\n')
            # print(mealName)

            # 获取综合得分
            mealScore = ''
            try:
                mealScore = response.xpath(
                    '//div[@class="page-outer"]/div[@class="page-container"]/div[@class="pure-g"]/div[@class="pure-u-2-3 main-panel"]/div[@itemtype="http://schema.org/Recipe"]/div[@class="block block-has-padding white-bg recipe-show"]/div[@class="container pos-r"]/div[@class="stats"]/div[@class="score"]/div[@class="overview"]/span[@class="number"]/text()').extract()[
                    0]
                # print(mealScore)
            except Exception:
                pass
            mealTimes = ''
            # 获取多少人做过
            try:
                mealTimes = \
                response.xpath('//div[@class="cooked"]/div[@class="overview"]/span[@class="number"]/text()').extract()[
                    0]
                # print(mealTimes)
            except Exception:
                pass

            mealDescription = ''
            # 简介
            try:
                mealDescription = response.xpath('//div[@class="desc"]/text()').extract()[0].strip('\n').strip(
                    ' ').strip('\n')
                # print(mealDescription)
            except Exception:
                pass

            # 用料
            ingredients = {}
            ingredientTrs = response.xpath(
                '//div[@class="page-outer"]/div[@class="page-container"]/div[@class="pure-g"]/div[@class="pure-u-2-3 main-panel"]/div[@itemtype="http://schema.org/Recipe"]/div[@class="block block-has-padding white-bg recipe-show"]/div[@class="ings"]/table/tr[@itemprop="recipeIngredient"]')
            for ingredientTr in ingredientTrs:
                ingredientName = ''
                ingredientName = ingredientTr.xpath('./td[@class="name has-border"]/text()').extract()[0].strip(
                    '\n').strip(' ').strip('\n')
                if ingredientName is '':
                    ingredientName = '    ' + ingredientTr.xpath('./td[@class="name has-border"]/a/text()').extract()[
                        0].strip('\n').strip(' ').strip('\n')

                # print('=='+ingredientName)
                ingredientQuantity = ingredientTr.xpath('./td[@class="unit has-border"]/text()').extract()[0].strip(
                    '\n').strip(' ').strip('\n')
                ingredients.update({ingredientName: ingredientQuantity})
            # print(ingredients)
            # errorTxt(str(ingredients))

            # 获取做这道菜的作者主页链接
            authorUrl = 'http://www.xiachufang.com' + response.xpath(
                '//div[@class="page-outer"]/div[@class="page-container"]/div[@class="pure-g"]/div[@class="pure-u-2-3 main-panel"]/div[@itemtype="http://schema.org/Recipe"]/div[@class="block block-has-padding white-bg recipe-show"]/div[@class="author"]/a[@class="avatar-link"]/@href').extract()[
                0]
            # print(authorUrl)

            # 步骤

            procedure = ''
            try:
                mealStepsLocation = response.xpath('//div[@class="steps"]/ol/li[@class="container"]')
                index = 0
                for step in mealStepsLocation:
                    index += 1
                    text = '(' + str(index) + ')' + '.  ' + step.xpath('./p[@class="text"]/text()').extract()[0] + '\n'
                    procedure += text
                    # errorTxt(procedure)
            except Exception:
                pass
            # 将菜的信息保存在txt中
            with open('/Users/omtbreak/Desktop/Meal/' + mealName + '.txt', 'a+')as file:
                file.write('1, 菜的名字是： ' + mealName + '\n')
                file.write('2, 菜肴图片链接是： ' + mealPictureUrl + '\n')
                file.write('3, 菜的综合得分是： ' + mealScore + '\n')
                file.write('4, 做过这道菜的人数有： ' + mealTimes + '\n')
                file.write('5, 这道菜的简介是: ' + mealDescription + '\n')
                file.write('6, 这道菜的材料有: ' + '\n')
                for ingName, ingQuantity in ingredients.items():
                    file.write('材料名字是: ' + ingName + '    ' + '材料用量' + ingQuantity + '\n')
                file.write('7, 作者主页链接是： ' + authorUrl + '\n')
                file.write('8, 这道菜的操作步骤是: ' + '\n' + procedure)
            # 这道菜的信息已经保存完了，所以这道菜的链接可以设定为已经被抓取过了
            self.hasBeenCrawledMealUrls.add(response.url)
            with open('/Users/omtbreak/Desktop/track/hasBeenCrawledMealUrls.txt', 'a+')as file:
                file.write(response.url + '\n')
            if authorUrl:
                yield scrapy.Request(url=authorUrl, callback=self.processAuthorInformation)

      
