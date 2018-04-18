from flask import *

app = Flask(__name__)

@app.route("/")
def main():
	print("got to main")
	return render_template('index.html')

@app.route('/post', methods=['GET', 'POST'])
def post(pic):
	### run ML shit here
	print("got to post")
	return render_template('post_result.html')



if __name__ == "__main__":
	app.run()
