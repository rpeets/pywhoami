import os
import sys
import socket
from flask import Flask

fport = 8080
myhost = os.uname()[1]
ipaddr = socket.gethostbyname(socket.gethostname())
pyver  = sys.version.split()[0]

data = {'version': '1.0.0',
        'hostname': myhost,
        'ipaddress': ipaddr,
        'port': fport, 
        'python': pyver}

app = Flask(__name__)
@app.route('/')
def hello_world():
    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=fport, debug=True)
