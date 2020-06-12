from flask import Flask, render_template

def create_app():
	app = Flask(__name__)
	@app.route("/")
	def index():
		return render_template("index.html")
	@app.route("/new")
	def new():
		return render_template("whatsnew.html")
	@app.route("/productfocus")
	def productfocus():
		return render_template("productfocus.html")
	@app.route("/distributors")
	def distributors():
		return render_template("distributors.html")
	@app.route("/distributors/africa")
	def africa():
		return render_template("distributors.html")
	@app.route("/distributors/asia")
	def asia():
		return render_template("distributors.html")
	@app.route("/distributors/europe")
	def europe():
		return render_template("distributors.html")
	@app.route("/distributors/southamerica")
	def southamerica():
		return render_template("distributors.html")
	@app.route("/distributors/northamerica")
	def northamerica():
		return render_template("distributors.html")
	return app
