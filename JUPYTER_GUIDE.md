# G2PY Jupyter 使用指南

## 🚀 快速开始

G2PY重构版本完全支持Jupyter Notebook和JupyterLab环境，提供了专门优化的渲染方法和更好的用户体验。

### 环境要求
- Python 3.11+
- Jupyter Notebook 或 JupyterLab
- jinja2 >= 3.1.0

## 📦 安装和设置

### 1. 安装G2PY
```bash
pip install -r requirements.txt
```

### 2. 启动Jupyter
```bash
# Jupyter Notebook
jupyter notebook

# 或者 JupyterLab (推荐)
jupyter lab
```

## 🎯 基础使用

### 在Jupyter Notebook中创建图表

```python
from g2py import Plot

# 准备数据
data = [
    {'month': '1月', 'sales': 1200},
    {'month': '2月', 'sales': 1500},
    {'month': '3月', 'sales': 1800},
    {'month': '4月', 'sales': 2100}
]

# 创建图表
plot = Plot("interval")
plot.set_options({
    "type": "interval",
    "data": data,
    "encode": {
        "x": "month",
        "y": "sales"
    }
})
plot.set_title("月度销售数据")

# 在Notebook中显示
plot.render_notebook()
```

### 在JupyterLab中使用(优化版本)

```python
# 相同的代码，但使用优化的渲染方法
plot.render_jupyter_lab()  # JupyterLab专用优化
```

## 🔧 核心功能

### 1. 环境自动检测

G2PY会自动检测当前运行环境并选择最佳渲染方式：

```python
# 自动环境检测
plot = Plot("line")
plot.set_options({
    "type": "line",
    "data": data,
    "encode": {
        "x": "month",
        "y": "sales"
    }
})

# 会自动选择最佳渲染方式
plot.render_notebook()  # 自动适配环境
```

### 2. 链式API调用

```python
# 链式调用让代码更简洁
(Plot("point")
 .set_options({
     "type": "point",
     "data": scatter_data,
     "encode": {
         "x": "x",
         "y": "y",
         "size": "size"
     },
     "style": {
         "fill": "#52c41a"
     }
 })
 .set_title("散点图")
 .render_notebook())
```

### 3. 交互式图表

```python
# 带交互功能的图表
plot = Plot("interval")
plot.set_options({
    "type": "interval",
    "data": data,
    "encode": {
        "x": "category",
        "y": "value",
        "color": "category"
    },
    "tooltip": True,
    "legend": True
})
plot.render_notebook()
```

## 📊 图表类型示例

### 柱状图
```python
plot = Plot("interval")
plot.set_options({
    "type": "interval",
    "data": data,
    "encode": {"x": "month", "y": "sales"}
})
plot.render_notebook()
```

### 折线图
```python
plot = Plot("line")
plot.set_options({
    "type": "line",
    "data": data,
    "encode": {"x": "month", "y": "sales"}
})
plot.render_notebook()
```

### 散点图
```python
plot = Plot("point")
plot.set_options({
    "type": "point",
    "data": data,
    "encode": {"x": "x", "y": "y"}
})
plot.render_notebook()
```

### 饼图
```python
plot = Plot("interval")
plot.set_options({
    "type": "interval",
    "data": pie_data,
    "encode": {"y": "value", "color": "category"},
    "coordinate": "theta"
})
plot.render_notebook()
```

### 区域图
```python
plot = Plot("area")
plot.set_options({
    "type": "area",
    "data": data,
    "encode": {"x": "month", "y": "sales"}
})
plot.render_notebook()
```

## 🎨 样式自定义

### 基础样式
```python
plot = Plot("line")
plot.set_options({
    "type": "line",
    "data": data,
    "encode": {"x": "month", "y": "sales"},
    "style": {
        "stroke": "#1890ff",     # 线条颜色
        "lineWidth": 3,          # 线条宽度
        "opacity": 0.8           # 透明度
    }
})
plot.render_notebook()
```

### 高级样式
```python
plot.set_options({
    "type": "interval",
    "data": data,
    "encode": {"x": "month", "y": "sales"},
    "style": {
        "fill": "#fa541c",       # 填充色
        "stroke": "#722ed1",     # 边框色
        "lineDash": [5, 5],      # 虚线样式
        "shadowColor": "#000",   # 阴影色
        "shadowBlur": 10         # 阴影模糊度
    }
})
```

## 📱 响应式设计

### 自适应容器
```python
# 图表会自动适应容器大小
plot = Plot("interval")
plot.set_options({
    "type": "interval",
    "data": data,
    "encode": {"x": "month", "y": "sales"},
    "height": 400  # 设置固定高度
})
plot.render_notebook()
```

## 🔄 动态数据更新

### 模拟实时数据
```python
import time
import random

# 初始化数据
data = [{'time': i, 'value': random.randint(50, 100)} for i in range(10)]

# 创建图表
plot = Plot("line")
plot.set_options({
    "type": "line",
    "data": data,
    "encode": {"x": "time", "y": "value"}
})
plot.set_title("实时数据监控")

# 显示图表
plot.render_notebook()

# 在新的cell中更新数据
# data.append({'time': 10, 'value': random.randint(50, 100)})
# plot.set_options({"data": data})
# plot.render_notebook()
```

## 🛠️ 高级功能

