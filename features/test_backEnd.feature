#language: pt


Funcionalidade Testes para o endpoint relacionado aos usuarios da API
--- url base: http://jsonplaceholder.typicode.com/users
--- validar o metodo get, put, post, delete da API
--- validar o JSON Schema e http code das respostas


#### CENARIOS PARA O METODO GET ###

  Cenario Obter usuarios (GET)
    Dado a API endpoint "http://jsonplaceholder.typicode.com/users"
    Quando usuario realiza uma solicitacao GET sem passar parametro
    Entao o codigo de resposta deve ser 200
    E a resposta deve seguir o esquema JSON esperado para usuarios
    E deve trazer na resposta uma lista com todos os usuarios


  Cenario Obter usuario por ID (GET /{id})
    Dado um ID de usuario existente na base
    Quando realiza uma solicitacao GET para "/users/{id}"
    Entao o codigo de resposta deve ser 200
    E a resposta deve seguir o esquema JSON esperado para um usuario
    E deve trazer na resposta apenas o cadastro do usuario referente ao ID informado na requisicao

Cenario Obter usuario por E-mail (GET /email)
    Dado um email de usuario existente na base
    Quando realiza uma solicitacao GET para "/users
    E no header inseri email com valor do email
    Entao o codigo de resposta deve ser 200
    E a resposta deve seguir o esquema JSON esperado para um usuario
    E deve trazer na resposta apenas o cadastro do usuario referente ao email informado na requisicao


### CENARIO PARA O METODO POST ###

  Cenario Criar um novo usuario (POST)
    Dado um novo usuario com dados validos
    Quando realiza uma solicitacao POST para "/users"
    Entao o codigo de resposta deve ser 201
    E a resposta deve seguir o esquema JSON esperado para um usuario criado
    E os dados do novo usuario devem ser salvos na tabela Users


### CENARIO PARA O METODO PUT ###

  Cenario Atualizar dados de um usuario existente (PUT /{id})
    Dado um ID de usuario existente
    E novos dados para atualizacao
    Quando realiza uma solicitacao PUT para "/users/{id}"
    Entao o codigo de resposta deve ser 200
    E a resposta deve seguir o esquema JSON esperado para um usuario atualizado
    E os dados atualizados devem ser salvos na tabela Users


### CENARIO PARA O METODO DELETE ###

  Cenario Deletar um usuario existente (DELETE /{id})
    Dado um ID de usuario existente
    Quando realiza uma solicitacao DELETE para "/users/{id}"
    Entao o codigo de resposta deve ser 200
    E o registro do ID utilizado na requisicao deve ser exlcuido da tabela Users
