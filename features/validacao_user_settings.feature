Funcionalidade Validar a tela Settings
-- Usuario esta na tela Settings e quer ver as informacoes apresentadas no cadastro:
-- Dados dos cards no topo da pagina
-- Numero de amigos, quantidade de fotos, comentarios
-- Alterar os dados do cadastro
-- Validar os dados apresentados a direita da tela com o resumo do usuario

Contexto Dado que usuario esta logado e na pagina Settings
  Dado que o usuario esta logado com email: jesse@example.com
  E na tela Settings


#### VALIDACAO DOS CARDS ####

Cenario  Validar o card 'Traffic'

    Quando visualiza o card 'Traffic'
    Entao deve ser apresentado o mesmo numero retornado na API "return_traffic"
    E o percentual apresentado deve ser o mesmo numero retornado na API "return_percent_traffic"


Cenario  Validar o card 'New Users'

    Quando visualiza o card 'New Users'
    Entao deve ser apresentado o mesmo numero retornado na API "return_new_users"
    E o percentual apresentado deve ser o mesmo numero retornado na API "return_percent_new_user"


Cenario  Validar o card 'Sales'

    Quando visualiza o card 'Sales'
    Entao deve ser apresentado o mesmo numero retornado na API "return_sales"
    E o percentual apresentado deve ser o mesmo numero retornado na API "return_percent_sales"


Cenario  Validar o card 'Performance'

    Quando visualiza o card 'Performance'
    Entao deve ser apresentado o mesmo percentual retornado na API "return_percent_performance"
    E o percentual apresentado deve ser o mesmo numero retornado na API "return_last_percent_performance"


  #### VALIDACAO MY ACCOUNT ####

  ### USER INFORMATION ###

Esquema do Cenario  Validacao dos dados apresentados em User Information

    Quando visualiza as informacoes em User Information
    Entao deve ser apresentado os <campos>
    E e os <dados> de acordo com o que esta salvo na tabela

Exemplos:

  |campo         |dados             |
  |username      |lucky.jesse       |
  |email address |jesse@exemple.com |
  |first name    |Lucky             |
  |last name     |Jesse             |


### CONTACT INFORMATION ###

Esquema do Cenario  Validacao dos dados apresentados em User Information

    Quando visualiza as informacoes em User Information
    Entao deve ser apresentado os <campos>
    E e os <dados> de acordo com o que esta salvo na tabela

Exemplos:

  |campo         |dados                                                  |
  |address       |Bld Mihail Kogalniceanu, nr. 8 Bl 1, Sc 1, Ap 09       |
  |city          |New York                                               |
  |country       |United States                                          |
  |postal code   |Postal Code                                            |


### ABOUT ME ###

Esquema do Cenario  Validacao dos dados apresentado em About Me

    Quando visualiza as informacoes em About Me
    Entao deve ser apresentado o <campo>
    E e os <dados> de acordo com o que esta salvo na tabela

Exemplo:

  |campo         |dados                                                                               |
  |about me      |A beautiful UI Kit and Admin for React & Tailwind CSS. It is Free and Open Source.  |


#### EDICAO DOS CAMPOS EM MY ACCOUNT ####

  ### USER INFORMATION ###

Esquema do Cenario validar a edicao dos campos no quadro User Information

  Quando visualiza os '<campos>' do quadro User Information
  Então o campo deve ser editavel
  E seguir as '<regras>'
  E as informacoes alteradas devem ser salvas corretamente na tabela

  Exemplos:
    |campos      |regras                                                                                                         |
    |username    |todos as letras devem ficar minusculas, aceitar numeros e letras, aceitar minimo de 3 caracteres e maximo de 20|
    |email Adress|todos as letras devem ficar minusculas, estar com formato de e-mail valido, aceitar no maximo 30 caracteres    |
    |First Name  |Aceitar no maximo 20 caracteres, não aceitar numeros, aceitar caracteres especiais como acentos                |
    |Last Name   |Aceitar no maximo 80 caracteres, não aceitar numeros, aceitar caracteres especiais como acentos                |


##### CONTACT INFORMATION #####

Esquema do Cenario: validar a edição dos campos do quadro Contact Information

  Quando visualiza os '<campos>' do quadro Contact Information
  Então o campo deve ser editável
  E seguir as '<regras>'
  E as informacoes alteradas devem ser salvas corretamente na tabela

Exemplos:
    |campos      |regras                                                                                          |
    |address     |não aceitar em branco, aceitar numeros e letras, aceitar minimo de 5 caracteres e maximo de 80  |
    |city        |não aceitar em branco, aceitar somente letras, aceitar minimo de 3 caracteres e maximo de 30    |
    |country     |não aceitar em branco, aceitar somente letras, aceitar minimo de 3 caracteres e maximo de 30    |
    |postal code |não aceitar em branco, Aceitar somente numeros, aceitar somente 8 caracteres                    |


#####  ABOUT ME  #####

Esquema do Cenario: validar a edição dos campos do quadro About Me

  Quando visualiza o '<campo>' do quadro About me
  Então o campo deve ser editável
  E seguir as '<regras>'
  E as informacoes alteradas devem ser salvas corretamente na tabela

  Exemplo:
    |campo       |regras                                                                                   |
    |about me    |aceitar em branco, aceitar numeros e letras, maximo de 500, Aceitar emojis|


#### VALIDACAO DADOS A DIREITA DA TELA RESUMO SOBRE O USUARIO ####

Cenario: validar se a foto exibida e a mesma que a foto cadastrada
  Quando visualiza o campo da foto do usuário
  Então  verifica se a foto exibida e a mesma que a cadastrada no banco de dados Users


Cenario: validar o total de Friends, Photos, Comments do usuario
  Quando visualiza o total de Friends, Photos, Comments do usuario
  Então o total de Friends deve ser o mesmo que o valor retornado na API 'friens_user'
  E o total de Photos deve ser o mesmo que o valor retornado na API 'photos_user'
  E o total de Comments deve ser o mesmo que o valor retornado na API 'comments_user'


Cenario: validar o nome, sobrenome e o endereço do usuário
  Quando visualiza os campos Nome e Endereço
  Então o nome de ser o concatenacao dos campos First_Name e Last_Name registrados no banco
  E o Endereço deve ser a concatenacao dos campos City e Country resgistrados no banco


Cenario: validar o local de trabalho e a formação Academica
  Quando visualiza os Local de Trabalho e a formação academica
  Então o campo local de trabalho deve ser o mesmo que o registrado na base de dados Users tabela Works
  E o campo formacao Academica deve ser o mesmo que o registrado na base de dados Users tabelas Schools


Cenario: validar o resumo do usuario
  Quando visualiza o resumo do usuario
  Então deve exibir os 200 primeiros caractes do texto salvo no banco de dados Users - About Me
  E caso esteja em branco o campo no banco esse quadro resumo nao deve ser exibido