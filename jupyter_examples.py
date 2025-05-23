#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
G2PY Jupyter环境演示脚本
支持Python 3.11+，重构版本
"""

from g2py import Plot
import random
import json

def generate_sample_data():
    """生成示例数据"""
    return {
        'sales': [
            {'month': f'{i}月', 'value': random.randint(800, 2000)} 
            for i in range(1, 13)
        ],
        'categories': [
            {'name': cat, 'value': random.randint(100, 500)} 
            for cat in ['电子产品', '服装', '家居', '图书', '运动']
        ],
        'scatter': [
            {'x': random.randint(10, 100), 'y': random.randint(20, 200)} 
            for _ in range(30)
        ]
    }

def demo_notebook_basic():
    """Jupyter Notebook基础演示"""
    print("=== Jupyter Notebook 基础图表演示 ===")
    
    data = generate_sample_data()['categories']
    
    # 创建柱状图
    plot = Plot("interval")
    plot.set_options({
        "type": "interval",
        "data": data,
        "encode": {
            "x": "name",
            "y": "value"
        },
        "style": {
            "fill": "#1890ff"
        }
    })
    plot.set_title("类目销售数据 - Notebook版本")
    
    # 在Jupyter Notebook中显示
    return plot.render_notebook()

def demo_jupyterlab_optimized():
    """JupyterLab优化演示"""
    print("=== JupyterLab 优化图表演示 ===")
    
    data = generate_sample_data()['sales']
    
    # 创建折线图
    plot = Plot("line")
    plot.set_options({
        "type": "line",
        "data": data,
        "encode": {
            "x": "month",
            "y": "value"
        },
        "style": {
            "stroke": "#52c41a",
            "lineWidth": 3,
            "opacity": 0.8
        },
        "tooltip": True
    })
    plot.set_title("月度销售趋势 - JupyterLab优化版本")
    
    # 在JupyterLab中显示（自动优化）
    return plot.render_jupyter_lab()

def demo_interactive_notebook():
    """交互式Notebook演示"""
    print("=== 交互式图表演示 ===")
    
    # 多系列数据
    multi_data = []
    months = ['Q1', 'Q2', 'Q3', 'Q4']
    for month in months:
        multi_data.extend([
            {'quarter': month, 'type': '收入', 'value': random.randint(1000, 2000)},
            {'quarter': month, 'type': '利润', 'value': random.randint(300, 800)}
        ])
    
    plot = Plot("interval")
    plot.set_options({
        "type": "interval",
        "data": multi_data,
        "encode": {
            "x": "quarter",
            "y": "value",
            "color": "type"
        },
        "tooltip": True,
        "legend": True
    })
    plot.set_title("季度财务数据对比")
    
    return plot.render_notebook()

def demo_chain_api_jupyter():
    """链式API在Jupyter中的使用"""
    print("=== 链式API演示 ===")
    
    data = generate_sample_data()['scatter']
    
    # 使用链式API创建散点图
    return (Plot("point")
            .set_options({
                "type": "point",
                "data": data,
                "encode": {
                    "x": "x",
                    "y": "y"
                },
                "style": {
                    "fill": "#fa541c",
                    "opacity": 0.7,
                    "size": 8
                },
                "tooltip": True
            })
            .set_title("性能分析散点图 - 链式API")
            .render_notebook())

def demo_custom_styling():
    """自定义样式演示"""
    print("=== 自定义样式演示 ===")
    
    # 饼图数据
    pie_data = [
        {'segment': 'A类客户', 'value': 35},
        {'segment': 'B类客户', 'value': 28},
        {'segment': 'C类客户', 'value': 22},
        {'segment': 'D类客户', 'value': 15}
    ]
    
    plot = Plot("interval")
    plot.set_options({
        "type": "interval",
        "data": pie_data,
        "encode": {
            "y": "value",
            "color": "segment"
        },
        "coordinate": "theta",  # 极坐标系统，创建饼图
        "legend": True
    })
    plot.set_title("客户分布饼图")
    
    return plot.render_notebook()

def demo_real_time_simulation():
    """模拟实时数据演示"""
    print("=== 实时数据模拟演示 ===")
    
    # 模拟时间序列数据
    time_data = []
    for i in range(20):
        time_data.append({
            'time': f'T{i:02d}',
            'value': random.randint(50, 150) + (i * 2)  # 添加趋势
        })
    
    plot = Plot("area")
    plot.set_options({
        "type": "area",
        "data": time_data,
        "encode": {
            "x": "time",
            "y": "value"
        },
        "style": {
            "fill": "#722ed1",
            "opacity": 0.6
        }
    })
    plot.set_title("实时监控数据")
    
    return plot.render_notebook()

def demo_environment_detection():
    """环境自动检测演示"""
    print("=== 环境自动检测演示 ===")
    
    data = generate_sample_data()['categories']
    
    plot = Plot("interval")
    plot.set_options({
        "type": "interval",
        "data": data,
        "encode": {
            "x": "name",
            "y": "value"
        }
    })
    plot.set_title("环境自适应图表")
    
    # G2PY会自动检测当前环境并选择最佳渲染方式
    try:
        # 尝试Jupyter Lab渲染
        return plot.render_jupyter_lab()
    except:
        try:
            # 回退到Notebook渲染
            return plot.render_notebook()
        except:
            # 最终回退到HTML渲染
            return plot.render_html()

def demo_offline_mode():
    """离线模式演示"""
    print("=== 离线模式演示 ===")
    
    data = generate_sample_data()['sales']
    
    # 创建离线模式图表
    try:
        plot = Plot("line", offline=True)
        plot.set_options({
            "type": "line",
            "data": data,
            "encode": {
                "x": "month",
                "y": "value"
            },
            "style": {
                "stroke": "#1890ff",
                "lineWidth": 2
            }
        })
        plot.set_title("离线模式图表")
        
        return plot.render_notebook()
    except FileNotFoundError as e:
        print(f"离线模式需要g2.min.js文件: {e}")
        # 使用在线模式作为备用
        plot = Plot("line", offline=False)
        plot.set_options({
            "type": "line",
            "data": data,
            "encode": {
                "x": "month",
                "y": "value"
            }
        })
        return plot.render_notebook()

def jupyter_tips_and_tricks():
    """Jupyter使用技巧演示"""
    print("=== Jupyter使用技巧 ===")
    
    tips = [
        "✓ 使用 render_notebook() 在Jupyter Notebook中显示",
        "✓ 使用 render_jupyter_lab() 在JupyterLab中获得更好效果",
        "✓ 使用 set_options() 配置图表选项",
        "✓ 支持链式调用：plot.set_options().set_title().render_notebook()",
        "✓ 支持离线模式和在线模式切换",
        "✓ 完全兼容Python 3.11+"
    ]
    
    for tip in tips:
        print(tip)
    
    # 创建功能展示图表
    feature_data = [
        {'feature': 'Notebook支持', 'score': 10},
        {'feature': 'JupyterLab优化', 'score': 10},
        {'feature': 'API简洁度', 'score': 9},
        {'feature': '性能', 'score': 9},
        {'feature': '兼容性', 'score': 10}
    ]
    
    plot = Plot("interval")
    plot.set_options({
        "type": "interval",
        "data": feature_data,
        "encode": {
            "x": "feature",
            "y": "score"
        },
        "style": {
            "fill": "#13c2c2"
        }
    })
    plot.set_title("G2PY功能评分")
    
    return plot.render_notebook()

def run_all_demos():
    """运行所有演示"""
    print("🚀 G2PY Jupyter环境演示开始")
    print("=" * 50)
    
    demos = [
        demo_notebook_basic,
        demo_jupyterlab_optimized,
        demo_interactive_notebook,
        demo_chain_api_jupyter,
        demo_custom_styling,
        demo_real_time_simulation,
        demo_environment_detection,
        demo_offline_mode,
        jupyter_tips_and_tricks
    ]
    
    results = []
    for i, demo in enumerate(demos, 1):
        try:
            print(f"\n{i}. 执行 {demo.__name__}")
            result = demo()
            results.append(f"✓ {demo.__name__} - 成功")
            print(f"   状态: 成功")
        except Exception as e:
            results.append(f"✗ {demo.__name__} - 失败: {str(e)}")
            print(f"   状态: 失败 - {str(e)}")
    
    print("\n" + "=" * 50)
    print("📊 演示结果总结:")
    for result in results:
        print(f"  {result}")
    
    success_count = len([r for r in results if "✓" in r])
    total_count = len(demos)
    
    print(f"\n🎉 演示完成！共执行了 {total_count} 个演示案例")
    print(f"✅ 成功: {success_count}/{total_count}")
    print("💡 在Jupyter环境中运行此脚本以查看图表效果")

if __name__ == "__main__":
    # 检查是否在Jupyter环境中
    try:
        import IPython
        if IPython.get_ipython() is not None:
            print("🔍 检测到Jupyter环境")
            print("📝 建议：将此脚本中的函数复制到Jupyter cell中执行")
            print("🎯 或者直接调用单个演示函数")
        else:
            print("🔍 当前在标准Python环境中")
            print("📝 建议：在Jupyter Notebook或JupyterLab中运行以获得最佳效果")
    except ImportError:
        print("🔍 当前在标准Python环境中")
        print("📝 建议：在Jupyter Notebook或JupyterLab中运行以获得最佳效果")
    
    print("\n📊 可用的演示函数:")
    print("1. demo_notebook_basic() - 基础图表演示")
    print("2. demo_jupyterlab_optimized() - JupyterLab优化演示")
    print("3. demo_interactive_notebook() - 交互式图表演示")
    print("4. demo_chain_api_jupyter() - 链式API演示")
    print("5. demo_custom_styling() - 自定义样式演示")
    print("6. demo_real_time_simulation() - 实时数据模拟演示")
    print("7. demo_environment_detection() - 环境自动检测演示")
    print("8. demo_offline_mode() - 离线模式演示")
    print("9. jupyter_tips_and_tricks() - 使用技巧演示")
    print("10. run_all_demos() - 运行所有演示")
    
    print("\n💡 在Jupyter中单独运行某个演示:")
    print("   例如: demo_notebook_basic()")
    print("   或者: run_all_demos() 查看所有演示")
    
    # 不自动运行所有演示，让用户选择
    # run_all_demos() 