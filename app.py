from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # 物理注入 DOM 结构与 CSS 渲染树 (Variabili CSS integrate)
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Fancy Test</title>
        <style>
            body {
                margin: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                /* 机制 1: 动态渐变背景 */
                background: linear-gradient(-45deg, #0f2027, #203a43, #2c5364, #121212);
                background-size: 400% 400%;
                animation: gradientBG 15s ease infinite;
                font-family: 'Helvetica Neue', -apple-system, sans-serif;
            }

            @keyframes gradientBG {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }

            .glass-card {
                /* 机制 2: 毛玻璃拟态 */
                background: rgba(255, 255, 255, 0.03);
                box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
                backdrop-filter: blur(12px);
                -webkit-backdrop-filter: blur(12px);
                border: 1px solid rgba(255, 255, 255, 0.05);
                border-radius: 24px;
                padding: 50px 100px;
                text-align: center;
            }

            h1 {
                margin: 0;
                font-size: 7vw;
                font-weight: 300;
                letter-spacing: 16px;
                text-transform: uppercase;
                color: #ffffff;
                /* 机制 3: 辉光叠加 */
                text-shadow: 0 0 10px rgba(255,255,255,0.2), 0 0 20px rgba(255,255,255,0.1);
            }
        </style>
    </head>
    <body>
        <div class="glass-card">
            <h1>ZEFH GAY</h1>
        </div>
    </body>
    </html>
    """
    return html_content

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
