palavra = input()
invertida=''
for c in list(palavra)[::-1]:
  invertida+=c

print(f'A palavra invertida fica: {invertida}')
