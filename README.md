# projeto_automacao

Olá, Tudo bem ?

Segue minha solução para o teste apresentado. Tentei mostrar algumas tecnicas que conheço. Fico a disposição para dúvidas e explicações sobre esse modelo.

Utilizei Selenium Webdriver com Python para realizar os testes front-end, Postman para realizar os testes back-end e a extensão Cucumber Scenario no Pycharm para criar os cenários de teste de ambos, utilizando o método BDD escrito em Gherkin. Automação dos testes da API Rest, utilizei o Pytest.

* Para o Teste 1 - Criei o arquivo com os cenarios de testes: 'validacao_user_settings.feature' que está no caminho abaixo:

  ° projeto_automacao > features  

* Para o Teste 2 - criei os arquivos com os cenários de testes: 'test_frontEnd_botao_start.fealure' e 'test_frontEnd_login.fealure' que está no caminho abaixo:

     ° projeto_automacao > features  

  Para a Automação Front-End criei o arquivo:

  ° projeto_automacao > meu_projeto  
  
* Para o Teste 3 - Criei o arquivo com os cenarios de testes: 'test_backEnd.feature' que está no caminho abaixo:

   ° projeto_automacao > features

  Para os testes realizados da API Rest, disponibilizei o arquivo: 'Validar Users.postman_collection.json'  que está no caminho abaixo:

   ° projeto_automacao > Collection_Postman
  
  Para a Automação Back-End, disponibilizei o arquivo:  'api_tests.py' que está no caminho abaixo:

  ° projeto_automacao > Automacao back-end

Para a automação do teste Back-End certifique-se de ter o PyCharm instalado. Se não tiver o pytest e a biblioteca requests, instale-os via pip:

pip install requests pytest

Para rodar todos os testes:

pytest api_tests.py

Para rodar apenas um teste específico:

pytest api_tests.py::test_post_new_user

Isso executará apenas o teste test_post_new_user() do arquivo api_tests.py.
Substitua test_post_new_user pelo nome da função do teste que você deseja executar.

  
