---
tipo: sistema
titulo: "Ecossistema e Ideias PKM"
tags: [pkm, ferramentas, ideias, arquitetura]
data_criacao: "2026-08-08"
---

# 🧠 Ecossistema e Ideias PKM (Personal Knowledge Management)

Este documento serve como um repositório central para catalogar ferramentas, arquiteturas e inspirações open-source que podem ser integradas ao nosso Segundo Cérebro no Obsidian.

## 🛠️ Ferramentas Mapeadas

### 1. [Joplin](https://github.com/laurent22/joplin)
- **O que é:** Um app de anotações open-source focado em privacidade e sincronização.
- **Principais Ideias para Extrair:**
  - Criptografia de ponta a ponta (E2EE) nativa.
  - **Web Clipper:** Possui uma das melhores extensões de navegador para salvar sites inteiros em Markdown. Podemos buscar plugins semelhantes para o Obsidian (como Omnivore ou MarkDownload).
  - Sincronização via nuvem (WebDAV, Nextcloud, Dropbox).

### 2. [Quartz](https://github.com/jackyzha0/quartz)
- **O que é:** O melhor Gerador de Sites Estáticos (SSG) projetado especificamente para o Obsidian.
- **Principais Ideias para Extrair:**
  - **Jardim Digital (Digital Garden):** Transforma as notas do Obsidian em um site público e navegável.
  - Entende nativamente a sintaxe do Obsidian (wikilinks `[[nota]]`, callouts, tags e o grafo interativo).
  - Pode ser automatizado com GitHub Actions para publicações grátis via GitHub Pages.

### 3. [Obsidian LiveSync](https://github.com/vrtmrz/obsidian-livesync)
- **O que é:** Um plugin da comunidade para sincronização em tempo real (estilo Google Docs) usando um banco de dados CouchDB.
- **Principais Ideias para Extrair:**
  - **Alternativa Open-Source ao Obsidian Sync:** Permite sincronizar notas entre o PC e o Celular em *milissegundos*.
  - Resolve o problema de conflitos de merge do Git quando editamos a mesma nota no celular e no computador ao mesmo tempo.
  - Exige uma pequena infraestrutura própria (self-host de um servidor CouchDB na nuvem, como AWS, Fly.io, ou local).
  - Possui Criptografia de Ponta a Ponta E2EE.

---
*Mande mais links para continuarmos expandindo o radar tecnológico do nosso sistema!*
