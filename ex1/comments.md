1. PEP8 
* Переносы
* Названия файлов jsonplaseholder.py и test_Dog_API
2. Константы
```
URL = https://dog.ceo/api/breeds
response = requests.get(URL + "/husky/images")
response = requests.get(f"{URL}/husky/images")
```
3. Много одинаковых проверок
```
    assert response.status_code == 200
    assert response.json()["status"] == "success"
```
4. Вместо response["status"] лучше использовать response.("status")
5. 