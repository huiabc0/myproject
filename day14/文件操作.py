f = open('test.txt','r',encoding='utf-8')
content = f.read()
print(content)
f.close()

#上下文管理，等同于上面方法
with open('test.txt','r',encoding='utf-8')as f:
    content = f.read()
    print(content)
