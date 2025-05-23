#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
G2PY 折线图演示 - Jupyter环境
支持Python 3.11+
"""

from g2py import Plot
import random

def generate_line_data():
    """生成折线图数据"""
    return {
        'monthly_sales': [
            {'month': f'{i}月', 'sales': random.randint(800, 2000)} 
            for i in range(1, 13)
        ],
        'temperature': [
            {'date': f'2024-{i:02d}-01', 'temp': random.randint(-5, 35)} 
            for i in range(1, 13)
        ],
        'stock_price': [
            {'day': i, 'price': 100 + random.randint(-20, 30) + (i * 2)} 
            for i in range(1, 31)
        ]
    }

def demo_basic_line():
    """基础折线图演示"""
    print("📈 基础折线图演示")
    
    data = generate_line_data()['monthly_sales']
    
    plot = Plot("line")
    plot.set_options({
        "type": "line",
        "data": data,
        "encode": {
            "x": "month",
            "y": "sales"
        },
        "style": {
            "stroke": "#1890ff",
            "lineWidth": 2
        }
    })
    plot.set_title("2024年月度销售趋势")
    
    return plot.render_notebook()

def demo_styled_line():
    """带样式的折线图"""
    print("🎨 带样式的折线图")
    
    data = generate_line_data()['temperature']
    
    plot = Plot("line")
    plot.set_options({
        "type": "line",
        "data": data,
        "encode": {
            "x": "date",
            "y": "temp"
        },
        "style": {
            "stroke": "#ff4d4f",
            "lineWidth": 3,
            "lineDash": [5, 5],
            "opacity": 0.8
        },
        "tooltip": True,
        "width": 600,
        "height": 300
    })
    plot.set_title("2024年月度气温变化")
    
    return plot.render_notebook()

def demo_area_line():
    """区域折线图"""
    print("📊 区域折线图")
    
    data = generate_line_data()['stock_price']
    
    plot = Plot("area")
    plot.set_options({
        "type": "area",
        "data": data,
        "encode": {
            "x": "day",
            "y": "price"
        },
        "style": {
            "fill": "#52c41a",
            "opacity": 0.6,
            "stroke": "#389e0d",
            "lineWidth": 2
        },
        "height": 400
    })
    plot.set_title("股价走势图")
    
    return plot.render_notebook()

def demo_multi_line():
    """多系列折线图"""
    print("📈 多系列折线图")
    
    # 生成多系列数据
    multi_data = []
    months = ['1月', '2月', '3月', '4月', '5月', '6月']
    for month in months:
        multi_data.extend([
            {'month': month, 'type': '线上销售', 'value': random.randint(800, 1500)},
            {'month': month, 'type': '线下销售', 'value': random.randint(600, 1200)}
        ])
    
    plot = Plot("line")
    plot.set_options({
        "type": "line",
        "data": multi_data,
        "encode": {
            "x": "month",
            "y": "value",
            "color": "type"
        },
        "style": {
            "lineWidth": 3
        },
        "tooltip": True,
        "legend": True,
        "width": 800,
        "height": 350
    })
    plot.set_title("线上线下销售对比")
    
    return plot.render_notebook()

def demo_responsive_line():
    """响应式折线图"""
    print("📱 响应式折线图")
    
    data = generate_line_data()['monthly_sales']
    
    plot = Plot("line")
    plot.set_options({
        "type": "line",
        "data": data,
        "encode": {
            "x": "month",
            "y": "sales"
        },
        "style": {
            "stroke": "#722ed1",
            "lineWidth": 2
        },
        "tooltip": True,
        "autoFit": True  # 自适应容器大小
    })
    plot.set_title("自适应折线图")
    
    return plot.render_notebook()

# 演示函数列表
DEMOS = [
    ("demo_basic_line", "基础折线图"),
    ("demo_styled_line", "带样式的折线图"),
    ("demo_area_line", "区域折线图"),
    ("demo_multi_line", "多系列折线图"),
    ("demo_responsive_line", "响应式折线图")
]

def run_all_line_demos():
    """运行所有折线图演示"""
    print("🚀 G2PY 折线图演示开始")
    print("=" * 40)
    
    for func_name, desc in DEMOS:
        try:
            print(f"\n📈 执行: {desc}")
            result = globals()[func_name]()
            print(f"   ✓ 成功")
        except Exception as e:
            print(f"   ✗ 失败: {e}")
    
    print("\n🎉 折线图演示完成！")

if __name__ == "__main__":
    print("📈 G2PY 折线图演示")
    print("=" * 30)
    print("🔍 可用的演示函数:")
    for i, (func_name, desc) in enumerate(DEMOS, 1):
        print(f"{i}. {func_name}() - {desc}")
    
    print("\n💡 使用方法:")
    print("   在Jupyter中: demo_basic_line()")
    print("   运行所有: run_all_line_demos()")
    print("\n📏 尺寸设置示例:")
    print("   在set_options中设置: 'width': 800, 'height': 400")
    print("   自适应设置: 'autoFit': True") 