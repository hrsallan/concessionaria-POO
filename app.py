class Carro:
    """Classe que representa um carro com atributos como modelo, marca, ano, condição e quantidade disponível."""
    def __init__(self, modelo, marca, ano, condicao, quantidade):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.condicao = condicao
        self.quantidade = quantidade

    """Propriedade que verifica se o carro está disponível com base na quantidade."""
    @property
    def disponivel(self):
        return self.quantidade>0
    
    """Método que retorna uma representação em string do carro, incluindo seu status de disponibilidade."""
    def __str__(self):
        status = 'Disponível' if self.disponivel else 'Esgotado'
        return f'{self.modelo} ({self.marca}) - {self.ano} - {self.condicao} | Qtd: {self.quantidade} [{status}]'
    
class Concessionaria:
    """Classe que representa uma concessionária de carros, permitindo gerenciar um estoque de veículos."""
    def __init__(self):
        self.estoque = []
    
    def adicionar_carro(self, carro):
        """Adiciona um carro ao estoque da concessionária."""
        self.estoque.append(carro)
        print(f'Carro {carro.modelo} adicionado ao estoque.')

    def remover_carro(self, modelo):
        """Remove um carro do estoque da concessionária pelo modelo."""
        encontrado = any(carro.modelo == modelo for carro in self.estoque)
        if encontrado:
            self.estoque = [carro for carro in self.estoque if carro.modelo != modelo]
            print(f'Carro {modelo} removido do estoque.')
        else:
            print(f'Carro {modelo} não encontrado no estoque.')

    def atualizar_quantidade(self, modelo, nova_quantidade):
        """Atualiza a quantidade de um carro específico no estoque."""
        for carro in self.estoque:
            if carro.modelo == modelo:
                carro.quantidade = nova_quantidade
                break

    def listar_estoque(self):
        """Lista todos os carros disponíveis no estoque da concessionária."""
        for carro in self.estoque:
            print(carro)

# Exemplo de uso
concessionaria = Concessionaria()
    
c1 = Carro("Civic", "Honda", 2020, "Novo", 5)
c2 = Carro("Corolla", "Toyota", 2019, "Usado", 3)
c3 = Carro("Model S", "Tesla", 2021, "Novo", 0)

concessionaria.adicionar_carro(c1)
concessionaria.adicionar_carro(c2)
concessionaria.adicionar_carro(c3)

print("\nEstoque da Concessionária:")
concessionaria.listar_estoque()

concessionaria.remover_carro("Corolla")
concessionaria.remover_carro("Fusca")  # Testando carro inexistente

print("\nEstoque atualizado:")
concessionaria.listar_estoque()

concessionaria.atualizar_quantidade("Civic", 10)
print("\nApós atualizar quantidade do Civic:")
concessionaria.listar_estoque()