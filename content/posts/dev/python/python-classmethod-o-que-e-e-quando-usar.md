Title: Python @classmethod - O que é e quando usar
Date: 2020-02-10 23:50
Tags: desenvolvimento, python
Slug: python-classmethod-o-que-e-e-quando-usar
Summary: Python possui uma funcionalidade específica para modificação de métodos que é capaz de torná-los métodos de classe. Nesse post eu falo um pouco sobre o que exatamente é um método de classe, quando é interessante utilizá-lo e quais os riscos envolvidos em sua má utilização


Recentemente, considerando os projetos de código Python que tenho mais
contato, tenho observado a utilização de métodos de classe com mais
frequência que o habitual. Eu nunca tinha parado para racionalizar a
questão dos métodos de classes já que não era tão comum para mim até
então. Entretanto ao me deparar com situações como a ilustrada no trecho
de código abaixo, percebi que alguma coisa não estava certa.

```python
class MyClass:
    def __init__(self, some_parameter):
        self.attr_value = some_parameter

    @classmethod
    def some_class_method(cls, my_class_instance):
        cls.do_something(my_class_instance)
        my_class_instance.attr_value += 1

    @classmethod
    def do_something(cls, my_class_instance):
        pass
```

Encare a definição de classe acima e os seus detalhes de forma
unicamente didática. A intenção é exemplificar um caso hipotético de um
possível uso errôneo de métodos de classe.

No código acima temos a especificação de uma classe chamada `MyClass`.
Essa classe possui um método inicializador `__init__` personalizado que
recebe um parâmetro e o armazena em um atributo de instância (`self`)
chamado `attr_value`. Além disso, e esse é o foco da nossa análise nesse
momento, também possui dois métodos de classe: `some_class_method` e
`do_something`. Ambos os métodos recebem um parâmetro que, não
coincidentemente, foram nomeados como `my_class_instance`. Esses métodos
de classe esperam, justamente, receber uma instância do tipo `MyClass`.

Em uma primeira vista ingênua esse código poderia até ser considerado
normal. Sem maiores problemas. Entretanto três coisas me chamam a
atenção: uma instância (objeto) da classe ser usada como parâmetro para
métodos da própria classe, a necessidade de se ter vários métodos de
classe (uma vez que um método de classe só pode invocar outros métodos
de classe) e a não utilização do parâmetro `cls` (classe, instância de
`type`) em nenhum dos casos.

Para tentar responder uma possível inadequação nessa forma de
implementação, algumas questões mais fundamentais sobre a orientação a
objetos merecem ser retomadas. Além disso vale observarmos algumas
características da linguagem Python referentes à sua implementação
no tocante ao suporte a orientação a objetos.

## Programação orientada a objetos

> - Eu pensei em objetos como sendo células e/ou computadores em uma
>   rede, só capazes de se comunicarem através de mensagens [...]
>
> - Meu background em matemática me fez perceber que cada objeto poderia
>   ter diversas álgebras associadas e poderia haver famílias deles.
>   Isso seria muito útil. O termo "polimorfismo" foi imposto muito
>   depois e não é tão válido assim já que ele veio da nomenclatura de
>   funções e eu procurava algo mais que funções. Eu cunhei o termo
>   "generecidade" para lidar com comportamentos genéricos de uma forma
>   quase algébrica.

O trecho acima é uma tradução livre das palavras do criador do termo
"programação orientada a objetos", [Alan Kay](1), ao responder qual era
a sua intenção ao propor o conceito de programação orientada a objetos.
Toda a [resposta de Kay](2) é uma leitura muito interessante. Inclusive
por um trecho bastante emblemático:

> Eu não sou contrário aos tipos (n.t. referência a tipagem estática),
> eu só não conheço qualquer sistema de tipagem estática que não seja
> completamente sofrível, assim sendo eu ainda gosto de tipagem
> dinâmica.

