---
titulo: "Especificações - Site de Sorteios Instagram"
tipo: projeto
status: em_desenvolvimento
data_criacao: 2026-04-24
data_atualizacao: 2026-04-24
tags: [projeto, saas, dev, sorteio, side-job]
---

# 🎯 Projeto: Sorteador Instagram (InstaSorteios)

> [!info] Visão Geral
> **Objetivo:** Criar um aplicativo web super moderno, rápido e bonito para realizar sorteios justos a partir de comentários do Instagram. O sistema será desenhado com estética "Premium" para ser usado durante transmissões ao vivo (lives de influenciadores).
> **Papel no "Beast Mode":** Servir como um Side Job / Produto SaaS para escalar rendimentos (aumentando a fatia de reserva financeira do planejamento geral).

---

## 🛠️ Stack Tecnológico (Implementado)

- **Front-end:** `React.js` + `Vite` + `TailwindCSS` — gerado via **Lovable**, hospedado no **Railway**.
- **Back-end:** `Python 3.13` + `FastAPI` + `SQLAlchemy` — hospedado no **Railway**.
- **Banco de Dados:** `PostgreSQL` — provisionado no Railway, tabelas criadas automaticamente no startup.
- **Gateway Financeiro:** `Mercado Pago` — Pix (avulso) + Preapproval (mensalidade). Comunicação via **Webhooks**.
- **Motor de Coleta de Dados:**
  - **Motor 1 (Meta Graph API):** Login com Facebook → leitura de comentários dos próprios posts. App Meta criado: `SaaS Sorteios`.
  - **Motor 2 (Apify Scraper API):** Raspagem de posts públicos de terceiros. Ativado somente após confirmação de pagamento.

---

## 🚀 Funcionalidades Chave (Escopo do Produto)

1. **Entrada Simplificada:** Um campo de busca estiloso onde o usuário cola apenas o link do Post (`instagram.com/p/...`).
2. **Regras Avançadas de Sorteio:**
   - 🛡️ **Filtro Anti-Spam:** Opção de "Remover múltiplos comentários do mesmo usuário" (1 chance por pessoa).
   - 🔍 **Filtro por Palavra/Menção:** O sorteador só valida comentários que possuam "Eu quero" ou que tenham marcado um `@amigo`.
3. **A Experiência Visual do Sorteio (A Mágica):**
   - Ao clicar em "Sortear", em vez de só mostrar o nome rápido, a tela escurece e os nomes/fotos de perfil dos participantes começam a passar voando na tela (Roleta visual), com um contador regressivo, gerando máxima expectativa para quem está assistindo.
4. **Certificado de Veracidade:** 
   - Exibição de um "Card" bonito com a foto do vencedor, o comentário exato e a data/hora do sorteio, pronto para tirar Print (Screenshot) e postar nos Stories.

---

## 💰 Modelo de Negócios e Monetização
*(A Estratégia Híbrida: O Melhor dos Dois Mundos)*

- **Modelo 1: Sorteio Expresso (Pay-per-use via Pix)**
  - Focado no cliente comum que quer rapidez. Ele só cola o link de qualquer post público.
  - **Como funciona:** O sistema usa o *Motor 2 (Apify)* em duas fases (Sondagem -> Pagamento -> Raspagem).
  - **Lógica de Cobrança (Tabelada):** A inteligência fará a sondagem do post para descobrir o número de comentários e enquadrar na nossa tabela de preços fixos:
    - *Até 1.000 comentários:* **R$ 19,90** (Custo R$ 11,50 | Lucro ~R$ 8,40)
    - *Até 2.000 comentários:* **R$ 39,90** (Custo R$ 23,00 | Lucro ~R$ 16,90)
    - *Até 5.000 comentários:* **R$ 89,90** (Custo R$ 57,50 | Lucro ~R$ 32,40)
    - *Acima de 5.000:* Bloqueio estratégico amigável indicando a necessidade de assinar o plano PRO (Motor 1) para viabilizar.

- **Modelo 2: Assinatura PRO (Mensalidade)**
  - Focado em agências, influenciadores e criadores de conteúdo frequentes.
  - **Como funciona:** O cliente vincula a própria conta profissional (usa o *Motor 1: Meta Graph API*).
  - **Cobrança:** R$ 29,90/mês para realizar sorteios **ilimitados**. Como a API da Meta é grátis e quem arca com a banda é o próprio servidor do Facebook, a nossa margem de lucro na mensalidade é absurda (~98%).

- **Tier Gratuito (Isca de Marketing):** Liberado apenas para quem fizer Login (Motor 1) e limitado a posts muito pequenos (ex: 300 comentários). Vai ter marca d'água ("Sorteado no: InstaSorteios") para gerar tráfego orgânico e exibir banners de AdSense.

---

## 🔐 Arquitetura de Segurança (Blindagem Total)

