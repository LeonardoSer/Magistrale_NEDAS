# AAI project 2021 

|Nome|Matricola|Mail|
|-|-|-|
|Leonardo Serilli| 274426| leonardo.serilli@student.univaq.it|
|Gabriele Colapelle| 274560 | gabriele.colapelle@student.univaq.it |
|Alessandro D'Orazio| | alessandro.dorazio@student.univaq.it |

# Introduzione

Il prblema che questo progetto risolve è quello di implementare, nel linguaggio **DALI**, un **Multy Agent System** in grado di automizzare i processi di deposito e ritiro di merci da un magazzino, tramite la presenza di due tipi di agente; **un agente di tipo Magazzino**, in grado sia di contenere informazioni riguradanti le posizioni e numero delle merci presenti nel magazzino che di gestire le richieste esterne di deposito e ritiro inoltrandole agli **agenti di tipo Muletto**, incaricati della risoluzione di tali task.

## Agente Magazzino

Un magazzino è diviso in **settori** e ogni settore può contenere vari tipi di **prodotti**. Per ogni prodotto l'agente conosce il **numero attuale di unità** e il **settore in cui si trovano**.

Nella knowledge base sono definiti **settori** e **prodotti**:

```prolog
settore(a1).
settore(a2).
settore(b1).
settore(b2).

prodotto(tastiera, 50, a1). 
prodotto(tv, 30, a1).
prodotto(telefono, 50, a2).
prodotto(ventilatore, 70, a2).
prodotto(mouse, 40, b1).
prodotto(computer, 15, b1).
prodotto(orologio, 100, b2).
prodotto(monitor, 20, b2).
```

In seguito sono desceritti i metodi per gestire gli eventi generati dagli agenti muletto, e mantenere un Knowledger base aggiornata.

### (0) Controllo diponibiltà prodotti
L'agente esegue un semplice check della quantità attuale del prodotto

```prolog
disponibilita_prodottoE(Prodotto) :>
    prodotto(Prodotto, Qta, Settore),
    write(Prodotto),
    write(Qta),
    write(Settore).
```

