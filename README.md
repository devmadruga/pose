# Reconhecimento de Ação em Vídeo

Projeto em Python fazendo uso de [OpenCV](https://opencv.org/) e [MediaPipe](https://google.github.io/mediapipe/) que detecta certos tipos de movimentos.

## :hammer: Tecnologias utilizadas
As seguinte tecnologias são utilizadas neste projeto:

1. Python
2. OpenCV
3. MediaPipe 


## :woman_cartwheeling: Movimentos/Posições detectadas

O projeto aqui compartilhado é capaz de detecar as seguintes posições:

<p align="center">
 <img src="https://github.com/devmadruga/pose/blob/main/movimentos.jpg" height="450"/>
</p>

Legendas:

1. "Rosca direta" com o braço esquerdo - como na academia, treinando biceps.
2. "Rosca direta" com o braço direito - como na academia, treinando biceps.
3. Braço direito paralelo ao chão.
4. Braço esquerdo paralelo ao chão.
5. Encostou uma mão na outra.
6. Levantou braço esquerdo para cima.
7. Levantou braço direito para cima
8. Braço esquerdo "descansando". Próximo ao corpo e "esticado para baixo".
9. Braço direito "descansando". Próximo ao corpo e "esticado para baixo".
10. Mostrando o "muque" do braço esquerdo.
11. Perna esquerda paralela ao chão.
12. Perna direita paralela ao chão.
13. Mão esquerda na boca.
14. Mão direita na boca.
15. Pessoa está de lado.
16. Cabeça inclinada para a direita.
17. Cabeça inclinada para a esquerda.
18. Pessoa está abaixada.
19. Pessoa está levantada.
20. Pessoa está deitada.


## :computer: Como rodar o projeto?

Você pode rodar o projeto através dos passos 1 -> 2 -> 3 ou 1 -> 2 -> 4 -> 5.

1. Você precisará do arquivo main.py e do diretório moves que contém os arquivos moves.py e __init__.py.
2. Você precisa ter o Python instalado na sua máquina e, se possível, criar um ambiente virtual para rodar o projeto.

Ainda, se você quiser instalar os pacotes necessários através do requirements.txt, você precisará do arquivo requirements.txt e rodar

3. > pip install -r requirements.txt

Você também pode instalar os pacotes através do pip, rodando:

4. > pip install opencv-python

e

5. > pip install mediapipe


## :heavy_check_mark: Etapas realizadas

Acabei upando um "projeto limpo" aqui no github, mas os commits realizados durante a realização do projeto ocorreram após cada etapa descrita:


- [X] Criadas e testadas as primeiras duas ou três funções que detectavam movimento.
- [X] Detecção implementada no código e layout ajustado para mostrar todos os contadores na tela.
- [X] Pensando em Classes - funções antes criadas, agora se tornaram métodos de classes específicas para cada tipo de movimento.
- [X] Detecção criar, implementada, testada e layout ajustado.
- [X] Criação, implementação e teste de nova Classe para detectar outro tipo de movimento.
- [X] Criação, implementação e teste de nova Classe para detectar outro tipo de movimento.
- .
- .
- .
- [x] Generalização das funções sobre distâncias e sobre ângulos.
- [x] Projeto entregue.

## :thinking: Oportunidades de melhorias:

Podemos realizar as seguintes melhorias no projeto:


## :ramen: Licença

Este projeto está sob "Unlicense license". Para maiores detalhes sobre a licença utilizada, click [aqui](https://github.com/devmadruga/elt_projeto/blob/main/LICENSE). 
