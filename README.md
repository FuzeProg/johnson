# JOHNSON
Vous écrirez une fonction qui calcule les plus cours chemins entre tout couple de sommets par l’algorithme de Johnson. L’argument de la fonction sera un graphe de taille n arbitraire sous forme de listes d’adjacence, les coûts des arcs 𝑐(𝑥, 𝑦) de type entier. La sortie sur écran et dans un fichier sera, pour couple s, t ∈ S, la liste ordonnée des sommets formant un chemin de coût minimum entre s et t ainsi que son coût, ou +∞ si t n’est pas accessible depuis s. Votre fonction utilisera la structure de données des tas binaires que vous devrez également programmer. Chaque fonction et procédure devra être testée sur des exemples. Ainsi, votre travail se décompose en les étapes suivantes.
1) Implémentation d’une fonction qui prend en entrée deux entiers n et m ≤ n(n − 1) et donne en sortie un graphe aléatoire orienté à n sommets et m arêtes donné sous forme de listes d’adjacence.
2) Implémentation de la variante de l’algorithme de Bellman-Ford qui retourne un message d’erreur si le graphe possède un circuit absorbant. Tests.
3) Implémentation naïve de l’algorithme de Dijkstra. Tests sur des petits graphes, et sur des graphes aléatoires dont les arcs ont des coûts aléatoires uniformes entre 0 et 1000.
4) Implémentation d’une file de priorité avec un tas binaire (tableau). Implémentation de l’algorithme de Dijkstra avec une file de priorité. Tests.
5) Comparer les deux implémentations de l’algorithme de Dijkstra et générer un tableau de comparaison.
6) Implémentation de l’algorithme de Johnson. Tests sur des petits graphes, et sur des graphes aléatoires dont les arcs ont des coûts aléatoires uniformes entre −500 et 1000.
7) Enfin, vous ferez quelques expériences en variant n et m pour vérifier expérimentalement la différence entre l’algorithme naïf et l’algorithme Johnson.

[1[2, 3, 5], 2[4, 3], ]