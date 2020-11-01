#!/usr/bin/env python3
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def ip():
    return jsonify(request.remote_addr)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7070)
