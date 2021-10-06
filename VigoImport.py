import csv
import os

#Oyvind leker seg med nytt repository

filSti = '/Users/oyvind.kvalnes/Downloads/test2.txt'
eksportRootFolder = '/Users/oyvind.kvalnes/Downloads/VINN/'
vedleggPath = '/Users/oyvind.kvalnes/Downloads/Vedlegg/'

kandidatfil = ""
kandidatFolder = ""

def mapCoordinatingSchool(schoolName):
    return {
        'KOORDINERINGSSKOLE OLAV DUUN VGS' : 'OLAskolen', 
        'lorem' : 'ipsumm'
    }[schoolName]

def kandidat(row):
    kandidatfil.write("------KANDIDAT------\n")
    kandidatfil.write("FNR: " + row[1] + "\n")
    kandidatfil.write("Koordinerende skole: " + row[2]+ "\n")
    kandidatfil.write("LinjeNavn: " + row[3]+ "\n")
    kandidatfil.write("Andre opplysninger " + row[4]+ "\n")
    kandidatfil.write("Webkommunikasjon: " + row[5]+ "\n")
    kandidatfil.write("Rettstype: " + row[6]+ "\n")
    kandidatfil.write("Sluttkompetanse: " + row[7]+ "\n")
    kandidatfil.write("Ønsker veiledning: " + row[8]+ "\n")
    kandidatfil.write("Ønsker RKV: " + row[9]+ "\n")
    kandidatfil.write("Ønsker opplæring: " + row[10]+ "\n")
    kandidatfil.write("Søknad Veiledning: " + row[11]+ "\n")
    kandidatfil.write("Søknad RKV: " + row[12]+ "\n")
    kandidatfil.write("Søknad Opplæring: " + row[13]+ "\n")
    kandidatfil.write("Nettbasert: " + row[14]+ "\n")
    kandidatfil.write("RKVVurdert: " + row[15]+ "\n")
    kandidatfil.write("Startet opplæring: " + row[16]+ "\n")
    kandidatfil.write("Avbrutt: " + row[17]+ "\n")
    kandidatfil.write("\n")
    
def ANExperiences(row):
    kandidatfil.write("------ERFARING------\n")
    kandidatfil.write("FNR: " + row[1] + "\n")
    kandidatfil.write("Fra: 08." + row[2] + "\n")
    kandidatfil.write("Til: 06." + row[3] + "\n")
    kandidatfil.write("Oppdragsgiver: " + row[4] + "\n")
    kandidatfil.write("Beskrivelse: " + row [5] + "\n")
    kandidatfil.write("\n")


def utdanning(row):
    kandidatfil.write("------UTDANNING------\n")
    kandidatfil.write("FNR: " + row[1] + "\n")
    kandidatfil.write("Startaar: 08." + row[2] + "\n")
    kandidatfil.write("Sluttaar: 06." + row[3] + "\n")
    kandidatfil.write("Lærersted: " + row[4] + "\n")
    kandidatfil.write("VedleggID: " + row[5] + "\n")
    kandidatfil.write("\n")
    if len(row[5]) > 1:
        kopierVedlegg(row[5])

def kurs(row):
    kandidatfil.write("------KURS------\n")
    kandidatfil.write("FNR: " + row[1] + "\n")
    kandidatfil.write("Fra dato: " + row[2] + "\n")
    kandidatfil.write("Til dato: " + row[3] + "\n")
    kandidatfil.write("Lærested: " + row[4] + "\n")
    kandidatfil.write("VedleggID" + row[5] + "\n")
    kandidatfil.write("\n")
    if len(row[5]) > 1:
        kopierVedlegg(row[5])

def sertifikat(row):
    kandidatfil.write("------SERTIFIKAT------\n")
    kandidatfil.write("FNR: " + row[1] + "\n")
    kandidatfil.write("Sertifikat: " + row[2] + "\n")
    kandidatfil.write("Beskrivelse: " + row[3] + "\n")
    kandidatfil.write("Gyldig fra: " + row[4] + "\n")
    kandidatfil.write("Gyldig til: " + row[5] + "\n")
    kandidatfil.write("VeldeggID: " + row[6] + "\n")
    kandidatfil.write("\n")
    if len(row[6]) > 1:
        kopierVedlegg(row[6])

def praksis(row):
    kandidatfil.write("------PRAKSIS------\n")
    kandidatfil.write("FNR: " + row[1] + "\n")
    kandidatfil.write("Fra dato: " + row[2] + "\n")
    kandidatfil.write("Til dato: " + row[3] + "\n")
    kandidatfil.write("Praksissted: " + row[4] + "\n")
    kandidatfil.write("Praksis: " + row[5] + "\n")
    kandidatfil.write("VedleggID: " + row[6].strip("\\") + "\n")
    kandidatfil.write("\n")
    
    if len(row[6]) > 1:
        kopierVedlegg(row[6])

def kopierVedlegg(attachment):
    filepath = attachment.strip("\\")
    filepath = filepath.split(".")[0]
    filepath = filepath + ".pdf"
    print(vedleggPath + filepath)
    from shutil import copyfile
    copyfile(vedleggPath+filepath, kandidatFolder + filepath)    

with open(filSti, newline='') as csvfile:
    csvReader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in csvReader:
        if not os.path.exists(eksportRootFolder + "/" + row[1]):
            os.mkdir(eksportRootFolder + "/" + row[1] + "/")
            kandidatFolder = eksportRootFolder + "/" + row[1] + "/"
            kandidatfil = open(kandidatFolder + row[1] + ".txt", "a")
        if row[0] == "KA":
            kandidat(row)
        elif row[0] == "UT": #Utdanning
            utdanning(row)
        elif row[0] == "KU": #Kurs
            kurs(row)
        elif row[0] == "SE": #Sertifikat
           sertifikat(row)
        elif row[0] == "PR": #praksis
           praksis(row)
        elif row[0] == "AN": #andre opplysninger
           ANExperiences(row)
