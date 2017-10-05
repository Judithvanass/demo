#oefening 1:  Vraag twee getallen aan de gebruiker.  Controleer of deze gelijk zijn aan elkaar of verschillend.  Print een gepaste boodschap af.
# getal1 = int(input("Geef een getal : "))
# getal2 = int(input("Geef nog een getal"))
#
# if (getal1 == getal2):
#     print("{0} is gelijk met {1}".format(getal1,getal2))
# else:
#     print("{0} is niet gelijk met {1}".format(getal1,getal2))



# oefening 2: Vraag een niet-decimaal getal aan de gebruiker. Bepaal of het opgegeven getal even of oneven is. Print een gepaste boodschap af
# getal = int(input("Geef een niet-decimaal getal : "))
#
# berekening
# resultaat = getal %2
#
# if ( resultaat == 0 ):
#     print("{0} is even".format(getal))
# else:
#     print("{0} is oneven".format(getal))



#oefening 3: Vraag aan de gebruiker wat zijn geboortejaar is. Indien hij nog geen 18 is, print dan ook een gepaste melding af.
# geboortejaar = int(input("Wat is uw geboortejaar? "))
# import datetime
#
# nu = datetime.datetime.now()
# nu = nu.year
#
# if (geboortejaar < nu-18):
#     print("Ok, u mag alcohol drinken")
# else:
#     print("U bent nog geen 18, kom volgend jaar terug!")



#oefening 4: Maak een Python programma dat de leeftijd van een hond vertaalt naar een overeenkomstige leeftijd van een mens. Vraag eerst aan de gebruiker de leeftijd van zijn hond. Nadien print je een correcte boodschap af waarbij: - Indien getal < 0, geef een foutmelding terug. - Indien leeftijd = 1  14 mensenjaren - Indien leeftijd = 2  22 mensenjaren - Indien meer dan 2: mensenleeftijd = 22 + (jaren – 2) * 5
# leeftijdHond = int(input("Wat is de leeftijd van uw hond? "))
# leeftijdMens = 22 + (leeftijdHond-2)*5
# if (leeftijdHond < 0):
#     print("Foutmelding")
# elif(leeftijdHond == 1):
#     print(14)
# elif(leeftijdHond == 2):
#     print(22)
# elif(leeftijdHond > 2):
#     print("leeftijdMens")
# print("Deze leeftijd komt overeen met {0} mensenjaren".format(leeftijdMens))



#oefening 5: Vraag de decimale score van een module aan de gebruiker. Print nadien af of hij/zij geslaagd is. Zorg ervoor dat de score correct afgerond wordt: indien het decimale gedeelte kleiner is dan 0,5 wordt er naar beneden afgerond. In het andere geval wordt er naar boven afgerond. Print ook de afgeronde score af.
# score = float(input("Geef uw score op: "))
# if (score < 5):
#     print("Helaas, volgende keer beter!")
# else:
#     print("U bent geslaagd!")
#
#
# import math
# achterKomma = score - math.floor(score)
# if (achterKomma < 0.5):
#     print(math.floor(score))
#     print("Het afgeronde getal is ")
# else:
#     print("Het afgeronde getal is ")
#     print(math.ceil(score))



#oefening 6: Controleer of Python bij het vergelijken van 2 strings al dan niet hoofdlettergevoelig is
# A = "test"
# a = "Hallo"
#
# A==a

#WERKEN MET FUNCTIES
#oefening 1: Schrijf een functie ‘printWelkom’ die een string als parameter heeft. Deze string stelt de naam voor. Print in de functie een welkomsbericht af waarin de naam gebruikt wordt.  Test de methode met verschillende namen.
# def printWelkom(naam):
#     print("Welkom {0}".format(naam))
#
# printWelkom (input("Wat is je naam: "))

#Oefening 2:  Schrijf een functie ‘printWelkom’ die twee strings als parameters heeft: naam en groep. Zorg ervoor dat de parameter groep een defaultwaarde ‘1NMCT1’ krijgt. Print een welkomstbericht af waarin naam & groep vermeld staan.  Test de functie voldoende
def printWelkom(naam,groep = "1NMCT1"):
    print("Welkom {0} uit de groep {1}".format(naam,groep))

printWelkom(input("Wat is je naam? "))
printWelkom(input("Wat is je groep? "))



