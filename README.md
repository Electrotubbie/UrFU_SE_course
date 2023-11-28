# practice_SE
Practical lessons in software engineering number.
## Участники команды
- Сорокин Андрей Дмитриевич (РИМ-130907)
- Кунгурцев Дмитрий Станиславович (РИМ-130907)
## Описание модели
С помощью рассматриваемой модели выполняется заполнение пропущенного слова на наиболее подходящее. 
В качестве входных данных принимается предложение с помеченным ```<mask>``` пропущенным словом.
## Использование модели
```python
from transformers import pipeline
unmasker = pipeline('fill-mask', model='xlm-roberta-base')
unmasker("Hello I'm a <mask> model.")

[{'score': 0.10563907772302628,
  'sequence': "Hello I'm a fashion model.",
  'token': 54543,
  'token_str': 'fashion'},
 {'score': 0.08015287667512894,
  'sequence': "Hello I'm a new model.",
  'token': 3525,
  'token_str': 'new'},
 {'score': 0.033413201570510864,
  'sequence': "Hello I'm a model model.",
  'token': 3299,
  'token_str': 'model'},
 {'score': 0.030217764899134636,
  'sequence': "Hello I'm a French model.",
  'token': 92265,
  'token_str': 'French'},
 {'score': 0.026436051353812218,
  'sequence': "Hello I'm a sexy model.",
  'token': 17473,
  'token_str': 'sexy'}]
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