> [!warning] Regra de Ouro
> **NENHUMA chave, token ou senha jamais deve aparecer no código-fonte (.py, .js) ou ser enviada ao GitHub.** A violação desta regra compromete todas as APIs (Apify, Mercado Pago, Meta) instantaneamente.

### 1. Gerenciamento de Variáveis de Ambiente (O Cofre de Chaves)
- Todas as chaves secretas vivem em um arquivo `.env` **local e jamais enviado ao GitHub**.
- No Railway (produção), as chaves são configuradas diretamente no painel como *Environment Variables*, sem passar por código.
- No repositório existe apenas um `.env.example` (esqueleto vazio) para orientar outros desenvolvedores.
- Biblioteca `python-dotenv` fará a leitura segura dessas variáveis em memória.

```
# Exemplo de .env.example (nunca preencher aqui!)
APIFY_TOKEN=""
MP_ACCESS_TOKEN=""
MP_WEBHOOK_SECRET=""
META_APP_SECRET=""
DATABASE_URL=""
JWT_SECRET_KEY=""
```

### 2. Proteção de Rotas (CORS — Firewall do Front-end)
- O **CORS Middleware** do FastAPI será configurado para que **apenas** o domínio do Front-end (Lovable/Railway) possa consumir a API Back-end.
- Qualquer tentativa de chamada de um domínio desconhecido será bloqueada antes de chegar à lógica do servidor.
- Em desenvolvimento local: `http://localhost:5173` autorizado. Em produção: apenas o domínio oficial do site.

### 3. Validação do Webhook do Mercado Pago (Anti-Fraude)
- O Mercado Pago envia uma **assinatura criptografada** (`x-signature`) em cada Webhook.
- Nosso servidor Python validará essa assinatura com o `MP_WEBHOOK_SECRET` antes de liberar qualquer sorteio.
- Sem assinatura válida = Requisição descartada silenciosamente. Isso bloqueia tentativas de "enganar" o servidor com um pedido HTTP falso de "pagamento aprovado".

### 4. Autenticação de Usuários (JWT Tokens)
- Usuários do **Plano PRO** (Mensalidade) receberão um **JWT (JSON Web Token)** assinado na hora do Login com Facebook.
- Cada requisição autenticada do Front-end enviará este token no cabeçalho `Authorization: Bearer <token>`.
- O servidor valida o token em cada chamada, verificando identidade e plano ativo sem precisar consultar o banco a toda hora.
- Tokens têm prazo de expiração configurável (ex: 24h), forçando re-autenticação periódica.

### 5. Rate Limiting (Proteção Anti-Abuso e Anti-Bot)
- **Limite de Sondagens por IP:** Máximo de 5 sondagens de post por hora por endereço de IP.
- **Limite de Tentativas de Pagamento:** Máximo de 3 tentativas de geração de Pix por sessão (evita flood de QR Codes falsos no Mercado Pago).
- Implementado via biblioteca `slowapi` no FastAPI, sem necessidade de infraestrutura extra.

### 6. Proteção do Banco de Dados (PostgreSQL)
- O PostgreSQL no Railway **nunca é exposto diretamente** ao Front-end. Toda comunicação passa pelo FastAPI.
- A `DATABASE_URL` (string de conexão com senha) só existe como variável de ambiente no Railway.
- Senhas dos usuários (se houver cadastro próprio) armazenadas com hash **bcrypt** — nunca em texto plano.
- Backups automáticos configurados no Railway para prevenir perda de dados de assinaturas e histórico de sorteios.

### 7. Proteção do Front-end (Lovable/GitHub)
- O código-fonte do Front-end no GitHub **jamais** conterá chaves de API.
- O Front-end só conhecerá a URL pública do nosso Back-end (Railway). Todas as chamadas para Apify e Mercado Pago partem do servidor Python, nunca do navegador do cliente.
- Variáveis de ambiente no Lovable/Vite prefixadas com `VITE_` (somente as seguras de expor: URL do Back-end).

### 8. Regras de Deployment (Proteção no Pipeline)
- `.gitignore` configurado para barrar: `.env`, `__pycache__/`, `.venv/`, `*.pyc`, logs e arquivos de IDE.
- Branch `main` = Produção. Qualquer commit direto em `main` proibido. Todo código passa por Pull Request.
- O Railway faz o deploy automático somente após o código passar nos testes (CI/CD).

---

## ⚙️ Implementação Real (Progresso em 24/04/2026)

> [!success] Back-end no Ar!
> API online e respondendo em: **https://web-production-a3e20b.up.railway.app**
> Swagger disponível em: `https://web-production-a3e20b.up.railway.app/docs`

### 🔗 Repositórios GitHub
- **Back-end:** `https://github.com/ismaelsantos0/sorteio-backend`
- **Front-end:** `https://github.com/ismaelsantos0/sorteio-r-pido`

