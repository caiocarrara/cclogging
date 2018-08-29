Title: Java Code Style (eclipse formatter e clean up)
Date: 2013-12-21 10:41
Tags: desenvolvimento, java
Slug: java-code-style-eclipse-formatter-e-clean-up  
Summary: Além de pensarmos na qualidade do código que estamos entregando para a máquina compilar, interpretar e executar, também precisamos nos importar com a qualidade do código fonte que continuará existindo para manutenções futuras. Apresento nesse artigo uma proposta de estilo de código fonte Java e como o Eclipse pode ajudar nisso.

Um ponto importante, mas que nem sempre é tratado com a seriedade que merece, é
o code style dos projetos em que trabalhamos. Seja qual for a linguagem,
escrevemos comportamentos para a máquina, mas quem mantém, altera e melhora
esses comportamentos em formato de código são humanos.  Assim sendo, nada mais
importante do que pensar nisso quando estamos escrevendo código.  

Graças as maravilhas do mundo moderno, os principais ambientes de
desenvolvimento para a plataforma Java já podem formatar e limpar o código pra
gente. No [Eclipse](http://www.eclipse.org/ "Eclipse Website"), foco desse post,
há duas funções básicas para isso: [Code
Formatter](http://help.eclipse.org/indigo/index.jsp?topic=%2Forg.eclipse.jdt.doc.user%2Freference%2Fpreferences%2Fjava%2Fcodestyle%2Fref-preferences-formatter.htm
"Help Eclipse Preferences Code Formatter") e [Code Clean
Up](http://help.eclipse.org/indigo/index.jsp?topic=%2Forg.eclipse.jdt.doc.user%2Freference%2Fpreferences%2Fjava%2Fcodestyle%2Fref-preferences-cleanup.htm
"Help Eclipse Preferences Clean Up").  O Clean Up além da formatação,  faz mais
algumas coisas no código, exemplo: declara variável como *final* quando
possível, adiciona o *this* quando necessário, organiza *imports*, etc. Ambos
são bastante configuráveis.

Eu fiz um clean up meu, com base no que acho necessário. Eu sugeriria altamente
a todos que trabalham com Java também usassem essa função.  Podem configurar um
Clean Up com as preferências pertinentes ao projeto que estão trabalhando, ou
que a equipe de desenvolvedores ache melhor.  Se desejarem, um ponto de partida
pode ser o
[caio-eclipse-cleanup.xml](https://dl.dropboxusercontent.com/u/23404136/caio-eclipse-cleanup.xml
"Arquivo Caio Eclipse Clean Up xml")

Também fiz um formatter. O que fiz é praticamente igual ao [Code Style do Google
para Java](http://google-styleguide.googlecode.com/svn/trunk/javaguide.html
"Code Style do Google para Java").  O que fiz foi alterar o espaço das
tabulações de 2 para 4 e a versão target do Java de 1.5 para 1.7. Todo o
formatador é configurável, mas o arquivo que estou usando também pode ser
utilizado como ponto de partida:
[eclipse-java-google-style.xml](https://dl.dropboxusercontent.com/u/23404136/eclipse-java-google-style.xml
"Eclipse Java Formatter by Google edited by Caio")

Para usar os arquivos que disponibilizei é simples, após o download os mesmos
precisam ser importados para os workspaces onde serão utilizados:  
**Code Formatter:**

-   <span style="letter-spacing: 0.05em;">Eclipse \> Window \>
    Preferences \> Java \> Code Style \> Formatter \> Import...</span>

**Code Cleanup:**

-   <span style="letter-spacing: 0.05em;">Eclipse \> Window \>
    Preferences \> Java \> Code Style \> Clean Up \> Import...</span>

**No dia a dia eu uso muito os atalhos:**

-   <span style="letter-spacing: 0.05em;">**Ctrl + Shift + F:** aplica a
    formatação definida no Formatter</span>
-   <span style="letter-spacing: 0.05em;">**Ctrl + Shift + O:** organiza
    os imports</span>

Com esses atalhos, aquele código escrito rapidamente para um teste, protótipo ou
mesmo exercício da faculdade, não tem mais desculpas para não ficar formatado
corretamente. Afinal, é muito rápido e fácil utilizá-los.

**Para passar o Clean Up:**  

Selecione um projeto, um pacote, um arquivo .java ou mesmo ctrl + a no arquivo
fonte, clique com o botão direito: Source \> Clean Up.

É isso. Espero que o código, além de performático e muito bom para as máquinas,
também fique ótimo para ser lido pelos programadores!

Abraço!

