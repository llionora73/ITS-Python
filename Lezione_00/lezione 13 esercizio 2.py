# Si supponga di voler calcolare l'ammontare del denaro depositato su un conto bancario ad interesse composto. 
# Se m è la somma depositata sul conto, la somma disponibile alla fine del mese sarà 1.005 volte m.
# Scrivere una funzione ricorsiva compoundInterest che calcoli la somma presente sul conto dopo t mesi data una somma di partenza m.


def compoundInterest(m:float, t:int) -> float:
# if t<=0 ritorna m, un float con 2 cifre decimali
    if t <= 0:
        return round(m, 2)
# if t =1 saldo sul conto sarà 1.005 * m = 1.005 * 1000 = 1005
# if t =2 saldo = 1.005 * 1.005 = 1.010
# if t= 3 saldo = 1.010 * 1.005 * 1.015

    else:
        return round(1.005 * compoundInterest(m, t-1), 2)
        
print(compoundInterest(1000, 9))
