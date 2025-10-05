from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home_page():
    return render_template('home.html')
@app.route('/melting')
def about_page():
    return render_template("melting.html",about_page="/melting.html")
@app.route('/melting2')
def melt_page():
    return render_template('melting2.html',melt_page="/melting2.html")
@app.route('/air')
def air_page():
    return render_template('air.html',air_page="/air.html")
@app.route('/air2')
def air2_page():
    return render_template('air2.html',air2_page="/air2.html")
@app.route('/cropland')
def cropland_page():
    return render_template('cropland.html',cropland_page="/cropland.html")
@app.route('/cropland2')
def cropland2_page():
    return render_template('cropland2.html',cropland_page="/cropland2.html")
@app.route('/why')
def why_page():
    return render_template('why.html',why_page="/why.html")



if __name__ == "__main__":
    app.run(debug=True)
