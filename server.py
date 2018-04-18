from flask import *

app = Flask(__name__)

@app.route("/")
def main():
	print("got to main")
	return render_template('index.html')

# @app.route('/post', methods=['GET', 'POST'])
# def post(pic):
# 	### run ML shit here
# 	print("got to post")
# 	return render_template('post_result.html')



if __name__ == "__main__":
	app.run(debug=True)



# from flask import Flask, render_template, request
# from werkzeug import secure_filename
# app = Flask(__name__)

# @app.route('/upload')
# def upload_file():
#    return render_template('upload.html')
	
# @app.route('/uploader', methods = ['GET', 'POST'])
# def upload_file():
#    if request.method == 'POST':
#       f = request.files['file']
#       f.save(secure_filename(f.filename))
#       return 'file uploaded successfully'
		
# if __name__ == '__main__':
#    app.run(debug = True)