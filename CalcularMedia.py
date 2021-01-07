def calcular_media(notas):
  quantidade = len(notas)
  soma = sum(notas)
  media = soma / quantidade
  return media

def verificar_aprovacao(media):
    if media >= 6:
      print('Aluno Aprovado!')
    else:
        print('Aluno reprovado!')


notas = [6.2,5.5,4.5,7.5]
media = calcular_media(notas)
print(f'A média do aluno é: {media:.1f}')
verificar_aprovacao(media)