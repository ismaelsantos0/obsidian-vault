# 🤖 Bot Obsidian via WhatsApp

> **Objetivo:** Criar um assistente pessoal que permite ler, criar e consultar o vault do Obsidian via WhatsApp, ativando APENAS para o número do dono.

---

## 1. ARQUITETURA GERAL

```
Você (WhatsApp) 
    → ConectaZap (Evolution API) 
        → Webhook N8N 
            → Filtro de Número (IF)
                → Agente IA (Gemini)
                    → GitHub API (Obsidian Vault)
                        → Resposta via WhatsApp
```

---

## 2. PRÉ-REQUISITOS

| Item | Detalhe |
|---|---|
| **Instância WhatsApp** | Criar instância separada no ConectaZap para o bot pessoal |
| **Seu número autorizado** | `5595XXXXXXX` (formato: DDI+DDD+Número) |
| **N8N** | Servidor próprio já rodando |
| **GitHub Token** | Personal Access Token com permissão `repo` |
| **Repositório** | `ismaelsantos0/obsidian-vault` |
| **Gemini API Key** | Para o Agente IA interpretar as mensagens |

---

## 3. FLUXO N8N (Passo a Passo)

### NÓ 1: Webhook (Entrada)
- **Tipo:** Webhook
- **Método:** POST
- **URL gerada:** `https://seu-n8n.com/webhook/bot-obsidian`
- **Ação:** Configurar essa URL no ConectaZap como Webhook da instância do bot.

---

### NÓ 2: Filtro de Número (Segurança)
- **Tipo:** IF
- **Condição:**
```
{{ $json.body.data.key.remoteJid }} == "5595XXXXXXX@s.whatsapp.net"
```
- **TRUE → Segue para o NÓ 3**
- **FALSE → Nó "NoOp" (ignora tudo)**

> ⚠️ **IMPORTANTE:** O formato do número no Evolution API é sempre:
> `5595XXXXXXX@s.whatsapp.net` (sem traços ou espaços)

---

### NÓ 3: Identificar Tipo de Mensagem
- **Tipo:** Switch
- **Campo:** `{{ $json.body.data.messageType }}`

| Tipo (`messageType`) | Ação |
|---|---|
| `conversation` ou `extendedTextMessage` | → Texto simples |
| `documentMessage` ou `documentWithCaptionMessage` | → PDF/Arquivo |
| `audioMessage` | → Áudio (transcrever) |
| `imageMessage` | → Imagem com legenda |

---

### NÓ 4A: Processar Texto
- **Tipo:** Code (JavaScript)
```javascript
// Extrai o texto da mensagem
const msg = $json.body.data.message;
const text = msg.conversation 
  || msg.extendedTextMessage?.text 
  || msg.imageMessage?.caption 
  || "";

return { text: text.trim() };
```

---

### NÓ 4B: Processar PDF
- **Tipo:** HTTP Request
- **Ação:** Baixar o arquivo do Evolution API
```
GET {{ $json.body.data.message.documentMessage.url }}
Headers: { apikey: "SUA_API_KEY_CONECTAZAP" }
```
- **Próximo nó:** Chamar o script `read_pdf.py` ou usar o nó de Code com biblioteca de PDF.

---

### NÓ 5: Agente IA (Gemini) — O Cérebro
- **Tipo:** HTTP Request (POST para a API Gemini)
- **URL:** `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent`

**System Prompt do Agente:**
```
Você é o assistente pessoal de Ismael. Você tem acesso ao vault do Obsidian dele.

Ao receber uma mensagem, você deve identificar a INTENÇÃO e retornar um JSON:

{
  "acao": "criar_nota" | "buscar" | "adicionar_em_nota" | "daily_note",
  "pasta": "pasta onde salvar (ex: 30_Dominio_Intelectual)",
  "titulo": "nome do arquivo sem .md",
  "conteudo": "conteúdo markdown para salvar",
  "query": "termo de busca (apenas para ação buscar)"
}

EXEMPLOS DE INTENÇÕES:
- "Salva isso no Obsidian: X" → criar_nota
- "Adiciona isso no Projeto Tinta: X" → adicionar_em_nota  
- "O que eu sei sobre X?" → buscar
- "Adiciona na daily de hoje: X" → daily_note

PASTAS DISPONÍVEIS:
- 10_Dominio_Pessoal → Assuntos pessoais
- 20_Dominio_Profissional/02_Projetos → Projetos
- 30_Dominio_Intelectual → Conhecimento e estudo
- Daily_Gravity → Diário diário
- 90_Sistema → Scripts e sistema
```

