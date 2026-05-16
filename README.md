# EPITA 2026 — Intelligence Symbolique

## Liste des sujets de projet

Ce document presente les sujets de projet pour le cours d'Intelligence Symbolique (SCIA). Chaque sujet inclut une description detaillee, des references academiques et pratiques, des liens vers les notebooks CoursIA pertinents, et les technologies a utiliser.

> **Consignes de choix** : Chaque groupe doit forker ce depot et creer un dossier pour son projet contenant le code source, un notebook explicatif OU une UI/demo fonctionnelle (au choix), et les slides de soutenance. Les livraisons se font via des pull requests regulieres.

---

## Modalites du projet

### Taille des groupes

| Taille | Bonus/Malus |
|--------|-------------|
| 3 personnes | Standard |
| 2 personnes | +1 point |
| 1 personne (solo) | +3 points |
| 4 personnes | -1 point |

### Soutenance — Evaluation collegiale

La soutenance finale est evaluee de maniere **collegiale** (pairs + enseignants). Chaque groupe est note sur **4 criteres** (0-10 chacun) :

| Critere | Description |
|---------|-------------|
| **Qualite de la presentation** | Communication, clarte, pedagogie, qualite des slides, demonstrations |
| **Qualite theorique** | Principes utilises, classes d'algorithmes, contexte historique, explication des performances et limitations |
| **Qualite technique** | Livrables (code, notebook, UI), qualite du code, commits Git, demonstrations, resultats, perspectives |
| **Organisation** | Planning, repartition des taches, collaboration, activite Git, documentation |

**Note finale = somme des 4 criteres / 2 (echelle /20), ajustee du bonus/malus taille de groupe.**

### Livrables attendus

- **Code source** documente dans un sous-dossier dedie (`groupe-XX-nom-sujet/`)
- **Notebook Jupyter** explicatif avec analyse et visualisations **OU** **UI/demo fonctionnelle** (au choix — un notebook tres complet peut tenir lieu de demo, et inversement)
- **Slides de soutenance** (PDF ou lien)
- **Pull Request** soumise au plus tard **2 jours avant la soutenance**

### Echeances

- **Date de soutenance** : en cours de confirmation avec la scolarite
- **Deadline PR** : 2 jours avant la soutenance

---

## Ressources communes a tous les sujets

