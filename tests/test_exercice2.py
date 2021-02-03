from exercices.exercice2 import *

def test_rechercheT():
 assert recherche("AATC", "GTACAAATCTTGCC") == True

def test_rechercheF():
    assert recherche("AGTC", "GTACAAATCTTGCC") == False
