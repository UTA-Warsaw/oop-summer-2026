#!/usr/bin/env python3
import webview
import os

HTML_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "redchecker.html")
with open(HTML_PATH, "r", encoding="utf-8") as f:
    HTML = f.read()

window = webview.create_window(
    title="Red Discord Checker",
    html=HTML,
    width=820,
    height=900,
    resizable=True,
    min_size=(600, 500),
)
webview.start(http_server=True)
