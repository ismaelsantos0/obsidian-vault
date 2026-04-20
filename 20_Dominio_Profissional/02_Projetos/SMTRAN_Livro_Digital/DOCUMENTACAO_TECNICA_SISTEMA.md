# 🛠️ Documentação Técnica do Sistema

## 🧱 Arquitetura
Client-Server: React (Frontend) ↔ Node.js (Backend) ↔ PostgreSQL (DB).

## 🗄️ Modelos de Dados (SQL)
- **Tabela `occorrences`**: `id`, `user_id`, `content`, `timestamp`, `signed`.
- **Tabela `signatures`**: `id`, `occurrence_id`, `gov_token`, `signed_data`.

## 🔌 Principais Endpoints
- `POST /auth/govbr`: Autenticação e Callback.
- `GET /book/current`: Livro de hoje.
- `POST /occurrence/new`: Registro com multipart/form-data.
- `POST /book/sign`: Gatilho de assinatura eletrônica.
