from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # 物理注入 DOM 结构与 CSS 渲染树
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Minimalist Test</title>
        <style>
            body {
                margin: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background-color: #121212; /* 深色极简背景 */
                color: #ffffff;            /* 高对比度白字 */
                font-family: 'Helvetica Neue', -apple-system, sans-serif;
            }
            h1 {
                font-size: 8vw;            /* 基于视口宽度的响应式缩放 */
                font-weight: 300;          /* 细体字重 */
                letter-spacing: 8px;       /* 增加字间距强化极简感 */
                text-transform: uppercase;
            }
        </style>
    </head>
    <body>
        <h1>ZEFH GAY</h1>
    </body>
    </html>
    """
    return html_content

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
