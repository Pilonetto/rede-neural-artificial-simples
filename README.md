# Rede Neural Artificial Simples
Este é um exemplo de como criar uma rede neural artificial simples utilizando a biblioteca Keras no Python.

## Descrição do Projeto
Este projeto demonstra como criar uma rede neural artificial simples utilizando a biblioteca Keras no Python. A rede neural criada utiliza uma camada oculta de 4 neurônios e uma camada de saída com um único neurônio. A função de ativação da camada oculta é a função relu e a função de ativação da camada de saída é a função sigmoid.

Os dados de entrada e saída utilizados no projeto são os seguintes:

`entrada = [[0,0], [0,1], [1,0], [1,1]]
saida = [0, 1, 1, 0]`
O modelo é treinado utilizando o algoritmo de otimização Adam e a função de perda binary_crossentropy. Após o treinamento, o modelo é testado utilizando os mesmos dados de entrada utilizados no treinamento.

## Pré-requisitos
Antes de executar o código deste projeto, certifique-se de que as seguintes bibliotecas estão instaladas no seu ambiente Python:

- Keras
- Numpy

## Como Executar o Projeto
Para executar o projeto, basta executar o arquivo main.py. O resultado da execução será a impressão dos valores de saída previstos pelo modelo para cada um dos dados de entrada.

## Contribuição
Contribuições são sempre bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença
Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para detalhes.