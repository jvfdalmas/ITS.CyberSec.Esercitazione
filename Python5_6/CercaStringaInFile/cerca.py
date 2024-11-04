import os
import mmap
import PyPDF2
import textract
import googlegemini
import subprocess
import shutil

# IMISSIONE DEI PARAMETRI

sRoot = input("Inserisci la root directory: ")
sStringaDaCercare = input("Inserisci la stringa da cercare: ")
SOutDir = input("Inserici la directory di output: ")
iNumFileTrovati = 0

# METODI

def CercaStringaInFileName(sFile, sStringToSearch):
    sFilename1 = sFile.lower()
    sStringToSearch1 = sStringToSearch.lower()
    print("Cerco {0} in {1}".format(sStringToSearch1, sFilename1))
    iRet = sFilename1.find(sStringToSearch1)
    if(iRet>=0):
        print("Trovato!")
        return True
    return False

def CercaStringaInFileContent(sFile, sString):
    sString = sString.lower()
    try:
        with open(sFile) as f:
            s = mmap.mmap(f.fileno(), 0, access = mmap.ACCESS_READ)
            sAppo = s.readline()
            while len(sAppo) > 0:
                SAppo = SAppo.lower()
                if sAppo.find(sString.encode() != -1):
                    return True
                else:
                    sAppo = s.readline()
    except:
        return False

def CercaInFilePdf(sFile,sString):
    object = PyPDF2.PdfReader(sFile)
    numPages = len(object.pages)
    for i in range(0, numPages):
        pageObj = object.pages[i]
        text = pageObj.extract_text()
        text = text
        if(text.find(sString)!=-1):
           return True
    return False

def CercaInFileDoc(sFile,sString):
    text = textract.process(sFile)
    text = text
    if(text.find(sString.encode())!=-1):
        return True
    return False

def SalvaFile(src_path, dest_folder):
    filename = os.path.basename(src_path)
    dest_path = os.path.join(dest_folder, filename)
    if os.path.exists(dest_path):
        base, ext = os.path.splitext(filename)
        counter = 2
        new_dest_path = os.path.join(dest_folder, f"{base}_{counter}{ext}")
        while os.path.exists(new_dest_path):
            counter += 1
            new_dest_path = os.path.join(dest_folder, f"{base}_{counter}{ext}")
        shutil.copy2(src_path, new_dest_path)
        print(f"Copied as: {new_dest_path}")
    else:
        shutil.copy2(src_path, dest_path)
        print(f"Copied to: {dest_path}")

#NAVIGA NEL FILE SYSTEM

for root, dirs, files in os.walk(sRoot):
    sToPrint = "Dir corrente {0} contenent {1} subdir e {2} files".format(root,len(dirs),len(files))
    print(sToPrint)

    for filename in files:
        
        iRet = CercaStringaInFileName(filename, sStringaDaCercare)
        if iRet == True:
            print("Trovato file: ", filename)
            iNumFileTrovati += 1
            SalvaFile(pathCompleto, SOutDir)
            
        else:
            pathCompleto = os.path.join(root,filename)
            iRet = CercaStringaInFileName(pathCompleto, sStringaDaCercare)
        
            sOutFileName,sOutFileExt = os.path.splitext(filename)

            if sOutFileExt.lower()==".pdf":
                iRet = CercaInFilePdf(pathCompleto,sStringaDaCercare)
                if iRet == True:
                    print("Trovato file: ", filename)
                    iNumFileTrovati += 1
                    SalvaFile(pathCompleto, SOutDir)

            elif sOutFileExt.lower()==".doc":
                print(CercaInFileDoc(pathCompleto,sStringaDaCercare))
                if iRet == True:
                    print("Trovato file: ", filename)
                    iNumFileTrovati += 1
                    SalvaFile(pathCompleto, SOutDir)

            elif sOutFileExt.lower() in [".jpg", ".gif"]:
                iRet = googlegemini.CercaIMGGemini(pathCompleto,sStringaDaCercare)
                subprocess.run(["rm", "./temp_img/image.jpg"])
                subprocess.run(["rm", "./request.json"])
                if iRet == True:
                    print("Trovato file: ", filename)
                    iNumFileTrovati += 1
                    SalvaFile(pathCompleto, SOutDir)
            else:
                print(CercaStringaInFileContent(pathCompleto,sStringaDaCercare))

print(iNumFileTrovati)
