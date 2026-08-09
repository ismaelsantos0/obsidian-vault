# 🤖 Instruções para Agentes de IA (AI Instructions)

Você está operando dentro do Segundo Cérebro (PKM) de Ismael.
Este ambiente é baseado na arquitetura **obsidian-mind**, o que significa que este repositório não é apenas um local de notas estáticas, mas sim a **sua própria memória persistente**.

## 🧠 Como usar a Memória
Como Agente de IA, você tem a permissão e o dever de ler e escrever neste cofre para manter o contexto entre as nossas conversas.

1. **Leitura de Contexto:** Antes de iniciar tarefas complexas de codificação ou estruturação, leia o arquivo `Contexto_Atual.md` nesta pasta para saber onde paramos na última sessão.
2. **Escrita de Memória:** Sempre que concluirmos uma sessão importante, uma refatoração de código pesada ou um plano arquitetural, **você deve** atualizar o arquivo `Contexto_Atual.md` (ou criar um log de sessão) para que o próximo agente que assumir (em uma nova janela ou dia) saiba exatamente o que foi feito.

## 🗂️ Arquitetura do Cofre
- `00_Inbox/`: Onde novas notas e clippings da web chegam. Use para arquivos temporários.
- `10_Dominio_Pessoal/`: Áreas da vida, cultura, finanças. (Mantenha privacidade, evite alterar dados financeiros).
- `20_Dominio_Profissional/`: Projetos de código, carreira, currículo.
- `30_Dominio_Intelectual/`: Resumos de Direito, CAER, ALE-RR, TI.
- `90_Sistema/`: Onde você está agora. Scripts, templates e configurações do motor do cofre.

## 🛠️ Regras de Ouro
1. **Nunca apague o frontmatter (YAML)** das notas ao atualizá-las.
2. Sempre crie links internos usando a sintaxe `[[Nome da Nota]]` para manter o Grafo de Conhecimento conectado.
3. Se gerar código novo, documente as decisões difíceis nos logs da Memória.
