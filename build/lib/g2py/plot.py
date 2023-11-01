# -*- coding: utf-8 -*-
'''
Created on 2023-09-22

> g2py Plot class.
'''
import uuid
from jinja2 import Environment
from g2py.engine import Engine
from g2py.helper.code import json_dump_to_js
from g2py.helper.file import write_utf8_file
from g2py.helper.html import HTML
from typing import Optional

G2_LIB = 'https://unpkg.com/@antv/g2@5.1.4/dist/g2.min.js'


class Plot():
    '''
    instance with plot type string
    '''
    def __init__(self, plot_type: str, version: str = '5'):
        self.plot_type = plot_type
        self.plot_id = uuid.uuid4().hex
        self.version = version
        self.options = {}
        self.page_title = "g2py"

    '''
    set the G2 options, G2 code documents [here](https://G2.antv.vision/)
    '''
    def set_options(self,  options: object = None, js_code: str = None):
      if options is not None:
        self.options = options
      if js_code is not None:
        self.options["js_code"] = js_code
      return self
    '''
    get the JavaScript options of G2
    get the JavaScript code of G2
    '''
    def dump_js_options(
        self,
        env: Optional[Environment] = None,
        **kwargs
    ) -> str:
        return json_dump_to_js(self.options)

    '''
    render plot into jupyter
    '''
    def render_notebook(
        self,
        env: Optional[Environment] = None,
        **kwargs
    ) -> HTML:
        self.js_options = self.dump_js_options(env=env, **kwargs)
        # get html string
        return HTML(Engine(env=env).render(
            plot=self,
            template_name="notebook.html",
            **kwargs
        ))

    '''
    render plot into jupyter lab
    '''
    def render_jupyter_lab(
        self,
        env: Optional[Environment] = None,
        **kwargs
    ) -> HTML:
        self.js_options = self.dump_js_options(env=env, **kwargs)
        # get html string
        return HTML(Engine(env=env).render(
            plot=self,
            template_name="jupyter-lab.html",
            **kwargs
        ))

    '''
    render plot to html string
    '''
    def render_html(
        self,
        env: Optional[Environment] = None,
        **kwargs
    ) -> str:
        self.js_options = self.dump_js_options(env=env, **kwargs)
        self.dependencies = [{
            "name": "G2",
            "asset": G2_LIB,
        }]
        # get html string
        return Engine(env=env).render(
            plot=self,
            template_name="plot.html",
            **kwargs
        )

    '''
    render the plot into html file
    '''
    def render(
        self,
        path: str = "plot.html",
        env: Optional[Environment] = None,
        **kwargs
    ) -> str:
        # get html string
        html = self.render_html(env, **kwargs)
        # write output into file
        write_utf8_file(path, html)
        return path


