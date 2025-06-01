def pyramid(layers):
    star='*'
    for i in range(0,layers):
        print(star.center(layers*2,' '))
        star=star+'**'
pyramid(10)