import json
import os
from collections import defaultdict
from datetime import datetime

# Configurações de Diretórios
VAULT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
CULTURA_DIR = os.path.join(VAULT_ROOT, "10_Dominio_Pessoal", "03_Recursos", "Cultura")
DASHBOARD_FILE = os.path.join(CULTURA_DIR, "🏆_Top_100_Musicas_Mais_Ouvidas.md")

# Template Base
TEMPLATE = """---
tipo: cultura
titulo: "{titulo}"
categoria: "{categoria}" 
criador: "{criador}"
rating: {rating}
data_inclusao: "{data_inclusao}"
tags: [cultura, auto-injetado]
---

# 🎵 {titulo}
**Categoria:** `$= dv.current().categoria` | **Criador/Artista:** `$= dv.current().criador` | **Rating:** `$= "⭐".repeat(dv.current().rating)`

---

## 🎧 Resumo do Histórico
> Você consumiu muito o conteúdo deste artista/criador. Aqui estão as suas faixas ou vídeos mais consumidos de acordo com a mineração de dados!

---

## 🌟 Faixas/Momentos Favoritos
{top_items}

---
"""

def process_spotify(filepath):
    if not os.path.exists(filepath):
        print(f"⚠️ Arquivo {filepath} não encontrado. Pulando Spotify...")
        return

    print("🎧 Processando Histórico do Spotify...")
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Agrupamentos
    artist_playtime = defaultdict(int)
    artist_tracks = defaultdict(lambda: defaultdict(int))
    track_playtime = defaultdict(int)

    for item in data:
        artist = item.get("artistName", "Desconhecido")
        track = item.get("trackName", "Desconhecido")
        ms_played = item.get("msPlayed", 0)
        
        # Só conta se ouviu por mais de 30 segundos
        if ms_played > 30000:
            artist_playtime[artist] += ms_played
            artist_tracks[artist][track] += ms_played
            track_playtime[f"{track} - {artist}"] += ms_played

    # 1. Gerar Arquivos por Artista (Top 50 Artistas)
    top_artists = sorted(artist_playtime.items(), key=lambda x: x[1], reverse=True)[:50]
    
    for artist, time in top_artists:
        # Pega as top 5 musicas do artista
        top_tracks = sorted(artist_tracks[artist].items(), key=lambda x: x[1], reverse=True)[:5]
        
        items_md = ""
        for track_name, _ in top_tracks:
            items_md += f"- {track_name}\n"
            
        safe_title = artist.replace("/", "-").replace("\\", "-").replace(":", "")
        file_path = os.path.join(CULTURA_DIR, f"{safe_title}.md")
        
        # Só cria se não existir, para não sobrescrever anotações manuais
        if not os.path.exists(file_path):
            content = TEMPLATE.format(
                titulo=artist,
                categoria="Música",
                criador=artist,
                rating=5,
                data_inclusao=datetime.now().strftime("%Y-%m-%d"),
                top_items=items_md
            )
            with open(file_path, 'w', encoding='utf-8') as fw:
                fw.write(content)

    # 2. Gerar Painel Top 100
    top_100 = sorted(track_playtime.items(), key=lambda x: x[1], reverse=True)[:100]
    
    dashboard_content = "---\ntags: [dashboard, musica, top100]\n---\n\n# 🏆 Top 100 Músicas Mais Ouvidas (All Time)\n\n"
    for i, (track, _) in enumerate(top_100, 1):
        dashboard_content += f"{i}. **{track}**\n"
        
    with open(DASHBOARD_FILE, 'w', encoding='utf-8') as fw:
        fw.write(dashboard_content)

    print(f"✅ Spotify finalizado! Criados {len(top_artists)} artistas e o Top 100.")


def process_youtube(filepath):
    if not os.path.exists(filepath):
        print(f"⚠️ Arquivo {filepath} não encontrado. Pulando YouTube...")
        return

    print("📺 Processando Histórico do YouTube...")
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    channel_views = defaultdict(int)
    channel_videos = defaultdict(lambda: defaultdict(int))

    for item in data:
        # YouTube JSON takeout tem a chave 'subtitles' com o nome do canal
        subs = item.get("subtitles", [])
        if subs:
            channel = subs[0].get("name", "Desconhecido")
            title = item.get("title", "Desconhecido").replace("Watched ", "")
            
            channel_views[channel] += 1
            channel_videos[channel][title] += 1

    # Filtrar Top 30 Canais
    top_channels = sorted(channel_views.items(), key=lambda x: x[1], reverse=True)[:30]

    for channel, views in top_channels:
        # Pega os 5 vídeos mais vistos do canal
        top_videos = sorted(channel_videos[channel].items(), key=lambda x: x[1], reverse=True)[:5]
        
        items_md = ""
        for video_title, _ in top_videos:
            items_md += f"- {video_title}\n"
            
        safe_title = channel.replace("/", "-").replace("\\", "-").replace(":", "")
        file_path = os.path.join(CULTURA_DIR, f"{safe_title}.md")
        
        if not os.path.exists(file_path):
            content = TEMPLATE.format(
                titulo=channel,
                categoria="YouTube",
                criador=channel,
                rating=5,
                data_inclusao=datetime.now().strftime("%Y-%m-%d"),
                top_items=items_md
            )
            with open(file_path, 'w', encoding='utf-8') as fw:
                fw.write(content)

    print(f"✅ YouTube finalizado! Criadas notas para {len(top_channels)} canais mais assistidos.")

if __name__ == "__main__":
    print("🚀 Iniciando Injeção em Massa no Segundo Cérebro...")
    
    spotify_path = os.path.join(os.path.dirname(__file__), "spotify_history.json")
    youtube_path = os.path.join(os.path.dirname(__file__), "youtube_history.json")
    
    process_spotify(spotify_path)
    process_youtube(youtube_path)
    
    print("🎉 Injeção concluída com sucesso! Abra sua pasta Cultura no Obsidian para ver.")