Penso que sejam importantes as colocações acima para compreendermos que
programação orientada a objetos refere-se aos objetos e a passagem de
mensagens entre eles e não sobre classes. Ainda que em algumas
linguagens seja dado um peso maior para a construção de classes para se
programar, a função primordial de uma classe é servir como especificação
de um objeto daquela classe. O objeto em si deve então ser encarado como
elemento central da dinâmica de execução (vide o próprio nome do
paradigma).

Ainda em sua colocação Kay sumariza:

> Programação orientada a objetos para mim significa comunicação através
> de mensagem, retenção local, proteção e ocultação de estado e processo
> e vinculação tardia de todas as coisas.

Dessa forma, ao menos de algum modo, conseguimos ir um passo além da
definição de alguns componentes da programação orientada a objetos e
compreender a correspondência de cada elemento com a ideia fundamental
da POO. Objetos, especificados por suas classes, devem ser capazes de
ocultar seus estados através de seus atributos e garantir a comunicação
através da passagem de mensagens pelos de seus métodos.

## Em Python tudo é objeto

> Objetos são abstrações de Python para dados. Todos os dados em um
> programa Python são representados por objetos e relações entre eles.

A afirmação acima é a primeira sentença da documentação oficial da
linguagem Python sobre [Data Model - Objects, values and types](3). Essa
mesma página da documentação traz informações e definições super
importantes sobre cada um dos elementos que compõem o sistema de tipos
padrão da linguagem. Nela podemos encontrar a seguinte definição para o
que são as Classes:

> Classes são _invocáveis_ (n.t objetos que podem ser invocados:
> `objeto()`). Esses objetos geralmente atuam como _factories_ de novas
> instâncias deles mesmos, mas variações são possíveis para classes que
> sobrescrevam o método `__new__`. Os argumentos usados ao invocar uma
> classe são passados para o método  `__new__` e, tipicamente, para o
> método `__init__` para que a nova instância seja inicializada.

É interessante notar que a definição de uma classe merece, na
documentação da linguagem, somente mais um tópico dentro da definição do
que são objetos invocáveis (não encontrei uma tradução melhor para
_callable_).

Dessa forma, as classes em Python são somente mais um tipo de objeto.
Logo classes em Python também são objetos.

## O que são métodos de classe

Uma vez que em Python classes também são objetos e objetos possuem dados
(atributos) e ações (métodos), parece ser de certa forma esperado que
consigamos implementar ações nas classes personalizadas que programamos.
Como vimos acima, uma classe já possui algumas ações padrões que podemos
sobrescrever como o método `__init__`. Relembrando o nosso caso inicial:

```python
class MyClass:
    def __init__(self, some_parameter):
        self.attr_value = some_parameter
```

Ao implementar o método `__init__` sobrescrevemos o comportamento padrão
para enriquecer a sua execução com um comportamento personalizado. No
caso, o recebimento de um argumento e a atribuição desse argumento à uma
variável da instância sendo criada (`self`).

Além das ações prévias de uma classe, podemos ainda escrever nossas
próprias ações customizadas no nível do objeto `Class` e não no nível da
instância da classe. A forma (muito elegante por sinal), que Python
disponibiliza essa capacidade é através do decorador `@classmethod`
quando usado em um método comum na especificação de uma classe. Logo,
para termos um método de classe basta:

```python
class MyClass:
    def __init__(self, some_parameter):
        self.attr_value = some_parameter

    @classmethod
    def some_class_method(cls):
        pass

    def some_instance_method(self):
        pass
```

No exemplo acima, ao decorarmos o método `some_class_method` com o
decorador `@classmethod` o tornamos um método da classe `MyClass` e não
das instâncias de `MyClass`. Isso quer dizer que podemos invocar esse
método no nível da classe:

```python
MyClass.some_class_method()
```

Vale lembrar que também é possível a invocação de um método de classe
através de uma instância da classe. Portanto o código abaixo também
funcionaria:

```python
my_class_instance = MyClass()
my_class_instance.some_class_method()
```

Seja pela invocação através da própria classe ou de uma de suas
instâncias, o primeiro argumento passado implicitamente para um método
de classe sempre será a própria classe (que é um objeto, lembre-se!).
Por isso é uma convenção nomear esse primeiro argumento como `cls`. Essa
característica já traz um indício sobre quando devemos utilizar métodos
de classe em Python.

