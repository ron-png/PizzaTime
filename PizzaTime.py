# To Do: Accept "n" and "y" as answers too.


rightInput = True

while rightInput:

    # ask if user wants pizza
    pizzaTime=str(input("Do you want pizza? (Yes/No) \n")) 

    #give pizza
    if "YES" in pizzaTime.upper():
        print("                                     ._ \n"+
        "                                   ,(  `-.\n"+
        "                                 ,': `.   `.\n"+
        "                               ,` *   `-.   \ \n"+
        "                             ,'  ` :+  = `.  `.\n"+
        "                           ,~  (o):  .,   `.  `.\n"+
        "                         ,'  ; :   ,(__) x;`.  ;\n" +
        "                       ,'  :'  itz  ;  ; ; _,-'\n"+
        "                     .'O ; = _' C ; ;'_,_ ;\n"+
        "                   ,;  _;   ` : ;'_,-'   i'\n"+
        "                 ,` `;(_)  0 ; ','       :\n"+
        "               .';6     ; ' ,-'~\n"+
        "             ,' Q  ,& ;',-.'\n"+
        "           ,( :` ; _,-'~  ;\n"+
        "         ,~.`c _','\n"+
        "       .';^_,-' ~\n"+
        "     ,'_;-''\n"+
        "    ,,~\n"+
        "    i'\n"+
        "    :\n")  
        rightInput = False

    #give no pizza :(
    elif "NO" in pizzaTime.upper():
        print('''        .-""""""-. \n'''+
        '''      .'          '. \n'''+
        '''     /   O      O   \ \n'''+
        '''    :           `    : \n'''+
        '''    |                |    \n'''+
        '''    :    .------.    : \n'''+
        '''     \  '        '  / \n'''+
        '''      '.          .' \n'''+
        '''        '-......-' ''')
        rightInput = False

    elif "EXIT" in pizzaTime.upper():
        rightInput = False

    #If the answer to question was wrong, go Back to top...
    else:
        input('''You can only answer with "Yes", "No" or "Exit". \n ''' +
        '''(press ENTER to continue)''')
input("(press ENTER to exit)")