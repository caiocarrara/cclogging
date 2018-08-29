Title: [Dica] Instalando PostgreSQL no Fedora 19
Date: 2014-04-02 22:00
Tags: desenvolvimento, fedora, linux, postgresql
Slug: instalando-postgresql-no-fedora-19  
Summary: Esse post tem como objetivo ficar de nota para posterior registro de como instalar o PostgreSQL no Fedora 19.

Fala ai galera! Beleza?

Hoje trago uma dica rápida e que não é bem muita novidade, mas é sempre últil
ter um guia rápido assim quando queremos fazer uma nova instalação. Aqui irei
considerar a minha distribuição Linux favorita, o Fedora, mas pode ajudar para
as demais distros também.

Primeiro, baixe e instale os pacotes do PostgreSQL (lembrando que o símbolo \#
indica prompt com nível root):

    :::bash
    # yum install postgresql postgresql-server

Terminando a instalação, vamos iniciar o banco de dados, habilitar e iniciar o
serviço do PostgreSQL:

    :::bash  
    # postgresql-setup initdb  
    # systemctl enable postgresql.service  
    # systemctl start postgresql.service  

Agora vamos acessar o prompt com o usuário *postgres *para podermos cadastrar
uma senha para esse usuário na base:

    :::bash  
    # su postgres  

Vamos agora iniciar o prompt do PostgreSQL e cadastrar uma senha para a ROLE
*postgres* e sair:

    :::bash  
    $ pgsql  
    $ postgres: ALTER ROLE postgres WITH ENCRYPTED PASSWORD 'suasenha';  
    $ postgres: \\q  
    $ exit  

Assim voltamos para o prompt root, vamos mudar o método de autenticação do banco
para utilizarmos md5. Basta editar o arquivo *`/var/lib/pgsql/data/pg_hba.conf`*
e mudar as configurações *peer *e *ident* para *md5* conforme o exemplo abaixo:

    :::bash  
    # TYPE DATABASE USER ADDRESS METHOD
    # "local" is for Unix domain socket connections only local all all md5  
    # IPv4 local connections:  
        host all all 127.0.0.1/32 md5  
    # IPv6 local connections:  
        host all all ::1/128 md5  

Salve o arquivo e reinicie o serviço do PostgreSQL:

    :::bash  
    # systemctl restart postgresql.service  

É possível testar a nova configuração tentando acessar o console do PostgreSQL
com o usuário postgres:

    :::bash  
    # pgsql -U postgres -W  

Vai ser solicitada a senha. Informando-a, caso consiga acesso ao prompt, a
configuração está completa.

É isso ai, abraço e até a próxima!

