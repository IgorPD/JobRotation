pertence = False

def fib(n, x):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    soma = fib(n-1, x) + fib(n-2, x)
    if soma == x:
      global pertence
      pertence = True
    return soma

n = int(input('Digite o numero para a sequencia de Fibonacci: '))
pert = int(input('Digite o numero que deseja verificar: '))
print(f'Fibonacci({n}) = {fib(n, pert)}')
print(f'{pert} pertence a sequencia de Fibonacci? {pertence}')