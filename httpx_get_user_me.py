import httpx  # Импортируем библиотеку HTTPX

# Инициализируем JSON-данные, которые будем отправлять в API
login_payload = {
    "email": "user@examp.com",
    "password": "123"
}

# Выполняем POST-запрос к эндпоинту /api/v1/authentication/login
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
# Выводим JSON-ответ и статус-код
print("Status code:", login_response.status_code)
print("Login response:", login_response_data)

#Забираем accessToken и передаем в Client
access_Token=login_response_data['token']['accessToken']
client = httpx.Client(headers={"Authorization": f"Bearer {access_Token}"})

# Выполняем GET-запрос к эндпоинту /api/v1/users/me
users_me_response = client.get("http://localhost:8000/api/v1/users/me")
# Выводим JSON-ответ и статус-код
print("Status code:", users_me_response.status_code)
print("Users me response", users_me_response.json())

