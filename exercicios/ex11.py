large = float(input('qual a largura da parede: '))
height = float(input('qual a altura da parede: '))

area = large * height
qtd_tinta = area / 2

print(f'a area da parede é {area:.2f} m2')
print(f'a quantidade de tinta é {qtd_tinta:.2f} L')
