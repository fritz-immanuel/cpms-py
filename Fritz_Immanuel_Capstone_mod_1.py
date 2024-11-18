import os, re

projectStatuses = ["Canceled", "In Progress", "Completed"]
clientTypes = ["Individual", "Business"]

def validateClientCode(cc: str)->bool:
  pattern = r"^CL\d{3}$"

  if re.match(pattern, cc):
    return True

  return False

def validateProjectCode(cc: str)->bool:
  pattern = r"^PR\d{3}$"

  if re.match(pattern, cc):
    return True

  return False

clientStorage = {
  "CL001": {
    "Name": "John Doe",
    "Address": "123 Main Street, New York, NY 10001",
    "PhoneNumber": "(123) 456-7890",
    "Email": "johndoe@example.com",
    "Type": 0,
  },
}

projectStorage = {
  "PR001": {
    "Name": "Project 1",
    "Description": "A simple web app for managing clients",
    "TimeRequired": "4 hours",
    "ProjectValue": "$1000",
    "Client": "CL001",
    "Status": 1,
  },
}

def main():
  while True:
    os.system('cls')
    showMainMenu()
    menuChoice = input("Enter your choice [1-3]: ")
    if menuChoice == "1":
      clientList()
    elif menuChoice == "2":
      projectList()
    elif menuChoice == "3":
      print("Shutting Down...")
      break
    else:
      print("Invalid input! Press 'Enter' to try again....")
      input()

def showMainMenu():
  print("==========================================")
  print("+   Client - Project Management System   +")
  print("==========================================")
  print("1. Client List")
  print("2. Project List")
  print("3. Exit")

# Client

def showClientList(data = clientStorage):
  print("Client List")
  print("=================================================================================================================================================")
  print("| No |  Code  |          Name         |                 Address                 |     Phone Number     |           Email           |    Type    |")
  print("=================================================================================================================================================")

  if len(data) == 0:
    print("                                                             - No Data -")

  for id, client in enumerate(data):
    print(f"| {id+1:<2} | {client:<6} | {data[client]['Name']:<21} | {data[client]['Address']:<39} | {data[client]['PhoneNumber']:<20} | {data[client]['Email']:<25} | {clientTypes[data[client]['Type']]:<10} |")
  print("=================================================================================================================================================")

  print()

def clientList():
  while True:
    os.system('cls')

    showClientList()

    print("1. Add a new Client")
    print("2. Edit an existing Client")
    print("3. Delete an existing Client")
    print("4. Return to Main Menu")
    print("5. Exit the program")

    clientListInput = input("What would you like to do? [1-5]: ")
    if clientListInput == "1":
      addClient()
    elif clientListInput == "2":
      editClient()
    elif clientListInput == "3":
      deleteClient()
    elif clientListInput == "4":
      break
    elif clientListInput == "5":
      print("Shutting Down...")
      exit()
    else:
      print("Invalid input! Press 'Enter' to try again....")
      input()

def addClient():
  isNotExit = True

  newDataStorage = {}

  while isNotExit:
    os.system('cls')

    print("Add a new Client")
    print()

    while True:
      newClientCode = input("Enter the code [CLXXX][X = digit]: ")
      if not validateClientCode(newClientCode):
        print("Invalid client code!")
      elif clientStorage.get(newClientCode) or newDataStorage.get(newClientCode):
        print("Client code already exists!")
      else:
        newDataStorage[newClientCode] = {}
        break

    while True:
      newClientName = input("Enter the name [5-20 chars]: ")
      if len(newClientName) < 5 or len(newClientName) > 20:
        print("Name must be between 5 and 20 characters!")
        input("Press 'Enter' to try again....")
        continue
      else:
        newDataStorage[newClientCode]["Name"] = newClientName
        break

    while True:
      newClientAddress = input("Enter the address [5-39 chars]: ")
      if len(newClientAddress) < 5 or len(newClientAddress) > 39:
        print("Address must be between 5 and 39 characters!")
        input("Press 'Enter' to try again....")
        continue
      else:
        newDataStorage[newClientCode]["Address"] = newClientAddress
        break

    while True:
      newClientPhoneNumber = input("Enter the phone number [10-20 chars]: ")
      if len(newClientPhoneNumber) < 10 or len(newClientPhoneNumber) > 20:
        print("Phone number must be between 10 and 20 characters!")
        input("Press 'Enter' to try again....")
        continue
      else:
        newDataStorage[newClientCode]["PhoneNumber"] = newClientPhoneNumber
        break

    while True:
      newClientEmail = input("Enter the email [5-25 chars]: ")
      if len(newClientEmail) < 5 or len(newClientEmail) > 25:
        print("Email must be between 5 and 25 characters!")
        input("Press 'Enter' to try again....")
        continue
      else:
        newDataStorage[newClientCode]["Email"] = newClientEmail
        break

    while True:
      newClientType = input("Enter the client type (0 = individual, 1 = business): ")
      if newClientType not in ["0", "1"]:
        input("Invalid input! Press 'Enter' to try again....")
      else:
        newDataStorage[newClientCode]["Type"] = int(newClientType)
        break

    while True:
      addAnotherClient = input("Do you want to add another client? [y/n]: ")
      if addAnotherClient.lower() == "y":
        break
      elif addAnotherClient.lower() == "n":
        isNotExit = False
        while True:
          showClientList(newDataStorage)
          saveDataConfirm = input("Do you want to save all clients? [y/n]: ")
          if saveDataConfirm.lower() == "y":
            clientStorage.update(newDataStorage)
            print("Client saved successfully!")
            break
          elif saveDataConfirm.lower() == "n":
            newDataStorage = {}
            print("Client not saved!")
            input("Press 'Enter' to return to Client List....")
            break
          else:
            input("Invalid input! Press 'Enter' to try again....")
        break
      else:
        input("Invalid input! Press 'Enter' to try again....")

