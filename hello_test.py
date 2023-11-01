from g2py import Plot,JS
chart = Plot("Chart")

chart.set_options(
  {"type": "interval",
  "autoFit": "true",
  "data": {
    "type": "fetch",
    "value":
      "https://gw.alipayobjects.com/os/bmw-prod/fb9db6b7-23a5-4c23-bbef-c54a55fee580.csv",
  },
  "encode": { "x": "letter", "y": "frequency" },
  "axis": { "y": { "labelFormatter": ".0%" } },
})

# chart.set_js_options({"sssssssssssssss"})
# chart.options['js_code']=A
print(chart.render_html())

