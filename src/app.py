from flask import Flask ,jsonify ,request
# del modulo flask importar la clase Flask y los métodos jsonify,request
from flask_cors import CORS       # del modulo flask_cors importar CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
app=Flask(__name__)  # crear el objeto app de la clase Flask
CORS(app) #modulo cors es para que me permita acceder desde el frontend al backend
# configuro la base de datos, con el nombre el usuario y la clave
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost/administracion'
# URI de la BBDD                      driver de la BD  user:clave@URL/nombreBBDD
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False #none
db= SQLAlchemy(app)
ma=Marshmallow(app)
 
# defino la tabla Cliente
class Cliente(db.Model):   # la clase Producto hereda de db.Model     
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    codigo=db.Column(db.String(100))
    apellidoNombre=db.Column(db.String(100))
    iva=db.Column(db.String(100))
    telefono=db.Column(db.String(100))
    def __init__(self,codigo,apellidoNombre,iva,telefono):   #crea el  constructor de la clase
        self.codigo=codigo   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.apellidoNombre=apellidoNombre
        self.iva=iva
        self.telefono=telefono
 
 
 
with app.app_context():
    db.create_all()  # crea las tablas
#  ************************************************************
class ClienteSchema(ma.Schema):
    class Meta:
        fields=('id', 'codigo','apellidoNombre','iva','telefono')
cliente_schema=ClienteSchema()            # para crear un producto
clientes_schema=ClienteSchema(many=True)  # multiples registros
 
# crea los endpoint o rutas (json)
@app.route('/clientes',methods=['GET'])
def get_Clientes():
    all_clientes=Cliente.query.all()     # query.all() lo hereda de db.Model
    result=clientes_schema.dump(all_clientes)  # .dump() lo hereda de ma.schema
    return jsonify(result)
 
@app.route('/clientes/<id>',methods=['GET'])
def get_cliente(id):
    cliente=Cliente.query.get(id)
    return cliente_schema.jsonify(cliente)

@app.route('/clientes/<id>',methods=['DELETE'])
def delete_cliente(id):
    cliente=Cliente.query.get(id)
    db.session.delete(cliente)
    db.session.commit()
    return cliente_schema.jsonify(cliente)

@app.route('/clientes', methods=['POST']) # crea ruta o endpoint
def create_cliente():
    print(request.json)  # request.json contiene el json que envio el cliente
    codigo=request.json['codigo']
    apellidoNombre=request.json['apellidoNombre']
    iva=request.json['iva']
    telefono=request.json['telefono']
    new_cliente=Cliente(codigo,apellidoNombre,iva,telefono)
    db.session.add(new_cliente)
    db.session.commit()
    return cliente_schema.jsonify(new_cliente)

@app.route('/clientes/<id>' ,methods=['PUT'])
def update_cliente(id):
    cliente=Cliente.query.get(id)
   
    codigo=request.json['codigo']
    apellidoNombre=request.json['apellidoNombre']
    iva=request.json['iva']
    telefono=request.json['telefono']
 
    cliente.codigo=codigo
    cliente.apellidoNombre=apellidoNombre
    cliente.iva=iva
    cliente.telefono=telefono
    db.session.commit()
    return cliente_schema.jsonify(cliente)

 
# programa principal *******************************
if __name__=='__main__':  
    app.run(debug=True, port=5000)  
