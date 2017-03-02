def errorTxt(s):
    with open('/Users/omtbreak/Desktop/track/error.txt', 'a+') as file:
        file.write(s)


with open('/Users/omtbreak/Desktop/track/hasBeenCrawledAuthorUrls.txt', 'a+')as file:
    for line in file.readlines():
        print(line)
