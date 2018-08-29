Title: Migrando do Wordpress para o Pelican  
Date: 2014-09-02 00:45  
Tags: python, pelican  
Slug: migrando-do-wordpress-para-o-pelican  
Summary: Aqui eu explico quais os motivos me levaram a migrar meu antigo blog Wordpress para Pelican + Github Pages. Além disso explico passo a passo como fazer essa migração.


Hoje pela manhã eu terminei a migração desse meu blog do [Wordpress] para o
[Pelican]. Eu utilizava o antigo sistema gerenciador de conteúdo há algum tempo,
desde quando comecei as atividades aqui no _caiocarrara.com.br_.  Na ocasião era
a única ferramenta que conhecia e eu achava fácil para instalar e customizar,
portanto foi a escolha mais óbvia para mim. De lá para cá, ainda que a
utilização não tenha sido intensa, e talvez justamente por isso, o Wordpress
estava suprindo minhas necessidades. Nos últimos dias comecei acessá-lo
regularmente para rascunhar alguns artigos e juntamente com a utilização mais
recorrente eu comecei a desgostar da ferramenta.  

Assim como é muito mais rápido e convidativo abrir um editor de textos como o
[Sublime] do que uma IDE como o [Eclipse] para programar, ou mesmo o console
interativo do [Python] para uma validação de código rápida, acho muito mais
convidativo abrir um editor de textos simples de minha preferência para
rascunhar e escrever um artigo do que ter que sofrer as "intempéries" da
Internet brasileira para abrir uma página de autenticação, se autenticar, clicar
para escrever um post, esperar todo aquele editor de textos com recursos que
raramente utilizo carregar para só então colocar um pedaço de ideia "no papel".
Muitas vezes um texto é construído com a união de pequenas ideias que vão
aparecendo. Repetir esse ciclo todo e juntar todas as ideias estava ficando
lento. Naturalmente passei a anotar minhas ideias em arquivos de texto simples e
o Pelican então caiu como uma luva!

###Pelican  

Basicamente o Pelican é um gerador de páginas HTML estáticas. Ele faz seu
trabalho a partir de arquivos de textos com marcações especiais, como o
[reStructuredText] ou o [Markdown] (minha preferência). Eu poderia me aprofundar
nessa parte, mas o [Arthur Alves] já fez um belo trabalho lá no PythonClub
explicando bem o Pelican no seu artigo [Criando sites estáticos com Pelican
Framework]. Se alguém quiser saber mais os fundamentos do Pelican, esse artigo
será ótimo!

###Migrando Wordpress para o Pelican  

Depois de brincar um pouco com o Pelican e me sentir um pouco mais familiarizado
com o gerador e seus comandos resolvi colocar a mão na massa e partir para a
migração. A seguir vou colocar uma receitinha de como fazer isso, os passos são
os que lembro de ter feito.  

O Pelican já possui uma ferramenta que faz todo o trabalho pesado de importação
pra gente, chama-se `pelican-import`. Esse recurso atua sobre o xml de
exportação gerado em seu site Wordpress. Para gerar esse arquivo acesse o painel
de administração do seu Wordpress, no meu lateral esquerdo acesse `Tools >
Export`. No meu caso eu selecionei para exportar `All Content` e cliquei para
fazer o download.  

Tendo o arquivo xml gerado, vamos certificar de ter instalado as dependências
para se importar o conteúdo do XML. O Pelican utiliza os pacotes
_BeautifulSoup4_ e _lxml_. A instalação é feita como com qualquer outro pacote:

    :::bash
    $ pip install BeautifulSoup4 lxml  

Estando com as dependências em ordem, já podemos rodar o `pelican-import`. Esse
utilitário é capaz de importar um site de diversas fontes para o formato
esperado pelo Pelican. Como estamos focando no Wordpress, o comando é o
seguinte:  

    :::bash
    $ pelican-import --wpfile -m -o content/ /path/to/export.xml  

No comando acima, além da chamada do utilitário de importação foram passados
alguns parâmetros:  

