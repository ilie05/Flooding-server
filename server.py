from flask import Flask, render_template
from flask_socketio import SocketIO, emit

from rnd import RandomThread, thread

app = Flask(__name__)
app.config['SECRET_KEY'] = '`O(znh#|Ig`3oczwbGEK%I+;6.f?@Ju-+1NVo[B/NI*]5i"ik<CX[Es4Z=!t17J'
socket_io = SocketIO(app)


@socket_io.on('my event')  # Decorator to catch an event called "my event":
def test_message(message):  # test_message() is the event callback function.
    emit('my response', {'data': 'got it!'})  # Trigger a new event called "my response"


@socket_io.on('connect', namespace='/test')
def test_connect():
    # need visibility of the global thread object
    # global thread
    print('Client connected')
    # Start the random number generator thread only if the thread has not been started before.
    # if not thread.is_alive():
    print("Starting Thread")
    thread = RandomThread(socket_io)
    thread.start()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test')
def test():
    return "render_template('index.html')"


if __name__ == '__main__':
    socket_io.run(app, port=3000, debug=True)
