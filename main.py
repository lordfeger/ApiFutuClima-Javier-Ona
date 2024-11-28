from flask import Flask, render_template, request
import requests
from jinja2 import Environment

app = Flask(__name__)

# funcion de  integracion de claves para el api 
def get_weather_data(city:str):

    API_KEY = 'a3d8460614b578049bfc3bf8f056bfc6'
    idioma='es'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang={idioma}&appid={API_KEY}'
    r =requests.get(url).json()
    #print(r) # para  verificar el Json 
    return r



@app.route('/',methods=['GET','POST'])#decorador, crear la ruta, la ubica, 
def index():
    if request.method=='GET':
        return render_template('index.html', ciudad='', humedad='',presion='', descripcion='', icon = '',cod = '', lat='', lon='', country='',temperatura='', temperatura_min='', temperatura_max='', velocidad_viento='' )
    ciudad= request.form.get('txtCiudad')
    if ciudad:
        data=get_weather_data(ciudad)
        cod=data.get('cod')
        if cod != 200:
            return render_template('index.html', ciudad='', humedad='',presion='', descripcion='', icon = '',cod = '', lat='', lon='', country='',temperatura='', temperatura_min='', temperatura_max='', velocidad_viento='' )
        humedad=data.get('main').get('humidity')
        presion=data.get('main').get('pressure')
        descripcion=data.get('weather')[0].get('description')
        icon=data.get('weather')[0].get('icon')
        lat=data.get('coord').get('lat')
        lon=data.get('coord').get('lon')
        country=data.get('sys').get('country')
        temperatura=data.get('main').get('temp')
        temperatura_min=data.get('main').get('temp_min')
        temperatura_max=data.get('main').get('temp_max')
        velocidad_viento=data.get('wind').get('speed')
        
        return render_template('index.html',
                               country=country, 
                               ciudad=ciudad.upper(),
                               humedad=humedad,
                               presion=presion, 
                               descripcion=descripcion.capitalize(), 
                               icon = icon , 
                               cod = cod, 
                               lat=lat, 
                               lon=lon,
                               temperatura=temperatura,
                               temperatura_max=temperatura_max,
                               temperatura_min=temperatura_min,
                               velocidad_viento=velocidad_viento
                               )
    else:
        return render_template('index.html', ciudad='', humedad='',presion='', descripcion='', icon = '',cod = '', lat='', lon='', country='',temperatura='', temperatura_min='', temperatura_max='', velocidad_viento='' )


#  ruta para la hoja de vida
@app.route('/javier_ona_curriculum.html')
def javier_ona_curriculum():
    return render_template('javier_ona_curriculum.html')



# bloque de protección de entrada principal
if __name__=="__main__":
    app.run(debug=True)
    