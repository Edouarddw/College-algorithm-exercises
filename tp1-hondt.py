#First exercices, counting votes using the Hondt system
def plus_forte_moyenne(n_sieges, resultat_vote):
    vote = []
    t = []
    parti = 0
    for i in range(len(resultat_vote)):
        t.append(0)
        vote.append([resultat_vote[i]])
        for j in range(n_sieges - 1): 
            vote[i].append(resultat_vote[i]/(j+2))
    for k in range (0, n_sieges):
        max1 = 0
        for i in range(len(resultat_vote)):
            for j in range(len(vote[i])):
                if vote[i][j] > max1:
                    max1 = vote[i][j]
                    parti = i
        t[parti] += 1
        vote[parti].remove(max1)
    return t
          
if not plus_forte_moyenne(11, [437, 478, 85]) == [5,5,1]:
    print("Exemple de la méthode de D'Hondt")

    

def beta_plus_forte_moyenne(n_sieges, resultat_vote):
    somme_vote = 0
    for i in resultat_vote :
        somme_vote += i
    allocation_vote = []
    for vote in resultat_vote :
        allocation_vote.append(int(vote/somme_vote)*n_sieges)
    if len(allocation_vote) == 1 :
        t = allocation_vote
        return t
    for i in range(n_sieges) :
        _previous_max = 0
        for index, j in enumerate(resultat_vote):
            k = allocation_vote[index]
            _max = j/(k+1)
            if _max > _previous_max :
                _previous_max = _max
                index_max = index
        allocation_vote[index_max] += 1 
    t = allocation_vote
    return t
            
if not beta_plus_forte_moyenne(13, [482]) == [13]:
    print("------------------------------")
    
