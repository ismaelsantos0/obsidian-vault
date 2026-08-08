---
tags: [dashboard, moc, cultura]
---

# 🎵 Cultura e Hobbies (Second Brain)

Suas músicas, filmes, séries e interesses pessoais categorizados. Adicione ideias cruas no **Inbox** e a Inteligência Artificial classificará aqui.

---

## 🎧 Músicas e Bandas
```dataview
table criador as "Artista/Banda", rating as "Avaliação"
from "10_Dominio_Pessoal/03_Recursos/Cultura"
where tipo = "cultura" and categoria = "Música"
sort rating desc
```

## 🎬 Filmes e Séries
```dataview
table criador as "Diretor/Estúdio", rating as "Avaliação"
from "10_Dominio_Pessoal/03_Recursos/Cultura"
where tipo = "cultura" and (categoria = "Filme" or categoria = "Série")
sort rating desc
```

## 🎨 Hobbies & Outros
```dataview
table categoria as "Categoria", rating as "Avaliação"
from "10_Dominio_Pessoal/03_Recursos/Cultura"
where tipo = "cultura" and categoria != "Música" and categoria != "Filme" and categoria != "Série"
```
