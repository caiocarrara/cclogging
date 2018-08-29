Title: Crie as suas oportunidades para aprender  
Date: 2014-02-09 17:34  
Tags: carreira  
Slug: crie-as-suas-oportunidades-para-aprender  
Summary: Não espere que surja um tempo livre na sua rotina para aprender algo novo. Vivemos várias oportunidades no dia-a-dia que poderão ser ótimas chances de conhecer algo novo, basta sermos mais sensíveis a esses momentos e criarmos nossas oportunidades para aprender.  

Nós somos muito acostumados a tentar separar um tempo para fazer um curso,
assistir uma palestra ou aprender uma nova linguagem de programação, dentre
outras coisas. A questão é que para quem já está trabalhando, ou às vezes só
estudando ainda, esse tempo pode nunca aparecer. São tantas as nossas
atribuições diárias que os estudos e novos conhecimentos sempre ficam para
depois, ou nunca. Hoje eu tenho a oportunidade de estar trabalhando em uma
Startup que valoriza muito o conhecimento e nos motiva a separar um tempo
semanal para focarmos em estudos, inovação e projetos paralelos. Porém nem
sempre foi assim.

No ano passado eu estava trabalhando em outra empresa, com um ambiente
formidável também, porém mais clássico de focar o tempo dos colaboradores 100%
em projetos da própria empresa. Eu estava trabalhando em um projeto que envolvia
tecnologia Microsfot .Net e Adobe ActionScript (=P). Eu nunca fui fã dessas
tecnologias e, para ser sincero, tenho muito pouco interesse em aprofundar meus
conhecimentos sobre elas. Mas comigo "missão dada é missão cumprida, parceiro",
logo fiz o meu melhor!

Em uma ocasião nesse projeto apareceu uma tarefa daquelas que você facilmente
passa para o estagiário mais próximo (hahaha). Precisava ser atualizada dezenas
e dezenas de arquivos .html do help do sistema. Havia muitas páginas e cada help
era traduzido para uma dezena de idioma.  Teria que abrir arquivo por arquivo,
localizar um trecho do código específico e substituir por outro trecho
específico também. No mesmo momento acendeu aquela *lâmpada* de uma nova ideia!

No mesmo período eu estava com um projeto pessoal sendo desenvolvido em
Python/Django e eu vivo constantemente pesquisando e *brincando* com Python
sempre que posso. Tendo em vista a tarefa que precisava ser feita, pensei: "por
que não usar Python pra isso?". Eu poderia, claro, ter usado qualquer outra
linguagem, poderia ter feito a tarefa na mão (se fosse louco!), poderia ter
feito de conta que a tarefa não existia (o que já vi acontecer em empregos por
ai), mas não! Resolvi criar a minha oportunidade em codificar em Python.

Em alguns minutos já tinha meu ambiente Windows preparado para rodar Python e
versionar meu projeto no Github. Mais alguns minutos depois eu tinha o script
pronto! Bastava um comando no cmd do Windows passando como argumento o diretório
base dos arquivos .html, o caracter que deveria ser removido e o caracter que
seria inserido. O help estava versionado então eu rodei o script de primeira,
sem medo, para ver o que dava e não é que funcionou?! O script em questão segue
abaixo e também pode ser acessado no [meu
Github](https://github.com/cacarrara/py_scripts/blob/master/replace_in_all_files.py
"Github do Caio Carrara python scripts"):

    :::python  
    # coding: utf-8  
    import os  
    from sys import argv  

    def replace_in_all_files(parent_folder_path, oldChar, newChar):  
        """Replace the oldChar for newChar in all text  
        files found in parent_folder_path and its children  
        directories.  
        """  
        filenames = os.listdir(parent_folder_path)

        for filename in filenames:  
            filename = os.path.join(parent_folder_path, filename)

            if os.path.isdir(filename):  
                replace_in_all_files(filename, oldChar, newChar)  
            else:  
                arq = open(os.path.join(parent_folder_path, filename), 'r')  
                oldContent = arq.readlines()  
                arq.close()

                arq = open(os.path.join(parent_folder_path, filename), 'w')  
                newContent = ""  
                for line in oldContent:  
                newContent += line.replace(oldChar, newChar)  
                arq.write(newContent)  
                arq.close()  
                print "OK: " + filename

    if __name__ == "__main__":  
    if len(argv) \< 3:  
        print "You need to inform all params: rootPath, oldChar, newChar"  
    else:  
        rootPath = str(argv[1])  
        oldChar = str(argv[2])  
        newChar = str(argv[3])  
        replace_in_all_files(rootPath, oldChar, newChar)  

Independente da qualidade do código, da performance, se seguiu ou não os
padrões, o importante é manter em mente que todo momento é o momento certo para
aprender e fazer algo novo. Não compensa ficar esperando até que apareça o
momento certo, mas sim fazer de cada momento o certo para você.

Grande abraço e foco nos estudos pessoal!

