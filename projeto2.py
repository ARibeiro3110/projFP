'''

Projeto 2 - "O Prado" - 19/11/2021

Afonso da Conceição Ribeiro, 102763, 1.º Ano

afonsodaconceicaoribeiro@tecnico.ulisboa.pt

Unidade Curricular de Fundamentos da Programação

Licenciatura em Engenharia Informática e de Computadores - Alameda

Instituto Superior Técnico - Universidade de Lisboa

Ano Letivo 2021/2022, Semestre 1, Período 1

'''





''' ############################################################################
    2.1.1 TAD posicao
    Representação interna: tuplo com dois elementos, respetivamente, a
    componente x e a componente y da posição.
    
    cria_posicao: int x int -> posicao
    cria_copia_posicao: posicao -> posicao
    obter_pos_x: posicao -> int
    obter_pos_y: posicao -> int
    eh_posicao: universal -> booleano
    posicoes_iguais: posicao x posicao -> booleano
    posicao_para_str: posicao -> str
''' ############################################################################



##### Construtor #####


def cria_posicao(x, y):
    
    """ cria_posicao: int x int -> posicao
    
    Recebe os valores correspondentes às coordenadas de uma posição e devolve a
    posição correspondente. """
    
    # Verificação da validade dos argumentos:
    if type(x) != int or type(y) != int or x < 0 or y < 0:
        # Os argumentos têm de ser inteiros não negativos.
        
        return ValueError("cria_posicao: argumentos invalidos")
    
    return (x, y)


def cria_copia_posicao(p):
    
    """ cria_copia_posicao: posicao -> posicao
    
    Recebe uma posição e devolve uma cópia nova da posição. """
    
    # Verificação da validade do argumento:
    if not eh_posicao(p):
        # O argumento tem de ser do tipo posicao.
        
        raise ValueError("cria_copia_posicao: argumento invalido")    
    
    return cria_posicao(obter_pos_x(p), obter_pos_y(p))



##### Seletores #####


def obter_pos_x(p):
    
    """ obter_pos_x: posicao -> int
    
    Devolve a componente x da posição 'p'. """
    
    return p[0]


def obter_pos_y(p):
    
    """ obter_pos_y: posicao -> int
    
    Devolve a componente y da posição 'p'. """
    
    return p[1]



##### Reconhecedor #####


def eh_posicao(arg):
    
    """ eh_posicao: universal -> booleano
    
    Devolve True caso o seu argumento seja um TAD posicao e False caso
    contrário. """
    
    return (     type(arg) == tuple and len(arg) == 2
             and type(arg[0]) == int and type(arg[1]) == int
             and arg[0] >= 0 and arg[1] >= 0
                 # O argumento é um TAD posicao se for um tuplo com dois
                 # elementos inteiros não negativos.
           )



##### Teste #####


def posicoes_iguais(p1, p2):
    
    """ posicoes_iguais: posicao x posicao -> booleano
    
    Devolve True apenas se 'p1' e 'p2' são posições e são iguais. """
    
    if p1 != p2:
        return False
        # Se os objetos a que correspondem as variáveis 'p1' e 'p2' não forem
        # iguais, nunca poderão ser posições iguais, de acordo com a
        # representação interna definida, pelo que a função retorna False.
    
    return eh_posicao(p1) and eh_posicao(p2)
        # Se forem iguais, retornará True se e apenas se ambos forem do tipo
        # posicao.



##### Transformador #####


def posicao_para_str(p):
    
    """ posicao_para_str: posicao -> str
    
    Devolve a cadeia de carateres '(x, y)' que representa o seu argumento,
    sendo os valores x e y as coordenadas de 'p'. """
    
    return f"({obter_pos_x(p)}, {obter_pos_y(p)})"



##### Funções de alto nível #####


def obter_posicoes_adjacentes(p):
    
    """ obter_posicoes_adjacentes: posicao -> tuplo
    
    Devolve um tuplo com as posições adjacentes à posição 'p', começando pela
    posição acima de 'p' e seguindo no sentido horário. """
    
    
    def tuplo_posicao(x, y):
        
        """ tuplo_posicao: inteiro x inteiro -> tuplo
        
        Se os seus argumentos corresponderem a coordenadas válidas para uma
        posição, retorna um tuplo com a posição criada pelas mesmas, caso
        contrário, retorna o tuplo vazio. """
        
        if eh_posicao(cria_posicao(x, y)):
            return (cria_posicao(x, y),)
        
        return () # Else: não são coordenadas válidas.
    
    
    pos_adj = (   tuplo_posicao(obter_pos_x(p), obter_pos_y(p) - 1)
                + tuplo_posicao(obter_pos_x(p) + 1, obter_pos_y(p))
                + tuplo_posicao(obter_pos_x(p), obter_pos_y(p) + 1)
                + tuplo_posicao(obter_pos_x(p) - 1, obter_pos_y(p)) )
        # Adicionam-se ao tuplo 'pos_adj' as posições adjacentes à posição 'p',
        # caso estas existam. As posições adjacentes a uma posição (x, y) podem
        # ser (x, y - 1), (x + 1, y), (x, y + 1) e (x - 1, y).
    
    return pos_adj


