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

⚠️ **Progetto in Early MVP Development** - Fondazioni tecniche in place, focus su meccaniche di gioco e pipeline GM/Planner/Executor.

Lo sviluppo è in corso seguendo una **roadmap granulare di 6 fasi**. Le fondazioni base sono completate e il lavoro si concentra ora sulle meccaniche di gioco (dadi, prove di abilità, entità di gioco) e sull'integrazione del database. Il focus immediato è su:
1. **Fase 1**: GM conversazionale coerente con memoria di sessione e NPC
2. **Fase 2**: RAG system per consultazione regole D&D 5e via SRD
3. **Fase 3+**: Meccaniche di gioco progressivamente elaborate

### Stato Attuale (ultimi commit)

- Loop conversazionale CLI funzionante (`main.py` + grafo LangGraph)
- Pipeline **Planner → Executor → GM**: il planner analizza l'intento del giocatore, l'executor risolve le meccaniche, il GM narra il risultato
- **Prove di abilità** implementate (`ability_check` action): tiro d20 + modificatore vs difficoltà
- **Sistema dadi** operativo (d4, d6, d8, d10, d12, d20, d100)
- **Personaggio giocatore** (`Player`) con punteggi di abilità e calcolo modificatori
- **Database SQLite** operativo via SQLAlchemy (`data/databases/entities.sqlite`)
- **Parser SRD** che estrae oggetti (Gear, Tools) dall'SRD e li inserisce nel database
- Routing comandi in chat (`/help`, `/save`, `/load`, `/exit`)
- Persistenza stato campagna in JSON (`data/saves/campaign.json`)
- Configurazione provider LLM tramite file `.env`

