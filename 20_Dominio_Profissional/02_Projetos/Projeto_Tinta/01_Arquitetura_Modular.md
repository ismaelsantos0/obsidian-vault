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

## 3. A Stack Tecnológica Definitiva (Otimizada para Hardware Básico)
O sistema deve rodar perfeitamente como um arquivo `.exe` nativo em máquinas modestas (ex: Intel i3 antigo com 8GB de RAM), sem engasgos.

- **Interface Desktop (Frontend):** `Tauri` (Motor em Rust) + `React`.
  - *Motivo:* Ao contrário do Electron, o Tauri não embute um navegador pesado. Ele usa o próprio visualizador do Windows (WebView2), reduzindo o consumo de memória para incríveis ~20MB. O visual será de um aplicativo React lindíssimo, responsivo e ultra-fluido.
- **Backend (O Cérebro Sidecar):** Processo em `Python` empacotado.
  - *Motivo:* A pesada matemática das tintas (fórmula de Kubelka-Munk) será feita pelo Python (Scipy). O Tauri vai gerenciar o Python como um processo "Sidecar", mantendo-o dormente para economizar CPU, acordando-o apenas quando o módulo de tintometria precisar calcular fórmulas.
- **Armazenamento e Cloud Backup (Offline-First):**
  - **Banco Local:** O sistema principal rodará 100% em `SQLite` salvo localmente na máquina, garantindo velocidade instantânea e vendas sem internet.
  - **Backup na Nuvem:** Uma rotina programada (CRON job) em segundo plano vai enviar/sincronizar todas as notas e movimentações de estoque do dia para um servidor online (ex: PostgreSQL no `Supabase` ou AWS) toda madrugada.
