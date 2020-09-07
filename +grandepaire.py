#! /usr/bin/python3

class Queue:
    ########################################################
    # TODO: écrivez les spécifications complètes de la classe
    # TODO: complétez les méthodes de la classe pour implémenter
    #       une file par un tableau dynamique circulaire
    def __init__(self):
        
        self.items = []
        return None
        
    def __len__(self):
        
        
        return len(self.items)
    
    def enqueue(self, item):
       
        self.items.append(item)
        return None
    
    def dequeue(self):
        """
        pre: 
        post:
        """
        return None
    def is_empty(self):
        
        if self.__len__() == 0 : return True
        else : return False
        
    ########################################################
    # Si vous le désirez, vous pouvez implémenter la méthode
    # __str__(self) pour obtenir une représentation de votre
    # file sous forme de string
    # Exemple:
    def __str__(self):
        str_queue = "This is a Queue. Ideally, I should report "\
        "my content.\n"
        return str_queue




#Exemples de tests:
file = Queue()
items = [i for i in range(1, 50)]

if not file.is_empty():
    print("Une nouvelle file devrait être vide après initialisation.")

for item in items:
    file.enqueue(item)
    if not len(file) == item:
        print("La taille de la file ({}) est incorrecte après ajout de l'élément : {}.".format(len(file), item))

for item in items:
    if not file.dequeue() == item:
        print("La suppression d'un élément ne renvoit pas le bon élément : {}.".format(item))