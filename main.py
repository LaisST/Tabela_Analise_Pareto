#Declaração das variaveis que irão armazenar a quantidade de ocorrências.
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
acumulo = 0
# Solicitação do nome do arquivo onde estão as variaveis qualitativas nominais para análise.

arquivo = input("Qual arquivo deseja abrir para fazer a análise? \n")
defeitos = open(arquivo, "rt")
        

#Contagem dos dados qualitativos nominais armazenados no arquivo .txt.
for x in defeitos:
    if x == 'A\n':
        a += 1 
    elif x == 'B\n':
        b += 1 
    elif x == 'C\n':
        c += 1
    elif x == 'D\n':
        d += 1
    elif x == 'E\n':
        e += 1
    elif x == 'F\n':
        f += 1
    elif x == 'G\n':
        g += 1
        
#Calculo total de ocorrências   
totalfr = a + b + c + d + e + f + g

#Dicionário onde a Key é o tipo de defeito e o value é a quantidade de ocorrências para cada defeito.
Dic = { "A - Defeito na cobertura plástica": a, 
        "B - Defeito no teclado": b, 
        "C - Defeito na fonte de energia": c, 
        "D - Soldas soltas": d, 
        "E - Defeito na placa da unidade de processamento": e, 
        "F - Defeito no visor": f,
        "G - Outros": g
    
}
#Inicio ta tabela contendo quatro colunas: Defeito, quantidade, frequencia em % e o total acumulado em %.
print("\033[1;36m ___________________________________________________________________________________________\033[m ")
print("\033[1;36m|                                                                                           |\033[m")
print("\033[1;36m|                 Relatório de Defeitos da Fabrica de Calculadoras                          |\033[m")
print("\033[1;36m|___________________________________________________________________________________________|\033[m")
print("\033[1;36m|                  Defeito                       | Quantidade |    Fr%    |  Acumulado(fr%) |\033[m")

#Loop para ler cada item do dicionário em sua devida posição. Calculo da frequencia em % e soma do Fr% 
#para calculo do acumulado em %.

analise = {}
c = 0 #Variavel contador para o loop.
while c < len(Dic):
    for i in sorted(Dic, key = Dic.get, reverse=True):
        fr = (Dic[i]/totalfr*100) #Calculo de frequencia em %.
        if c == 0:
            acumulo = fr
            print("\033[1;36m|\033[m{:48}{}|{} {:6}     {}|{}  {:5.2f}%   {}|{}    {:6.2f}%      {}|{}".format(i,'\033[1;36m', '\033[m', Dic[i],'\033[1;36m', '\033[m', fr,'\033[1;36m', '\033[m', acumulo, '\033[1;36m', '\033[m'))

        else: 
            acumulo = acumulo +fr
            print("\033[1;36m|\033[m{:48}{}|{} {:6}     {}|{}  {:5.2f}%   {}|{}    {:6.2f}%      {}|{}".format(i,'\033[1;36m', '\033[m', Dic[i],'\033[1;36m', '\033[m', fr,'\033[1;36m', '\033[m', acumulo, '\033[1;36m', '\033[m'))

        c +=1

print("\033[1;36m|                                                |            |           |                 |\033[m")
print("\033[1;36m|\033[mTotal                                           \033[1;36m|\033[m {:6}     \033[1;36m|\033[m  {:5.2f}%  \033[1;36m|\033[m                 \033[1;36m|\033[m".format(totalfr, acumulo))
print("\033[1;36m|___________________________________________________________________________________________|\033[m")
print("\033[1;36m|                                                                                           |\033[m")
print("\033[1;36m|                            Fonte: Exercicio de sala                                       |\033[m")
print("\033[1;36m|___________________________________________________________________________________________\033[1;36m|\033[m")
#Fim da tabela.