# zooDictionary by Mr. Considine
# 10/29/20
# This program is a dictionary example to describe animals in a zoo and their
# enclosures.

def main():

    print("Here is a guide to Zoo locations!")

    zooPlaces = {
       "elephant": "Savannah",
       "polar bear": "Arctic",
       "arctic fox": "Arctic",
       "penguin": "Ice Arena",
       "shark": "Sea",
       "hippo": "Wetlands",
       "eagle": "Forest",
       "camel": "Desert"
        }

    # We can find any enclosure through the key associated with it


    #print(zooPlaces["penguin"])

    # Let's find all possible enclosures.
    # Start with creating a list of the keys

    keyList = ["elephant", "polar bear", "arctic fox", "penguin", "shark",
               "hippo", "eagle", "camel"]

    for i in range(len(keyList)):
        # if we loop 8 times, i starts at 0 and increases by 1 each loop.
        # keyList[i] is the element in the list at the i position. 
        print(zooPlaces[keyList[i]])

    print("Here is a list of all of the animals.")
    print(keyList)
    animal = input("Pick a number 1 through 8 to choose the animal associated with it.")
    animal = int(animal) 
    print("Here is the enclosure you should find.")
    print(zooPlaces[keyList[animal - 1]])
    





if __name__ == "__main__":
    main()
