'''

Projeto 1 - "Buggy Data Base (BDB)" - 05/11/2021

Afonso da Conceição Ribeiro, 102763, 1.º Ano

afonsodaconceicaoribeiro@tecnico.ulisboa.pt

Unidade Curricular de Fundamentos da Programação

Licenciatura em Engenharia Informática e de Computadores - Alameda

Instituto Superior Técnico - Universidade de Lisboa

Ano Letivo 2021/2022, Semestre 1, Período 1

'''




#########
# 1.2.1 #
#########

def corrigir_palavra(palavra):
    
    """ corrigir_palavra: cadeia de carateres -> cadeia de carateres
    
    Esta função recebe uma cadeia de carateres que representa uma palavra
    (potencialmente modificada por um surto de letras) e devolve a cadeia de
    carateres que corresponde à aplicação da sequência de reduções para obter a
    palavra corrigida. """
    
    indice = 0
        # Começa-se pelo primeiro caráter da palavra.
    
    while indice < (len(palavra) - 1): 
        # Corre-se a função para cada caráter da palavra, exceto para o último,
        # pois esse já não tem nenhum à frente para comparar.
        
        if palavra[indice] == palavra[indice + 1].swapcase():
            # Avalia-se se o caráter de determinado índice e o seguinte são o
            # mesmo, mas com "letter cases" opostos.
            
            if indice + 2 <= (len(palavra) - 1):
                palavra = palavra[ :indice] + palavra[indice + 2: ] 
                    # Se ainda houver carateres a seguir aos dois que se
                    # pretende eliminar, estes têm de ser incluídos ...
            
            else:
                palavra = palavra[ :indice] 
                    # ... caso contrário, a palavra corresponde apenas à cadeia
                    # dos carateres anteriores aos que se pretende eliminar.
            
            indice -= 1 
                # Na proxima execução do ciclo, tem de se comparar a
                # partir do caráter imediatamente anterior aos dois
                # que se eliminaram (exemplo: ab(cC)Bd -> a(bB)d -> ad).
        
        else:
            indice += 1 
                # Se para o caráter do índice atual não se verificou
                # correspondência com o seguinte, na próxima execução
                # do ciclo começa-se a partir desse.
        
    return palavra



#########
# 1.2.2 #
#########

def eh_anagrama(palavra1, palavra2): # 
    
    """ eh_anagrama: cadeia de carateres x cadeia de carateres -> booleano
    
    Esta função recebe duas cadeias de carateres correspondentes a duas
    palavras e devolve True se e só se uma é anagrama da outra, isto é, se as
    palavras são constituídas pelas mesmas letras, ignorando diferenças entre
    maiúsculas e minúsculas e a ordem entre carateres. """
    
    palavra1 = palavra1.lower()
    palavra2 = palavra2.lower()
        # Ignoram-se as diferenças entre maiúsculas e minúsculas.
    
    palavra1_ordenada = "".join(sorted(palavra1))
    palavra2_ordenada = "".join(sorted(palavra2))
        # Cria-se uma lista cujos elementos são os carateres das palavras,
        # ordenam-se alfabeticamente e juntam-se em cadeias de carateres.
    
    return palavra1_ordenada == palavra2_ordenada
        # A condição é verdadeira se as palavras ordenadas forem iguais, ou
        # seja, se as palavras originais forem anagramas.



#########
# 1.2.3 #
#########

def validacao_corrigir_doc(argumento):
    
    """ validacao_corrigir_doc: universal -> booleano
    
    Esta função recebe um argumento de qualquer tipo e devolve True se e só se
    o seu argumento corresponde a um texto com erros da documentação da BDB. """
    
    if ( type(argumento) != str or argumento == ""
         or argumento[0] == " " or argumento[-1] == " "
         or "  " in argumento ):
        # O argumento tem de ser uma cadeia de carateres não vazia e não pode
        # começar nem acabar com espaços nem ter dois seguidos.
        
        return False
    
    cod_carateres = list(range(65,91)) + list(range(97,123)) + [32]
        # Lista dos códigos decimais para as letras maiúsculas, as letras
        # minúsculas e o espaço.
    
    for indice in range(len(argumento)):
        
        if ord(argumento[indice]) not in cod_carateres:
            # Todos os carateres do texto têm de ser letras, maiúsculas ou
            # minúsculas, ou espaços.
            
            return False
    
    return True


