from flask import Flask, render_template, send_file, request, url_for, redirect, session
import networkx as nx
from io import BytesIO
import matplotlib.pyplot as plt
import grafo as grafoModulo

app = Flask(__name__)
app.secret_key = "PROJETO DE ALGORITMOS"

@app.route('/', methods=["POST", "GET"])
def inicial():
  if request.method == "POST":
    session["materia"] = request.form["materia_texto"]
    return redirect(url_for("ind"))
  else:
    return render_template("inicial.html")

@app.route('/grafo_info')
def ind():
  return render_template("image.html", caminhos = session["caminhos"], materia = session["materia"])

@app.route('/grafo_img')
def pagina():
  G = grafoModulo.Grafo()
  G.adicionaNos()
  G.adicionaVertices()
  novoGrafo = nx.DiGraph()
  novoGrafo, session["caminhos"] = G.achaFluxo(session["materia"])
  plt.figure(figsize=(10,7))
  nx.draw_spectral(novoGrafo, with_labels=True, node_shape="s", arrows = True,arrowstyle = 'fancy',arrowsize=10, node_color="none", bbox=dict(facecolor="skyblue", edgecolor='black', boxstyle='round,pad=0.2'), width = 2, node_size = 3000)
  img = BytesIO()
  plt.savefig(img)
  plt.clf()
  img.seek(0)
  plt.clf()

  return send_file(img, mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True)