def ordenar_posicoes(t):
    
    """ ordenar_posicoes: tuplo -> tuplo
    
    Devolve um tuplo contendo as mesmas posições do tuplo fornecido como
    argumento, ordenadas de acordo com a ordem de leitura do prado. """
    
    
    def ordenar_sem_repetidos(lista_int):
        
        """ ordenar_sem_repetidos: lista -> lista
        
        Recebe uma lista de inteiros e devolve uma lista com os mesmos
        elementos por ordem crescente e sem repetições. """
        
        lista_nova = []
        
        for i in lista_int:
            if i not in lista_nova:
                # Adiciona-se cada elemento de 'lista_int' a 'lista_nova'
                # apenas se este ainda não estiver lá.
                
                lista_nova.append(i)
        
        return sorted(lista_nova)
    
    
    lista_x = ordenar_sem_repetidos([obter_pos_x(p) for p in t])
    lista_y = ordenar_sem_repetidos([obter_pos_y(p) for p in t])
        # Listas ordenadas das componentes 'x' e 'y' presentes em pelo menos
        # uma posição do tuplo.
    
    pos_ord = ()
    
    for y in lista_y:
        for x in lista_x:
            posicao = cria_posicao(x, y)
            
            if any([posicoes_iguais(posicao, t[i]) for i in range(len(t))]):
                # Para cada valor da lista 'lista_y', itera-se pelos valores da
                # lista 'lista_x', verificando-se se existe, no tuplo 't',
                # uma posição com essas coordenadas, e, se sim, adiciona-se a
                # mesma ao tuplo "pos_ord".
                
                pos_ord += (posicao,)
    
    return pos_ord
        # Uma vez que se iterou por listas ordenadas, as posições do tuplo
        # "pos_ord" estão ordenadas pelas suas componentes y, e as posições com
        # as mesmas componentes y estão ordenadas pelas suas componentes x.




''' ############################################################################
    2.1.2 TAD animal
    Representação interna: dicionário com cinco pares chave-valor, sendo as
    chaves "especie", "freq_reproducao", "freq_alimentacao", "idade" e "fome" e
    sendo os valores as características de cada animal para cada chave.
    
    cria_animal: str x int x int -> animal
    cria_copia_animal: animal -> animal
    obter_especie: animal -> str
    obter_freq_reproducao: animal -> int
    obter_freq_alimentacao: animal -> int
    obter_idade: animal -> int
    obter_fome: animal -> int
    aumenta_idade: animal -> animal
    reset_idade: animal -> animal
    aumenta_fome: animal -> animal
    reset_fome: animal -> animal
    eh_animal: universal -> booleano
    eh_predador: universal -> booleano
    eh_presa: universal -> booleano
    animais_iguais: animal x animal -> booleano
    animal_para_char: animal -> str
    animal_para_str: animal -> str
''' ############################################################################



##### Construtor #####


def cria_animal(s, r, a):
    
    """ cria_animal: str x int x int -> animal
    
    Recebe uma cadeia de carateres 's' não vazia correspondente à espécie do
    animal e dois valores inteiros correspondentes à frequência de reprodução
    'r' e à frequência de alimentação 'a'; e devolve o animal. Animais com
    frequência de alimentação maior que 0 são considerados predadores, caso
    contrário são considerados presas. """
    
    # Verificação da validade dos argumentos:
    if (    type(s) != str or s == "" or type(r) != int or type(a) != int
         or r <= 0 or a < 0 ):
        # O argumento 's' tem de ser uma cadeia de carateres não vazia, o
        # argumento 'r' tem de ser um inteiro positivo e o argumento 'a' tem de
        # ser um inteiro não negativo.
        
        raise ValueError("cria_animal: argumentos invalidos")
    
    return {"especie":s, "freq_reproducao":r, "freq_alimentacao":a,
            "idade":0, "fome":0}


def cria_copia_animal(a):
    
    """ cria_copia_animal: animal -> animal
    
    Recebe um animal 'a' e devolve uma nova cópia do animal. """
    
    # Verificação da validade dos argumentos:
    if not eh_animal(a):
        # O argumento tem de ser do tipo animal.
        
        raise ValueError("cria_copia_animal: argumento invalido")    
    
    return {"especie":obter_especie(a),
            "freq_reproducao":obter_freq_reproducao(a),
            "freq_alimentacao":obter_freq_alimentacao(a),
            "idade":obter_idade(a),
            "fome":obter_fome(a)}



##### Seletores #####


def obter_especie(a):
    
    """ obter_especie: animal -> str
    
    Devolve a cadeia de carateres correspondente à espécie do animal. """
    
    return a["especie"]


def obter_freq_reproducao(a):
    
    """ obter_freq_reproducao: animal -> int
    
    Devolve a frequência de reprodução do animal 'a'. """
    
    return a["freq_reproducao"]


def obter_freq_alimentacao(a):
    
    """ obter_freq_alimentacao: animal -> int
    
    Devolve a frequência de alimentação do animal 'a' (as presas devolvem
    sempre 0). """
    
    return a["freq_alimentacao"]


