from flask import Flask,  render_template

app = Flask(__name__)





@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/booking")
def booking():
    return render_template('booking.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/destination")
def dest():
    return render_template('destination.html')

@app.route("/package")
def pack():
    return render_template('package.html')

@app.route("/service")
def service():
    return render_template('service.html')

@app.route("/team")
def team():
    return render_template('team.html')

@app.route("/testimonial")
def testimonial():
    return render_template('testimonial.html')

@app.route("/reservas")
def reservas():
    return render_template('reservas_act.html')

if __name__=='__main__':
    app.run(debug=True)