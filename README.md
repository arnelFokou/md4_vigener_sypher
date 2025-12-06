# Documentation du projet : Chiffrement César et Vigenère en Python

## Description du projet

Ce projet consiste en l’implémentation de deux méthodes classiques de chiffrement de texte : le **chiffrement de César** et le **chiffrement de Vigenère**. L’objectif principal était de créer un système de chiffrement capable de gérer **tous les caractères imprimables** en Python, afin d’éviter les problèmes liés aux caractères non affichables ou aux encodages Unicode.

Le projet fournit également des fonctionnalités supplémentaires pour tester et analyser les messages chiffrés.

---

## Ce qui a été implémenté

1. **Alphabet personnalisé**
   - Tous les caractères imprimables sont inclus grâce à `string.printable`.  
   - Deux dictionnaires ont été créés pour convertir les caractères en indices et vice-versa, permettant un chiffrement sûr, contrôlé et une reduction de la complexite( O(1)) pour la recherche de caractere.
   - Ces dictionnaires remplacent les fonctions `ord()` et `chr()` classiques pour assurer que tous les caractères restent imprimables.

2. **Chiffrement et déchiffrement César**
   - La fonction `cesar_sypher` chiffre un message en décalant chaque caractère d’une valeur donnée.  
   - La même fonction permet de **déchiffrer** un message en appliquant le décalage inverse.  
   - Gestion automatique du dépassement d’index grâce au modulo sur la taille de l’alphabet personnalisé.

3. **Brute-force sur le chiffrement César**
   - La fonction `hack_cesar_sypher` génère toutes les possibilités de messages déchiffrés en essayant tous les décalages possibles.
   - Permet de retrouver un message chiffré sans connaître la clé.

4. **Chiffrement et déchiffrement Vigenère**
   - La fonction `vigener_sypher` chiffre ou déchiffre un message en utilisant une clé composée de plusieurs caractères.  
   - Chaque caractère du message est décalé selon la valeur du caractère correspondant de la clé, répétée si nécessaire.  
   - S’appuie sur la fonction César pour le décalage individuel de chaque caractère.

5. **Gestion complète des caractères imprimables**
   - Grâce à l’alphabet personnalisé, tous les caractères du message et de la clé restent visibles après chiffrement.  
   - Aucun caractère non imprimable ni octet invalide n’est généré, ce qui garantit une compatibilité totale avec Python et les affichages classiques.

---

## Fonctionnalités principales

- Chiffrement César (avec clé unique)  
- Déchiffrement César  
- Brute-force sur César  
- Chiffrement Vigenère (avec clé multiple)  
- Déchiffrement Vigenère  
- Gestion de tous les caractères imprimables  
- Code clair et modulable, prêt pour des expérimentations éducatives

---

## Conclusion

Ce projet fournit une **implémentation complète des chiffrements classiques de type César et Vigenère** adaptée aux caractères imprimables en Python. Il permet de chiffrer et déchiffrer des messages, de tester tous les décalages possibles pour le César, et de travailler avec des clés de Vigenère de longueur variable.  

C’est un outil pédagogique pour comprendre le fonctionnement du chiffrement et la manipulation des caractères et des indices dans un alphabet personnalisé.