def obter_idade(a):
    
    """ obter_idade: animal -> int
    
    Devolve a idade do animal 'a'. """
    
    return a["idade"]


def obter_fome(a):
    
    """ obter_fome: animal -> int
    
    Devolve a fome do animal 'a' (as presas devolvem sempre 0). """
    
    return a["fome"]



##### Modificadores #####


def aumenta_idade(a):
    
    """ aumenta_idade: animal -> animal
    
    Modifica destrutivamente o animal 'a' incrementando o valor da sua idade em
    uma unidade, e devolve o próprio animal. """
    
    a["idade"] += 1
    
    return a


def reset_idade(a):
    
    """ reset_idade: animal -> animal
    
    Modifica destrutivamente o animal 'a' definindo o valor da sua idade igual
    a 0, e devolve o próprio animal. """
    
    a["idade"] = 0
    
    return a


def aumenta_fome(a):
    
    """ aumenta_fome: animal -> animal
    
    Modifica destrutivamente o animal predador 'a' incrementando o valor da sua
    fome em uma unidade, e devolve o próprio animal. Esta operação não modifica
    os animais presa. """
    
    if eh_predador(a):
        a["fome"] += 1
    
    return a


def reset_fome(a):
    
    """ reset_fome: animal -> animal
    
    Modifica destrutivamente o animal predador 'a' definindo o valor da sua
    fome igual a 0, e devolve o próprio animal. Esta função não modifica os
    animais presa. """
    
    if eh_predador(a):
        a["fome"] = 0
    
    return a



##### Reconhecedor #####


def eh_animal(arg):
    
    """ eh_animal: universal -> booleano
    
    Devolve True caso o seu argumento seja um TAD animal e False caso
    contrário. """
    
    return (     type(arg) == dict and arg.keys() == {"especie",
                 "freq_reproducao", "freq_alimentacao", "idade", "fome"}
                 # O argumento tem de ser um dicionário com cinco pares
                 # chave-valor, sendo as chaves os elementos do set acima.
             
             and type(arg["especie"]) == str and arg["especie"] != ""
                 # O valor do dicionário correspondente à chave "especie" tem de
                 # ser uma cadeia de carateres não vazia.
             
             and type(arg["freq_reproducao"]) == int
             and arg["freq_reproducao"] > 0
                 # O valor do dicionário correspondente à chave
                 # "freq_reproducao" tem de ser um inteiro positivo.
             
             and type(arg["freq_alimentacao"]) == int
             and arg["freq_alimentacao"] >= 0
             and type(arg["idade"]) == int and arg["idade"] >= 0
             and type(arg["fome"]) == int and arg["fome"] >= 0
                 # Os valores do dicionário correspondentes às chaves
                 # "freq_alimentacao", "idade" e "fome" têm de ser inteiros não
                 # negativos.             
           )


def eh_predador(arg):
    
    """ eh_predador: universal -> booleano
    
    Devolve True caso o seu argumento seja um TAD animal do tipo predador e
    False caso contrário. """
    
    return eh_animal(arg) and obter_freq_alimentacao(arg) > 0


def eh_presa(arg):
    
    """ eh_presa: universal -> booleano
    
    Devolve True caso o seu argumento seja um TAD animal do tipo presa e False
    caso contrário. """
    
    return eh_animal(arg) and obter_freq_alimentacao(arg) == 0



##### Teste #####


def animais_iguais(a1, a2):
    
    """ animais_iguais: animal x animal -> booleano
    
    Devolve True apenas se 'a1' e 'a2' são animais e são iguais. """
    
    return (     eh_animal(a1) and eh_animal(a2)
             and obter_especie(a1) == obter_especie(a2)
             and obter_freq_reproducao(a1) == obter_freq_reproducao(a2)
             and obter_freq_alimentacao(a1) == obter_freq_alimentacao(a2)
             and obter_idade(a1) == obter_idade(a2)
             and obter_fome(a1) == obter_fome(a2)
           )



##### Transformadores #####


def animal_para_char(a):
    
    """ animal_para_char: animal -> str
    
    Devolve a cadeia de carateres dum único elemento correspondente ao primeiro
    caráter da espécie do animal passada por argumento, em maiúscula para
    animais predadores e em minúscula para animais presa. """
    
    if eh_presa(a):
        return obter_especie(a)[0].lower()
    
    return obter_especie(a)[0].upper() # Else: é predador.


def animal_para_str(a):
    
    """ animal_para_str: animal -> str
    
    Devolve a cadeia de carateres que representa o animal. """
    
    if eh_presa(a):
        return \
        f"{obter_especie(a)} [{obter_idade(a)}/{obter_freq_reproducao(a)}]"
    
    else: # Predador.
        return \
        f"{obter_especie(a)} [{obter_idade(a)}/{obter_freq_reproducao(a)};" + \
        f"{obter_fome(a)}/{obter_freq_alimentacao(a)}]"



##### Funções de alto nível #####


def eh_animal_fertil(a):
    
    """ animal -> booleano
    
    Devolve True caso o animal 'a' tenha atingido a idade de reprodução e False
    caso contrário. """
    
    return obter_idade(a) >= obter_freq_reproducao(a)


