import os


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


if __name__ == '__main__':
    # Get location of files for analysis and get output directory name
    homeFile = input("Please enter the path of the file that contains the applications for analysis: ")
    files = getFiles(homeFile)

    for filePath in files:
        # Run the de-compiler
        os.system(r"python apk_decompiler.py -a " + filePath)