## Quando utilizar métodos de classe

_Antes de entrarmos no mérito sobre quando devemos utilizar métodos de
classes, vale lembrar que essa é somente uma interpretação. Como
qualquer interpretação está aberta a críticas e completamente passível a
erros. Dito isso, vamos ao que interessa._

Acabamos de perceber que em Python tudo é um objeto. Que objetos possuem
seus atributos (dados) e métodos (comportamentos). Uma vez que tudo é
objeto em Python, inclusive as Classes, podemos implementar
comportamentos nessas classes através de métodos de classes. A forma com
que Python entrega essa funcionalidade é através do decorador
`@classmethod`.

É interessante que exista a funcionalidade de se sobrescrever métodos de
uma classe ou de se implementar novos métodos para ela para que possamos
incrementar as capacidades de uma classe. Entretanto, para que
mantenhamos a coesão da nossa implementação, também é importante que não
alteremos a responsabilidade de uma classe. E para que possamos
compreender a responsabilidade de uma Classe (principalmente dentro da
representação do modelo de tipos do Python), podemos recorrer mais uma
vez à documentação oficial:

> Classes são _invocáveis_. **Esses objetos geralmente atuam como
> _factories_ de novas instâncias deles mesmos**, mas variações são
> possíveis para classes que sobrescrevam o método `__new__`.

Ou seja, ainda que possam existir variações na responsabilidade de uma
classe, **geralmente esses objetos atuam como fábricas de instâncias
deles mesmos**.

Dessa forma podemos encarar os métodos de classe passíveis de serem
implementados como formas de ampliar a capacidade de uma classe em
fabricar instâncias dela mesma. Para ilustrar essa definição, o exemplo
hipotético a seguir pode ser útil.

```python
class Livro:
    def __init__(self, titulo, paginas=None):
        self.titulo = titulo
        self.paginas = [] if not paginas else paginas

    @classmethod
    def cria_a_partir_de_paginas(cls, paginas):
        return cls(titulo="", paginas=paginas)
```

No exemplo acima temos uma definição de uma classe chamada `Livro`. Essa
classe possui um método inicializador que obrigatoriamente recebe um
argumento `titulo` e opcionalmente recebe um argumento `paginas`.
Supondo que seja um caso real a necessidade de se criar novas instâncias
de `Livro` sem um título (ou com um título padrão) e somente com suas
páginas. Desconsiderando que poderíamos reescrever o método padrão de
inicialização. Uma forma de atender essa demanda seria escrevendo o
método de classe escrito acima: `cria_a_partir_de_paginas`.

Percebam que, diferentemente do exemplo que abriu esse artigo, o método
para a criação do livro a partir de páginas, utiliza o primeiro
argumento adicionado implicitamente no método de classe. A classe
recebida como primeiro argumento é utilizada para a criação da instância
dela mesma. Afinal todos os argumentos que são passados para um método
deveriam ser utilizados por ele. Se não o são, é um sinal que o código
pode ser melhorado.

O código acima poderia então ser utilizado das duas formas a seguir:

```python

meu_livro = Livro("Titulo do Livro", paginas=["pagina1", "pagina2"])
meu_outro_livro = Livro.cria_a_partir_de_paginas(["pagina1", "pagina2"])
```

Um detalhe é que mesmo nesse caso hipotético a utilização de um método
de classe, uma vez que foi utilizado de forma apropriada, aumentou o
nível de significância e expressividade do código. A criação de um livro
sem título ainda pode ser feita da seguinte forma:

```python
meu_livro = Livro("", paginas=["pagina1", "pagina2"])
```

Entretanto dessa maneira adicionamos esse texto vazio mágico como
primeiro argumento que não expressa o real significado da chamada: criar
uma instância de `Livro` somente se importando com suas páginas:

```python
meu_livro = Livro.cria_a_partir_de_paginas(["pagina1", "pagina2"])
```

## O risco em se utilizar métodos de classe erroneamente

