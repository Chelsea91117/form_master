import requests

# URL приложения
url = "http://localhost:5000/get_form"

# Тестовые данные
test_data = [
    {
        "email": "test@example.com",
        "phone": "+7 123 456 78 90",
        "order_date": "2024-12-01"
    },
    {
        "user_email": "feedback@example.com",
        "comments": "Great service!"
    },
    {
        "unknown_field": "Some text",
        "another_field": "example@example.com"
    }
]

# Выполнение запросов
for data in test_data:
    response = requests.post(url, data=data)
    print(f"Request: {data}")
    print(f"Response: {response.json()}")
