#entre un caractere entre 1 et 4 caractere sinon repose la question
continuer = True
while continuer:
    message=input('entre votre message')
    messagetrim=message.strip()
    l=len(message) 
    if l>0:
        if l<=4:
            continuer = False
            print('reussi')
        else:
            True 
    