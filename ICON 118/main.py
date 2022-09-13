import Classifier
import CosineSimilarity
import warnings
import Utils
import Prints
from HospitalResources import HospitalResources
import knowledge_base
import os
import random
from graph import Graph


# resourcesInsertion definisce il numero di risorse necessarie in base alla tipologia di codice
def resourcesInsertion(code, node):
    # Codice Bianco
    if (code == 0):
        hr = HospitalResources(80, 'SSP', 1, 0, 0, node)
    # Codice Verde
    if (code == 1):
        hr = HospitalResources(60, 'A', 0, 1, 1, node)
    # Codice Giallo
    if (code == 2):
        hr = HospitalResources(40, 'B', 1, 1, 1, node)
    # Codice Rosso
    if (code == 3):
        hr = HospitalResources(20, 'C', 1, 2, 1, node)

    return hr


# random_call genera una chiamata di richiesta di soccorso con valori casuali
def random_call(graph):
    test = [[]]
    tempList = []
    pathology = 0

    print()
    print("Generazione di una chiamata di soccorso in corso...")
    pathology = random.randint(0, 7)

    tempList.append(pathology)
    n = random.randint(0, 10)
    if n > 7:
        tempList.append(1)  # coscienza
    else:
        tempList.append(0)
    tempList.append(random.randint(0, 3))  # lesioni
    tempList.append(random.randint(0, 2))  # respiro
    tempList.append(random.randint(0, 1))  # dolore toracico
    tempList.append(random.randint(0, 1))  # emorragia
    tempList.append(random.randint(0, 3))  # ustioni

    print("Informazioni sul paziente generate: ")
    print()
    print("Patologia: " + Utils.switch_pathology(pathology))

    if tempList[1] == 0:
        string_cos = "presente"
    else:
        string_cos = "assente"
    print("Stato di coscienza del paziente: " + string_cos)

    if tempList[2] == 0:
        string_les = "assenti"
    if tempList[2] == 1:
        string_les = "lievi"
    if tempList[2] == 2:
        string_les = "medie"
    if tempList[2] == 3:
        string_les = "gravi"
    print("Lesioni: " + string_les)

    if tempList[3] == 0:
        string_res = "normale"
    if tempList[3] == 1:
        string_res = "irregolare"
    if tempList[3] == 2:
        string_res = "assente"
    print("Respiro: " + string_res)

    if tempList[4] == 0:
        string_dol = "assente"
    if tempList[4] == 1:
        string_dol = "presente"
    print("Dolore toracico: " + string_dol)

    if tempList[5] == 0:
        string_emo = "assente"
    if tempList[5] == 1:
        string_emo = "presente"
    print("Emorragia: " + string_emo)

    if tempList[6] == 0:
        string_ust = "assente"
    if tempList[6] == 1:
        string_ust = "primo grado"
    if tempList[6] == 2:
        string_ust = "secondo grado"
    if tempList[6] == 3:
        string_ust = "terzo grado"
    print("Grado di ustioni: " + string_ust)

    test = [tempList]

    ROOT_DIR = os.path.abspath(os.curdir)
    code = Classifier.classify(test, Utils.fixPath(ROOT_DIR) + '/resources/datasetICON.csv')

    nodeNamesList = list(graph.adjac_lis.keys())
    nodeNamesList.remove('O1')
    nodeNamesList.remove('O2')
    nodeNamesList.remove('O3')
    nodeNamesList.remove('O4')
    nodeNamesList.remove('O5')

    randomNode = nodeNamesList[random.randint(0, len(nodeNamesList) - 1)]


    return code, pathology, randomNode


