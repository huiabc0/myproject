import json
"""
json字符反序列化成python数据数据
"""
#方法一
with open('xiaowanzi.json','r',encoding='utf-8')as f:
    comment = f.read()
res = json.loads(comment)
print(res)

#方法二
str_json = '{"name":"花花","age":22}'
str1 = json.loads(str_json)
print(str1,type(str1))

"""
将python数据序列化成json字符串
"""
str2 = json.dumps(res,ensure_ascii=False,indent=4)
print(str2)

#将json字符串写入到文件中 方法一
with open('new_json','w',encoding='utf-8') as f:
    comment = f.write(str2)
    print(comment)

# 方法二
with open('new_json','w',encoding='utf-8') as f:
    res= json.dump(res,f,ensure_ascii=False,indent=3)
    print(res)

    