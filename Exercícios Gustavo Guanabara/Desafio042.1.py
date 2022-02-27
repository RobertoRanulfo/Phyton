s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 > s2 + s3 or s2 > s1 + s3 or s3 > s2 + s1:
    print('Os segmentos acima NÃO PODEM FORMAR UM TRIÂNGULO.')
elif s1 == s2 == s3:
    print('Os segmentos formam um TRIÂNGULO EQUILÁTERO')
elif s1==s2 or s2==s3 or s1==s3:
    print('Os segmentos formam um TRIÂNGULO ISÓSCELES ')
elif s1 != s2 != s3:
    print('Os segmentos formam um TRIÂNGULO ESCALENO ')
# NÃO SEI SE ESTÁ CERTO!!!!! VER 042.2
#se a soma das medidas de dois deles é sempre maior que a medida do
# terceiro, então, eles podem formar um triângulo.