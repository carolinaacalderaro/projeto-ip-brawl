# 🎮 CIn Brawl

Jogo desenvolvido em **Python + Pygame** como projeto da disciplina de **Introdução à Programação** (1º período) do **Centro de Informática (CIn) - UFPE**.

CIn Brawl é um jogo de combate 1v1, local e por turnos de ação em tempo real, inspirado em *Brawl Stars*. Dois jogadores escolhem seus personagens e se enfrentam em um mapa com diversos obstáculos, arbustos para se esconder e itens que concedem vantagens, em uma disputa de melhor de 3 rodadas.

## 📖 Sobre o projeto

O jogo foi construído como forma de aplicar, na prática, os principais conceitos vistos ao longo do período: estruturas condicionais e de repetição, funções, listas, dicionários e orientação a objetos (classes e herança).

## ✨ Funcionalidades

- **Modo 2 jogadores (local utilizando o mesmo teclado)**, cada um com seu próprio conjunto de controles.
- **4 personagens jogáveis**: Shelly, Piper, Colt e Iyoda, cada um com sprites próprios de movimentação.
- **Tela inicial** e **tela de seleção de personagens** com animações e confirmação individual de cada jogador.
- **Sistema de tiro** com munição limitada (4 balas) e recarga automática por tempo.
- **Mapa interativo** carregado a partir de um arquivo `.tmx` (Tiled Map Editor), com:
  - **Paredes**, que bloqueiam o movimento e os projéteis;
  - **Água**, que impede a passagem dos jogadores;
  - **Arbustos**, que escondem o jogador (e o "camuflam" no HUD) quando ele está suficientemente coberto.
- **Itens coletáveis** que reaparecem aleatoriamente pelo mapa:
  - 💚 **Vida**: adiciona e/ou recupera 1 ponto de vida (até o máximo);
  - 💥 **Dano**: aumenta o dano dos projéteis (até 3 níveis);
  - ⚡ **Velocidade**: aumenta a velocidade de movimento (até 3 níveis).
- **HUD completo** com vida, munição, bônus de dano/velocidade e placar de rodadas.
- **Sistema de rodadas**: vence a partida quem ganhar **2 rodadas** primeiro; ao final de uma rodada os personagens são reposicionados e os itens redistribuídos.
- **Tela de fim de jogo** com opção de reiniciar o campeonato ou voltar à tela de seleção de personagens.

## 🕹️ Controles

| Ação                | Player 1 (Azul)      | Player 2 (Vermelho)      |
|----------------------|-----------------------|----------------------------|
| Mover cima/baixo/esq/dir | `W` `A` `S` `D`  | `↑` `↓` `←` `→`         |
| Atirar               | `ESPAÇO`              | `ENTER`                    |
| Selecionar personagem | `A` / `D`             | `←` / `→`                  |
| Confirmar personagem  | `ESPAÇO`              | `ENTER`                    |
| Sair do jogo          | `ESC`                 | `ESC`                      |

Na tela de fim de jogo:
- `R` — reinicia o campeonato (placar zerado, mesmos personagens);
- `T` — volta para a tela de seleção de personagens.

## 🗂️ Estrutura do projeto

```
projeto-ip-brawl/
├── main.py            # Ponto de entrada do jogo
├── game.py             # Loop principal, regras de partida e HUD
├── players.py          # Classe Player e subclasses Player1/Player2
├── personagens.py      # Dicionário com os personagens disponíveis
├── itens.py             # Classes Item (coletáveis) e Projectile (balas)
├── mapa.py              # Carregamento do mapa .tmx e áreas de colisão
├── tela_inicial.py     # Tela inicial do jogo
├── tela_selecao.py     # Tela de seleção de personagens
├── settings.py          # Configurações gerais (resolução da tela)
├── utils.py              # Funções utilitárias
└── assets/                # Sprites, mapa, fontes e imagens de UI
```

## 🛠️ Tecnologias utilizadas

- [Python 3](https://www.python.org/)
- [Pygame](https://www.pygame.org/) — engine do jogo
- [PyTMX](https://github.com/bitcraft/PyTMX) — leitura de mapas criados no [Tiled Map Editor](https://www.mapeditor.org/)

## 🚀 Como rodar o projeto

### Pré-requisitos
- Python 3 instalado
- Git (opcional, para clonar o repositório)

### Passo a passo (Windows)

1. Clone o repositório:
   ```bash
   git clone https://github.com/carolinaacalderaro/projeto-ip-brawl.git
   cd projeto-ip-brawl
   ```

2. Crie um ambiente virtual:
   ```powershell
   python -m venv venv
   ```

3. Ative o ambiente virtual:
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
   > Se ocorrer erro de permissão no PowerShell, rode antes:
   > ```powershell
   > Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
   > ```

4. Instale as dependências:
   ```bash
   pip install pygame pytmx
   ```

5. Execute o jogo:
   ```bash
   python main.py
   ```

## 📌 Como jogar

1. Na tela inicial, pressione a tecla indicada para começar.
2. Cada jogador escolhe seu personagem (setas/`A`-`D`) e confirma (`ESPAÇO`/`ENTER`).
3. Movam-se pelo mapa, colidam com itens para ganhar vantagens e usem os arbustos para se esconder do adversário.
4. Atirem no oponente para reduzir sua vida — quem chegar a 0 de vida perde a rodada.
5. Vence o jogo quem ganhar **2 rodadas**.

## 👥 Autoria

Projeto desenvolvido para a disciplina de Introdução à Programação — CIn/UFPE.

## 📄 Licença

Projeto acadêmico, desenvolvido para fins educacionais.
