---
titulo: "Agenda Clean - Agendamento Clinicas SaaS"
data_criacao: 2026-07-26
data_atualizacao: 2026-07-26
tags: [saas, agendamento, clinicas, whatsapp, react, fastapi]
status: 80% - integracao de instancias pendente
url_producao: https://agendaclean.up.railway.app
relacionado_a: ["[[API_WhatsApp]]", "[[Gateway]]", "[[Carreira e Transicao]]"]
---

# Agenda Clean - SaaS de Agendamento para Clinicas

Sistema de agendamento White-Label para clinicas com automacao nativa de WhatsApp. Possui landing page publica, portal do paciente e painel admin para a clinica.

Site: https://agendaclean.up.railway.app

## Stack Tecnologico

| Camada | Tecnologia |
|:---|:---|
| Frontend Web (Admin + Paciente) | React / TypeScript / Vite |
| Backend | FastAPI (Python) |
| Banco de Dados | PostgreSQL |
| Automacao WPP | [[API_WhatsApp]] - ConectaZap (Evolution API) |
| Pagamentos e Assinaturas | [[Gateway]] - Mercado Pago |
| Deploy | Railway |

## Tabela de Precos (Atual)

| Plano | Preco | Para quem | Diferenciais |
|-------|-------|-----------|--------------|
| Basico | R$ 49/mes | Profissional Independente | 1 Profissional, Agendamentos Ilimitados, Pagina de Agendamento, Suporte por Email |
| Profissional | R$ 99/mes | Clinicas em Crescimento (MAIS ESCOLHIDO) | Ate 5 Profissionais, Lembretes Automaticos WPP, Gestao de Faltas, Suporte Prioritario |
| Clinica | R$ 199/mes | Multiplas Unidades e Grandes Equipes | Profissionais Ilimitados, Multiplos Niveis de Acesso, Treinamento Exclusivo, Gerente de Conta |

## Paineis do Sistema

| Painel | Para quem | Funcionalidade |
|--------|-----------|----------------|
| Landing Page | Visitante | Apresentacao, planos e cadastro |
| Portal do Paciente | Cliente da clinica | Agendar, cancelar, ver historico |
| Painel Admin | Clinica | Gerir agenda, pacientes, profissionais, instancias WPP |

## Integracao com Gateway e ConectaZap

Ao assinar um plano, o [[Gateway]] processa o pagamento via Mercado Pago e libera o acesso. O sistema entao chama o [[API_WhatsApp]] (ConectaZap) e cria automaticamente as instancias de WhatsApp proporcionais ao plano contratado.

- Plano Basico: 1 instancia WPP
- Plano Profissional: instancias para ate 5 profissionais
- Plano Clinica: instancias ilimitadas

## Gargalo Atual (20% restante)

- [ ] Finalizar o fluxo de criacao automatica de instancias no momento do cadastro/assinatura
- [ ] Testes de estabilidade end-to-end (cadastro -> pagamento -> instancia WPP ativa)
- [ ] Preparar ambiente de demo para clinicas em vista
- [ ] Fechar primeiro cliente beta (clinicas ja identificadas)

## Projecao de Receita

| Cenario | Clientes | Plano | Receita/mes |
|---------|----------|-------|-------------|
| Conservador | 5 | Basico (R) | R$ 245 |
| Realista | 3 Basico + 2 Prof | Misto | R$ 345 |
| Otimista | 5 | Profissional (R) | R$ 495 |

[[Carreira e Transicao]] | [[API_WhatsApp]] | [[Gateway]]

## Levantamento de Mercado - Boa Vista/RR

> Status: PENDENTE - ainda nao foi feito o mapeamento das clinicas da cidade

### O que levantar por clinica:

| Campo | Exemplo |
|-------|---------|
| Nome da clinica | Clinica X |
| Especialidade | Odontologia, Estetica, Psicologia... |
| Porte estimado | 1 prof / 2-5 profs / grande |
| Contato (dono/gestor) | Nome + WhatsApp |
| Sistema atual | Papel, Google Agenda, outro app |
| Receptividade estimada | Alta / Media / Baixa |

- [ ] **ACAO PRIORITARIA:** Fazer levantamento das clinicas de Boa Vista - objetivo: mapear 20-30 clinicas com nome, especialidade, porte e contato
- [ ] Classificar por potencial de conversao e plano mais adequado
- [ ] Definir abordagem comercial (WhatsApp direto, visita presencial, indicacao)