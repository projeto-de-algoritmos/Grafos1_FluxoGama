import networkx as nx
import matplotlib.pyplot as plt

class Grafo:
  def __init__(self):
    self.grafo = nx.DiGraph()
  def adicionaNos(self):
    for i in self.todasMaterias():
      self.grafo.add_node(i)
  def adicionaVertices(self):
    self.grafo.add_edges_from([("Cálculo 1", "Cálculo 2"), ("Cálculo 1", "Probabilidade e Estatística Aplicada à Engenharia") , ("Cálculo 1", "Projeto e Análisede Algoritmos"),
                          ("Algoritmos e Programação de Computadores", "Orientação a Objetos"), ("Algoritmos e Programação de Computadores", "Estruturas de Dados 1"),
                          ("Desenho Industrial Assistido por Computador", "Interação Humano Computador"),
                          ("Cálculo 2", "Métodos Numéricos para Engenharia"),
                          ("Introdução à Álgebra Linear", "Teoria de Eletrônica Digital 1"), ("Introdução à Álgebra Linear", "Prática de Eletrônica Digital 1"),
                          ("Engenharia Econônica", "Gestão da Produção e Qualidade"),
                          ("Teoria de Eletrônica Digital 1", "Fundamentos de Arquiteturas de Computadores"),
                          ("Orientação a Objetos", "Projeto Integrador de Engenharia 1"), ("Orientação a Objetos", "Paradigmas de Programação"), ("Orientação a Objetos", "Métodos de Desenvolvimento de Software"),
                          ("matemática Discreta 1", "Matemática Discreta 2"),
                          ("Gestão da Produção e Qualidade", "Qualidade de Software 1"),
                          ("Métodos de Desenvolvimento de Software", "Requisitos de Software"), ("Métodos de Desenvolvimento de Software", "Testes de Software"), ("Métodos de Desenvolvimento de Software", "Interação Humano Computador"),
                          ("Estrutura de Dados 1", "Compiladores 1"), ("Estrutura de Dados 1", "Estrutura de Dados 2"), ("Estrutura de Dados 1", "Projeto de Algoritmos"),
                          ("Fundamentos de Arquiteturas de Computadores", "Fundamentos de Sistemas Operacionais"), 
                          ("Matemática Discreta 2", "Sistemas de Banco de Dados 1"),
                          ("Projeto Integrador de Engenharia 1", "Projeto Integrador de Engenharia 2"),
                          ("Interação Humano Computador", "Qualidade de Software 1"),
                          ("Requisitos de Software", "Arquitetura e Desenho de Software"),
                          ("Sistemas de Banco de Dados 1", "Sistemas de Banco de Dados 2"),
                          ("Fundamentos de Sistemas Operacionais", "Fundamentos de Redes de Computadores"), ("Fundamentos de Sistemas Operacionais", "Fundamentos de Sistemas Embarcados"),
                          ("Compiladores 1", "Paradigmas de Programação"),
                          ("Estruturas de Dados 2", "Programação para Sistemas Paralelos e Distribuídos"),
                          ("Testes de Software", "Gerência de Configuração e Evolução de Software"), ("Testes de Software", "Técnicas de Programação em Plataformas Emergentes"),
                          ("Arquitetura e Desenho de Software", "Técnicas de Programação em Plataformas Emergentes"),
                          ("Fundamentos de Redes de Computadores", "Programação para Sistemas Paralelos e Distribuídos"),
                          ("Técnicas de Programação em Plataformas Emergentes", "Engenharia de Produto de Software"),
                          ("Engenharia de Produto de Software", "Projeto Integrador de Engenharia 2"),
                          ("Trabalho de Conclusão de Curso 1", "Trabalho de Conclusão de Curso 2")
                          ])
  def todasMaterias(self):
    return ["Cálculo 1","Cálculo 2","Métodos Numéricos para Engenharia","Probabilidade e Estatística Aplicada à Engenharia","Projeto e Análisede Algoritmos","Física 1","Algoritmos e Programação de Computadores","Desenho Industrial Assistido por Computador","Engenharia e Ambiente","Introdução à Engenharia","Física 1 Experimental","Introdução à Álgebra Linear","Engenharia Econômica","Humanidades e Cidadania","Teoria de Eletrônica Digital 1","Prática de Eletrônica Digital 1","Orientação a Objetos","Matemática Discreta 1","Gestão da Produção e Qualidade","Métodos de Desenvolvimento de Software","Estruturas de Dados 1","Fundamentos de Arquiteturas de Computadores","Matemática Discreta 2","Projeto Integrador de Engenharia 1","Interação Humano Computador","Requisitos de Software","Sistemas de Banco de Dados 1","Fundamentos de Sistemas Operacionais","Compiladores 1","Estruturas de Dados 2","Qualidade de Software 1","Testes de Software","Arquitetura e Desenho de Software","Fundamentos de Redes de Computadores","Sistemas de Banco de Dados 2","Projeto de algoritmos","Técnicas de Programação em Plataformas Emergentes","Paradigmas de Programação","Fundamentos de Sistemas Embarcados","Programação para Sistemas Paralelos e Distribuídos","Engenharia de Produto de Software","Gerência de Configuração e Evolução de Software","Estágio Supervisionado","Trabalho de Conclusão de Curso 1","Projeto Integrador de Engenharia 2","Trabalho de Conclusão de Curso 2"]
  def achaFluxo(self, materia):
    roots = []
    leaves = []
    caminho = []
    caminhos = []
    for node in self.grafo.nodes :
      if self.grafo.in_degree(node) == 0 :
        roots.append(node)
      elif self.grafo.out_degree(node) == 0 :
        leaves.append(node)

    for root in roots :
      for leaf in leaves :
        for path in nx.all_simple_paths(self.grafo, root, leaf) :
            if materia in path:
                caminho = path
                caminhos.append(caminho)

    G = nx.DiGraph()
    for i in range(len(caminhos)):
      for j in range(len(caminhos[i]) - 1):
        G.add_edge(caminhos[i][j].replace(" ", "\n"), caminhos[i][j+1].replace(" ", "\n"))
    return G, caminhos