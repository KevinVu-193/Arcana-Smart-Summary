


def SemesterFileCreation(x): 
    for i in range(x): 
        f = open("Week " + str(i+1) + ".txt", "w")
    print("Files created successfully")


SemesterFileCreation(12)