# input_call genera una chiamata di richiesta di soccorso tramite tastiera
def input_call(graph):
    warnings.filterwarnings("ignore")

    tempList = []
    pathology = 0

    print()
    words = input('Descrivi con poche parole i sintomi del paziente (premi invio per saltare): ')
    if(not(words == "")):
        #print('Entrato')
        cosValue, index = CosineSimilarity.calculateSimilarity(words)

        if (index == -1 or (cosValue >= 0 and cosValue < 0.1)):
            tempList.append(0)
        else:
            pathology = index + 1
            tempList.append(pathology)
    else:
        tempList.append(0)

    correct = False
    while correct == False:
        temp = input('Il paziente è cosciente? (si: 0,  no: 1) >>_')
        if temp == "1":
            tempList.append(int(temp))
            correct = True
        elif temp == "0":
            tempList.append(int(temp))
            correct = True
        else:
            print("Input non valido.")

    correct = False
    while correct == False:
        temp = input('Il paziente presenta lesioni? (no: 0,  lievi: 1, medie: 2, gravi: 3) >>_')
        if temp == "0":
            tempList.append(int(temp))
            correct = True
        elif temp == "1":
            tempList.append(int(temp))
            correct = True
        elif temp == "2":
            tempList.append(int(temp))
            correct = True
        elif temp == "3":
            tempList.append(int(temp))
            correct = True
        else:
            print("Input non valido.")

    correct = False
    while correct == False:
        temp = input('Il paziente respira? (si: 0,  respira con fatica: 1, no: 2) >>_')
        if temp == "0":
            tempList.append(int(temp))
            correct = True
        elif temp == "1":
            tempList.append(int(temp))
            correct = True
        elif temp == "2":
            tempList.append(int(temp))
            correct = True
        else:
            print("Input non valido.")

    correct = False
    while correct == False:
        temp = input('Il paziente presenta dolore toracico? (no: 0, si: 1) >>_')
        if temp == "0":
            tempList.append(int(temp))
            correct = True
        elif temp == "1":
            tempList.append(int(temp))
            correct = True
        else:
            print("Input non valido.")

    correct = False
    while correct == False:
        temp = input('Il paziente presenta un emorragia? (no: 0,  si: 0) >>_')
        if temp == "0":
            tempList.append(int(temp))
            correct = True
        elif temp == "1":
            tempList.append(int(temp))
            correct = True
        else:
            print("Input non valido.")

    correct = False
    while correct == False:
        temp = input('Il paziente presente ustioni? (0: no, lievi: 1, medie: 2, gravi: 3) >>_')
        if temp == "0":
            tempList.append(int(temp))
            correct = True
        elif temp == "1":
            tempList.append(int(temp))
            correct = True
        elif temp == "2":
            tempList.append(int(temp))
            correct = True
        elif temp == "3":
            tempList.append(int(temp))
            correct = True
        else:
            print("Input non valido.")

    test = [tempList]

    ROOT_DIR = os.path.abspath(os.curdir)
    code = Classifier.classify(test, ROOT_DIR + '/resources/datasetICON.csv')

    nodeNamesList = list(graph.adjac_lis.keys())
    nodeNamesList.remove('O1')
    nodeNamesList.remove('O2')
    nodeNamesList.remove('O3')
    nodeNamesList.remove('O4')
    nodeNamesList.remove('O5')

    randomNode = nodeNamesList[random.randint(0, len(nodeNamesList) - 1)]

    return code, pathology, randomNode


