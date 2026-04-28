class ProjetoIntegrador:
    def __init__(self, titulo, curso, periodo, descricao):
        self.titulo = titulo
        self.curso = curso
        self.periodo = periodo
        self._descricao = descricao

    def alterar_descricao(self, nova_descricao):
        """Função para alterar a descrição."""
        self._descricao = nova_descricao
        return "Descrição atualizada com sucesso."

    def to_dict(self):
        """Função de dicionário."""
        return {
            "titulo": self.titulo,
            "curso": self.curso,
            "periodo": self.periodo,
            "descricao": self._descricao
        }

    def mostrar_dados(self):
        """Função pra mostrar os dados"""
        print(f"Projeto: {self.titulo} | Descrição: {self._descricao} | Curso: {self.curso} | Período: {self.periodo}")