def editClient():
  isNotExit = True
  updatedClientStorage = {}

  while isNotExit:
    os.system('cls')

    print("Edit an existing Client")
    print()

    showClientList()

    while True:
      updateClientCode = input("Enter the client code to update [CLXXX][X = digit]: ")
      if not validateClientCode(updateClientCode):
        print("Invalid client code!")
      elif clientStorage.get(updateClientCode):
        updatedClientStorage[updateClientCode] = {}
        break
      else:
        print("Client code does not exists!")

    while True:
      updateClientName = input(f"Enter the name [5-20 chars] [{clientStorage[updateClientCode]['Name']}]: ")
      if len(updateClientName) < 5 or len(updateClientName) > 20:
        print("Name must be between 5 and 20 characters!")
        input("Press 'Enter' to try again....")
        continue
      else:
        updatedClientStorage[updateClientCode]["Name"] = updateClientName
        break

    while True:
      updateClientAddress = input(f"Enter the address [5-39 chars] [{clientStorage[updateClientCode]['Address']}]: ")
      if len(updateClientAddress) < 5 or len(updateClientAddress) > 39:
        print("Address must be between 5 and 39 characters!")
        input("Press 'Enter' to try again....")
        continue
      else:
        updatedClientStorage[updateClientCode]["Address"] = updateClientAddress
        break

    while True:
      updateClientPhoneNumber = input(f"Enter the phone number [10-20 chars] [{clientStorage[updateClientCode]['PhoneNumber']}]: ")
      if len(updateClientPhoneNumber) < 10 or len(updateClientPhoneNumber) > 20:
        print("Phone number must be between 10 and 20 characters!")
        input("Press 'Enter' to try again....")
        continue
      else:
        updatedClientStorage[updateClientCode]["PhoneNumber"] = updateClientPhoneNumber
        break

    while True:
      updateClientEmail = input(f"Enter the email [5-25 chars] [{clientStorage[updateClientCode]['Email']}]: ")
      if len(updateClientEmail) < 5 or len(updateClientEmail) > 25:
        print("Email must be between 5 and 25 characters!")
        input("Press 'Enter' to try again....")
        continue
      else:
        updatedClientStorage[updateClientCode]["Email"] = updateClientEmail
        break

    while True:
      updateClientType = input(f"Enter the client type (0 = individual, 1 = business) [{clientStorage[updateClientCode]['Type']}]: ")
      if updateClientType not in ["0", "1"]:
        input("Invalid input! Press 'Enter' to try again....")
      else:
        updatedClientStorage[updateClientCode]["Type"] = int(updateClientType)
        break

    while True:
      updateAnotherClient = input("Do you want to update another client? [y/n]: ")
      if updateAnotherClient.lower() == "y":
        break
      elif updateAnotherClient.lower() == "n":
        isNotExit = False
        while True:
          showClientList(updatedClientStorage)
          saveDataConfirm = input("Do you want to save updates? [y/n]: ")
          if saveDataConfirm.lower() == "y":
            clientStorage.update(updatedClientStorage)
            print("Client saved successfully!")
            break
          elif saveDataConfirm.lower() == "n":
            updatedClientStorage = {}
            print("Client not saved!")
            input("Press 'Enter' to return to Client List....")
            break
          else:
            input("Invalid input! Press 'Enter' to try again....")
        break
      else:
        input("Invalid input! Press 'Enter' to try again....")

