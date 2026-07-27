---
titulo: "Annalicia Backend"
data_criacao: 2026-07-26
data_atualizacao: 2026-07-26
tags: [backend, fastapi, python, postgresql, api]
relacionado_a: ["[[Annalicia_App]]"]
---

# ⚙️ Annalicia Backend (annalicia-back)

Repositório backend da aplicação Annalicia, responsável por fornecer a API REST para a loja, gerenciar produtos, pedidos e autenticação.

## 🛠️ Tecnologias
- **Framework:** FastAPI (Python)
- **Banco de Dados:** PostgreSQL
- **Autenticação:** JWT (com exportação do campo `email` no `UserOut` corrigido na rota `/auth/me`)
- **Deploy:** Railway

## 📌 Contexto Recente
Conforme registros de Julho/2026:
- Foi corrigido o bug de autenticação onde o e-mail não retornava no frontend. A modelagem Pydantic foi atualizada para exportar o email corretamente.
- A estrutura de pastas foi alinhada com o frontend para garantir sincronia.

## 🔗 Links e Repositórios
- Repositório: `https://github.com/ismaelsantos0/annalicia-back`
- Integra-se com: `[[annalicia-front]]` (Frontend React)

---
[[Annalicia_App|⬅️ Voltar para Projeto Principal]]
