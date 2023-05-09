import shutil
import os
import random as rand
import numpy as np

rand.seed(42)

initial_count = 0
score_types = [["accidental tucking", 18], 
               ["accidentals 1", 11],  
               ["accidentals grace notes", 14],
               ["accidentals mid-bar key signatures", 13],
               ["accidentals", 50], 
               ["Alkan - Posement", 63],
               ["Bach - Goldberg Variation 16", 9], 
               ["Bach - Goldberg Variation 25", 18], 
               ["Bartok - Mikrokosmos 144", 25],
               ["Bartok - Nights Music", 38],
               ["Bartok - Solo Violin Sonata mvt 4", 59],
               ["Bartok - String Quartet 5 mvt 3", 86],
               ["beam groups 3", 18],
               ["beam groups 8 semiquavers", 85],
               ["beam groups 12 demisemiquavers simple", 1365],
               ["beam groups 12 semiquavers compound", 1302],
               ["beam groups 12 semiquavers simple", 1292],
               ["beam groups nested tuplets", 10],
               ["beam groups rests 1", 72],
               ["beam stem weight notes 1", 40],
               ["beam subdivisions crotchet unit", 11],
               ["beam subdivisions quaver unit", 38],
               ["beamed grace notes 2-note intervals", 11],
               ["beams 2-note intervals", 20],
               ["beams 4-note directions", 40],
               ["Beethoven - Diabelli Variation XIV", 7],
               ["Beethoven - Diabelli Variation XXIII", 9],
               ["Beethoven - Diabelli Variation XXVII", 10],
               ["Beethoven - Diabelli Variation XXXI", 15],
               ["Chopin - Etude Op 10 no 1", 39],
               ["Chopin - Etude Op 10 no 11", 21],
               ["Delius - String Quartet mvt III", 35],
               ["Haydn - Piano Trio 27 mvt I", 56],
               ["Janacek - 1X1905 mvt 2", 28],
               ["Mendelssohn - Songs Without Words 17", 44],
               ["Reger - Improvisationen 3", 13],
               ["Reger - Improvisationen 4", 16],
               ["Reger - Improvisationen 7", 27],
               ["Reger - Improvisationen 8", 47],
               ["Reger - Introduction", 26],
               ["Satie - Gnossienne 1", 17],
               ["Schumann - String Quartet 1 mvt 3", 35],
               ["Scriabin - Prelude Op 11 no 14", 23],
               ["syncopation 1b", 29],
               ["Webern - Variations Op 27 III", 20]]

original_root_dir = "Sheet_Music_Dataset"
target_root_dir = "Small_Sheet_Music_Dataset"

if(not os.path.exists(target_root_dir)):
    os.mkdir(target_root_dir)

for f in os.listdir(target_root_dir):
    os.remove(os.path.join(target_root_dir, f))

for i in range(len(score_types)):
    choices = np.array([], dtype = int)
    choice = -1
    for j in range(3):
        while(choice in choices and not choices.size == 0 or choice == -1):
            choice = rand.randint(1, score_types[i][1])
        choices = np.append(choices, choice)

        if(choice >= 1 and choice < 10):
            image_choice = f"{score_types[i][0]}-00{choice}.png"
        elif(choice >= 10 and choice < 100):
            image_choice = f"{score_types[i][0]}-0{choice}.png"
        elif(choice >= 100):
            image_choice = f"{score_types[i][0]}-{choice}.png"

        shutil.copy(f"{original_root_dir}/{image_choice}", f"{target_root_dir}/{image_choice}")

count = 0
for path in os.listdir(target_root_dir):
    if os.path.isfile(os.path.join(target_root_dir, path)):
        count += 1
print(count)