import calculator
import guessing
import to_do_list
import mad_lib
import text_based_adventure
import encryption_decryption
import tic_tac_toe





print(""""
___________              __  .__                                             
\__    ___/___   _______/  |_|__| ____    ____                               
  |    |_/ __ \ /  ___/\   __\  |/    \  / ___\                              
  |    |\  ___/ \___ \  |  | |  |   |  \/ /_/  >                             
  |____| \___  >____  > |__| |__|___|  /\___  /   /\  /\  /\  /\  /\  /\  /\ 
             \/     \/               \//_____/    \/  \/  \/  \/  \/  \/  \/       
      """)

choice = int(input(""""
    Welcome to python's game collection 
    1. Calculator
    2. Guess the number
    3. To_do List
    4. Mad Libs
    5. Text-based adventure Game
    6. Basic encrryption/Decreption
    7. Tic_tac_toe
    Choose a number...
               
"""))

if choice == 1:
    print("""
            ___________.__               _________        .__               .__          __                         
\__    ___/|  |__   ____     \_   ___ \_____  |  |   ____  __ __|  | _____ _/  |_  ___________          
  |    |   |  |  \_/ __ \    /    \  \/\__  \ |  | _/ ___\|  |  \  | \__  \\   __\/  _ \_  __ \         
  |    |   |   Y  \  ___/    \     \____/ __ \|  |_\  \___|  |  /  |__/ __ \|  | (  <_> )  | \/         
  |____|   |___|  /\___  >    \______  (____  /____/\___  >____/|____(____  /__|  \____/|__| /\  /\  /\ 
                \/     \/            \/     \/          \/                \/                 \/  
/  \/ 
          """)
          
		
		
    while True:
        print("Choose an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Square Root")
        print("7. Factorial")
        print("8. Logarithm")
        print("9. Trigonometric Functions")
        print("10. Exit")

        choice = input("Enter your choice (1-10): ")

        if choice == '10':
            break
            

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        object1 = calculator.Calculator(num1, num2)
        # object2 = calculator.Calculator(num1)

        if choice == '1':
            result = object1.add()
        elif choice == '2':
            result = object1.subtract()
        elif choice == '3':
            result = object1.multiply()
        elif choice == '4':
            result = object1.divide()
        elif choice == '5':
            result = object1.power()
        elif choice == '6':
            object1 = calculator.Calculator(num1)
            result = object1.square_root()
        elif choice == '7':
            result = object1.factorial()
        elif choice == '8':
            result = object1.logarithm()
        elif choice == '9':
            function = input("Enter the trigonometric function (sin, cos, tan): ")
            result = object1.trigonometric_functions()
        else:
            print("Invalid input")
            continue

        print("Result:", result)


elif choice == 2:
    print("""
  ________                                                                                                                   
 /  _____/ __ __   ____   ______ ______         ____  __ __   ____   ______ ______         ____  __ __   ____   ______ ______
/   \  ___|  |  \_/ __ \ /  ___//  ___/        / ___\|  |  \_/ __ \ /  ___//  ___/        / ___\|  |  \_/ __ \ /  ___//  ___/
\    \_\  \  |  /\  ___/ \___ \ \___ \        / /_/  >  |  /\  ___/ \___ \ \___ \        / /_/  >  |  /\  ___/ \___ \ \___ \ 
 \______  /____/  \___  >____  >____  >       \___  /|____/  \___  >____  >____  >       \___  /|____/  \___  >____  >____  >
        \/            \/     \/     \/       /_____/             \/     \/     \/       /_____/             \/     \/     \/ 
          """)



    choice = int(input("Guess a number from range 1 - 99: "))
    
    object1 = guessing.Guessing(choice)
    auto = object1.guessed_number()

    while True:
        if choice > auto:
            print("Your guess is to high")
            choice = int(input("Guess a number from range 1 - 99: "))
        elif choice < auto:
            print("Your guess is to low")
            choice = int(input("Guess a number from range 1 - 99: "))
        elif choice == auto:
            print("You guessed it right, You win")
            break
        else:
            print("Invalid input")
            choice = int(input("Guess a number from range 1 - 99: "))

