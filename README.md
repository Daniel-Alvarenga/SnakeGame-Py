# SnakeGame-Py
Snake game made in Python to be played on terminal

Este é um jogo clássico da cobrinha (Snake Game) criado em Python. O jogo oferece uma interface para terminal (cmd, powershell, dentre outros) onde você controla a cobra para pegar maçãs e evita colidir com a própria cauda. Você também pode coletar "proteções" para tornar a experiência mais "segura". O jogo é uma ótima maneira de testar suas habilidades de raciocínio e reflexos.

![Demonstração do Snake Game](demo.gif)

## Uso

Certifique-se de ter o Python instalado em seu sistema. Recomenda-se criar um ambiente virtual Python para gerenciar as dependências do projeto.

1. Clone o repositório:

   ```shell
   git clone https://github.com/seu-usuario/snake-game.git
   cd snake-game
   ```

2. Crie um ambiente virtual:

    ```shell
    python -m venv venv
    ```

3. Ative o ambiente virtual:

    No Windows:

    ```shell
    venv\Scripts\activate
    ```
    No macOS e Linux:
    ```shell
        source venv/bin/activate
    ```
    
  4. Instale as dependências do projeto a partir do arquivo requirements.txt:
     ```shell
        pip install -r requirements.txt
     ```

## Como jogar

Para jogar siga os seguites passos  

  1. Inicie o jogo: 
     ```shell
       python snake_game.py
     ```
     
  2. Use as setas do teclado para mover a cobra:  
          ↑ (seta para cima): Mover para cima  
          ↓ (seta para baixo): Mover para baixo  
          ← (seta para a esquerda): Mover para a esquerda  
          → (seta para a direita): Mover para a direita

  3. Colete maçãs para aumentar o tamanho da cobra e sua pontuação, se você completar todo o tabuleiro você zera o jogo.

  4. Evite morder a própria cauda da cobra, caso contrário, ao se morder irá perder.
  
      *Dicas*
      
      Você pode coletar "proteções" para ter uma chanche a mais caso se colida com a cauda comendo as maças douradas que têm 1% de chanche de aparecer a cada frame.
  
      Segure a tecla de espaço para pausar o jogo.
  
      Quando o jogo terminar, pressione ENTER para começar um novo jogo ou pressione ESC para encerrar o jogo.

## Créditos

Este projeto foi criado por Daniel R. Alvarenga em 11/2023.

Visite também essa [versão em site][link] do projeto no meu GitHub

[link]: https://github.com/Daniel-Alvarenga/Snake-Game

Contribuições são bem-vindas! Sinta-se à vontade para enviar solicitações de pull (pull requests) para melhorar o jogo.