* `--wpfile`: indica que a importação deverá utilizar um arquivo XML de exportação do Wordpress;  
* `-m`: indica que o arquivo de saída deverá estar no formado Markdown. O padrão é rst;  
* `-o content/`: indica o diretório nos quais os arquivos Mardown gerados deverão ser escritos;  
* `/path/to/export.xml`: o arquivo exportado do Wordpress.  

Para testar a importação, basta executar o Pelican para gerar os arquivos html
estáticos e rodar o servidor HTTP de desenvolvimento:  

    :::bash
    $ pelican content
    $ ./development_server.sh start  

Acesse `localhost:8000` para ver como ficou.  

No geral e para os tipos de posts e páginas que eu tinha no meu Wordpress essa
sequência simples foi praticamente o suficiente. Adicionalmente eu precisei
editar alguns links que ficaram quebrados e fazer algumas melhorias nos
_metadata_ dos arquivos do Pelican.  

###Deploy no Github Pages  

Antes eu usava uma hospedagem particular para rodar o Wordpress, mas agora com
as páginas estáticas eu não tenho mais a necessidade de ter o [PHP] e [MySql],
basta um servidor [HTTP] bem simples. Resolvi simplificar ainda mais e  delegar
isso para o serviço provido pelo próprio [Github], o [Github Pages]. Essa foi a
escolha mais imediata pois já  estou utilizando o Github para versionar os meus
artigos.  

Todo usuário do Github já possui previamente uma conta no serviço [Pages], basta
criar um repositório cujo nome seja `[username].github.io`. No meu caso o
repositório ficou com o nome `cacarrara.github.io`. Os arquivos que estiverem no
branch `master` desse repositório são utilizados pelo Pages para exibir as
páginas do site na url com o mesmo nome do repositório criado.  

Seguindo a mesma ideia do pessoal do [PythonClub], eu criei um branch chamado
`pelican` para os arquivos do Pelican e os _Markdown_ originais das minhas
publicações e o branch `master` abriga somente as páginas html geradas. Para
ajudar um pouco nesse processo de subir para o Github os arquivos a cada
geração, eu utilizo um utilitário chamado `ghp-import`. Para instalá-lo utilize
o _pip_ também:  

    :::bash
    $ pip install ghp-import  

Após a geração do Pelican, basta executar:  

    :::bash
    $ ghp-import output  

* `output`: indica o diretório onde estão os arquivos gerados pelo Pelican  

O comando `ghp-import` atualiza o branch local de nome `gh-pages` com o conteúdo
do diretório `output`. Depois disso, basta fazer o `push` do branch `gh-pages`
para o branch `master` do reposiório remoto:  

    :::bash
    $ git push origin gh-pages:master  

E pronto! Pode ser que a sincronia do Github Pages demore um pouquinho para de
fato publicar a primeira versão da sua página, mas se tudo deu certo logo estará
no ar!

Além disso também atualizei meu DNS para utilizar o domínio caiocarrara.com.br
no Github Pages, caso essa também seja a vontade de quem lê esse artigo,
recomendo a própria documentação do Github para isso: [Github Pages - Custom
URLs]. Qualquer dúvida deixa nos comentários que posso ajudar!  

Para quem quiser dar uma olhada, o repositório desse site está no meu Github:
[cacarrara.github.io].

Bom, é isso. Até a próxima! 


[Wordpress]:http://wordpress.org  
[Pelican]:http://getpelican.com  
[Sublime]:http://sublimetext.com  
[Eclipse]:http://eclipse.org  
[Python]:http://python.org  
[reStructuredText]:http://docutils.sourceforge.net/rst.html  
[Markdown]:http://daringfireball.net/projects/markdown/  
[Arthur Alves]:http://twitter.com/Arthur_4lves  
[PythonClub]:http://pythonclub.com.br
[Criando sites estáticos com Pelican Framework]:http://pythonclub.com.br/criando-sites-estaticos-com-pelican.html  
[PHP]:http://php.net  
[MySql]:http://mysql.com  
[HTTP]:http://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol  
[Github]:http://github.com  
[Github Pages]:http://pages.github.com
[Pages]:http://pages.github.com  
[Github Pages - Custom URLs]:https://help.github.com/articles/setting-up-a-custom-domain-with-github-pages
[cacarrara.github.io]:https://github.com/cacarrara/cacarrara.github.io/
