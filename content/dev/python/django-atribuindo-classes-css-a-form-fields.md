Title: Django - atribuindo classes CSS e atributos HTML a Form Fields
Date: 2015-04-15 01:30
Tags: python, django
Slug: django-atribuindo-classes-css-e-atributos-html-a-form-fields
Summary: Nesse post eu falo sobre a distinção de responsabilidades entre Fields e Widgets no sistema de formulários do Django e um potencial problema nessa maneira de abstrair o Form quanto à sua apresentação. Assim sendo eu proponho uma maneira de se trabalhar utilizando a lib django-widget-twaks para solucionar o problema apresentado, reforçando a separação de responsabilidade entre a camada de apresentação e a de lógica de negócios.

##Django Fields e Widgets

Tentando simplificar as diversas complexidades que existem na criação e
manipulação de formulários em uma aplicação web, o framework [Django] abstrai o
componente de formulário em um conjunto de classes [Python]. Trabalhando dessa
forma o desenvolvedor tem a possibilidade de definir diversos aspectos de um
formulário simplesmente através de programação com [Python]. Entre esses
aspectos estão tanto os que atingem a camada de apresentação (HTML) quanto a
camada de processamento no servidor.

Nessa abordagem da abstração de formulários do [Django] existem, entre outros,
dois componentes importantes: os [Form Fields] e os [Widgets]. Enquanto a
responsabilidade dos Fields é a de gerenciar os dados e validá-los em uma
submissão ao servidor, os [Widgets] são responsáveis por definir como esses
campos serão apresentados no navegador para o usuário final.

Uma vez que são os [Widgets] que definem como um campo de um formulário irá se
apresentar na página HTML, nada mais coerente do que o próprio Widget suportar a
atribuição das classes CSS desse campo. Assim sendo, de acordo com a própria
[documentação oficial] do [Django], a forma de se estilizar os campos no HTML é
informando atributos adicionais ao Widget no momento de sua instanciação e
atribuição ao respectivo Field. Vamos aos exemplos.

###Estilizando Widgets

De acordo com a documentação oficial uma das maneiras de se atribuir classes CSS
a um widget é a seguinte:

    :::python
    class CommentForm(forms.Form):
        name = forms.CharField(widget=forms.TextInput(attrs={'class': 'special'}))
        url = forms.URLField()
        comment = forms.CharField(widget=forms.TextInput(attrs={'size': '40'}))

Outra maneira de fazer essa atribuição é através do atributo widget da classe
Meta. Em um [ModelForm], por exemplo, a atribuição ficaria assim:

    :::python
    class MeuModelForm(ModelForm):
        class Meta:
            model = MeuModel
            fields = '__all__'
            widgets = {
                'field_one': TextInput(attrs={'class': 'special'}),
                'field_two': Textarea(attrs={'class': 'special'})
            }

Entretanto, sabemos muito bem que em aplicações reais não somente o atributo
class precisamos atribuir aos fields. Assim sendo o exemplo anterior pode
facilmente evoluir para o seguinte exemplo:

    :::python
    class MeuModelForm(ModelForm):
        class Meta:
            model = MeuModel
            fields = '__all__'
            widgets = {
                'field_one': TextInput(attrs={'class': 'special',
                                              'id': 'field_one',
                                              'placeholder': 'Field One',
                                              'required': ''}),
                'field_two': Textarea(attrs={'class': 'special',
                                             'data-rules': 'required',
                                             'id': 'field_two',
                                             'placeholder': 'Field Two',
                                             'rows': 8})
            }

A tendência é que esse trecho do código aumente consideravelmente para
formulários um pouco mais complexos, seja na quantidade de campos ou na forma
com que os mesmos serão apresentados, precisando assim de classes CSS ou outros
atributos HTML. Ainda assim, mesmo com mais código sendo produzido nesse ponto,
não podemos negar que há certa organização.

###Um problema ao se definir classes CSS nos atributos da classe Widget

Um problema que enfrentei recentemente relacionado à esse tema foi o de precisar
voltar ao módulo de Forms (forms.py) somente para alterar o estilo de alguns
formulários. Nessa oportunidade específica a pessoa que estava fazendo a
manutenção nos templates ainda não tinha muito conhecimento de [Python] e muito
pouca familiaridade com a estrutura de um projeto [Django]. Ela sabia muito bem
de front-end e sabia se econtrar no diretório dos templates da aplicação apenas.

Independente da experiência do desenvolvedor que estiver fazendo a manutenção
dos formulários, se pensarmos um pouco, quando estamos alterando a apresentação
de um form é muito mais comum nos encontrarmos manipulando arquivos de template,
CSS e javascript do que o módulo [Python] de formulários. Dessa forma, pelo
menos na minha visão, seria preferível, na maior parte dos casos, definir as
classes CSS no próprio arquivo de template do [Django], bem como os demais
atributos HTML dos campos de um formulário.

###Utilizando django-widget-tweaks

A [django-widget-tweaks] é uma biblioteca simples, direta e bem feita, que
permite que possamos ajustar classes CSS e atributos HTML dos [Form Fields] do
[Django] nos próprios arquivos de template. Ela possibilita que desenvolvedores
possam atualizar arquivos de template sem precisar se envolver diretamente com
códigos [Python]. Essa é uma grande vantagem quando se tem equipes com
conhecimentos distintos ou mesmo quando se precisa pragmaticamente separar as
definições de apresentação das instruções de código [Python].

Para utilizar a lib basta instalá-la através do [pip]:

    :::bash
    $ pip install django-widget-tweaks

Adicioná-la às INSTALED_APPS no settings:

    :::python
    INSTALED_APPS = (
        ...,
        'widget_tweaks',
    )

Uma das formas de utilizá-la nos arquivos de template é através de [filtros]
como o a seguinte:

    :::html
    {% load widget_tweaks %}

    <!-- adiciona 2 novas classes ao campo -->
    {{ form.title|add_class:"css_class_1 css_class_2" }}

Outros atributos HTML também podem ser atribuídos de maneira semelhante com
filtros:

    :::html
    {% load widget_tweaks %}

    <!-- muda o tipo do campo, por exemplo para conformidade com HTML5 -->
    {{ form.search_query|attr:"type:search" }}

    <!-- adiciona/modifica alguns atributos -->
    {{ form.text|attr:"rows:20"|attr:"cols:20"|attr:"title:Hello, world!" }}

    <!-- adiciona atributos sem parâmetros -->
    {{ form.search_query|attr:"autofocus" }}

Mais detalhes e informações sobre a django-widget-tweaks podem ser encontrados
no completo [README] do projeto no github. Não deixe de conferir se quiser usar.

Até a próxima!


[Django]:http://djangoproject.com
[Python]:http://python.org
[Form Fields]:http://docs.djangoproject.com/en/1.8/ref/forms/fields/
[Widgets]:https://docs.djangoproject.com/en/1.8/ref/forms/widgets/
[documentação oficial]:https://docs.djangoproject.com/en/1.8/ref/forms/widgets/#styling-widget-instances
[README]:https://docs.djangoproject.com/en/1.8/ref/forms/widgets/#styling-widget-instances
[ModelForm]:https://docs.djangoproject.com/en/1.8/topics/forms/modelforms/
[django-widget-tweaks]:https://github.com/kmike/django-widget-tweaks
[pip]:http://caiocarrara.com.br/virtualenv-instalacao-e-utilizacao.html
[filtros]:https://docs.djangoproject.com/en/1.8/howto/custom-template-tags/#writing-custom-template-filters
