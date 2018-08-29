Title: Meu primeiro Hackathon
Date: 2014-08-24 15:43
Slug: meu-primeiro-hackathon
Tags: appengine, hackathon, python  
Summary: Eu participei do meu primeiro Hackathon da Transparência Brasil. Foi uma experiência incrível e resolvi contar um pouco o que a ONG Transparência Brasil e a Sensedia fizeram lá na sede do Google Brasil.

Ontem ocorreu o primeiro [Hackathon Transparência
Brasil](http://dev.transparencia.org.br/api-portal/hackathon "Hackathon
transparência Brasil"). O evento foi realizado pela [ONG Transparência
Brasil](http://transparencia.org.br/ "Transparência Brasil") (TBrasil) em
conjunto com a [Sensedia](http://sensedia.com/br/ "Sensedia") e contou com o
apoio do Google Brasil que ofereceu toda a infra-estrutura para os participantes
em sua sede.

"Hackathon" é uma palavra que nasceu da composição de duas outras em inglês:
*Hack* e *Marathon*, para designar eventos onde desenvolvedores de software -
não somente programadores, mas também designers, e gerentes de projetos -
juntam-se e colaboram intensivamente para a construção de projetos de software
e/ou hardware. Tradicionalmente Hackathons tem duração mínima de um dia mas
podem chegar até uma semana.  Os objetivos de um hackathon pode ser diverso,
para maior noção eu recomendo a leitura do [verbete hackathon na
Wikipedia](http://en.wikipedia.org/wiki/Hackathon). Mais do que simplesmente
programar, o termo inglês hack também designa exploração e descoberta.

Descobrir como melhor utilizar os dados disponibilizados pelas APIs da
TBrasil foi justamente o intuito do Hackathon de ontem. As APIs abertas da
Transparência Brasil fornecem informações detalhadas e estatísticas sobre
candidatos a presidência, governo estadual, senado e de candidatos à reeleição,
além de informações sobre os  candidatos a deputado federal e estadual. Todos os
participantes do hackathon ganharam um Chromecast (dias contados para os caros
projetores!) e a equipe vencedora ganhou um Chromebook cada um. Os critérios
para o julgamento do melhor produto foram: impacto da proposta de valor,
qualidade do produto final e mérito técnico como forma de desempate.

As inscrições para o Hackathon poderiam ser feitas por equipes previamente
formadas ou de forma individual. Eu me inscrevi individualmente e na hora foi
realizado sorteio para juntar os participantes que estavam sozinhos. Em um
primeiro momento eu me senti um pouco inseguro em partir para o meu primeiro
hackathon sozinho, mas ao final do dia eu só pude comprovar que foi o melhor que
poderia ter feito.

Depois dos momentos "eu no Google" com poses para as fotos e do café da manhã
(com ovos e bacon!) começou a organização das equipes. A grande maioria já
estava formada previamente, mas houveram algumas que foram formadas no dia. A
minha equipe foi uma dessas.

Éramos em quatro totalmente desconhecidos: [Rafael
Nunes](https://twitter.com/rafanunes "Rafael Nunes twitter"), Julia, Taiolor
(sim, é o nome dele) e eu. Cada um com um histórico técnico e cultural diferente
o que fez com que além do desafio do próprio hackathon tivéssemos que também
descobrir como trabalhar juntos. Uma maratona de programação tende a requisitar
profissionais de alto desempenho, bem como equipes de alto desempenho, para que
consigam atingir os desafios propostos. Sabemos que equipes de alto desempenho
possuem como premissa um avançado grau de entrosamento, justamente o que não
tínhamos. Mas a ideia era superar desafio, então seguimos em frente!

Em alguns minutos definimos uma ideia: disponibilizar uma forma com que os
eleitores pudessem selecionar um candidato, para qualquer cargo, de acordo com
alguns filtros que julgamos pertinentes. Para que não precisassem toda hora
filtrar para lembrar suas preferências, os usuários também poderiam marcar, de
forma privada, um candidato que lhe interessasse. Se a proposta era ajudar na
seleção do candidato, já definimos também o nome da equipe: Seleição! (que
criatividade einh!).  Logo em seguida precisávamos definir com qual tecnologia
implementaríamos a ideia, para minha alegria escolhemos Python!!!  Usaríamos a
plataforma do [AppEngine](https://cloud.google.com/products/app-engine/
"AppEngine") do Google para publicar.

Mas nem tudo são flores, a equipe não tinha nenhum designer ou desenvolvedor
front-end. Porém, como iríamos utilizar o [Jinja](http://jinja.pocoo.org/ "Jinja
Pocoo") como template engine e eu tinha o conhecimento de Jinja e um pouco de
[bootstrap](http://getbootstrap.com/ "Bootsstrap"), acabei ficando com a árdua
tarefa! hahaha. Então já tinhamos a divisão das tarefas: o Rafael com a
comunicação do nosso aplicativo com a API da TBrasil, eu mostrando os dados na
tela e interação do usuário, a Julia me disponibilizando alguns end points e o
Taiolor pensando nos filtros e desenhando a estrutura das páginas. Foi assim
praticamente o dia todo e é impressionante a sensação da passagem do tempo em um
ambiente desses.  Particularmente eu nem senti o tempo passar.

Ao final do dia estávamos com um início de aplicativo rodando e conseguimos
apresentar muito bem! Chegamos a publicar em
[seleicao.appspot.com](http://seleicao.appspot.com/), mas quando rodamos um job
para popular nosso datastore estouramos o limite (free) de escrita no AppEngine
=P. Todo histórico do nosso trabalho e o código fonte está no
[GitHub](https://github.com/rafaelnunes/seleicao "Github Seleição")
também. Fizemos um ótimo trabalho juntos e colaboramos intensivamente para
algo minimamente utilizável que consumia as APIs da TBrasil. Meu objetivo estava
concluído!

A premiação, em minha opinião, foi justa! Ganhou uma equipe que desenvolveu um
[Greenhouse](https://chrome.google.com/webstore/detail/greenhouse/ifomhmgandipmpnelclcmbefppopfklc?hl=en
"Greenhouse chrome extension") mas com os dados da TPBrasil. Uma ferramenta de
fácil acesso e que pode ajudar muito o eleitor sem muitos esforços para a
utilização.

Como falei, ao final do dia eu pude voltar para casa muito satisfeito, muito
mais do que se eu tivesse ido com uma equipe formada. Eu não voltei com um
Chromebook na bagagem, mas voltei com história pra contar.  Mais do que isso, eu
conheci, interagi, colaborei e trabalhei com gente diferente e com histórias
contrastantes e muito legais! Eu poderia ter formado uma equipe, mas preferi ir
pra conhecer e programar com gente desconhecida. Conhecer novas ideias e trocar
experiências. Para ficar ainda melhor tudo isso ocorreu com muito *self*
explícito!

Quem tiver a oportunidade de participar de um Hackathon, não deixe passar! E se
não estiver tão interessado na premiação, vá sozinho, de mente aberta e disposto
a fazer coisas que não faz geralmente. Pense em uma ideia na hora, colabore e
trabalhe arduamente para fazer algo funcional.

Para encerrar, só posso dizer que foi fenomenal! A cada dia eu gosto mais de
Python pela facilidade que a linguagem me dá em expressar a ideia do software
que tenho na mente sem deixar de produzir software de ótima qualidade. O
dia-a-dia de um desenvolvedor sério e ético já é muito difícil, ter ainda mais
dificuldade de colocar suas ideias em formato de código é inadmissível! Python e
a comunidade envolvida possibilitam que essa dificuldade seja muito menor.

Obrigado TBrasil, Sensedia, Google Brasil e em especial Rafael Nunes, Julia e
Taiolor!

Nos vemos no próximo Hackathon!

