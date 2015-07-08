# api_forum
# Utilisateurs
#### Structure d'un utilisateur ####
```
{
	"data":[
		{
			"id": 1,
			"username": "Cliko",
			"email": "benjamin.garcia@hetic.net",
			"first_name": "Benjamin",
			"last_name": "Garcia",
			"password": "password",
			"age": "22",
			"profile_picture": "url/to/image.jpg"
		},
	]
}
```
## Gestion des informations utilisateurs ##
#### Lister les utiliseurs ####
```
/users
```
#### Créer un utilisateur ####
```
/users + POST
```
#### Voir le profil d'un utilisateur ####
```
/users/:user_id
```
#### Mettre à jour un utilisateur ####
```
/users/:user_id + PUT
```
#### Supprimer un utilisateur ####
```
/users/:user_id + DELETE
```
# Catégories
#### Structure d'une catégorie ####
```
{
	"data":[
		{
			"id": 1,
			"name": "Général",
			"slug": "general"
		},
	]
}
```
## Gestion des catégories ##
#### Lister les catégories ####
```
/categorys
```
#### Créer une catégorie ####
```
/categorys + POST
```
#### Voir le profil d'une catégorie ####
```
/categorys/:category_id
```
#### Mettre à jour une catégorie ####
```
/categorys/:category_id + PUT
```
#### Supprimer une catégorie ####
```
/categorys/:category_id + DELETE
```
# Topics
#### Structure d'un topic ####
```
{
	"data":[
		{
			"id": 1,
			"title": "Comment trouver un sujet ?",
			"description": "Je cherche à trouver les sujets car je ne les trouve pas",
			"imageUrl": "url/to/image.jpg",
			"vues": 50,
			"created_by": 53 (user_id),
			"category": 22 (category_id)
		},
	]
}
```
## Gestion des informations topics ##
#### Lister les topics ####
```
/topics
```
#### Créer un topic ####
```
/topics + POST
```
#### Voir le profil d'un topic ####
```
/topics/:topic_id
```
#### Mettre à jour un topic ####
```
/topics/:topic_id + PUT
```
#### Supprimer un topic ####
```
/topics/:topic_id + DELETE
```
# Catégories
#### Structure d'une catégorie ####
```
{
	"data":[
		{
			"id": 1,
			"name": "Général",
			"slug": "general"
		},
	]
}
```
## Gestion des catégories ##
#### Lister les catégories ####
```
/categorys
```
#### Créer une catégorie ####
```
/categorys + POST
```
#### Voir le profil d'une catégorie ####
```
/categorys/:category_id
```
#### Mettre à jour une catégorie ####
```
/categorys/:category_id + PUT
```
#### Supprimer une catégorie ####
```
/categorys/:category_id + DELETE
```
# Messages
#### Structure d'un message ####
```
{
	"data":[
		{
			"id": 1,
			"title": "Voici la réponse",
			"description": "JE pense qu'en fait tu dois investir dans des lunettes...",
			"userID": 22 (user_id),
			"topicID": 50 (topic_id)
		},
	]
}
```
## Gestion des informations messages ##
#### Lister les messages ####
```
/messages
```
#### Créer un message ####
```
/messages + POST
```
#### Voir le profil d'un message ####
```
/messages/:message_id
```
#### Mettre à jour un message ####
```
/messages/:message_id + PUT
```
#### Supprimer un message ####
```
/messages/:message_id + DELETE
```
# Commentaires
#### Structure d'un commentaire ####
```
{
	"data":[
		{
			"id": 1,
			"content": "Tu as raison ! Je valide !",
			"userID": 22 (user_id),
			"messageID": 50 (message_id)
		},
	]
}
```
## Gestion des informations commentaires ##
#### Lister les commentaires ####
```
/coms
```
#### Créer un commentaire ####
```
/coms + POST
```
#### Voir le profil d'un commentaire ####
```
/coms/:com_id
```
#### Mettre à jour un commentaire ####
```
/coms/:com_id + PUT
```
#### Supprimer un commentaire ####
```
/coms/:com_id + DELETE
```
