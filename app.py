from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=5000, debug=True)
    app.run(host='0.0.0.0', port=8080, debug=True) # to be accessed via 1, opening instance 8080 sg access; 2, copying Public IPv4 DNS + :8080 to web browser
