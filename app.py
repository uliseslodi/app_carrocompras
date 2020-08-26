# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField
from wtforms.validators import DataRequired, NumberRange
from flask_wtf.csrf import CSRFProtect

### TODO: implementar aquí el modelo para el formulario: FormularioCompra

class FormularioCompra(FlaskForm):
    nombre = StringField('nombre', validators=[DataRequired()])
    cantidad = IntegerField('cantidad', validators=[DataRequired(), NumberRange(min=0, max=20)])

app = Flask("myapp")
csrf = CSRFProtect(app)
app.config['SECRET_KEY'] = "aprobado"

compras = []

@app.route("/")
def lista():

    ### TODO: implementar aquí los cambios que se crean necesarios

    return render_template("lista.html", productos = compras) 

@app.route("/agregar", methods=["GET", "POST"])
def agregar():
    form = FormularioCompra()
    if form.validate_on_submit():

        ### TODO:   obtener los datos del formulario (nombre y cantidad)
        ###         y colóquelos en un diccionario llamado "producto"
        ###         que será luego agregado al arreglo de compras

        producto = {
            'nombre': form.nombre.data,
            'cantidad': form.cantidad.data,
        }
        
        compras.append(producto)

        ## TODO: redireccionar al endpoint "/"
        return redirect("/")
    
    else:
        return render_template("agregar.html", form=form)


### TODO: implementar aquí el endpoint "/nosotros"
@app.route("/nosotros")
def nosotros():
    return render_template("nosotros.html")


app.run()