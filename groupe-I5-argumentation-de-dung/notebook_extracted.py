
--- MARKDOWN CELL ---
# 0. Introduction

--- MARKDOWN CELL ---
Dans le cadre de l'IA symbolique, ce projet et notre réalisation s'intéresse à la modélisation du raisonnement d'un agent face à des informations contradictoires. Nous étudions ici les graphes d'argumentation de Dung, un formalisme puissant qui permet d'évaluer la validité de différents arguments en conflit afin de dégager des ensembles de conclusions logiquement cohérentes.

--- MARKDOWN CELL ---
## Imports

--- CODE CELL ---
import os
import time
import subprocess
import matplotlib.pyplot as plt
import networkx as nx

from src.grounded import grounded_extension
from src.preferred import preferred_extension
from src.stable import stable_extension
from src.check import is_grounded, is_preferred, is_stable
from src.show import show_graph
from src.generate import generate_af
from src.parser import parse_af

--- MARKDOWN CELL ---
# 1. Graph de Dung / Argumentation Framework

--- MARKDOWN CELL ---
Un graphe de Dung (ou Argumentation Framework dans le cadre informatique) est un réseau mathématique simple où les nœuds représentent des arguments et les flèches représentent des relations d'attaque (de conflit) entre eux. L'objectif est d'appliquer des règles logiques sur ce graphe pour déterminer quels arguments peuvent être acceptés ensemble et lesquels doivent être rejetés. C'est un outil intuitif et visuel pour modéliser des débats, des prises de décision ou des résolutions de contradictions en IA.

Voici un exemple simple, qui va nous servir à tester nos solveurs sur un cas basique, et à montrer intuitivement ce que représente les différente sémantique de Dung:

