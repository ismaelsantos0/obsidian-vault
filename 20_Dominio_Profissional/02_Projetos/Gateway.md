---
titulo: "Gateway de Assinaturas"
data_criacao: 2026-07-17
data_atualizacao: 2026-07-26
tags: [gateway, saas, mercadopago, assinaturas, financeiro, nodejs]
status: funcional - uso proprio
relacionado_a: ["[[API_WhatsApp]]", "[[Agendamento_Clinicas]]", "[[Carreira e Transicao]]"]
---

# Gateway de Assinaturas

Hub central de gerenciamento de assinaturas e pagamentos de todos os SaaS. Conectado ao Mercado Pago e oferece um dashboard que mostra de onde esta chegando cada receita.

## Visao Geral

O Gateway e o sistema financeiro dos sistemas. Quando um cliente do [[Agendamento_Clinicas]] paga uma assinatura, o fluxo passa pelo Gateway que processa, registra e libera o acesso. O dashboard consolida toda a receita por produto/plano.

## Stack Tecnologico

| Camada | Tecnologia |
|:---|:---|
| Backend | Node.js / Prisma ORM |
| Banco de Dados | PostgreSQL |
| Pagamentos | Mercado Pago (PIX + Cartao) |
| Deploy | Railway |

## Funcionalidades

- Gerenciamento de assinaturas por produto (Agendamento, API WPP, etc.)
- Integracao com Mercado Pago para cobranca automatica
- Dashboard consolidado mostrando receita por origem
- Webhooks de confirmacao de pagamento para os SaaS

## Status Atual

- [x] Funcional e hospedado
- [x] Integracao com Mercado Pago ativa
- [x] Dashboard de receita operacional
- [ ] Conectado formalmente ao [[Agendamento_Clinicas]] para liberacao automatica de planos

## Repositorio

- Local: C:\Users\ismae\OneDrive\Documentos\GATEWAY
- Remoto: https://github.com/ismaelsantos0/GATEWAY

[[API_WhatsApp]] | [[Agendamento_Clinicas]] | [[Carreira e Transicao]]