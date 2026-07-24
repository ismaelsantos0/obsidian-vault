# 03 - Comunicação com Hardware

O maior gargalo de um software para o varejo de tintas é conversar com o mundo físico. O Módulo de Tintometria será totalmente isolado para não travar o Sistema Base em caso de pane de hardware.

## 1. Como Conversar com a Máquina Dosadora
As máquinas que injetam os corantes (Corob, Fast&Fluid, Santint, Hero) se conectam ao computador geralmente por cabo **Serial (RS-232)** ou USB emulado como COM port.

- **A Biblioteca:** Usaremos a biblioteca `pyserial` no Python para enviar blocos de bytes pelo cabo.
- **O Gargalo:** O protocolo de comunicação (a "linguagem" da máquina). As fabricantes não divulgam isso abertamente.
- **Solução A:** Entrar em contato com o suporte da fabricante no Brasil e solicitar o manual do protocolo/API do desenvolvedor.
- **Solução B:** Rodar um software analisador de portas ("Serial Port Sniffer") enquanto a máquina roda o software oficial dela para interceptar os pacotes de dados e fazer engenharia reversa.

## 2. Como Conversar com a Frente de Caixa
- **Impressoras Térmicas (Recibo):** Bibliotecas como `python-escpos` são perfeitas para imprimir os recibos e os cupons QR da NFC-e diretamente via rede (IP) ou cabo.
- **Leitores de Código de Barras:** São os equipamentos mais simples. Eles emulam um teclado. Quando bipam a lata, apenas injetam um texto na tela do PDV (ex: `789123456789`) seguido de um 'Enter'. O Frontend (React) só precisa de um "Event Listener" oculto escutando números sendo digitados em rápida sucessão para colocar a lata no carrinho sem que o vendedor precise clicar no campo de busca.
