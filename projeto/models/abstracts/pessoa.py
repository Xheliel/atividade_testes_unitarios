from abc import ABC
from models.endereco import Endereco
from projeto.models.enums.unidade_federal import Uf

class Pessoa(ABC, Endereco):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, logradouro: str, numero: int, complemento: str, cep: str, cidade: str, uf: Uf) -> None:
        super().__init__(logradouro, numero, complemento, cep, cidade, uf)
        self.id = self._id_verificado(id)
        self.nome = self._nome_verificado(nome)
        self.telefone = self._telefone_verificado(telefone)
        self.email = self._email_verificado(email)
        self.endereco = self._endereco_verificado(endereco)

    def __str__(self) -> str:
        return super().__str__()