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

def calcula_preco():
    pass

def main():
    print(f'OPÇÕES: \n [1] Calcular calorias da dieta \n [2] Calcular preço da dieta \n')
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        calcula_calorias()

if __name__ == "__main__":
    main()
