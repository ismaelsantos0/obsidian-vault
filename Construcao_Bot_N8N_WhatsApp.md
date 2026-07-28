# Construção do Bot N8N - WhatsApp para Obsidian

## 🎯 Objetivo do Projeto
Criar um assistente pessoal via WhatsApp capaz de receber textos e áudios, processar o conteúdo utilizando a IA do Gemini (para formatação e transcrição de áudio), e salvar as anotações diretamente no Obsidian utilizando a API do GitHub.

---

## 🛑 Desafios Enfrentados e Soluções

### 1. O Mistério do Áudio Criptografado (Base64)
* **O Problema:** Quando enviávamos um áudio pelo WhatsApp, o Webhook da Evolution API/ConectaZap enviava apenas a URL criptografada (`.enc`) e as chaves de segurança (`mediaKey`), mas o Gemini precisava do áudio bruto em Base64 para conseguir transcrever.
* **As Tentativas:** Tentamos criar um Nó de HTTP Request para forçar o download da mídia no endpoint `/message/getBase64FromMediaMessage`, mas o servidor retornava um **Erro 404 (Página não encontrada)**.
* **O Diagnóstico:** Descobrimos que a URL usada (`conectazap.up...`) era apenas o painel visual (Frontend em Next.js) e não expunha as rotas da API.
* **A Solução Definitiva:** O desenvolvedor do SaaS atualizou o backend da plataforma para interceptar a mensagem de áudio, descriptografar nativamente e injetar o código Base64 diretamente no payload do webhook original (dentro de `data.message.base64`). Isso eliminou a necessidade de baixar a mídia manualmente pelo N8N.

### 2. O Erro de Sintaxe no JSON do N8N
* **O Problema:** Os nós de HTTP Request (Gemini e Formatação) apresentavam o erro: `The value in the "JSON Body" field is not valid JSON. Unexpected token '='`.
* **A Solução:** O N8N não aceita sinais de igual (`=`) no início de um campo JSON puro. A solução foi limpar o código, garantindo que o JSON começasse estritamente com as chaves `{`, ou utilizar o modo *Expression* de forma correta.

### 3. A Nota Salva em Branco no Obsidian
* **O Problema:** O robô conseguia transcrever o áudio, e o GitHub criava a nota diária (com o horário correto), mas o texto da transcrição não era salvo.
* **O Diagnóstico:** O Nó 6 (Código JavaScript de formatação final) estava codificado rigidamente para puxar o texto bruto da entrada do WhatsApp (`$('3').item.json.texto`), ignorando completamente o texto gerado pelo Nó 5 (Gemini).
* **A Solução:** Reescrevemos o código do Nó 6 para interceptar a resposta do Gemini, limpar os blocos de Markdown (` ```json `), transformar em Objeto e extrair perfeitamente a chave `conteudo`. 
```javascript
let ai_text = $input.first().json.candidates[0].content.parts[0].text;
ai_text = ai_text.replace(/```json/gi, '').replace(/```/g, '').trim();
const json_ai = JSON.parse(ai_text);
let texto_novo = json_ai.conteudo;
```

### 4. O Retorno (Confirmação) no WhatsApp Dando Erro 404
* **O Problema:** O nó final da automação (Nó 8), responsável por responder ao usuário com um "✅ Nota Salva", estava retornando um HTML gigante de **404 Not Found** do Next.js.
* **As Tentativas:** Testamos mudar as rotas, adicionar `/v1/`, e trocar tokens, mas o servidor continuava retornando a página visual de erro em vez de processar a mensagem ou dar um erro de permissão (JSON).
* **A Solução Definitiva:** Após analisar o HTML devolvido e confrontar o desenvolvedor, o mestre do SaaS percebeu que havia passado a URL do Frontend (`conectazap.up...`) em vez do Backend real da API.
A requisição final foi corrigida para bater na URL correta: `https://apiwhatsappp.up.railway.app/api/v1/messages/send`, autenticada com um Token de API exclusivo da mesma Workspace gerado no painel, utilizando o método POST.

---

## 🚀 Status Atual
**100% Funcional e Blindado.**
- Áudios são transcritos com perfeição.
- Textos são formatados inteligentemente.
- O GitHub salva na nota do dia e resolve conflitos (empilha o conteúdo em vez de sobrescrever).
- O usuário recebe recibo instantâneo no WhatsApp.
