
def main():
    #importing libraries needed for makeShuffle function
    import time
    import sys
    import random

    #importing libraries needed for main
    import shutil
    import os

    #prompt user for directory that we will be using
    base_file_directory = input("Please enter the file directory for your starcraft folder:\nLeaving this empty will assume it is in the default location\n")
    print(base_file_directory)

    #check for valid user input
    #if it is empty, assume the default directory
    if base_file_directory == "\n":
        print("boy that is a new line")
        base_file_directory = "Z:\\My Drive\\Dropbox\\New folder (3)\\Starcraft II\\Accounts\\"
    elif base_file_directory == "":
        print("boy that is an empty string")

    #the accountIds of the accounts you want to copy and shuffle hotkeys to
    #this should be changed so that it copies them automatically
    accounts = ["1736517", "70056340", "72705267", "77732427", "85434961", "86373425", "86492430", "87808971", "89446409", "89662727", "126384011", "315855594", "350403565", "351690861", "377437837", "377785739", "377793407", "379201447", "379209204", "379220901", "379220943", "379252463", "379252496", "379266120", "379906113", "381274912", "381827850", "381857282", "381867033", "448356624"]
    for x in accounts:
        makeShuffle()
        shutil.move( "C:\\Users\\MLT-Acer\\Downloads\\MLT-Shuffle.SC2Hotkeys", "Z:\\My Drive\\Dropbox\\New folder (3)\\Starcraft II\\Accounts\\" + x + "\Hotkeys\MLT.SC2Hotkeys")


def makeShuffle():

    #path to original file
    inputfile = open("Z:\\My Drive\\Dropbox\\New folder (3)\\Starcraft II\\accounts\\56959549\\Hotkeys\\MLT.SC2Hotkeys","r")


    keywords = ["ControlGroupAppendAndSteal", "ControlGroupAppend", "ControlGroupAssignAndSteal", "ControlGroupAssign", "ControlGroupRecall", "CameraSave", "CameraView"]
    keywords2 = ["Shift+Alt+","Shift+","Alt+", "Control+",""]
    lines = inputfile.readlines()
    inputfile.close()
    commandHotkeys = "\n"+"[Commands]"
    passedCommandHotkeys  = False
    counter1=counter2=counter3=counter4=counter5=counter6=counter7=0

    # Creates a list containing 5 lists, each of 8 items, all set to ""
    w, h = 10, 7;
    key1 = [["" for x in range(w)] for y in range(h)]
    key2 = [["" for x in range(w)] for y in range(h)]
    #the string at the end of the
    otherString = ""


    #initialize to default values
    for x in range ( 0, 5 ):
        for y in range ( 0, 10 ):
            key1[x][y] = keywords[x] + str(y)
            key2[x][y] = keywords2[x] + str(y)

    for y in range ( 0, 4 ):
        key1[5][y] = keywords[5] + str(y)
        key2[5][y] = "Control+F" + str(y+5)

    for y in range ( 4, 8 ):
        key1[5][y] = keywords[5] + str(y)
        key2[5][y] = "Control+Shift+F" + str(y+1)

    for y in range ( 0, 4 ):
        key1[6][y] = keywords[6] + str(y)
        key2[6][y] = "F" + str(y+5)

    for y in range ( 4, 8 ):
        key1[6][y] = keywords[6] + str(y)
        key2[6][y] = "Shift+F" + str(y+1)



    #test print
    #for x in range ( 0, 7 ):
    #    for y in range ( 0, 10 ):
    #        print(key1[x][y]+"="+key2[x][y])

    #parse all the text
    for line in lines:
        line = line.strip()
        if passedCommandHotkeys == True:
            commandHotkeys = commandHotkeys + "\n" + line
        elif "ControlGroupAppendAndSteal" in line:
            parsed = line.split("=",2)
            number = int (parsed[0][ len(keywords[0]) ])

            key1[0][number] = parsed[0]
            key2[0][number] = parsed[1]
