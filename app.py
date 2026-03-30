from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Neon Test</title>
        <style>
            body {
                margin: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background-color: #050505; /* 机制 1: 纯黑吸收环境光 */
                font-family: 'Helvetica Neue', -apple-system, sans-serif;
            }

            .neon-box {
                padding: 40px 80px;
                border: 2px solid #0ff;
                border-radius: 15px;
                /* 机制 3: 容器内外双向反射发光 */
                box-shadow: 0 0 15px #0ff, inset 0 0 15px #0ff;
            }

            h1 {
                margin: 0;
                font-size: 7vw;
                font-weight: 300;
                letter-spacing: 12px;
                text-transform: uppercase;
                color: #fff;
                /* 机制 2: 核心白光 + 指数级衰减的青色散射光 */
                text-shadow:
                    0 0 5px #fff,
                    0 0 10px #fff,
                    0 0 20px #0ff,
                    0 0 40px #0ff,
                    0 0 80px #0ff,
                    0 0 120px #0ff;
            }
        </style>
    </head>
    <body>
        <div class="neon-box">
            <h1>Hello World</h1>
        </div>
    </body>
    </html>
    """
    return html_content

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
