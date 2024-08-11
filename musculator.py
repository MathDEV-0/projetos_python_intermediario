import math

def calcula_preco():
    #Prefixos que devem ser eliminados para extrair a quantidade
    prefixos = [
        'Aveia:', 
        'Doce de Leite:', 
        'Whey (proteína de soro de leite):', 
        'Arroz cozido:', 
        'Carne (bovina cozida):', 
        'Frango (peito cozido):', 
        'Legumes:', 
        'Nozes:', 
        'Banana:', 
        'Pão Francês:', 
        'Maçã:'
    ]

    #Preço dos produtos por peso, envolvidos em tuplas, já que tuplas armazenam dados imutáveis e relacionados
    precos_peso = [
        ('Aveia', 165, 12.99),
        ('Doce de Leite', 450, 10.00),
        ('Whey (proteína de soro de leite)', 1000, 120.00),
        ('Arroz cozido', 1000, 9.19),
        ('Carne (bovina cozida)', 1000, 27.99),
        ('Frango (peito cozido)', 1000, 21.97),
        ('Legumes', 180, 4.99),
        ('Nozes', 180, 9.99)
    ]
    
    #Preço dos produtos por unidade
    precos_unidade = [
        ('Banana', 6, 3.99),
        ('Pão Francês', 2, 1.90), 
        ('Maçã', 11, 8.99)
    ]


    precos_peso_dict = {item: (peso, preco) for item, peso, preco in precos_peso} #Utilização do método dict comprehension: cria um dicionário e dá append em item, primeiro arg da tupla,peso, preco
    precos_unidade_dict = {item: (unidade, preco) for item, unidade, preco in precos_unidade}

    quantidades = {} #Dicionário das quantidades, vai armazenar nome do item e quantidade total 
    lista_aux = []

    #Leitura do arquivo 'calorias_dia.txt'
    with open('calorias_dia.txt', 'r') as arquivo: 
        for linha in arquivo:
            if 'g/unidade' in linha:
                lista_aux.append(linha.strip()) #Joga para lista auxiliar, apenas as linhas que contém item: pesagem/unidade

    #Iteração sobre a lista auxiliar
    for linha in lista_aux: 
        for prefixo in prefixos:
            if linha.startswith(prefixo): #Se a linha começa com os prefixos, então, são eliminados
                restante = linha.removeprefix(prefixo).strip()
                quantidade = float(restante.split()[0]) #'quantidade' é o primeiro item da lista restante que será splitada por espaços em branco. ex: '[2.0, g, ...]
                produto = prefixo.replace(":", "").strip()#Depois, removemos os espaços em branco para pegar o nome do item
                if produto in quantidades:
                    quantidades[produto] += quantidade #Soma a quantidade ao produto relacionado no dicionário
                else:
                    quantidades[produto] = quantidade
                break

    custo_mensal = 0
    
    for produto, quantidade in quantidades.items():
        if produto in precos_peso_dict:
            peso_pacote, preco_pacote = precos_peso_dict[produto]
            total_gramas = quantidade * 30
            pacotes_necessarios = math.ceil(total_gramas / peso_pacote)
            custo_produto = pacotes_necessarios * preco_pacote
        elif produto in precos_unidade_dict:
            unidade_pacote, preco_pacote = precos_unidade_dict[produto]
            total_unidades = quantidade * 30
            pacotes_necessarios = math.ceil(total_unidades / unidade_pacote)
            custo_produto = pacotes_necessarios * preco_pacote
        else:
            continue
        
        custo_mensal += custo_produto
        print(f'{produto}: {quantidade * 30:.2f} total - {pacotes_necessarios} pacotes x R$ {preco_pacote:.2f}/pacote = R$ {custo_produto:.2f}')

    print(f'\nCusto total mensal: R$ {custo_mensal:.2f}')
    
    salvar_preco(custo_mensal)

def calcula_calorias():
    refeicoes = {
        'primeira_refeicao': [],
        'segunda_refeicao': [],
        'terceira_refeicao': [],
        'quarta_refeicao': [],
        'quinta_refeicao': []
    }

    itens_peso = [
        ('Aveia', 389),  
        ('Doce de Leite', 315), 
        ('Whey (proteína de soro de leite)', 350), 
        ('Arroz cozido', 130), 
        ('Frango (peito cozido)', 165), 
        ('Carne (bovina cozida)', 250), 
        ('Legumes', 40), 
        ('Nozes', 654)   
    ]

    itens_unidade = [
        ('Banana', 105),
        ('Pão Francês', 271), 
        ('Maçã', 95)
    ]

    for nome_refeicao in refeicoes.keys():
        print(f'ITENS:')
        print("Itens por peso:")
        for idx, (item, calorias) in enumerate(itens_peso, start=1):
            print(f' [{idx}] {item}')
        print("Itens por unidade:")
        for idx, (item, calorias) in enumerate(itens_unidade, start=len(itens_peso) + 1):
            print(f' [{idx}] {item}')

        n = int(input(f"Digite quantos itens vão na sua {nome_refeicao.replace('_', ' ')}: "))

        for _ in range(n):
            item_idx = int(input(f"Digite o número do item que está incluso na {nome_refeicao.replace('_', ' ')}: ")) - 1
            
            if item_idx < 0 or item_idx >= len(itens_peso) + len(itens_unidade):
                print("Índice inválido. Por favor, escolha um número válido de item.")
                continue

            quantidade = float(input("Digite a gramatura/unidade do item (em gramas ou unidades): "))
            
            if item_idx < len(itens_peso):
                item_nome, item_calorias = itens_peso[item_idx]
                calorias_totais = (item_calorias / 100) * quantidade  
            else:
                item_nome, item_calorias = itens_unidade[item_idx - len(itens_peso)]
                calorias_totais = item_calorias * quantidade 
            
            refeicoes[nome_refeicao].append((item_nome, quantidade, calorias_totais))

    total_calorias = 0
    for nome_refeicao, itens_refeicao in refeicoes.items():
        calorias_refeicao = sum(calorias for _, _, calorias in itens_refeicao)
        total_calorias += calorias_refeicao
        print(f"Total de calorias na {nome_refeicao.replace('_', ' ')}: {calorias_refeicao:.2f} kcal")

    print(f"Total de calorias no dia: {total_calorias:.2f} kcal")

    salvar_calorias(refeicoes, total_calorias)

def salvar_calorias(refeicoes, total_calorias):
    with open('calorias_dia.txt', 'w') as arquivo:
        for nome_refeicao, itens_refeicao in refeicoes.items():
            arquivo.write(f'{nome_refeicao.replace("_", " ").title()}\n')
            for item_nome, quantidade, calorias_totais in itens_refeicao:
                arquivo.write(f'{item_nome}: {quantidade} g/unidade - {calorias_totais:.2f} kcal\n')
            calorias_refeicao = sum(calorias for _, _, calorias in itens_refeicao)
            arquivo.write(f'Total de calorias na refeição: {calorias_refeicao:.2f} kcal\n')
            arquivo.write('\n')

        arquivo.write(f'Total de calorias no dia: {total_calorias:.2f} kcal\n')

def salvar_preco(total_preco):
    with open('preco_mensal.txt', 'w') as arquivo:
        arquivo.write(f"Total de preço da dieta no mês: R$ {total_preco:.2f}\n")

def main():
    print(f'OPÇÕES: \n [1] Calcular calorias da dieta \n [2] Calcular preço da dieta \n')
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        calcula_calorias()
    elif opcao == 2:
        calcula_preco()

if __name__ == "__main__":
    main()