### 多系列数据
```python
# 准备多系列数据
multi_data = []
for month in ['1月', '2月', '3月', '4月']:
    multi_data.extend([
        {'month': month, 'type': '线上', 'sales': random.randint(800, 1500)},
        {'month': month, 'type': '线下', 'sales': random.randint(600, 1200)}
    ])

# 创建多系列图表
plot = Plot("interval")
plot.set_options({
    "type": "interval",
    "data": multi_data,
    "encode": {
        "x": "month",
        "y": "sales",
        "color": "type"
    }
})
plot.set_title("线上线下销售对比")
plot.render_notebook()
```

### 自定义JavaScript
```python
# 使用自定义JS代码
custom_js = """
// 自定义交互逻辑
chart.on('element:click', (e) => {
    console.log('点击了:', e.data);
});
"""

plot = Plot("interval")
plot.set_options({
    "type": "interval",
    "data": data,
    "encode": {"x": "month", "y": "sales"}
}, js_code=custom_js)
plot.render_notebook()
```

## 🐛 调试和错误处理

### 调试模式
```python
# 启用调试模式（通过JavaScript检查）
plot = Plot("interval")
plot.set_options({
    "type": "interval",
    "data": data,
    "encode": {"x": "month", "y": "sales"}
}, js_code="console.log('调试信息:', chart);")
plot.render_notebook()
```

### 错误处理
```python
try:
    plot = Plot("interval")
    plot.set_options({
        "type": "interval",
        "data": data,
        "encode": {"x": "month", "y": "sales"}
    })
    result = plot.render_notebook()
except Exception as e:
    print(f"图表渲染失败: {e}")
    # 使用备用渲染方式
    plot.render_html()
```

## ⚡ 性能优化

### 大数据集处理
```python
# 对于大数据集，可以进行采样
large_data = [{'x': i, 'y': random.randint(1, 100)} for i in range(10000)]

# 采样处理
sampled_data = large_data[::100]  # 每100个取一个

plot = Plot("point")
plot.set_options({
    "type": "point",
    "data": sampled_data,
    "encode": {"x": "x", "y": "y"}
})
plot.render_notebook()
```

### 缓存渲染结果
```python
# 缓存复杂图表的渲染结果
plot_cache = {}

def get_cached_plot(data_key, data):
    if data_key not in plot_cache:
        plot = Plot("interval")
        plot.set_options({
            "type": "interval",
            "data": data,
            "encode": {"x": "month", "y": "sales"}
        })
        plot_cache[data_key] = plot
    return plot_cache[data_key].render_notebook()
```

## 📝 最佳实践

### 1. 代码组织
```python
# 将图表创建封装成函数
def create_sales_chart(data, title="销售数据"):
    plot = Plot("interval")
    plot.set_options({
        "type": "interval",
        "data": data,
        "encode": {"x": "month", "y": "sales"},
        "style": {"fill": "#1890ff"}
    })
    plot.set_title(title)
    return plot.render_notebook()

# 使用函数创建图表
create_sales_chart(monthly_sales, "2024年月度销售")
```

### 2. 数据验证
```python
def validate_data(data):
    """验证数据格式"""
    if not isinstance(data, list):
        raise ValueError("数据必须是列表格式")
    if not data:
        raise ValueError("数据不能为空")
    return True

# 在创建图表前验证数据
if validate_data(data):
    plot = Plot("interval")
    plot.set_options({
        "type": "interval",
        "data": data,
        "encode": {"x": "month", "y": "sales"}
    })
    plot.render_notebook()
```

### 3. 主题一致性
```python
# 定义统一的样式主题
DEFAULT_STYLE = {
    "fill": "#1890ff",
    "stroke": "#096dd9",
    "opacity": 0.8
}

# 应用统一样式
plot = Plot("interval")
plot.set_options({
    "type": "interval",
    "data": data,
    "encode": {"x": "month", "y": "sales"},
    "style": DEFAULT_STYLE
})
plot.render_notebook()
```

## 🚨 常见问题

### Q: 图表不显示？
```python
# 检查数据格式
print("数据类型:", type(data))
print("数据内容:", data[:2])

# 检查配置选项
plot = Plot("interval")
options = {
    "type": "interval",
    "data": data,
    "encode": {"x": "month", "y": "sales"}
}
print("配置选项:", options)
plot.set_options(options)
```

### Q: 样式不生效？
```python
# 确保样式配置正确
style_config = {"fill": "#ff4d4f"}
plot.set_options({
    "type": "interval",
    "data": data,
    "encode": {"x": "month", "y": "sales"},
    "style": style_config
})
print("样式配置:", style_config)
```

### Q: 在JupyterLab中显示异常？
```python
# 尝试使用标准渲染方式
plot.render_notebook()  # 而不是 render_jupyter_lab()
```

## 📚 示例集合

完整的示例代码请参考：
- `jupyter_examples.py` - Python脚本版本
- `jupyter_demo.ipynb` - Jupyter Notebook版本
- `examples_updated.py` - 全功能演示

## 🔗 相关资源

- [G2 官方文档](https://g2.antv.vision)
- [Python 3.11+ 新特性](https://docs.python.org/3.11/whatsnew/3.11.html)
- [Jupyter 使用指南](https://jupyter.org/documentation)

---

💡 **提示**: 在Jupyter环境中使用G2PY时，建议使用JupyterLab以获得更好的显示效果和性能。使用`set_options()`方法配置所有图表选项。 