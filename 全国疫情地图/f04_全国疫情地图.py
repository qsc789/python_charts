import json
from pyecharts.charts import Map
from pyecharts.options import *
f=open("D:/疫情.txt","r",encoding="utf-8")
data=f.read()
f.close()

data_dict=json.loads(data)
province_data_list=data_dict["areaTree"][0]["children"]

data_list=[]# 画图用的数据列表
for province_data in province_data_list:# 数据封装为元组
    province_name=province_data["name"]
    province_confirm=province_data["total"]["confirm"]
    data_list.append((province_name,province_confirm))

map=Map()
map.add("各省份确诊人数",data_list,"china")
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,# 是否显示
        is_piecewise=True,# 是否分段
        pieces=[
            {"min":1,"max":99,"lable":"1-99人","color":"#CCFFFF"},
            {"min":100,"max":999,"lable":"100-999人","color":"#FFFF99"},
            {"min":1000,"max":4999,"lable":"1000-4999人","color":"#FF9966"},
            {"min":5000,"max":9999,"lable":"5000-9999人","color":"#FF6666"},
            {"min":10000,"max":99999,"lable":"10000-99999人","color":"#CC3333"},
            {"min":100000,"lable":"100000+","color":"#990033"}
        ]
    )
)
map.render("全国疫情地图.html")