#            print("1: ", number, line)
        elif "ControlGroupAppend" in line:

            parsed = line.split("=",2)
            number = int (parsed[0][ len(keywords[1]) ])

            key1[1][number] = parsed[0]
            key2[1][number] = parsed[1]
#            print("2: ", number, line)
        elif "ControlGroupAssignAndSteal" in line:
            parsed = line.split("=",2)
            number = int (parsed[0][ len(keywords[2]) ])

            key1[2][number] = parsed[0]
            key2[2][number] = parsed[1]
#            print("3: ", number, line)

        elif "ControlGroupAssign" in line:
            parsed = line.split("=",2)
            number = int (parsed[0][ len(keywords[3]) ])
            key1[3][number] = parsed[0]
            key2[3][number] = parsed[1]
#            print("4: ", number, line)
        elif "ControlGroupRecall" in line:
            parsed = line.split("=",2)
            number = int (parsed[0][ len(keywords[4]) ])
            key1[4][number] = parsed[0]
            key2[4][number] = parsed[1]
#            print("5: ", number, line)
        elif "CameraSave" in line:
            parsed = line.split("=",2)
            number = int (parsed[0][ len(keywords[5]) ])

            key1[5][number] = parsed[0]
            key2[5][number] = parsed[1]
 #           print("6: ", number, line)
        elif "CameraView" in line:
            parsed = line.split("=",2)
            number = int (parsed[0][ len(keywords[6]) ])

            key1[6][number] = parsed[0]
            key2[6][number] = parsed[1]
#            print("7: ", number, line)
        elif "[Commands]" in line:
            passedCommandHotkeys = True
        else:
            otherString = otherString + line + "\n"
            #print("8:", otherString)



    #decide the shuffling order
    #initialize array

    hotkeyOrder = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    cameraOrder = [0, 1, 2, 3, 4, 5, 6, 7]
    #for making the hotkeys  more believable
    hotkeyOrder1 = [0, 1, 2, 3]
    hotkeyOrder2 = [4, 5, 6, 7, 8, 9]


    #shuffle the array
    #random.shuffle( hotkeyOrder )
    random.shuffle( cameraOrder )
    random.shuffle( hotkeyOrder1 )
    random.shuffle( hotkeyOrder2 )

    for x in range ( 0, len(hotkeyOrder1) ):
        hotkeyOrder[x]= hotkeyOrder1[x]

    for x in range ( 0, len(hotkeyOrder2) ):
        hotkeyOrder[x+len(hotkeyOrder1)] = hotkeyOrder2[x]

    #print( hotkeyOrder )
    #print ( cameraOrder )
    for x in range ( 0, 5 ):
        for y in range ( 0, 10 ):
            a=1
            #put the shuffled strings back in the temp file
            #print( "\n" + key1[x][y] + "=" + key2[x][hotkeyOrder[y]] )
            #print( "\n" + key1[x][y] + "=" + key2[x][y] )

    #put hotkeys back untouched (hotkeys that don't need to be shuffled)
    outputfile = open("C:\\Users\\MLT-Acer\\Downloads\\MLT-Shuffle.SC2Hotkeys", "w")
    outputfile.write( otherString )

    for x in range ( 0, 5 ):
        for y in range ( 0, 10 ):
            a=1
            #put the shuffled strings back in the temp file
#            print( "\n" + key1[x][y] + "=" + key2[x][hotkeyOrder[y]] )
            outputfile.write( "\n" + key1[x][y] + "=" + key2[x][hotkeyOrder[y]] )

    for x in range ( 5, 7 ):
        for y in range ( 0, 8 ):
            a=1
            #put the shuffled strings back in the temp file
#            print( "\n" + key1[x][y] + "=" + key2[x][ cameraOrder[y] ] )
            outputfile.write( "\n" + key1[x][y] + "=" + key2[x][cameraOrder[y]] )



    outputfile.write ( "\n" + commandHotkeys )
    #close the output file
    outputfile.close(  )


    # pause 5.5 seconds
    # time.sleep(5.5)


if __name__ == "__main__":
    main()
