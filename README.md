## Simple Examples in python 3.6:

### Installation

```bash
pip install -r requirements.txt
```

### Microservice 

Example of a simple microservice using Flask that has two endpoints:

1. /messages takes a message (a string) as a POST and returns the SHA256 hash digest of that message (in hexadecimal format)
2. /messages/<hash> is a GET request that returns the original message. A request to a non-existent <hash> should return a 404 error.

```bash
echo -n "foo" | shasum -a 256
2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae -
```

### Start Server
```bash
python flask_app.py
```

### Test from curl

Test service hosted on localhost via:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"message": "foo"}'  http://127.0.0.1:5000/messages
{
 "digest": "2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae"
}

curl http://127.0.0.1:5000/messages/2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae
{
 "message": "foo"
}
```

Test service hosted on vinayski.pythonanywhere.com via:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"message": "foo12345678901234567"}' http://vinayski.pythonanywhere.com/messages

curl -X POST -H "Content-Type: application/json" -d '{"message": "foo"}'  http://vinayski.pythonanywhere.com/messages
{
 "digest": "2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae"
}

curl -i http://vinayski.pythonanywhere.com/messages/bb4eca334f61af3b67b5d528907d30285151610200539302f4c8cabe66225b5323
HTTP/1.1 404 NOT FOUND
Server: openresty/1.9.15.1
Date: Wed, 02 Aug 2017 00:06:36 GMT
Content-Type: application/json
Content-Length: 37
Connection: keep-alive

{
  "err_msg": "Message not found"
}
```

### Example of a command line argument parser using Fire.

```bash
python replacex.py  -- --help
```

### Example of a search algorithm

```bash
python find_pair.py -- --help
```
