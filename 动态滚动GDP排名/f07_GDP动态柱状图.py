from pyecharts.charts import Bar,Timeline
from pyecharts.options import LabelOpts

my_list=[["a",33],["b",55],["c",11]]
# def choose_sort_key(element):
#     return element[1]# 按第二个元素排序
#
# my_list.sort(key=choose_sort_key(),reverse=True)# 降序
my_list.sort(key=lambda element:element[1],reverse=True)
f=open("D:/1960-2019全球GDP数据.csv","r",encoding="GB2312")
data_lines=f.readlines()
f.close()
# 删掉第一行
data_lines.pop(0)
data_dict={}
for line in data_lines:
    year=int(line.split(",")[0])
    country=line.split(",")[1]
    gdp=float(line.split(",")[2])
    try:
        data_dict[year].append([country,gdp])          # year不一定在列表中
    except KeyError:
        data_dict[year]=[]
        data_dict[year].append([country, gdp])

time_line=Timeline()
# 排序年份
sorted_year_list=sorted(data_dict.keys())
for year in sorted_year_list:
    data_dict[year].sort(key=lambda element:element[1],reverse=True)
    # 取出本年前8国家
    year_data=data_dict[year][0:8]
    x_data=[]
    y_data=[]
    for country_gdp in year_data:
        x_data.append(country_gdp[0])
        y_data.append(country_gdp[1]/100000000)
    bar=Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP（亿）",y_data,label_opts=LabelOpts(position="right"))

    bar.reversal_axis()
    time_line.add(bar,str(year))

time_line.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False
)

time_line.render("1960-2019年全球GDP前8国家.html")