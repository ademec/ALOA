#!/usr/bin/env python 
#-*- coding: utf-8 -*-
"""
Création du gazetteer minimaliste des lieux pour le NER 
sur les positions de thèses de l'ENC.
"""

import csv

if __name__ == "__main__":
    input_csv = "../output_data_prepared/quicherat_voyages_geolocalises_images_enrichi.csv"
    output_file = "../output_data_prepared/Gazetteer_loc_quicherat"
    intermediate = []
    with open(input_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            intermediate.append(row[11])

    # deduplication des lieux 
    locations = list(set(intermediate))
    # écriture du gazetter (mention LOC)
    with open(output_file, mode="w", encoding="utf-8") as of:
        for location in locations:
            of.write(f"{location},LOC\n")


