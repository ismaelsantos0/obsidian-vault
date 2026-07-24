# 02 - Bases de Código Aberto (Open Source)

Não começaremos o código do zero. Utilizaremos peças consolidadas da comunidade Open Source para montar a base do Sistema e a parte matemática do Tintômetro.

## 1. Bases para o Sistema Base (Core) e ERP
Repositórios no GitHub perfeitos para servirem de esqueleto:

- **Odoo (Python):** O maior ERP modular open source do mundo. Tem o recurso de "Bill of Materials" nativo perfeito para tintas. (Curva de aprendizado altíssima).
- **ERPNext (Python):** Concorrente do Odoo, excelente gestão de estoque e PDV nativo.
- **ZatoBox:** PDV de código aberto feito sob medida para a nossa stack preferida (`FastAPI` + `React/Next.js`). Ideal se quisermos total controle sobre o código e um visual mais moderno.
- **Full-Stack-FastAPI-Template:** O template oficial da comunidade FastAPI. Vem apenas com banco de dados, login e segurança do CORE prontos. O resto nós construiríamos do zero.

## 2. Bases para o Módulo Tintométrico (Cálculo Físico de Cores)
Se evoluirmos para um software que inventa cores (e não apenas lê receitas estáticas), usaremos estas "peças soltas" do GitHub:

- **`RNVizion/rnv-color-mixer`:** Um app desktop em Python (PyQt6) feito especificamente para misturar tintas fisicamente. Ótima inspiração visual de paletas.
- **`colour-science/colour`:** A biblioteca Python padrão-ouro mundial para ciência da cor. Tem todas as fórmulas para achar distâncias de cores usando o espaço `CIELAB` e o cálculo de erro `Delta E`.
- **`lwander/open-km`:** Implementação direta da teoria de *Kubelka-Munk*, que é a matemática (Física Óptica) real usada em máquinas de tingir para calcular o Espalhamento e Absorção da luz em pigmentos opacos.
