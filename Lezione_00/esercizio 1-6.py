# esercizio 1-6

menu: dict= {"primi": {"Pizza": 9.00 , "Pasta": 10.50, "Zuppa" : 7.00 },
              "secondi": {"Hamburger": 15.50, "Cotoletta": 10.00, "Salmone" : 20.20}, 
              "contorni": {"Patatine Fritte": 5.50, "Patate al forno": 5.50, "Verdura del giorno": 7.00}, 
              "dolce": {"Cheesecake": 6.00, "Tiramisù": 6.00, "Focaccia con Nutella": 6.00}, 
              "bevande": {"Coca Cola": 3.50, "Acqua": 1.50, "Vino": 5.00}}

ordine: dict= {"primi": "Pasta",
               "secondi": "Cotoletta", 
               'contorni': 'Patate al forno', 
               'bevande': 'Coca Cola', 
               'dolce': 'Tiramisù'}

conto_totale = 0


conto_totale += menu['primi'][ordine['primi']]
conto_totale += menu['secondi'][ordine['secondi']]
conto_totale += menu['contorni'][ordine['contorni']]
conto_totale += menu['bevande'][ordine['bevande']]
conto_totale += menu['dolce'][ordine['dolce']]

print(f"Il conto totale da pagare è: €{conto_totale:.2f}")