### Solveurs et outils
- **Z3 SMT Solver** : solveur SMT de reference pour verification formelle et raisonnement symbolique. [Documentation](https://z3prover.github.io/api/html/namespacez3py.html), [Tutoriel Python](https://ericpony.github.io/z3py-tutorial/guide-examples.htm)
- **Google OR-Tools CP-SAT** : solveur CP pour problemes combinatoires. [Documentation](https://developers.google.com/optimization/cp/cp_solver)
- **CVC5 SMT Solver** : solveur SMT alternatif. [Documentation](https://cvc5.github.io/)
- **TweetyProject** : librairie Java pour logique formelle, argumentation et raisonnement probabiliste. [Documentation](https://tweetyproject.org/)

### Frameworks et plateformes
- **Semantic Kernel** : orchestration d'agents IA avec plugins. [GitHub](https://github.com/microsoft/semantic-kernel)
- **Fast Downward** : planificateur PDDL de reference. [Site](https://www.fast-downward.org/)
- **Solidity / Foundry** : developpement et test de smart contracts. [Documentation](https://docs.soliditylang.org/)
- **PySAT** : interface Python pour solveurs SAT. [Documentation](https://pysathq.github.io/)

### Notebooks du cours CoursIA
Les notebooks suivants sont disponibles dans le depot CoursIA ([jsboige/CoursIA](https://github.com/jsboige/CoursIA)) et constituent des prerequis ou des points de depart pour les projets :

#### Logique formelle et SAT/SMT
- **SymbolicAI/Linq2Z3.ipynb** : Z3 SMT Solver en C#
- **SymbolicAI/OR-tools-Stiegler.ipynb** : OR-Tools CP en C#
- **Sudoku/** : 18 notebooks couvrant Sudoku avec multiples solveurs (Z3, CP-SAT, backtracking)

#### Smart Contracts et Blockchain
- **SymbolicAI/SmartContracts/** : Serie de 27 notebooks (SC-0 a SC-26) couvrant blockchain, Solidity, verification formelle (SC-14), fuzz testing (SC-13), cryptographie ZKP/HE (SC-15/16)

#### Planification
- **SymbolicAI/Planners/** : Planners-1 a Planners-12 couvrant PDDL, Fast Downward, planification temporelle, HTN, LLM Planning

#### Theorie des Jeux
- **GameTheory/** : 17+ notebooks couvrant Nash Equilibrium, Cooperative Games, Shapley Value, Mechanism Design

#### Programmation par Contraintes
- **Search/Part2-CSP/** : CSP-1 (Fondamentaux), CSP-4 (Scheduling), CSP-5 (Optimization), CSP-6 (Hybridation CP+SAT, LLM+CSP), CSP-7 (Soft Constraints), CSP-9 (Distributed CSP)
- **Search/Applications/CSP/** : App-4 (Job-Shop Scheduling), App-8 (MiniZinc), App-11 (Picross)

#### Recherche et Metaheuristiques
- **Search/Part1-Foundations/** : Search-1 (StateSpace), Search-3 (A*, heuristiques), Search-4 (Local Search), Search-9 (Programmation lineaire), Search-11 (Metaheuristiques)

---

## Index des Sujets

### Categorie A : Logique Formelle, SAT et Demonstration Automatique

| # | Sujet | Difficulte |
|---|-------|------------|
| [A1](#a1---resolution-automatique-de-theoremes-par-sat) | Resolution automatique de theoremes par SAT | 3/5 |
| [A2](#a2---synthese-de-programmes-par-programming-by-sketching) | Synthese de programmes par Programming-by-Sketching | 4/5 |
| [A3](#a3---model-checking-de-protocoles-de-communication) | Model checking de protocoles de communication | 3/5 |
| [A4](#a4---resolution-de-puzzles-logiques-par-smt) | Resolution de puzzles logiques par SMT | 2/5 |
| [A5](#a5---demonstration-automatique-en-geometrie) | Demonstration automatique en geometrie | 4/5 |

### Categorie B : Verification Formelle et Surete des Logiciels

| # | Sujet | Difficulte |
|---|-------|------------|
| [B1](#b1---verification-formelle-de-smart-contracts-solidity-par-smt) | Verification formelle de smart contracts Solidity par SMT | 3/5 |
| [B2](#b2---fuzzing-guide-par-contraintes-constraint-based-fuzzing) | Fuzzing guide par contraintes (constraint-based fuzzing) | 4/5 |
| [B3](#b3---analyse-statique-et-detection-de-vulnerabilites-par-abstraction) | Analyse statique et detection de vulnerabilites par abstraction | 3/5 |
| [B4](#b4---preuves-de-correcteur-zero-knowledge-zk-snarks) | Preuves de correcteur Zero-Knowledge (zk-SNARKs) | 4/5 |

### Categorie C : Planification et Ordonnancement

| # | Sujet | Difficulte |
|---|-------|------------|
| [C1](#c1---planification-robotique-avec-pddl-et-integration-capteurs) | Planification robotique avec PDDL et integration capteurs | 3/5 |
| [C2](#c2---planification-htn-pour-jeux-video) | Planification HTN pour jeux video | 3/5 |
| [C3](#c3---ordonnancement-multi-agent-par-csp-distribue) | Ordonnancement multi-agent par CSP distribue | 4/5 |
| [C4](#c4---planification-temporelle-pour-systemes-cyber-physiques) | Planification temporelle pour systemes cyber-physiques | 4/5 |

### Categorie D : Theorie des Jeux et Mechanism Design

| # | Sujet | Difficulte |
|---|-------|------------|
| [D1](#d1---comptabilite-maximin-et-equilibres-de-nash-par-programmation-lineaire) | Comptabilite maximin et equilibres de Nash par programmation lineaire | 3/5 |
| [D2](#d2---encheres-combinatoires-et-allocation-de-biens-publics) | Encheres combinatoires et allocation de biens publics | 4/5 |
| [D3](#d3---jeux-cooperatifs-et-valeur-de-shapley) | Jeux cooperatifs et valeur de Shapley | 3/5 |
| [D4](#d4---conception-de-mecanismes-resistants-a-la-manipulation) | Conception de mecanismes resistants a la manipulation | 4/5 |

### Categorie E : Smart Contracts et Blockchain Symbolique

| # | Sujet | Difficulte |
|---|-------|------------|
| [E1](#e1---super-optimisation-de-gas-solidity-par-max-smt) | Super-optimisation de gas Solidity par Max-SMT | 4/5 |
| [E2](#e2---ordonnancement-mev-resistant-de-transactions-on-chain) | Ordonnancement MEV-resistant de transactions on-chain | 3/5 |
| [E3](#e3---circuits-zero-knowledge-sous-contraintes-arithmetiques) | Circuits Zero-Knowledge sous contraintes arithmetiques | 4/5 |
| [E4](#e4---governance-decentralisee-et-vote-quadratique) | Governance decentralisee et vote quadratique | 3/5 |

### Categorie F : Representation des Connaissances et Raisonnement

| # | Sujet | Difficulte |
|---|-------|------------|
| [F1](#f1---systeme-de-maintenance-de-verite-jtms) | Systeme de maintenance de verite (JTMS) | 3/5 |
| [F2](#f2---ontologies-et-raisonnement-semantique-owl-reasoning) | Ontologies et raisonnement semantique (OWL Reasoning) | 3/5 |
| [F3](#f3---graphes de-connaissances-et-reponse-a-des-questions) | Graphes de connaissances et reponse a des questions | 3/5 |
| [F4](#f4---logique-description-et-raisonnement-sur-des-domaines-medicaux) | Logique de description et raisonnement sur des domaines medicaux | 4/5 |

### Categorie G : Argumentation et Raisonnement Debateur

| # | Sujet | Difficulte |
|---|-------|------------|
| [G1](#g1---analyse-et-detection-de-sophismes-par-apprentissage-symbolique) | Analyse et detection de sophismes par apprentissage symbolique | 3/5 |
| [G2](#g2---generation-de-contre-arguments-par-raisonnement-formel) | Generation de contre-arguments par raisonnement formel | 3/5 |
| [G3](#g3---argumentation-dialogique-multi-agents) | Argumentation dialogique multi-agents | 4/5 |
| [G4](#g4---evaluation-automatique-de-la-qualite-argumentative) | Evaluation automatique de la qualite argumentative | 3/5 |

### Categorie H : Agents Symboliques et Architecture Cognitive

| # | Sujet | Difficulte |
|---|-------|------------|
| [H1](#h1---systeme-multi-agents-de-resolution-de-problemes-par-planification) | Systeme multi-agents de resolution de problemes par planification | 3/5 |
| [H2](#h2---agent-cognitif-hybride-symbolique--subsymbolique) | Agent cognitif hybride (symbolique + subsymbolique) | 4/5 |
| [H3](#h3---serveur-mcp-doutils-danalyse-symbolique) | Serveur MCP d'outils d'analyse symbolique | 3/5 |
| [H4](#h4---integration-llm--solveurs-symboliques-llm-as-a-reasoner) | Integration LLM + solveurs symboliques (LLM-as-a-reasoner) | 4/5 |

### Categorie I : Cryptographie Symbolique et Securite

| # | Sujet | Difficulte |
|---|-------|------------|
| [I1](#i1---cryptanalyse-par-contraintes-de-chiffrements-classiques) | Cryptanalyse par contraintes de chiffrements classiques | 3/5 |
| [I2](#i2---verication-de-protocoles-cryptographiques-par-model-checking) | Verification de protocoles cryptographiques par model checking | 4/5 |
| [I3](#i3---chiffrement-homomorphe-et-calcul-sur-donnees-chiffrees) | Chiffrement homomorphe et calcul sur donnees chiffrees | 4/5 |

### Categorie J : Puzzles, Jeux et Problemes Combinatoires

| # | Sujet | Difficulte |
|---|-------|------------|
| [J1](#j1---resolution-de-sudoku-par-multiples-solveurs-sat-cp-lll) | Resolution de Sudoku par multiples solveurs (SAT, CP, LLL) | 2/5 |
| [J2](#j2---generation-procedurale-par-contraintes-de-niveaux-de-jeu) | Generation procedurale par contraintes de niveaux de jeu | 3/5 |
| [J3](#j3---resolution-de-jeux-combinatoires-par-minimax-et-alpha-beta-symbolique) | Resolution de jeux combinatoires par minimax et alpha-beta symbolique | 3/5 |

---

> **Note** : Les descriptions detaillees de chaque sujet, les references academiques et les notebooks CoursIA associes seront enrichis progressivement. Cette premiere version est un draft soumis pour revue et enrichissement par l'equipe pedagogique.