def corrigir_doc(texto_com_erros):
    
    """ corrigir_doc: cadeia de carateres -> cadeia de carateres
    
    Esta função recebe uma cadeia de carateres que representa o texto com erros
    da documentação da BDB e devolve a cadeia de carateres filtrada com as
    palavras corrigidas e os anagramas retirados, ficando apenas a sua primeira
    ocorrência. """
    
    if not validacao_corrigir_doc(texto_com_erros):
        # A função "validacao_corrigir_doc" avalia a validade do argumento da
        # função "corrigir_doc" e retorna True caso este seja válido.
        
        return ValueError("corrigir_doc: argumento invalido")
    
    texto_com_erros = corrigir_palavra(texto_com_erros)
        # Corrigem-se os potenciais surtos de letras no texto com erros, com
        # recurso à função "corrigir_palavra".
    
    lista_palavras = list(texto_com_erros.split(" "))
        # Cria-se uma lista cujos elementos são as palavras do texto com erros.
    
    for indice1 in range(len(lista_palavras) - 1):
        # Pretende-se comparar cada palavra da lista com as seguintes, pelo que
        # "indice1" tomará todos os valores possíveis para índices da lista,
        # exceto o último, pois esse não tem mais palavras com que comparar.
        
        indice2 = indice1 + 1
            # "indice2" começa por tomar o valor seguinte a "indice1" e, ao
            # longo do ciclo while, será incrementado, até representar o último
            # elemento da lista.
        
        while len(lista_palavras[indice2: ]) > 0:
            # O ciclo é executado enquanto houver elementos de índice superior
            # ou igual a "indice2".
            
            palavra1 = lista_palavras[indice1]
            palavra2 = lista_palavras[indice2]
            
            if ( eh_anagrama(palavra1, palavra2)
                 and palavra1.lower() != palavra2.lower() ):
                # Comparam-se as palavras e verifica-se se são anagramas, com
                # recurso à função "eh_anagrama". Apenas são retirados
                # anagramas que correspondem a palavras diferentes, ignorando
                # diferenças entre maiúsculas e minúsculas.
                
                del lista_palavras[indice2]
                    # Se o elemento de índice "indice2" for eliminado, a
                    # próxima palavra a comparar mantém esse valor, pelo que
                    # "indice2" não é incrementado.
            
            else:
                indice2 += 1
    
    return " ".join(lista_palavras)
        # A função retorna a cadeia de carateres correspondente à união dos
        # elementos da lista de palavras, separados por espaços entre si, ou
        # seja, o texto corrigido.



#########
# 2.2.1 #
#########

def obter_posicao(instrucao, posicao_atual):
    
    """ obter_posicao: cadeia de carateres x inteiro -> inteiro
    
    Esta função recebe uma cadeia de carateres contendo apenas um caráter que
    representa a direção de um único movimento e um inteiro representando a
    posição atual; e devolve o inteiro que corresponde à nova posição. """
    
    if instrucao == "C":
        # Se a posição atual estiver na primeira linha (ou seja, com valores
        # entre 1 e 3), esta mantém-se. Caso contrário, a nova posição
        # corresponde, na mesma coluna, à posição imediatamente acima.
        if posicao_atual - 3 < 1:
            return posicao_atual
        else:
            return posicao_atual - 3
    
    elif instrucao == "B":
        # Se a posição atual estiver na última linha (ou seja, com valores
        # entre 7 e 9), esta mantém-se. Caso contrário, a nova posição
        # corresponde, na mesma coluna, à posição imediatamente abaixo.
        if posicao_atual + 3 > 9:
            return posicao_atual
        else:
            return posicao_atual + 3
    
    elif instrucao == "E":
        # Se a posição atual estiver na primeira coluna (ou seja, com valores
        # 1, 4 ou 7), esta mantém-se. Caso contrário, a nova posição
        # corresponde, na mesma linha, à coluna imediatamente à esquerda.
        if posicao_atual in (1, 4, 7):
            return posicao_atual
        else:
            return posicao_atual - 1
    
    elif instrucao == "D":
        # Se a posição atual estiver na última coluna (ou seja, com valores
        # 3, 6 ou 9), esta mantém-se. Caso contrário, a nova posição
        # corresponde, na mesma linha, à coluna imediatamente à direita.
        if posicao_atual in (3, 6, 9):
            return posicao_atual
        else:
            return posicao_atual + 1