def eh_animal_faminto(a):
    
    """ eh_animal_faminto: animal -> booleano
    
    Devolve True caso o animal 'a' tenha atingido um valor de fome igual ou
    superior à sua frequência de alimentação e False caso contrário. As presas
    devolvem sempre False. """
    
    if eh_presa(a):
        return False
    
    return obter_fome(a) >= obter_freq_alimentacao(a) # Else: é predador


def reproduz_animal(a):
    
    """ reproduz_animal: animal -> animal
    
    Recebe um animal 'a' devolvendo um novo animal da mesma espécie com idade e
    fome igual a 0, e modificando destrutivamente o animal passado como
    argumento 'a' alterando a sua idade para 0. """
    
    a = reset_idade(a)
    
    return reset_fome(cria_copia_animal(a))




''' ############################################################################
    2.1.3 TAD prado
    Representação interna: dicionário com quatro pares chave-valor, sendo as
    chaves 'd', 'r', 'a' e 'p', e sendo os valores correspondentes às mesmas,
    respetivamente, a posição do canto inferior direito do prado, o tuplo das
    posições correspondentes aos rochedos que não são as montanhas dos limites
    exteriores do prado, o tuplo dos animais e o tuplo das posições
    correspondentes ocupadas pelos animais.
    
    cria_prado: posicao x tuplo x tuplo x tuplo -> prado
    cria_copia_prado: prado -> prado
    obter_tamanho_x: prado -> int
    obter_tamanho_y: prado -> int
    obter_numero_predadores: prado -> int
    obter_numero_presas: prado -> int
    obter_posicao_animais: prado -> tuplo posicoes
    obter_animal: prado x posicao -> animal
    eliminar_animal: prado x posicao -> prado
    mover_animal: prado x posicao x posicao -> prado
    inserir_animal: prado x animal x posicao -> prado
    eh_prado: universal -> booleano
    eh_posicao_animal: prado x posicao -> booleano
    eh_posicao_obstaculo: prado x posicao -> booleano
    eh_posicao_livre: prado x posicao -> booleano
    prados_iguais: prado x prado -> booleano
    prado_para_str: prado -> str
''' ############################################################################



##### Construtor #####


def validacao_cria_prado(d, r, a, p):
    
    """ universal x universal x universal x universal -> booleano
    
    Esta função recebe quatro argumentos de qualquer tipo e devolve True se e
    só se os seus argumentos permitem a criação de um prado válido, com a
    função cria_prado. """
    
    # 1. Validações para 'd' e para os restantes argumentos em geral:
    
    if ( not eh_posicao(d) or obter_pos_x(d) < 2 or obter_pos_y(d) < 2
         or type(r) != tuple or type(a) != tuple or type(p) != tuple
         or len(a) != len(p) or len(a) == 0 ):
        # 'd' tem de ser do tipo posicao e as suas coordenadas não podem ser
        # inferiores a 2, pois, nesse caso, não existiriam posições passíveis
        # de serem ocupadas por animais. 'r' tem de ser um tuplo. 'a' e 'p' têm
        # de ser tuplos não vazios e com o mesmo número de elementos.
        
        return False
    
    # 2. Validações específicas para 'a':
    
    for elemento in a:
        if not eh_animal(elemento):
            # Todos os elementos de 'a' têm de ser animais.
            
            return False
    
    # 3. Validações específicas para 'r' e 'p':
    
    rp = r + p
        # Tuplo com todas as posições ocupadas por rochedos ou animais.
    
    for i in range(len(rp)):
        
        if not ( eh_posicao(rp[i]) and 0 < obter_pos_x(rp[i]) < obter_pos_x(d)
           and 0 < obter_pos_y(rp[i]) < obter_pos_y(d) and not
           any([posicoes_iguais(rp[i], rp[j]) for j in range(i + 1, len(rp))])):
            # Cada elemento do tuplo tem de ser uma posição com coordenadas
            # maiores que 0 e menores que as coordenadas de 'd', e não pode ser
            # igual a nenhuma outra posição do tuplo, pois isso significaria a
            # existência de dois animais, ou dois rochedos, ou um animal e um
            # rochedo, a ocupar a mesma posição.
            
            return False
    
    return True


def cria_prado(d, r, a, p):
    
    """ cria_prado: posicao x tuplo x tuplo x tuplo -> prado
    
    Recebe uma posição 'd' correspondente à posição que ocupa a montanha do
    canto inferior direito do prado, um tuplo 'r' de 0 ou mais posições
    correspondentes aos rochedos que não são as montanhas dos limites
    exteriores do prado, um tuplo 'a' de 1 ou mais animais, e um tuplo 'p' da
    mesma dimensão do tuplo 'a' com as posições correspondentes ocupadas pelos
    animais; e devolve o prado que representa internamente o mapa e os animais
    presentes. """
    
    # Verificação da validade dos argumentos:
    if not validacao_cria_prado(d, r, a, p):
        # A função "validacao_cria_prado" avalia a validade dos argumentos da
        # função "cria_prado" e retorna True caso estes sejam válidos.
        
        raise ValueError("cria_prado: argumentos invalidos")
    
    return {"d":d, "r":r, "a":a, "p":p}


