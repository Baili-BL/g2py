# G2PY

[![Python Version](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://python.org)
[![G2 Version](https://img.shields.io/badge/G2-5.1.4-green.svg)](https://g2.antv.vision)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

**G2PY** 是基于蚂蚁集团 [G2](https://g2.antv.vision) 可视化引擎的 Python 数据可视化库，提供简洁的 API 和丰富的图表类型，完美支持 Jupyter 环境。

## 特性

- 🚀 **现代化架构** - 支持 Python 3.11+，采用现代化设计模式
- 📊 **丰富图表** - 支持折线图、柱状图、散点图、气泡图、面积图等
- 🎨 **灵活配置** - 完整的样式自定义和交互配置支持
- 📱 **响应式设计** - 自适应容器大小，支持多种尺寸设置
- 🌐 **双模式运行** - 支持在线 CDN 和离线静态文件模式
- 📝 **Jupyter 原生支持** - 无缝集成 Jupyter Notebook 和 JupyterLab
- 🔗 **链式 API** - 支持方法链式调用，代码简洁优雅

## 安装

```bash
# 克隆项目
git clone https://github.com/your-repo/g2py.git
cd g2py

# 安装依赖
pip install jinja2>=3.1.0 simplejson>=3.17.0
```

## 快速开始

```python
from g2py import Plot

# 准备数据
data = [
    {'month': '1月', 'sales': 1200},
    {'month': '2月', 'sales': 1500}, 
    {'month': '3月', 'sales': 1800}
]

# 创建图表
plot = Plot("line")
plot.set_options({
    "type": "line",
    "data": data,
    "encode": {"x": "month", "y": "sales"}
})

# 渲染图表
plot.show()  # Jupyter 环境
# 或
plot.render("chart.html")  # 保存为文件
```

## 核心 API

### Plot 类

```python
Plot(plot_type="Chart", version="5", offline=False)
```

### 主要方法

| 方法 | 说明 | 示例 |
|------|------|------|
| `set_options(options)` | 设置图表配置 | `plot.set_options({"type": "line", "data": data})` |
| `set_title(title)` | 设置页面标题 | `plot.set_title("销售趋势图")` |
| `show()` | 在 Jupyter 中显示 | `plot.show()` |
| `render(path)` | 保存为 HTML 文件 | `plot.render("chart.html")` |

### 配置选项

```python
plot.set_options({
    "type": "line",                    # 图表类型
    "data": data,                      # 数据源
    "encode": {                        # 数据映射
        "x": "field_name",
        "y": "field_name", 
        "color": "category_field"
    },
    "style": {                         # 样式配置
        "stroke": "#1890ff",
        "lineWidth": 2,
        "opacity": 0.8
    },
    "width": 800,                      # 图表宽度
    "height": 400,                     # 图表高度
    "autoFit": True,                   # 自适应容器
    "tooltip": True,                   # 显示提示框
    "legend": True                     # 显示图例
})
```

## 图表类型

### 基础图表

| 类型 | 说明 | 示例文件 |
|------|------|----------|
| `line` | 折线图 | `jupyter_demo_line.py` |
| `interval` | 柱状图 | `jupyter_demo_interval.py` |
| `point` | 散点图 | `jupyter_demo_point.py` |
| `area` | 面积图 | - |

### 使用示例

```python
# 折线图
from jupyter_demo_line import demo_basic_line
demo_basic_line()

# 柱状图  
from jupyter_demo_interval import demo_basic_bar
demo_basic_bar()

# 散点图
from jupyter_demo_point import demo_basic_point
demo_basic_point()
```

## 运行模式

### 在线模式（默认）
```python
plot = Plot("line")  # 使用 CDN 加载 G2
```

### 离线模式
```python
plot = Plot("line", offline=True)  # 使用本地 G2 文件
```

## 高级功能

### 链式调用
```python
chart = (Plot("line")
         .set_options({"type": "line", "data": data, "encode": {"x": "x", "y": "y"}})
         .set_title("趋势图"))
```

### 响应式图表
```python
plot.set_options({"autoFit": True})  # 自适应容器大小
```

### 多系列数据
```python
# 支持分组、堆叠等多种数据展示方式
plot.set_options({
    "transform": [{"type": "dodgeX"}],  # 分组
    "encode": {"color": "category"}     # 按类别着色
})
```

## 系统要求

- **Python**: 3.11+
- **依赖项**: 
  - `jinja2>=3.1.0`
  - `simplejson>=3.17.0`
- **可选**: Jupyter Notebook/Lab 支持

## 项目结构

```
g2py/
├── g2py/
│   ├── __init__.py
│   ├── plot.py                 # 核心 Plot 类
│   ├── engine.py              # 模板引擎
│   ├── templates/             # HTML 模板
│   └── static/                # 静态资源
├── jupyter_demo_line.py       # 折线图演示
├── jupyter_demo_interval.py   # 柱状图演示
├── jupyter_demo_point.py      # 散点图演示
├── JUPYTER_GUIDE.md          # Jupyter 使用指南
└── README.md
```

## 文档

- [Jupyter 使用指南](JUPYTER_GUIDE.md) - 详细的 Jupyter 环境使用说明
- [API 参考](g2py/plot.py) - 完整的 API 文档
- [示例集合](examples_updated.py) - 综合示例代码

## 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## 相关链接

- [G2 官方文档](https://g2.antv.vision)
- [问题反馈](https://github.com/your-repo/g2py/issues)
- [贡献指南](CONTRIBUTING.md)