#########
# 2.2.2 #
#########

def obter_digito(seq_movimentos, posicao_inicial):
    
    """ obter_digito: cadeia de carateres x inteiro -> inteiro
    
    Esta função recebe uma cadeia de carateres contendo uma sequência de um ou
    mais movimentos e um inteiro representando a posição inicial; e devolve o
    inteiro correspondente ao dígito a marcar após finalizar os movimentos. """
    
    posicao_atual = posicao_inicial
        # Para começar, a posição atual corresponde à posição inicial.
        
    for instrucao in seq_movimentos:
        # Cada caráter da cadeia de carateres "seq_movimentos" corresponde a
        # uma instrução.
        
        posicao_atual = obter_posicao(instrucao, posicao_atual)
            # A posição atual é trocada pela aplicação da instrução a ela mesma.
        
    posicao_final = posicao_atual
        # A posição final corresponde à posição atual obtida após a aplicação
        # de todas as instruções.
    
    return posicao_final



#########
# 2.2.3 #
#########

def validacao_obter_pin(argumento):
    
    """ validacao_obter_pin: universal -> booleano
    
    Esta função recebe um argumento de qualquer tipo e devolve True se e só se
    o seu argumento corresponde a um tuplo contendo entre 4 e 10 sequências de
    movimentos. """
    
    if type(argumento) != tuple or len(argumento) < 4 or len(argumento) > 10:
        # O argumento tem de ser um tuplo com entre 4 e 10 elementos.
        
        return False
    
    for indice1 in range(len(argumento)):
        
        if type(argumento[indice1]) != str or argumento[indice1] == "":
            # Todos os elementos do tuplo têm de ser strings não vazias.
            
            return False
        
        else:
            for indice2 in range(len(argumento[indice1])):
                
                if argumento[indice1][indice2] not in ('C', 'B', 'E', 'D'):
                    # Todos os carateres das strings têm de ser letras que
                    # correspondem a instruções.
                    
                    return False
    
    return True


def obter_pin(sequencias):
    
    """ obter_pin: tuplo -> tuplo
    
    Esta função recebe um tuplo contendo entre 4 e 10 sequências de movimentos
    e devolve o tuplo de inteiros que contêm o pin codificado de acordo com o
    tuplo de movimentos. """
    
    if not validacao_obter_pin(sequencias):
        # A função "validacao_obter_pin" avalia a validade do argumento da
        # função "obter_pin" e retorna True caso este seja válido.
        
        return ValueError("obter_pin: argumento invalido")
    
    pin = ()
    
    posicao_inicial = 5
        # Para a primeira sequência de movimentos, inicia-se no botão 5.
    
    for seq_movimentos in sequencias:
        
        novo_digito = obter_digito(seq_movimentos, posicao_inicial)
            # Para cada sequência de movimentos, obtém-se um digito do pin, com
            # recurso à função 2.2.2.
        
        pin += (novo_digito,)
            # Concatena-se, ao tuplo do pin, um tuplo com o novo dígito.
        
        posicao_inicial = novo_digito
            # A posição inicial da próxima sequência de movimentos corresponde
            # ao digito obtido na sequência de movimentos anterior.
    
    return pin



