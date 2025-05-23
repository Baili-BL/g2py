#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
G2PY 柱状图演示 - Jupyter环境
支持Python 3.11+
"""

from g2py import Plot
import random

def generate_bar_data():
    """生成柱状图数据"""
    return {
        'sales_by_region': [
            {'region': '华东', 'sales': random.randint(1000, 3000)},
            {'region': '华南', 'sales': random.randint(800, 2500)},
            {'region': '华北', 'sales': random.randint(1200, 2800)},
            {'region': '西南', 'sales': random.randint(600, 2000)},
            {'region': '东北', 'sales': random.randint(400, 1500)}
        ],
        'product_performance': [
            {'product': '产品A', 'q1': random.randint(500, 1000), 'q2': random.randint(600, 1200)},
            {'product': '产品B', 'q3': random.randint(400, 900), 'q4': random.randint(700, 1300)},
            {'product': '产品C', 'q1': random.randint(800, 1500), 'q2': random.randint(500, 1100)}
        ],
        'monthly_revenue': [
            {'month': f'{i}月', 'revenue': random.randint(10000, 50000)} 
            for i in range(1, 7)
        ]
    }

def demo_basic_bar():
    """基础柱状图演示"""
    print("📊 基础柱状图演示")
    
    data = generate_bar_data()['sales_by_region']
    
    plot = Plot("interval")
    plot.set_options({
        "type": "interval",
        "data": data,
        "encode": {
            "x": "region",
            "y": "sales"
        },
        "style": {
            "fill": "#1890ff"
        }
    })
    plot.set_title("各区域销售业绩")
    
    return plot.render_notebook()

def demo_styled_bar():
    """带样式的柱状图"""
    print("🎨 带样式的柱状图")
    
    data = generate_bar_data()['monthly_revenue']
    
    plot = Plot("interval")
    plot.set_options({
        "type": "interval",
        "data": data,
        "encode": {
            "x": "month",
            "y": "revenue"
        },
        "style": {
            "fill": "#52c41a",
            "opacity": 0.8,
            "stroke": "#389e0d",
            "lineWidth": 2
        },
        "tooltip": True,
        "width": 700,
        "height": 350
    })
    plot.set_title("月度营收统计")
    
    return plot.render_notebook()

def demo_horizontal_bar():
    """横向柱状图"""
    print("↔️ 横向柱状图")
    
    data = generate_bar_data()['sales_by_region']
    
    plot = Plot("interval")
    plot.set_options({
        "type": "interval",
        "data": data,
        "encode": {
            "x": "sales",
            "y": "region"
        },
        "style": {
            "fill": "#722ed1"
        },
        "tooltip": True,
        "width": 600,
        "height": 400
    })
    plot.set_title("区域销售排行榜")
    
    return plot.render_notebook()

def demo_grouped_bar():
    """分组柱状图"""
    print("📊 分组柱状图")
    
    # 生成分组数据
    grouped_data = []
    categories = ['线上', '线下']
    regions = ['华东', '华南', '华北', '西南']
    
    for region in regions:
        for category in categories:
            grouped_data.append({
                'region': region,
                'category': category,
                'value': random.randint(500, 2000)
            })
    
    plot = Plot("interval")
    plot.set_options({
        "type": "interval",
        "data": grouped_data,
        "encode": {
            "x": "region",
            "y": "value",
            "color": "category"
        },
        "transform": [{"type": "dodgeX"}],
        "tooltip": True,
        "legend": True,
        "width": 800,
        "height": 400
    })
    plot.set_title("线上线下销售对比")
    
    return plot.render_notebook()

def demo_stacked_bar():
    """堆叠柱状图"""
    print("📚 堆叠柱状图")
    
    # 生成堆叠数据
    stacked_data = []
    quarters = ['Q1', 'Q2', 'Q3', 'Q4']
    products = ['产品A', '产品B', '产品C']
    
    for quarter in quarters:
        for product in products:
            stacked_data.append({
                'quarter': quarter,
                'product': product,
                'sales': random.randint(200, 800)
            })
    
    plot = Plot("interval")
    plot.set_options({
        "type": "interval",
        "data": stacked_data,
        "encode": {
            "x": "quarter",
            "y": "sales",
            "color": "product"
        },
        "transform": [{"type": "stackY"}],
        "tooltip": True,
        "legend": True,
        "width": 700,
        "height": 400
    })
    plot.set_title("季度产品销售堆叠图")
    
    return plot.render_notebook()

def demo_responsive_bar():
    """响应式柱状图"""
    print("📱 响应式柱状图")
    
    data = generate_bar_data()['sales_by_region']
    
    plot = Plot("interval")
    plot.set_options({
        "type": "interval",
        "data": data,
        "encode": {
            "x": "region",
            "y": "sales"
        },
        "style": {
            "fill": "#fa8c16"
        },
        "tooltip": True,
        "autoFit": True  # 自适应容器大小
    })
    plot.set_title("自适应柱状图")
    
    return plot.render_notebook()

# 演示函数列表
DEMOS = [
    ("demo_basic_bar", "基础柱状图"),
    ("demo_styled_bar", "带样式的柱状图"),
    ("demo_horizontal_bar", "横向柱状图"),
    ("demo_grouped_bar", "分组柱状图"),
    ("demo_stacked_bar", "堆叠柱状图"),
    ("demo_responsive_bar", "响应式柱状图")
]

def run_all_bar_demos():
    """运行所有柱状图演示"""
    print("🚀 G2PY 柱状图演示开始")
    print("=" * 40)
    
    for func_name, desc in DEMOS:
        try:
            print(f"\n📊 执行: {desc}")
            result = globals()[func_name]()
            print(f"   ✓ 成功")
        except Exception as e:
            print(f"   ✗ 失败: {e}")
    
    print("\n🎉 柱状图演示完成！")

if __name__ == "__main__":
    print("📊 G2PY 柱状图演示")
    print("=" * 30)
    print("🔍 可用的演示函数:")
    for i, (func_name, desc) in enumerate(DEMOS, 1):
        print(f"{i}. {func_name}() - {desc}")
    
    print("\n💡 使用方法:")
    print("   在Jupyter中: demo_basic_bar()")
    print("   运行所有: run_all_bar_demos()")
    print("\n📏 尺寸设置示例:")
    print("   在set_options中设置: 'width': 800, 'height': 400")
    print("   自适应设置: 'autoFit': True") 