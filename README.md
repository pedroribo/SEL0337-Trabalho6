# SEL0337-Trabalho6

Alunos:
Matheus Maquera Torres 5270220;
Pedro Ricieri Borchio 12547552

## Projeto da Verificação da tag de Acesso

  O ID da tag é salvo como um int no código, com o comando ".read_id()" o ID do cartão aproximado é lido e transformado em um variável int. Finalmente, é feita a comparação com o id cadastrado e se forem iguais é printado "acesso liberado" e o led verde é acesso, caso contrário, "acesso negado" e o led vermelho acende.
  
![20231127_170121](https://github.com/pedroribo/SEL0337-Trabalho6/assets/89107333/f8abc32a-84dc-41d8-81b7-055e52cbb1d4)
  

## Projeto Reconhecimento Facial com Print na Imagem

Usando a biblioteca picamera 2 e OpenCV, capturamos uma imagem com auxílio do algoritmo "haarcascade_frontalface_default.xml". O código detecta rostos e os salva em escala de cinza com o número usp dos integrantes do grupo.

Não foi possível capturar a imagem devido a complicações na utilização das câmeras com a Raspberry Pi.

 ![20231204_172519](https://github.com/pedroribo/SEL0337-Trabalho6/assets/89107333/03fdd1d3-5678-44be-bc57-9e49c4f956ad)
