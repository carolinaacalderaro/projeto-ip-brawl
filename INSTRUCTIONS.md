Passos necessários para rodar o jogo(windows):
1- Ter criado o ambiente virtual(venv) em seu vscode:
      python -m venv venv

2-Ativar o venv:
      .\venv\Scripts\Activate.ps1

2.5- Se der erro de permissão no PowerShell, tente o comando abaixo antes de ativar:
      Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process 

3- Instalar o Pygame e o PyTMX:
      pip install pygame pytmx

FALTA:
mudar o placar
mudar o hud -> melhorar vida, mudar o texto do bonus de speed e dano para o icone com a contagem
mudar a tela de vitoria de rodada e do jogo
(minha opinião) personagens terem mais vida para alongar a batalha
mudar a seleção