# process_call verifica quale ospedale può intervenire alla chiamata generata, interroga la base di conoscenza
# e aggiorna le risorse
def process_call(code, pathology, randomNode, graph, id_call, one_call):
    if code == 0:
        string_code = "BIANCO"
    if code == 1:
        string_code = "VERDE"
    if code == 2:
        string_code = "GIALLO"
    if code == 3:
        string_code = "ROSSO"

    print()
    print("La chiamata di emergenza e' stata effettuata dal nodo", end=": ")
    print(randomNode)
    print("Il codice generato per il paziente e': " + string_code)
    print()
    print("Interrogazione della base di conoscenza in corso...")

    hr = resourcesInsertion(code, randomNode)


    time1 = graph.timeForPath(graph.a_star_algorithm(randomNode, 'O1'))
    kb.assertz("tempo(ospedale_1, " + str(time1) + ")")

    time2 = graph.timeForPath(graph.a_star_algorithm(randomNode, 'O2'))
    kb.assertz("tempo(ospedale_2, " + str(time2) + ")")

    time3 = graph.timeForPath(graph.a_star_algorithm(randomNode, 'O3'))
    kb.assertz("tempo(ospedale_3, " + str(time3) + ")")

    time4 = graph.timeForPath(graph.a_star_algorithm(randomNode, 'O4'))
    kb.assertz("tempo(ospedale_4, " + str(time4) + ")")

    time5 = graph.timeForPath(graph.a_star_algorithm(randomNode, 'O5'))
    kb.assertz("tempo(ospedale_5, " + str(time5) + ")")

    department = Utils.switch_department(pathology)

    # Vengono definite le query che andranno ad interrogare la base di conoscenza

    # In base al codice, il paziente verrà trasportato all'ospedale più vicino che ha il giusto reparto che può
    # risolvere la problematica del paziente

    strQueryRed = "ospedale(X), tempo(X,Y), infermieri(X,I), soccorritori(X,S), medici(X,M), ambulanza_C(X,C), gestione(X,D,P), " \
                  "Y < " + str(hr.time + 1) + ", I >= " + str(hr.nurses) + ", S >= " + str(hr.rescuers) + ", M >= " \
                  + str(hr.doctors) + ", C >= 1, Y =\= 0, D = " + department + ", P = 1"

    strQueryYellow = "ospedale(X), tempo(X,Y), infermieri(X,I), soccorritori(X,S), medici(X,M), ambulanza_B(X,B)," \
                     " gestione(X,D,P), Y < " + str(hr.time + 1) + ", I >= " + str(hr.nurses) + ", S >= " \
                     + str(hr.rescuers) + ", M >= " + str(hr.doctors) + ", B >= 1, D = " + department + \
                     ", P = 1, Y =\= 0"

    strQueryGreen = "ospedale(X), tempo(X,Y), infermieri(X,I), soccorritori(X,S), medici(X,M), ambulanza_A(X,A), gestione(X,D,P), " \
                    "Y < " + str(hr.time + 1) + ", I >= " + str(hr.nurses) + ", S >= " + str(hr.rescuers) + \
                    ", M >= " + str(hr.doctors) + ", A >= 1, D = " + department + ", P = 1,Y =\= 0"

    strQueryWhite = "ospedale(X), tempo(X,Y), infermieri(X,I), soccorritori(X,S), medici(X,M), ambulanza_SSP(X,SSP), gestione(X,D,P), " \
                    "Y < " + str(hr.time + 1) + ", I >= " + str(hr.nurses) + ", S >= " + str(hr.rescuers) + ", M >= " \
                    + str(hr.doctors) + ", SSP >= 1, D = " + department + ", P = 1, Y =\= 0"

    # La query che viene utilizzata dipende dal codice di emergenza (rosso,verde,giallo,bianco)

    if (code == 0):
        strQuery = strQueryWhite
    if (code == 1):
        strQuery = strQueryGreen
    if (code == 2):
        strQuery = strQueryYellow
    if (code == 3):
        strQuery = strQueryRed

    # Si interroga la base di conoscenza

    myList = list(kb.query(strQuery))

    if len(myList) > 0:
        print("Gli ospedali che sono in grado di rispondere alla richiesta di soccorso sono:")
        for item in myList:
            print(item['X'])

        if len(myList) != 0:
            minOsp = myList[0]
            for osp in myList:
                if(osp['Y'] < minOsp['Y']):
                    minOsp = osp
            print()
            print("L'ospedale che riesce ad inviare un'ambulanza nel minor tempo possibile e':", minOsp['X'])
            if minOsp['X'] == "ospedale_1":
                path = graph.a_star_algorithm(randomNode, "O1")
            if minOsp['X'] == "ospedale_2":
                path = graph.a_star_algorithm(randomNode, "O2")
            if minOsp['X'] == "ospedale_3":
                path = graph.a_star_algorithm(randomNode, "O3")
            if minOsp['X'] == "ospedale_4":
                path = graph.a_star_algorithm(randomNode, "O4")
            if minOsp['X'] == "ospedale_5":
                path = graph.a_star_algorithm(randomNode, "O5")

            print('Percorso effettuato: :{}'.format(path))
    else:
        print()
        print("Nessun ospedale e' in grado di intervenire.")

    print()
    if(len(myList) != 0):

        # per ogni chiamata, nella kb si inseriscono i suoi relativi dati, i dati sono i seguenti:
        # - id della chiamata
        # - codice generato
        # - nodo da cui parte la chiamata
        # - ospedale che risponde alla chiamata
        # - stato sul tragitto dell'ambulanza (0: non completato, 1: completato)

        node = Utils.switch_letter_to_number(str(randomNode))
        kb.assertz("chiamata(" + str(id_call) + ", " + str(code) + ", " + str(node) + ", " + minOsp['X'] + ", " + str(0) + ")")

        one_call = True

        #Dall'ospedale che risponderà alla chiamata di soccorso, vengono individuati i valori delle
        #risorse disponibili,i quali verranno sottratti al numero di risorse richieste.

        query_doctors = "medici(X,Y)"
        list_doctors = list(kb.query(query_doctors))
        for item in list_doctors:
            if item['X'] == minOsp['X']:
                doctors_number = item['Y']

        query_nurses =  "infermieri(X,Y)"
        list_nurses = list(kb.query(query_nurses))
        for item in list_nurses:
            if item['X'] == minOsp['X']:
                nurses_number = item['Y']

        query_rescuers = "soccorritori(X,Y)"
        list_rescuers = list(kb.query(query_rescuers))
        for item in list_rescuers:
            if item['X'] == minOsp['X']:
                rescuers_number = item['Y']

        query_ambulance_A = "ambulanza_A(X,Y)"
        list_ambulance_A = list(kb.query(query_ambulance_A))
        for item in list_ambulance_A:
            if item['X'] == minOsp['X']:
                ambulance_A_number = item['Y']

        query_ambulance_B = "ambulanza_B(X,Y)"
        list_ambulance_B = list(kb.query(query_ambulance_B))
        for item in list_ambulance_B:
            if item['X'] == minOsp['X']:
                ambulance_B_number = item['Y']

        query_ambulance_C = "ambulanza_C(X,Y)"
        list_ambulance_C = list(kb.query(query_ambulance_C))
        for item in list_ambulance_C:
            if item['X'] == minOsp['X']:
                ambulance_C_number = item['Y']

        query_ambulance_SSP = "ambulanza_SSP(X,Y)"
        list_ambulance_SSP = list(kb.query(query_ambulance_SSP))
        for item in list_ambulance_SSP:
            if item['X'] == minOsp['X']:
                ambulance_SSP_number = item['Y']

        #Per ogni tipologia di codice, si inizializzano le variabili che verranno usate per modificare il numero
        #delle risorse disponibili.

        if str(code) == "[3]": #se codice rosso

            doctors_needed = 1
            nurses_needed = 2
            rescuers_needed = 1
            ambulance_A_needed = 0
            ambulance_B_needed = 0
            ambulance_C_needed = 1
            ambulance_SSP_needed = 0

        if str(code) == "[2]": #se codice giallo

            doctors_needed = 1
            nurses_needed = 1
            rescuers_needed = 1
            ambulance_A_needed = 0
            ambulance_B_needed = 1
            ambulance_C_needed = 0
            ambulance_SSP_needed = 0

        if str(code) == "[1]":  # se codice verde

            doctors_needed = 0
            nurses_needed = 1
            rescuers_needed = 1
            ambulance_A_needed = 1
            ambulance_B_needed = 0
            ambulance_C_needed = 0
            ambulance_SSP_needed = 0

        if str(code) == "[0]":  # se codice bianco

            doctors_needed = 0
            nurses_needed = 0
            rescuers_needed = 1
            ambulance_A_needed = 0
            ambulance_B_needed = 0
            ambulance_C_needed = 0
            ambulance_SSP_needed = 1

        #Aggiornamento della base di conoscenza

        # aggiornamento medici
        kb.retract("medici(" + minOsp['X'] + ", " + str(doctors_number) + ")")
        doc_number = int(doctors_number) - doctors_needed
        kb.assertz("medici(" + minOsp['X'] + ", " + str(doc_number) + ")")

        # aggiornamento infermieri
        kb.retract("infermieri(" + minOsp['X'] + ", " + str(nurses_number) + ")")
        nurses_number = int(nurses_number) - nurses_needed
        kb.assertz("infermieri(" + minOsp['X'] + ", " + str(nurses_number) + ")")

        # aggiornamento soccorritori
        kb.retract("soccorritori(" + minOsp['X'] + ", " + str(rescuers_number) + ")")
        rescuers_number = int(rescuers_number) - rescuers_needed
        kb.assertz("soccorritori(" + minOsp['X'] + ", " + str(rescuers_number) + ")")

        # aggiornamento ambulanze A
        kb.retract("ambulanza_A(" + minOsp['X'] + ", " + str(ambulance_A_number) + ")")
        ambulance_A_number = int(ambulance_A_number) - ambulance_A_needed
        kb.assertz("ambulanza_A(" + minOsp['X'] + ", " + str(ambulance_A_number) + ")")

        # aggiornamento ambulanze B
        kb.retract("ambulanza_B(" + minOsp['X'] + ", " + str(ambulance_B_number) + ")")
        ambulance_B_number = int(ambulance_B_number) - ambulance_B_needed
        kb.assertz("ambulanza_B(" + minOsp['X'] + ", " + str(ambulance_B_number) + ")")

        # aggiornamento ambulanze C
        kb.retract("ambulanza_C(" + minOsp['X'] + ", " + str(ambulance_C_number) + ")")
        ambulance_C_number = int(ambulance_C_number) - ambulance_C_needed
        kb.assertz("ambulanza_C(" + minOsp['X'] + ", " + str(ambulance_C_number) + ")")

        # aggiornamento ambulanze SSP
        kb.retract("ambulanza_SSP(" + minOsp['X'] + ", " + str(ambulance_SSP_number) + ")")
        ambulance_SSP_number = int(ambulance_SSP_number) - ambulance_SSP_needed
        kb.assertz("ambulanza_SSP(" + minOsp['X'] + ", " + str(ambulance_SSP_number) + ")")

    #A termine della chiamata della funzione, si pulisce sia la kb (solo i fatti riguardanti il tempo) e sia la lista

    myList.clear()
    kb.retract("tempo(ospedale_1, " + str(time1) + ")")
    kb.retract("tempo(ospedale_2, " + str(time2) + ")")
    kb.retract("tempo(ospedale_3, " + str(time3) + ")")
    kb.retract("tempo(ospedale_4, " + str(time4) + ")")
    kb.retract("tempo(ospedale_5, " + str(time5) + ")")

    return one_call


