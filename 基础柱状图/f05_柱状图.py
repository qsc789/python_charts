from pyecharts.charts import Bar
from pyecharts.options import LabelOpts
bar=Bar()
bar.add_xaxis(["中国","美国","英国"])
bar.add_yaxis("GDP",[30,20,10],label_opts=LabelOpts(position="right"))

bar.reversal_axis()# 反转坐标轴，柱变成横着的
bar.render("基础柱状图.html")