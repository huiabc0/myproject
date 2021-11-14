"""
1. 使用python将提供的csv文件中的内容读到内存，并使用列表来表示。（提示，csv文件的编码是gbk）

2. 将第1题中解析出的列表再组织成csv格式写入一个新的csv文件。

1.csv文件是一个二维的表格数据
id	品种编号	花瓣长	花瓣宽	花萼长	花萼宽
0	0	5.1	3.5	1.4	0.2
1	0	4.9	3	1.4	0.2
2	0	4.7	3.2	1.3	0.2

[['id','品种编号','花瓣长','花瓣宽','花萼长','花萼宽'],[0,0,5.1,3.5,1.4,0.2]]
"""
data = [] #定义一个变量用来存放数据
# 1.读取csv文件
with open('鸢尾.csv','r',encoding='gbk') as f:
    for line in f:
        #去掉媳妇串收尾不可见字符
        line = line.strip()
        #根据逗号进行分割
        line = line.split(',')
        #添加到data列表中
        data.append(line)
        # 2.构造数据结构
print(data)

with open('new.csv','w',encoding='utf-8') as f:
    for item in data:
        item = ','.join(item)+'\n'
        f.write(item)