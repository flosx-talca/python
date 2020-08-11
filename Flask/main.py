from flask import Flask, redirect, url_for, render_template #obligatorio
app = Flask(__name__) #nombre de la aplicacion


@app.route("/") #directorio raiz "Flask"
def index():    #primera funcion probar cambiar nombre
        return redirect(url_for("home")) # para rederigir url al home

@app.route("/home") 
def home():    
        texto = "Esta es una prueba de <strong>parametro</strong>"
        #return "Hola este es el home"
        return render_template('home.html', texto_var= texto)  

@app.route("/nosotros")
def nosotros():
        #return  "Acerca de nosotros"
        return render_template('nosotros.html')


@app.route("/servicios")
def servicios():
        #return  "Los servicios"
        return render_template("servicios.html")


@app.route("/servicios/detalle/<slug>")
def servicios_detalle(slug):
        #return  f"Detalle del servicio <strong>{slug} </strong> " 
        return render_template('servicios-detalle.html', slug=slug)


@app.route("/servicios/detalle-dos/<int:id1>")
@app.route("/servicios/detalle-dos/<int:id1>/<id2>")
def servicios_detalle_dos(id1, id2=None):
        return  f"Detalle del servicio id1: <strong>{id1} </strong> id2: <strong>{id2} </strong> " 



@app.route("/contactos/<parametro>")
def contactos(parametro):
        return render_template('contactos.html', parametro=parametro)

if __name__ == "__main__": #obligatorio
        app.run(debug=True) #modo debug para ambiente en desarrollo
