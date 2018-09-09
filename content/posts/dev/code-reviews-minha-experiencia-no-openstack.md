Title: Code Reviews: minha experiência no OpenStack
Date: 2018-09-09 01:00
Tags: dev, opensource, coding
Summary: Muito se fala a respeito de contribuições em projetos Open Source (de código aberto) e revisões de código. Nesse post eu pretendo relatar um pouco sobre como foi minha experiência com Code Reviews em um projeto embrionário do Open Stack onde acabei me tornando core commiter.

O ano era 2015 e eu havia acabado de começar a trabalhar na [ThoughtWorks
Brasil](https://www.thoughtworks.com/pt/). Entrei para trabalhar lá muito em
função da minha experiência como programador Python. A ThoughtWorks é uma
consultoria global de desenvolvimento de software com muitos projetos sendo
executados por diversos times. O meu primeiro projeto como um ThoughtWorker foi
na área de DevOps.  

O projeto em questão envolvia desenvolvimento relacionado ao OpenStack (por isso
um cara de Python no meio).  Na prática eu digo que era relacionado pois não
envolvia colaboração com o core do projeto, mas sim em subprojetos do extenso
guarda-chuva que é o OpenStack. O objetivo geral do nosso time era assegurar a
qualidade e eficiência dos builds da solução para cloud computing de um grande
cliente. Essa solução do cliente era uma versão personalizada do OpenStack
upstream (versão aberta).  

Como é (ou deveria ser) comum para corporações que utilizam soluções de código
aberto, o nosso trabalho não se limitava em codificar somente a solução
downstream (do cliente), mas também a versão upstream. Isso não era uma
benevolência, mas uma mistura de necessidade (afinal tínhamos que submeter para
a comunidade as demandas que faziam sentido pra gente) com responsabilidade de
retribuição. Aliás, o confronto de ideias, necessidades, demandas e visões
diferentes é um fator fundamental para a qualidade de projetos de código aberto
como o OpenStack.  

Eu estava em um universo completamente novo. Nova empresa, novo projeto, novo
segmento de software onde tinha atuado muito pouco. Eu poderia fazer (e talvez
faça) dezenas de posts falando sobre minhas experiências durante esse período,
mas o foco desse são os code reviews.  

##Contribuido para o OpenStack  
Antes de falarmos das revisões de código em si, precisamos entender um pouco
melhor o cenário como um todo. O OpenStack é um projeto de código aberto, logo
permite que absolutamente qualquer pessoa possa ter acesso ao código fonte e
contribuir com mudanças nesse código. Para que seja possível milhares de pessoas
contribuírem com dezenas de projetos sob o arcabouço OpenStack algum processo
deve existir para que a qualidade desses projetos não seja degradada. De forma
resumida o fluxo de contribuição com código é o seguinte:  

1. Clona o repositório do projeto que quer contribuir pra sua máquina;  
2. Prepara seu ambiente e roda os testes locais;  
3. Cria o patch com suas alterações;  
4. Submete para revisão da comunidade;  
5. Obtem pelo menos duas aprovações de core commiters;  
6. Tem o patch aceito por um core commiter.  

No passo destacado acima a dinâmica é a seguinte: qualquer pessoa pode revisar
códigos no OpenStack. Cada revisor pode fazer comentários gerais na submissão ou
específicos em um trecho do código proposto. Além dos comentários, os revisores
possuem votos, podendo ser +1 (gostei), 0 (zero) ou -1 (não gostei). Core
commiters possuem, além desses votos comuns, +2 (aprovado) ou -2 (reprovado).
Tanto o voto -1 quanto o -2 não são necessariamente terminativos. Provavelmente
junto com eles vem alguma requisição para melhoria ou ajuste. Assim que a
submissão tiver pelo menos 2 votos +2 (independente de quantos +1 tiver), um
core commiter pode marcar a submissão como aceita para iniciar o processo de
merge.  

## Code review   
A revisão de código é uma prática obrigatória em projetos de código aberto e eu
vejo cada vez mais adotada por empresas em projetos internos.  Essa etapa no
processo de desenvolvimento de software proporciona diversos benefícios. Tanto
para a qualidade do código que é produzido quanto para a as pessoas que
trabalham juntas.  

De maneira imediata e simplista revisar um código é exatamente aquilo que o
conceito remete: parar para olhar o código por outras pessoas e avaliar se
aquele código 1) atende ao propósito da alteração 2) é um código de boa
qualidade 3) não quebra o projeto. As avaliações 1 e 3, ainda que bastante
objetivas, na prática não são triviais. Porém a análise 2, sendo a de maior
carga subjetiva dentre as três, é a mais complexa e mais recompensadora para o
projeto.  

Um ponto importante de se lembrar é que em projetos reais, mesmo os de código
aberto, não há tempo infinito para a análise de submissões de código. O software
sendo produzido existe para auxiliar na solução demandas do mundo real. Essas
demandas impõem cronogramas, prazos, níveis de qualidade, priorizações, etc.
Logo, todo o processo de desenvolvimento, inclusive o de revisão de código, não
pode ser executado de tal maneira que as demandas do negócio sejam
subvalorizadas.  

## Minha experiência  
Especificamente nessa oportunidade que tive passando pela ThoughtWorks, a
revisão de código era tarefa fundamental para o sucesso do nosso projeto. Isso
porque o time estava constantemente submetendo patches para upstream e, como
todos sabemos (não é?): a definição de pronto não pode ser qualquer coisa que
não envolva código em produção. Assim, para atendermos as demandas do negócio
precisávamos ter nossos códigos aceitos. E para ter o código aceito precisávamos
dos reviews, desses pelo menos dois positivos de core commiters. Era regra: o
tempo para conseguir as aprovações era maior do que para codificar.  

