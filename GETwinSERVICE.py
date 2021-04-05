import psutil
import pprint
import win32serviceutil
import sys
import time

#77777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
def SERVICE_RESTART(service_NAME):#7777777777777777777777777777777777777777777777777777777777777777777777777777777777777

    while True:
        try:
            win32serviceutil.RestartService(service_NAME)
            time.sleep(5)
            SERVICE_QUERY(service_NAME)
            break
        except Exception as ex:
            print("OOOPS!!!", ex.__dict__["strerror"], "....Please try again.")
            BIG_CHOICES(service_NAME)
            break

#66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
def SERVICE_START(service_NAME):#666666666666666666666666666666666666666666666666666666666666666666666666666666666666666

    while True:
        try:
            win32serviceutil.StartService(service_NAME)
            time.sleep(5)
            SERVICE_QUERY(service_NAME)
        except Exception as ex:
            print("OOOPS!!!", ex.__dict__["strerror"], "....Please try again.")
            BIG_CHOICES(service_NAME)
            break

#55555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
def SERVICE_STOP(service_NAME):#5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
    while True:
        try:
            win32serviceutil.StopService(service_NAME)
            time.sleep(5)
            SERVICE_QUERY(service_NAME)
            break
        except Exception as ex:
            print("OOOPS!!!", ex.__dict__["strerror"], "....Please try again.")
            BIG_CHOICES(service_NAME)
            break

#44444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
def BIG_CHOICES(service_NAME):#44444444444444444444444444444444444444444444444444444444444444444444444444444444444444444

    choice = ""

    while choice != "Exit".casefold():
        print("[stop]    the service")
        print("[start]   the service")
        print("[restart] the service")
        print("[show]    the service details")
        print("[exit]    the program")

        choice = input("Try me. Enter your response here >>>> ")

        if choice == "stop".casefold():
            SERVICE_STOP(service_NAME)
            CAN_I_HELP_YOU(service_NAME)
            return
        if choice == "start".casefold():
            SERVICE_START(service_NAME)
            CAN_I_HELP_YOU(service_NAME)
            return
        if choice == "restart".casefold():
            SERVICE_RESTART(service_NAME)
            CAN_I_HELP_YOU(service_NAME)
            return
        if choice == "show".casefold():
            SERVICE_QUERY(service_NAME)
            pprint.pprint(service_READ_DICTIONARY)
            CAN_I_HELP_YOU(service_NAME)
            return
        if choice == "exit".casefold():
            break
        else:
            print("I'm so sorry that is not a given choice. Please try again.")
    print("You have chosen to Exit. Goodbye")
    return

#33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
def CAN_I_HELP_YOU(service_NAME):#333333333333333333333333333333333333333333333333333333333333333333333

    print(f"The service {service_NAME} is {service_CURRENT_STATUS}")
    print("Can I help you with anything else?")

    choice = ""

    while choice != "no".casefold():
        print("\n[yes] Let's do more!")
        print("[no] I want to go...")

        choice = input("\nEnter your response here >>>> ").casefold()

        if choice == "yes".casefold():
            print("\nAwesome!!! Your still in the game Chief!!!")
            print("What would you like to do next?")
            BIG_CHOICES(service_NAME)
            return
        elif choice == "no".casefold():
            break
        else:
            print("So sorry, that is not a valid choice. Please enter 'yes' or 'no'")

    print("Awww... Sorry to see you go. Til' next time.... Peace.")
    return None

#22222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
def SERVICE_QUERY(service_NAME):#222222222222222222222222222222222222222222222222222222222222222222222222222222222222222

    global service_CURRENT_STATUS
    global service_READ_DICTIONARY
    global service_FIND_NAME

    while True:
        try:

            service_FIND_NAME = psutil.win_service_get(service_NAME)
            assert isinstance(service_FIND_NAME, object)
            service_READ_DICTIONARY = service_FIND_NAME.as_dict()
            assert isinstance(service_READ_DICTIONARY, object)
            service_CURRENT_STATUS = service_READ_DICTIONARY["status"]
            assert isinstance(service_CURRENT_STATUS, object)
            break

        except Exception as ex:
            print("OOOPS!!!", ex.__dict__["msg"], "....Please try again.")
            SERVICE_NAME()
            break

    return service_CURRENT_STATUS, service_READ_DICTIONARY, service_FIND_NAME

#11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
def SERVICE_NAME():#1111111111111111111111111111111111111111111111111111111111111111111111111111111111111

    service_NAME = input("Tell me the name of your service >>>> ").casefold()
    # The objet service_NAME is sent to SERVICE_QUERY
    SERVICE_QUERY(service_NAME)
    CAN_I_HELP_YOU(service_NAME)


tina = list(
    "Hello, my name is Tina,\nI am a program created by Dalin Bryant Luster\nto help you Start, Stop, or Restart\na "
    "Windows Service. Or if you like we can can\ngather information on a service.\nWhen your ready let's have some fun "
    "with Services!!!\n")
for letters in tina:
    sys.stdout.write(letters)
    sys.stdout.flush()
    time.sleep(0.0)
print()

SERVICE_NAME()




