# practice_SE
Practical lessons in software engineering number.
## Участники команды
- Сорокин Андрей Дмитриевич (РИМ-130907)
- Кунгурцев Дмитрий Станиславович (РИМ-130907)
## Опробование модели
Для того, чтобы попробовать модель на практике, в облаке streamlit было развернёто веб-приложение, которое доступно по ссылке: https://practice-se.streamlit.app/
## Описание модели
С помощью рассматриваемой модели выполняется заполнение пропущенного слова на наиболее подходящее. 
В качестве входных данных принимается предложение на **английском языке** с помеченным ```<mask>``` пропущенным словом.
## Использование модели
```python
from transformers import pipeline
unmasker = pipeline('fill-mask', model='roberta-base')
unmasker("Hello I'm a <mask> model.")

[{'score': 0.21280737221240997,
  'token': 2734,
  'token_str': ' fashion',
  'sequence': "Hello, i'm a fashion model."},
 {'score': 0.20130988955497742,
  'token': 2943,
  'token_str': ' male',
  'sequence': "Hello, i'm a male model."},
 {'score': 0.05615966394543648,
  'token': 2038,
  'token_str': ' professional',
  'sequence': "Hello, i'm a professional model."},
 {'score': 0.028213199228048325,
  'token': 18150,
  'token_str': ' freelance',
  'sequence': "Hello, i'm a freelance model."},
 {'score': 0.026147497817873955,
  'token': 2182,
  'token_str': ' female',
  'sequence': "Hello, i'm a female model."}]
```
## Использование веб-приложения и API из репозитория
### Установка библиотек
Для того, чтобы использовать функции локально, необходимо установить библиотеки из requirements.txt, написав в командной строке ОС:
```
pip install -r requirements.txt
```
### Запуск веб-приложения
После установки необходимых библиотек для запуска веб-приложения требуется выполнить следующую команду ***из директории с файлами ```unmask.py``` и ```streamlit_web.py```***:
```
streamlit run ./streamlit_web.py
```
### Запуск API
Для запуска API необходимо выполнить:
```
uvicorn api:app
```
Для использования модели через API необходимо выполнить POST-запрос по соответствующему адресу, например:
```
curl -X 'POST' 'http://127.0.0.1:8000/unmask/' -H 'Content-Type: application/json' -d '{"text": "Method <mask> is HTTP request"}'
```  
