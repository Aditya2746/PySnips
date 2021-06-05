""" Imports """
import os
from pathlib import Path
import datetime

def getTime():
    """ To Get the current time"""
    return datetime.datetime.now()
while True:
    def registerUser():
        """To Register a new user"""
        print("Register yourself, Already An User \"aau\"")
        username = input("Enter Username: ")
        if username == "aau":
            login()
            
        else:
            password = input("Enter Password: ")
            check_password = input("Repeat Password: ")
            if password == check_password:
                os.mkdir(f"C:\\Users\\Admin\\OneDrive\\Desktop\\aditya\\pythondir\\healthmanagementproj\\{username}")
                f = open(f"healthmanagementproj\\{username}\\password.txt", "w")
                creating_account = f.write(f"{password}")
                f.close()
                f1 = open(f"healthmanagementproj\\{username}\\exercise.txt", "w")
                creating_exercise = f1.write(f"")
                f1.close()
                f2 = open(f"healthmanagementproj\\{username}\\diet.txt", "w")
                creating_diet = f2.write(f"")
                f2.close()
                login()
            elif password != check_password:
                print("Your Password Didn't Match the old one")

    def login():
        """To give access to the their files to user"""
        print("Logging in yourself")
        username = input("Enter Username: ")
        user = Path(f"healthmanagementproj\\{username}")
        doesUserExists = user.exists()
        if doesUserExists:
            def getPassword():
                logindb = open(f"healthmanagementproj\{username}\password.txt", "r")
                gotPassword = logindb.read()
                logindb.close()
                return gotPassword.replace(" ", "")
            gotPassword = getPassword()
            password = input("Enter Password: ")
            if password == gotPassword:
                print("You are successfully logged in and now you have access to your exercise files")
                accessToFiles(username)

    def accessToFiles(user):
        """ To Give user access to their files """
        while True:
            filesIn = Path(f"healthmanagementproj\\{user}")
            whatToDo = input("You want to Add or to Get: ")
            if whatToDo == "get":
                toGet = input("To Get exercise 1 and for diet 2: ")            
                if toGet == "1":
                    exerciseFile = open(os.path.join(filesIn, "exercise.txt"), "r")
                    exercise = exerciseFile.read()
                    print(exercise)
                    exerciseFile.close()
                elif toGet == "2":
                    dietFile = open(os.path.join(filesIn, "diet.txt"), "r")
                    diet = dietFile.read()
                    print(diet)
                    dietFile.close()
            elif whatToDo == "add":
                toAdd = input("To add exercise 1 and for diet 2: ")
                if toAdd == "1":
                    exerciseFile = open(os.path.join(filesIn, "exercise.txt"), "a")
                    addExercise = input("Add Exercise: ")
                    creating_exercise = exerciseFile.write(f"\n[{getTime()}]    {addExercise}")
                    print("Exercise Added")
                    exerciseFile.close()
                elif toAdd == "2":
                    dietFile = open(os.path.join(filesIn, "diet.txt"), "a")
                    addDiet = input("Add Diet: ")
                    creating_diet = dietFile.write(f"\n[{getTime()}]    {addDiet}")
                    print("Diet Added")
                    dietFile.close()
            elif whatToDo == "logout":
                break
    
    if __name__ == "__main__":
        registerUser()
    