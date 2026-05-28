# GS_DSA - MONITORAMENTO DE MISSÃO ESPACIAL
Projeto acadêmico (FIAP); Realizado por dois estudantes de Ciência da Computação (1° semestre).
Giovane Salazar Fioriavante  RM: 570396
Leonardo Basile Takachi  RM: 569066
Neste projeto, utilizamos a linguagem Python para criar um sistema interativo dentro do terminal para monitorar dados operacionais de uma missão espacial experimental. Dentro dessas interações, realizamos o uso de funções com linhas de código afim de realizar várias tarefas relacionadas com o tema do projeto.

* Explicação da Lógica Utilizada *
A lógica foi divida em quatro pilares principais:
1. Modularização pem funçôes:
Para melhor organização do código e para facilitar alguma manutenção futura, dividimos o código em funções (cadastrar_dados, analisar_missao, exibir_historico).

2. Estruturas de Dados:
Realizamos o uso de dicionários para agrupar variáveis e utilizamos Listas(vetores) para fazer um histórico que armazene esses dicionários. 

3. Processamento Condicional:
A função "analisar_missao" utiliza uma estrutura de if/elif/else para realizar a Verificação Automática. Ela cruza os dados para identificar três estados críticos:
Superaquecimento: Temperatura > 80.
Economia de Energia: Energia < 20.
Falha na comunicação: Comunicação = 0.

4. Interface e Repetição:
O menu_principal utiliza um laço while True para que o sistema permaneça operacional até o usuário escolha encerrar, permitindo uma simulação contínua.



<img width="1276" height="525" alt="image" src="https://github.com/user-attachments/assets/c559e911-0af1-4163-99e7-3e715d9ceaf2" />
