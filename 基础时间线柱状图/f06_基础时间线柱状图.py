from pyecharts.charts import Bar,Timeline
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType# 导入主题类型

bar1=Bar()
bar1.add_xaxis(["中国","美国","英国"])
bar1.add_yaxis("GDP",[30,20,10],label_opts=LabelOpts(position="right"))
bar1.reversal_axis()# 反转坐标轴，柱变成横着的

bar2=Bar()
bar2.add_xaxis(["中国","美国","英国"])
bar2.add_yaxis("GDP",[50,50,50],label_opts=LabelOpts(position="right"))
bar2.reversal_axis()# 反转坐标轴，柱变成横着的

bar3=Bar()
bar3.add_xaxis(["中国","美国","英国"])
bar3.add_yaxis("GDP",[70,60,60],label_opts=LabelOpts(position="right"))
bar3.reversal_axis()# 反转坐标轴，柱变成横着的

# 创建时间线对象
timeline=Timeline(
    {"theme":ThemeType.LIGHT}# 设置主题
)
# 在时间线内添加柱状图对象
timeline.add(bar1,"点1")
timeline.add(bar2,"点2")
timeline.add(bar3,"点3")

# 自动播放
timeline.add_schema(
    play_interval=1000,# 间隔时间
    is_timeline_show=True,# 显示时间线
    is_auto_play=True,# 自动播放
    is_loop_play=True# 循环播放
)
# 绘图是用时间线绘图，不用bar对象
timeline.render("基础时间线柱状图.html")