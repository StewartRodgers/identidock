from flask import Flask, Response
import requests
app = Flask(__name__)
default_name = 'Stewart Rodgers'

@app.route('/')
def get_identicon():
	name = default_name
	header = '<html><head><title>Identidock</title></head><body>'
	footer = '</body></html>'
	body = '''<form method="POST">
			Hello <input type="text" name="name" value="{}">
			<input type="submit" value="submit">
			</form>
			<p>You look like a:
			<img src="/monster/monster.png"/>'''.format(name)
	return header + body + footer
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')