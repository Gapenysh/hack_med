
from flask_socketio import SocketIO, emit

socketio = SocketIO(cors_allowed_origns="*")

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    emit('message', {'data': 'Connected'})

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('message')
def handle_message(data):
    print('Message received: ' + str(data))
    emit('message', {'data': 'Message received: ' + str(data)})