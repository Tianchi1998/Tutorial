def translate(word,language):
    if word=="cat":
        if language=="German":
            answer="katze"
        elif language=="French":
            answer="chat"
        elif language=="Spanish":
            answer="gato"
        else:
            answer="no"
            print("Sorry,I can't translate that.")


    if word=="dog":
        if language=="German":
            answer="hund"
        elif language=="French":
            answer="chien"
        elif language=="Spanish":
            answer="perro"
        else:
            answer="no"
            print("Sorry,I can't translate that.")

    if answer in ["katze","chat","gato","hund","chien","perro"]:
       print("The translation of %s into %s is "%(word,language)+answer)
    else:
        while True:
            break

translate("lion","German")