#########
# 3.2.1 #
#########

def eh_entrada(argumento):
    
    """ eh_entrada: universal -> booleano
    
    Esta função recebe um argumento de qualquer tipo e devolve True se e só se
    o seu argumento corresponde a uma entrada da BDB (potencialmente corrupta).
    """
    
    cod_minusculas = list(range(97,123))
    cod_traco = [45]
        # Listas dos códigos decimais para as letras minúsculas e o traço.
    
    # 1. Validações para o argumento em geral:
    
    if ( type(argumento) != tuple or len(argumento) != 3
         or type(argumento[0]) != str or type(argumento[1]) != str
         or type(argumento[2]) != tuple ):
        # O argumento tem de ser um tuplo constituído por três elementos: duas
        # cadeias de carateres e um tuplo, respetivamente.
        
        return False
    
    cifra = argumento[0]
    checksum = argumento[1]
    seguranca = argumento[2]
        # Os elementos do tuplo correspondem, por esta ordem, à cifra, à
        # checksum e aos números de segurança.
    
    # 2. Validações para a cifra:
    
    if cifra == "" or cifra[0] == "-" or cifra[-1] == "-" or "--" in cifra:
        # A cifra tem de ser uma cadeia de carateres não vazia e não pode
        # começar nem acabar com traços nem ter dois seguidos.
        
        return False
    
    for indice in range(len(cifra)):
        
        if ord(cifra[indice]) not in (cod_minusculas + cod_traco):
            # Todos os carateres da cifra têm de ser letras minúsculas ou
            # traços.
            
            return False
    
    # 3. Validações para a checksum:
    
    if len(checksum) != 7 or checksum[0] != "[" or checksum[-1] != "]":
        # A checksum tem de ser uma cadeia de carateres com 7 carateres, sendo
        # o primeiro o último parêntesis retos aberto e fechado, respetivamente.
        
        return False
    
    for indice in range(1,6):
        
        if ord(checksum[indice]) not in cod_minusculas:
            # Os carateres da checksum dentro dos parêntesis retos têm de
            # ser letras minúsculas.
            
            return False
    
    # 4. Validações para os números de segurança:
    
    if len(seguranca) < 2:
        # O tuplo tem de ter dois ou mais números de segurança.
        
        return False
    
    for indice in range(len(seguranca)):
        
        if type(seguranca[indice]) != int or seguranca[indice] <= 0:
            # Os números de segurança têm de ser inteiros positivos.
            
            return False
    
    return True
        # Se em nenhuma validação a função retornar False, o argumento
        # corresponde a uma entrada da BDB.



#########
# 3.2.2 #
#########

def validar_cifra(cifra, controlo_input):
    
    """ validar_cifra: cadeia de carateres x cadeia de carateres -> booleano
    
    Esta função recebe uma cadeia de carateres contendo uma cifra e uma outra
    cadeia de carateres contendo uma sequência de controlo, e devolve True se e
    só se a sequência de controlo é coerente com a cifra conforme descrito. """
    
    cifra = "".join(cifra.rsplit("-"))
        # Remover os traços da cifra, pois só se pretende utilizar as letras.
    
    controlo_input = controlo_input[1:6]
        # Remover os parêntesis retos da sequência de controlo recebida.
    
    for letra in controlo_input:
        if letra not in cifra:
            # Se a sequência de controlo recebida tiver alguma letra não
            # presente na cifra, já se sabe que não é coerente com a mesma.
            
            return False
    
    freq_abs = {letra:cifra.count(letra) for letra in cifra}
        # Dicionário em que, a cada letra da cifra, corresponde a sua
        # frequência absoluta na mesma.
    
    controlo_calc = ""
        # Cadeia de carateres que corresponderá à sequência de controlo
        # coerente com a cifra.
    
    for execucao in range(5):
        # Pretende-se correr as instruções deste ciclo cinco vezes.
        
        letras = sorted(freq_abs.keys())
            # Lista ordenada alfabeticamente das letras da cifra. Atualiza-se a
            # cada execução do ciclo, pois vão sendo eliminados elementos do
            # dicionário de frequências absolutas.
        
        letra_atual = letras[0]
            # Começa-se a comparação das frequências absolutas das letras pela
            # primeira.
        
        for letra in letras[1:]:
            
            if freq_abs[letra_atual] < freq_abs[letra]:
                # Uma vez que os empates são decididos por ordem alfabética e a
                # lista "letras" tem os elementos por essa ordem, só se altera
                # a "letra_atual" quando se encontra outra com maior frequência
                # absoluta.
                
                letra_atual = letra
        
        controlo_calc += letra_atual
            # Adiciona-se a "letra_atual" à sequência de controlo.
        
        del(freq_abs[letra_atual])
            # Elimina-se a "letra_atual" das chaves do dicionário, pois, caso
            # contrário, seria sempre adicionada a mesma letra à sequência de
            # controlo.
    
    return controlo_calc == controlo_input
        # Se a sequência de controlo recebida for igual à calculada, então essa
        # é coerente com a cifra e a função retorna True.



