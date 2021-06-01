def sao_multiplicaveis(m1, m2):
    '''Recebe duas matrizes como parâmetros e devolve True se as matrizes forem multiplicáveis (número de colunas
    da primeira é igual ao número de linhs da segunda). False se não forem
    '''

    if len(m1[0]) == len(m2):
        return True
    else:
        return False

m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]
print(sao_multiplicaveis(m1, m2))