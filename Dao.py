from Model import *

class DaoCategoria:
    @classmethod
    def salvar(cls, categoria):
        with open('categorias.txt', 'a') as arq:
            arq.writelines(categoria)
            arq.writelines('\n')
            
    @classmethod
    def ler(cls):
        with open('categorias.txt', 'r') as arq:
            cls.categoria = arq.readlines()
        
        # Tratar \n
        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))
        
        categorias = []
        for i in cls.categoria:
            categorias.append(Categoria(i))
        
        return categorias
    
class DaoVenda:
    @classmethod
    def salvar(cls, venda: Vendas):
        with open('vendas.txt', 'a') as arq:
            arq.writelines(venda.itemVendido.nome + '|' + 
                           venda.itemVendido.preco + '|' +
                           venda.itemVendido.categoria + '|' +
                           venda.vendedor + '|' +
                           venda.comprador + '|' +
                           str(venda.quantidadeVendida) + '|' +
                           venda.data)
            arq.writelines('\n')
         
    @classmethod   
    def ler(cls):
        with open('vendas.txt', 'r') as arq:
            cls.venda = arq.readlines()
            
                # Tratar \n
        cls.venda = list(map(lambda x: x.replace('\n', ''), cls.venda))
        cls.venda = list(map(lambda x: x.split('|'), cls.venda))
        
        vendas = []
        for i in cls.venda:
            vendas.append(Vendas(Produtos(i[0], i[1], i[2]), i[3], i[4], i[5], i[6]))

            return vendas