### (1) Richiesta deposito prodotti
1. Richiesta di deposito per un** prodotto gia presente**: l'evento **richiesta_deposito_prodottoE(Agente, Prodotto)** è generato dall'agente **muletto** in quale è intenzionato il settore in cui si trova in prodotto da aggiungere (informazione posseduto nella KB dell'agente **magazzino** ). infine al verificarsi di **prodotto_depositatoE(Prodotto, Qta, Settore)** la KB viene modificata con la nuova quantità per il prodotto.
 
```prolog
richiesta_deposito_prodottoE(Agente, Prodotto) :>
    prodotto(Prodotto, QtaAttuale, Settore),
    format('Richiesta di deposito prodotto da agente ~w', Agente), nl,
    messageA(Agente, send_message(risposta_deposito_prodotto(Prodotto, Settore), Me)).

prodotto_depositatoE(Prodotto, Qta, Settore) :> 
    prodotto(Prodotto, QtaAttuale, Settore),
    NuovaQta is Qta + QtaAttuale,
    retract(prodotto(Prodotto, QtaAttuale, Settore)),
    assertz(prodotto(Prodotto, NuovaQta, Settore)),
    write('Nuova quantita: '),
    write(NuovaQta).
```

3.   Richiesta di deposito per un **prodotto NON presente**: a differenza del metodo precedente, una volta depositato il nuovo prodotto, l'agente creerà una nuova entry della KB per il nuovo prodotto.

```prolog
richiesta_deposito_prodottoE(Agente, Prodotto) :>
    not(prodotto(Prodotto,_,_)),
    format('Richiesta di deposito di un nuovo prodotto da agente ~w', Agente), nl,
    messageA(Agente, send_message(risposta_deposito_prodotto(Prodotto, b1), Me)).
	
prodotto_depositatoE(Prodotto, Qta, Settore) :>
    not(prodotto(Prodotto, _, Settore)),
    assertz(prodotto(Prodotto, Qta, Settore)),
    write('Prodotto aggiunto al magazzino').
	
```

### (2) Richiesta prelievo prodotti
Ci sono 3 scenari possibili: 
- che il prodotto sia disponibile nella quantità richiesta;
- che il prodotto sia disponibile ma la quantità richiesta supera la disponibilità
- che il prodotto no sia disponibile
  
1. Richiesta di prelievo per un prodotto **disponibile nella quantità richiesta**: l 'evento **richiesta_prelievo_prodottoE(Agente, Prodotto, Qta)** si verfiica quanto un agente **muletto** è intenzionato a prelevare un prodotto, vinene effettuato un controllo sulla disponibilità e dopodiche, tramite **send_msg** viene autorizzato al prelievo. Una volta notificato il deposito dall'agente **muletto**, viene aggiornata la quantità tramite **prodotto_prelevatoE**

```Prolog
richiesta_prelievo_prodottoE(Agente, Prodotto, Qta) :>
    prodotto(Prodotto, QtaAttuale, Settore),
    Qta =< QtaAttuale,
    format('Richiesta di prelievo di un prodotto da agente ~w', Agente),
    sleep(2),
    messageA(Agente, send_message(risposta_prelievo_prodotto(Prodotto, Settore), Me))
	

prodotto_prelevatoE(Prodotto, Qta) :>
    prodotto(Prodotto, QtaAttuale, Settore),
    QtaAttuale > Qta,
    NuovaQta is QtaAttuale - Qta,
    retract(prodotto(Prodotto, QtaAttuale, Settore)),
    assertz(prodotto(Prodotto, NuovaQta, Settore)),
    write('Nuova quantita: '),
    write(NuovaQta).
	

prodotto_prelevatoE(Prodotto, Qta) :>
    prodotto(Prodotto, QtaAttuale, Settore),
    Qta == QtaAttuale,
    retract(prodotto(Prodotto, QtaAttuale, Settore)),
    write('Prodotto rimosso').	
```

2. Richiesta di prelievo per un prodotto **NON disponibile nella quantità richiesta**: in questo caso viene notificato all'utente che il prodotto non è disponibile nella quantità richiesta.

```prolog
richiesta_prelievo_prodottoE(Agente, Prodotto, Qta) :>
    prodotto(Prodotto, QtaAttuale, Settore),
    Qta > QtaAttuale,
    write('Richiesta di prelievo di un prodotto che non abbiamo'),
    messageA(Agente, send_message(risposta_deposito_prodotto(Prodotto, null), Me)).
	- 

prodotto_prelevatoE(Prodotto, Qta) :>
    prodotto(Prodotto, QtaAttuale, Settore),
    Qta > QtaAttuale,
    write('Non posso rimuovere una quantita superiore a quella presente').
```

3. Richiesta di prelievo per un prodotto **NON disponibile**: in questo caso viene notificato all'utente che il prodotto non è disponibile.

```prolog
richiesta_prelievo_prodottoE(Agente, Prodotto, Qta) :>
    not(prodotto(Prodotto, _, _)),
    format('Richiesta di prelievo di un prodotto che non abbiamo'),
    messageA(Agente, send_message(risposta_prelievo_prodotto(Prodotto, null), Me)).

prodotto_prelevatoE(Prodotto, Qta) :>
    not(prodotto(Prodotto, _, _)),
    write('Prodotto non trovato').
```

## Agente Muletto
Un agente **muletto** si occupa di processare le richieste di deposito e prelievo generate dagli utenti attivi. 


### (1) Deposito prodotti
- i seguenti sono semplicemente eventi di controllo per verificare che l'agente non sia impegnato in un altra task.

```Prolog
richiesta_deposito_prodottoE(Prodotto, Qta) :>
  deposito(X, Y),
  write('Sono impegnato in un deposito').


richiesta_deposito_prodottoE(Prodotto, Qta) :>
  prelievo(X, Y),
  write('Sono impegnato in un prelievo').
```

- L'agente al verificarsi di **richiesta_deposito_prodottoE(Prodotto, Qta)** , dopo aver controllato di non essere impegnato un un altra attività, richiede al **magazzino** cosi da ottenere l'informazione sul settore in cui depositare il prodotto, poi lo deposita tramite **risposta_deposito_prodottoE(Prodotto, Settore)** , tramite l'azione **depositoA(Prodotto, Qta, Settore)** notifica al **magazzino** il deposito avvenuto e infine torna all'HUB.

```Prolog
richiesta_deposito_prodottoE(Prodotto, Qta) :>
  not(deposito(_,_)),
  not(prelievo(_,_)),
  format('Richiesta deposito ~w', Prodotto), nl,
  assertz(deposito(Prodotto, Qta)),
  messageA(agentMagazzino, send_message(richiesta_deposito_prodotto(Me, Prodotto), Me)).

risposta_deposito_prodottoE(Prodotto, Settore) :> 
  vado_al_settoreA(Settore),
  deposito(Prodotto, Qta),
  depositoA(Prodotto, Qta, Settore),
  torno_all_hubA,
  retractall(deposito(_,_)).

depositoA(Prodotto, Qta, Settore) :- 
  sleep(3),
  messageA(agentMagazzino, send_message(prodotto_depositato(Prodotto, Qta, Settore), Me)).
```
 
### (1) Prelievo prodotti
- I seguenti sono, come prima, eventi di controllo per verificare che l'agente non sia impegnato in un altra task.

```Prolog
richiesta_prelievo_prodottoE(Prodotto, Qta) :>
  deposito(_, _),
  write('Sono impegnato in un deposito').

richiesta_prelievo_prodottoE(Prodotto, Qta) :>
  prelievo(_, _),
  write('Sono impegnato in un prelievo').
  
```

- L'agente al verificarsi di **richiesta_prelievo_prodottoE(Prodotto, QtaRichiesta)** , dopo aver controllato di non essere impegnato un un altra attività, richiede al **magazzino** cosi da ottenere l'informazione sul settore in cui effettuare il prelievo.

```Prolog
richiesta_prelievo_prodottoE(Prodotto, QtaRichiesta) :>
  not(deposito(_,_)),
  not(prelievo(_,_)),
  format('Sto prelevando il prodotto ~w', Prodotto), nl,
  assertz(prelievo(Prodotto, QtaRichiesta)),
  messageA(agentMagazzino, send_message(richiesta_prelievo_prodotto(Me, Prodotto, QtaRichiesta), Me)).
```

- Alla risposta del magazzino **risposta_prelievo_prodottoE(Prodotto, Settore)**, ci sono due possibilità:
	
1. il magazzino risponde con il settore in cui prelevare il prodotto: l'agente allora preleva il prodotto

```prolog
risposta_prelievo_prodottoE(Prodotto, Settore) :>
  write('Entro'),
  X = null,
  Settore \== null,
  prelievo(Prodotto, QtaRichiesta),
  vado_al_settoreA(Settore),
  prelevoA(Prodotto, QtaRichiesta),
  torno_all_hubA.
  
prelevoA(Prodotto, Qta) :-
  format("Prelevo il prodotto ~w", Prodotto),
  sleep(3),
  messageA(agentMagazzino, send_message(prodotto_prelevato(Prodotto, Qta), Me)).

vado_al_settoreA(Settore) :- 
  format("Vado al settore ~w", Settore),
  sleep(3).
```

2. il magazzino risponde con settore **null**, questo significa che la disponibilità non soddisfa la richiesta, quindi non esegue le azioni  ** vado_al_settoreA(Settore)** **prelevoA(Prodotto, QtaRichiesta)**, **torno_all_hubA**

```prolog
risposta_prelievo_prodottoE(Prodotto, Settore) :>
  write('Entro2'),
  X = null,
  Settore == X,
  prodotto(Prodotto, QtaRichiesta),
  write("Il prodotto non puo essere prelevato poiche non ci sono abbastanza unita"),
  torno_all_hubA.
```


### (3) Ritornare all'HUB
Una volta completato il processo di prelievo l'agente torna all'HUB, e smette di essere impegnato in una qualsiasi azione, rimuovendo tutte le formule della sua KB che lo asseriscono:

```prolog
operazione_completataA :- retractall(deposito(_,_)), retractall(prelievo(_,_)).
torno_all_hubA :- sleep(3), operazione_completataA.
```