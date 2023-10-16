from transformers import pipeline

unmasker = pipeline('fill-mask', model='xlm-roberta-base')

text = "Hello, i'm a <mask> model."
variants = unmasker(text)
print('Varians:')
print(*[variant['sequence'] for variant in variants], sep='\n')
