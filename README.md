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
			"topic_set": [
                "Topic"
            ]
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
			"topics": [
            {
                "id": 3,
                "title": "Topic 1",
                "description": "Topic",
                "created": "2015-07-10T07:28:31Z",
                "updated": "2015-07-10T07:28:31Z",
                "imageURL": null,
                "views": 0,
                "creator": {
                    "id": 1,
                    "username": "alberish"
                }
            }
        ]
		},
	]
}
```
## Gestion des catégories ##
#### Lister les catégories ####
```
/categories
```
#### Créer une catégorie ####
```
/categories + POST
```
#### Voir le profil d'une catégorie ####
```
/categories/:category_id
```
#### Mettre à jour une catégorie ####
```
/categories/:category_id + PUT
```
#### Supprimer une catégorie ####
```
/categories/:category_id + DELETE
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
            "created": "2015-07-09T08:12:16Z",
            "updated": "2015-07-09T08:12:16Z",
			"imageUrl": "url/to/image.jpg",
			"views": 50,
			"creator": {
			    "id": 22,
			    "username": "Cliko"
		    },
		    "messages": [
            	{
			        "id": 1,
			        "title": "Voici la réponse",
			        "content": "JE pense qu'en fait tu dois investir dans des lunettes...",
                    "created": "2015-07-09T08:12:46Z",
                    "updated": "2015-07-09T08:12:46Z",
			        "user": 22 (user_id),
			        "topic": 50 (topic_id)
		        },
		    ],
			"category": 22 (category_id),
			"type_topic": 1 (type_id),
			"favorite_topics": [1, 2] (user_id)
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
# Messages
#### Structure d'un message ####
```
{
	"data":[
		{
			"id": 1,
			"title": "Voici la réponse",
			"content": "JE pense qu'en fait tu dois investir dans des lunettes...",
            "created": "2015-07-09T08:12:46Z",
            "updated": "2015-07-09T08:12:46Z",
			"user": 22 (user_id),
			"topic": 50 (topic_id)
			"comments"[
						{
							"id": 1,
							"content": "Tu as raison ! Je valide !",
							"created": "2015-07-09T13:34:15Z",
							"user": 22 (user_id),
							"message": 50 (message_id)
						},
			]
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
			"created": "2015-07-09T13:34:15Z",
			"user": 22 (user_id),
			"message": 50 (message_id)
		},
	]
}
```
## Gestion des informations commentaires ##
#### Lister les commentaires ####
```
/comments
```
#### Créer un commentaire ####
```
/comments + POST
```
#### Voir le profil d'un commentaire ####
```
/comments/:comments_id
```
#### Mettre à jour un commentaire ####
```
/comments/:comments_id + PUT
```
#### Supprimer un commentaire ####
```
/comments/:comments_id + DELETE
```

# Types
#### Structure d'un type ####
```
{
	"data":[
		{
			"id": 1,
			"name": "Question"
		},
	]
}
```
## Gestion des informations des types ##
#### Lister les commentaires ####
```
/types
```
#### Créer un commentaire ####
```
/types + POST
```
#### Voir le profil d'un commentaire ####
```
/types/:type_id
```
#### Mettre à jour un commentaire ####
```
/types/:type_id + PUT
```
#### Supprimer un commentaire ####
```
/types/:type_id + DELETE
```