#########
# 3.2.3 #
#########

def validacao_filtrar_bdb(argumento):
    
    """ validacao_filtrar_bdb: universal -> booleano
    
    Esta função recebe um argumento de qualquer tipo e devolve True se e só se
    o seu argumento corresponde a uma lista contendo uma ou mais entradas da
    BDB. """
    
    if type(argumento) != list or argumento == []:
        # O argumento tem de ser uma lista não vazia.
        
        return False
    
    for elemento in argumento:
        
        if not eh_entrada(elemento):
            # Todos os elementos da lista têm de ser entradas da BDB.
            
            return False
    
    return True


def filtrar_bdb(entradas_BDB):
    
    """ filtrar_bdb: lista -> lista
    
    Esta função recebe uma lista contendo uma ou mais entradas da BDB e devolve
    apenas a lista contendo as entradas em que a checksum não é coerente com a
    cifra correspondente, na mesma ordem da lista original. """
    
    if not validacao_filtrar_bdb(entradas_BDB):
        # A função "validacao_filtrar_bdb" avalia a validade do argumento da
        # função "filtrar_bdb" e retorna True caso este seja válido.
        
        return ValueError("filtrar_bdb: argumento invalido")
    
    for indice in range(len(entradas_BDB) - 1, -1, -1):
        # Itera-se do último para o primeiro elemento da lista porque, caso
        # contrário, devido às alterações nos índices, provenientes da
        # eliminação de elementos da lista, não se poderia utilizar o ciclo for.
        
        if validar_cifra(entradas_BDB[indice][0], entradas_BDB[indice][1]):
            # Cada elemento da lista é um tuplo que representa uma entrada da
            # BDB.
            
            del entradas_BDB[indice]
                # Se a checksum da entrada da BDB é coerente com a cifra, a
                # mesma é eliminada da lista, restando apenas, como elementos
                # desta, as entradas com incoerência.
    
    return entradas_BDB



#########
# 4.2.2 #
#########

def obter_num_seguranca(seq_seguranca):
    
    """ obter_num_seguranca: tuplo -> inteiro
    
    Esta função recebe um tuplo de números inteiros positivos e devolve o
    número de segurança, isto é, a menor diferença positiva entre qualquer par
    de números. """
    
    seq_seguranca = sorted(list(seq_seguranca))
        # A partir do tuplo da sequência de segurança, cria-se uma lista com os
        # elementos do mesmo por ordem crescente.
    
    num_seguranca = seq_seguranca[-1]
        # Tem de ser dado à variável um valor inicial que, com certeza, seja
        # maior do que a menor diferença entre dois números da sequência de
        # segurança.
    
    for indice in range(len(seq_seguranca) - 1):
        
        if seq_seguranca[indice + 1] - seq_seguranca[indice] < num_seguranca:
            # Quanto maior o índice do elemento, maior o valor do elemento,
            # pelo que esta subtração nunca retorna valores negativos.
            
            num_seguranca = seq_seguranca[indice + 1] - seq_seguranca[indice]
                # Se a diferença entre os dois elementos for menor do que o
                # valor atual do número de segurança, este é substituído pela
                # mesma.
    
    return num_seguranca



