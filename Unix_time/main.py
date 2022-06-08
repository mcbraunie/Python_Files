import os
import time


from flask import Flask

app = Flask(__name__)

# Unix date example: 1557783982

@app.route('/')
def get_unixtime():
	''' Returns today's date in Unix Time (number of seconds since January 1, 1970'''
	t = str(time.time())

	return t


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)