# hospital_menu definisce un menu dal quale l'utente può visualizzare le informazioni degli ospedali
def hospital_menu():

    choice = "0"
    while choice != "6":
        Prints.print_hospital_menu()
        query_info_hospital = "medici(X,M), infermieri(X,I), soccorritori(X,S), ambulanza_A(X,A), ambulanza_B(X,B), ambulanza_C(X,C), ambulanza_SSP(X,SSP), gestione(X,R,P)"
        list_resources = list(kb.query(query_info_hospital))

        choice = input(">>_")
        if choice == "1":
            for item in list_resources:
                if item['X'] == "ospedale_1":
                    print()
                    print("+-------------------------------+")
                    print("|           ospedale 1          |")
                    print("+-------------------------------+")
                    print("|  Personale disponibile:       |")
                    print("|    medici: " + str(item['M']) + "                  |")
                    print("|    infermieri: " + str(item['I']) + "              |")
                    print("|    soccorritori: " + str(item['S']) + "            |")
                    print("|                               |")
                    print("|  Ambulanze disponibili:       |")
                    print("|    tipo A: " + str(item['A']) + "                  |")
                    print("|    tipo B: " + str(item['B']) + "                  |")
                    print("|    tipo C: " + str(item['C']) + "                  |")
                    print("|    tipo SSP: " + str(item['SSP']) + "                |")
                    print("|                               |")
                    print("|  Reparti presenti:            |")
                    print("|    Rianimazione               |")
                    print("|    Ortopedia                  |")
                    print("|    Cardiologia                |")
                    print("|    Pneumologia                |")
                    print("|    Neurologia                 |")
                    print("|    Medicina                   |")
                    print("+-------------------------------+")
                    break;

        elif choice == "2":
            for item in list_resources:
                if item['X'] == "ospedale_2":
                    print()
                    print("+-------------------------------+")
                    print("|           ospedale 2          |")
                    print("+-------------------------------+")
                    print("|  Personale disponibile:       |")
                    print("|    medici: " + str(item['M']) + "                  |")
                    print("|    infermieri: " + str(item['I']) + "              |")
                    print("|    soccorritori: " + str(item['S']) + "            |")
                    print("|                               |")
                    print("|  Ambulanze disponibili:       |")
                    print("|    tipo A: " + str(item['A']) + "                  |")
                    print("|    tipo B: " + str(item['B']) + "                  |")
                    print("|    tipo C: " + str(item['C']) + "                  |")
                    print("|    tipo SSP: " + str(item['SSP']) + "                |")
                    print("|                               |")
                    print("|  Reparti presenti:            |")
                    print("|    Rianimazione               |")
                    print("|    Psichiatria                |")
                    print("|    Cardiologia                |")
                    print("|    Pneumologia                |")
                    print("|    Neurologia                 |")
                    print("|    Medicina                   |")
                    print("|    Oncologia                  |")
                    print("+-------------------------------+")
                    break;

        elif choice == "3":
            for item in list_resources:
                if item['X'] == "ospedale_3":
                    print()
                    print("+-------------------------------+")
                    print("|           ospedale 3          |")
                    print("+-------------------------------+")
                    print("|  Personale disponibile:       |")
                    print("|    medici: " + str(item['M']) + "                  |")
                    print("|    infermieri: " + str(item['I']) + "              |")
                    print("|    soccorritori: " + str(item['S']) + "            |")
                    print("|                               |")
                    print("|  Ambulanze disponibili:       |")
                    print("|    tipo A: " + str(item['A']) + "                  |")
                    print("|    tipo B: " + str(item['B']) + "                  |")
                    print("|    tipo C: " + str(item['C']) + "                  |")
                    print("|    tipo SSP: " + str(item['SSP']) + "                |")
                    print("|                               |")
                    print("|  Reparti presenti:            |")
                    print("|    Rianimazione               |")
                    print("|    Cardiologia                |")
                    print("|    Medicina                   |")
                    print("+-------------------------------+")
                    break;
        elif choice == "4":
            for item in list_resources:
                if item['X'] == "ospedale_4":
                    print()
                    print("+-------------------------------+")
                    print("|           ospedale 4          |")
                    print("+-------------------------------+")
                    print("|  Personale disponibile:       |")
                    print("|    medici: " + str(item['M']) + "                  |")
                    print("|    infermieri: " + str(item['I']) + "              |")
                    print("|    soccorritori: " + str(item['S']) + "            |")
                    print("|                               |")
                    print("|  Ambulanze disponibili:       |")
                    print("|    tipo A: " + str(item['A']) + "                  |")
                    print("|    tipo B: " + str(item['B']) + "                  |")
                    print("|    tipo C: " + str(item['C']) + "                  |")
                    print("|    tipo SSP: " + str(item['SSP']) + "                |")
                    print("|                               |")
                    print("|  Reparti presenti:            |")
                    print("|    Psichiatria                |")
                    print("|    Neurologia                 |")
                    print("|    Medicina                   |")
                    print("+-------------------------------+")
                    break;

        elif choice == "5":
            for item in list_resources:
                if item['X'] == "ospedale_5":
                    print()
                    print("+-------------------------------+")
                    print("|           ospedale 5          |")
                    print("+-------------------------------+")
                    print("|  Personale disponibile:       |")
                    print("|    medici: " + str(item['M']) + "                  |")
                    print("|    infermieri: " + str(item['I']) + "              |")
                    print("|    soccorritori: " + str(item['S']) + "            |")
                    print("|                               |")
                    print("|  Ambulanze disponibili:       |")
                    print("|    tipo A: " + str(item['A']) + "                  |")
                    print("|    tipo B: " + str(item['B']) + "                  |")
                    print("|    tipo C: " + str(item['C']) + "                  |")
                    print("|    tipo SSP: " + str(item['SSP']) + "                |")
                    print("|                               |")
                    print("|  Reparti presenti:            |")
                    print("|    Rianimazione               |")
                    print("|    Cardiologia                |")
                    print("|    Ortopedia                  |")
                    print("|    Pneumologia                |")
                    print("|    Neurologia                 |")
                    print("|    Medicina                   |")
                    print("|    Gastroenterologia          |")
                    print("+-------------------------------+")
                    break;

        elif choice == "6":
            print("Ritorno al menu' principale...")

        else:
            print("Input non valido.")
            print()