#########
# 4.2.3 #
#########

def decifrar_texto(cifra, num_seguranca):
    
    """ decifrar_texto: cadeia de carateres x inteiro -> cadeia de carateres
    
    Esta função recebe uma cadeia de carateres contendo uma cifra e um número
    de segurança, e devolve o texto decifrado. """
    
    decifrado = ""
        # Variável à qual serão concatenados os carateres descodificados.
    
    for indice in range(len(cifra)):
        
        if cifra[indice] == "-":
            
            decifrado += " "
                # Os traços são substituídos por espaços.
        
        else:
            
            if indice % 2 == 0:
                
                cod_nova_letra = ord(cifra[indice]) + num_seguranca + 1
                    # Se o caráter estiver numa posição par, avança-se 
                    # (num_seguranca + 1) vezes.
            
            else:
                
                cod_nova_letra = ord(cifra[indice]) + num_seguranca - 1
                    # Se o carater estiver numa posição ímpar, avança-se 
                    # (num_seguranca - 1) vezes.
            
            while not 97 <= cod_nova_letra <= 122:
                # As operações com os códigos decimais dos carateres podem
                # originar códigos que não correspondem a letras minúsculas,
                # devendo-se, nesse caso, ir subtraindo 26, até que o código
                # esteja no intervalo dos códigos destas.
                
                cod_nova_letra -= 26
            
            decifrado += chr(cod_nova_letra)
                # Concatena-se à cadeia de carateres "decifrado" a cadeia de 
                # carateres com o novo caráter decifrado.
    
    return decifrado



#########
# 4.2.4 #
#########

def decifrar_bdb(entradas_BDB):
    
    """ decifrar bdb: lista -> lista
    
    Esta função recebe uma lista contendo uma ou mais entradas da BDB e
    devolve uma lista de igual tamanho, contendo o texto das entradas
    decifradas na mesma ordem. """
    
    if type(entradas_BDB) != list or len(entradas_BDB) == 0:
        # O argumento tem de ser uma lista não vazia.
        
        return ValueError("decifrar_bdb: argumento invalido")
    
    for indice in range(len(entradas_BDB)):
        # O ciclo é percorrido para o índice de cada entrada da lista.
        
        if not eh_entrada(entradas_BDB[indice]):
            # Todos os elementos da lista têm de ser entradas da BDB.
            
            return ValueError("decifrar_bdb: argumento invalido")
        
        entradas_BDB[indice] = decifrar_texto( entradas_BDB[indice][0], 
                               obter_num_seguranca(entradas_BDB[indice][2]) )
            # Cada entrada é corrigida e coloca-se, na lista, no elemento com o
            # seu índice, o respetivo texto decifrado.
    
    return entradas_BDB



#########
# 5.2.1 #
#########

