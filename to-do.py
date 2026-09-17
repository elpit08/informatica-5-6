def main():
    to_do = []
    print("Write the task you have to do, press enter to write the a new task")
    listobject = ""

    while True:
        command = input("What do you wan to do? (add, complete, exit): ")

        if command == 'add':
            numbertask = int(input("how many task you want to add: "))
            taskwriten = 0
            while taskwriten < numbertask:

                listobject = input("write a task: ")
                to_do.append(listobject)
                taskwriten +=1

        if command == 'complete':
            print(len(to_do))
            print(to_do)
            completed_tasks = int(input("How many task did you complete: "))
            
            while

            complete = input("What task did you complete: ")
            to_do.remove(complete)

        if command == 'exit':
            break






if __name__=="__main__":
    main()
