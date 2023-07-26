#=======Library========
import math
import datetime

#========array=========
laporanAdopsi = []
laporanDonasi = []
totalDonasi = 0

#====uname & pass admin====
#Uname admin = admin
#passw admin = adm123

#=======================================SINGLY LINKED LIST====================================================
class NodeHewan:
    def __init__(self, Name, Species,
                 Gender, Age, Breed,
                 Eyes, Fur, Vaccine,
                 Description, Status):
        self.Name = Name
        self.Species = Species
        self.Gender = Gender
        self.Age = Age
        self.Breed = Breed
        self.Eyes = Eyes
        self.Fur = Fur
        self.Vaccine = Vaccine
        self.Description = Description
        self.Status = Status
        self.next = None

class LinkedHewan:
    def __init__(self):
        self.head = None
        self.count = 0

    def getData(self, index):
        if index < 0 or index > self.count - 1:
            print("           Data tersebut tidak tersedia")
            return False
        else:
            nodeTampil = self.head
            for i in range(index):
                nodeTampil = nodeTampil.next
            LinkedHewan.printData(self, nodeTampil)


    def getStatus(self, index):
        if index < 0 or index > self.count - 1:
            return False
        else:
            nodeTampil = self.head
            for i in range(index):
                nodeTampil = nodeTampil.next
            return nodeTampil.Status

    def updateData(self, index):
        nodeUpdate = self.head
        print("Ingin mengubah data apa?")
        print(" 1. Vaccine")
        print(" 2. Description")
        print(" 3. Status")
        print("—————————————————————————————————————————————————————")
        pilihUpdate = input("Masukkan pilihan: ")
        print("—————————————————————————————————————————————————————")
        for i in range(index):
            nodeUpdate = nodeUpdate.next
        if pilihUpdate == "1":
            while True: #vaccine
                print("Vaccine: 1. Vaccinated")
                print("       : 2. Not Yet")
                z = input("Masukkan status vaccine terbaru: ")
                if z == "1":
                    updateVacc = ("Vaccinated")
                elif z == "2":
                    updateVacc = ("Not yet")
                else:
                    print("Pilihan tidak tersedia")
                    continue
                break
            nodeUpdate.Vaccine = updateVacc
            print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
            print("          Status vaksin berhasil diperbarui           ")
            print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
            
        elif pilihUpdate == "2":
            updateDesc = input("Masukkan deskrpsi baru: ")
            nodeUpdate.Description = updateDesc
            print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
            print("            Deskripsi berhasil diperbarui            ")
            print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
            
        elif pilihUpdate == "3":
            while True: #vaccine
                print("Vaccine: 1.Open for adoption")
                print("       : 2. On adoption process")
                print("       : 3. Adopted")
                x = input("Masukkan status adopsi terbaru: ")
                if x == "1":
                    updateStatus = ("Open for Adoption")
                elif x == "2":
                    updateStatus = ("On adoption process")
                elif x == "3":
                    updateStatus = ("Adopted")
                else:
                    print("Pilihan tidak tersedia")
                    continue
                break
            nodeUpdate.Status = updateStatus
            print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
            print("         Status adopsi berhasil diperbarui           ")
            print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")

        else:
            print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
            print("               Pilihan tidak tersedia               ")
            print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")

    def ubahStatus(self, index):
        nodeUpdate = self.head
        for i in range(index):
            nodeUpdate = nodeUpdate.next
        nodeUpdate.Status = "On adoption process"
            

    def addLast(self, Name, Species, Gender, Age,
                Breed, Eyes, Fur, Vaccine,
                Description, Status):
        if self.head is None:
            self.head = NodeHewan(Name, Species, Gender, Age,
                                  Breed, Eyes, Fur, Vaccine,
                                  Description, Status)
            self.count += 1
        else:
            nodeAkhir = self.head
            while nodeAkhir.next is not None:
                nodeAkhir = nodeAkhir.next
            nodeAkhir.next = NodeHewan(Name, Species, Gender,
                                       Age, Breed, Eyes, Fur,
                                       Vaccine, Description, Status)
            self.count += 1

    def newDataForm(self, namaBaru): #Tambah data hewan
        while True: #Species
            print("Species: 1. Cat")
            print("       : 2. Dog")
            w = input("Masukkan pilihan species: ")
            if w == "1":
                speciesBaru = ("Cat")
            elif w == "2":
                speciesBaru = ("Dog")
            else:
                print("Pilihan tidak tersedia")
                continue
            break
        
        while True: #Gender
            print("Gender : 1. Male")
            print("       : 2. Female")
            x = input("Masukkan pilihan gender: ")
            if x == "1":
                genderBaru = ("Male")
            elif x == "2":
                genderBaru = ("Female")
            else:
                print("Pilihan tidak tersedia")
                continue
            break
        
        while True: #Age
            print("Age    : 1. Less than 1 year old")
            print("       : 2. 1-2 years old")
            print("       : 3. 3-4 years old")
            print("       : 4. 5++ years old")
            y = input("Masukkan pilihan age: ")
            if y == "1":
                ageBaru = ("Less than 1 year old")
            elif y == "2":
                ageBaru = ("1-2 years old")
            elif y == "3":
                ageBaru = ("3-4 years old")
            elif y == "4":
                ageBaru = ("5++ years old")
            else:
                print("Pilihan tidak tersedia")
                continue
            break
        
        breedBaru = input("Breed  : ")
        eyesBaru = input("Eyes   : ")
        furBaru = input("Fur    : ")
        
        while True: #vaccine
            print("Vaccine: 1. Vaccinated")
            print("       : 2. Not Yet")
            z = input("Masukkan pilihan vaccine: ")
            if z == "1":
                vaccBaru = ("Vaccinated")
            elif z == "2":
                vaccBaru = ("Not yet")
            else:
                print("Pilihan tidak tersedia")
                continue
            break
        
        descBaru = input("Desc   : ")
        statusBaru = ("Open for adoption")
        input("Status : Open for adoption")
        
        LinkedHewan.addLast(self, namaBaru, speciesBaru, genderBaru,
                            ageBaru, breedBaru, eyesBaru, furBaru,
                            vaccBaru, descBaru, statusBaru)
        print("—————————————————————————————————————————————————————")
        print("            Data baru berhasil ditambahkan           ")
                 
    def deleteNode(self, key):
        # Store head node
        temp = self.head
        if (temp is not None):
            if (temp.Name == key):
                self.head = temp.next
                temp = None
                return
        while(temp is not None):
            if temp.Name == key:
                break
            prev = temp
            temp = temp.next
            
        if(temp == None):
            return
 
        prev.next = temp.next
 
        temp = None

        
    def printList(self):
        if self.head is None:
            print("Linked List Kosong")
        else:
            print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
            print("                L I S T  H E W A N                    ")
            print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
            nomor = 1
            nodeTampil = self.head
            while nodeTampil is not None:
                print(" {}. {}".format(nomor, nodeTampil.Name))
                print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
                nomor += 1
                nodeTampil = nodeTampil.next

    def iterate_item(self):
        # Iterate the list.
        current_item = self.tail
        while current_item:
            val = current_item.Name
            current_item = current_item.next
            yield val

    def printData(self, node):
        print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
        print(" Name   : {}".format(node.Name))
        print(" Species: {}".format(node.Species))
        print(" Gender : {}".format(node.Gender))
        print(" Age    : {}".format(node.Age))
        print(" Breed  : {}".format(node.Breed))
        print(" Eyes   : {}".format(node.Eyes))
        print(" Fur    : {}".format(node.Fur))
        print(" Vaccine: {}".format(node.Vaccine))
        print(" Desc   : {}".format(node.Description))
        print(" Status : {}".format(node.Status))      
        print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
     
    def sortedMerge(self, a, b):
        result = None
        if a == None:
            return b
        if b == None:
            return a
        if a.Name <= b.Name:
            result = a
            result.next = self.sortedMerge(a.next, b)
        else:
            result = b
            result.next = self.sortedMerge(a, b.next)
        return result
     
    def mergeSort(self, h):
        if h == None or h.next == None:
            return h
        middle = self.getMiddle(h)
        nexttomiddle = middle.next
        middle.next = None
        left = self.mergeSort(h)
        right = self.mergeSort(nexttomiddle)
        sortedlist = self.sortedMerge(left, right)
        return sortedlist

    def getMiddle(self, head):
        if (head == None):
            return head
 
        slow = head
        fast = head
 
        while (fast.next != None and
               fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
             
        return slow

    def checkDups(self, name):
        current = self.head
        while current is not None: #First loop
            if current.Name.lower() == name: 
                return True 
            current = current.next
        return False

    def searchKey(self, index):
        if index < 0 or index > self.count - 1:
            print("—————————————————————————————————————————————————————")
            print("           Data tersebut tidak tersedia")
            
        else:
            nodeTampil = self.head
            for i in range(index):
                nodeTampil = nodeTampil.next
                
            return nodeTampil.Name

    def makeList(self):
        values = []
        current = self.head
        while current is not None: #First loop
            values.append({"Name":(current.Name), "Species":(current.Species), "Gender":(current.Gender),
                            "Age":(current.Age), "Breed":(current.Breed),
                            "Eyes":(current.Eyes), "Fur":(current.Fur),
                            "Vaccine":(current.Vaccine), "Description":(current.Description),
                            "Status":(current.Status)})
            current = current.next
        return values
    
def printDict(array,indexHewan):
    print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
    print(" Name   : {}".format(array[indexHewan]["Name"]))
    print(" Species: {}".format(array[indexHewan]["Species"]))
    print(" Gender : {}".format(array[indexHewan]["Gender"]))
    print(" Age    : {}".format(array[indexHewan]["Age"]))
    print(" Breed  : {}".format(array[indexHewan]["Breed"]))
    print(" Eyes   : {}".format(array[indexHewan]["Eyes"]))
    print(" Fur    : {}".format(array[indexHewan]["Fur"]))
    print(" Vaccine: {}".format(array[indexHewan]["Vaccine"]))
    print(" Desc   : {}".format(array[indexHewan]["Description"]))
    print(" Status : {}".format(array[indexHewan]["Status"]))         
    print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")

def jumpSearch( array , namaHewan , n ):
    x = namaHewan
    step = math.sqrt(n)
    prev = 0
    
    while array[int(min(step, n)-1)]["Name"].lower() < x.lower():
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1

    while array[int(prev)]["Name"].lower() < x.lower():
        prev += 1
        if prev == min(step, n):
            return -1

    if array[int(prev)]["Name"].lower() == x.lower(): 
        return prev
     
    return -1

#=========================================DOUBLY LINKED LIST======================================================
class NodeUser:
    def __init__(self, Username, Password):
        self.Username = Username
        self.Password = Password
        self.next = None
        self.prev = None
        
class LinkedUser:
    def __init__(self):
        self.head = None
        self.count = 0
  
              
    def push(self, newUname, newPass):
        new_node = NodeUser(newUname, newPass)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def checkDups(self, newUname):
        current = self.head
        while current is not None:
            if current.Username == newUname:
                print("")
                print("—————————————————————————————————————————————————————")
                print("Username sudah tidak tersedia, coba username lain")
                return True 
            current = current.next
        return False
               

    def regisUser(self):
        print("—————————————————————————————————————————————————————")
        print("Berikan username dan password untuk akun baru Anda ")
        ulang = True
        while ulang == True:
            newUname = input("Username: ")
            check = linkedUser.checkDups(newUname)
            if check == False:
                newPass = input("Password: ")
                linkedUser.push(newUname, newPass)
                self.count += 1
                print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
                print("              Registrasi akun berhasil               ")
                print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
                input("        Klik ENTER untuk kembali ke menu login        ")
                ulang = False

    def checkIndexUser(self, uname):
        current = self.head
        nomor = 1
        while current is not None:
            if current.Username == uname:
                return nomor - 1
            current = current.next
            nomor += 1
        return -1

    def checkPassUser(self, index, passw):
        current = self.head
        for i in range(index):
            current = current.next
        if current.Password == passw:
            return True
        else:
            return False
           
    def loginUser(self):
        global uname
        print("—————————————————————————————————————————————————————")
        print("Silakan masukkan username dan password Anda")
        uname = input("Username: ")
        indexU = linkedUser.checkIndexUser(uname)
        if indexU < 0 :
            print("")
            print("               Username tidak ditemukan              ")
            print("    Pastikan Anda sudah melakukan registrasi akun     ")
            return False
            
        elif indexU >= 0:
            passw = input("Password: ")
            checkPass = linkedUser.checkPassUser(indexU, passw)
            if checkPass == True:
                MenuUser.welcomeUser()
                return True
            
            elif checkPass == False:
                print("")
                print("  Password Anda tidak sesuai, silakan login kembali  ")
                return False
         
    def printList(self, node):
        temp = self.head
        print ("Forward Traversal using next poitner")
        while(node is not None):
            print(node.Username)
            temp = node
            node = node.next
#=====================================QUEUE  &  DOUBLY LINKED LIST======================================== 
class nodeQueue():
    def __init__(self, data):
        self.data = data # Assign data
        self.antre = 0
        self.next = None # Initialize next as null
        self.prev = None # Initialize prev as null


class Queue:
   
    # Function to initialize head 
    def __init__(self):
        self.head = None
        self.last=None
        self.count = 0
        self.batas = 3

    def checkDups(self, uname):
        current = self.head
        nomor = 1
        while current is not None:
            if current.data == uname:
                print("       !! Anda sudah mengambil nomor antrean !!       ")
                print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
                print("          i n f o r m a s i   a n t r e a n           ")
                print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
                print(" In service      : {}".format(queue.first()))
                print(" No. antrean Anda: {}".format(current.antre))
                return True 
            current = current.next
            nomor += 1
        return False
         
    def enqueue(self, data):
        if self.isEmpty():
            self.head = nodeQueue(data)
            current = self.head
            self.last = self.head
            self.count += 1
            current.antre = 1
            print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
            print("          i n f o r m a s i   a n t r e a n           ")
            print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
            print(" In service      : {}".format(queue.first()))
            print(" No. antrean Anda: {}".format(current.antre))
  
        else:
            current = self.head
            dups = self.checkDups(uname)
            if dups == False and self.size() < self.batas:
                self.last.next = nodeQueue(data)
                self.last.next.prev = self.last
                self.last = self.last.next
                while current.next is not None:
                    current = current.next
                current.antre = self.size()
                print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
                print("          i n f o r m a s i   a n t r e a n           ")
                print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
                print("In service      : {}".format(queue.first()))
                print("No. antrean Anda: {}".format(current.antre))
                
            elif self.size() == self.batas:
                print(" Maaf antrean sudah penuh, silakan datang lain waktu ")
                

    def dequeue(self):
        if self.isEmpty():
            raise IndexError('Can not dequeue from an empty queue')
            return None
        else:
            temp = self.head.data
            self.head = self.head.next
            #self.head.prev = None
            
        return temp

   
    def first(self):
        return self.head.antre

   
    def size(self):
        temp=self.head
        count=0
        while temp is not None:
            count=count+1
            temp=temp.next
        return count

       
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def printQueue(self):
        print("—————————————————————————————————————————————————————")
        print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
        print("                l i s t   a n t r e a n              ")
        print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
        temp = self.head
        while temp is not None:
            print(" {}. {}".format(temp.antre, temp.data))
            temp=temp.next

#===================================MENU USER======================================
class MenuUser:
    def welcomeUser(self):
        print("—————————————————————————————————————————————————————")
        print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
        print("                    W E L C O M E                    ")
        print("                         T O                         ")
        print("                 P A W S  &  P U R R                 ")
        print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
        print("             a n i m a l   s h e l t e r             ")
        print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
        
    def menu1(self):
        print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
        print("            j a m    o p e r a s i o n a l           ")
        print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
        print("       Senin - Kamis             07:00 - 17:00       ")
        print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
        print("       Jumat - Sabtu             09:00 - 17:00       ")
        print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
        print("           Minggu                    TUTUP           ")
        print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
        print("—————————————————————————————————————————————————————")
        time = datetime.datetime.now()
        today = (time.strftime("%A"))
        if today == "Sunday":
            print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
            print("      Mohon maaf, Shelter tutup pada hari Minggu      ")
            print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
        else:
            queue.enqueue(uname)
        print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
        input("          Klik ENTER untuk kembali ke menu           ")
        
    def menu2(self):
        Input = ""
        while (Input == ""):
            linkedHewan.head = linkedHewan.mergeSort(linkedHewan.head) #MergeSort
            linkedHewan.printList() #printList
            try:
                print("—————————————————————————————————————————————————————")
                pilihHewan = int(input("Masukkan pilihan: "))
                print("—————————————————————————————————————————————————————")
                index = pilihHewan - 1
                linkedHewan.getData(index) #print Data
                statusAdopt = linkedHewan.getStatus(index)
                if statusAdopt == "Open for adoption":
                    key = linkedHewan.searchKey(index) #get nama hewan
                    adopt = input("Apakah Anda tertarik untuk mengadopsi {}(ya/tidak)? ".format(key))
                    if adopt.lower() == "ya":
                        MenuUser.syaratAdopsi()
                        setuju = input("Apakah Anda bersedia memenuhi syarat tersebut(ya/tidak)? ")
                        if setuju.lower() == "ya":
                            linkedHewan.ubahStatus(index)
                            laporanAdopsi.append("{} mengajukan permintaan adopsi untuk {}".format(uname, key))
                            print("—————————————————————————————————————————————————————")
                            print("        Permintaan adopsi Anda telah diajukan        ")
                            print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
                            print("     Selanjutnya silakan mengunjungi shelter untuk   ")
                            print("              melanjutkan proses adopsi              ")
                            break

                        else:
                            print("—————————————————————————————————————————————————————")
                            print("       Permintaan pengajuan adopsi dibatalkan        ")
                            print(" Silakan datang kembali apabila Anda berubah pikiran ")
                            break
                    else:
                        print("—————————————————————————————————————————————————————")
                        print(" Silakan datang kembali apabila Anda berubah pikiran ")
                        break
                    
                elif statusAdopt == "On adoption process" or statusAdopt == "Adopted":
                    key = linkedHewan.searchKey(index)
                    print("      {} saat ini tidak tersedia untuk diadopsi      ".format(key))
                    print("—————————————————————————————————————————————————————")
                    keluar = input("Apakah Anda ingin kembali ke menu(ya/tidak)? ")
                    print("—————————————————————————————————————————————————————")
                    if keluar.lower() == "ya":
                        break
                else:
                    print("    Silakan pilih berdasarkan nomor yang tersedia    ")
                    print("—————————————————————————————————————————————————————")
                    
            except ValueError :
                print("—————————————————————————————————————————————————————")
                print("                Pilihan tidak tersedia               ")
                print("   Silakan pilih berdasarkan nomor yang tersedia     ")
        print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
        Input = input("          Klik ENTER untuk kembali ke menu           ")


    def menu3(self):
        global nominalDonasi
        global totalDonasi
        print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
        print("               k o t a k   d o n a s i               ")         
        print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
        while True:
            try:
                print("Silakan masukkan nominal donasi yang Anda inginkan")
                nominalDonasi = int(input(" Donate: Rp. "))
                if nominalDonasi > 5000:
                    totalDonasi = int(totalDonasi + nominalDonasi)
                    laporanDonasi.append("{} baru saja berdonasi senilai Rp. {}".format(uname, nominalDonasi))
                    print("—————————————————————————————————————————————————————")
                    print("        Terimakasih atas support dan donasinya       ")
                    print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
                    break
                else:
                    print("")
                    print("        Batas minimal donasi yakni, Rp. 5000         ")
                    print("—————————————————————————————————————————————————————")
                    lanjut = input("Apakah Anda ingin melanjutkan donasi(ya/tidak)? ")
                    print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
                    if lanjut.lower() != "ya":
                        break
            except ValueError :
                print("—————————————————————————————————————————————————————")
                print("   Mohon hanya memasukkan angka nominal setelah Rp.  ")
                print("   Example: Rp. 100000")
                print("—————————————————————————————————————————————————————")
                lanjut = input("Apakah Anda ingin melanjutkan donasi(ya/tidak)? ")
                print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
                if lanjut.lower() != "ya":
                    break
        input("          Klik ENTER untuk kembali ke menu           ")


    def syaratAdopsi(self):
        print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
        print("        s y a r a t   a d o p s i   h e w a n         ")         
        print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
        print(" 1. Calon adopter minimal telah berusia 18 tahun dan")
        print("    sanggung bertanggung jawab atas hewan adopsi")
        print(" 2. Adopter wajib memberikan dasar hidup yang layak")
        print("    kepada hewan adopsi")
        print(" 3. Adopter dilarang memindahtangankan/menjual hewan")
        print("    adopsi tanpa sepengetahuan dan izin dari shelter")
        print(" 4. Adopter wajib melaporkan keadaan hewan adopsi")
        print("    minimal 1 tahun sekali kepada pihak shelter")
        print(" 5. Shelter berhak melakukan pengecekkan langsung ")
        print("    terhadap hewan yang telah diadopsi")
        print(" 6. Apabila hewan ditemui dalam keadaan yang tidak ")
        print("    sepatutnya maka shelter berhak menarik kembali")
        print("    hewan tersebut ke dalam perlindungan kami")
        print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
                
            
#============================================MENU ADMIN===================================================
class MenuAdmin:
    def loginAdmin(self):
        print("—————————————————————————————————————————————————————")
        print("Silakan masukkan username dan password admin")
        unameAdm = input("Username: ")
        passAdm = input("Password: ")
        if unameAdm == "admin" and passAdm == "adm123":
            return True
        else:
            print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
            print("                     LOGIN GAGAL                     ")            
            print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
            input("        Klik ENTER untuk kembali ke menu login       ")
            return False

    def menu1(self):
        global loginAdm
        Menu1 = True
        while Menu1 == True:
            checkQ = queue.isEmpty()
            if checkQ == True:
                print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
                print("             a n t r e a n   k o s o n g             ")
                print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
                print("—————————————————————————————————————————————————————")
                Menu1 = False
                loginAdm = True
                input("          Klik ENTER untuk kembali ke menu           ")

            elif checkQ == False:
                queue.printQueue()
                print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
                print(" In service      : {}".format(queue.first()))
                print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
                print("             n a v i g a s i   m e n u 1             ")
                print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
                print(" 1. Urai antrean (dequeue)")
                print(" 2. Kembali ke menu utama")
                print("—————————————————————————————————————————————————————")
                pilih = input("Masukkan pilihan: ")
                if pilih == "1":
                    queue.dequeue()
                    print("—————————————————————————————————————————————————————")
                    print("              Antrian telah diperbarui               ")

                elif pilih == "2":
                    Menu1 = False
                    loginAdm = True
                    print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
                    input("          Klik ENTER untuk kembali ke menu           ")


    def menu2(self):
        if len(laporanAdopsi) == 0 and len(laporanDonasi) == 0:
             print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
             print("             l a p o r a n   k o s o n g             ")
             print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
             print("—————————————————————————————————————————————————————")

        else:
            if len(laporanAdopsi) >= 1:
                print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
                print("             l a p o r a n   a d o p s i             ")
                print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
                nomor = 1
                for i in laporanAdopsi:
                    print(" {}. {}".format(nomor, i))
                    nomor += 1
                    print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
                print("—————————————————————————————————————————————————————")

            if len(laporanDonasi) >= 1:
                print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
                print("             l a p o r a n   d o n a s i             ")
                print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
                nomor = 1
                for i in laporanDonasi:
                    print(" {}. {}".format(nomor, i))
                    nomor += 1
                    print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
                    
                print("     Total donasi: {}".format(totalDonasi))
                print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
                print("—————————————————————————————————————————————————————")
        input("          Klik ENTER untuk kembali ke menu           ")
                
                          
    def menu3(self):
        kembali = False
        while kembali == False:
            linkedHewan.head = linkedHewan.mergeSort(linkedHewan.head) #MergeSort
            linkedHewan.printList() #printList
            try:
                print("—————————————————————————————————————————————————————")
                pilihHewan = int(input("Masukkan pilihan: "))
                print("—————————————————————————————————————————————————————")
                index = pilihHewan - 1
                dataHewan = linkedHewan.getData(index) #print Data
                if dataHewan != False:
                    print("—————————————————————————————————————————————————————")
                    updateData = input("Ketik 'ya' jika Anda ingin megubah data: ")
                    print("—————————————————————————————————————————————————————")
                    if updateData.lower() == "ya":
                        linkedHewan.updateData(index)
                kembaliMenu = input("Apakah Anda ingin kembali ke menu(ya/tidak)? ")
                print("—————————————————————————————————————————————————————")
                if kembaliMenu.lower() == "ya":
                    input("          Klik ENTER untuk kembali ke menu           ")
                    kembali = True
                else:
                    pass
 
            except ValueError :
                print("—————————————————————————————————————————————————————")
                print("                Pilihan tidak tersedia               ")
                print("—————————————————————————————————————————————————————")
                kembaliMenu = input("Apakah Anda ingin kembali ke menu(ya/tidak)? ")
                print("—————————————————————————————————————————————————————")
                if kembaliMenu.lower() == "ya":
                    input("          Klik ENTER untuk kembali ke menu           ")
                    kembali = True
                else:
                    pass
            


    def menu4(self):
        menu3 = True
        print("Silakan melengkapi data-data berikut: ")
        while menu3 == True:
            namaBaru = input("Nama   : ")
            dups = linkedHewan.checkDups(namaBaru.lower())
            if dups == True:
                print("Nama sudah terpakai, silakan coba nama lain")
            elif dups == False:
                namaBaru = namaBaru.capitalize()
                linkedHewan.newDataForm(namaBaru)
                print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
                input("          Klik ENTER untuk kembali ke menu           ")
                menu3 = False
                

    def menu5(self):
        cariNama = input("Masukkan nama Hewan yang ingin dicari: ")
        print("—————————————————————————————————————————————————————")
        linkedHewan.head = linkedHewan.mergeSort(linkedHewan.head)
        listArray = linkedHewan.makeList()
        n = len(listArray)
        index = int(jumpSearch(listArray , cariNama , n ))
        if index == -1:
            print("—————————————————————————————————————————————————————")  
            print("    Data hewan dengan nama {} tidak ditemukan".format(cariNama))
        else:
            printDict(listArray, index)
        input("          Klik ENTER untuk kembali ke menu           ")
        

    def menu6(self):
        linkedHewan.head = linkedHewan.mergeSort(linkedHewan.head) #MergeSort
        linkedHewan.printList() #printList
        try:
            print("—————————————————————————————————————————————————————")
            pilihHewan = int(input("Masukkan pilihan: "))
            index = pilihHewan - 1
            key = linkedHewan.searchKey(index)
            if key != None:
                print("—————————————————————————————————————————————————————")
                confirm = input("Yakin ingin menghapus data {}(ya/tidak)? ".format(key))
                print("—————————————————————————————————————————————————————")
                if confirm.lower() == "ya":
                    linkedHewan.deleteNode(key)
                    print("               Data berhasil di hapus")
                else:
                    print("             Penghapusan data dibatalkan")
        except ValueError :
                    print("—————————————————————————————————————————————————————")
                    print("                Pilihan tidak tersedia               ")
        print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
        input("          Klik ENTER untuk kembali ke menu           ")


def printLogOut():
    print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
    print("                Thank you for coming                 ")
    print("                   See you around!                   ")
    print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
    
#====SHORTCUT CLASS===================================================================================================
linkedHewan = LinkedHewan()
linkedUser = LinkedUser()
MenuAdmin = MenuAdmin()
MenuUser = MenuUser()
queue = Queue()

#========================================DATA HEWAN=========================================
linkedHewan.addLast("Luna", "Cat", "Female", "1-2 years old", "Shorthair/Domestic", "Red",
               "Black", "Vaccinated", "Behaved, smart, would turn you into a sailor scout",
               "Open for adoption")

linkedHewan.addLast("Artemis", "Cat", "Male", "1-2 years old", "Shorthair/Domestic", "Blue",
               "White", "Vaccinated", "Simp, can work as your sidekick",
               "Open for adoption")

linkedHewan.addLast("Orenee", "Cat", "Male", "Less than 1 year old", "Shorthair/Domestic", "Oren", "Oren",
        "Vaccinated", "Nakal, barbar, lincah, kadang manis", "Open for adoption")

linkedHewan.addLast("Hachi", "Dog", "Male", "5++ years old","Akita Inu", "Brown","White", "Vaccinated",
                   "Loyal, would sits all day long in front of your house door until you're back from work",
                   "Open for adoption")

linkedHewan.addLast("Dobby", "Dog", "Male","3-4 years old","American Pit Bull Terrier","Brown",
                   "Brown - Tan","Vaccinated","Trained as a guard dog, spoiled, active, obedient",
                   "Open for adoption")

#============================================================ M A I N ============================================================

    #========================MENU LOGIN===========================
pilihLogin = False
while pilihLogin == False:
    print("—————————————————————————————————————————————————————")
    print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
    print("                 M E N U   L O G I N                 ")
    print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
    print("—————————————————————————————————————————————————————")
    print(" 1. Login sebagai user")
    print(" 2. Login sebagai admin")
    print(" 3. Registrasi akun")
    print(" 4. Keluar")
    print("—————————————————————————————————————————————————————")
    pilihLogin = input("Masukkan pilihan: ")
    print("—————————————————————————————————————————————————————")

    #========================LOGIN USER & MENU USER===========================
    if pilihLogin == "1":
        print("                 L O G I N   U S E R                 ")
        loginU = linkedUser.loginUser()
        
        if loginU == False:
            print("—————————————————————————————————————————————————————")
            input("        Klik ENTER untuk kembali ke menu login        ")
            pilihLogin = False
            
        while loginU == True:
            print("—————————————————————————————————————————————————————")
            print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
            print("                     M  E  N  U                      ")
            print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
            print("—————————————————————————————————————————————————————")
            print(" 1. Ambil antrean kunjungan")
            print(" 2. Lihat data hewan untuk diadopsi")
            print(" 3. Donasi")
            print(" 4. Log out")
            print("—————————————————————————————————————————————————————")
            pilihMenu = input("Masukkan pilihan: ")
            print("—————————————————————————————————————————————————————")

            if pilihMenu == "1":
                MenuUser.menu1()

            elif pilihMenu == "2":
                MenuUser.menu2()

            elif pilihMenu == "3":
                MenuUser.menu3()
            
            elif pilihMenu == "4":
                printLogOut()
                loginU = False
                pilihLogin = False

            else:
                print("               Pilihan tidak tersedia               ")


    #========================LOGIN ADMIN & MENU ADMIN===========================
    elif pilihLogin == "2":
        print("                L O G I N   A D M I N                ")
        loginAdm = MenuAdmin.loginAdmin()
        if loginAdm == False:
            pilihLogin = False
            
        while loginAdm == True:
            print("—————————————————————————————————————————————————————")
            print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
            print("                     M  E  N  U                      ")
            print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
            print("—————————————————————————————————————————————————————")
            print(" 1. Lihat antrean kunjungan")
            print(" 2. Lihat laporan")
            print(" 3. Lihat dan/atau ubah data hewan")
            print(" 4. Tambah data hewan baru")
            print(" 5. Cari data hewan")
            print(" 6. Hapus hewan dari data")
            print(" 7. Log out")
            print("—————————————————————————————————————————————————————")
            pilihMenu = input("Masukkan pilihan: ")
            print("—————————————————————————————————————————————————————")
            if pilihMenu == "1":
                MenuAdmin.menu1()

            elif pilihMenu == "2":
                MenuAdmin.menu2()

            elif pilihMenu == "3":
                MenuAdmin.menu3()

            elif pilihMenu == "4":
                MenuAdmin.menu4()

            elif pilihMenu == "5":
                MenuAdmin.menu5()

            elif pilihMenu == "6":
                MenuAdmin.menu6()

            elif pilihMenu == "7":
                printLogOut()
                loginAdm = False
                pilihLogin = False  
            else:
                print("               Pilihan tidak tersedia               ")
                
   
    #=============================REGIS AKUN============================ 
    elif pilihLogin == "3":
        print("                 R E G I S T R A S I                 ")
        linkedUser.regisUser()
        pilihLogin = False

    elif pilihLogin == "4":
        printLogOut()
        exit()
        break
    
        
    else:
        pilihLogin = False
        print("                Pilihan tidak tersedia               ")
        print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
        input("        Klik ENTER untuk kembali ke menu logi        ")
