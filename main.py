class Candidato:
    def __init__(self, nome, habilidades):
        self._nome = nome
        self._habilidades = set(habilidades)
        self._vagas_compativeis = []
    
    def getNome(self):
        return self._nome
    
    def setNome(self, nome):
        self._nome = nome
    
    def getHabilidades(self):
        return self._habilidades
    
    def setHabilidades(self, habilidades):
        self._habilidades = set(habilidades)
    
    def getVagasCompativeis(self):
        return self._vagas_compativeis
    
    def setVagasCompativeis(self, vagas):
        self._vagas_compativeis = vagas

class Vaga:
    def __init__(self, titulo, requisitos, empresa):
        self._titulo = titulo
        self._requisitos = set(requisitos)
        self._empresa = empresa
        self._candidatos_compativeis = []
    
    def getTitulo(self):
        return self._titulo
    
    def setTitulo(self, titulo):
        self._titulo = titulo
    
    def getRequisitos(self):
        return self._requisitos
    
    def setRequisitos(self, requisitos):
        self._requisitos = set(requisitos)
    
    def getEmpresa(self):
        return self._empresa
    
    def setEmpresa(self, empresa):
        self._empresa = empresa
    
    def getCandidatosCompativeis(self):
        return self._candidatos_compativeis
    
    def setCandidatosCompativeis(self, candidatos):
        self._candidatos_compativeis = candidatos

class SistemaTalentos:
    def __init__(self):
        self._candidatos = []
        self._vagas = []
    
    def adicionar_candidato(self, nome, habilidades):
        candidato = Candidato(nome, habilidades)
        self._candidatos.append(candidato)
        self._atualizar_compatibilidades(candidato)
        return candidato
    
    def adicionar_vaga(self, titulo, requisitos, empresa):
        vaga = Vaga(titulo, requisitos, empresa)
        self._vagas.append(vaga)
        self._atualizar_compatibilidades(vaga)
        return vaga
    
    def _atualizar_compatibilidades(self, novo_item):
        if isinstance(novo_item, Candidato):
            for vaga in self._vagas:
                if self._verificar_compatibilidade(novo_item.getHabilidades(), vaga.getRequisitos()):
                    novo_item.getVagasCompativeis().append(vaga)
                    vaga.getCandidatosCompativeis().append(novo_item)
        else:
            for candidato in self._candidatos:
                if self._verificar_compatibilidade(candidato.getHabilidades(), novo_item.getRequisitos()):
                    candidato.getVagasCompativeis().append(novo_item)
                    novo_item.getCandidatosCompativeis().append(candidato)
    
    def _verificar_compatibilidade(self, habilidades, requisitos):
        return requisitos.issubset(habilidades)
    
    def buscar_vagas_para_candidato(self, nome_candidato):
        for candidato in self._candidatos:
            if candidato.getNome() == nome_candidato:
                return [(vaga.getTitulo(), vaga.getEmpresa()) for vaga in candidato.getVagasCompativeis()]
        return []
    
    def buscar_candidatos_para_vaga(self, titulo_vaga, empresa):
        for vaga in self._vagas:
            if vaga.getTitulo() == titulo_vaga and vaga.getEmpresa() == empresa:
                return [candidato.getNome() for candidato in vaga.getCandidatosCompativeis()]
        return []

def executar_testes():
    sistema = SistemaTalentos()
    
    candidato1 = sistema.adicionar_candidato("Ana", ["Python", "SQL"])
    vaga1 = sistema.adicionar_vaga("Analista de Dados", ["Python", "SQL"], "TechCorp")
    assert len(candidato1.getVagasCompativeis()) == 1
    
    vaga2 = sistema.adicionar_vaga("Dev Frontend", ["JavaScript", "React"], "WebCo")
    assert len(candidato1.getVagasCompativeis()) == 1
    
    candidato2 = sistema.adicionar_candidato("Bruno", ["Python", "SQL", "JavaScript", "React"])
    assert len(candidato2.getVagasCompativeis()) == 2
    
    vagas = sistema.buscar_vagas_para_candidato("Ana")
    assert len(vagas) == 1 and vagas[0][0] == "Analista de Dados"
    
    candidatos = sistema.buscar_candidatos_para_vaga("Dev Frontend", "WebCo")
    assert len(candidatos) == 1 and candidatos[0] == "Bruno"
    
    print("Todos os testes passaram!")

if __name__ == "__main__":
    executar_testes()