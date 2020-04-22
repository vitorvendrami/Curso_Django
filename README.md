# Instruções Git

#### Configurações de Repositório

* Iniciar, Apagar e ver Status do Repositório
                
        git init // inicia repositório
        rm -rf .git //deleta repositório 
        git status // verifica o status do repositório

#### Configurações Globais
* Nome e Endereço de email global
                
        git config --global user.name nome
        git config --global user.email email

* Mostrar as configurações globais
        
        git config --global --list
        
#### Commits
##### Para efetuar um commit deve-se seguir 2 passos:

1. Mover o arquivo para Staged
        
        git add nome_do_arquivo //move o arquivo para staged 
        git add . //move todos os arquivos mostrados p/ staged
2. Fazer o commit
        
        git commit -m "mensagem de commit" //Faz o commit
    
* atalho para fazer isso desde que o arquivo não esteja em Untracked
    
        git commit -am "mensagem de commit" // passa para staged e já faz o commit 
   
#### Visualização dos Commits

* Mostrar commits

        git log // mostra todos os commits
        git log --oneline // mostra commits em única linha
        
* Mostra os ultimos n commits
        
        git log -n(numeros dos ultimos commits a serem mostrados) //mostra os ultimos n commits
        
* Mostra o status do ultimo commit        
        
        git log -1 --stat //mostra quantas linhas adicionadas e excluidas no commit
        
* Mostra commits com o autor pesquisado        
        
        git log --author=nome do autor // mostra commits do autor pesquisado
        
* Mostra todos os commits de todas as branchs        
        
        git log --all // mostra todos os commits de todas as branchs
        
 * Mostra graficamente a branch
        
        git log --graph //mostra graficamente a branch
        
 * Mostra o que aconteceu com o commit
 
        git show hash_do_commit //mostra alterações do commit
        
#### Visualização entre diferenças do mesmo commit

* Mostra diferença entre arquivo e seu estado anterior
        
        git diff (arquivo)//mostra a diferença entre um arquivo e o seu estado anterior
        git diff --staged 
        git diff hashpai..hasfilho // mostra as alterações entre os commits
        
#### Alterações no(s) commit(s)
   
        git checkout --arquivo // discarta alterações que não foram para o stage
        git reset --arquivo // tira o arquivo da stage
        git reset --soft hash_pai // pega o arquivo comitado e volta pra stage
        git reset --mixed hash_pai // pega o arquivo comitado e volta pra modified
        git reset --hard hash_pai // apaga o comit e as alterações
        git revert hashdocommit "mensagem" ou --no-edit // faz revert do commite
        git rm nome do arquivo// deleta tudo arquivo e modificações dos filhos
        git mv nomeantigo nomenovo // muda nome arquivo

        
### Conexão com o repositório remoto
 
* Conectar a um repositório do git
 
        git remote add origin urldogit//ligar o git no repositório do github
        
* Verificar onde está conectado e URL 
        
        git remote // verifica onde está conectado o repositorio
        git remote -v //mostra o url do repositório
        
* Upload de arquivos pro repositório
        
        git push origin master // sobe os arquivos pro git
        git push origin nomedabranchlocal:nomedabranchremota // Sobe os arquivos de uma branch local para outra do servidor 
        
* Download de arquivos do repositório  
        
        git pull origin master // pega o repositorio atualizado do git
        
* Clona um repositório do git
        
        git clone url nome(nome do repositorio opcional) // clona um repositorio do git 
        
### Comandos para Branchs
 
* Criar Branch

        git branch nome // cria branch com o nome

* Mostra todas as branchs existentes
        
        git branch //mostra as branch que existem o * mostra qual branch está

* Mostra todas as branchs remotas

        git branch -r

* Cria branch 'truncada'

        git branch nomecria nomedaquetrunca

* Muda de branch 

        git checkout nome_Da_branch

* Deleta branch

        git branch -d nomedabranch 

* Junta branchs com merge

        git merge nome_da_branch

* Junta branchs com rebase      
        
        git rebase nome_da_branch        
        
     