Uma característica bastante importante dos métodos de classe em Python é
que um método de classe só pode invocar outros métodos de classe. Esse
comportamento se dá em virtude das passagens de argumentos implícitas de
Python nas chamadas de métodos. Quando invocamos os métodos de classe o
Python passa implicitamente a própria classe como primeiro argumento do
método. Quando invocamos métodos da instância Python passa
implicitamente a própria instância como primeiro argumento. Logo, vamos
considerar o seguinte código:

```python
class MyClass:
    @classmethod
    def some_class_method(cls):
        return cls.other_method()

    def other_method(self):
        return 1

MyClass.some_class_method()
```

Ao executarmos o trecho acima o interpretador irá levantar um
`TypeError`: `TypeError: other_method() missing 1 required positional
argument: 'self'`.


De forma bastante simples podemos entender esse comportamento se
lembrarmos que a execução de um método de classe é uma execução no
objeto do tipo Classe e não em uma instância daquela classe. Dessa
forma, não há instância para ser passada implicitamente como primeiro
argumento do método de instância.

A utilização desenfreada e pouco planejada de métodos de classe pode se
tornar comum quando os princípios da orientação a objetos levantados lá
no começo, exemplificados pelas colocações do Alan Key, são deixados de
lado. Quando classes, especialmente em código Python, são encaradas como
um agrupador de funções sem critério, corre-se o risco de se ferir
tanto os princípios da programação orientada a objetos como os
princípios de um código Pythonico.

A característica de um método de classe só poder ser invocado por outro
método de classe, quando situada em um contexto onde classes são
utilizadas como agrupadoras de funções, pode levar a casos no mínimo
estranhos. No nosso último exemplo, se quiséssemos fazer o Python
executar o código seguindo a mesma estrutura tínhamos duas opções:

* Ainda que não faça sentido, poderíamos transformar o `other_method` em
  um método de classe. Dessa forma não somente infringimos as
  responsabilidades de uma classe como abrimos espaço para métodos de
  classe começarem a ser propagados na classe em questão:
```python
class MyClass:
    @classmethod
    def some_class_method(cls):
        return cls.other_method()

    @classmethod
    def other_method(cls):
        return 1
```

* Outra opção, na minha visão ainda pior e beirando o absurdo, seria
  começar a passar instâncias da própria classe para os métodos de
  classe de modo a ter acesso aos métodos de instância:
```python
class MyClass:
    @classmethod
    def some_class_method(cls, my_class_instance):
        return my_class_instance.other_method()

    def other_method(self):
        return 1
```

Ambos os riscos apresentados acima não são problemas somente em si
mesmos, mas exemplos de casos que devem ser considerados como
manifestações de um problema de modelagem da solução e do código sendo
implementado. No médio e longo prazo esse tipo de implementação pode
levar a comprometimentos sérios da capacidade de evolução do código,
comportamentos inesperados ou ainda dificuldades impensáveis para
detecção de falhas.


## Conclusão

Algumas das características que mais me chamam atenção na linguagem
Python é a sua flexibilidade e a liberdade que ela proporciona para as
pessoas que se propõe a desenvolver software com Python. Justamente sua
característica permissiva pode ser percebida na capacidade de extensão
dos comportamentos de um tipo de dado padrão da linguagem (o tipo
Classe). Ao se abrir e se flexibilizar a linguagem exige também mais
responsabilidade e consciência de quem a utiliza. Não é diferente quando
o assunto é método de classes.

É importante que tenhamos consciência enquanto profissionais de
desenvolvimento de software das motivações e razões que nos levam a
implementar uma solução de determinada forma. Mais importante do que
algo supostamente certo ou errado é a consciência ao tomar uma decisão.
A utilização desenfreada de métodos de classe podem ser manifestações
tanto da falta de consciência na tomada de decisão ao se implementar
software quanto um comprometimento na qualidade da implementação.


[1]: https://en.wikipedia.org/wiki/Alan_Kay
[3]: https://docs.python.org/3/reference/datamodel.html
[2]: https://userpage.fu-berlin.de/~ram/pub/pub_jf47ht81Ht/doc_kay_oop_en
