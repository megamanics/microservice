"""
Simple Flask MicroService
"""

import hashlib
from flask import Flask, request, abort
from flask_sqlalchemy import SQLAlchemy

APP = Flask(__name__)
_BIGSTR = 20

APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
#APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
DB = SQLAlchemy(APP)

class Message(DB.Model):
    """Construct a Message class.
    """
    keyid = DB.Column(DB.Integer, primary_key=True)
    msg = DB.Column(DB.String(_BIGSTR), unique=True)
    digest = DB.Column(DB.String(256), unique=True)

    def __init__(self, msg):
        self.msg = msg
        self.digest = hashlib.sha256(msg.encode('utf-8')).hexdigest()

    def __repr__(self):
        return self.digest

def add(msgtxt):
    """ Add msg to the db
    param: msgtxt
    msg string
    return: digest
    digest of msg
    """
    #with app.app_context():
    msg = Message(msgtxt)
    DB.session.add(msg)
    DB.session.commit()
    DB.session.flush()
    return msg

def querymsg(msgtxt):
    """ Query DB
    param: msgtxt
    msg string
    return: Message
    """
    msg = Message.query.filter_by(msg=msgtxt).first()
    return msg

def querydigest(digestxt):
    """ Query DB with digest string.

    Parameters
    ----------
    param: digestxt
        msg digestxt
    Returns
    -------
        Message
    """
    msg = Message.query.filter_by(digest=digestxt).first()
    return msg

@APP.route('/')
def showhelp():
    """Help page
    # Arguments
    # Returns
      Instructions to use the service
    """
    return 'query format: /messages/stringtext1'

@APP.route('/messages/<inhash>')
def query(inhash):
    """Query existing hash. Implementation for a GET request that returns the original message.
    Parameters
    ----------
    inhash: string
        hash string to query.
    Returns
    -------
    str: string
        Orginal string if found
    Raises
    ------
         A request to a non-existent <hash> should return a 404 error.
    Example
    -------
    >>> curl -X POST -H "Content-Type: application/json" -d '{"message": "foo12345678901234567"}' \
        http://vinayski.pythonanywhere.com/messages
    >>> curl http://vinayski.pythonanywhere.com/messages/a
    """
    strlen = len(inhash)
    if strlen > 256:
        return "Upgrade your account to process big strings. Contact SKi@sankhe.com"
    else:
        msg = querydigest(inhash)
        if msg is None:
            abort(404)
        else:
            return msg.msg

@APP.route('/all')
def showall():
    """
    Implementation for service that takes a message (a string) as a POST and
    returns the SHA256 hash digest of that message (in hexadecimal format)


    Example:
    --------
    >>> curl http://vinayski.pythonanywhere.com/all/10

    Returns
    --------
    str: String
        SHA256 hash digest of that message (in hexadecimal format).
    """
    msglist = Message.query.limit(10).all()
    [print("{},{}".format(m.msg, m.digest)) for m in msglist]
    return "done"

@APP.route('/messages', methods=['POST'])
def digest():
    """
    Implementation for service that takes a message (a string) as a POST and
    returns the SHA256 hash digest of that message (in hexadecimal format)


    Example:
    --------
    >>> curl -X POST -H "Content-Type: application/json" -d '{"message": "foo12345678901234567"}' \
        http://vinayski.pythonanywhere.com/messages

    Returns
    --------
    str: String
        SHA256 hash digest of that message (in hexadecimal format).
    """
    msgtxt = request.json['message']
    strlen = len(msgtxt)
    if strlen > _BIGSTR:
        return "Upgrade your account to process big strings. Contact SKi@sankhe.com"
    else:
        msg = querymsg(msgtxt)
        if msg is None:
            msg = add(msgtxt)
            return msg.digest
        else:
            return msg.digest

if __name__ == "__main__":
    APP.debug = True
    #app.app_context().push()
    DB.create_all()
    APP.run()
