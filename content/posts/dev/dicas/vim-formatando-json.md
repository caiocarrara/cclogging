Title: [vim] Formatando JSON
Date: 2017-06-22 18:00
Tags: desenvolvimento, dicas, vim
Slug: vim-formatando-json
Summary: Dica rápida de como formatar JSON dentro do vim


Esse post inaugura uma nova seção aqui no blog. Regularmente postarei dicas
gerais e diretas. A ideia é servir mais como um caderno de anotações pra mim
mesmo em consultas futuras mas que também pode ser útil pra mais alguém.

A primeira dica e bem simples. Como formatar JSON utilizando o vim:

    :::vim
    :%!python -m json.tool

O comando acima irá executar o módulo `json.tool` do Python.

O mesmo módulo pode ser utilizado fora do vim:

    :::bash
    $ echo '{"atributo": "valor"}' | python -m json.tool
    {
        "atributo": "valor"
    }

Se ficou dúvida, comenta abaixo que eu tento ajudar.

Até a próxima.

