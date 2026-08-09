# 💉 Guia: Como Injetar Seu Histórico no Obsidian

O motor em Python já está codificado e aguardando os seus dados nesta pasta (`injetor_cultura.py`). 

Siga este passo-a-passo exato para explodir dezenas de artistas e canais automaticamente para dentro do seu "Segundo Cérebro".

## Passo 1: Baixar os Dados
Você precisará de dois arquivos:

**🎧 Spotify:**
1. Acesse [spotify.com/account/privacy](https://www.spotify.com/account/privacy).
2. Vá até o final da página e peça para "Baixar seus dados" (Histórico de Streaming de 1 ano ou Histórico Estendido).
3. Quando receber o e-mail (demora alguns dias), abra o arquivo `.zip` e encontre o arquivo chamado `StreamingHistory0.json` (pode ter outro número).
4. Renomeie esse arquivo para `spotify_history.json`.

**📺 YouTube:**
1. Acesse o [Google Takeout](https://takeout.google.com/).
2. Desmarque tudo e marque apenas **YouTube e YouTube Music**.
3. Clique em "Vários formatos" e garanta que o formato de Histórico seja **JSON** (em vez de HTML).
4. Exporte, baixe o `.zip`, abra a pasta do YouTube e encontre o arquivo `watch-history.json`.
5. Renomeie para `youtube_history.json`.

## Passo 2: Colocar na Pasta Certa
> [!IMPORTANT]
> Mova os arquivos `spotify_history.json` e `youtube_history.json` para **dentro** desta pasta (`90_Sistema/03_Recursos/scripts/`). Eles devem ficar exatamente ao lado do arquivo `injetor_cultura.py`.

## Passo 3: Apertar o Play!
Abra o seu terminal (PowerShell ou CMD), navegue até a pasta dos scripts e execute o código:

```powershell
cd "c:\Users\ismae\OneDrive\Documentos\OBSIDIAN\90_Sistema\03_Recursos\scripts\"
python injetor_cultura.py
```

> [!SUCCESS] A Mágica
> O script vai avisar na tela quantos arquivos processou. Ele vai criar as notas dos seus **50 Artistas** mais ouvidos, dos seus **30 Canais** mais vistos, e vai gerar uma nota bônus chamada `🏆_Top_100_Musicas_Mais_Ouvidas.md` direto na sua pasta de **Cultura**! Tudo auto-linkado e padronizado no Dataview.
