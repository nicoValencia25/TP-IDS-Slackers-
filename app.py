from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    
    return render_template('index.html')

@app.route('/vacaciones')
def provincias():
    
    return render_template('provincias.html')

@app.route('/vacaciones/<string:provincia>')
def hoteles(provincia):

    return render_template('hoteles.html', provincia=provincia)

@app.route('vacaciones/<string:provincia>/<string:hotel>')
def habitaciones(hotel):
    
    return render_template('habitaciones.html', hotel=hotel)

@app.route('vacaciones/<string:provincia>/<string:hotel>/<string:habitacion>')
def reservar(habitacion):
    
    return render_template('reservar.html', habitacion=habitacion)

@app.route('reservas')
def reservas():
    
    return render_template('reservas.html')

@app.route('reservas/<string:reserva>/editar_reserva')
def editar_reserva(reserva):
    
    return render_template('editar_reserva.html', reserva=reserva)

@app.route('reservas/<string:reserva>/cancelar_reserva')
def cancelar_reserva(reserva):
    
    return render_template('cancelar_reserva.html', reserva=reserva)

@app.route('sobre_nosotros')
def sobre_nosotros():
    
    return render_template('sobre_nosotros.html')

@app.route('contacto')
def contacto():
    
    return render_template('contacto.html')

if __name__=='__main__':
    app.run(debug=True)
