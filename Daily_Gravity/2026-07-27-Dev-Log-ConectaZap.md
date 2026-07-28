# Daily Log - ConectaZap Webhooks e Base64
**Data**: 27 de Julho de 2026

## 🎯 Missão Principal
O cliente estava precisando que o SaaS dele (Agenda Clean) repassasse áudios/imagens em formato **Base64** diretamente no payload do webhook, para que a Inteligência Artificial no N8N conseguisse processar as mídias (já que a Evolution API geralmente manda apenas a URL criptografada e a `mediaKey`).

## 🐞 Problemas Encontrados & Resoluções

### 1. Duplicação de Planos no Painel
- **Problema:** A tela de configurações da Workspace exibia planos duplicados (dois Starters, dois Pros, etc).
- **Causa:** O script de Seed do Prisma tinha rodado mais de uma vez gerando IDs diferentes com o mesmo nome, e a API do Dashboard (`/api/admin/dashboard`) não filtrava essas repetições.
- **Resolução:** Adicionamos um filtro (deduplicação por nome) direto na resposta da API (`route.ts`) e removemos a tabela visual de planos, focando o ConectaZap no que importa (Gateway).

### 2. Criação da "Chavinha" Base64 na Interface
- **Problema:** O cliente precisava de uma forma simples de habilitar/desabilitar o Base64 na Evolution API.
- **Resolução:** 
  - Adicionamos a coluna `webhookBase64` (Boolean) na tabela `Instance` no Prisma.
  - Criamos a aba **Configurações de Webhook** no Frontend (React/Vite).
  - Construímos a rota `POST /api/v1/instances/[id]/webhook` que atualiza a instância na Evolution API via `evolution.setGlobalWebhook(...)` e salva no banco do ConectaZap.

### 3. O Bug do "Duplo JSON" no Frontend
- **Problema:** Ao clicar na chavinha, o painel estourava um erro 500 no backend.
- **Causa:** O método genérico `apiRequest` no Frontend já aplicava `JSON.stringify`, mas estávamos passando uma string formatada no argumento `body`, criando um JSON duplo (`""{\"base64\": true}""`).
- **Resolução:** Removemos o `JSON.stringify` na chamada da rota, passando o objeto limpo `{ base64: true }`.

### 4. A Evolution "Ocultando" o Base64
- **Problema:** Mesmo ativando a configuração no "motor", o webhook final ainda NÃO continha o Base64, e sim a URL da mídia.
- **Causa:** 
  - 1º: A Evolution, para economizar banda, por vezes opta por enviar apenas URL + `mediaKey` ignorando a diretriz do webhookBase64 dependendo do peso da mídia.
  - 2º: A nossa rota de reencaminhamento (`/api/webhooks/evolution`) pegava os dados recebidos, fazia um `cleanPayload` pegando o nome, número e texto e *excluía* o resto, incluindo o Base64.
- **Resolução (Fallback Ativo e Blindado):** 
  - Alteramos a montagem do `cleanPayload`. 
  - Implementamos uma lógica proativa: se a chavinha de Base64 está ativada no ConectaZap, mas a Evolution mandou só a URL, o próprio ConectaZap faz um `fetch` no endpoint `/chat/getBase64FromMediaMessage/` internamente, baixa o arquivo, e *injeta* o base64 direto no payload limpo antes de disparar pro N8N do cliente. **Garantia 100% de entrega!**

### 5. O Erro 404 ao Disparar Mensagens do N8N
- **Problema:** O N8N do cliente estava dando `404 Not Found` ao tentar enviar mensagens de resposta ao WhatsApp.
- **Causa:** A arquitetura do sistema foi desenhada dividida (Frontend em React no site principal, Backend em Next.js em outro serviço). O cliente usou a URL do painel visual (`https://conectazap.up.railway.app`) em vez da URL do Motor/API (`https://apiwhatsappp.up.railway.app`).
- **Resolução:** Orientamos o uso da URL correta (`https://apiwhatsappp.up.railway.app/api/v1/messages/send`) passando o `instanceId` gerado pelo próprio Gateway.
