import json
from os import system
from datetime import datetime



def main():

    while True:
        print("\n===== Notes Menu =====\n")
        print("\n 1. Show all Notes\n 2. Add Note\n 3. Quit\n")
        selection = int(input("Enter an option number: "))

        if selection == 1:
            system("cls")
            showDocs()
        
        if selection == 2:
            addDoc()
        
        if selection == 3:
            break

    system("cls")

    return

def readDB():
    f = open("notes-db.json", 'r')
    j = json.load(f)
    f.close()
    return j

def writeDB(allDocs):
    f = open("notes-db.json", "w")
    f.write(json.dumps(allDocs))
    f.close()
    return

def addDoc():
    doc = {
        "timestamp": datetime.now().strftime("%d-%b-%Y (%H:%M:%S)"), 
        "docTitle": None, 
        "docData": None, 
        "docNote": None
        }
    doc["docTitle"] = str(input("Add Title ('Enter' to skip): ")) or None
    doc["docData"] = str(input("Add URL/Data/Code Snippet ('Enter' to skip): ")) or None
    doc["docNote"] = str(input("Add Note ('Enter' to skip): ")) or None

    if doc["docTitle"] == None and doc["docData"] == None and doc["docNote"] == None:
        i = str(input("Blank Note not saved. Press Enter to continue"))
        return
    
    allDocs = readDB()
    entries = allDocs["totalEntries"]

    allDocs["rows"].append({"_id": entries+1, "doc":doc})
    allDocs["totalEntries"] += 1

    writeDB(allDocs)
    
    return

def showDocs():
    allNotes = readDB()["rows"]
    output = ""

    for note in allNotes:
        oneNote = "===============\n \n"
        id = "ID: " + str(note["_id"]) + "\n"
        timestamp = "Timestamp: " + str(note["doc"]["timestamp"]) + "\n"
        title = "Title: " + (str(note["doc"]["docTitle"]) or "None") + "\n"
        data = "Note Data: " + (str(note["doc"]["docData"]) or "None") + "\n"
        text = "Note: " + (str(note["doc"]["docNote"]) or "None") + "\n"
        outroPadding = "\n===============\n \n"

        oneNote += id + timestamp + title + data + text + outroPadding

        output += oneNote
    
    print(output)

    input("\nPress Enter to continue...")
    system("cls")

    return
def formatNote():
    return

def resetDB():
    db = {
        "totalEntries": 0,
        "rows":[]
    }
    f = open("notes-db.json", "w")
    f.write(json.dumps(db))
    f.close()

    print("DB reset")
    return

if __name__ == "__main__":
    main()