---
tipo: guia
titulo: "Como Publicar o Jardim Digital (Quartz)"
---

# 🪴 Guia Oficial: Publicando seu Cérebro na Web com Quartz

Para transformar suas anotações do Obsidian em um site interativo (Digital Garden) acessível ao público, utilizaremos o **Quartz**. 

Como esta configuração exige o `Node.js` (npm) e a criação de um repositório separado no seu GitHub, siga os passos abaixo no seu terminal (WSL, Git Bash ou CMD):

## Passo 1: Clonar e Preparar o Motor do Quartz
Abra o terminal em uma pasta fora do seu Obsidian (ex: `Documentos/Projetos`) e rode:

```bash
git clone https://github.com/jackyzha0/quartz.git meu-jardim-digital
cd meu-jardim-digital
npm i
```

## Passo 2: Sincronizar com o seu Obsidian Vault
Para que o Quartz leia as suas notas automaticamente, delete a pasta `content` vazia que veio nele e crie um **symlink** (atalho simbólico) para o seu vault real, ou configure como submódulo:

**No Windows (CMD como Administrador):**
```cmd
rmdir /s /q content
mklink /D content "C:\Users\ismae\OneDrive\Documentos\OBSIDIAN"
```
*(Nota: Lembre-se de configurar o `quartz.config.ts` na pasta do Quartz para ignorar diretórios privados como `00_Inbox` se não quiser publicá-los).*

## Passo 3: Testar Localmente
```bash
npx quartz build --serve
```
Acesse `http://localhost:8080` no seu navegador. Você verá o seu site funcionando perfeitamente!

## Passo 4: Publicar no GitHub (Grátis)
1. Crie um repositório vazio no GitHub chamado `meu-jardim-digital`.
2. No seu terminal, limpe o histórico velho e envie para o seu novo repositório:
```bash
rm -rf .git
git init
git add .
git commit -m "Initial Quartz setup"
git remote add origin https://github.com/ismaelsantos0/meu-jardim-digital.git
npx quartz sync
```

Daqui pra frente, sempre que quiser atualizar seu site com notas novas, basta abrir o terminal do Quartz e rodar `npx quartz sync`. A automação em nuvem fará o resto!
