# menu function based on match case format

def menu():
    # Display options with numerics
    # take input for integers
    # assign integers to func calls
    # use switch cases to assign for this
    print(" TASK ACTION SELECTION MENU : \n     1. Add a new task \n     2. Update the status of an existing task \n     3. Delete an existing task \n     4. List all tasks  ")
    optionNumber= int(input("\n Please enter the number for your action : "))
    

    
    # match optionNumber:

    #     case 1 :
    #         add_task()

    #     case 2 : 
    #         update_task()

    #     case 3 :
    #         delete_task()

    #     case 4 :
    #         list_task()

        # case _:
            # print("Please select an appropriate option ")



def main():
    print(" Task Manager - am pushing to main ")
    menu()

if __name__ == "__main__":
    main()  

