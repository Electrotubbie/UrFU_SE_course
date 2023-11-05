from transformers import pipeline

unmasker = pipeline('fill-mask', model='xlm-roberta-base')
# Ниже код для проверки работы модели в 1 задании, далее теряет актуальность
# text = "Hello, i'm a <mask> model."
# variants = unmasker(text)
# print('Varians:')
# print(*[variant['sequence'] for variant in variants], sep='\n')
