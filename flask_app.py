"""
Simple Flask MicroService
"""

import hashlib
from flask import Flask, request, abort

_APP = Flask(__name__)
_BIGSTR = 20

@_APP.route('/')
def showhelp():
    """Help page
    # Arguments
    # Returns
      Instructions to use the service
    """
    return 'query format: /messages/stringtext1'

@_APP.route('/messages/<hash>')
def query(inhash):
    """Query existing hash. Implementation for a GET request that returns the original message.
    A request to a non-existent <hash> should return a 404 error.

    # Arguments
        hash: hash string to query.
        example:
        curl -X POST -H "Content-Type: application/json" -d '{"message": "foo12345678901234567"}' \
        http://vinayski.pythonanywhere.com/messages
        curl http://vinayski.pythonanywhere.com/messages/a
    # Returns
        returns the orginal string if found.
    """
    return gethash(inhash)

def gethash(inhash):
    """
    #Arguments
        hash: hash string to query.
    # Returns
        returns the orginal string if found.
    """
    if len(inhash) > _BIGSTR:
        abort(404)
    else:
        return inhash

@_APP.route('/messages', methods=['POST'])
def digest():
    """
    Implementation for service that takes a message (a string) as a POST and
    returns the SHA256 hash digest of that message (in hexadecimal format)
    # Arguments
        Test example:
        curl -X POST -H "Content-Type: application/json" -d '{"message": "foo12345678901234567"}' \
        http://vinayski.pythonanywhere.com/messages

    # Returns
        returns SHA256 hash digest of that message (in hexadecimal format).
    """
    strlen = len(request.json['message'])
    if strlen > _BIGSTR:
        return "Upgrade your account to process big strings. Contact SKi@sankhe.com"
    else:
        return hashlib.sha256(request.json['message'].encode('utf-8')).hexdigest()