def cria_copia_prado(p):
    
    """ cria_copia_prado: prado -> prado
    
    Recebe um prado e devolve uma nova cópia do prado. """
    
    # Verificação da validade do argumento:
    if not eh_prado(p):
        # O argumento tem de ser do tipo prado.
        
        raise ValueError("cria_copia_prado: argumento invalido")
    
    d = cria_copia_posicao(p["d"])
    r = tuple(cria_copia_posicao(posicao) for posicao in p["r"])
    a = tuple(cria_copia_animal(animal) for animal in p["a"])
    p = tuple(cria_copia_posicao(posicao) for posicao in p["p"])
        # Cópia da posição 'p["d"]' e tuplos com cópias das posições presentes
        # nos tuplos 'p["r"]', 'p["a"]' e 'p["p"]' do prado 'p'.
    
    return cria_prado(d, r, a, p)



##### Seletores #####


def obter_tamanho_x(m):
    
    """ obter_tamanho_x: prado -> int
    
    Devolve o valor inteiro que corresponde à dimensão Nx do prado. """
    
    return obter_pos_x(m["d"]) + 1
        # A dimensão Nx do prado corresponde ao valor da componente x da
        # posição que ocupa a montanha do canto inferior direito mais 1. """


def obter_tamanho_y(m):
    
    """ obter_tamanho_y: prado -> int
    
    Devolve o valor inteiro que corresponde à dimensão Ny do prado. """
    
    return obter_pos_y(m["d"]) + 1
        # A dimensão Ny do prado corresponde ao valor da componente y da
        # posição que ocupa a montanha do canto inferior direito mais 1. """


def obter_numero_predadores(m):
    
    """ obter_numero_predadores: prado -> int
    
    Devolve o número de animais predadores no prado. """
    
    return len([a for a in m["a"] if eh_predador(a)])
        # Cria-se uma lista com os animais do tuplo 'm["a"]' que são predadores
        # e devolve-se o número de elementos da mesma.


def obter_numero_presas(m):
    
    """ obter_numero_presas: prado -> int
    
    Devolve o número de animais presa no prado. """
    
    return len([a for a in m["a"] if eh_presa(a)])
        # Cria-se uma lista com os animais do tuplo "m["a"]" que são presas
        # e devolve-se o número de elementos da mesma.


def obter_posicao_animais(m):
    
    """ obter_posicao_animais: prado -> tuplo posicoes
    
    Devolve um tuplo contendo as posições do prado ocupadas por animais,
    ordenadas em ordem de leitura do prado. """
    
    return ordenar_posicoes(m["p"])
        # Devolve-se o tuplo correspondente à ordenação das posições do tuplo
        # 'm["p"]', com recurso à função 'ordenar_posicoes'.


def indice_posicao(t, p):
    
    """ indice_posicao: tuplo posicoes x posicao -> int
    
    Recebe um tuplo contendo posições não repetidas e uma posição, e devolve o
    índice em que essa posição se encontra no tuplo. """
    
    for i in range(len(t)):
        if posicoes_iguais(t[i], p):
            # Itera-se pelos índices das posições do tuplo 't' e, quando se
            # encontrar o índice cuja posição é igual à posição 'p', devolve-se
            # o seu valor (cada posição só aparece uma vez nesse tuplo).
            
            return i


def obter_animal(m, p):
    
    """ obter_animal: prado x posicao -> animal
    
    Devolve o animal do prado que se encontra na posição p. """
    
    return m["a"][ indice_posicao(m["p"], p) ]
        # Devolve-se o animal do tuplo 'm["a"]' cujo índice é aquele em que
        # aparece a posição 'p' no tuplo 'm["p"]'.



##### Modificadores #####


def eliminar_animal(m, p):
    
    """ eliminar_animal: prado x posicao -> prado
    
    Modifica destrutivamente o prado 'm' eliminando o animal da posição 'p'
    deixando-a livre. Devolve o próprio prado. """
    
    i = indice_posicao(m["p"], p)
        # Índice em que aparece a posição "p" no tuplo 'm["p"]'.
    
    m["p"] = m["p"][:i] + m["p"][i + 1:]
    m["a"] = m["a"][:i] + m["a"][i + 1:]
        # Alteram-se os valores do dicionário correspondentes às chaves 'p' e
        # 'a', passando estes a corresponder a tuplos iguais aos anteriores sem 
        # os elementos que tinham índice 'i'.
    
    return m


def mover_animal(m, p1, p2):
    
    """ mover_animal: prado x posicao x posicao -> prado
    
    Modifica destrutivamente o prado 'm' movimentando o animal da posição 'p1'
    para a nova posição 'p2', deixando livre a posição onde se encontrava.
    Devolve o próprio prado. """
    
    m = inserir_animal(m, obter_animal(m, p1), p2)
    m = eliminar_animal(m, p1)
        # Insere-se o animal que se encontra na posição 'p1' na posição 'p2' e,
        # de seguida, elimina-se o mesmo da posição 'p1'.
    
    return m


