from openpyxl import load_workbook


def get_data_excel(file, sheet_name=None):
    #读取excel文件
    wb = load_workbook(file)
    #获取对应的表
    if sheet_name is None:
        ws = wb.active
    else:
        ws  =wb[sheet_name]
    #创建容器用语存放数据
    data = []
    # 4.1获取表头作为字典的key
    rows_list = list(ws.rows)
    # title = []
    # #拿到第一行迭代
    # for key in row_list[0]
    #     title.append(key.value)
    # 上面三句等价下面的一句
    title = [item.value for item in rows_list[0]]  # 列表生成式
    # 4.2获取其他数据
    for row in rows_list[1:]:
        # 再获取每一行数据
        temp = [i.value for i in row]
        # 将表头与这一行的数据打包，换成字典
        data.append(dict(zip(title, temp)))
    return data

if __name__ =='__main__':
    res = get_data_excel('../testdata/testdata.xlsx')
    print(res)