# Generatore di Dati CDA di Pazienti Fittizi

## Panoramica
Questo repository è progettato per generare e salvare dati fittizi del Clinical Document Architecture (CDA) di pazienti, utilizzando l'API GPT-4 di OpenAI. Include funzionalità per elaborare e formattare i dati in XML e salvarli con nomi di file unici in una directory specificata.

## Funzionalità
- **Generazione dei Dati**: Utilizza l'API GPT-4 di OpenAI per creare dati CDA di pazienti realistici ma fittizi.
- **Elaborazione XML**: Elabora il formato XML, incluso rimuovere specifiche linee dal contenuto XML.
- **Gestione dei File**: Genera file con nomi unici usando numeri casuali e li salva in una cartella designata.

## Installazione
Per configurare questo progetto, seguire questi passaggi:

1. **Clonare il Repository**
   ```bash
   git clone [https://github.com/spuliz/dati_sanitari_sintetici.git]
 ```  ```

2. **Creare un Ambiente Virtuale**

   ```bash
   python -m venv venv
   source venv/bin/activate
   ``` ```

3. **Installare le dipendenze** 
   ```bash
   pip install -r requirements.txt
 ```  ```
## Utilizzo
Per generare e salvare dati CDA fittizi di pazienti:

1. **Impostare la Chiave API di OpenAI**: Assicurarsi di aver impostato la chiave API di OpenAI nelle variabili d'ambiente o all'interno dello script.

2. **Eseguire lo Script**: Eseguire lo script principale per generare dati e salvarli nel formato specificato.

   ```bash
   python script.py
 ``` ```
3. **Struttura delle cartelle**
```bash
├── dati/ # Cartella dove i file XML generati vengono salvati
├── script.py # Script principale per la generazione e l'elaborazione dei dati
└── README.md # Documentazione di questo progetto
 ```
## Contributi
I contributi a questo progetto sono benvenuti. Si prega di seguire questi passi:

1. Forkare il repository.
2. Creare un nuovo ramo per la propria funzionalità (`git checkout -b feature/FantasticaFunzionalità`).
3. Commit delle modifiche (`git commit -m 'Aggiungere qualche FantasticaFunzionalità'`).
4. Push sul ramo (`git push origin feature/FantasticaFunzionalità`).
5. Aprire una pull request.

## Licenza
Distribuito sotto la Licenza MIT. Vedere `LICENSE` per maggiori informazioni.

## Contatto
Saverio Pulizzi - [saverio.pulizzi91@gmail.com]

Link del Progetto: [Dati Sanitari Sintetici](https://github.com/spuliz/dati_sanitari_sintetici.git)