def inserir_animal(m, a, p):
    
    """ inserir_animal: prado x animal x posicao -> prado
    
    Modifica destrutivamente o prado 'm' acrescentando na posição 'p' do prado
    o animal 'a' passado como argumento. Devolve o próprio prado. """
    
    m["a"] = m["a"] + (a,)
    m["p"] = m["p"] + (p,)
        # Os tuplos 'm["a"]' e 'm["p"]' são substituídos pela concatenação de
        # si próprios com tuplos com, respetivamente, o animal e a 
        # correspondente posição que se pretendem inserir.
    
    return m



##### Reconhecedores #####


def eh_prado(arg):
    
    """ eh_prado: universal -> booleano
    
    Devolve True caso o seu argumento seja um TAD prado e False caso contrário.
    """
    
    return (     type(arg) == dict and arg.keys() == {"d", "r", "a", "p"}
             and validacao_cria_prado(arg["d"], arg["r"], arg["a"], arg["p"])
           )
                 # O argumento tem de ser um dicionário com quatro pares
                 # chave-valor, sendo as chaves "d", "r", "a" e "p", e os
                 # valores desse dicionário têm de originar um prado válido
                 # quando inseridos como argumentos da função "cria_prado",
                 # pelo que a função "validacao_cria_prado", com esses
                 # argumentos, tem de devolver True.


def eh_posicao_animal(m, p):
    
    """ eh_posicao_animal: prado x posicao -> booleano
    
    Devolve True apenas no caso da posição 'p' do prado estar ocupada por um
    animal. """
    
    return any([posicoes_iguais(p, m["p"][i]) for i in range(len(m["p"]))])
        # Se se encontrar uma posição igual a 'p' no tuplo 'm["p"]', quer dizer
        # que a posição 'p' está ocupada por um animal.


def eh_posicao_obstaculo(m, p):

    """ eh_posicao_obstaculo: prado x posicao -> booleano
    
    Devolve True apenas no caso da posição 'p' do prado corresponder a uma
    montanha ou rochedo. """
    
    return (    obter_pos_x(p) == 0 or obter_pos_y(p) == 0
             or obter_pos_x(p) == obter_tamanho_x(m) - 1
             or obter_pos_y(p) == obter_tamanho_y(m) - 1
             or any([posicoes_iguais(p, m["r"][i]) for i in range(len(m["r"]))])
           )
                # Uma posição corresponde a uma montanha se uma das suas
                # componentes for zero ou igual à respetiva componente da
                # posição do canto inferior direito do prado, e corresponde a
                # uma rocha se se encontrar uma posição igual a 'p' no tuplo
                # 'm["r"]'.


def eh_posicao_livre(m, p):
    
    """ eh_posicao_livre: prado x posicao -> booleano
    
    Devolve True apenas no caso da posição 'p' do prado corresponder a um
    espaço livre (sem animais, nem obstáculos). """
    
    return not eh_posicao_animal(m, p) and not eh_posicao_obstaculo(m, p)
        # Uma posição corresponde a um espaço livre se não estiver ocupada por
        # um animal nem por um obstáculo.



##### Teste #####


def prados_iguais(p1, p2):
    
    """ prados_iguais: prado x prado -> booleano
    
    Devolve True apenas se 'p1' e 'p2' forem prados e forem iguais. """
    
    return (     eh_prado(p1) and eh_prado(p2)
             and posicoes_iguais(p1["d"], p2["d"])
                 # 'p1' e 'p2' têm de ser do tipo prado e as posições dos seus
                 # cantos inferiores direitos têm de ser iguais.
             
             and {posicao_para_str(x) for x in p1["r"]} == \
                 {posicao_para_str(x) for x in p2["r"]}
             and len(p1["a"]) == len(p2["a"])
                 # Os sets constituídos pelas cadeias de carateres que
                 # representam as posições de 'p1["r"]' e de 'p2["r"]' têm de
                 # ter os mesmos elementos, e os tuplos 'p1["a"]' e 'p2["a"]'
                 # têm de ter o mesmo número de elementos (que também será
                 # igual ao dos tuplos 'p1["p"]' e 'p2["p"]').
             
             and {posicao_para_str(p1["p"][i]) : animal_para_str(p1["a"][i])
                  for i in range(len(p1["p"]))} == \
                 {posicao_para_str(p2["p"][i]) : animal_para_str(p2["a"][i])
                  for i in range(len(p2["p"]))}
                 # Cria-se, para cada argumento, um dicionário cujas chaves e
                 # valores são as cadeias de carateres que representam as
                 # posições ocupadas por animais as que representam os animais
                 # que ocupam tais posições, respetivamente. Os dicionários têm
                 # de ter exatamente os mesmos pares chave-valor.
           )



##### Transformador #####


