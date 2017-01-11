# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
total=set()

with open('/Users/omtbreak/kaishi/mealPageUrls.txt','r+')as file:
    for line in file.readlines():
        total.add(line.strip('\n'))

with open('/Users/omtbreak/kaishi/mealPageUrls.txt','w+')as file:
    for url in total:
        file.write(url+'\n')

print(len(total))
read=set()
with open('/Users/omtbreak/kaishi/resolutionBreakdownUrl.txt','r')as file:
    for line in file.readlines():
        line=line.strip('\n')
        read.add(line)
print(len(read))
with open('/Users/omtbreak/kaishi/resolutionBreakdownUrl.txt','w+')as file:
    for url in read:
        file.write(url+'\n')


notread=total-read
'''
with open('/Users/omtbreak/kaishi/notread.txt','r+')as file:
    for line in file.readlines():
        url=line.strip('\n')
        notread.add(url)
'''
with open('/Users/omtbreak/kaishi/notread.txt','w+')as file:
    for url in notread:
        file.write(url+'\n')

print(len(notread))
print(notread)
foodPage=set()
with open('/Users/omtbreak/kaishi/foodPage.txt','r')as file:
    for line in file.readlines():
        foodPage.add(line.strip('\n'))

with open('/Users/omtbreak/kaishi/foodPage.txt','w+')as file:
    for text in foodPage:
        file.write(text+'\n')


