#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
G2PY 重构版本测试脚本
验证Python3.11+兼容性、离线模式和新功能
"""

import sys
import os
import tempfile
from pathlib import Path

def test_python_version():
    """测试Python版本兼容性"""
    print(f"✓ Python版本: {sys.version}")
    
    major, minor = sys.version_info[:2]
    if major >= 3 and minor >= 8:
        print("✓ Python版本符合要求 (>=3.8)")
    else:
        print("❌ Python版本过低，需要3.8+")
        return False
    return True

def test_dependencies():
    """测试依赖兼容性"""
    print("\n📦 测试依赖兼容性...")
    
    try:
        import jinja2
        print(f"✓ jinja2版本: {jinja2.__version__}")
        
        # 检查版本是否符合要求
        from packaging import version
        if version.parse(jinja2.__version__) >= version.parse("3.1.0"):
            print("✓ jinja2版本符合要求 (>=3.1.0)")
        else:
            print("❌ jinja2版本过低，需要>=3.1.0")
            return False
            
    except ImportError as e:
        print(f"❌ 依赖导入失败: {e}")
        return False
    
    try:
        import simplejson
        print(f"✓ simplejson版本: {simplejson.__version__}")
    except ImportError:
        print("⚠️ simplejson未安装，使用标准json库")
    
    return True

def test_g2py_import():
    """测试G2py导入"""
    print("\n📊 测试G2py导入...")
    
    try:
        from g2py import Plot
        print("✓ G2py导入成功")
        
        # 测试基础实例化
        chart = Plot("Chart")
        print("✓ Plot实例创建成功")
        
        # 测试新参数
        chart_offline = Plot("Chart", offline=True)
        print("✓ 离线模式实例创建成功")
        
        return True
    except Exception as e:
        print(f"❌ G2py导入失败: {e}")
        return False

def test_basic_functionality():
    """测试基础功能"""
    print("\n⚙️ 测试基础功能...")
    
    try:
        from g2py import Plot
        
        # 测试在线模式
        chart = Plot("Chart", offline=False)
        chart.set_title("测试图表")
        chart.set_options({
            "type": "interval",
            "data": [{"x": "A", "y": 10}, {"x": "B", "y": 20}],
            "encode": {"x": "x", "y": "y"}
        })
        
        # 测试HTML生成
        html = chart.render_html()
        print("✓ HTML渲染成功")
        
        # 测试链式调用
        chain_chart = (Plot("Chart")
                      .set_title("链式测试")
                      .set_options({"type": "point", "data": []}))
        print("✓ 链式调用成功")
        
        return True
    except Exception as e:
        print(f"❌ 基础功能测试失败: {e}")
        return False

def test_offline_mode():
    """测试离线模式"""
    print("\n🔌 测试离线模式...")
    
    try:
        from g2py import Plot
        
        # 检查离线文件是否存在
        offline_file = Path(__file__).parent / "g2py" / "static" / "g2.min.js"
        if not offline_file.exists():
            print("⚠️ 离线G2文件不存在，跳过离线模式测试")
            return True
        
        print("✓ 离线G2文件存在")
        
        # 测试离线模式创建
        chart = Plot("Chart", offline=True)
        chart.set_options({
            "type": "line",
            "data": [{"x": 1, "y": 10}, {"x": 2, "y": 20}]
        })
        
        # 测试HTML生成（离线模式）
        html = chart.render_html()
        if "g2.min.js" in html:
            print("✓ 离线模式HTML包含本地引用")
        else:
            print("❌ 离线模式HTML未包含本地引用")
            return False
        
        return True
    except Exception as e:
        print(f"❌ 离线模式测试失败: {e}")
        return False

def test_jupyter_methods():
    """测试Jupyter方法"""
    print("\n📓 测试Jupyter方法...")
    
    try:
        from g2py import Plot
        
        chart = Plot("Chart", offline=False)
        chart.set_options({
            "type": "point",
            "data": [{"x": 1, "y": 10}]
        })
        
        # 测试notebook渲染
        notebook_html = chart.render_notebook()
        print("✓ render_notebook方法成功")
        
        # 测试jupyterlab渲染
        lab_html = chart.render_jupyter_lab()
        print("✓ render_jupyter_lab方法成功")
        
        # 测试show方法
        show_html = chart.show()
        print("✓ show方法成功")
        
        return True
    except Exception as e:
        print(f"❌ Jupyter方法测试失败: {e}")
        return False

def test_file_operations():
    """测试文件操作"""
    print("\n📁 测试文件操作...")
    
    try:
        from g2py import Plot
        
        with tempfile.TemporaryDirectory() as temp_dir:
            chart = Plot("Chart", offline=False)
            chart.set_options({
                "type": "interval",
                "data": [{"category": "A", "value": 40}],
                "encode": {"x": "category", "y": "value"}
            })
            
            # 测试文件渲染
            output_path = os.path.join(temp_dir, "test_chart.html")
            result_path = chart.render(output_path)
            
            if os.path.exists(result_path):
                print("✓ 文件渲染成功")
                
                # 检查文件内容
                with open(result_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if "G2.Chart" in content:
                        print("✓ HTML文件内容正确")
                    else:
                        print("❌ HTML文件内容异常")
                        return False
            else:
                print("❌ 输出文件不存在")
                return False
        
        return True
    except Exception as e:
        print(f"❌ 文件操作测试失败: {e}")
        return False

def main():
    """主测试函数"""
    print("=== G2PY 重构版本兼容性测试 ===\n")
    
    tests = [
        ("Python版本检查", test_python_version),
        ("依赖兼容性检查", test_dependencies),
        ("G2py导入测试", test_g2py_import),
        ("基础功能测试", test_basic_functionality),
        ("离线模式测试", test_offline_mode),
        ("Jupyter方法测试", test_jupyter_methods),
        ("文件操作测试", test_file_operations),
    ]
    
    passed = 0
    failed = 0
    
    for test_name, test_func in tests:
        print(f"\n--- {test_name} ---")
        try:
            if test_func():
                passed += 1
                print(f"✅ {test_name} 通过")
            else:
                failed += 1
                print(f"❌ {test_name} 失败")
        except Exception as e:
            failed += 1
            print(f"❌ {test_name} 异常: {e}")
    
    print(f"\n=== 测试结果总结 ===")
    print(f"✅ 通过: {passed}")
    print(f"❌ 失败: {failed}")
    print(f"📊 总计: {passed + failed}")
    
    if failed == 0:
        print("\n🎉 所有测试通过！G2PY重构版本可以正常使用。")
    else:
        print(f"\n⚠️ 有{failed}个测试失败，请检查相关功能。")
    
    return failed == 0

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 