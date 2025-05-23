# -*- coding: utf-8 -*-
"""
Created on 2023-09-22

> g2py Plot class - 重构版本
支持Python3.11+, 优化代码结构，添加离线模式支持
"""
import uuid
import os
from pathlib import Path
from jinja2 import Environment
from typing import Optional, Dict, Any, Union, List

from g2py.engine import Engine
from g2py.helper.code import json_dump_to_js
from g2py.helper.file import write_utf8_file
from g2py.helper.html import HTML

# G2库配置
G2_ONLINE_LIB = 'https://unpkg.com/@antv/g2@5.1.4/dist/g2.min.js'
G2_OFFLINE_LIB_PATH = os.path.join(os.path.dirname(__file__), 'static', 'g2.min.js')


class Plot:
    """
    G2图表封装类
    
    提供统一的图表创建、配置和渲染接口
    支持在线和离线模式，兼容Jupyter Notebook和JupyterLab
    """
    
    def __init__(self, plot_type: str = "Chart", version: str = "5", offline: bool = False):
        """
        初始化图表实例
        
        Args:
            plot_type (str): 图表类型，默认为"Chart"
            version (str): G2版本，默认为"5"
            offline (bool): 是否使用离线模式，默认False
        """
        self.plot_type = plot_type
        self.plot_id = uuid.uuid4().hex
        self.version = version
        self.offline = offline
        self.options = {}
        self.page_title = "G2Py 图表"
        self._validate_offline_files()

    def _validate_offline_files(self) -> None:
        """验证离线文件是否存在"""
        if self.offline and not os.path.exists(G2_OFFLINE_LIB_PATH):
            raise FileNotFoundError(
                f"离线G2文件不存在: {G2_OFFLINE_LIB_PATH}\n"
                "请确保g2.min.js文件在static目录中"
            )

    def set_options(self, options: Optional[Dict[str, Any]] = None, 
                   js_code: Optional[str] = None) -> 'Plot':
        """
        设置G2图表配置选项
        
        Args:
            options (dict, optional): G2配置对象
            js_code (str, optional): 自定义JavaScript代码
            
        Returns:
            Plot: 返回self以支持链式调用
        """
        if options is not None:
            self.options.update(options)
        if js_code is not None:
            self.options["js_code"] = js_code
        return self

    def set_title(self, title: str) -> 'Plot':
        """
        设置页面标题
        
        Args:
            title (str): 页面标题
            
        Returns:
            Plot: 返回self以支持链式调用
        """
        self.page_title = title
        return self

    def set_size(self, width: Optional[int] = None, height: Optional[int] = None, 
                 auto_fit: bool = False) -> 'Plot':
        """
        设置图表尺寸
        
        Args:
            width (int, optional): 图表宽度，不设置则使用默认值
            height (int, optional): 图表高度，不设置则使用默认值  
            auto_fit (bool): 是否自适应容器大小，默认False
            
        Returns:
            Plot: 返回self以支持链式调用
        """
        if auto_fit:
            self.options["autoFit"] = True
            # 移除固定尺寸设置
            self.options.pop("width", None)
            self.options.pop("height", None)
        else:
            if width is not None:
                self.options["width"] = width
            if height is not None:
                self.options["height"] = height
            # 确保不使用自适应
            self.options.pop("autoFit", None)
        return self

    def dump_js_options(self, env: Optional[Environment] = None, **kwargs) -> str:
        """
        导出JavaScript配置选项
        
        Args:
            env (Environment, optional): Jinja2环境
            **kwargs: 额外参数
            
        Returns:
            str: JavaScript配置字符串
        """
        return json_dump_to_js(self.options)

    def _get_dependencies(self) -> List[Dict[str, str]]:
        """
        获取依赖项配置
        
        Returns:
            list: 依赖项列表
        """
        if self.offline:
            # 使用相对路径指向静态文件
            offline_path = "./g2.min.js"  # 相对于HTML文件的路径
            return [{
                "name": "G2",
                "asset": offline_path,
                "local": True
            }]
        else:
            return [{
                "name": "G2", 
                "asset": G2_ONLINE_LIB,
                "local": False
            }]

    def render_notebook(self, env: Optional[Environment] = None, **kwargs) -> HTML:
        """
        在Jupyter Notebook中渲染图表
        
        Args:
            env (Environment, optional): Jinja2环境
            **kwargs: 额外参数
            
        Returns:
            HTML: HTML对象，用于在Notebook中显示
        """
        self.js_options = self.dump_js_options(env=env, **kwargs)
        self.dependencies = self._get_dependencies()
        
        return HTML(Engine(env=env).render(
            plot=self,
            template_name="notebook.html",
            **kwargs
        ))

    def render_jupyter_lab(self, env: Optional[Environment] = None, **kwargs) -> HTML:
        """
        在JupyterLab中渲染图表
        
        Args:
            env (Environment, optional): Jinja2环境  
            **kwargs: 额外参数
            
        Returns:
            HTML: HTML对象，用于在JupyterLab中显示
        """
        self.js_options = self.dump_js_options(env=env, **kwargs)
        self.dependencies = self._get_dependencies()
        
        return HTML(Engine(env=env).render(
            plot=self,
            template_name="jupyter-lab.html",
            **kwargs
        ))

    def render_html(self, env: Optional[Environment] = None, **kwargs) -> str:
        """
        渲染为HTML字符串
        
        Args:
            env (Environment, optional): Jinja2环境
            **kwargs: 额外参数
            
        Returns:
            str: HTML字符串
        """
        self.js_options = self.dump_js_options(env=env, **kwargs)
        self.dependencies = self._get_dependencies()
        
        return Engine(env=env).render(
            plot=self,
            template_name="plot.html",
            **kwargs
        )

    def render(self, path: str = "plot.html", env: Optional[Environment] = None, 
              copy_static: bool = True, **kwargs) -> str:
        """
        渲染图表到HTML文件
        
        Args:
            path (str): 输出文件路径，默认"plot.html"
            env (Environment, optional): Jinja2环境
            copy_static (bool): 是否复制静态文件到输出目录，默认True
            **kwargs: 额外参数
            
        Returns:
            str: 输出文件路径
        """
        # 渲染HTML内容
        html = self.render_html(env, **kwargs)
        
        # 写入HTML文件
        write_utf8_file(path, html)
        
        # 如果是离线模式，复制静态文件
        if self.offline and copy_static:
            self._copy_static_files(path)
            
        return path

    def _copy_static_files(self, html_path: str) -> None:
        """
        复制静态文件到HTML文件同目录
        
        Args:
            html_path (str): HTML文件路径
        """
        try:
            import shutil
            html_dir = os.path.dirname(os.path.abspath(html_path))
            dest_path = os.path.join(html_dir, "g2.min.js")
            
            if not os.path.exists(dest_path):
                shutil.copy2(G2_OFFLINE_LIB_PATH, dest_path)
                print(f"已复制G2离线文件到: {dest_path}")
        except Exception as e:
            print(f"复制静态文件失败: {e}")

    def show(self, width: int = 800, height: int = 400) -> HTML:
        """
        快捷显示方法，自动检测环境
        
        Args:
            width (int): 图表宽度，默认800
            height (int): 图表高度，默认400
            
        Returns:
            HTML: HTML对象用于显示
        """
        # 设置图表尺寸
        if "autoFit" not in self.options:
            self.options["width"] = width
            self.options["height"] = height
            
        # 尝试检测Jupyter环境
        try:
            from IPython import get_ipython
            ipython = get_ipython()
            if ipython is not None:
                if hasattr(ipython, 'kernel'):
                    # JupyterLab环境
                    return self.render_jupyter_lab()
                else:
                    # Jupyter Notebook环境
                    return self.render_notebook()
        except ImportError:
            pass
            
        # 默认返回notebook渲染
        return self.render_notebook()

    def __repr__(self) -> str:
        """字符串表示"""
        return f"Plot(type='{self.plot_type}', id='{self.plot_id[:8]}...', offline={self.offline})"


