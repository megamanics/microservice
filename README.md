# microservice
example of a simple microservice using Flask that has two endpoints:

1. /messages takes a message (a string) as a POST and returns the SHA256 hash digest of that message (in hexadecimal format)
2. /messages/<hash> is a GET request that returns the original message. A request to a non-existent <hash> should return a 404 error.

#Test from curl
curl -X POST -H "Content-Type: application/json" -d '{"message": "foo12345678901234567"}' http://127.0.0.1:5000/messages

curl -X POST -H "Content-Type: application/json" -d '{"message": "foo"}'  http://127.0.0.1:5000/messages
{
 "digest": "2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae"
}

echo -n "foo" | shasum -a 256
2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae -


curl http://127.0.0.1:5000/messages/2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae
{
 "message": "foo"
}

$ curl -i http://mywebsite.com/messages/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
HTTP/1.0 404 NOT FOUND
Content-Type: application/json
Content-Length: 36
Server: Werkzeug/0.11.5 Python/3.5.1
Date: Wed, 31 Aug 2016 14:21:11 GMT
{
 "err_msg": "Message not found"
}

