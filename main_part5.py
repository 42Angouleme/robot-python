from pybot import Robot

robot = Robot()
robot.demarrer_webapp()

long = 1200
haut = 500

blanc = (255, 255, 255)
noir = (0, 0, 0)
rouge = (235, 64, 52)
rouge_sombre = (117, 23, 16)
bleu = (52, 164, 235)
bleu_sombre = (30, 93, 133)
vert = (105, 230, 83)
vert_sombre = (59, 135, 46)
jaune = (237, 212, 66)
jaune_sombre = (171, 128, 19)

bouton_suppression = None
bouton_deconnexion = None

session_ouverte = False

mettre_a_jour_affichage = True
def preparer_programme():
    global bouton_suppression, bouton_deconnexion
    robot.allumer_ecran(long, haut)
    robot.couleur_fond(noir)

    robot.ajouter_evenement("echap", "stop")
    bouton_deconnexion = robot.creer_bouton(200, 60, 25, 200, jaune_sombre)
    bouton_deconnexion.ajouter_texte("Deconnexion", 5, 20)
    bouton_suppression = robot.creer_bouton(200, 60, 25, 300, rouge_sombre)
    bouton_suppression.ajouter_texte("Supprimer utilisateur", 5, 20)

def affichage_ecran():
    global mettre_a_jour_affichage, session_ouverte
    if mettre_a_jour_affichage:
        robot.afficher_fond()
        if session_ouverte:
            bouton_deconnexion.afficher()
            bouton_suppression.afficher()
        robot.afficher_texte("CREATION", 1000, 5, 30, (255, 255, 255))
        robot.afficher_texte("PROFIL", 80, 5, 30, (255, 255, 255))
        mettre_a_jour_affichage = False

def verifier_boutons():
    global mettre_a_jour_affichage, afficher_camera, afficher_photo, session_ouverte
    if robot.verifier_session() != session_ouverte:
        session_ouverte = robot.verifier_session()
        mettre_a_jour_affichage = True
    elif session_ouverte:
        if bouton_suppression.verifier_contact():
            robot.supprimer_utilisateur()
            session_ouverte = False
            mettre_a_jour_affichage = True
        if bouton_deconnexion.verifier_contact():
            robot.deconnecter()
            session_ouverte = False
            mettre_a_jour_affichage = True

def boucle_programme():
    global mettre_a_jour_affichage, session_ouverte
    while robot.est_actif():
        events = robot.verifier_evenements()
        if "stop" in events:
            robot.eteindre_ecran()
        robot.afficher_camera(300, 10)
        if not session_ouverte:
            robot.connecter()
            if robot.verifier_session():
                print(f"Hello \033[96;1m{robot.utilisateur_connecte.first_name} {robot.utilisateur_connecte.last_name}\033[0;0m !")
            else:
                carte_detectee = robot.detecter_carte()
                if carte_detectee:
                    robot.afficher_carte_detectee(carte_detectee, 980, 200)
        affichage_ecran()
        verifier_boutons()
        robot.dessiner_ecran()


if __name__ == "__main__":
    preparer_programme()
    boucle_programme()
