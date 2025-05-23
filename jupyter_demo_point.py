#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
G2PY 散点图演示 - Jupyter环境
支持Python 3.11+
"""

from g2py import Plot
import random

def generate_point_data():
    """生成散点图数据"""
    return {
        'correlation': [
            {
                'x': random.randint(10, 100), 
                'y': random.randint(20, 80),
                'category': random.choice(['A', 'B', 'C'])
            } 
            for _ in range(50)
        ],
        'bubble': [
            {
                'x': random.randint(1, 50),
                'y': random.randint(10, 90),
                'size': random.randint(5, 30),
                'category': random.choice(['产品1', '产品2', '产品3', '产品4'])
            }
            for _ in range(30)
        ],
        'performance': [
            {
                'score': random.randint(60, 100),
                'salary': random.randint(5000, 20000),
                'experience': random.randint(1, 10),
                'department': random.choice(['技术部', '销售部', '市场部'])
            }
            for _ in range(40)
        ]
    }

def demo_basic_point():
    """基础散点图演示"""
    print("⭐ 基础散点图演示")
    
    data = generate_point_data()['correlation']
    
    plot = Plot("point")
    plot.set_options({
        "type": "point",
        "data": data,
        "encode": {
            "x": "x",
            "y": "y"
        },
        "style": {
            "fill": "#1890ff",
            "stroke": "#0050b3",
            "r": 3
        }
    })
    plot.set_title("基础散点图")
    
    return plot.render_notebook()

def demo_colored_point():
    """彩色分类散点图"""
    print("🌈 彩色分类散点图")
    
    data = generate_point_data()['correlation']
    
    plot = Plot("point")
    plot.set_options({
        "type": "point",
        "data": data,
        "encode": {
            "x": "x",
            "y": "y",
            "color": "category"
        },
        "style": {
            "r": 4,
            "stroke": "#fff",
            "lineWidth": 1
        },
        "tooltip": True,
        "legend": True,
        "width": 600,
        "height": 400
    })
    plot.set_title("按类别分色的散点图")
    
    return plot.render_notebook()

def demo_bubble_chart():
    """气泡图"""
    print("🎈 气泡图演示")
    
    data = generate_point_data()['bubble']
    
    plot = Plot("point")
    plot.set_options({
        "type": "point",
        "data": data,
        "encode": {
            "x": "x",
            "y": "y",
            "size": "size",
            "color": "category"
        },
        "style": {
            "stroke": "#fff",
            "lineWidth": 1,
            "opacity": 0.7
        },
        "tooltip": True,
        "legend": True,
        "width": 700,
        "height": 450
    })
    plot.set_title("产品表现气泡图")
    
    return plot.render_notebook()

def demo_styled_point():
    """带样式的散点图"""
    print("🎨 带样式的散点图")
    
    data = generate_point_data()['performance']
    
    plot = Plot("point")
    plot.set_options({
        "type": "point",
        "data": data,
        "encode": {
            "x": "score",
            "y": "salary",
            "color": "department"
        },
        "style": {
            "r": 5,
            "stroke": "#666",
            "lineWidth": 2,
            "opacity": 0.8
        },
        "tooltip": True,
        "legend": True,
        "width": 650,
        "height": 400
    })
    plot.set_title("员工绩效薪资关系图")
    
    return plot.render_notebook()

def demo_size_encoded_point():
    """尺寸编码散点图"""
    print("📏 尺寸编码散点图")
    
    data = generate_point_data()['performance']
    
    plot = Plot("point")
    plot.set_options({
        "type": "point",
        "data": data,
        "encode": {
            "x": "score",
            "y": "salary",
            "size": "experience",
            "color": "department"
        },
        "style": {
            "stroke": "#fff",
            "lineWidth": 1,
            "opacity": 0.8
        },
        "tooltip": True,
        "legend": True,
        "width": 800,
        "height": 500
    })
    plot.set_title("多维度员工数据分析")
    
    return plot.render_notebook()

def demo_responsive_point():
    """响应式散点图"""
    print("📱 响应式散点图")
    
    data = generate_point_data()['correlation']
    
    plot = Plot("point")
    plot.set_options({
        "type": "point",
        "data": data,
        "encode": {
            "x": "x",
            "y": "y",
            "color": "category"
        },
        "style": {
            "r": 4,
            "opacity": 0.7
        },
        "tooltip": True,
        "legend": True,
        "autoFit": True  # 自适应容器大小
    })
    plot.set_title("自适应散点图")
    
    return plot.render_notebook()

# 演示函数列表
DEMOS = [
    ("demo_basic_point", "基础散点图"),
    ("demo_colored_point", "彩色分类散点图"),
    ("demo_bubble_chart", "气泡图"),
    ("demo_styled_point", "带样式的散点图"),
    ("demo_size_encoded_point", "尺寸编码散点图"),
    ("demo_responsive_point", "响应式散点图")
]

def run_all_point_demos():
    """运行所有散点图演示"""
    print("🚀 G2PY 散点图演示开始")
    print("=" * 40)
    
    for func_name, desc in DEMOS:
        try:
            print(f"\n⭐ 执行: {desc}")
            result = globals()[func_name]()
            print(f"   ✓ 成功")
        except Exception as e:
            print(f"   ✗ 失败: {e}")
    
    print("\n🎉 散点图演示完成！")

if __name__ == "__main__":
    print("⭐ G2PY 散点图演示")
    print("=" * 30)
    print("🔍 可用的演示函数:")
    for i, (func_name, desc) in enumerate(DEMOS, 1):
        print(f"{i}. {func_name}() - {desc}")
    
    print("\n💡 使用方法:")
    print("   在Jupyter中: demo_basic_point()")
    print("   运行所有: run_all_point_demos()")
    print("\n📏 尺寸设置示例:")
    print("   在set_options中设置: 'width': 800, 'height': 400")
    print("   自适应设置: 'autoFit': True") 