### 📁 Estrutura de Pastas do Back-end (`C:\Projetos\sorteio-backend`)
```
sorteio-backend/
├── main.py                    ← App FastAPI (CORS, Rate Limit, Lifespan DB)
├── Procfile                   ← Comando de start para o Railway
├── requirements.txt           ← Dependências Python (compatível com Python 3.13)
├── .env.example               ← Modelo de variáveis (sem valores)
├── .gitignore
├── core/
│   ├── config.py              ← Porteiro de chaves (pydantic-settings)
│   └── security.py            ← JWT: criar e validar tokens (PyJWT)
├── database/
│   ├── models.py              ← Tabelas: usuarios, assinaturas, sorteios, transacoes
│   └── connection.py          ← Engine async PostgreSQL + init_db()
├── services/
│   ├── apify_service.py       ← Sondagem + Raspagem de comentários
│   ├── payment_service.py     ← Pix + Validação de Webhook anti-fraude
│   └── sorteio_service.py     ← Algoritmo de sorteio com filtros
└── api/routes/
    ├── auth.py                ← POST /api/auth/login
    ├── scrape.py              ← POST /api/scrape/sondagem
    ├── payment.py             ← POST /api/payment/checkout | /webhook | /status
    └── sorteio.py             ← POST /api/sorteio/executar
```

### 🗄️ Banco de Dados (PostgreSQL)
| Tabela | Função |
|---|---|
| `usuarios` | Perfis cadastrados via Facebook Login |
| `assinaturas` | Controle do Plano PRO (status + ID Mercado Pago) |
| `sorteios` | Histórico de sorteios com vencedor e filtros usados |
| `transacoes` | Cada Pix gerado e seu status (pending/approved) |

### 🔑 Variáveis de Ambiente no Railway
| Variável | Status |
|---|---|
| `JWT_SECRET_KEY` | ✅ Configurada |
| `DATABASE_URL` | ✅ PostgreSQL Railway |
| `APIFY_TOKEN` | ✅ Configurada |
| `MP_ACCESS_TOKEN` | ✅ Configurada |
| `MP_PUBLIC_KEY` | ✅ Configurada |
| `META_APP_ID` | ✅ App: "SaaS Sorteios" |
| `META_APP_SECRET` | ✅ Configurada |
| `MP_WEBHOOK_URL` | ⚠️ Atualizar com URL real |
| `ALLOWED_ORIGINS` | ⚠️ Atualizar com URL do front-end |

---

## 📋 Lista de Tarefas (Roadmap de Execução)

> [!todo] Fase 1: Back-end (Python + FastAPI no Railway)
> - [x] Criar conta no Railway e inicializar novo projeto.
> - [x] Criar o repositório `sorteio-backend` no GitHub.
> - [x] Configurar estrutura de pastas: `main.py`, `core/config.py`, `api/routes/`, `database/`.
> - [x] Adicionar `.gitignore`, `requirements.txt` e `.env.example`.
> - [x] Configurar as variáveis de ambiente secretas no painel do Railway.
> - [x] Criar rota `/api/scrape/sondagem` (Motor 2 — sondagem via Apify).
> - [x] Criar rota `/api/payment/checkout` (gera QR Code Pix via Mercado Pago).
> - [x] Criar rota `/api/payment/webhook` (recebe e valida confirmação do MP).
> - [x] Criar rota `/api/sorteio/executar` (só após webhook aprovado).
> - [x] Criar rota `/api/auth/login` (Login Facebook → JWT).
> - [x] Criar modelos do banco (usuarios, assinaturas, sorteios, transacoes).
> - [x] Deploy no Railway — API respondendo em produção!

> [!todo] Fase 2: Front-end (Lovable → GitHub → Railway)
> - [x] Criar o projeto visual no **Lovable** (SorteioPro).
> - [x] Corrigir endpoints do `sorteioPro.ts` para apontar para o backend FastAPI real.
> - [ ] Fazer push do front-end para `ismaelsantos0/sorteio-r-pido`.
> - [ ] Conectar o repositório ao Railway para deploy automático.
> - [ ] Configurar variável `VITE_SORTEIOPRO_API_URL` no Railway.
> - [ ] Validar fluxo completo: Colar link → Sondagem → Checkout Pix → Webhook → Roleta → Sorteio.

> [!todo] Fase 3: Testes, Segurança e Lançamento
> - [ ] Atualizar `MP_WEBHOOK_URL` e `ALLOWED_ORIGINS` no Railway com URLs reais.
> - [ ] Testar fluxo completo do Pix (pagamento real de R$ 0,01 para validação).
> - [ ] Testar fluxo de assinatura PRO com Mercado Pago Preapproval.
> - [ ] Auditar o `.gitignore` e garantir que nenhuma chave foi para o GitHub.
> - [ ] Configurar domínio personalizado (ex: `sortiopro.com.br`).
> - [ ] Fazer o lançamento público 🚀

---
*Gerado por Antigravity. Parte do ecossistema de projetos.*