def deleteClient():
  isNotExit = True

  while isNotExit:
    os.system('cls')

    print("Delete an existing Client")
    print()

    showClientList()

    deleteClientCode = ""

    while True:
      deleteClientCode = input("Enter the client code to delete [CLXXX][X = digit]: ")
      if not validateClientCode(deleteClientCode):
        print("Invalid client code!")
      elif clientStorage.get(deleteClientCode):
        break
      else:
        print("Client code does not exists!")

    while True:
      saveDataConfirm = input("Are you sure you want to delete this client? [y/n]: ")
      if saveDataConfirm.lower() == "y":
        del clientStorage[deleteClientCode]
        print("Client deleted successfully!")
        input("Press 'Enter' to continue....")
        break
      elif saveDataConfirm.lower() == "n":
        deleteClientCode = ""
        print("Client not deleted!")
        input("Press 'Enter' to continue....")
        break
      else:
        input("Invalid input! Press 'Enter' to try again....")

    if len(clientStorage) == 0:
      isNotExit = False
    else:
      while True:
        deleteAnotherClient = input("Do you want to delete another client? [y/n]: ")
        if deleteAnotherClient.lower() == "y":
          break
        elif deleteAnotherClient.lower() == "n":
          isNotExit = False
          break
        else:
          input("Invalid input! Press 'Enter' to try again....")


# Project

def showProjectList(data = projectStorage, status = -1):
  print("Project List")
  print("=======================================================================================================================================================")
  print("| No |  Code  | Client |              Name              |                  Description                  | Time Required | Project Value |    Status   |")
  print("=======================================================================================================================================================")

  if len(data) == 0:
    print("                                                                     - No Data -")


  for id, project in enumerate(data):
    if status != -1 and data[project]['Status'] != status:
      continue
    print(f"| {id+1:<2} | {project:<6} | {data[project]["Client"]:<6} | {data[project]['Name']:<30} | {data[project]['Description']:<45} | {data[project]['TimeRequired']:<13} | {data[project]['ProjectValue']:<13} | {projectStatuses[data[project]['Status']]:<10} |")
  print("=======================================================================================================================================================")

  print()

def projectList():
  while True:
    os.system('cls')

    showProjectList()

    print("1. Add a new Project")
    print("2. Edit an existing Project")
    print("3. Delete an existing Project")
    print("4. Return to Main Menu")
    print("5. Exit the program")

    projectListInput = input("What would you like to do? [1-5]: ")
    if projectListInput == "1":
      addProject()
    elif projectListInput == "2":
      editProject()
    elif projectListInput == "3":
      deleteProject()
    elif projectListInput == "4":
      break
    elif projectListInput == "5":
      print("Shutting Down...")
      exit()
    else:
      print("Invalid input! Press 'Enter' to try again....")
      input()