# upgrade_calls_menu implement un menu dal quale l'utente può visualizzare il registro delle chiamate,
# e ripristinare le risorse utilizzate
def upgrade_calls_menu(one_call):
    choice = "0"
    while choice != "3":
        Prints.print_upgrade_calls_menu()
        choice = input(">>_")
        if choice == "1":
            if one_call == True:
                queryCalls = "chiamata(A,B,C,D,E)"
                calls_list = list(kb.query(queryCalls))
                if len(calls_list) != 0:
                    print("+--------------+----------+--------------------+------------+---------------+")
                    print("| ID chiamata  |  codice  |  nodo di partenza  |  ospedale  |     stato     |")
                    print("+--------------+----------+--------------------+------------+---------------+")
                    t = "|"
                    for item in calls_list:
                        if item['E'] == 0:
                            stato = "IN CORSO"
                        else:
                            stato = "COMPLETATA"
                        print(f"{t}{str(item['A']): ^14}{t}{Utils.switch_code2(str(item['B'])): ^10}{t}{Utils.switch_number_to_letter(item['C']): ^20}{t}{str(item['D']): ^12}{t}{stato: ^15}{t}")
                    print("+--------------+----------+--------------------+------------+---------------+")
                    print()
                else:
                    print("Il registro delle chiamate e' vuoto.")
            else:
                print("Il registro delle chiamate e' vuoto.")
        elif choice == "2":
            print()

            if one_call == True:

                print("Indica l'id della chiamata che vuoi segnare come \"COMPLETATA\" (premi 0 per annullare): ")
                id = input(">>_")
                if id != "0":
                    queryCalls = "chiamata(A,B,C,D,E), A = " + str(id) + ", E = " + str(0)
                    calls_list = list(kb.query(queryCalls))
                    if len(calls_list) != 0:
                        for item in calls_list:
                            if item['A'] == int(id):
                                kb.retract("chiamata(" + str(item['A']) + ", " + str(item['B']) + ", " + str(item['C']) + ", " + str(item['D']) + ", " + str(item['E']) + ")")
                                stato = 1
                                kb.assertz("chiamata(" + str(item['A']) + ", " + str(item['B']) + ", " + str(item['C']) + ", " + str(item['D']) + ", " + str(stato) + ")")

                                query_doctors = "medici(X,Y)"
                                list_doctors = list(kb.query(query_doctors))
                                for item in list_doctors:
                                    if item['X'] == item['X']:
                                        doctors_number = item['Y']

                                query_nurses = "infermieri(X,Y)"
                                list_nurses = list(kb.query(query_nurses))
                                for item in list_nurses:
                                    if item['X'] == item['X']:
                                        nurses_number = item['Y']

                                query_rescuers = "soccorritori(X,Y)"
                                list_rescuers = list(kb.query(query_rescuers))
                                for item in list_rescuers:
                                    if item['X'] == item['X']:
                                        rescuers_number = item['Y']

                                query_ambulance_A = "ambulanza_A(X,Y)"
                                list_ambulance_A = list(kb.query(query_ambulance_A))
                                for item in list_ambulance_A:
                                    if item['X'] == item['X']:
                                        ambulance_A_number = item['Y']

                                query_ambulance_B = "ambulanza_B(X,Y)"
                                list_ambulance_B = list(kb.query(query_ambulance_B))
                                for item in list_ambulance_B:
                                    if item['X'] == item['X']:
                                        ambulance_B_number = item['Y']

                                query_ambulance_C = "ambulanza_C(X,Y)"
                                list_ambulance_C = list(kb.query(query_ambulance_C))
                                for item in list_ambulance_C:
                                    if item['X'] == item['X']:
                                        ambulance_C_number = item['Y']

                                query_ambulance_SSP = "ambulanza_SSP(X,Y)"
                                list_ambulance_SSP = list(kb.query(query_ambulance_SSP))
                                for item in list_ambulance_SSP:
                                    if item['X'] == item['X']:
                                        ambulance_SSP_number = item['Y']

                                # Per ogni tipologia di codice, si inizializzano le variabili che verranno usate per modificare il numero
                                # delle risorse disponibili.

                                if str(code) == "[3]":  # se codice rosso

                                    doctors_needed = 1
                                    nurses_needed = 2
                                    rescuers_needed = 1
                                    ambulance_A_needed = 0
                                    ambulance_B_needed = 0
                                    ambulance_C_needed = 1
                                    ambulance_SSP_needed = 0

                                if str(code) == "[2]":  # se codice giallo

                                    doctors_needed = 1
                                    nurses_needed = 1
                                    rescuers_needed = 1
                                    ambulance_A_needed = 0
                                    ambulance_B_needed = 1
                                    ambulance_C_needed = 0
                                    ambulance_SSP_needed = 0

                                if str(code) == "[1]":  # se codice verde

                                    doctors_needed = 0
                                    nurses_needed = 1
                                    rescuers_needed = 1
                                    ambulance_A_needed = 1
                                    ambulance_B_needed = 0
                                    ambulance_C_needed = 0
                                    ambulance_SSP_needed = 0

                                if str(code) == "[0]":  # se codice bianco

                                    doctors_needed = 0
                                    nurses_needed = 0
                                    rescuers_needed = 1
                                    ambulance_A_needed = 0
                                    ambulance_B_needed = 0
                                    ambulance_C_needed = 0
                                    ambulance_SSP_needed = 1

                                # Aggiornamento della base di conoscenza

                                # aggiornamento medici
                                kb.retract("medici(" + item['X'] + ", " + str(doctors_number) + ")")
                                doc_number = int(doctors_number) + doctors_needed
                                kb.assertz("medici(" + item['X'] + ", " + str(doc_number) + ")")

                                # aggiornamento infermieri
                                kb.retract("infermieri(" + item['X'] + ", " + str(nurses_number) + ")")
                                nurses_number = int(nurses_number) + nurses_needed
                                kb.assertz("infermieri(" + item['X'] + ", " + str(nurses_number) + ")")

                                # aggiornamento soccorritori
                                kb.retract("soccorritori(" + item['X'] + ", " + str(rescuers_number) + ")")
                                rescuers_number = int(rescuers_number) + rescuers_needed
                                kb.assertz("soccorritori(" + item['X'] + ", " + str(rescuers_number) + ")")

                                # aggiornamento ambulanze A
                                kb.retract("ambulanza_A(" + item['X'] + ", " + str(ambulance_A_number) + ")")
                                ambulance_A_number = int(ambulance_A_number) + ambulance_A_needed
                                kb.assertz("ambulanza_A(" + item['X'] + ", " + str(ambulance_A_number) + ")")

                                # aggiornamento ambulanze B
                                kb.retract("ambulanza_B(" + item['X'] + ", " + str(ambulance_B_number) + ")")
                                ambulance_B_number = int(ambulance_B_number) + ambulance_B_needed
                                kb.assertz("ambulanza_B(" + item['X'] + ", " + str(ambulance_B_number) + ")")

                                # aggiornamento ambulanze C
                                kb.retract("ambulanza_C(" + item['X'] + ", " + str(ambulance_C_number) + ")")
                                ambulance_C_number = int(ambulance_C_number) + ambulance_C_needed
                                kb.assertz("ambulanza_C(" + item['X'] + ", " + str(ambulance_C_number) + ")")

                                # aggiornamento ambulanze SSP
                                kb.retract("ambulanza_SSP(" + item['X'] + ", " + str(ambulance_SSP_number) + ")")
                                ambulance_SSP_number = int(ambulance_SSP_number) + ambulance_SSP_needed
                                kb.assertz("ambulanza_SSP(" + item['X'] + ", " + str(ambulance_SSP_number) + ")")

                                print()
                                print("Le risorse dell'" + item['X'] + " sono state ripristinate.")
                    else:
                        print()
                        print("La chiamata indicata non esiste o e' stata già indicata come \"COMPLETATA\".")
                        print()
            else:
                print("Non è stata effettuata nessuna chiamata.")
                print()

        elif choice == "3":
            print("Ritorno al menu' principale...")
        else:
            print("Input non valido.")
            print()