---

### NÓ 6: Executar Ação no GitHub (Obsidian)

#### 6A — CRIAR/ATUALIZAR NOTA
- **Tipo:** HTTP Request
- **Método:** PUT
- **URL:**
```
https://api.github.com/repos/ismaelsantos0/obsidian-vault/contents/{{ $json.pasta }}/{{ $json.titulo }}.md
```
- **Headers:**
```json
{
  "Authorization": "Bearer SEU_GITHUB_TOKEN",
  "Content-Type": "application/json"
}
```
- **Body:**
```json
{
  "message": "bot: nova nota via WhatsApp",
  "content": "{{ Buffer.from($json.conteudo).toString('base64') }}",
  "branch": "main"
}
```

#### 6B — BUSCAR NO VAULT
- **Tipo:** HTTP Request
- **Método:** GET (busca nos arquivos via GitHub API ou usando o Search)
```
GET https://api.github.com/search/code?q={{ $json.query }}+repo:ismaelsantos0/obsidian-vault
```

#### 6C — DAILY NOTE (APPEND)
- Primeiro GET para pegar o conteúdo atual do arquivo `Daily_Gravity/YYYY-MM-DD.md`
- Depois PUT com o conteúdo original + nova linha adicionada no final

---

### NÓ 7: Responder no WhatsApp
- **Tipo:** HTTP Request
- **Método:** POST
- **URL:**
```
https://SEU-CONECTAZAP.com/message/sendText/NOME_DA_INSTANCIA
```
- **Headers:** `{ apikey: "SUA_API_KEY" }`
- **Body:**
```json
{
  "number": "5595XXXXXXX",
  "text": "✅ Nota criada com sucesso!\n📁 {{ $json.pasta }}/{{ $json.titulo }}.md"
}
```

---

## 4. COMANDOS QUE VOCÊ PODE USAR

| Comando (WhatsApp) | O que acontece |
|---|---|
| `salva: [conteúdo]` | Cria nota em `30_Dominio_Intelectual` |
| `projeto tinta: [task]` | Adiciona no arquivo do Projeto Tinta |
| `daily: [texto]` | Adiciona na Daily Note de hoje |
| `busca: [termo]` | Pesquisa no vault e retorna resultado |
| `[link de artigo]` | Extrai e salva o conteúdo do link |
| `[PDF anexado]` | Extrai texto e cria nota |

---

## 5. VARIÁVEIS DE AMBIENTE (N8N)

Salve essas variáveis de forma segura nas Credentials do N8N:

```env
GITHUB_TOKEN=ghp_XXXXXXXXXXXXXXXXXXXX
GITHUB_REPO=ismaelsantos0/obsidian-vault
CONECTAZAP_API_KEY=SUA_KEY_AQUI
CONECTAZAP_URL=https://seu-conectazap.com
INSTANCIA_BOT=nome-da-instancia-bot
MEU_NUMERO=5595XXXXXXX@s.whatsapp.net
GEMINI_API_KEY=AIzaSy_XXXXXXXXXXXXXXXXXXXX
```

---

## 6. PRÓXIMOS PASSOS

- [ ] Criar instância do bot no ConectaZap
- [ ] Gerar GitHub Personal Access Token (scope: `repo`)
- [ ] Criar o workflow no N8N seguindo os nós acima
- [ ] Testar o filtro de número com uma mensagem simples
- [ ] Testar criação de nota básica
- [ ] Testar busca no vault
- [ ] Testar append na Daily Note
- [ ] Testar upload de PDF

---

*Tags: [[ConectaZap]] [[N8N]] [[Obsidian]] [[Bot_Pessoal]] [[GitHub_API]]*
