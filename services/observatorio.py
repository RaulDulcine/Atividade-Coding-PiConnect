"""Modulo para criar a classe Observatório"""

from models.ProjetoIntegrador import ProjetoIntegrador


class Observatorio:
    """Classe para criar o Observatorio."""
    def __init__(self):
        self.projetos = []

    def adicionar_projeto(self, titulo, curso, periodo, descricao):
        """Função para Adicionar Projeto."""
        if titulo == "" or curso == "":
            return "Erro: Título e Curso são obrigatórios."

        novo_projeto = ProjetoIntegrador(titulo, curso, periodo, descricao)
        self.projetos.append(novo_projeto)
        return f"Projeto '{titulo}' adicionado."

    def listar_projetos(self):
        """Função para Listar Projeto."""
        return [p.to_dict() for p in self.projetos]

    def buscar_projeto(self, titulo):
        """Função para buscar projeto."""
        for projeto in self.projetos:
            if projeto.titulo.lower() == titulo.lower():
                return projeto
        return None

    def filtrar_por_curso(self, curso):
        """Função para filtrar por curso."""
        lista_filtrada = []
        for projeto in self.projetos:
            if projeto.curso.lower() == curso.lower():
                lista_filtrada.append(projeto)
        return lista_filtrada