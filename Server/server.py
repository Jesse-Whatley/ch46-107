from flask import Flask

app = Flask(__name__) # is the server 

@app.get("/")# this is the API
def home(): # this is the API
    return "hello from flask" # this is the API

app.run(debug=True)