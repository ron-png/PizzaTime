# Variables needed to check if the right Input was given 
rightInput = True
yes = {"YES", "Y", "YE", ""}
no = {"NO", "N"}
getout = {"EXIT", "E", "EXI", "EX"}

#While loop in case of User typing the wrong input
while rightInput:

    # ask if user wants pizza
    pizzaTime = input("Do you want pizza? [Yes/No] \n")

    #give pizza
    if pizzaTime.upper() in yes:
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
    elif pizzaTime.upper() in no:
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

    #exit commnand
    elif pizzaTime.upper() in getout:
        rightInput = False

    #If the answer to question was wrong, go Back to top...
    else:
        input('''You can only answer with "[Y]es", "[N]o" or "[E]xit". \n ''' +
        '''(press ENTER to continue)''')
input(" (press ENTER to exit)")