def prado_para_str(m):
    
    """ prado_para_str: prado -> str
    
    Devolve uma cadeia de carateres que representa o prado. """
    
    prado_str = f'+{ "-" * (obter_tamanho_x(m) - 2) }+\n'
        # A primeira linha começa e acaba com um caráter '+' e, entre esses
        # dois, tem carateres '-' de maneira a que o número total de carateres
        # da linha seja igual à dimensão Nx do prado.
    
    for y in range(1, obter_tamanho_y(m) - 1):
        # As linhas intermédias começam e acabam com '|', e, para as restantes
        # posições, aparece '.' se a posição estiver livre, '@' se a posição
        # tiver um rochedo, e uma letra se a posição tiver um animal.
        
        prado_str += "|"
        
        for x in range(1, obter_tamanho_x(m) - 1):
            p = cria_posicao(x, y)
            
            if eh_posicao_animal(m, p):
                prado_str += f'{animal_para_char(obter_animal(m, p))}'
                    # A letra que aparece nas posições com animais é obtida com
                    # recurso à função 'animal_para_char'.
            
            elif eh_posicao_obstaculo(m, p):
                prado_str += "@"
            
            else: # Posição livre.
                prado_str += "."
    
    
        prado_str += "|\n"
    
    prado_str += f'+{ "-" * (obter_tamanho_x(m) - 2) }+'
        # A última linha é igual à primeira.
    
    return prado_str



##### Funções de alto nível #####


def obter_valor_numerico(m, p):
    
    """ obter_valor_numerico: prado x posicao -> int
    
    Devolve o valor numérico da posição 'p' correspondente à ordem de leitura no
    prado 'm'. """
    
    return obter_pos_y(p) * obter_tamanho_x(m) + obter_pos_x(p)


def obter_movimento(m, p):
    
    """ obter_movimento: prado x posicao -> posicao
    
    Devolve a posição seguinte do animal na posição 'p' dentro do prado 'm' de
    acordo com as regras de movimento dos animais no prado. """
    
    obter_pos_adj = list(obter_posicoes_adjacentes(p))
        # Lista obtida das posições adjacentes a 'p'.
    
    animal = obter_animal(m, p)
    
    if eh_predador(animal):
        
        pos_adj = obter_pos_adj[:]
            # Cópia da lista obtida das posições adjacentes a 'p'.
        
        for i in range( len(pos_adj) - 1 , -1, -1):
            # Itera-se pelos índices dos elementos da lista, do fim para o
            # início.
            
            if not (     eh_posicao_animal(m, pos_adj[i])
                     and eh_presa(obter_animal(m, pos_adj[i])) ):
                         # Se a posição de índice 'i' não corresponder a uma
                         # presa, elimina-se da lista. Se, no fim, a lista
                         # ficar vazia, significa que não há presas nas
                         # posições adjacentes.
                
                del pos_adj[i]
    
    if eh_presa(animal) or len(pos_adj) == 0:
        # Caso o animal seja presa ou caso o animal seja predador e não haja
        # presas nas posições adjacentes.
        
        pos_adj = obter_pos_adj[:]
            # Cópia da lista obtida das posições adjacentes a 'p'.
        
        for i in range( len(pos_adj) - 1 , -1, -1):
            # Itera-se pelos índices dos elementos da lista, do fim para o
            # início.
            
            if not eh_posicao_livre(m, pos_adj[i]):
                # Se a posição de índice 'i' não estiver livre, elimina-se da
                # lista.
                
                del pos_adj[i]
    
    if len(pos_adj) == 0:
        # Se a lista final das posições possíveis estiver vazia, o animal
        # mantém-se na mesma posição ...
        
        return cria_copia_posicao(p)
    
    else:
        # ... caso contrário, seleciona-se uma posição de acordo com as regras.
        
        Np = len(pos_adj)
            # Número de possíveis posições.
        N = obter_valor_numerico(m, p)
        
        return cria_copia_posicao(pos_adj[N % Np])




''' ############################################################################
    2.2 Funções adicionais
''' ############################################################################



##### 2.2.1 geracao #####


def geracao(m):
    
    """ geracao: prado -> prado
    
    Função auxiliar que modifica o prado 'm' fornecido como argumento de acordo
    com a evolução correspondente a uma geração completa, e devolve o próprio
    prado. Isto é, seguindo a ordem de leitura do prado, cada animal (vivo)
    realiza o seu turno de ação de acordo com as regras descritas. """
    
    posicoes_animais = list(obter_posicao_animais(m))
        # Lista das posições do prado com animais.
    
    i = 0
    
    while i < len(posicoes_animais):
        # Itera-se pelos índices das posições do prado com animais. Como podem
        # ser eliminados elementos da lista, não se usa um ciclo for.
        
        animal = obter_animal(m, posicoes_animais[i])
        
        aumenta_idade(animal)
        
        if eh_predador(animal):
            
            aumenta_fome(animal)
        
        posicao_nova = obter_movimento(m, posicoes_animais[i])
            # Posição seguinte do animal, de acordo com as regras de movimento.
        
        if not posicoes_iguais(posicoes_animais[i], posicao_nova):
            # Se a posição seguinte não for igual à atual, o animal move-se,
            # podendo, se for caso disso, comer outro animal ou reproduzir-se.
            
            if (     eh_predador(animal) and eh_posicao_animal(m, posicao_nova)
                 and eh_presa(obter_animal(m, posicao_nova)) ):
                     # Se o animal for predador e na posição seguinte estiver
                     # uma presa, a mesma é comida (eliminada) e a fome do
                     # animal é redefinida para 0.
                
                eliminar_animal(m, posicao_nova)
                
                reset_fome(animal)
                
                for j in range(i + 1, len(posicoes_animais)):
                    if posicoes_iguais(posicao_nova, posicoes_animais[j]):
                        # Se a presa que estava na posição nova não tiver tido
                        # turno nesta geração, ou seja, se a posição nova
                        # aparecer, pela ordem de leitura, a seguir à posição
                        # atual do predador, tem de se eliminar essa posição da
                        # lista de posições, caso contrário, o predador
                        # voltaria a ter turno nesta geração.
                        
                        del posicoes_animais[j]
                        
                        break
                            # Cada posição só aparece uma vez na lista, pelo
                            # que, se for encontrada uma posição igual, pode-se
                            # terminar o ciclo.
            
            if eh_animal_fertil(animal):
                # Se o animal atingiu a idade de reprodução, a sua idade é
                # redefinida para 0 e fica, na posição anterior, um outro
                # animal, obtido com recurso à função 'reproduz_animal'.
                
                inserir_animal(m, reproduz_animal(animal), posicoes_animais[i])
            
            mover_animal(m, posicoes_animais[i], posicao_nova)
        
        if eh_predador(animal) and eh_animal_faminto(animal):
            # Se o animal for predador e, após o turno, estiver faminto, morre.
            
            eliminar_animal(m, posicao_nova)
        
        i += 1
    
    return m



