import os
import xml.etree.ElementTree as ET


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


def getPermissions(xmlFile):
    tree = ET.parse(xmlFile)
    root = tree.getroot()

    # Loop through the XMl file and search for permissions
    for elem in root:
        if elem.tag == "uses-permission":
            print(elem.attrib)
        for subelem in elem.findall('uses-permission'):
            print(subelem.attrib)
            print(subelem.get('name'))


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
        #os.system("apktool d " + filePath)

    for name in fileNames:
        print("Permissions for " + name)
        getPermissions(name + r"\AndroidManifest.xml")






