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
## Использование веб-приложения из репозитория
Для того, чтобы использовать веб приложение локально, необходимо установить библиотеки из requirements.txt, написав в командной строке ОС:
```
pip install -r requirements.txt
```
После установки необходимых библиотек требуется выполнить следующую команду ***из директории с файлами ```unmask.py``` и ```streamlit_web.py```***:
```
streamlit run ./streamlit_web.py
```
