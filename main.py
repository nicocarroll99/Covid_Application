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

    for elem in root:
        print(elem.attrib)
        for subelem in elem.findall('uses-permission'):
            print(subelem.attrib)
            print(subelem.get('name'))

if __name__ == '__main__':

    getPermissions("AndroidManifest.xml")

    # Get location of files for analysis and get output directory name
    #homeFile = input("Please enter the path of the file that contains the applications for analysis: ")
    #files = getFiles(homeFile)

    #for filePath in files:
        # Run the de-compiler
        #os.system("apktool d " + filePath)




