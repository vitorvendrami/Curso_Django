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
   
##### Visualização dos Commits

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
        
 