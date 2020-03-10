from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename #la idea es verificar el nombre del archivo y si pudiera ser perjudicial pues lo cambiaria (archivo que se parezca a ruta relativao ,cambia /)
from flask_sqlalchemy import SQLAlchemy
import os #para la ruta

UPLOAD_FOLDER = os.path.abspath("./uploads/") #donde se van a guardar los ficheros (pasa a ser la ruta usada)
ALLOWED_EXTENSIONS = set(["png","jpg","jpge","gif","txt"]) #Formatos permitidos de archivo

def allowed_file(filename): #funcion que nos permita validar la extension del archivo
	return "." in filename and filename.rsplit(".", 1)[1] in ALLOWED_EXTENSIONS #split te divide la cadena, hemos especificado que por el punto, y el [1] te coge lo de la derecha del . , en este caso la extension 

app = Flask(__name__) #Importamos flask y creamos la app
app.config["UPLOAD_FOLDER"]= UPLOAD_FOLDER #Almacenamos en el diccionario de claves, una para la ruta absoluta donde queremos que se suban los archivos
app.config["SQLALCHEMY_DATABASE_URI"]= 'sqlite:///site.db' #la ruta relativa de la base de datos?

db = SQLAlchemy(app) #creamos la instancia de la bd

class Foto (db.Model):
	id = db.Column(db.Integer, primary_key =True)
	image_name = db.Column(db.String(20), unique=True, nullable=False) #nullable es que no puede estar vacio
	image_file = db.Column(db.String(20), unique=True, nullable=False)
	descripcion = db.Column(db.String(200), unique=False, nullable=False) #Descripcion de la imagen (hay que añadirlo)
	datos = db.relationship('Datos', backref='nombrefoto', lazy=True) #backref es como añadir otro campo a Datos para saber de que foto son esos datos. 
	
	def __repr__(self):
		return f"Foto('{self.image_name}','{self.image_file})"
		
class Datos (db.Model):
	id = db.Column(db.Integer, primary_key =True)
	tp = db.Column(db.String(20), unique=False, nullable=False)
	Tg = db.Column(db.String(20), unique=False, nullable=False)
	cpx = db.Column(db.String(20), unique=False, nullable=False)
	cpy = db.Column(db.String(20), unique=False, nullable=False)
	varianza = db.Column(db.String(20), unique=False, nullable=False)
	estimacion = db.Column(db.String(20), unique=False, nullable=False)
	foto_id = db.Column(db.Integer, db.ForeignKey('foto.id'), nullable=False)
	

@app.route("/")
@app.route("/index")
def hello():
	return render_template('index.html')
	
@app.route("/upload", methods=["GET","POST"]) 
def upload(): 
	if request.method == "POST":
		if "ourfile" not in request.files:	#tiene que ver con no tener bien lo del enctype
			return "The form has no file part"
		f= request.files["ourfile"] #recuperar el archivo
		if f.filename == "": #Si no seleccionamos archivo que de error
			return "No se ha seleccionado ningun archivo"
		if f and allowed_file(f.filename): #si existe f y tiene una extension permitida que se guarde
			#si es una foto hacer algo y si es un txt hacer otra.
			if f.filename == "txt": #si son los datos
			#Tienes que ir a la base de datos para ver si el nombre de la imagen esta y cogerle. Si esta vincularlos añadiendo a la base de datos los datos. Si no esta? (Devolver error y mensaje de que no hay foto)
			#abrir archivo - open
			#ultima linea
			#coger lo que va despues de imagen: - expresion regular
			
			#l="imagen: portero.jpg"
			#l.split("imagen: ")[1]
			
			#if Foto.query.filter_by(image_file='nombre imagen').all()
			#si existe (no es lista vacia que trabaje con ello y sino pues error)
			#Si trabaja con ello que cree la instancia de Datos con los valores del fichero.
			
			#else: #si es una imagen
				#pedirle la descripcion - flask input pero tras subirlo? como?
				#COMPROBAR QUE NO HAY 2 imagenes con el mismo nombre (en la base de datos) (Requisito) (igual que cuando compruebas el txt)
								
				#Copio el nombre en la base de datos y subo la imagen al directorio (como ya estoy haciendo)
				#Entrar en la carpeta uploads y coger el nombre del archivo (que tiene el nombre y el nombre del archivo con extension)
			
			
			filename = secure_filename(f.filename) #recuperar el nombre del archivo y si lo tiene que cambiar lo cambia
			f.save(os.path.join(app.config["UPLOAD_FOLDER"], filename)) #guardar el archivo en la ruta que hemos indicado
			return redirect(url_for("get_file", filename=filename))
		return "Archivo no Permitido"
	return"""
<form method="POST" enctype="multipart/form-data"> 			
<input type="file" name="ourfile">
<input type="submit" value="UPLOAD">
</form>	
"""
#enctype para que no dara error

@app.route("/uploads/<filename>")
def get_file (filename):
	return send_from_directory(app.config["UPLOAD_FOLDER"], filename)
	
@app.route("/about")
def about():
	return render_template('about.html')
	
if __name__ == '__main__': #para ejecutarlo como en python (que se actualice al instante y que no haya que parar y arrancar de nuevo)
	app.run(debug=True)