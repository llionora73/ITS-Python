
messaggi = ["ciao", "arrivederci", "benvenuto", "addio", "come stai?"]
sent_messages =  []

def show_messages(messaggi, sent_messages) -> None:
    for messaggio in messaggi:
        print(messaggio)
        sent_messages.append(messaggio)
    print(f"Messaggi originali: {messaggi}")
    print(f"Lista dei messaggi inviati:{sent_messages}")

show_messages(messaggi, sent_messages)