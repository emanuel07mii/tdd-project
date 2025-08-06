# 🛒 API Store

Este projeto foi desenvolvido como parte do bootcamp da [DIO (Digital Innovation One)](https://www.dio.me/), com o objetivo de praticar o desenvolvimento de uma API utilizando o framework **FastAPI** seguindo os princípios do **TDD (Test-Driven Development)**.

## 🚀 Objetivos do projeto

Essa aplicação tem como objetivo principal trazer conhecimentos sobre o TDD, na prática, desenvolvendo uma API com o Framework Python, FastAPI. Utilizando o banco de dados MongoDB, para validações o Pydantic, para os testes Pytest e entre outras bibliotecas.

- Aplicar TDD na criação de uma API.
- Utilizar FastAPI para estruturação de rotas e validação de dados.
- Criar testes automatizados para garantir a estabilidade e a qualidade do código.
- Praticar boas práticas de desenvolvimento de APIs RESTful.
- Implementar melhorias e desafios adicionais para expandir a aplicação.

## 📖 O que é?
Uma aplicação que:
- tem fins educativos;
- permite o aprendizado prático sobre TDD com FastAPI + Pytest;

## 📒 O que não é?
Uma aplicação que:
- se comunica com apps externas;


## ⚙️ Solução Proposta
Desenvolvimento de uma aplicação simples a partir do TDD, que permite entender como criar tests com o `pytest`. Construindo testes de Schemas, Usecases e Controllers (teste de integração).


## 🧩 Desafio
- Create
    - Mapear uma exceção, caso dê algum erro de inserção e capturar na controller
- Update
    - Modifique o método de patch para retornar uma exceção de Not Found, quando o dado não for encontrado
    - a exceção deve ser tratada na controller, pra ser retornada uma mensagem amigável pro usuário
    - ao alterar um dado, a data de updated_at deve corresponder ao time atual, permitir modificar updated_at também
- Filtros
    - cadastre produtos com preços diferentes
    - aplique um filtro de preço, assim: (price > 5000 and price < 8000)


## 📚 Referência

Repositório base fornecido pela DIO:
🔗 [digitalinnovationone/store_api](https://github.com/digitalinnovationone/store_api)

---
