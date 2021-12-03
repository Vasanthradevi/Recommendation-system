labels = ["G1", "G2", "G3", "G4"]
classArousal = open("Trained data/class arousal.csv",'w')
classValence = open("Trained data/class valence.csv",'w')
for j in range(28):
    for i in labels:
        Ar_file = "Training data/Ar_" + i + ".txt"
        Va_file = "Training data/Va_" + i + ".txt"
        with open(Ar_file, "r") as Ar:
            with open(Va_file, "r") as Va:
                Ar_val = Ar.readlines()
                Va_val = Va.readlines()
                if float(Ar_val[j]) > 3:
                    classArousal.write(str(3) + "\n")
                else:
                    classArousal.write(str(1) + "\n")
                if float(Va_val[j]) > 3:
                    classValence.write(str(3) + "\n")
                else:
                    classValence.write(str(1) + "\n")



