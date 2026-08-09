---
tipo: guia
titulo: Sincronização Mobile com Obsidian Git
---

# 📱 Guia de Sincronização Mobile: Obsidian Git

Se você não achou o "Obsidian Git" pesquisando na loja de aplicativos (Play Store/App Store), é porque ele **não é um app separado**. Ele é um **Plugin Comunitário** que você instala por dentro do próprio Obsidian!

Siga este passo a passo exatamente na ordem para ter seu cofre do GitHub rodando no celular:

## Passo 1: Configurar a Segurança no GitHub (PC)
O celular não tem como fazer login com usuário e senha no Git, então precisamos de um "Token" especial.
1. No seu PC, abra o navegador e vá no GitHub: `Settings` > `Developer settings` > `Personal access tokens (classic)`.
2. Clique em **Generate new token (classic)**.
3. Dê um nome (ex: `Obsidian Celular`), coloque a validade para "No expiration" (sem validade) e marque a caixinha **`repo`** (Full control of private repositories).
4. Clique em gerar e **COPIE o código gigante que vai aparecer**. Salve ele num bloco de notas seguro (ou mande para você mesmo no WhatsApp/Telegram), pois vamos usar no celular.

## Passo 2: Preparar o Terreno no Celular
1. Abra o app oficial do **Obsidian** no celular.
2. Crie um Vault (cofre) completamente vazio chamado `OBSIDIAN`.
3. Vá nas **Configurações** (ícone de engrenagem) > **Plugins Comunitários**.
4. Desative o "Modo de Segurança" (Turn off Safe Mode).
5. Clique em **Procurar (Browse)** e digite `Obsidian Git` (O autor é o *Vinzent* ou *DenisOgr*).
6. Clique em **Instalar** e depois em **Ativar**.

## Passo 3: Baixar seu Cérebro para o Celular
Ainda no celular, com o plugin ativado:
1. Puxe a tela de cima para baixo no Obsidian (ou abra a Paleta de Comandos).
2. Digite: `Obsidian Git: Clone an existing remote repo`.
3. Ele vai pedir a URL do repositório. Digite a URL do seu GitHub: `https://github.com/ismaelsantos0/obsidian-vault.git`
4. Quando ele pedir **Autenticação**, coloque o seu nome de usuário (`ismaelsantos0`) e na senha, **COLE O TOKEN GIGANTE** que você gerou no Passo 1.
5. Ele vai perguntar se deseja reiniciar o Obsidian ou clonar em uma pasta. Pode confirmar!

## Pronto! 🎉
Sempre que você abrir o Obsidian no celular agora, o plugin vai rodar um "Pull" automático e baixar tudo o que fizemos no PC (inclusive a Biblioteca de Filosofia e as notas da ALE-RR). E quando fechar o app, ele faz um "Push" automático das coisas que você digitou deitado no sofá!
