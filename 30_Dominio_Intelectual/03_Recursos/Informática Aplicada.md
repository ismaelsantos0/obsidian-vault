---
titulo: "Informática Aplicada (Padrão FCC Atual)"
data_criacao: 2026-04-17
dominio: 30_Dominio_Intelectual
sub_categoria: 03_Recursos
tipo: recurso
tags: [estudos, ale-rr, informatica, fcc]
relacionado_a: ["[[Concurso ALE-RR]]"]
---

# 💻 Informática Aplicada — Padrão FCC 2022-2026

> [!IMPORTANT]
> O padrão mudou. A FCC saiu do **Windows XP / Office 2003** e passou a cobrar **Microsoft 365, Google Workspace, segurança digital e nuvem**. Questões sobre "formatar disquete" não caem mais.

---

## 1. Conceitos Fundamentais de Hardware

| Componente | Função |
|:---|:---|
| **CPU (Processador)** | Unidade central de processamento. Executa instruções. |
| **RAM (Memória)** | Memória volátil de trabalho. Perde dados ao desligar. |
| **HD / SSD** | Armazenamento permanente. SSD é mais rápido que HD. |
| **GPU** | Processador de vídeo/gráficos. |
| **Placa-mãe** | Conecta todos os componentes. |
| **ROM / BIOS/UEFI** | Memória de inicialização do computador. |

**Tipos de memória:**
- **Volátil:** RAM — perde dados sem energia.
- **Não-volátil:** HD, SSD, Pendrive, ROM — mantém dados sem energia.

**Periféricos:**
- **Entrada:** Teclado, mouse, scanner, microfone, webcam.
- **Saída:** Monitor, impressora, caixas de som.
- **Entrada/Saída:** Pendrive, HD externo, touchscreen.

---

## 2. Sistemas Operacionais

### Windows 10/11 (Padrão atual FCC)
| Atalho | Função |
|:---:|:---|
| `Ctrl + C / V / X` | Copiar / Colar / Recortar |
| `Ctrl + Z` | Desfazer |
| `Ctrl + S` | Salvar |
| `Ctrl + P` | Imprimir |
| `Alt + F4` | Fechar janela/programa |
| `Alt + Tab` | Alternar entre janelas abertas |
| `Win + D` | Mostrar área de trabalho |
| `Win + L` | Bloquear sessão |
| `Win + E` | Abrir Explorador de Arquivos |
| `PrtScn` | Captura de tela (área de transferência) |
| `Win + Shift + S` | Recorte de tela customizado |
| `Ctrl + Alt + Del` | Segurança / Gerenciador de Tarefas |

> [!IMPORTANT]
> **Lixeira:** Arquivos deletados com `Delete` vão para a Lixeira (podem ser restaurados). Deletados com `Shift + Delete` são excluídos permanentemente (NÃO vão para a lixeira).

### Extensões de arquivo mais cobradas
| Extensão | Tipo |
|:---:|:---|
| `.docx` | Word (documento de texto) |
| `.xlsx` | Excel (planilha) |
| `.pptx` | PowerPoint (apresentação) |
| `.pdf` | Documento portátil (Adobe) |
| `.jpg / .png` | Imagem |
| `.mp3 / .wav` | Áudio |
| `.mp4 / .avi` | Vídeo |
| `.zip / .rar` | Arquivo compactado |
| `.exe` | Executável (programa) |

---

## 3. Microsoft 365 (Word, Excel, PowerPoint)

### Word
- **Modos de exibição:** Leitura, Layout de Impressão, Web, Estrutura de Tópicos.
- **Estilos e Formatação:** Negrito (`Ctrl+N`), Itálico (`Ctrl+I`), Sublinhado (`Ctrl+U`).
- **Parágrafo:** Alinhar à esquerda (`Ctrl+Q`), Centralizar (`Ctrl+E`), Direita (`Ctrl+G`), Justificar (`Ctrl+J`).
- **Mala Direta:** Recurso para enviar documentos personalizados em massa (cartas, etiquetas).
- **Controle de Alterações:** Rastreia edições feitas no documento para revisão.

