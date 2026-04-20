---
titulo: "Guia de Configuração dos Plugins"
data_criacao: 2026-04-17
dominio: 90_Sistema
tipo: recurso
tags: [obsidian, plugins, configuracao]
---

# ⚙️ Guia de Configuração dos Plugins
*Configure uma vez. Use para sempre.*

---

## 1. 🔥 Templater (PRIORIDADE MÁXIMA)

O Templater é o motor de tudo. Ele auto-preenche datas, nomes e estruturas.

### Passo a passo:
1. Vá em **Configurações** (engrenagem) → **Plugins da comunidade** → **Templater** → ⚙️ (ícone de opções)
2. Em **Template folder location**, coloque: `90_Sistema/03_Recursos`
3. Ative **Trigger Templater on new file creation** ← isso aplica templates automaticamente
4. Ative **Automatic jump to cursor** ← o cursor vai para onde você precisa escrever

### Como usar na prática:
- Pressione `Ctrl + P` → digite `Templater` → escolha **"Create new note from template"**
- Selecione o template desejado → Templater cria a nota já com a data preenchida

### Templates disponíveis:
- [[Template_Diario_Estudo]] → para `Diario_Estudo_DD-MM-AAAA`
- [[Template_Questoes_Sessao]] → para cadernos de questões
- [[Template_Resultado_Sessao]] → para páginas de resultado

---

## 2. 📅 Calendar (integração com diário)

O Calendar aparece na barra lateral. Clicar em um dia abre ou cria a nota daquele dia.

### Passo a passo:
1. Vá em **Configurações** → **Plugins nativos** → **Daily Notes** → ⚙️
2. Em **New file location**, coloque: `10_Dominio_Pessoal/04_Logs`
3. Em **Template file location**, coloque: `90_Sistema/03_Recursos/Template_Diario_Estudo`
4. Em **Date format**, coloque: `DD-MM-YYYY`

### Como usar:
- Clique em qualquer dia no painel Calendar (barra lateral direita)
- Se não houver nota para aquele dia → cria automaticamente com o template do diário
- Se já houver → abre direto

---

## 3. 🔘 Buttons (botões no Roteiro Mestre)

Adiciona botões clicáveis em notas. Já estão configurados no [[Roteiro Mestre - ALE-RR]].

### Como funciona:
- Os botões no Roteiro Mestre são blocos de código com a tag `button`
- Em modo de leitura (Preview), eles aparecem como botões clicáveis
- **IMPORTANTE:** Para ver os botões, alterne para o modo **Leitura** (`Ctrl + E`)

### Ações dos botões do Roteiro:
- **"📓 Criar Diário Hoje"** → abre modal do Templater para criar o diário do dia
- **"❓ Nova Sessão de Questões"** → cria novo caderno de questões
- **"📊 Novo Resultado"** → cria nova página de resultado

---

## 4. 🔍 Omnisearch (busca turbinada)

Funciona sem configuração. Substitui o `Ctrl + Shift + F` padrão.

### Como usar:
- `Ctrl + Shift + F` ou `Ctrl + U` → busca no vault inteiro
- Busca dentro do conteúdo das notas, não só no título
- Resultado com preview do contexto onde a palavra aparece

---

## 5. 📄 PDF Plus (anotar o edital)

Permite highlight e anotações no PDF do edital diretamente no Obsidian.

### Como usar:
1. Arraste o PDF do edital para a pasta `30_Dominio_Intelectual/03_Recursos/`
2. Clique no PDF no explorador → abre o PDF Plus
3. Selecione texto → clique em **Highlight** → escolha a cor
4. A anotação fica linkada na nota que você especificar

> [!TIP]
> Use cores diferentes por prioridade: 🟡 médio · 🔴 alto · 🟢 já domina

---

## 6. 🎨 Style Settings (aparência)

Para funcionar, você precisa de um tema compatível (ex: **Minimal**, **AnuPpuccin**, **Typewriter**).

### Como ativar:
1. Vá em **Configurações** → **Aparência** → **Temas** → Procure e instale **"Minimal"**
2. Depois vá em **Plugins da comunidade** → **Style Settings** → personalização visual completa

---

## 7. 🔗 Links (manipulação de links)

Converte links entre formatos. Útil para organização.

### Funções principais:
- `Ctrl + P` → "Links: Convert Wikilinks to Markdown links" (e vice-versa)
- "Links: Extract links" → lista todos os links de uma nota
- "Links: Copy link to clipboard" → copia link formatado

---

## ✅ Checklist de Configuração

- [ ] Templater → pasta de templates configurada para `90_Sistema/03_Recursos`
- [ ] Templater → "Trigger on new file creation" ativado
- [ ] Daily Notes → pasta `10_Dominio_Pessoal/04_Logs`, template `Template_Diario_Estudo`
- [ ] Daily Notes → formato de data `DD-MM-YYYY`
- [ ] Calendar → ativo na barra lateral (ícone de calendário)
- [ ] PDF Plus → edital em PDF copiado para o vault
- [ ] Style Settings → tema Minimal instalado *(opcional)*
