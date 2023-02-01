# 4A_SQR_CI_CD

<p align="center">
  <a href="https://bde-esirem.fr/" target="_blank"><img src="https://user-images.githubusercontent.com/95021980/210582471-8ddd094d-ac9d-4e56-8dad-29d0fd7e7058.png" width="100" height="100" /></a>
  <a href="https://www.youtube.com/@esicast" target="_blank"><img src="https://user-images.githubusercontent.com/95011291/210586766-d2a52a72-45c3-480d-9545-15d152e0efc8.png" width="100" height="100"></a>
</p>

<div centering style="display: flex; flex_direction: row;  margin-left: auto;">

<div />

## Présentation

Nous sommes [Max Bonnici](https://github.com/MaxBonnici), [Doğan Kaptan](https://github.com/DoganKaptan) et [Anis Mouniym](https://github.com/AnisMouniym)


## Langage utilisé

<p align="center">
  <img src="http://ForTheBadge.com/images/badges/made-with-python.svg">
</p>



## Choix du sujet

Nous avons choisis le sujet guidé n'étant pas des experts en création d'API nous n'avons pas voulu être perdu lors de notre projet.

## Explication du sujet

Objectif : Utilisation du langage Python pour créer une API Flask pour gérer un système de transaction avec de la gestion CRUD (Create Read Update Delete) 
  
### Réalisation d'une première version de l'API REST
  
Commande CURL:

E1: 
````
curl -X GET http://localhost:5000/transactions/"
````
E2:
````
curl -d "r=<receiver>&s=<sender>&amount=<amount>&t=<jour/mois/année>" POST http://localhost:5000/add_transaction/
````
E3:
````
curl -X GET http://localhost:5000/transactions/"<person>"
````
E4:
````
curl -X GET http://localhost:5000/balance/"<person>"
````


### Documentation de l'API à l'aide du fichier README et Swagger
  
  [Swagger](swagger.yaml)
  
### Création de github actions

![GitHub watchers](https://github.com/MaxBonnici/4A_SQR_CI_CD/actions/workflows/app_build.yml/badge.svg)  
![GitHub watchers](https://github.com/MaxBonnici/4A_SQR_CI_CD/actions/workflows/build_and_push.yml/badge.svg)  
![GitHub watchers](https://github.com/MaxBonnici/4A_SQR_CI_CD/actions/workflows/build_image.yml/badge.svg) 
  
### Déploiement de la publication automatique des nouvelles version dans un registre de conteneur Google




