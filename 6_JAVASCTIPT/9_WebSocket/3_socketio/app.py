from flask import Flask, send_from_directory
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key' # socketio가 내부적으로 세션을 사용함
socketio = SocketIO(app)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@socketio.on('message')
def handle_message(msg):
    print('Message: ', msg)
    send(msg, broadcast=True)



if __name__=="__main__":
    # app.run(debug=True)
    socketio.run(app, debug=True)

