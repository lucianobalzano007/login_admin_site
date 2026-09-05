# 🚗 Med Patente

Gestionale web per la gestione di uno studio medico dedicato al rinnovo delle patenti di guida italiane.

L'applicazione è sviluppata con Python e Flask, utilizza MongoDB come database e viene eseguita tramite Docker Compose.
## 📋 Indice

    Descrizione
    Tecnologie
    Rouli Utente
    Autore

## 📝 Descrizione

Med Patente è un'applicazione web pensata per supportare la gestione amministrativa di uno studio medico che effettua visite per il rinnovo delle patenti.

L'applicazione fornisce una base per la gestione degli utenti dello studio e prevede differenti livelli di accesso in base al ruolo dell'utente.

Il backend è realizzato utilizzando Flask, mentre i dati vengono persistiti su MongoDB. L'intero sistema può essere avviato tramite container Docker, semplificando la configurazione dell'ambiente di esecuzione.

## 🛠️ Tecnologie

Il progetto utilizza principalmente:
| Tecnologia　　　　| Utilizzo                     |
| -------------------| ------------------------------|
| 🐍 Python 3.13　　| Linguaggio di programmazione |
| 🌶️ Flask　　　　　| Framework web                |
| 🍃 MongoDB　　　　| Database NoSQL               |
| 🍃 PyMongo　　　　| Connessione a MongoDB        |
| 🐳 Docker　　　　 | Containerizzazione           |
| 🐳 Docker Compose | Orchestrazione dei container |
| HTML/CSS　　　　　| Interfaccia web              |
| Jinja2　　　　　　| Template engine di Flask     |

Le dipendenze Python attualmente dichiarate sono Flask e pymongo. 

## 👥 Ruoli utente
| Ruolo      | Descrizione                                              | Stato         |
| ------------| ----------------------------------------------------------| ---------------|
| Admin      | Gestione amministrativa dell'applicazione e degli utenti | ✅ Disponibile |
| Medico     | Funzionalità dedicate al medico                          | 🚧 In sviluppo |
| Segreteria | Funzionalità dedicate alla segreteria                    | 🚧 In sviluppo |

## 👤 Autore

Luciano Balzano

[Repository](https://github.com/lucianobalzano007/med_patente)