### Excel
- **Célula** = interseção de linha e coluna. Ex: `A1`, `B3`.
- **Fórmulas** sempre começam com `=`
- **Funções essenciais:**

| Função | O que faz |
|:---|:---|
| `=SOMA(A1:A10)` | Soma o intervalo |
| `=MÉDIA(A1:A10)` | Calcula a média |
| `=MÁXIMO(A1:A10)` | Maior valor |
| `=MÍNIMO(A1:A10)` | Menor valor |
| `=CONT.NÚM(A1:A10)` | Conta células com número |
| `=SE(A1>10;"Sim";"Não")` | Condição lógica |
| `=PROCV(valor;tabela;col;0)` | Busca vertical |

- **Referência absoluta:** `$A$1` — não muda ao copiar a fórmula.
- **Referência relativa:** `A1` — muda ao copiar (padrão).
- **Filtro:** Dados → Filtrar. Permite exibir só linhas que atendem a um critério.
- **Congelar Painéis:** Exibição → Congelar Painéis. Fixa linhas/colunas na tela.

> [!IMPORTANT]
> **Pegadinha Excel FCC:** Ao arrastar uma fórmula pela alça de preenchimento, as referências relativas mudam automaticamente. `=A1+B1` se torna `=A2+B2` na linha seguinte.

### PowerPoint
- **Slide Mestre:** Define o layout padrão de todos os slides.
- **Transições:** Efeito entre slides.
- **Animações:** Efeito aplicado a elementos dentro de um slide.
- **Apresentador:** modo de tela cheia com notas visíveis só para o apresentador.

---

## 4. Google Workspace (cobrado desde 2022)

| Produto | Equivalente Office | Formato nativo |
|:---|:---|:---:|
| **Google Docs** | Word | `.gdoc` (exporta como .docx) |
| **Google Planilhas** | Excel | `.gsheet` (exporta como .xlsx) |
| **Google Apresentações** | PowerPoint | `.gslides` (exporta como .pptx) |
| **Google Drive** | OneDrive | Armazenamento em nuvem |
| **Gmail** | Outlook | E-mail |
| **Google Meet** | Teams | Videoconferência |
| **Google Forms** | Forms | Formulários e pesquisas |

**Vantagens do Google Workspace:**
- Edição **colaborativa em tempo real** (múltiplos usuários ao mesmo tempo).
- **Salva automaticamente** na nuvem (sem precisar de Ctrl+S).
- Histórico de versões automático.
- Acesso de qualquer dispositivo via navegador.

---

## 5. Internet, Navegador e E-mail

### Navegadores
| Atalho (Chrome/Edge) | Função |
|:---:|:---|
| `Ctrl + T` | Nova aba |
| `Ctrl + W` | Fechar aba |
| `Ctrl + N` | Nova janela |
| `Ctrl + Shift + N` | Nova janela anônima (privada) |
| `Ctrl + H` | Histórico |
| `Ctrl + D` | Favoritar a página |
| `F5 / Ctrl + R` | Recarregar página |
| `Ctrl + F` | Buscar na página |
| `Ctrl + L` | Ir para a barra de endereço |

**Conceitos importantes:**
- **URL (Uniform Resource Locator):** Endereço de uma página. Ex: `https://www.google.com`
- **HTTPS:** Protocolo seguro (cadeado na barra do navegador). Dados criptografados.
- **HTTP:** Protocolo sem criptografia. **Evitar** para dados sensíveis.
- **Cache:** Arquivos temporários guardados pelo navegador para agilizar o acesso.
- **Cookie:** Arquivo que guarda preferências e sessão do usuário no navegador.

### Protocolos de E-mail
| Protocolo | Função |
|:---:|:---|
| **SMTP** | **Envio** de e-mail |
| **POP3** | **Recebimento** — baixa e-mails para o dispositivo (remove do servidor) |
| **IMAP** | **Recebimento** — sincroniza e-mails no servidor (acesso em múltiplos dispositivos) |

