# g2py

> 🎨 g2py 是 [`@AntV/G2`](https://github.com/antvis/G2) 在 Python3 上的封装。与 G2Plot采用同样的方式进行封装 

[![Latest Stable Version](https://img.shields.io/pypi/v/g2py.svg)](https://pypi.python.org/pypi/g2py)
[![Pypi Download](https://img.shields.io/pypi/dm/g2py)](https://pypi.python.org/pypi/g2py)


<div align="center">
  <img src="https://free.wzznft.com/i/2023/10/19/u4chtb.png" width="800">
</div>


**相关文档**： [English README](./README.md)  ·  [绘制常用统计图表](./docs/plot.md)  ·  [在 Jupyter 中使用](./docs/jupyter.md)  ·  [技术原理](./docs/how.md)

## 安装

```bash
$ pip install g2py
```


## 使用

#### **渲染成 HTML**

```py


from g2py import Plot
chart10 = Plot("Chart")
chart10.set_options({
  "type": "density",
  "autoFit": "true",
  "data": {
    "type": "fetch",
    "value": "https://assets.antv.antgroup.com/g2/species.json",
    "transform": [{"type": "kde", "field": "y", "groupBy": ["x"], "size": 20 }],
  },
  "encode": { "x": "x", "y": "y", "color": "x", "size": "size" },
  "tooltip": 'true',
})

# 1. 渲染成 html 文件
chart10.render("plot.html")
# 2. 渲染成 html 字符串
chart10.render_html()
```


#### **在 Jupyter 中使用**

```py
from g2py import Plot
chart10 = Plot("Chart")
chart10.set_options({
  "type": "density",
  "autoFit": "true",
  "data": {
    "type": "fetch",
    "value": "https://assets.antv.antgroup.com/g2/species.json",
    "transform": [{"type": "kde", "field": "y", "groupBy": ["x"], "size": 20 }],
  },
  "encode": { "x": "x", "y": "y", "color": "x", "size": "size" },
  "tooltip": 'true',
})


chart10.render_notebook()

chart10.render_jupyter_lab()
```
```



使用 `JS` 方法，你可以创建一个 JavaScript 的代码片段去处理各种回调方法属性。


## API

目前 `g2py` 只提供简单的一个 API。

 - **Plot**

1. *Plot(plot_type: str)*: 获取 `Plot` 对应的类实例。

2. *plot.set_options(options: object)*: 给图表实例设置一个 [G2](https://g2.antv.antgroup.com/) 图形的配置，文档可以直接参考 G2 官网，未进行任何二次数据结构包装。

3. *plot.render(path, env, **kwargs)*: 渲染出一个 HTML 文件，同时可以传入文件的路径，以及 jinja2 env 和 kwargs 参数。

4. *plot.render_notebook(env, **kwargs)*: 将图形渲染到 jupyter 的预览。

5. *plot.render_jupyter_lab(env, **kwargs)*: 将图形渲染到 jupyter lab 的预览。

6. *plot.render_html(env, **kwargs)*: 渲染出 HTML 字符串，同时可以传入 jinja2 env 和 kwargs 参数。

7. *plot.dump_js_options(env, **kwargs)*: 输出 Javascript 的 option 配置结构，同时可以传入 jinja2 env 和 kwargs 参数，可以用于 Server 中的 HTTP 结构返回数据结构。



