from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    
    return render_template('index.html')


@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/log')
def log():
    return render_template('iniciar_sesion.html')

@app.route('/dest')
def provincias():
    
    return render_template('destination.html')

@app.route('/book')
def hoteles():

    return render_template('booking.html')

@app.route('/vacaciones/<string:provincia>')
def hoteles2(provincia):

    return render_template('booking.html', provincia=provincia)

@app.route('/vacaciones/<string:provincia>/<string:hotel>')
def habitaciones(hotel):
    
    return render_template('habitaciones.html', hotel=hotel)

@app.route('/vacaciones/<string:provincia>/<string:hotel>/<string:habitacion>')
def reservar2(habitacion):
    
    return render_template('reservar2.html', habitacion=habitacion)

@app.route('/reservas')
def reservas():
    
    return render_template('reservas_act.html')

@app.route('/reservas/<string:reserva>/editar_reserva')
def editar_reserva(reserva):
    
    return render_template('reservar.html', reserva=reserva)

@app.route('/reservas/<string:reserva>/cancelar_reserva')
def cancelar_reserva(reserva):
    
    return render_template('cancelar_reserva.html', reserva=reserva)

@app.route('/us')
def nosotros():
    
    return render_template('about.html')

@app.route('/contacto')
def contacto():
    
    return render_template('contact.html')

@app.route('/reservar')
def reservar_hotel():

    return render_template('reservar.html')

@app.route('/editar')
def reservar_editar():

    return render_template('editar_reserva.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/package')
def package():
    return render_template('package.html')

if __name__=='__main__':
    app.run(debug=True)
