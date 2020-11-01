#!/usr/bin/env python3
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def get_ip():
    x_forwarded_for = request.headers.getlist('X-Forwarded-For')
    if x_forwarded_for:
        remote_ip = x_forwarded_for[0]
    else:
        remote_ip = request.remote_addr

    return jsonify(remote_ip), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7070)
