---
titulo: "ConectaZap - API WhatsApp SaaS"
data_criacao: 2026-07-09
data_atualizacao: 2026-07-26
tags: [saas, whatsapp, evolution-api, docker, railway, nodejs]
status: funcional - bug fixes e seguranca pendentes
url_producao: https://conectazap.up.railway.app
relacionado_a: ["[[Agendamento_Clinicas]]", "[[Gateway]]", "[[Carreira e Transicao]]"]
---

# ConectaZap - API WhatsApp SaaS

Plataforma SaaS para gerenciamento de multiplas instancias de WhatsApp via Evolution API. Hospedado em producao. Atualmente em uso proprio como infraestrutura dos outros sistemas.

Site: https://conectazap.up.railway.app

## Stack Tecnologico

| Camada | Tecnologia |
|:---|:---|
| Core | Evolution API + Baileys |
| Backend | Node.js / TypeScript |
| Banco de Dados | PostgreSQL + Redis |
| Auth | JWT (tokens unicos por cliente) |
| Deploy | Railway |

## Tabela de Precos (Atual)

| Plano | Preco | Instancias | Creditos IA | Obs |
|-------|-------|------------|-------------|-----|
| Starter (Free) | R$ 0/mes | 1 | 30/mes | Ideal para testes |
| Pro | R$ 147/mes | 3 | 1.000/mes | Mais escolhido |
| Agency | R$ 347/mes | 10 | 5.000/mes | Para agencias e CRMs |
| Enterprise | R$ 997/mes | Ilimitadas | Ilimitados | Servidor isolado |

Creditos avulsos: R$ 47 (+1.000) | R$ 197 (+5.000)

## Funcionalidades

- Instancias ilimitadas (conforme plano)
- Webhooks em tempo real (mensagens, leitura, conexao)
- API REST documentada (Node, Python, PHP, Typebot)
- Envio de texto, imagem, video, documento e audio
- Tokens JWT unicos por cliente (Global API Key nunca exposta)

## Status Atual

- [x] Hospedado e funcional em producao
- [x] Sistema de planos e cobranca configurado
- [ ] Correcao de bugs identificados em uso proprio
- [ ] Validacoes de seguranca (rate limiting, autenticacao robusta)
- [ ] Abertura para clientes externos (pos bugs e seguranca)

## Repositorio

- Local: C:\Users\ismae\OneDrive\Documentos\API-WHATSAPP
- Remoto: https://github.com/ismaelsantos0/API-WHATSAPP

[[Agendamento_Clinicas]] | [[Gateway]] | [[Carreira e Transicao]]