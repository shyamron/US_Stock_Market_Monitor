from flask import Flask, request
from flask_cors import CORS
from checking_threshold import *
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import uuid
from threading import Thread

app = Flask(__name__)
cors = CORS(app)
cors = CORS(app, origins=["*"])
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print("File modified")

def start_task(entry_id,entered_data):
    monitor(entry_id,entered_data)
    
@app.route("/submit", methods=["POST"])
def submit_form():
    entered_data = request.get_json()    
    print(entered_data)
    entry_id = str(uuid.uuid1())
    thread = Thread(target=start_task, args=(entry_id,entered_data))
    thread.start()
    return "Your request has been saved!"
        
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__=="main":
    observer = Observer()
    event_handler = MyHandler()
    observer.schedule(event_handler, path='.', recursive=True)
    observer.start()
    app.run(debug=True)    
        

