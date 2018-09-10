Title: Porque saí do GitHub Pages
Date: 2018-09-10 01:00
Tags: social, internet, liberdade
Summary: Após mais de 4 anos utilizando o serviço GitHub Pages para hospedar meu site/blog pessoal resolvi que era hora de mudar. Nesse post eu faço uma autoanálise dos princípios nos quais essa minha decisão foi baseada: liberdade, autonomia, transparência, responsabilidade e diversão.


Primeiramente o motivo pelo qual migrei meu site/blog pessoal do [GitHub
Pages](https://pages.github.com/) para um [Servidor Virtual Privado
(VPS)](https://en.wikipedia.org/wiki/Virtual_private_server) próprio não foi a
recente [compra do GitHub pela
Microsoft](https://news.microsoft.com/2018/06/04/microsoft-to-acquire-github-for-7-5-billion/).
Esse fato pode ter me tirado de uma momentânea inércia, mas não foi
determinante. A minha decisão foi baseada em alguns princípios fundamentais que
podem ou não estar relacionados com isso.  São eles: liberdade, autonomia,
transparência, responsabilidade enquanto profissional de tecnologia e diversão.
Essas mesmas ideias me fizeram há um tempo abandonar outros serviços como o
Medium para publicações e o Google para gerenciamento de calendário e contatos.
Em posts futuros pretendo falar mais especificamente sobre esses serviços, mas
nesse momento gostaria de compartilhar um pouco mais sobre a minha saída do
GitHub Pages para hospedagem do meu site/blog pessoal.  

## Geradores de sites estáticos e o GitHub Pages

Uma das coisas que precisam ser relembradas é que o serviço GitHub Pages não é
um gerador de sites estáticos. Há divesas opções de geradores desse tipo
disponíveis e o utilizado pelo Github em seu serviço é o
[Jekyll](https://jekyllrb.com/). O serviço provido pelo GitHub é o de hospedagem
gratuita de arquivos. O que o torna diferente é a sua integração com
repositórios git hospedados no GitHub. Assim sendo, de modo resumido basta
versionarmos os arquivos de um site em um repositório git no GitHub que o mesmo
será disponibilizado na Internet como um site estático.  

O serviço é realmente bom, simples e fácil de usar. É uma ótima escolha em
diversas situações assim como foi para mim há 4 anos quando passei a utilizá-lo.
Porém ser uma boa escolha em determinado momento não significa ser uma boa
escolha para sempre. Além do mais é comum acontecer de um serviço se tornar tão
amplamente utilizado que ele passa ser sinônimo de algo que não é. Isso é
bastante evidente atualmente quando observaoms pessoas associarem Google e
Facebook como sendo *a Internet*. Dentre tantos problemas que isso pode
provocar, um dos mais simples é que aos poucos vamos perdendo a capacidade de
perceber as alternativas para aquele serviço ou produto.  

## O que é bom hoje pode não ser amanhã

Quando escolhemos utilizar um produto ou serviço, ainda que seja difícil,
precisamos ter claro as nossas reais motivações. Em 2014 quando passei a
utilizar o GitHub Pages eu pagava por um servidor compartilhado tradicional.
Nele eu rodava uma instalação do famoso [Wordpress](https://wordpress.org/) para
um blog pessoal. Naquele momento eu estava achando a solução muito complexa e
burocráica (PHP, banco de dados, servidor web, cPanel, backups) além de
relativamente lenta de modo geral para o meu propósito. Era lento e pesado
abrir o editor web para escrever conteúdo, era lento para que eu pudesse colocar
uma alteração no template em produção, era lento para renderizar para o usuário
do blog.  

Na busca por alternativas acabei encontrando essa até então desconhecida maneira
para mim de se fazer e publicar sites: [geradores de sites
estáticos](https://www.staticgen.com/). Na época eu já programava em Python e
chegar até o [Pelican](http://getpelican.com/) foi uma consequência eminente.  

Além das desvantagens já falada sobre a solução com o Wordpress em um servidor
compartilhado, eu também estava buscando redução de custos naquela época. Desde
muito tempo eu mantenho blogs escrevendo e programando-os. Personalizar
templates e subir as alterações via FTP em algum servidor era o que eu passava
madrugadas fazendo há mais de uma década. Assim, pagar por hospedagens era até
então o normal na minha concepção. A descoberta de um serviço gratuito como o
GitHub Pages acabou juntando o útil ao agradável. Dessa forma a união Pelican +
GitHub Pages acabou sendo a solução perfeita para as minhas necessidades.  

Muito tempo se passou desde então e hoje eu acredito que um próximo passo
precisa ser dado uma vez que os motivos do passado não fazem tanto sentido
atualmente. Eu continuo preferindo o fluxo de trabalho de escrita, edição,
personalização e deploy oferecido por geradores de sites estáticos, mas a
realidade atual não me restringe tanto quanto a gastos com um servidor próprio,
meu conhecimento técnico me permite manter razoavelmente bem esse servidor e,
mais importante do que tudo, minha consciência atual me faz valorizar aspectos
diferentes na escolha de uma solução tecnológica.  

## Liberdade e autonomia

Talvez estejamos passando por um momento muito importante para prezar por
autonomia e liberdade no consumo e produção tecnológica. Se o movimento do
[software livre seguido pelo de código
aberto](https://en.wikipedia.org/wiki/Free_and_open-source_software) algum dia
foi questionado e criticado, trazendo dúvidas sobre como deveríamos abordar o
desenvolvimento de software, hoje é praticamente consenso as vantagens do
[FOSS](https://en.wikipedia.org/wiki/Free_and_open-source_software). Entretanto
estamos em uma época de *open source, closed services*.  

Os maiores agentes do mercado de tecnologia atualmente mantêm altos
investimentos em projetos de código aberto. Alguns possuem até o núcleo do
negócio baseados em open source. Porém através de software de código aberto
oferecem um serviço "fechado". Geralmente esses serviços possuem extensos termos
de aceitação naturalmente negligenciados pela imensa maioria dos usuários.  

A verdade atual é que diversos tipos de software se tornaram uma espécie de
*commodity*. A indústria de software, em especial aquela fração que movimenta a
Internet, há muito acabou percebendo que o valor efetivo de suas soluções (o
pote de ouro) está tanto no software como nos dados que são armazenados e
processados por esse software. Para proteger a riqueza, é natural que algumas
barreiras fossem construídas.  

Os chamados *walled gardens* são sistemas de informações cujos provedores
possuem total controle sobre as regras que regem as aplicações, dados
(utilização, armazenamento e compartilhamento), quem pode interagir com o
sistema e como essa interação será realizada. É perfeitamente possível utilizar
software livre e de código aberto para criação de sistemas com essas
características.  

O GitHub Pages em um primeiro momento não é dos sistemas fechados mais
problemáticos. Entretanto se olharmos com um pouco mais de cuidado para as
regras desse *jardim murado* percebemos algumas coisas no mínimo preocupantes:

* **Quem define o que pode ou não pode ser publicado é o GitHub.** Ainda que a
  publicação de um site na Internet seja um ato de expressão pública, ao
  utilizar o Pages o usuário escolhe deliberadamente subjulgar-se sobre as
  regras de uma instituição privada. Por mais que o conteúdo que seu site esteja
  divulgando seja legítmo e respaldado pela legislação vigente, caso a empresa
  controladora do GitHub julgue inapropriado ela poderá retirar o conteúdo do ar
  sem problema algum. É interessante notar que no tocante as regras do que é
  permitido ou não de ser publicado em plataformas fechadas geralmente há
  cláusulas bastante confusas ou subjetivas como ["content that misrepresents
  your identity or site
  purpose"](https://help.github.com/articles/what-is-github-pages/#usage-limits)
  ou ["violent or threatening content or
  activity"](https://help.github.com/articles/what-is-github-pages/#usage-limits).
  *Importante: esses mesmos termos regem a utilização do GitHub*.

* **Um serviço obrigatoriamente atrelado a utilização de outro da mesma
  empresa.** Se algum dia o usuário do Pages se descontentar com o GitHub por
  qualquer motivo e não quiser mais hospedar seu repositório Git do próprio site
  no serviço, irá precisar dar adeus as supostas comodidades do GitHub Pages.
  Isso além de claramente tirar a autonomia de quem quer **hospedar um site**,
  também é repsonsável por prender cada vez mais o usuário à empresa. É o que
  acontece com muitas pessoas que começaram utilizando o GMail e hoje possuem
  toda a vida pessoal e profissional presa nos serviços da G Suite.  

* **Limitações do serviço se tornam limitações do usuário.** Ainda que o GitHub
  Pages tivesse suporte a HTTPS desde 2009, [somente no começo de 2018 foi que o
  serviço passou a suportar HTTPS em domínios
  personalizados](https://blog.github.com/2018-05-01-github-pages-custom-domains-https/)
  (diferentes de *.github.io*). Antes disso, caso um usuário desejasse essa
  funcionalidade ele não teria nada para fazer, apenas aceitar. Quem se submete
  as regras dos *walled gardens* também se submete a priorização das empresas
  mantenedoras dos serviços.  

Esses são apenas alguns dos fatores mais evidentemente problemáticos que não são
exclusivos do GitHub Pages, mas da maioria das plataformas fechadas controladas
por empresas privadas. Pessoalmente não acho que por si só essa forma de ofertar
soluções seja boa ou ruim. Assim como as empresas podem oferecer o que quiserem
da forma que desejarem, usuários devem ter o poder de escolha. Porém, dado o
contexto de "alfabetização tecnológica" o que inicialmente parece somente uma
manifestação da liberdade de alguns (empresas) pode se tornar inadvertidamente o
prejuízo de outos (usuários).

## Transparência

Há muito tempo eu ouvi a expressão de que "cloud computing é só o computador de
outra pessoa". Quando esse computador é de uma empresa as coisas podem se
tornar bastante problemáticas. Isso porque ainda que existam malabarismos
argumentativos a função primária de uma empresa privada é a obtenção de lucro.
Como dito anteriormente, vivemos em uma época em que os dados possuem muitas
vezes mais valor do que o software. Logo colocar seus dados no computador de uma
empresa privada é literalmente colocar *moedas no já abarrotado cofrinho de
outro*. Além disso aqueles que trabalham com tecnologia sabem bem que quando
dizemos "dados" estamos nos referindo a muito mais informações do que somente
aquelas diretamente escritas em um site estático, por exemplo. De padrões
comportamentais de utilização até preferências pessoais valiosíssimas para o
mercado, a capacidade e possibilidade de obtenção de dados vai muito além de
textos puros.  

Especificamente no caso do GitHub, ao subjulgar-se sobre as regras de utilização
um usuário garante alguns direitos para a empresa no tocante aos dados
produzidos pelo usuário. Segue um [trecho dos termos de serviço atuais
(2018)](https://help.github.com/articles/github-terms-of-service/#d-user-generated-content):
*...This includes the right to do things like copy it to our database and make
backups; show it to you and other users; parse it into a search index or
otherwise analyze it on our servers; share it with other users; and perform it,
in case Your Content is something like music or video*.  

Vale destacar a passagem *analyze it on our servers*. Nós usuários não sabemos
como essas análises ou utilizações são feitas. Mais do que isso nós não
possuímos remota ideia do que "análise" pode significar no futuro para os
futuros controladores da empresa. Não ter procedimentos prejudiciais ou injustos
para com os usuários hoje não é garantia de não terão para sempre.  

Pode parecer demasiadamente injusto esse tipo de relação, e realmente é. Não
acredito que esse contexto se dê unicamente pela intenção de empresas ou
qualquer outro agente maléfico, mas sim pela assimetria das relações. As
propostas de uma grande empresa (com poucos ou nenhum concorrente)
materializadas em extensos termos de uso possuem muito mais relevância do que a
aceitação ou rejeição de um usuário. Junta-se a isso uma sociedade naturalmente
alheia as especificidades técnicas e uma comunidade técnica alienada sobre
questões de privacidade, transparência e liberdade dos usuários e tem-se um
contexto propício para relações injustas e assimétricas.  

## Responsabilidade enquanto profissional de tecnologia

Todas as abordagens expostas até aqui são passíveis de serem absorvidas e
interpretadas plenamente por cada pessoa. Usar ou não usar determinado serviço,
software ou tecnologia é, na maioria dos casos, exclusivamente opção individual.
Porém, no meu entendimento, profissionais inseridos no contexto de tecnologia
(em especial desenvolvedores de software) possuem um peso maior em suas decisões
justamente pela responsabilidade profissional. Essas pessoas além de decidirem
por si mesmas, acabam levando a influência de suas decisões e opiniões para o
resto da sociedade que tem nesses profissionais maior garantia de opiniões
baseadas em conhecimentos racionais.  

Há um motivo por encararmos com espanto um médico fuma, por exemplo. Essa é uma
atitude no mínimo inesperada segundo o entendimento comum. Pensamos que em
função do conhecimento altamente especializado daquele profissional quanto aos
melefícios do cigarro para uma pessoa, não haveria a menor condição do mesmo
tomar a decisão deliberada de partir por esse caminho. Pensando por esse lado eu
fico me perguntando quando que iremos, ao menos como comunidade de profissionais
de tecnologia, nos espantarmos quando nos depararmos com colegas de profissão
que negligenciam questões da própria privacidade digital, da sua própria
autonomia na utilização de serviços e ferramentas ou na transparência exigida
de seus provedores de soluções.  

Recentemente em conversa com conhecidos de profissão estávamos comentando sobre
a postura que uma pessoa que trabalha com desenvolvimento de software deveria
ter quando confrontado com hábitos, práticas, procedimentos ou mesmo costumes
que proporcionam má qualidade no produto sendo construído. Tanto para os
clientes quanto para os próprios profissionais que o desenvolvem. Alguns falaram
que existem empresas que não possibilitam qualquer mudança, outros se mostraram
evidentemente desanimados em tentar algo diferente. A minha posição foi mais
enfática: um profissional do desenvolvimento de software abdicar-se de exigir as
melhores condições de trabalho, as melhores práticas de qualidade por todos os
envolvidos ou mesmo lavar as mãos para desvios que ocorrem, age intencionalmente
de forma antiética. Isso é inadmissível. Para mim, não existe a "ética no
trabalho" e a ética fora dele. Ter ou não responsabilidade quanto as escolhas
tecnológicas pessoais é ser ou não ético enquanto profissional de tecnologia.  

## Diversão

Apesar da relevância dos pontos anteriores, não poderia deixar de lado outro
fator que me fez querer manter e administrar o meu próprio servidor novamente: é
divertido demais. Eu passei o último feriado prolongado de 7 de setembro focado
em colocar as coisas em produção: criar  um novo tema para o Pelican que fosse
*JavaScript Free*, procurar uma nova distribuição Linux para o VPS, fazer backup
das coisas antigas que estavam rodando em um VPS que já tinha, configurar o
servidor HTTP em uma nova distribuição, migrar os domínios, habilitar o
HTTPS, configurar subdomínios específicos para arquivos estátivos, subir outros
serviços além do site/blog pessoal entre outras coisas.  

O dia a dia de profissional do desenvolvimento há quase 10 anos proporciona
desafios interessantíssimos, coisas de outro nível que exigem competências e
habilidades diferentes. Na rotina profissional (pelo menos a minha) sou
constantemente colocado em situações onde tenho que lidar com o desconhecido.
Mas a carga de responsabilidade envolvida, as pressões corporativas e as
formalidades inerentes acabam tirando boa parte do prazer em se trabalhar. Hora
ou outra talvez precisemos encarar problemas sem toda a carga profissional.
Foram situações como essas nesse feriado que me remeteram a dezenas de anos
atrás quando eu programava justamente porque era divertido. Perder a hora de ir
dormir e acabar sonhando com uma solução que você não tinha pensado ou em um
novo serviço que poderia hospedar por mim mesmo. Tudo isso é muito mais
divertido do que um simples "push" no GitHub.  

O primeiro título desse post era "Porque eu saí do GitHub e você também
deveria". Porém uma das coisas que a gente deveria aprender é que exigir dos
outros atitudes iguais a sua é no mínimo infantil. Esperar dos outros conclusões
e pensamentos como os próprios é injusto quando isso parte de uma vontade
honesta e doentio quando isso parte de qualquer outra motivação Assim sendo, a
única pretensão desse texto é justamente ser uma autoanálise pública onde
"mastigo" meus próprios pensamentos.  

Se chegou até aqui, muito obrigado pela leitura. Abraço!
