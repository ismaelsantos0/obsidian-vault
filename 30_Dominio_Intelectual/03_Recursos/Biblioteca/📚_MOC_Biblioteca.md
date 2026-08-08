---
tags: [dashboard, moc, biblioteca]
---

# 📚 Biblioteca (Second Brain)

Aqui estão todos os seus resumos de livros e leituras, auto-organizados pelas metadados. Jogue os novos livros no **Inbox** que a Inteligência Artificial arquivará aqui!

---

## 📖 Lendo Atualmente
```dataview
table autor as "Autor", genero as "Gênero", data_leitura as "Data"
from "30_Dominio_Intelectual/03_Recursos/Biblioteca"
where status = "lendo" and tipo = "livro"
```

## ⭐ Favoritos (5 Estrelas)
```dataview
table autor as "Autor", genero as "Gênero"
from "30_Dominio_Intelectual/03_Recursos/Biblioteca"
where rating = 5 and tipo = "livro"
```

## 📚 Estante Completa
```dataview
table autor as "Autor", rating as "Avaliação", status as "Status"
from "30_Dominio_Intelectual/03_Recursos/Biblioteca"
where tipo = "livro"
sort rating desc
```
