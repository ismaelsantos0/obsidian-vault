---
titulo: "Sistema de Passagem de Livro Digital — SMTRAN"
status: congelado
prioridade: baixa (até 28/06/2026)
tipo: projeto
tags: [smtran, governo, assinatura-gov, nodejs, react, postgresql]
relacionado_a: ["[[RR Smart Soluções]]"]
---

# 🚓 SMTRAN — Sistema de Passagem de Livro Digital

> [!CAUTION]
> **PROJETO CONGELADO ATÉ 28/06/2026**
> Este é um projeto de alta complexidade (integração Gov.br, LGPD). Foco total na ALE-RR no momento. Registro realizado para execução futura.

## 📝 Resumo do Projeto
Substituição dos livros físicos de passagem de turno da SMTRAN por um sistema digital autenticado via **Assinatura Gov.br**, garantindo integridade, padronização e busca eficiente de ocorrências.

---

## 🏗️ 1. Especificação Técnica (SMTRAN)
*   **Problema:** Relatos manuais em papel são difíceis de auditar e perdem a integridade com o tempo.
*   **Solução:** WebApp com login Gov.br para assinatura digital das ocorrências do dia.
*   **Timeline:** 3 meses (estimado).
*   **Orçamento:** R$ 17k - 30k (estimado).

## 🎨 2. Fluxo Visual e Jornada
1.  **Operador:** Cria ocorrência → Insere fotos/dados → Assina com Gov.br.
2.  **Supervisor:** Revisa as ocorrências do turno → Assina digitalmente o fechamento do livro.
3.  **Gerente:** Consulta histórico → Exporta relatórios PDF assinados.

## 🛠️ 3. Stack Tecnológica (MVP)
*   **Backend:** Node.js + Express / NestJS.
*   **Frontend:** React (Painel Web).
*   **Banco de Dados:** PostgreSQL (Histórico de logs e assinaturas).
*   **Integração:** API Gov.br (Assinador Digital).

## 🗄️ 4. Modelagem de Dados (Core)
*   **Users:** ID, CPF, Nome, Cargo, Permissão.
*   **Occurrences:** ID, User_ID, Descrição, Data/Hora, Status.
*   **Attachments:** ID, Occurrence_ID, S3_Link (Fotos/Docs).
*   **Signatures:** ID, Occurrence_ID, Signature_Hash, Timestamp.

## ✅ 5. Checklist de Implementação
- [ ] Configuração do Ambiente (Docker + Repo)
- [ ] Integração OAuth2 Gov.br
- [ ] Desenvolvimento do CRUD de Ocorrências
- [ ] Módulo de Assinatura via API de Assinatura Eletrônica (ITI/Gov.br)
- [ ] Exportador de PDF com Carimbo de Tempo

---

## 🎯 PRÓXIMOS PASSOS (PÓS-CONCURSO)
1. Apresentação da Especificação para a SMTRAN.
2. Definição do time de desenvolvimento.
3. Setup do ambiente de integração Gov.br.

---
[[Ismael Oliveira dos Santos|⬅️ Perfil]] | [[RR Smart Soluções|🏢 RR Smart]]
