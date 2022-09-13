def print_introduction():
    print(
        "\n+----------------------------------------------------------------------------------------------------------+\n"
        "|                                               118.py                                                     |\n"
        "+----------------------------------------------------------------------------------------------------------+\n"
        "| 118.py è un programma che simula il funzionamento del servizio sanitario di urgenza "
        "ed emergenza medica. |\n"
        "| Il programma consente di generare delle chiamate di emergenza in due modi:                               |\n"
        "|                                                                                                          |\n"
        "| 1) tramite input attraverso la tastiera;                                                                 |\n"
        "| 2) auto-generata in modo casuale.                                                                        |\n"
        "|                                                                                                          |\n"
        "| In base alla richiesta di soccorso, si individuerà qual'è l'ospedale che puo' intervenire nei tempi      |\n"
        "| richiesti e con le giuste risorse.                                                                       |\n"
        "| Per interagire col programma digita i numeri affiancati alle diverse voci del menù,                      |\n"
        "| ciascuna delle quali corrisponde ad una funzionalità diversa.                                            |\n"
        "+----------------------------------------------------------------------------------------------------------+\n")


def printmenu():

    print("+------------------------------------------------------+\n"
          "|                        Menu'                         |\n"
          "+------------------------------------------------------+\n"
          "| 1) Effettua una chiamata manualmente                 |\n"
          "| 2) Genera una chiamata automatica con valori casuali |\n"
          "| 3) Visualizza lo stato degli ospedali                |\n"
          "| 4) Gestisci lo stato delle chiamate                  |\n"
          "| 5) Visualizza il grafo                               |\n"
          "| 6) Aiuto                                             |\n"
          "| 7) Esci                                              |\n"
          "+------------------------------------------------------+")
    print()


def print_help():
    print("+------------------------------------------------------------------------------------------------------+")
    print("|                                               Aiuto                                                  |")
    print("+------------------------------------------------------------------------------------------------------+")
    print("| Il programma consente di simulare il funzionamento del sistema del 118.                              |")
    print("| L'applicazione presenta diverse funzionalita', si seguito si riporta la loro spiegazione:            |")
    print("|                                                                                                      |")
    print("| - Effettua una chiamata manualmente:                                                                 |")
    print("|       Consente di generare una chiamata di aiuto, permettendo di inserire, attraverso la tastiera,   |")
    print("|       le condizioni che il paziente presenta. In base alle condizioni di salute del paziente,        |")
    print("|       il programma verificherà quale ospedale presenta le giuste risorse per poter prendersi         |")
    print("|       cura del paziente.                                                                             |")
    print("|                                                                                                      |")
    print("| - Genera una chiamata automatica con valori casuali:                                                 |")
    print("|       Permette di generare una chiamata in modo automatico, la condizione del paziente verrà         |")
    print("|       generata in modo casuale e successivamente il programma verificherà quale ospedale può         |")
    print("|       prendersi cura del paziente.                                                                   |")
    print("|                                                                                                      |")
    print("| - Visualizza lo stato degli ospedali:                                                                |")
    print("|       Permette di visualizzare le risorse disponibili nei vari ospedali.                             |")
    print("|                                                                                                      |")
    print("| - Gestisci lo stato delle chiamate:                                                                  |")
    print("|       Consente di visualizzare il registro delle chiamate effettuate e di indicare quale chiamata    |")
    print("|       è stata completata, ovvero se l'ambulanza ha portato a termine il percorso.                    |")
    print("|       Quando una chiamata viene segnata come \"completata\", le risorse dell'ospedale che ha           |")
    print("|       intervenuto vengono ripristinate                                                               |")
    print("|                                                                                                      |")
    print("| - Visualizza il grafo:                                                                               |")
    print("|       Permette di visualizzare il grafo. Per ogni nodo viene mostrato i nodi che sono                |")
    print("|       ad esso collegati ed il costo.                                                                 |")
    print("|                                                                                                      |")
    print("| - Esci:                                                                                              |")
    print("|       Consente di terminare l'esecuzione del programma.                                              |")
    print("+------------------------------------------------------------------------------------------------------+")
    print()


def print_hospital_menu():
    print("+-------------------------------------------+")
    print("|               Menu' ospedali              |")
    print("+-------------------------------------------+")
    print("| Visualizza le informazioni dell'ospedale: |")
    print("|                                           |")
    print("| 1) ospedale 1                             |")
    print("| 2) ospedale 2                             |")
    print("| 3) ospedale 3                             |")
    print("| 4) ospedale 4                             |")
    print("| 5) ospedale 5                             |")
    print("| 6) ritorna al menu' principale            |")
    print("+-------------------------------------------+")


def print_upgrade_calls_menu():
    print("+--------------------------------------+")
    print("|            Menu chiamate             |")
    print("+--------------------------------------+")
    print("| 1) Visualizza registro chiamate      |")
    print("| 2) Aggiorna lo stato di una chiamata |")
    print("| 3) Ritorna al menu' principale       |")
    print("+--------------------------------------+")
