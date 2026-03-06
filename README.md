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

⚠️ **Progetto in Early MVP Development** - Fondazioni tecniche in place, focus su GM conversazionale robusto.

Lo sviluppo è in corso seguendo una **roadmap granulare di 6 fasi**. Attualmente sono state completate le fondazioni base (Python, Langchain, Langgraph, Ollama). Il focus immediato è su:
1. **Fase 0-1**: Persistenza dati + GM conversazionale coerente con memoria di sessione
2. **Fase 2**: RAG system per consultazione regole D&D 5e via SRD
3. **Fase 3+**: Meccaniche di gioco progressivamente elaborate

Vedi [Roadmap di Sviluppo](#-roadmap-di-sviluppo) per dettagli granulari.

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

- [ ] Implementare sistema di save/load conversazione in JSON
- [ ] Definire structure minimalista per salvare history conversazionale
- [ ] Creare primo fixture di test per conversation persistence
- [ ] Testare save/load singola sessione conversazionale

---

### Fase 1 — GM Conversazionale Robusto 🤖
**[CORE MVP]**

GM mantiene coerenza narrativa, memoria di sessione, adattamento dinamico.

**1.1 — Memory & Context Management**
- [ ] Implementare sliding-window context (ultimi N turni + metadata campagna)
- [ ] Aggiungere nodo per memory management nel grafo Langgraph
- [ ] Evitare token explosion con summarization/compression

**1.2 — GM Personality & Consistency**
- [ ] Separare prompt in componenti modularizzabili (base instructions / campaign context / session state)
- [ ] Implementare composizione dinamica prompt basata su campagna attiva
- [ ] Testare coerenza narrativa e tono GM across multiple turns

**1.3 — Multi-turn Dialogue & NPC Interaction**
- [ ] Supportare scelte NPC nella conversazione
- [ ] Implementare memoria semplice per personalità NPC e relazioni con PG
- [ ] Aggiungere nodo per NPC interaction nel grafo

**1.4 — Session Continuity & Loading**
- [ ] Implementare session resume + recap narrativo
- [ ] Persistere conversazione tra multiple run
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
- [ ] Definire schema dati personaggio (ability scores, proficiencies, hp, skills)
- [ ] Implementare character creation flow conversazionale (GM guida giocatore via chat)
- [ ] Validazione vs D&D 5e rules (via RAG)
- [ ] Implementare save/load personaggio in JSON
- [ ] Testare creazione personaggio end-to-end

**3.2 — Dice Mechanics**
- [ ] Implementare dice roller (d20, d12, d8, d6, d4, d100)
- [ ] Supporto advantage/disadvantage
- [ ] Dice expression parser (es. "2d20 + modifier")
- [ ] Integrazione in Langgraph (nodo per action resolution)
- [ ] Extraction intenzione azione da conversazione
- [ ] Proposta roll + esecuzione + narrazione risultato

**3.3 — Basic Combat System**
- [ ] Turn-based initiative system
- [ ] Action parsing (attack, dodge, etc)
- [ ] Damage calculation vs HP
- [ ] Condition tracking (stunned, poisoned, etc)
- [ ] Simple monster templates/stats
- [ ] Combat encounter flow integrato in GM conversation

**3.4 — Equipment & Inventory**
- [ ] Definire inventory data structure
- [ ] Creare item templates (weapons, armor, consumables)
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
- **Struttura cartelle e naming** dei moduli
- **Nome classi e funzioni** (TypedDict, functions, nodes)
- **Endpoints API** specifici
- **Database choice** (JSON vs SQLite) — opzione iniziale: JSON, migrazione in Fase 4 se needed
- **Vector DB choice** — opzione iniziale: Chroma (locale, no dependencies)
- **Embedding model** — opzione iniziale: HF MiniLM-L6
- **Language support** — MVP: Lingue supportate dall'LLM

---

### Scope Espliciti

✅ **In Scope**:
- Single-player (uno o più giocatori con GM AI)
- Single LLM source (Ollama attuale)
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