# initializeGraph inizializza il grafo su cui poggia il progetto
def inizializeGraph():
    adjac_lis = {
        'X': [('Y', 6), ('W', 5),('A', 11)],
        'W': [('X', 5), ('O1', 2), ('V', 4)],
        'O1': [('W', 2), ('Y', 2)],
        'Y': [('X', 6), ('O1', 2), ('Z', 6)],
        'V': [('W', 4), ('Z', 7)],
        'Z': [('Y', 6), ('V', 7),('F',11)],
        'A': [('B',7), ('D',6),('X',11)],
        'B': [('C', 7), ('A',7), ('O2',4)],
        'D': [('A',6), ('O2',4), ('C',5), ('F',5)],
        'C': [('B',7),('D',5),('O2',3), ('E', 4), ('I',10)],
        'O2': [('B',4), ('D',4), ('C',3)],
        'F' : [('D',5), ('Z', 11), ('E',6), ('G',6),('O3',5)],
        'E' : [('F', 6), ('C',4), ('H',7), ('O3',4)],
        'G' : [('F',6), ('O3',3), ('H',5)],
        'H' : [('G', 5), ('O3',2), ('E',7), ('S',12)],
        'I' : [('C',10), ('O',3), ('J', 7), ('L',9)],
        'O' : [('I',3), ('J', 4), ('R', 8)],
        'J' : [('I',7), ('O',4)],
        'L' : [('I',9), ('K', 4), ('N', 6), ('O4',2)],
        'K': [('L', 4), ('O4', 5), ('M', 9)],
        'N': [('L',6), ('O4',2), ('M',5), ('P',10)],
        'M': [('K',9), ('N',5), ('O4',3)],
        'P': [('R',5), ('Q',6), ('N',10)],
        'R': [('O',8), ('P',5), ('S',8), ('O5',7)],
        'S': [('R',8), ('H',12), ('O5',6), ('U',4)],
        'U': [('S',4), ('T',8)],
        'T': [('U',8), ('O5',4), ('Q',5)],
        'Q': [('T',5), ('O5',5), ('P',6)],
        'O3': [('F',5), ('G',3), ('E',4), ('H',2)],
        'O4': [('K',5), ('L',2), ('N',2), ('M',3)],
        'O5': [('R',7), ('S',6), ('Q',5), ('T',4)],
    }
    return adjac_lis


