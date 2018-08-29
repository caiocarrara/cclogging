Title: Virtualenv: Instalação e utilização
Date: 2013-11-24 18:08
Tags: desenvolvimento, django, python, virtualenv
Slug: virtualenv-instalacao-e-utilizacao  
Summary: Virtualenv é uma ferramenta indispensável para quem desenvolve software utilizando Python. Nesse artigo mostro os motivos pelos quais você deveria utilizar e como fazer a instalação e configuração inicial.

**O que é virtualenv:**

De acordo com o próprio site do virtualenv, trata-se de uma ferramenta para a
criação de ambientes Python isolados (ambientes virtuais, virtual environments,
virtualenv). Essa própria descrição é bastante elucidativa, o que ainda pode
estar em dúvida é a necessidade de se utilizar o virtualenv, ou de se ter
ambientes isolados.

**Por que eu deveria utilizar o virtualenv?**

Limitando-se às necessidades de um desenvolvedor, ambientes Python isolados são
necessários pois possibilitam o desenvolvimento de soluções em diferentes vesões
do Python e de seus módulos sem haver interferência entre os ambientes.

Um exemplo bastante prático que me fez utilizar o virtualenv pela primeira vez
foi a necessidade de manutenção de um sistema desenvolvido em Django em uma
versão mais antiga. Atualmente eu tenho o Django mais recente (1.5.1) instalado
no meu ambiente real. Entretanto apareceu um freelancer para eu fazer a
manutenção em um sistema que foi desenvolvido no Django 1.3.0. Logo, na
preparação do ambiente para subir esse sistema na minha máquina eu pensei: e
agora? Não estava nem um pouco disposto a reinstalar uma versão do Django.

Eu já tinha ouvido falar muito do virtualenv, mas não tinha realmente precisado
utilizar, então sempre posterguei sua utilização, mas chegou a hora. Como fazer?

**Instalando o virtualenv:**

A instalação do virtualenv é rápida, fácil e indolor. Vou mostrar como fiz no
Fedora 18.

Primeiro você deverá ter instalado o setuptools, caso não tenha siga as
instruções da versão desejada em: <https://pypi.python.org/pypi/setuptools>. O
setuptools é um ferramenta para a instalação, build, atualização e demais
tarefas relativas à pacotes Python. A sua forma de utilização é bastante
simples:

    :::bash  
    # easy_install <Pacote_a_ser_instalado>  

Assim sendo, para instalarmos o virtualenv basta utilizar:

    :::bash  
    $ easy_install virtualenv  

**Utilizando o virtualenv:**

Tendo o virtualenv instalado, é hora de colocarmos a mão na massa.  Inicialmente
escolha um diretório qualquer onde ficará o seu ambiente virtual. Caso esteja
fazendo um ambiente dedicado à um projeto (que é meu caso), pode nomear o
diretório com o nome do projeto. Você pode criar o diretório manualmente, caso o
virtualenv seja utilizado com um diretório que não existe ele se encarrega de
criá-lo, sendo assim vamos criar nosso ambiente:

    :::bash   
    $ virtualenv ~/meu_ambiente  

Esse comando criará o novo ambiente no diretório especificado. Dentro do
diretório pode perceber que foram criados os subdiretórios:

-   **bin:** alguns executáveis que atuarão exclusivamente no ambiente
-   **lib:** módulos e bibliotecas python exclusivas para o ambiente
-   **include:** headers exclusivos para o ambiente

Pronto! O ambiente isolado já está criado. Estando no diretório do ambiente,
para ativar o mesmo e não utilizar o ambiente Python do sistema basta o comando:

    :::bash  
    [~/meu_ambiente]$ source bin/activate  

Você perceberá que o ambiente está ativado pelo próprio console, que agora está
assim:

    :::bash  
    (meu_ambiente)[~/meu_ambiente]$  

Para desativar o ambiente Python exclusivo basta o comando:

    :::bash  
    (meu_ambiente)[~/meu_ambiente]$ deactivate  

**Instalando pacote Python:**

Caso nesse momento você ainda não tenha o pip instalado, instale assim:

    :::bash  
    (meu_ambiente)[~/meu_ambiente]$ easy_install pip  

A instalação de pacotes e módulos no ambiente virtual do virtualenv é bem
simples, como acabamos de ver caso tenha sido necessário instalar o pip. Estando
com o ambiente ativado, vamos instalar o yolk (usado para listar os pacotes
Python instalados):

    :::bash  
    (meu_ambiente)[~/meu_ambiente]$ pip install yolk  

Para usar o yolk e listar o que tem instalado no seu ambiente:

    :::bash  
    (meu_ambiente)[~/meu_ambiente]$ yolk -l  

**Instalando Django no ambiente virtual:**

Como dito no início do post, a minha necessidade em utilizar o virtualenv foi
para usar uma versão do Django específica para desenvolvimento. Assim sendo,
caso deseje instalar uma versão determinada do framework, basta usar o pip para
isso:

    :::bash  
    (meu_ambiente)[~/meu_ambiente]$ pip install Django==1.3.0  

O comando acima irá instalar a versão 1.3.0 do framework. Após o término da
instalação pode-se verificar através do yolk mais uma vez:

    :::bash  
    (meu_ambiente)[~/meu_ambiente]$ yolk -l  

É isso ai! Já existe bastante material sobre a utilização do virtualenv pela
internet, mas em português há poucos que sejam direto ao ponto, então resolvi
escrever. Esse meu post baseou-se nas fontes abaixo que sugiro enormente a
visita:

-   <https://pypi.python.org/pypi/setuptools/0.9.8>
-   <http://www.virtualenv.org/en/latest/>
-   <http://simononsoftware.com/virtualenv-tutorial/>
-   <http://klauslaube.com.br/2011/03/18/python-django-virtualenv/>

Até a próxima!

