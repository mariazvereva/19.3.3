import json
import requests

#Добавление нового питомца (POST)
data={"id": 0,"category": {"id": 0,"name": "dog"},
      "name": "Bob",
      "photoUrls": ["no foto"],
      "tags": [{"id": 0,"name": "string"}],
      "status": "available"}
res_add_new_pet= requests.post(f"https://petstore.swagger.io/v2/pet",
                               headers={'accept':'application/json', 'Content-Type':'application/json'},
                               data=json.dumps(data))

print(f"Статус ответа на POST запрос- ", res_add_new_pet.status_code)
print(f"Ответ - ", res_add_new_pet.text)

#Обновление данных о существующем питомце (PUT)
pet_id = "99223372036854649710"
new_data={"id": pet_id,"category": {"id": 0,"name": "dog"},
      "name": "Mike",
      "photoUrls": ["no foto"],
      "tags": [{"id": 0,"name": "string"}],
      "status": "available"}
res_update_pet= requests.put(f"https://petstore.swagger.io/v2/pet",
                               headers={'accept':'application/json', 'Content-Type':'application/json'},
                               data=json.dumps(new_data))

print(f"Статус ответа на PUT запрос- ", res_update_pet.status_code)
print(f"Ответ - ", res_update_pet.text)

# Поиск питомца по ID (GET)
res_find_id= requests.get(f"https://petstore.swagger.io/v2/pet/{pet_id}",
                               headers={'accept':'application/json', 'Content-Type':'application/json'})
print(f"Статус ответа на GET запрос- ", res_find_id.status_code)
print(f"Ответ - ", res_find_id.text)

# Удаление питомца (DELETE)
res_delete_pet= requests.delete(f"https://petstore.swagger.io/v2/pet/{pet_id}",
                               headers={'accept':'application/json', 'Content-Type':'application/json'},
                                data=json.dumps(new_data))
print(f"Статус ответа на DELETE запрос- ", res_delete_pet.status_code)
print(f"Ответ - ", res_delete_pet.text)

