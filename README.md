# Tecnologias Web - 2026.2 - Projeto 1B

Link para a plataforma: https://tecweb-2026-2-projeto1b-ypek.onrender.com


docker run --name pg-docker \
-e POSTGRES_PASSWORD=escolhaumasenha \
-d \
-p 5432:5432 \
-v $HOME/docker/volumes/postgres:/var/lib/postgresql \
postgres