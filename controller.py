import json
import random 


def returnToMenu():
    Decision = input(" Do you want to return to main menu ( y/n ) ? ")

    if Decision == "y" :
        menu()

    elif Decision == "n":
        return
 



def add_task():
   
    taskname = input("Enter task name : \n" )
    # print(taskname)

    ID = random.randint(1000 , 9999)
    taskJson = {
        "id" : ID,  
        "task" : taskname,
        "status" : "pending"
    }

        
    try :

        with open("tasks.json", "r") as fobject:
            data = json.load(fobject)               # If task already exists this will look like -  <listOfDicts> [ {"task": "buy", "id": [2834], "status": "pending"} ]

         

    except FileNotFoundError:
        data = []               # if task does not exist - creating empty list

    data.append(taskJson)

    with open("tasks.json", "w") as fobject:
        json.dump(data, fobject)

   
    print("\n")
    returnToMenu()



def list_task():
    
    with open("tasks.json" , "r" ) as file:
        y = json.load(file)

    print(y)

    print("\n")
    returnToMenu()




# Purpose : Deletes a task by given ID
# Input : 1. task ID <Integer>
def delete_task (): 

    # 1. Read existing tasks from json file                                                        
    with open("tasks.json" , "r" ) as file:
        data = json.load(file)

    # 2. Check if there are any existing tasks, if not, deletion not allowed
    if data == None and not data:
        print("\n Warning - There are no tasks available for deletion \n")

    # 3. if tasksList exists, following logic
    else:   
        taskID = input("\n enter 4 digit id of task to be deleted : \n")

        #ListOfDicts = [ {"task": "buy", "id": [2834], "status": "pending"}, 
                    #{"task": "buy", "id": [2834], "status": "pending"} ]

    # 4. Check for given ID by traversing through list of tasks
        for item in data:
            print("type of taskID: " , type(taskID))
            
    # 5. If ID found in tasks list, delete that task
            if item['id'] == int(taskID):
                
                print("ID was found, deleting item now...")
                data.remove(item)
                
                print("\n Item here : ", item['id'])
                print(data)
           
                with open("tasks.json", "w") as fobject:
                    json.dump(data, fobject)

                print("\n")
                returnToMenu()    

    #5. If traversing completed and task not found, Print msg
        print("ID not found")
        
        print("\n")
        returnToMenu()

            


def update_task(): 

     # 1. Read existing tasks from json file                                                        
    with open("tasks.json" , "r" ) as file:
        data = json.load(file)

    # 2. Check if there are any existing tasks, if not, updating status not allowed
    if data == None and not data:
        print("\n Warning - There are no tasks available for updates \n")

    # 3. if tasksList exists, following logic
    else:   
        taskID = input("\n enter 4 digit id of task to be updated : \n")

        #ListOfDicts = [ {"task": "buy", "id": [2834], "status": "pending"}, 
                    #{"task": "buy", "id": [2834], "status": "pending"} ]

    # 4. Check for given ID by traversing through list of tasks
        for item in data:
            # print("type of taskID: " , type(taskID))
            
    # 5. If ID found in tasks list, update task status
            if item['id'] == int(taskID):

                statusInput = input( "enter status as pending/completed : " )
                item['status'] = statusInput

                print("\n Item here : ", item['status'])
                print(data)

    # 6. Write updated to json file
                with open("tasks.json", "w") as fobject:
                    json.dump(data, fobject)
                print("\n")
                returnToMenu()    

     #5. If traversing completed and task not found, Print msg
        print("ID not found")
        
        print("\n")
        returnToMenu()

   



# menu function based on match case format

def menu():
  
    print(" TASK ACTION SELECTION MENU : \n     1. Add a new task \n     2. Update the status of an existing task \n     3. Delete an existing task \n     4. List all tasks  ")
    optionNumber= int(input("\n Please enter the number for your action : "))
    

    
    match optionNumber:

        case 1 :
            add_task()

        case 2 : 
            update_task()

        case 3 :
            delete_task()

        case 4 :
            list_task()

        case _:
            print("Please select an appropriate option ")



def main():
    print(" Task Manager  ")
    menu()

if __name__ == "__main__":
    main()  

