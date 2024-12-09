from flask import Flask, request, jsonify
import re
from pymongo import MongoClient

app = Flask(__name__)

# Подключение к базе данных MongoDB
client = MongoClient("mongodb://mongo:27017/")
db = client["form_templates"]
templates_collection = db["templates"]


# Функция валидации поля
def validate_field(value):
    if re.match(r'^\+7 \d{3} \d{3} \d{2} \d{2}$', value):
        return "phone"
    elif re.match(r'^\d{2}\.\d{2}\.\d{4}$', value) or re.match(r'^\d{4}-\d{2}-\d{2}$', value):
        return "date"
    elif re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', value):
        return "email"
    else:
        return "text"


# Эндпоинт для обработки формы
@app.route('/get_form', methods=['POST'])
def get_form():
    # Получение данных из запроса
    data = request.form.to_dict()

    # Получение всех шаблонов из базы данных
    templates = templates_collection.find()

    # Проверка данных на соответствие шаблонам
    for template in templates:
        is_match = all(
            field in data and validate_field(data[field]) == template[field]
            for field in template if field != "name"
        )
        if is_match:
            return jsonify({"template_name": template["name"]})

    # Если совпадений не найдено, возвращаем типы полей
    field_types = {key: validate_field(value) for key, value in data.items()}
    return jsonify(field_types)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
