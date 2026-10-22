class Conta:
    def __init__(self, numero: str):
        self.numero = numero
        self.saldo = 0.0  # Saldo inicial igual a zero


class BancoService:
    def __init__(self):
        self.contas = {}  # Armazena as contas em memória (sem BD)

    def cadastrar_conta(self, numero: str) -> bool:
        if numero in self.contas:
            return False  # Conta já existe
        self.contas[numero] = Conta(numero)
        return True