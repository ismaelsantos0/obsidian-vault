# 01 - Arquitetura Modular (O Monolito Modular)

O Projeto Tinta será desenhado com o padrão **Modular Monolith** (Arquitetura baseada em Plugins), idêntico a gigantes como Odoo e SAP. Se um módulo falhar, o restante da loja continua operando.

## 1. O "Sistema Base" (Core)
É a fundação do software. Não possui regras de tintas, apenas regras de negócios globais.
- **Segurança:** Autenticação (Login, Tokens JWT).
- **RBAC (Role-Based Access Control):** Gestão de níveis (Gerente, Caixa, Colorista).
- **Multi-empresa:** Configurações globais, CNPJ, Filiais.
- **Auditoria:** Gravação de logs de segurança ("Quem fez o quê").

## 2. Os Módulos Independentes (Plugins)
Eles herdam a segurança do Sistema Base.

### 📦 Módulo Estoque
- Introduz o conceito de **BOM (Bill of Materials)**. 
- A Tinta customizada não é um produto simples, é um produto fabricado que consome: `1 Lata de Base + 12ml Corante A + 4ml Corante B`.

### 🛒 Módulo PDV (Frente de Caixa)
- Inteface web empacotada em Desktop.
- Foca apenas na velocidade de passar itens e emitir nota (NFC-e).

### 🎨 Módulo Tintômetro
- Conecta-se ao Módulo Estoque para checar se há corante suficiente no cilindro da máquina antes de mandar a ordem.

## 3. A Stack Tecnológica Recomendada
- **Backend (O Cérebro):** Python com o framework `FastAPI`. 
  - *Motivo:* Python lidera tanto no desenvolvimento ágil de APIs (para o PDV) quanto na matemática científica pesada (Scipy) necessária para a mistura de tintas.
- **Frontend (A Interface):** `React` empacotado via `Tauri` ou `Electron`.
  - *Motivo:* Lojas físicas precisam de aplicativos de balcão (Desktop) para poder conversar localmente com impressoras de recibo e máquinas via cabos COM/USB, sem depender 100% da internet.
- **Banco de Dados:** `PostgreSQL` para a nuvem, com *cache* local (`SQLite`) nas lojas para operações offline críticas.