def eh_utilizador(argumento):
    
    """ eh_utilizador: universal -> booleano
    
    Esta função recebe um argumento de qualquer tipo e devolve True se e só se
    o seu argumento corresponde a um dicionário contendo a informação de
    utilizador relevante da BDB. """
    
    return (     type(argumento) == dict
             and set(argumento.keys()) == {"name", "pass", "rule"}
                 # O argumento tem de ser um dicionário com três pares
                 # chave-valor, sendo as chaves "name", "pass" e "rule".
             
             and type(argumento["name"]) == str
             and argumento["name"] != ""
             and type(argumento["pass"]) == str
             and argumento["pass"] != ""
                 # Os valores do dicionário correspondentes às chaves "name" e
                 # "pass" têm de ser strings não vazias.
             
             and type(argumento["rule"]) == dict
             and set(argumento["rule"].keys()) == {"vals", "char"}
                 # O valor do dicionário correspondente à chave "rule" tem de
                 # ser um dicionário (seja esse o dicionário das regras) com
                 # dois pares chave-valor, sendo as chaves "vals" e "char".
             
             and type(argumento["rule"]["vals"]) == tuple
             and len(argumento["rule"]["vals"]) == 2
                 # O valor do dicionário das regras correspondente à chave
                 # "vals" tem de ser um tuplo com dois elementos.
             
             and type(argumento["rule"]["vals"][0]) == int
             and type(argumento["rule"]["vals"][1]) == int
             and 0 < argumento["rule"]["vals"][0] < argumento["rule"]["vals"][1]
                 # Os elementos do tuplo têm de ser números inteiros positivos,
                 # tais que o primeiro é menor do que o segundo.
             
             and type(argumento["rule"]["char"]) == str
             and len(argumento["rule"]["char"]) == 1
                 # O valor do dicionário das regras correspondente à chave
                 # "char" tem de ser uma string com um caráter.
             
             and ord(argumento["rule"]["char"]) in list(range(97,123))
                 # O caráter da string tem de ser uma letra minúscula, ou seja,
                 # o seu código decimal deve pertencer à lista dos códigos
                 # decimais das letras minúsculas.
           )



#########
# 5.2.2 #
#########

def eh_senha_valida(senha, regra):
    
    """ eh_senha_valida: cadeia de carateres x dicionário -> booleano
    
    Esta função recebe uma cadeia de carateres correspondente a uma senha e um
    dicionário contendo a regra individual de criação da senha, e devolve True
    se e só se a senha cumpre com todas as regras de definição (gerais e
    individual). """
    
    if ( senha.count("a") + senha.count("e") + senha.count("i") +
         senha.count("o") + senha.count("u") < 3 ):
        # Se a senha não contiver pelo menos três vogais minúsculas, uma regra
        # geral não é cumprida.
        
        return False
    
    repetido = False
        # A variável "repetido" corresponderá ao valor lógico da proposição
        # "a senha contém pelo menos um caráter que apareça duas vezes
        # consecutivas".
    
    for indice in range(len(senha) - 1):
        if senha[indice] == senha[indice + 1]:
            # Se se encontrarem dois carateres iguais seguidos, a variável
            # "repetido" é alterada para True e o ciclo acaba.
            
            repetido = True
            break
    
    if not repetido:
        # Se não tiverem sido encontrados dois carateres iguais seguidos, uma
        # regra geral não é cumprida.
        return False
    
    return regra["vals"][0] <= senha.count(regra["char"]) <= regra["vals"][1]
        # Se a frequência absoluta do caráter "regra["char"]" na senha não
        # for maior ou igual ao primeiro elemento do tuplo "regra["vals"]"
        # e menor ou igual ao segundo elemento desse mesmo tuplo, A regra
        # individual não é cumprida. Caso contrário, todas as regras de
        # definição são cumpridas, pelo que a função retorna True.



#########
# 5.2.3 #
#########

def filtrar_senhas(lista_dict):
    
    """ filtrar_senhas: lista -> lista
    
    Esta função recebe uma lista com um ou mais dicionários correspondentes às
    entradas da BDB como descritas anteriormente, e devolve a lista ordenada
    alfabeticamente com os nomes dos utilizadores com senhas erradas. """
    
    if type(lista_dict) != list or lista_dict == []:
        # O argumento tem de ser uma lista não vazia.
        
        return ValueError("filtrar_senhas: argumento invalido")
    
    lista_nomes = []
        # Lista à qual serão adicionados os nomes dos utilizadores com senhas
        # erradas.
    
    for elemento in lista_dict:
        
        if not eh_utilizador(elemento):
            # Todos os elementos da lista têm de ser dicionários
            # correspondentes às entradas da BDB.
            
            return ValueError("filtrar_senhas: argumento invalido")
        
        if not eh_senha_valida(elemento["pass"], elemento["rule"]):
            
            lista_nomes.append(elemento["name"])
    
    return sorted(lista_nomes)