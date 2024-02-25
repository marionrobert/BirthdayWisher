# Birthday Wisher

## Présentation
Le projet Birthday Wisher automatise le processus d'envoi de vœux d'anniversaire par courriel à vos amis et membres de votre famille. Il vérifie un fichier CSV contenant les détails des anniversaires, les associe à la date du jour et envoie des courriels d'anniversaire personnalisés aux destinataires respectifs.

## Fonctionnement
1. Mise à Jour de birthdays.csv : Mettez à jour le fichier birthdays.csv avec les détails de vos amis et membres de votre famille. Assurez-vous qu'une des entrées correspond à la date du jour à des fins de test. Le format doit être le suivant: nom,courriel,année,mois,jour.

2. Vérification des Anniversaires :
Le script vérifie si la date du jour correspond à un anniversaire dans le fichier birthdays.csv.
Il crée un tuple à partir du mois et du jour du jour actuel en utilisant le module datetime.

3. Envoi des Vœux d'Anniversaire : S'il y a correspondance, le script sélectionne un modèle de lettre aléatoire dans le dossier letter_templates et remplace [NOM] par le nom réel de la personne à partir de birthdays.csv. Ensuite, il envoie le courriel d'anniversaire personnalisé à l'adresse courriel du destinataire.

## Configuration & Installation
- Python : Version 3.9.6
- Bibliothèques Python : requests, datetime, smtplib, time
- Paramètres de Courriel : Fournissez votre adresse courriel Gmail (mon_courriel) et votre mot de passe de l'application (mon_mot_de_passe) pour permettre au script d'envoyer des courriels.

## Exécution
Exécutez le script birthdaywisher.py. Le script vérifie les anniversaires dans le fichier birthdays.csv. S'il trouve un anniversaire, il sélectionne un modèle de lettre aléatoire, le personnalise et l'envoie par courriel.

## Remarques
Ce projet a été réalisé dans le cadre du cours [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/) de Angela Yu sur la plateforme Udemy.



