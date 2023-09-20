from flask import Flask, jsonify, request
from markupsafe import escape

app = Flask(__name__)

## Creo la ruta vacia ruta principal la ruta base 
@app.route('/')
def index():     ## Funcion que no recibe nada y retorna Index
    return 'Index' 


@app.route('/ping')
def ping():       ## Si invoco /ping en la ruta base + \ping retorna pong
    return jsonify({"message":"pong"})    ## Funcion json clave mensaje


@app.route('/usuarios/<string:nombre>')     ## Cuando tenga la ruta base + / usuarios/ y una cadena algo_nombre
def usuario_by_name(nombre):                 ## la funcion recibe lo que esta a continuacion de usuarios
    return jsonify({"name": nombre}) ## y lo retorna 

@app.route('/usuarios/<int:id>')     ## Cuando tenga la ruta base + / usuarios/ y un entero
def usuario_by_id(id):                 ## la funcion recibe lo que esta a continuacion de usuarios
    return jsonify({"id": id})

@app.route('/<path:nombre>')
def no_hacer(nombre):
    return escape(nombre)

## Consulta de varios recursos
@app.route('/recurso', methods = ['GET'])
def get_recursos():
    return jsonify({"data":"lista de todos los los items de este recurso"})

## POST nuevo 'recurso'
@app.route('/recurso', methods = ['POST'])
# @app.post('/recurso') este seria otra forma de hacerlo pero Carlos recomienda el anterior
def post_reucrso():
    print(request.get_json())
    body = request.get_json()
    name = body["name"]
    modelo = body["modelo"]
    
    # Insertar en la BD
    return jsonify({"recurso":{
                    "name": name,
                    "modelo": modelo
                    }})


@app.route('/recurso/<int:id>', methods = ['GET'])
def get_recurso_by_id(id):
    # buscar en la BD un regiustro con ese id y lo retorna
    return jsonify({"recurso":{
        "name": "Nombre correspondiente a ese id",
        "modelo": "modelo corrspondiente a ese id"
    }})




## controla que el nombre del QUE LA APLICACION SE LANCE SI ES EJECUTADA DE ESTA FORMA CON python app.py
if __name__ == '__main__':
    ##  Suba directo los cambios   puerto 5000
    app.run(debug=True, port=5000)