def addProject():
  isNotExit = True

  newDataStorage = {}

  while isNotExit:
    os.system('cls')

    print("Add a new Project")
    print()

    # code
    while True:
      newProjectCode = input("Enter the code [PRXXX][X = digit]: ")
      if not validateProjectCode(newProjectCode):
        print("Invalid project code!")
      elif projectStorage.get(newProjectCode) or newDataStorage.get(newProjectCode):
        print("Project code already exists!")
      else:
        newDataStorage[newProjectCode] = {}
        break

    # client code
    while True:
      newProjectClientCode = input("Enter the Client code [CLXXX][X = digit]: ")
      if not validateClientCode(newProjectClientCode):
        print("Invalid Client code!")
      elif not clientStorage.get(newProjectClientCode):
        print("Client code doesnt exist!")
      else:
        newDataStorage[newProjectCode]["Client"] = newProjectClientCode
        break

    # name
    while True:
      newProjectName = input("Enter the name [5-30 chars]: ")
      if len(newProjectName) < 5 or len(newProjectName) > 30:
        print("Name must be between 5 and 30 characters!")
        input("Press 'Enter' to try again....")
        continue
      else:
        newDataStorage[newProjectCode]["Name"] = newProjectName
        break

    # description
    while True:
      newProjectDescription = input("Enter the description [5-45 chars]: ")
      if len(newProjectDescription) < 5 or len(newProjectDescription) > 45:
        print("Description must be between 5 and 39 characters!")
        input("Press 'Enter' to try again....")
        continue
      else:
        newDataStorage[newProjectCode]["Description"] = newProjectDescription
        break

    # time required
    while True:
      newProjectTimeRequired = input("Enter the Time Required [3-10 chars] [XXX days| weeks | months] [X = digit (1-999)]: ")
      if not re.match("^\d{1,3} (days|weeks|months)$", newProjectTimeRequired):
        print("Invalid input!")
      elif len(newProjectTimeRequired) < 3 or len(newProjectTimeRequired) > 10:
        print("Time Required must be between 3 and 10 characters!")
        input("Press 'Enter' to try again....")
        continue
      else:
        newDataStorage[newProjectCode]["TimeRequired"] = newProjectTimeRequired
        break

    # value
    while True:
      newProjectValue = input("Enter the Project Value [5-13 chars]: ")
      if len(newProjectValue) < 5 or len(newProjectValue) > 13:
        print("Email must be between 5 and 13 characters!")
        input("Press 'Enter' to try again....")
        continue
      else:
        newDataStorage[newProjectCode]["ProjectValue"] = newProjectValue
        break

    # status
    while True:
      newProjectStatus = input("Enter the project status (0 = Canceled, 1 = In Progress, 2 = Completed): ")
      if newProjectStatus not in ["0","1","2"]:
        input("Invalid input! Press 'Enter' to try again....")
      else:
        newDataStorage[newProjectCode]["Status"] = int(newProjectStatus)
        break

    while True:
      addAnotherProject = input("Do you want to add another project? [y/n]: ")
      if addAnotherProject.lower() == "y":
        break
      elif addAnotherProject.lower() == "n":
        isNotExit = False
        while True:
          showProjectList(newDataStorage)
          saveDataConfirm = input("Do you want to save all projects? [y/n]: ")
          if saveDataConfirm.lower() == "y":
            projectStorage.update(newDataStorage)
            print("Project saved successfully!")
            break
          elif saveDataConfirm.lower() == "n":
            newDataStorage = {}
            print("Project not saved!")
            input("Press 'Enter' to return to Project List....")
            break
          else:
            input("Invalid input! Press 'Enter' to try again....")
        break
      else:
        input("Invalid input! Press 'Enter' to try again....")

def editProject():
  isNotExit = True
  updatedDataStorage = {}

  while isNotExit:
    os.system('cls')

    print("Update an existing Project")
    print()

    showProjectList()

    # code
    while True:
      updatedProjectCode = input("Enter the code [PRXXX][X = digit]: ")
      if not validateProjectCode(updatedProjectCode):
        print("Invalid project code!")
      elif projectStorage.get(updatedProjectCode):
        updatedDataStorage[updatedProjectCode] = {}
        break
      else:
        print("Project code does not exists!")

    # client code
    while True:
      newProjectClientCode = input("Enter the Client code [CLXXX][X = digit]: ")
      if not validateClientCode(newProjectClientCode):
        print("Invalid Client code!")
      elif not clientStorage.get(newProjectClientCode):
        print("Client code doesnt exist!")
      else:
        updatedDataStorage[updatedProjectCode]["Client"] = newProjectClientCode
        break

    # name
    while True:
      updatedProjectName = input("Enter the name [5-30 chars]: ")
      if len(updatedProjectName) < 5 or len(updatedProjectName) > 30:
        print("Name must be between 5 and 30 characters!")
        input("Press 'Enter' to try again....")
        continue
      else:
        updatedDataStorage[updatedProjectCode]["Name"] = updatedProjectName
        break

    # description
    while True:
      updatedProjectDescription = input("Enter the description [5-45 chars]: ")
      if len(updatedProjectDescription) < 5 or len(updatedProjectDescription) > 45:
        print("Description must be between 5 and 39 characters!")
        input("Press 'Enter' to try again....")
        continue
      else:
        updatedDataStorage[updatedProjectCode]["Description"] = updatedProjectDescription
        break

    # time required
    while True:
      updatedProjectTimeRequired = input("Enter the Time Required [3-10 chars] [XXX days| weeks | months] [X = digit (1-999)]: ")
      if not re.match("^\d{1,3} (days|weeks|months)$", updatedProjectTimeRequired):
        print("Invalid input!")
      elif len(updatedProjectTimeRequired) < 3 or len(updatedProjectTimeRequired) > 10:
        print("Time Required must be between 3 and 13 characters!")
        input("Press 'Enter' to try again....")
        continue
      else:
        updatedDataStorage[updatedProjectCode]["TimeRequired"] = updatedProjectTimeRequired
        break

    # value
    while True:
      updatedProjectValue = input("Enter the Project Value [5-13 chars]: ")
      if len(updatedProjectValue) < 5 or len(updatedProjectValue) > 13:
        print("Email must be between 5 and 13 characters!")
        input("Press 'Enter' to try again....")
        continue
      else:
        updatedDataStorage[updatedProjectCode]["ProjectValue"] = updatedProjectValue
        break

    # status
    while True:
      updatedProjectStatus = input("Enter the project status (0 = Canceled, 1 = In Progress, 2 = Completed): ")
      if updatedProjectStatus not in ["0","1","2"]:
        input("Invalid input! Press 'Enter' to try again....")
      else:
        updatedDataStorage[updatedProjectCode]["Status"] = int(updatedProjectStatus)
        break

    while True:
      updateAnotherProject = input("Do you want to update another project? [y/n]: ")
      if updateAnotherProject.lower() == "y":
        break
      elif updateAnotherProject.lower() == "n":
        isNotExit = False
        while True:
          showProjectList(updatedDataStorage)
          saveDataConfirm = input("Do you want to save all projects? [y/n]: ")
          if saveDataConfirm.lower() == "y":
            projectStorage.update(updatedDataStorage)
            print("Project saved successfully!")
            break
          elif saveDataConfirm.lower() == "n":
            updatedDataStorage = {}
            print("Project not saved!")
            input("Press 'Enter' to return to Project List....")
            break
          else:
            input("Invalid input! Press 'Enter' to try again....")
        break
      else:
        input("Invalid input! Press 'Enter' to try again....")

