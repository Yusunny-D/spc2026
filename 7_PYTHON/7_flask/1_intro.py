from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>웰컴투 마이 홈2</h1>
    """

if __name__ == '__main__':
    # app.run(debug=True) # 디버그 모드 개발 끝나고는 꼭 끄기.. 특히 배포 전에는!!
    app.run()

