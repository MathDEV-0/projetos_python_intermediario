________________________________________
Documentação do Projeto: Calculadora de Calorias e Preços

Foco do projeto: Python

Nível do projeto: intermediário

1.Breve Descrição do Projeto
O projeto é um sistema de gerenciamento para calcular o custo mensal e as calorias diárias de uma dieta. Ele lê dados de consumo de alimentos de um arquivo, calcula o custo mensal com base nos preços dos pacotes e as quantidades consumidas, e calcula o total de calorias para as refeições diárias. O sistema também permite salvar os resultados em arquivos para análise posterior.

2.Funcionalidades
  a) Cálculo de Preço Mensal:
  -Lê um arquivo com informações sobre consumo diário.
  -Calcula o custo mensal com base na quantidade consumida e no preço dos pacotes de alimentos.
  -Imprime o custo mensal e detalha o custo por item.
  b) Cálculo de Calorias Diárias:
  -Permite ao usuário inserir informações sobre a dieta diária.
  -Calcula as calorias totais com base na quantidade de alimentos consumidos.
  -Imprime o total de calorias por refeição e por dia.
  c) Salvamento de Dados:
  -Salva os cálculos de calorias e preços em arquivos para análise futura.

3.Estrutura do Projeto

3.1. Arquivos
  a)	calorias_dia.txt
  -Contém informações sobre o consumo diário, incluindo tipo de alimento, quantidade e calorias.
  b) preco_dia.txt
  -Contém o cálculo do custo total diário da dieta.
  c) preco_mensal.txt
  -Contém o cálculo do custo total mensal da dieta.

3.2. Funções
  1.	calcula_preco()
  -Calcula o custo mensal dos alimentos com base nas quantidades consumidas e nos preços dos pacotes.
  -Lê dados de calorias_dia.txt.
  -Imprime e salva o custo mensal em preco_mensal.txt.
  2.	calcula_calorias()
  -Permite ao usuário inserir dados sobre as refeições diárias.
  -Calcula as calorias totais para cada refeição e para o dia.
  -Imprime e salva o total de calorias em calorias_dia.txt.
  3.	salvar_calorias(refeicoes, total_calorias)
  -Salva os dados das refeições e o total de calorias no arquivo calorias_dia.txt.
  4.	salvar_preco(total_preco)
  -Salva o custo total mensal da dieta no arquivo preco_mensal.txt.
  5.	main()
  -Função principal que oferece opções para calcular calorias ou preço.
  -Recebe a escolha do usuário e chama a função apropriada.

3.3. Como Executar
  a)	Rodar o Programa:
  -Execute o script Python.
  -Escolha a opção desejada (1 para calcular calorias, 2 para calcular o preço).
  b)	Verificar Resultados:
  -Após a execução, verifique os arquivos de saída (preco_dia.txt, preco_mensal.txt, calorias_dia.txt) para os resultados.