def deleteProject():
  isNotExit = True

  while isNotExit:
    os.system('cls')

    print("Delete an existing Project")
    print()

    print("1. Delete an existing Project by Project Code")
    print("2. Delete an existing Project by Client Code")
    print("3. Delete an existing Project by Status")
    print("4. Return to Project Menu")
    inputCreateMenu = input("What would you like to do? [1-4]: ")
    if inputCreateMenu == "1":
      os.system('cls')
      showProjectList()

      deleteProjectCode = ""

      while True:
        deleteProjectCode = input("Enter the project code to delete [PRXXX][X = digit]: ")
        if not validateProjectCode(deleteProjectCode):
          print("Invalid project code!")
        elif projectStorage.get(deleteProjectCode):
          break
        else:
          print("Project code does not exists!")


      deleteDataConfirm = input("Do you want to delete this project? [y/n]: ")
      if deleteDataConfirm.lower() == "y":
        del projectStorage[deleteProjectCode]
        print("Project deleted successfully!")
        input("Press 'Enter' to continue....")
      else:
        deleteProjectCode = ""
        print("Project not deleted!")
        input("Press 'Enter' to return to Project List....")
    elif inputCreateMenu == "2":
      os.system('cls')
      showProjectList()

      deleteProjectCode = []

      while True:
        deleteClientCode = input("Enter the client code to delete [CLXXX][X = digit]: ")
        if not validateClientCode(deleteClientCode):
          print("Invalid client code!")
        elif clientStorage.get(deleteClientCode):
          for projectCode in projectStorage:
            if projectStorage[projectCode]["Client"] == deleteClientCode:
              deleteProjectCode.append(projectCode)
          break
        else:
          print("Client code does not exists!")

      deleteDataConfirm = input("Do you want to delete this project? [y/n]: ")
      if deleteDataConfirm.lower() == "y":
        for projectCode in deleteProjectCode:
          del projectStorage[projectCode]
        print("Project deleted successfully!")
        input("Press 'Enter' to continue....")
      else:
        deleteProjectCode = ""
        print("Project not deleted!")
        input("Press 'Enter' to return to Project List....")
    elif inputCreateMenu == "3":
      os.system('cls')

      while True:
        print("Delete Project by Status")
        print("1. Canceled")
        print("2. In Progress")
        print("3. Completed")
        inputDeleteStatus = input("What status would you like to delete? [1-3]: ")
        if inputDeleteStatus not in ["1","2","3"]:
          input("Invalid input! Press 'Enter' to try again....")
        else:
          break

      deleteProjectStatus = int(inputDeleteStatus)-1

      showProjectList(status=deleteProjectStatus)

      while True:
        deleteStatusValidation = input("Are you sure you want to delete all projects with this status? [y/n]: ")
        if deleteStatusValidation.lower() == "y":
          for projectCode in list(projectStorage):
            if projectStorage[projectCode]["Status"] == deleteProjectStatus:
              del projectStorage[projectCode]
          print("Project deleted successfully!")
          input("Press 'Enter' to continue....")
          break
        elif deleteStatusValidation.lower() == "n":
          input("Press 'Enter' to return to Project List....")
          isNotExit = False
          break
        else:
          input("Invalid input! Press 'Enter' to try again....")

    elif inputCreateMenu == "4":
      break
    else:
      input("Invalid input! Press 'Enter' to try again....")

main()