# api_tests.py

import requests
import pytest


def test_get_all_users():
    # Faz a requisição GET para obter todos os usuários
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    json_response = response.json()

    # Valida o código de status da resposta (deve ser 200)
    assert response.status_code == 200, f'Código de status esperado: 200, Código obtido: {response.status_code}'

    # Valida a estrutura do JSON retornado para todos os usuários
    assert isinstance(json_response, list), "A resposta não é uma lista de usuários"
    assert len(json_response) > 0, "A lista de usuários está vazia"

    # Valida a estrutura de um usuário na lista (pode ser ajustado conforme a estrutura real da resposta)
    user_keys = ['id', 'name', 'username', 'email', 'address', 'phone', 'website', 'company']
    for user in json_response:
        for key in user_keys:
            assert key in user, f"Campo '{key}' está ausente em um usuário da lista"


def test_validate_json_structure_for_specific_id():
    # Defina o ID do usuário que você deseja obter (neste exemplo, usei o ID 1)
    user_id = 1

    # Faz a requisição GET específica para um ID
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}')
    json_response = response.json()

    # Valida o código de status da resposta
    assert response.status_code == 200, f'Código de status esperado: 200, Código obtido: {response.status_code}'

    # Valida a estrutura do JSON retornado para o ID específico
    assert 'id' in json_response, "Campo 'id' está ausente no JSON"
    assert 'name' in json_response, "Campo 'name' está ausente no JSON"
    assert 'username' in json_response, "Campo 'username' está ausente no JSON"
    assert 'email' in json_response, "Campo 'email' está ausente no JSON"

    assert 'address' in json_response, "Campo 'address' está ausente no JSON"
    address = json_response['address']
    assert 'street' in address, "Campo 'street' está ausente em 'address'"
    assert 'suite' in address, "Campo 'suite' está ausente em 'address'"
    assert 'city' in address, "Campo 'city' está ausente em 'address'"
    assert 'zipcode' in address, "Campo 'zipcode' está ausente em 'address'"

    geo = address['geo']
    assert 'lat' in geo, "Campo 'lat' está ausente em 'geo'"
    assert 'lng' in geo, "Campo 'lng' está ausente em 'geo'"

    assert 'phone' in json_response, "Campo 'phone' está ausente no JSON"
    assert 'website' in json_response, "Campo 'website' está ausente no JSON"

    assert 'company' in json_response, "Campo 'company' está ausente no JSON"
    company = json_response['company']
    assert 'name' in company, "Campo 'name' está ausente em 'company'"
    assert 'catchPhrase' in company, "Campo 'catchPhrase' está ausente em 'company'"
    assert 'bs' in company, "Campo 'bs' está ausente em 'company'"


def test_get_user_by_email():
    # Define o e-mail do usuário que você deseja obter
    user_email = "Lucio_Hettinger@annie.ca"

    # Faz a requisição GET para obter informações do usuário com base no e-mail
    response = requests.get(f'https://jsonplaceholder.typicode.com/users?email={user_email}')
    json_response = response.json()

    # Valida o código de status da resposta
    assert response.status_code == 200, f'Código de status esperado: 200, Código obtido: {response.status_code}'

    # Verifica se a resposta não está vazia e se há pelo menos um usuário com o e-mail especificado
    assert json_response, f"Nenhum usuário encontrado com o e-mail: {user_email}"
    assert any(
        user['email'] == user_email for user in json_response), f"Nenhum usuário encontrado com o e-mail: {user_email}"

    # Obtém informações do primeiro usuário encontrado com o e-mail especificado
    user_info = next(user for user in json_response if user['email'] == user_email)

    # Valida a estrutura do JSON retornado para o usuário encontrado
    assert 'id' in user_info, "Campo 'id' está ausente no JSON"
    assert 'name' in user_info, "Campo 'name' está ausente no JSON"
    assert 'username' in user_info, "Campo 'username' está ausente no JSON"
    assert 'email' in user_info, "Campo 'email' está ausente no JSON"

    assert 'address' in user_info, "Campo 'address' está ausente no JSON"
    # Valida outras chaves e estruturas conforme necessário


def test_post_new_user():
    # Informações para o corpo da requisição POST
    new_user_data = {
        "name": "Elon Gate",
        "username": "Elogate",
        "email": "testexample@april.biz",
        "address": {
            "street": "Rua dos estados",
            "suite": "Apt. 1",
            "city": "Paris",
            "zipcode": "98860-2222",
            "geo": {
                "lat": "-37.3159",
                "lng": "81.1496"
            }
        },
        "phone": "1-999-999-8031 x56442",
        "website": "testpost.org",
        "company": {
            "name": "Test-Pixeon",
            "catchPhrase": "Eu vou conseguir",
            "bs": "evoluir com este teste"
        }
    }

    # Faz a requisição POST com os dados do novo usuário
    response = requests.post('https://jsonplaceholder.typicode.com/users', json=new_user_data)
    json_response = response.json()

    # Valida o código de status da resposta (deve ser 201 para criação bem-sucedida)
    assert response.status_code == 201, f'Código de status esperado: 201, Código obtido: {response.status_code}'

    # Valida se a estrutura do JSON retornado corresponde aos dados enviados
    for key, value in new_user_data.items():
        assert key in json_response, f"Campo '{key}' está ausente no JSON retornado"
        assert json_response[key] == value, f"O valor para o campo '{key}' não corresponde ao esperado"

    # Validação adicional, se necessário


def test_put_user_data():
    # Informações para o corpo da requisição PUT
    updated_user_data = {
        "name": "Elon Gate",
        "username": "ElogateCn",
        "email": "testexamplecn@april.biz",
        "address": {
            "street": "Rua dos Estados",
            "suite": "Apt. 1",
            "city": "Paris",
            "zipcode": "98860-1111",
            "geo": {
                "lat": "-37.3159",
                "lng": "81.1496"
            }
        },
        "phone": "1-999-999-8031 x56442",
        "website": "testpost.org",
        "company": {
            "name": "Test-Pixeon",
            "catchPhrase": "Eu vou conseguir",
            "bs": "aproveitar para aprender com este teste"
        }
    }

    # Faz a requisição PUT com os dados atualizados do usuário no mesmo endpoint
    response = requests.put('https://jsonplaceholder.typicode.com/users/1', json=updated_user_data)
    json_response = response.json()

    # Valida o código de status da resposta (deve ser 200 para atualização bem-sucedida)
    assert response.status_code == 200, f'Código de status esperado: 200, Código obtido: {response.status_code}'

    # Valida se a estrutura do JSON retornado corresponde aos dados atualizados enviados
    for key, value in updated_user_data.items():
        assert key in json_response, f"Campo '{key}' está ausente no JSON retornado"
        assert json_response[key] == value, f"O valor para o campo '{key}' não corresponde ao esperado"

    # Validação adicional, se necessário


def test_delete_user_by_id():
    # Define o ID do usuário que deseja excluir (neste exemplo, usaremos o ID 10)
    user_id = 10

    # Faz a requisição DELETE para excluir o usuário com o ID especificado
    response = requests.delete(f'https://jsonplaceholder.typicode.com/users/{user_id}')

    # Valida o código de status da resposta (deve ser 200 para exclusão bem-sucedida)
    assert response.status_code == 200, f'Código de status esperado: 200, Código obtido: {response.status_code}'

