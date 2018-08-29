Title: Regras de negócio usando Domain Driven Design
Date: 2014-02-02 12:59
Tags: arquitetura, desenvolvimento, java
Slug: regras-de-negocio-usando-domain-driven-design  
Summary: O objetivo desse post não é explicar o Domain Driven Design, mas sim tentar ajudar a desmistificar uma dúvida que pode ser recorrente dos que começam a desenvolver software orientado ao domínio: como organizar a lógica de negócio evitando o modelo anêmico.

Aos que ainda não conhecem o conceito de [Domain Driven Design
(DDD)](http://en.wikipedia.org/wiki/Domain-driven_design "Domain Driven Design
Wikipedia"), sugiro que busquem conhecer o quanto antes (pode começar pela
indicação de livro no final do post). O objetivo desse post não é explicar o DDD
(talvez em um próximo post), mas sim tentar ajudar a desmistificar uma dúvida
que pode ser recorrente dos que começam a desenvolver software orientado ao
domínio.

A base do DDD diz que o desenvolvimento de uma solução de software deve ser
feito respeitando-se algumas camadas para a organização da solução:

-   **Camada de Apresentação:** é a famosa "interface com o
    usuário". Essa camada é a responsável por apresentear as informações
    ao usuário e interpretar os comandos do mesmo;
-   **Camada de Aplicação:** essa deve ser uma fina camada que coordena
    as atividades da aplição. Aqui não deve haver lógica de negócio
    envolvida.
-   **Camada de Domínio:** essa é a camada que possui as informações do
    domínio e deve ser considerada o "coração" da solução.
-   **Camada de Infraestrutura:** essa camada deve atuar como uma camada
    de suporte para as demais. Uma provedora da interligação entre as
    camadas, implementar a persistência dos objetos do negócio e conter
    as bilbiotecas de suporte.

Dentro da Camada de Domínio, onde realmente o DDD se foca, há ainda mais alguns
conceitos envolvidos:

-   **Entity:** objetos com uma identidade única;
-   **Value Objects:** objetos geralmente imutáveis, sem identidade,
    onde o que interessa é o seu valor. Geralmente objetos com valores
    iguais são considerados iguais;
-   **Aggregate:** coleções de objetos agrupados por uma entidade
    centralizadora;
-   **Service:** quando alguma operação não se enquadra em nenhuma
    entidades surgem os serviços;
-   **Repository:** abstração do grupo de todos os objetos do domínio de
    deterimnado tipo. Através do *Repository* é possível realizar
    operações no grupo de objetos: adicionar, remover, etc.
-   **Factory:** padrão para se delegar a criação de objetos de domínio.

Essa foi uma apresentação simplista e rápida dos principais conceitos
envolvidos. Agora, quando alguns desenvolvedores se deparam com todo esse novo
universo de organização pode se perguntar onde, de fato, implementar suas
lógicas de negócio. Lembrando que lógica do negócio é diferente da implementação
do fluxo da aplicação (tarefas ou interação com outros sistemas, por exemplo).

Se considerar somente os padrões da camada de domínio pode-se muito facilmente
concluir que a implementação de um software segundo esses padrões acarretará o
*anti-pattern* Modelo de Domínio Anêmico. Nesse *anti-pattern* as entidades
possuem somente estados (atributos) e nenhum comportamento (métodos). Nas
palavras do [Martin Fowler](http://martinfowler.com/ "Martin Fowler site")
[*bags of getters and
setters*](http://martinfowler.com/bliki/AnemicDomainModel.html "Anemic Domain
Model by Martin Fowler").  Nesse modelo as entidades não possuem quaisquer
lógicas de negócio, essas ficam abrigadas em classes estritamente de serviços,
onde a sua responsabilidade é fornecer as lógicas de negócio.

Dentre outros problemas, melhor apresentados no [artigo do
Fowler](http://martinfowler.com/bliki/AnemicDomainModel.html "Anemic Domain
Model by Martin Fowler"), com o Modelo de Domínio Anêmico corre-se um risco
eminete de se perder os princípios da orientação a objetos e tornar as classes
de serviços meras aberrações procedurais. Infortunadamente os problemas práticos
dessa abordagem só são percebidos no decorrer da manutenção do software.

Assim sendo, de maneira alguma o DDD prevê o Modelo Anêmico, muito pelo
contrário, com o DDD as Entities não são restritas a estados. Da mesma forma que
um bom design de projeto orientado a objetos, um projeto DDD deve detectar as
entidades do domínio **e os comportamentos das entidades de domínio.** Se uma
entidade possui seus atributos e comportamentos bem definidos, não há porquê
separá-los na implementação, de forma que uma entidade no DDD pode (e deve)
possuir, além de seus atributos, seus comportamentos com as regras de negócios
envolvidas.

Porém não deve-se com isso fazer com que a implementação do domínio distorça o
domínio real. Ao se analisar os problemas a serem resolvidos pela implementação
e tentar definir os objetos do modelo, muito facilmente haverão alguns aspectos
e comportamentos que não serão facilmente associados a nenhum objeto do modelo.
Para as ações "orfãs" de objetos do modelo é que existem os **Services**. Um
exemplo básico é a operação de transferência de dinheiro de uma conta para
outra. A ação (método) de transferência pertence à conta de origem ou à conta de
destino? Aparentemente não faz sentido em nenhuma das duas, não é?

Quando esse tipo de comportamento é detectado na análise da solução, a melhor
prática é implementá-lo como um serviço. A principal resposabilidade de um
Serviço é fornecer funcionalidades, que não são de responsabilidade direta de
qualquer objeto do modelo, para os próprios objetos do modelo. Vale atentar ao
fato de que, classes de serviço, como quaisquer outras da solução, **devem**
seguir obrigatoriamente, os princípios da orientação a objetos.

Respondendo a pergunta do título do post: se a regra de negócio for
explicitamente parte de um comportamento de uma entidade do modelo, então a
regra deve ser implementada no comportamento da entidade. Agora, se a regra de
negócio não pertence claramente a qualquer objeto do modelo, então deve-se
estudar e analisar muito bem a criação de um Serviço que ofereça determinada
funcionalidade que implemente a devida regra de negócio.

Links úteis:

-   Quer saber mais de DDD? [Domain Driven Design
    Quickly](http://www.infoq.com/minibooks/domain-driven-design-quickly "Domain Driven Design Quickly")
    por Abel Avram & Floyd Marinescu.
-   Quer saber mais sobre Arquitetura de software: [Introdução à
    Arquitetura e Design de
    Software](http://www.arquiteturajava.com.br/ "Introdução à Arquitetura e Design de Software"),
    Paulo Siveira, Guilherme Silveira, et al.