Dado essa característica, o time como um todo se esforçou muito em revisar,
tanto quanto produzir código. Não fui diferente. No release do OpenStack em que
participei, para o projeto onde atuamos, acabei sendo o membro que mais
contribuiu com code reviews do time.

<img class="image is-pulled-left"
     src="https://s.caiocarrara.com.br/openstack_graph.png"
     alt="gráfico de contribuições no openstack">

Nesse processo pude aprender algumas coisas importantes que trago comigo até
hoje e são úteis no meu trabalho atual. Uma delas é que se você precisa que seu
código seja revisado, então revise o código dos outros. Essa é uma abordagem que
proporciona pelo menos duas vantagens: quanto mais código de outras pessoas você
revisar, mais convidativo para as outras pessoas será revisar o seu código e
quanto menos submissões (que não a sua) existir, maior a probabilidade de outro
revisor pegar a sua para revisar.  

Talvez um dos aspectos mais importantes para a revisão de código ocorrer é o
quão convidativa a submissão está. Trabalhando remotamente e tendo todas as
interações com as outras pessoas mediadas através do computador esquecer que são
outras pessoas "do outro lado" se torna bastante comum. Pessoas que possuem suas
rotinas e suas próprias demandas de trabalho.  

Para uma proposta de alteração em um projeto ser convidativa e também levar o
menor tempo para ser aceita, há alguns aspectos que precisam ser levados em
conta:  

1. **Faça a menor submissão possível que entregue valor.** Submissões que
   possuem muitas alterações geralmente são deixadas para "depois" pelos
   revisores. Ainda que a alteração que você precise fazer seja muito grande,
   quebre-a em submissões menores;  
2. **Disponibilize as informações importantes e relevantes para o revisor.**
   Essas informações fazem parte da descrição da submissão. Exponha porquê
   aquela alteração é necessária, qual foi a solução e links externos para
   possíveis conteúdos relacionados. Ao mesmo tempo não sature demais a
   submissão, lembre-se que o revisor precisará ler o código também (ninguém
   disse que seria simples).  
3. **Procure sempre fazer o melhor código possível desde a primeira submissão.**
   Pode ser tentador a ideia de que a qualidade do código pode ser mediana em
   alguma submissão, já que haverá uma revisão. Um código mal feito, ou complexo
   demais, só irá resultar em notas negativas e mais iterações de revisão
   (review, request, change, submit). Quanto mais iterações uma submissão
   possuir mais desgastante é o processo para todos os envolvidos.

Em dado momento, o que mais nos prendia era o fato de ninguém do time ser core
commiter no projeto em que estávamos mais atuantes. Ainda que obtivéssemos
diversos votos +1 em nossos patches, sempre precisávamos esperar os escassos +2
para aceitação. Esse foi um fator que me ajudou a exercitar e aprender ainda
mais com revisões de código e relacionamento em comunidade.  

##O lado humano da colaboração em software  
Precisamos lembrar que a cada interação com revisão de código não estamos
interagindo com o código em si, nem com uma máquina. Estamos sempre falando para
outra pessoa. Assim, precisamos nos atentar para o que e como falamos. Seja em
uma linha de código, na submissão como um todo ou mesmo nas salas de chat.  

Existem algumas premissas que devemos nos atentar em atender
nas interações em comunidades. Seja em projetos de código aberto ou na própria
empresa em projetos fechados.  

1. **Seja propositivo em críticas.** Isso significa que ao invés de dizer "seu
   código está ruim, refaça", talvez seja melhor dizer "o seu código não cobre
   cenários a e b, provavelmente precisa ser adaptado nesse e naquele ponto para
   que não ocorra problemas".  
2. **Defenda seus argumentos sem esquecer que você pode estar errado.** Em
   praticamente todos os ambientes com desenvolvedores por onde estive (virtual
   ou real) o ego é um fator demasiadamente preponderante. Egos gigantes quando
   se encontram acabam desfocando do objeto da interação. No caso, a solução que
   o software atende.  Assim, para evitar conflitos indesejados e manter o foco
   no que realmente interessa, é válido escolher bem as palavras em seus
   argumentos. Na prática, ao invés de dizer "a funcionalidade xpto é
   irrelevante", talvez seja melhor dizer "não consegui compreender a razão de
   estarmos priorizando a entrega dessa funcionalidade nesse momento, pode me
   explicar?".  
3. **Comunique-se com uma pessoa, não com a tela do computador.** Isso é bem
   básico, mas é normal nos esquecermos.  Cumprimentar e se despedir podem ser
   um ótimo começo :)

A maneira com que você se comporta, junto ao valor que você entrega ao projeto,
seja com código ou não, podem trazer diversos benefícios. Pessoalmente, no
projeto em que estávamos atuando, acabou me rendendo o status de core commiter
(como pode ser visto pelos +2 abaixo):  

<img class="image" style="margin: 0 auto"
     src="https://s.caiocarrara.com.br/openstack_contributions.png"
     alt="tabela de contribuições no openstack">

Reparem que o número de commits é bem baixo, mas ainda assim acabei me tornando
core commiter no projeto. De acordo com as conversas na época isso se deu
justamente pelas minhas contribições em reviews e no IRC do projeto.  

Abraço!  
