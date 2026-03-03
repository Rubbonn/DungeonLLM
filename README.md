# DungeonLLM 🎲🤖

Un videogioco dove un Large Language Model funge da **Game Master**, creando e gestendo campagne di gioco in stile RPG da tavolo.

---

## 📋 Indice

- [Descrizione](#-descrizione)
- [Stato del Progetto](#-stato-del-progetto)
- [Funzionalità](#-funzionalità)
- [Stack Tecnologico](#-stack-tecnologico)
- [Struttura del Progetto](#-struttura-del-progetto)
- [Installazione](#-installazione)
- [Utilizzo](#-utilizzo)
- [Roadmap di Sviluppo](#-roadmap-di-sviluppo)
- [Sistema di Regole](#-sistema-di-regole)
- [Architettura Dati](#-architettura-dati)
- [Contribuire](#-contribuire)
- [Licenza](#-licenza)

---

## 🎮 Descrizione

**DungeonLLM** è un videogioco sperimentale che sfrutta la potenza dei Large Language Models per creare un'esperienza di gioco di ruolo dinamica e personalizzata. A differenza dei giochi tradizionali con narrative predefinite, DungeonLLM utilizza un LLM come Game Master intelligente che:

- Gestisce campagne create dal giocatore
- Crea e gestisce personaggi non giocanti (NPC) con personalità distinte
- Reagisce in modo dinamico alle scelte dei giocatori
- Applica le regole del gioco in modo contestuale

## 🚧 Stato del Progetto

⚠️ **Progetto in fase embrionale** - Molte componenti sono ancora in definizione e sviluppo attivo.

Il progetto è attualmente nelle fasi iniziali di sviluppo. Alcune tecnologie e architetture non sono ancora finalizzate e sono soggette a cambiamenti.

## ✨ Funzionalità

### Funzionalità Pianificate

- **🎭 Sistema di Campagne**
  - Creazione di campagne da parte del giocatore
  - Definizione di incipit narrativi
  - Selezione e aggiunta di oggetti, mostri, personaggi ed effetti personalizzati
  - Gestione procedurale di NPC con background e motivazioni
  - Sistema di loot dinamico

- **🎨 Generazione di Asset Grafici (Stable Diffusion)**
  - Sfondi e ambientazioni a tema
  - Ritratti di personaggi
  - Tabelle di gioco e mappe visuali

- **🔊 Sistema Audio Avanzato (TTS)**
  - Voce narrante per le descrizioni
  - Voice acting per i personaggi NPC
  - Effetti sonori contestuali

- **⚔️ Meccaniche di Gioco**
  - Sistema di combattimento a turni
  - Gestione inventario e utilizzo oggetti
  - Sistema di effetti e status
  - Creazione e personalizzazione personaggio
  - Lancio dadi e meccaniche probabilistiche
  - Sistema di progressione ed esperienza

- **💬 Chatbot di Consultazione Regole**
  - Consultazione rapida di manuale, creature, oggetti, effetti e contenuti di gioco
  - Risposte contestuali basate sulla campagna e sessione attuale
  - Supporto a domande su funzionamento del gioco e regole di DnD in generale
  - Recupero informazioni tramite ricerca semantica sulle regole (RAG)

## 🛠 Stack Tecnologico

### Backend & AI

| Componente | Tecnologia | Stato |
|------------|------------|-------|
| **Linguaggio** | Python 3.13+ | ✅ Definito |
| **Framework AI** | Langchain, Langgraph | ✅ Definito |
| **LLM Runtime** | Transformers (Huggingface) | 🔄 In valutazione |
| **Hosting LLM** | Locale (Cloud in dev) | 🔄 In valutazione |
| **Text-to-Speech** | Da definire | ❌ Non definito |
| **Image Generation** | Stable Diffusion | ✅ Definito |

### Frontend & Web

| Componente | Tecnologia | Stato |
|------------|------------|-------|
| **Architettura** | Single Page Application | ✅ Definito |
| **Rendering** | Webview | ✅ Definito |
| **Webserver** | Da definire | ❌ Non definito |
| **Frontend Framework** | Da definire | ❌ Non definito |

### Database

| Componente | Tecnologia | Stato |
|------------|------------|-------|
| **Vector DB** | Da definire | ❌ Non definito |
| **Database Principale** | Da definire | ❌ Non definito |

##  Installazione

> ⚠️ **Nota**: Le istruzioni di installazione sono preliminari e verranno aggiornate man mano che il progetto si sviluppa.

### Prerequisiti

- Python 3.13 o superiore
- pip (gestore pacchetti Python)
- Git

### Passaggi

```bash
# Clona il repository
git clone https://github.com/tuousername/DungeonLLM.git
cd DungeonLLM

# Crea un ambiente virtuale
python -m venv venv

# Attiva l'ambiente virtuale
# Su Windows:
venv\Scripts\activate
# Su Linux/Mac:
source venv/bin/activate

# Installa le dipendenze (quando disponibili)
pip install -r requirements.txt
```

## 💻 Utilizzo

> ⚠️ **Nota**: Il progetto è in fase iniziale. Le istruzioni di utilizzo verranno aggiunte quando sarà disponibile un MVP funzionante.

```bash
# Avvio previsto (da implementare)
python src/main.py
```

## 🗺 Roadmap di Sviluppo

Lo sviluppo seguirà un approccio incrementale, partendo da un **Minimum Viable Product (MVP)** e aggiungendo funzionalità progressivamente.

### Fase 1: MVP (Minimum Viable Product) 🎯
- [ ] Setup base del progetto Python
- [ ] Integrazione base con LLM (Langchain/Langgraph)
- [ ] Interfaccia testuale semplice
- [ ] Generazione narrativa base
- [ ] Sistema di dialogo giocatore-GM

### Fase 2: Regole Base ⚔️
- [ ] Parsing del SRD 5.2.1
- [ ] Integrazione database vettoriale per le regole
- [ ] Sistema di lancio dadi
- [ ] Creazione personaggio base
- [ ] Gestione statistiche e attributi

### Fase 2.5: Chatbot Regole & Lore 💬📚
- [ ] Implementazione chatbot di consultazione (manuale, creature, oggetti, effetti)
- [ ] Collegamento al database vettoriale delle regole (RAG)
- [ ] Contesto dinamico della campagna e sessione corrente
- [ ] Q&A su meccaniche interne del gioco
- [ ] Q&A su regole DnD in generale

### Fase 3: Combattimento 🗡️
- [ ] Sistema di iniziativa
- [ ] Turni di combattimento
- [ ] Gestione azioni e abilità
- [ ] Calcolo danni e HP
- [ ] Sistema di morte/svenimento

### Fase 4: Inventario & Oggetti 🎒
- [ ] Sistema di inventario
- [ ] Utilizzo oggetti
- [ ] Equipaggiamento e statistiche
- [ ] Sistema di loot

### Fase 5: Database dei Contenuti 📚
- [ ] Setup database principale
- [ ] Inserimento razze
- [ ] Inserimento mostri
- [ ] Inserimento incantesimi
- [ ] Inserimento oggetti

### Fase 6: Interfaccia Grafica 🖼️
- [ ] Scelta tecnologia frontend
- [ ] Setup webserver
- [ ] Design UI/UX
- [ ] Implementazione SPA
- [ ] Integrazione webview

### Fase 7: Generazione Asset 🎨
- [ ] Integrazione Stable Diffusion
- [ ] Generazione sfondi
- [ ] Generazione personaggi
- [ ] Generazione mappe

### Fase 8: Sistema Audio 🔊
- [ ] Scelta modello TTS
- [ ] Integrazione TTS
- [ ] Voce narrante
- [ ] Voice acting NPC

### Fase 9: Editor e Gestione Campagne 🏰
- [ ] Editor campagne per il giocatore
- [ ] Definizione incipit e narrativa
- [ ] Selezione e personalizzazione di oggetti, mostri, personaggi ed effetti
- [ ] Sistema di salvataggio/caricamento campagne
- [ ] Persistenza stato di gioco
- [ ] NPC con memoria e personalità

## 📖 Sistema di Regole

DungeonLLM implementa le regole del **System Reference Document (SRD) 5.2.1**, una versione open di regole per giochi di ruolo.

### File Presenti
- `IT_SRD_CC_v5.2.1.md` - Versione in Markdown del SRD in italiano
- `SRD_CC_v5.2.1.md` - Versione in Markdown del SRD in inglese

### Integrazione Regole

Le regole verranno integrate nel sistema in due modi complementari:

1. **Database Vettoriale**: 
   - Le regole saranno indicizzate in un vector database
   - L'LLM potrà consultare le regole relevanti al contesto
   - Permetterà ricerche semantiche rapide
   - Database specifico da definire (possibili opzioni: Chroma, Pinecone, Weaviate)

2. **Database Relazionale/NoSQL**:
   - Oggetti strutturati (incantesimi, mostri, razze, oggetti)
   - Query rapide per statistiche e proprietà
   - Relazioni tra entità
   - Database specifico da definire

## 🗄 Architettura Dati

### Database Vettoriale (Da definire)
**Scopo**: Archiviazione e recupero semantico delle regole

**Candidati**:
- Chroma
- Pinecone
- Weaviate
- Qdrant

### Database Principale (Da definire)
**Scopo**: Archiviazione strutturata di entità di gioco

**Tipologie di Dati**:
- Razze e sottotipologie
- Classi e sottoclassi
- Incantesimi e abilità
- Mostri e creature
- Oggetti e equipaggiamento
- Campagne e sessioni di gioco
- Personaggi giocatori e NPC

**Candidati**:
- PostgreSQL (relazionale)
- MongoDB (NoSQL)
- SQLite (sviluppo/testing)

## 🤝 Contribuire

Il progetto è attualmente in fase iniziale. Le linee guida per contribuire verranno definite nelle prossime fasi di sviluppo.

## 📄 Licenza

Da definire

---

**Nota**: Questo è un progetto sperimentale e in continua evoluzione. Documentazione e funzionalità verranno aggiornate regolarmente durante lo sviluppo.

## Crediti
Quest'opera include materiale tratto dal System Reference Document 5.2.1 ("SRD 5.2.1") di Wizards of the Coast LLC, disponibile all'indirizzo <https://www.dndbeyond.com/srd>. Il SRD 5.2.1 è concesso in licenza ai sensi della licenza di attribuzione 4.0 Internazionale di Creative Commons, disponibile all'indirizzo <https://creativecommons.org/licenses/by/4.0/legalcode>.