Vedi [Roadmap di Sviluppo](#-roadmap-di-sviluppo) per dettagli granulari.

## ✨ Funzionalità

### Funzionalità Attualmente Disponibili

- **💬 GM Conversazionale in CLI**
  - Avvio campagna con prompt di sistema + prompt ambientazione
  - Il GM narra ogni turno come agente LangChain con tool chiamate

- **⚙️ Pipeline Planner → Executor → GM**
  - `planner`: analizza il contesto della conversazione e pianifica le azioni meccaniche necessarie
  - `executor`: esegue le azioni pianificate (prove di abilità, tiri di dado) e inietta i risultati come `ToolMessage`
  - `send_message`: il GM narra il risultato in modo contestuale

- **🎲 Sistema Meccaniche di Gioco**
  - Prove di abilità (`ability_check`): tiro d20 + modificatore di caratteristica vs classe difficoltà
  - Lancio dadi: d4, d6, d8, d10, d12, d20, d100
  - Calcolo automatico modificatori di abilità del personaggio

- **🧙 Personaggio Giocatore**
  - Entità `Player` con nome, taglia e punteggi di abilità (Strength, Dexterity, ecc.)
  - Calcolo modificatori D&D 5e standard

- **🗄 Database Entità (SQLite)**
  - Database SQLite inizializzato via SQLAlchemy (`data/databases/entities.sqlite`)
  - Entità `Gear` e `Tool` mappate con ORM

- **📚 Parser SRD**
  - Grafo LangGraph dedicato (`srdparse`) che legge `SRD_CC_v5.2.1.md`
  - Estrae automaticamente gli oggetti (Adventuring Gear) tramite LLM e li inserisce nel database

- **🧭 Routing Comandi in Chat**
  - `/help` mostra i comandi disponibili
  - `/save` salva lo stato corrente della campagna
  - `/load` ricarica una campagna salvata
  - `/exit` termina la sessione

- **💾 Persistenza Campagna (MVP)**
  - Save/Load su file JSON locale in `data/saves/`
  - Serializzazione messaggi con utility LangChain

- **⚙️ Configurazione LLM via `.env`**
  - Provider e modello LLM configurabili tramite variabili d'ambiente (Ollama, NVIDIA, ecc.)

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

- **⚔️ Meccaniche di Gioco** (estensioni future)
  - Sistema di combattimento a turni
  - Gestione inventario e utilizzo oggetti
  - Sistema di effetti e status
  - Creazione e personalizzazione personaggio completa (hp, proficiencies, skills)
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
| **LLM Runtime (target)** | Transformers (Hugging Face) | 🔄 In valutazione |
| **Provider LLM (sviluppo)** | Ollama / NVIDIA via LangChain | ✅ Attivo in dev |
| **Configurazione LLM** | File `.env` (`LLM_MODEL`, `LLM_PROVIDER`) | ✅ Implementato |
| **Text-to-Speech** | Da definire | ❌ Non definito |
| **Image Generation** | Stable Diffusion | ✅ Definito |

### Frontend & Web

| Componente | Tecnologia | Stato |
|------------|------------|-------|
| **Interfaccia attuale** | CLI | ✅ Implementato |
| **Architettura target** | Single Page Application | 🔄 Pianificato |
| **Rendering target** | Webview | 🔄 Pianificato |
| **Webserver** | Da definire | ❌ Non definito |
| **Frontend Framework** | Da definire | ❌ Non definito |

### Database

| Componente | Tecnologia | Stato |
|------------|------------|-------|
| **Database Entità** | SQLite via SQLAlchemy | ✅ Implementato |
| **Vector DB** | Da definire | ❌ Non definito |

##  Installazione

> ⚠️ **Nota**: Le istruzioni di installazione sono preliminari e verranno aggiornate man mano che il progetto si sviluppa.

### Prerequisiti

- Python 3.13 o superiore
- pip (gestore pacchetti Python)
- Git
- Ollama (o altro provider LLM supportato da LangChain)

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

# Installa le dipendenze
pip install -r requirements.txt

# Configura le variabili d'ambiente
cp .env.example .env
# Modifica .env impostando LLM_MODEL, LLM_PROVIDER e le credenziali del provider scelto
```

## 🗂 Struttura del Progetto

```text
DungeonLLM/
|-- main.py
|-- README.md
|-- requirements.txt
|-- SRD_CC_v5.2.1.md
|-- .env.example
|-- app/
|   |-- database.py          # Engine e sessione SQLAlchemy (SQLite)
|   |-- prompts.py           # SYSTEM_PROMPT, PLANNER_PROMPT, CAMPAIGN_PROMPT
|   |-- tools.py             # Tool LangChain (es. get_player_info)
|   |-- entities/
|   |   |-- creatures.py     # Creature, Player
|   |   |-- features.py      # AbilityType, Ability, Size
|   |   \-- items.py         # Item, Gear, Tool (ORM SQLAlchemy)
|   |-- graph/
|   |   |-- gameplay.py      # Grafo LangGraph principale (gameplay)
|   |   \-- srdparse.py      # Grafo LangGraph per parsing SRD
|   |-- nodes/
|   |   |-- commands.py      # Nodi comandi (/save, /load, /help)
|   |   |-- nodes.py         # Nodi principali (planner, executor, send_message, srd_splitter, gear_parser)
|   |   \-- routers.py       # Router comandi/messaggi
|   |-- types/
|   |   |-- actions.py       # BaseAction, AbilityCheckAction
|   |   |-- planning.py      # Plan
|   |   \-- state.py         # GameplayState, SrdParserState
|   \-- utilities/
|       |-- functions.py     # throw_dice e altre utility
|       \-- jsonable.py      # Serializzazione/deserializzazione JSON
\-- data/
    |-- databases/           # Database SQLite (entities.sqlite)
    |-- saves/               # Salvataggi campagna (campaign.json)
    \-- temp/                # File temporanei del parser SRD
```

## 💻 Utilizzo

```bash
# Avvia il gioco da terminale
python main.py
```

> **Nota**: Al primo avvio, `main.py` esegue il parser SRD per popolare il database SQLite con gli oggetti dell'SRD 5.2.1. Assicurarsi di aver configurato il file `.env` prima di eseguire.

Comandi disponibili durante la sessione:

- `/help` - mostra i comandi supportati
- `/save` - salva la campagna corrente in `data/saves/campaign.json`
- `/load` - carica la campagna da `data/saves/campaign.json`
- `/exit` - termina la sessione

## 🗺 Roadmap di Sviluppo

Sviluppo incrementale in 6 fasi con checklist granulari. No stime temporali (development non-daily).

### Milestone Principali

| Milestone | Obiettivo |
|-----------|----------|
| **MVP v1** — Fase 1 | ✅ GM conversazionale coerente, sessione persiste, NPC mantengono memoria |
| **MVP v2** — Fase 3 | ✅ Combattimento narrativo + dadi, inventario base, character sheets, RAG per regole |
| **MVP v3** — Fase 4 | ✅ Multiple campagne, save/load robusti, scalabilità |

---

### Fase 0 — Fondazioni Dati 🏗️

Setup persistenza minimalista per conversazione GM.

- [x] Implementare sistema di save/load conversazione in JSON
- [x] Definire structure minimalista per salvare history conversazionale
- [ ] Creare primo fixture di test per conversation persistence
- [ ] Testare save/load singola sessione conversazionale

### Fase 1 — GM Conversazionale Robusto 🤖
**[CORE MVP]**

GM mantiene coerenza narrativa, memoria di sessione, adattamento dinamico.

**1.1 — Memory & Context Management**
- [ ] Implementare sliding-window context (ultimi N turni + metadata campagna)
- [ ] Aggiungere nodo per memory management nel grafo Langgraph
- [ ] Evitare token explosion con summarization/compression

**1.2 — GM Personality & Consistency**
- [x] Separare prompt in componenti modularizzabili (base instructions / campaign context / session state)
- [x] Implementare composizione dinamica prompt basata su campagna attiva
- [ ] Testare coerenza narrativa e tono GM across multiple turns

**1.3 — Multi-turn Dialogue & NPC Interaction**
- [ ] Supportare scelte NPC nella conversazione
- [ ] Implementare memoria semplice per personalità NPC e relazioni con PG
- [ ] Aggiungere nodo per NPC interaction nel grafo

**1.4 — Session Continuity & Loading**
- [ ] Implementare session resume + recap narrativo
- [x] Persistere conversazione tra multiple run
- [ ] Testare multi-session playthrough (session 1 → save → load → session 2)
- [ ] Verificare NPC recognition across sessions

---

### Fase 2 — RAG System per Regole SRD 📚

GM consulta regole D&D 5e in tempo reale senza context explosion.

**2.1 — Vector DB Setup & SRD Chunking**
- [ ] Selezionare vector store locale (no external services)
- [ ] Implementare chunking logico SRD per chapters
- [ ] Creare script di loading/initialization per embeddings

**2.2 — RAG Node in Langgraph**
- [ ] Implementare nodo per rules consultation nel grafo
- [ ] Query extraction da conversazione
- [ ] Semantic retrieval vs SRD embeddings
- [ ] Context hydration (injetta rule snippets in system prompt)
- [ ] Confidence scoring per query vague

**2.3 — Content-Specific Queries**
- [ ] Specializzare retrieval per entity types (spells, monsters, classes, items)
- [ ] Aggiungere filterable metadata (source, edition, category)

**2.4 — Validation & Accuracy Testing**
- [ ] Creare test set di domande D&D 5e
- [ ] Verificare retrieve accuracy vs expected rules
- [ ] Fine-tune chunking se retrieve sub-optimal

---

### Fase 3 — Character State & Game Rules ⚔️

Logica di gioco minimalista (dadi, stats, combattimento narrativo).

**3.1 — Character Creation & Stats**
- [x] Definire schema dati personaggio (ability scores)
- [ ] Definire schema completo personaggio (proficiencies, hp, skills)
- [ ] Implementare character creation flow conversazionale (GM guida giocatore via chat)
- [ ] Validazione vs D&D 5e rules (via RAG)
- [ ] Implementare save/load personaggio in JSON
- [ ] Testare creazione personaggio end-to-end

**3.2 — Dice Mechanics**
- [x] Implementare dice roller (d4, d6, d8, d10, d12, d20, d100)
- [x] Integrazione in Langgraph (nodo executor per action resolution)
- [x] Proposta roll + esecuzione + narrazione risultato (via planner/executor/GM)
- [ ] Supporto advantage/disadvantage
- [ ] Dice expression parser (es. "2d20 + modifier")

**3.3 — Basic Combat System**
- [ ] Turn-based initiative system
- [ ] Action parsing (attack, dodge, etc)
- [ ] Damage calculation vs HP
- [ ] Condition tracking (stunned, poisoned, etc)
- [ ] Simple monster templates/stats
- [ ] Combat encounter flow integrato in GM conversation

**3.4 — Equipment & Inventory**
- [x] Definire struttura dati oggetti (Gear, Tool via SQLAlchemy ORM)
- [x] Creare item templates base (Adventuring Gear da SRD)
- [ ] Definire inventory data structure per il personaggio
- [ ] Creare item templates per armi e armature
- [ ] Implementare usage in combat
- [ ] Support equipaggiamento effects on stats

---

### Fase 4 — Multi-Campaign Management 📂

Supportare multiple campagne in parallelo.

**4.1 — Campaign Editor/Selector**
- [ ] Definire schema dati per campagna (metadata, narrative progress, participants)
- [ ] Implementare CLI menu per create/load/delete campagne
- [ ] Campaign metadata editing (nome, descrizione, incipit)
- [ ] Select campagna attiva (context globale)
- [ ] Implementare save/load campagna in JSON

**4.2 — Full Session Serialization**
- [ ] Serializzare SessionState completo
- [ ] Implementare versioning per backward compatibility
- [ ] Strategy per save snapshots vs incremental

**4.3 — Session Resume & Continuity**
- [ ] Load campagna → resume narrator recap
- [ ] Auto-populate recent NPC/location context
- [ ] Re-initialize vector DB context per campagna (se needed)

---

### Fase 5 — Web Interface 🖥️
**[POST-MVP]**

Interfaccia grafica per usability scalino successivo.

**5.1 — Webserver & Static SPA**
- [ ] Setup minimal webserver
- [ ] SPA structure (HTML/CSS/JS template)
- [ ] Chat interface (input, output stream, history)

**5.2 — Backend API**
- [ ] Implementare API endpoints per campaign CRUD
- [ ] Implementare API per chat (POST messaggio → stream risposta)
- [ ] Implementare API per character management
- [ ] Session token authentication (minimalista)

**5.3 — UI Polish**
- [ ] Mobile responsive (se needed)
- [ ] Dark mode support
- [ ] Accessibility basics (ARIA, keyboard navigation)
- [ ] Tema coerente con Valdoria (medioevo low-magic)

---

### Fase 6 — Asset Generation 🎨
**[POLISH - Optional]**

Integrazione mediarich (images, audio).

**6.1 — Stable Diffusion Integration**
- [ ] Setup SD local + API
- [ ] Prompting per NPC portraits from description
- [ ] Prompting per location backgrounds
- [ ] Caching generated assets

**6.2 — Text-to-Speech (TTS)**
- [ ] Scegliere TTS model
- [ ] Voice per GM (narratore)
- [ ] Voices per NPC differentiate
- [ ] Audio streaming per narrative

---

### Decisioni Tecniche (da definire durante implementazione)

Questi aspetti saranno decisi in fase di sprint, non predefiniti:
- **Struttura cartelle e naming** dei moduli (impostata base in `app/`, ulteriori refactor possibili)
- **Nome classi e funzioni** (TypedDict, functions, nodes)
- **Endpoints API** specifici
- ~~**Database choice**~~ **Database choice**: SQLite via SQLAlchemy per entità di gioco ✅
- **Vector DB choice** — opzione iniziale: Chroma (locale, no dependencies)
- **Embedding model** — opzione iniziale: HF MiniLM-L6
- **Language support** — MVP: Lingue supportate dall'LLM

---

### Scope Espliciti

✅ **In Scope**:
- Single-player (uno o più giocatori con GM AI)
- Single LLM source per sessione (provider definitivo ancora da confermare)
- CLI interface per MVP
- Rules consultazione via RAG
- Conversational gameplay
- Persistenza su disk
- D&D 5e mechanics minimalista

❌ **Escluso (post-MVP)**:
- Multiplayer/server architecture
- Multi-LLM (fallback, ensembles)
- Web frontend (Fase 5)
- Stable Diffusion (Fase 6)
- TTS/Audio (Fase 6)
- Advanced mechanics (prestige classes, etc)

## 📖 Sistema di Regole

DungeonLLM implementa le regole del **System Reference Document (SRD) 5.2.1**, una versione open di regole per giochi di ruolo.

### File Presenti
- `SRD_CC_v5.2.1.md` - Versione in Markdown del SRD in inglese

### Integrazione Regole

Le regole vengono integrate nel sistema in due modi complementari:

1. **Database Relazionale (SQLite)** ✅:
   - Il parser SRD (`app/graph/srdparse.py`) estrae automaticamente oggetti strutturati dall'SRD
   - Adventuring Gear già estratto e inserito nel database tramite LLM
   - Query rapide per statistiche e proprietà tramite SQLAlchemy

2. **Database Vettoriale** (pianificato):
   - Le regole saranno indicizzate in un vector database
   - L'LLM potrà consultare le regole rilevanti al contesto
   - Permetterà ricerche semantiche rapide
   - Database specifico da definire (possibili opzioni: Chroma, Pinecone, Weaviate)

## 🗄 Architettura Dati

### Database Vettoriale (Da definire)
**Scopo**: Archiviazione e recupero semantico delle regole

**Candidati**:
- Chroma
- Pinecone
- Weaviate
- Qdrant

### Database Entità (SQLite via SQLAlchemy) ✅
**Scopo**: Archiviazione strutturata di entità di gioco
**File**: `data/databases/entities.sqlite`

**Entità implementate**:
- `Gear` — oggetti generici (nome, peso, costo, descrizione), popolati dal parser SRD
- `Tool` — strumenti con abilità associata e lista di materiali craftabili

**Entità pianificate**:
- Razze e sottotipologie
- Classi e sottoclassi
- Incantesimi e abilità
- Mostri e creature
- Armi e armature
- Campagne e sessioni di gioco
- Personaggi giocatori e NPC

## 🤝 Contribuire

Il progetto è attualmente in fase iniziale. Le linee guida per contribuire verranno definite nelle prossime fasi di sviluppo.

## 📄 Licenza

Da definire

---

**Nota**: Questo è un progetto sperimentale e in continua evoluzione. Documentazione e funzionalità verranno aggiornate regolarmente durante lo sviluppo.

## Crediti
Quest'opera include materiale tratto dal System Reference Document 5.2.1 ("SRD 5.2.1") di Wizards of the Coast LLC, disponibile all'indirizzo <https://www.dndbeyond.com/srd>. Il SRD 5.2.1 è concesso in licenza ai sensi della licenza di attribuzione 4.0 Internazionale di Creative Commons, disponibile all'indirizzo <https://creativecommons.org/licenses/by/4.0/legalcode>.