# 00 - Master Roadmap (Projeto Tinta)

Este documento é o guia definitivo de fases do desenvolvimento do Projeto Tinta.

## Fase 0: Missão de Descoberta (Checklist)
Antes de escrever código, valide estas informações no cliente:
- [ ] **Qual a máquina dosadora?** (Ex: Corob, Fast&Fluid, Santint? Usa cabo Serial ou USB?).
- [ ] **Como é o fluxo de vendas atual?** (O tintômetro é separado do caixa?).
- [ ] **A loja usa espectrofotômetro?** (Copiam cores ou só usam o leque de fábrica?).
- [ ] **Como o corante é estocado?** (Existe base de dados atual ou desperdiçam?).

## Fase 1: O "Sistema Base" (Core)
Desenvolver a fundação do ERP:
- Banco de Dados Central (PostgreSQL).
- Autenticação e Autorização (RBAC).
- Configurações da Empresa e Colaboradores.
*(Sem código de vendas ou tintas nesta fase).*

## Fase 2: Módulo PDV e Estoque Básico
Plugar o primeiro módulo no Core:
- Tela de Frente de Caixa rápida.
- Leitor de código de barras.
- Estoque de latas e bases (Galões, etc).

## Fase 3: Módulo Tintometria (Versão Catálogo)
- Importar as fórmulas de fábrica (CSV) para o banco de dados.
- Lojista pesquisa "Azul Oceano" no PDV e o sistema exibe a receita.
- **O Pulo do Gato (BOM):** Dar baixa automática na lata base e nos ml de corantes no Estoque.
*(A máquina física ainda é operada manualmente pelo lojista).*

## Fase 4: Módulo Tintometria (Integração de Hardware)
- Conectar o cabo na máquina.
- Usar a porta Serial do PC para enviar as ordens diretas para a máquina pingar a tinta.
