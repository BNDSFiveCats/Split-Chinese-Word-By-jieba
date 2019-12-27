import jieba
name = r"李白诗歌.txt"
jug = input("是否只统计单字,或不统计单字,0:不统计单字,1:统计单字,2:都统计:   ")
num = int(input("统计数量:"))
txt = open(name,"r",encoding="UTF-8").read()
stopwords = open(r"stopwords.txt","r",encoding="UTF-8").read().split("\n")
extstopwords = open(r"extstopwords.txt","r",encoding="UTF-8").read().split("\n")
words = jieba.lcut(txt)
counts = {}
for word in words:
    word = word.strip()
    if word == "":
        continue
    if jug =="0" :
    # 去掉字符长度为 1 的字符串
        if len(word) == 1:
            continue
        counts[word] = counts.get(word,0) + 1
    if jug =="1" :
    # 只查询单字
        if not len(word) == 1:
            continue
        counts[word] = counts.get(word,0) + 1
    if jug =="2":
        counts[word] = counts.get(word,0) + 1

items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
print("stopwords: ",extstopwords)
# for i in range(num):
i =-1
print()
print("{0:<8}{1:>5}".format("# 词语","词频"))
print("--------------------")
for i in range(num):
    word,count = items[i]
    # 不输出停用词
    if word in stopwords or word in extstopwords:
        continue
    # 不输出数字
    if word.isdigit():
        continue
    print("{0:<10}{1:>5}".format(str(i+1)+" "+word,count))
print("状态:"+jug+"   检索文件:"+name)
print("检索完成 范围: "+str(num))
