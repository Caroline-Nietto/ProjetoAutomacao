#language: pt


Funcionalidade Validacao do Login do Usuario

Esquema do Cenario Login com credencial valida

    Dado que o usuario esta na pagina de login
    Quando o usuario insere as credenciais corretas "<username>" e "<password>"
        E clica para fazer o login
    Entao e redirecionado para tela de Boas Vindas
        E deve ver a "<message>"

  Exemplos:

      | username 	| password                   | message
      | tomsmith 	| SuperSecretPassword!       |  You logged into a secure area!



Esquema do Cenario Login com credencial invalida

    Dado que o usuario esta na pagina de login
    Quando o usuario insere as credenciais incorretas "<username>" e "<password>"
        E clica para fazer o login
    Entao deve ver a "<message>"
        E permanecer na tela de Login

  Exemplos:

      | username 	| password                   | message
      | tomsmith 	| 123                        |   Your password is invalid!
      | tomsmith 	|                            |   Your password is invalid!
      |          	| 123                        |   Your password is invalid!
      | elon    	| SuperSecretPassword!       |   Your password is invalid!

