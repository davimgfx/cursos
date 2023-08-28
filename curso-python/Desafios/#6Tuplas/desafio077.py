tupla = ('aprender', 'programar', 'linguagem', 'python',
        'curso', 'gratis', 'estudar', 'praticar', 'safada'
        'trabalhar', 'mercardo', 'programador', 'futuro',
        'ladinha', 'ze polvino')
for i in tupla:
        print('\n')
        print(i, end=' ')
        for letra in i:
                if letra in 'aeiou':
                        print(letra, end=' ')  