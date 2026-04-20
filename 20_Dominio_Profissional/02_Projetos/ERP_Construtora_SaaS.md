---
titulo: "ERP para Construtoras (SaaS Modelo Single-Tenant)"
status: congelado
prioridade: baixa (até 28/06/2026)
tipo: projeto
tags: [saas, erp, construtora, python, fast-api, next-js]
relacionado_a: ["[[RR Smart Soluções]]"]
---

# 🏗️ ERP para Construtoras — SaaS Core

> [!CAUTION]
> **PROJETO CONGELADO ATÉ 28/06/2026**
> Prioridade absoluta: Aprovação ALE-RR. Esta ideia foi registrada para execução pós-concurso.

## 📋 1. Requisitos Funcionais (Core)
*   **Gestão de Obras:** Cadastro, medições e acompanhamento físico.
*   **Suprimentos/Almoxarifado:** Catálogo, estoque mínimo e movimentação.
*   **Financeiro Base:** Fluxo de caixa amarrado ao cronograma.
*   **Gestão de Pessoal:** Ponto e produtividade em campo.
*   **Motor de Webhooks:** Emissão de alertas (obra criada, NF recebida, estoque crítico) para automações externas via Make.com.

## 🔑 2. Arquitetura de Permissões
*   **Admins:** Controle total (configurações, exclusão, edição).
*   **Auditores/Operadores:** Acesso restrito (baixa de material, registro de ponto), sem visão gerencial.

## 🚀 3. Infraestrutura e Deploy
*   **Deploy Automatizado:** Docker + Railway (ambiente clonado por cliente).
*   **Canteiro Offline:** Frontend com cache para áreas sem sinal e sincronização posterior.
*   **Integridade Sugerida:** Busca obrigatória por IDs fixos (PK) para evitar falhas de cálculo/descrição.

## 🛠️ 4. Stack Tecnológico
| Camada | Tecnologia |
|:---|:---|
| **Backend** | Python (FastAPI ou Django) |
| **Frontend Web** | Next.js / React (Painel ADM) |
| **Frontend Mobile** | React Native (App Campo) |
| **Banco de Dados** | PostgreSQL (Instância única por cliente) |
| **Automação** | Webhooks + Make.com (Telegram/Relatórios) |

## 🗄️ 5. Modelagem do Banco (Schema)
*   **Users:** `id (PK)`, `nome`, `email`, `role`.
*   **Projects:** `id (PK)`, `nome_obra`, `status`, `orcamento_base`.
*   **Materials:** `id (PK)`, `codigo_interno`, `nome`, `unidade`.
*   **Inventory:** `id (PK)`, `project_id (FK)`, `material_id (FK)`, `quantidade`.
*   **Finance:** `id (PK)`, `project_id (FK)`, `valor`, `categoria`, `status_pagamento`.

## 📝 6. Próximos Passos (Pós-ALE-RR)
1.  Documentar API via Swagger/OpenAPI.
2.  Mapear lógica "Core" vs "Custom" (Make.com).
3.  Diagrama de Classe e Relacionamento.

---
[[Ismael Oliveira dos Santos|⬅️ Voltar para Perfil]] | [[RR Smart Soluções|🏢 RR Smart Soluções]]