> [!IMPORTANT]
> **Diferença POP3 vs IMAP:** POP3 baixa e apaga do servidor. IMAP mantém no servidor e sincroniza. A FCC adora essa distinção.

---

## 6. Segurança da Informação

### Princípios (CIA)
- **C**onfidencialidade — Só quem autorizado acessa.
- **I**ntegridade — Dado não foi alterado indevidamente.
- **D**isponibilidade — Sistema acessível quando necessário.

### Ameaças mais cobradas pela FCC
| Ameaça | O que é |
|:---|:---|
| **Vírus** | Código malicioso que se replica anexando-se a arquivos. Precisa de ação do usuário para se propagar. |
| **Worm** | Se propaga sozinho pela rede, sem precisar de arquivo hospedeiro. |
| **Trojan (Cavalo de Troia)** | Parece legítimo, mas abre backdoor para invasores. |
| **Ransomware** | Criptografa arquivos e exige resgate (ex: WannaCry). |
| **Phishing** | Golpe por e-mail/site falso para roubar credenciais. |
| **Spyware** | Monitora silenciosamente as atividades do usuário. |
| **Adware** | Exibe propagandas indesejadas. |
| **Rootkit** | Oculta a presença de malware no sistema. |

### Boas práticas de segurança
- **Antivírus:** Detecta e remove malware.
- **Firewall:** Controla o tráfego de rede (bloqueia conexões não autorizadas).
- **Backup:** Cópia de segurança dos dados. Regra **3-2-1**: 3 cópias, 2 mídias diferentes, 1 offsite.
- **Criptografia:** Transforma dados em código ilegível sem a chave.
- **Autenticação de dois fatores (2FA):** Senha + segundo fator (SMS, app, token).

---

## 7. Redes de Computadores

### Tipos de rede
| Sigla | Nome | Abrangência |
|:---:|:---|:---|
| **LAN** | Local Area Network | Local (escritório, casa) |
| **MAN** | Metropolitan Area Network | Cidade |
| **WAN** | Wide Area Network | País/mundo. A internet é uma WAN. |

### Dispositivos de rede
| Dispositivo | Função |
|:---|:---|
| **Roteador** | Direciona pacotes entre redes diferentes. Conecta a LAN à internet. |
| **Switch** | Conecta dispositivos dentro de uma mesma LAN. |
| **Modem** | Converte sinal da operadora em sinal de rede. |
| **Access Point** | Ponto de acesso Wi-Fi. |

### Conceitos cobrados
- **IP (Internet Protocol):** Endereço lógico do dispositivo na rede.
- **DNS:** Traduz nomes de domínio em endereços IP. (Ex: `google.com` → `142.250.x.x`)
- **VPN:** Cria túnel criptografado sobre internet pública. Usado para acesso remoto seguro.
- **Wi-Fi:** Rede sem fio. Padrão IEEE 802.11.

---

## 🧠 Active Recall Rápido

| Q: | R: |
|:---|:---|
| Atalho para janela anônima no Chrome? | `Ctrl + Shift + N` |
| Delete vs Shift+Delete? | Delete → Lixeira. Shift+Delete → exclusão permanente. |
| Diferença entre RAM e HD? | RAM: volátil (trabalho). HD: não-volátil (armazenamento). |
| Protocolo de envio de e-mail? | **SMTP** |
| Diferença POP3 e IMAP? | POP3 baixa e apaga do servidor. IMAP sincroniza no servidor. |
| O que é phishing? | Golpe por e-mail/site falso para roubar dados. |
| O que é ransomware? | Malware que criptografa arquivos e pede resgate. |
| HTTPS diferença para HTTP? | HTTPS é criptografado (seguro). HTTP não tem criptografia. |
| Referência absoluta no Excel? | `$A$1` — não muda ao copiar a fórmula. |
| Fórmula de soma no Excel? | `=SOMA(A1:A10)` |
| Google Docs salva automaticamente? | **Sim**, na nuvem, sem precisar do Ctrl+S. |
| Worm vs Vírus? | Vírus precisa de hospedeiro. Worm se propaga sozinho pela rede. |
