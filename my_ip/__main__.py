#!/usr/bin/env python3
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def get_ip():
    data = {
        'ip': _get_remote_address(),
    }

    return jsonify(data), 200


def _get_remote_address() -> str:
    x_forwarded_for = request.headers.getlist('X-Forwarded-For')
    if x_forwarded_for:
        return x_forwarded_for[0]

    return request.remote_addr


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7070)
