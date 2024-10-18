from flask import (Flask, render_template, request) # Importa o flask

app = Flask(__name__) # cria uma instância

@app.route("/",methods=('GET',)) # Assina uma rota
def index(): # função responsável pela página
    nome = request.args.get('nome') #use o seu nome
    return f""" "<h1> Página Inicial</h1><p>fellipe</p>
    <p>Olá {nome}, que nome bonito!
    """

@app.route("/galeria", methods=('GET',))
def outra():
    return "<h1>galeria</h1>"

@app.route("/contato", methods=('GET',))
def outra1():
    return "<h1>contato</h1>"

@app.route("/sobre", methods=('GET',))
def outra2():
    return "<h1>sobre</h1>"

@app.route("/area")
def area():
    altura= float (request.args.get('a'))
    largura= float (request.args.get('l'))
    return  f"""<h1> A área informada > L={largura}* A={altura} =) Area= {largura*altura}</h1>"""

@app.route("/par_ou_impar", methods=('GET',))
def par_ou_impar():
  numero = float(request.args.get('n'))
  if numero % 2 == 0:
    return f"O número {numero} é par."
  else:
    return f"O número {numero} é ímpar."
  
@app.route("/sobrenome", methods=('GET',))
def nomesobrenome():
  nome = request.args.get('nome')
  sobrenome = request.args.get('sobrenome')
  return f"""<h1> sobrenome </h1>
  <p>{sobrenome},{nome}</p>"""

@app.route("/tabuada/<int:numero>", methods=("GET",))
def tabuada(numero):
   
   return "render_template"('tabuada.html', numero=numero)