##### 2.2.2 simula_ecossistema #####


def simula_ecossistema_prado(f):
    
    """ simula_ecossistema_prado: str -> prado
    
    Recebe uma cadeia de carateres 'f', correspondente ao nome do ficheiro de
    configuração da simulação, e devolve o prado definido pelo mesmo. """
    
    with open(f, 'r') as file:
        
        # 1. Posição da montanha do canto inferior direito do prado, 'd':
        
        d_tuple = eval(file.readline())
        d = cria_posicao(d_tuple[0], d_tuple[1])
            # 'd_tuple' é o tuplo representado pela primeira linha do ficheiro.
        
        # 2. Tuplo das posições dos rochedos, 'r':
        
        r_tuple = eval(file.readline())
            # 'r_tuple' é o tuplo representado pela segunda linha do ficheiro.
        
        r = ()
        
        for elemento in r_tuple:
            # Os elementos do tuplo 'r_tuple' são tuplos de dois elementos,
            # correspondentes, respetivamente, às componentes x e y de cada
            # posição ocupada por um rochedo.
            
            r += (cria_posicao(elemento[0], elemento[1]),)
        
        # 3. Tuplos dos animais e das posições ocupadas por eles, 'a' e 'p':
        
        a = ()
        p = ()
        
        lines = list(map(eval, file.readlines()))
        
        for line in lines:
            # 'line', corresponderá, para cada uma das restantes linhas do
            # ficheiro, ao tuplo representado por essa linha, cujos
            # elementos são a espécie do animal, a sua frequência de
            # reprodução, a sua frequência de alimentação e o tuplo cujos
            # elementos correspondem, respetivamente, às componentes x e y
            # da sua posição.
            
            a += ( cria_animal(line[0], line[1], line[2]) ,)
            p += ( cria_posicao(line[3][0], line[3][1]) ,)
    
    return cria_prado(d, r, a, p)


def simula_ecossistema(f, g, v):
    
    """ simula_ecossistema: str x int x booleano -> tuplo
    
    Função principal que permite simular o ecossistema de um prado. Recebe uma
    cadeia de carateres 'f', correspondente ao nome do ficheiro de configuração
    da simulação, um valor inteiro 'g', correspondente ao número de gerações a
    simular, e um valor booleano 'v', que ativa o modo 'verboso' (True) ou o
    modo 'quiet' (False); e devolve o tuplo de dois elementos correspondentes
    ao número de predadores e presas no prado no fim da simulação. """
    
    prado = simula_ecossistema_prado(f)
    
    n_predadores_anterior = 0
    n_presas_anterior = 0
        # Inicialmente, o prado tem, pelo menos, um animal, pelo que pelo menos
        # um dos predicados 'n_predadores_anterior != n_predadores_atual' ou
        # 'n_presas_anterior != n_presas_atual' será sempre verdadeiro para
        # 'gen' igual a 0.
    
    for gen in range(g + 1):
        
        n_predadores_atual = obter_numero_predadores(prado)
        n_presas_atual = obter_numero_presas(prado)
        
        if (    (v and (    n_predadores_anterior != n_predadores_atual
                         or n_presas_anterior != n_presas_atual) )
                 # No modo verboso, após cada geração, mostra-se o prado apenas
                 # se o número de predadores ou presas se tiver alterado.
            
             or (not v and gen in (0, g))
                # No modo quiet, mostra-se o prado no início da simulação e
                # após a última geração.
           ):
            
            print(f"Predadores: {n_predadores_atual} vs Presas: " + \
                  f"{n_presas_atual} (Gen. {gen})")
            
            print(prado_para_str(prado))
        
        geracao(prado)
        
        n_predadores_anterior = n_predadores_atual
        n_presas_anterior = n_presas_atual
    
    return (n_predadores_atual, n_presas_atual)