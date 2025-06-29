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
  



# menu function based on match case format

def menu():
    # Display options with numerics
    # take input for integers
    # assign integers to func calls
    # use switch cases to assign for this
    print(" TASK ACTION SELECTION MENU : \n     1. Add a new task \n     2. Update the status of an existing task \n     3. Delete an existing task \n     4. List all tasks  ")
    optionNumber= int(input("\n Please enter the number for your action : "))
    

    
    match optionNumber:

        case 1 :
            add_task()

    #     case 2 : 
    #         update_task()

    #     case 3 :
    #         delete_task()

        case 4 :
            list_task()

        # case _:
            # print("Please select an appropriate option ")



def main():
    print(" Task Manager  ")
    menu()

if __name__ == "__main__":
    main()  