if __name__ == '__main__':

    graph = Graph(inizializeGraph())
    kb = knowledge_base.createKB()

    Prints.print_introduction()

    choice = "0"

    Prints.printmenu()
    id_call = 1

    one_call = False

    while choice != "8":
        choice = str(choice)
        choice = input(">>_")
        if choice == "1":
            # Genera una chiamata manuale
            code, pathology, randomNode = input_call(graph)
            one_call = process_call(code, pathology, randomNode, graph, id_call, one_call)
            id_call = id_call + 1
            print()
            Prints.printmenu()
        elif choice == "2":
            # Genera una chiamata automatica con valori casuali
            code, pathology, randomNode = random_call(graph)
            one_call = process_call(code, pathology, randomNode, graph, id_call, one_call)
            id_call = id_call + 1
            print()
            Prints.printmenu()
        elif choice == "3":
            # Visualizza stato ospedali
            hospital_menu()
            print()
            Prints.printmenu()
        elif choice == "4":
            # aggiorna stato chiamate
            upgrade_calls_menu(one_call)
            print()
            Prints.printmenu()
        elif choice == "5":
            # visualizza grafo
            graph.printGraph()
            print()
            Prints.printmenu()
        elif choice == "6":
            # Aiuto
            Prints.print_help()
            Prints.printmenu()
        elif choice == "7":
            # Esci
            end = False
            while end == False:
                print()
                print("Sei sicuro di voler chiudere il programma? (si / no)")
                s = input(">>_")
                if s == "si" or s == "SI" or s == "sì" or s == "Sì" or s == "Si":
                    print()
                    print("Programma terminato")
                    choice = "8"
                    end = True
                elif s == "no" or s == "No" or s == "NO":
                    print()
                    Prints.printmenu()
                    choice = "0"
                    end = True
                else:
                    print("Input non valido")
                    end = False
        else:
            print("Input non valido, utilizza il range di valori [1,7] per interagire con il menu principale.")
            print()
            Prints.printmenu()