from models.enums.unidade_federal import Uf

class Endereco:
    def __init__(self, logradouro: str, numero: int, complemento: str, cep: str, cidade: str, uf: Uf ) -> None:
        self.logradouro = self._logradouro_verificado(logradouro)
        self.numero = self._numero_verificado(numero)
        self.complemento = self._complemento_verificado(complemento)
        self.cep = self._cep_verificado(cep)
        self.cidade = self._cidade.verificado(cidade)
        self.uf = uf

    def __str__(self) -> str:
        return (
            f"\nEndereço\n"
            f"\nlogradouro: {self.logradouro}"
            f"\nnúmero: {self.numero}"
            f"\ncomplemento: {self.complemento}"
            f"\ncep: {self.cep}"
            f"\ncidade: {self.cidade}"
            f"\nuf: {self.uf}"
            f"\n"
        )

    # VERIFICANDO LOGRADOURO

    def _logradouro_verificado(self, logradouro):
        self._verificar_logradouro_vazio(logradouro)
        self._verificar_logradouro_tipo_invalido(logradouro)


    def _verificar_logradouro_tipo_invalido(self, logradouro):
        if not isinstance(logradouro, str):
            raise TypeError(" Utilize somente letras.")

    def _verificar_logradouro_vazio(self, logradouro):
        if not logradouro.strip():
            raise TypeError(" Preencha o logradouro.")
        
    # VERIFICANDO NÚMERO

    def _numero_verificado(self, numero):
        self._verificar_numero_vazio(numero)
        self._verificar_numeroo_tipo_invalido(numero)
        self._verificar_numero_negativa(numero)

    def _verificar_numero_tipo_invalido(self, numero):
        if not isinstance(numero, int):
            raise TypeError(" Use apenas números.")

    def _verificar_numero_vazio(self, numero):
        if not numero.strip():
            raise TypeError(" Preencha o número.")
        
    def _verificar_numero_negativa(self, numero):
        if numero <= 0:
            raise ValueError(" O número não pode ser negativo.")
        
    # VERIFICAR COMPLEMENTO

    def _complemento_verificado(self, complemento):
        self._verificar_complemento_vazio(complemento)
        self._verificar_complemento_tipo_invalido(complemento)


    def _verificar_complemento_tipo_invalido(self, complemento):
        if not isinstance(complemento, str):
            raise TypeError(" Utilize somente letras.")

    def _verificar_complemento_vazio(self, complemento):
        if not complemento.strip():
            raise TypeError(" Preencha o complemento.")
        
    # VERIFICAR CEP

    def _cep_verificado(self, cep):
        self._verificar_cep_vazio(cep)
    
    def _verificar_cep_vazio(self, cep):
        if not cep.strip():
            raise TypeError(" Preencha o cep.")
        
    # VERIFICAR CIDADE

    def _cidade_verificado(self, cidade):
        self._verificar_cidade_vazio(cidade)
        self.__verificar_cidade_tipo_invalido(cidade)

    def _verificar_cidade_vazia(self, cidade):
        if not cidade.strip():
            raise TypeError(" Preencha o nome da cidade.")
        
    def _verificar_cidade_tipo_invalido(self, cidade):
        if not isinstance(cidade, str):
            raise TypeError(" Utilize somente letras.")


