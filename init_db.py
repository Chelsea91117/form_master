from pymongo import MongoClient

# Подключение к MongoDB
client = MongoClient("mongodb://mongo:27017/")
db = client["form_templates"]
templates_collection = db["templates"]

# Очистка и заполнение базы данных
templates_collection.delete_many({})
templates_collection.insert_many([
    {
        "name": "Order Form",
        "email": "email",
        "phone": "phone",
        "order_date": "date"
    },
    {
        "name": "Feedback Form",
        "user_email": "email",
        "comments": "text"
    }
])

print("Database initialized!")