--- CODE CELL ---
G = nx.DiGraph()
arguments = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
attaques = [('A', 'B'), ('A', 'J'), ('B', 'A'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('D', 'I'), ('E', 'C'), ('F', 'A'), ('F', 'N'), ('G', 'B'), ('H', 'F'), ('H', 'G'), ('J', 'K'), ('L', 'M'), ('M', 'N')]
G.add_nodes_from(arguments)
G.add_edges_from(attaques)

show_graph(G, title="Argumentation Framework - No Extension")

--- MARKDOWN CELL ---
# 2. Extensions

--- MARKDOWN CELL ---
Dans le cadre des graphs d'argumentations de Dung, une extension est un ensemble "cohérent" d'arguments, c'est à dire qu'ils ne se contredisent pas, et sont capables de se défendre contre les attaques des arguments exterieurs. Dung définit alors plusieurs 'sémantiques', qui sont des types d'extensions plus strictes munis de règles suplémentaires, les 4 principales sont:

- <u>Extension Complète (Complete)</u> : C'est un ensemble d'arguments sans conflit interne qui contient (et défend) tous les arguments qu'il est capable de protéger contre les attaques extérieures.
- <u>Extension de Base (Grounded)</u> : C'est l'unique ensemble minimal qui ne prend aucun risque, contenant uniquement les arguments absolument incontestables (le "noyau dur" du consensus).
- <u>Extension Préférée (Preferred)</u> : C'est un ensemble maximal d'arguments cohérents, représentant le plus grand point de vue défendable possible dans le débat.
- <u>Extension Stable (Stable)</u> : C'est un ensemble cohérent d'arguments si fort qu'il attaque et rejette absolument tous les autres arguments extérieurs du graphe.

**<u>NB</u>: Toute extension grounded, et/ou preferred, et/ou stable, est nécessairement complète, nous nous interesseront donc uniquement à ces 3 sémantiqes.**

--- MARKDOWN CELL ---
## Calcul et affichage de différentes sémantiques

--- CODE CELL ---
GR = grounded_extension(G)
PR = preferred_extension(G)
ST = stable_extension(G)

show_graph(G, GR, "The Grounded Extension")
show_graph(G, PR, "A Preferred Extension")
show_graph(G, ST, "A Stable Extension")

--- MARKDOWN CELL ---
## Intuition géométrique et interprétation

--- MARKDOWN CELL ---
- On observe premièrement que la grounded extension du graph n'est pas vide, grâce à la présence d'arguments sources (arguments jamais contredits), qui propage l'extension en créant des conclusions en chaine sur les arguments qui suivent, jusqu'au niveau de la connexion 'A<->B'.
La partie gauche du graphe est la zone de verité incontestable, elle doit necessairement être incluse dans toutes extensions completes, ou "crédible" en quelque sorte.

- La connexion A<->B arrête la propagation de l'extension grounded, car c'est une attaque mutuelle, équivalente à "ma parole contre la tienne", ainsi cette connexion oblige une prise de décision, indépendament des arguments incontestables.

- L'extension preferred affiché est celle qui choisit de "croire" l'argument A, ainsi on fait un choix et des conclusions se propage sur J et K, c'est une branche de décision.

- Une conséquence de choisir de croire A, est le fait d'invalider B, ce qui a pour conséquence d'isoler le groupe C-D-E-I, hors ce groupe contient un cycle impair. Dans un graphe de Dung, un cycle impair isolé est comme une zone d'état indécis, au arguments de ce cycle de peut être défendu, c'est pour cela que l'extension preferred qui a choisit de croire A ne peut pas trancher et inclure un des arguments C, D, E ou I.

- La derniere extension affichée est stable, elle représente le scenario où l'on choisi de croire B, ce choix se propage alors, et "tranche" sur le cycle impair. Cette fois-ci l'extension contient, ou attaque, tous les noeuds du graphe.

--- MARKDOWN CELL ---
# 3. Performances

--- MARKDOWN CELL ---
Nous allons maintenant analyser les performances de nos solveurs, et les comparer aux performances d'un solveur très efficace issu de la compétition ICCMA 2023, nommé crustabri.

--- MARKDOWN CELL ---
## Affichage

--- CODE CELL ---
def plot_performance(model, n, s0, step, m):

    # Paramètres fixes pour la génération
    NB_THEMES = 3
    P_INNER = 0.5
    P_OUTER = 0.1
    SEED = 42

    # --- CONFIGURATION DU BENCHMARK ---
    graph_sizes = [s0 + step * i for i in range(n)]
    average_times = []

    # --- MESURE DES TEMPS ---
    for s in graph_sizes:

        total_time = 0
        for i in range(m):
            # 1. Génération du graphe
            graph = generate_af(
                s, 
                NB_THEMES, 
                P_INNER, 
                P_OUTER, 
                SEED
            )
            
            # 2. Chronométrage de la fonction stable_extension
            start_time = time.perf_counter()
            model(graph)
            end_time = time.perf_counter()
        
            # 3. Sauvegarde du temps écoulé (en secondes)
            total_time += end_time - start_time
        
        # 4. Sauvergarde du temps écoulé en moyenne pour les graphs de taille t
        average_time = total_time / m
        average_times.append(average_time)
        print(f"Taille: {s:3d} arguments | Temps Moyen: {average_time:.4f}s")

    # --- AFFICHAGE DU GRAPHIQUE ---
    plt.figure(figsize=(10, 6))
    plt.plot(graph_sizes, average_times, marker='o', linestyle='-', color='b', linewidth=2)

    # Personnalisation des axes et titres
    plt.title(f"{model.__name__}: Average computing time X Number of arguments", fontsize=12, fontweight='bold')
    plt.xlabel("Number of arguments", fontsize=10)
    plt.ylabel("Average computing time (seconds))", fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.6)

    # Affichage du graphique
    plt.show()

--- MARKDOWN CELL ---
## Notre Modèle

--- MARKDOWN CELL ---
### Stratégie:

Pour être optimisés, nos solveurs réduisent le problème de recherche d'extension en un problème SAT, chaque argument a alors un booléen associé, qui indique si il fait parti ou pas de l'extension. Il ne reste alors plus qu'à ajouter les contraintes spécifiques de la sémantique. Nous utilisons ensuite le moteur CP-SAT pour résoudre le problème, c'est la principale technique utilisée dans ce domaine et notamment par beaucoup d'équipes de la compétition ICCMA.

--- CODE CELL ---
plot_performance(grounded_extension, 8, 100, 200, 20)
plot_performance(preferred_extension, 8, 10, 10, 5)
plot_performance(stable_extension, 8, 100, 100, 5)

--- MARKDOWN CELL ---
## Crustabri: Modèle issu de la compétition ICCMA 2023

--- CODE CELL ---


--- MARKDOWN CELL ---
# Observations

--- MARKDOWN CELL ---
#TODO: parler de la complexité (O(n) etc. ) des problemes au vu des graphiques (trouver une extension GR vs PR vs ST), probleme P, NP-complet ou NP-difficile

--- MARKDOWN CELL ---
## 4. Benchmark / Comparaison

--- MARKDOWN CELL ---
#TODO: Comparer les performance de nos solveurs vs crustabri sur des graphes de la compétition (fichiers en .af dans data/ )

--- CODE CELL ---

