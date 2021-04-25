import os
import xml.etree.ElementTree as ET


# Function to get the APK files from the file specified by the user
def getFiles(directory):
    files = os.listdir(directory)
    allFiles = list()

    for entry in files:
        path = os.path.join(directory, entry)
        if os.path.isdir(path):
            allFiles = allFiles + getFiles(path)
        else:
            allFiles.append(path)

    return allFiles


# Print the list of permissions
def printPermissions(permissions):
    for permission in permissions:
        print(permission)


# Function to determine the risk rating of each application based on its permissions
def riskRating(permissions):
    risk = 0
    for permission in permissions:
        risk += .5
        if "bluetooth" in permission.lower():
            risk += 1
        if "access_background_location" in permission.lower():
            risk += 3
        if "access_coarse_location" in permission.lower():
            risk += 3
        if "access_fine_location" in permission.lower():
            risk += 3

    return risk


# Function to parse the APKs AndroidManifest.xml file into a tree structure for analysis
def getPermissions(xmlFile):
    tree = ET.parse(xmlFile)
    root = tree.getroot()
    elements = []

    # Loop through the XMl file and search for permissions
    for elem in root:
        if elem.tag == "uses-permission":
            elements.append(elem.attrib.get("{http://schemas.android.com/apk/res/android}name"))

    # Remove duplicates from the list of permissions
    elements = list(set(elements))
    # Print the permissions and risk rating
    printPermissions(elements)
    risk = riskRating(elements)
    print("OVERALL PRIVACY RATING = " + str(risk))

    # Assign a severity label based on the risk rating
    if 0 <= risk <= 3:
        print("SEVERITY LABEL: LOW")
    elif 4 <= risk <= 6:
        print("SEVERITY LABEL: NORMAL")
    elif 7 <= risk <= 9:
        print("SEVERITY LABEL: HIGH")
    else:
        print("SEVERITY LABEL: DANGEROUS")


if __name__ == '__main__':
    # Get location of files for analysis and get output directory name
    homeFile = input("Please enter the path of the file that contains the applications for analysis: ")
    files = getFiles(homeFile)
    fileNames = []

    for filePath in files:
        # Format the names of the files for pulling their XML files after de-compiling
        fileName = filePath.rpartition("\\")[2]
        fileName = fileName.replace(".apk", "")
        fileNames.append(fileName)

        # Run the de-compiler
        os.system("apktool d " + filePath)

    for name in fileNames:
        print("\n\nPermissions for " + name)
        getPermissions(name + r"\AndroidManifest.xml")