elif choice == 3:
    print("""
___________               .___           .__  .__          __   
\__    ___/___          __| _/____       |  | |__| _______/  |_ 
  |    | /  _ \        / __ |/  _ \      |  | |  |/  ___/\   __\
  |    |(  <_> )      / /_/ (  <_> )     |  |_|  |\___ \  |  |  
  |____| \____/       \____ |\____/      |____/__/____  > |__|  
                           \/                         \/        
    """)

    to_do_list.main()

elif choice == 4:
    print("""
   _____              .___      .____    ._____.    
  /     \ _____     __| _/      |    |   |__\_ |__  
 /  \ /  \\__  \   / __ |       |    |   |  || __ \ 
/    Y    \/ __ \_/ /_/ |       |    |___|  || \_\ \
\____|__  (____  /\____ |       |_______ \__||___  /
        \/     \/      \/               \/       \/ 
    """)

    mad_lib.mad_libs()

elif choice == 5:
    print("""
___________              __        ___.                            .___                .___                    __                        
\__    ___/___ ___  ____/  |_      \_ |__ _____    ______ ____   __| _/    _____     __| _/__  __ ____   _____/  |_ __ _________   ____  
  |    |_/ __ \\  \/  /\   __\      | __ \\__  \  /  ___// __ \ / __ |     \__  \   / __ |\  \/ // __ \ /    \   __\  |  \_  __ \_/ __ \ 
  |    |\  ___/ >    <  |  |        | \_\ \/ __ \_\___ \\  ___// /_/ |      / __ \_/ /_/ | \   /\  ___/|   |  \  | |  |  /|  | \/\  ___/ 
  |____| \___  >__/\_ \ |__|        |___  (____  /____  >\___  >____ |     (____  /\____ |  \_/  \___  >___|  /__| |____/ |__|    \___  >
             \/      \/                 \/     \/     \/     \/     \/          \/      \/           \/     \/                        \/ 
""")
    text_based_adventure.main()

elif choice == 6:
    print("""
                                           __  .__                         ____              .___                                  __  .__                
  ____   ____   ___________ ___.__._______/  |_|__| ____   ____           /  _ \           __| _/____   ___________ ___.__._______/  |_|__| ____   ____   
_/ __ \ /    \_/ ___\_  __ <   |  |\____ \   __\  |/  _ \ /    \          >  _ </\        / __ |/ __ \_/ ___\_  __ <   |  |\____ \   __\  |/  _ \ /    \  
\  ___/|   |  \  \___|  | \/\___  ||  |_> >  | |  (  <_> )   |  \        /  <_\ \/       / /_/ \  ___/\  \___|  | \/\___  ||  |_> >  | |  (  <_> )   |  \ 
 \___  >___|  /\___  >__|   / ____||   __/|__| |__|\____/|___|  /        \_____\ \       \____ |\___  >\___  >__|   / ____||   __/|__| |__|\____/|___|  / 
     \/     \/     \/       \/     |__|                       \/                \/            \/    \/     \/       \/     |__|                       \/  
""")
    encryption_decryption.main()


elif choice == 7:
    print("""
___________.__                 __                             __                 
\__    ___/|__| ____         _/  |______    ____            _/  |_  ____   ____  
  |    |   |  |/ ___\        \   __\__  \ _/ ___\           \   __\/  _ \_/ __ \ 
  |    |   |  \  \___         |  |  / __ \\  \___            |  | (  <_> )  ___/ 
  |____|   |__|\___  >        |__| (____  /\___  >           |__|  \____/ \___  >
                   \/                   \/     \/                             \/ 
""")
    object1 = tic_tac_toe.TicTacToe()
    object1.play_game()

else:
    print("Invalid input...")
    choice = int(input(""""
    Here are games you would love to test and play
    1. Calculator
    2. Guess the number
    3. To_do List
    4. Mad Libs
    5. Text-based adventure Game
    6. Basic encrryption/Decreption
    7. Tic_tac_toe
    Choose a number...
               
    """))
