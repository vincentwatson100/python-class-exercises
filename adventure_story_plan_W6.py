print('WELCOME TO YOUR OWN ADVENTURE!!!')
while True:  
   choice = input('Please choose one of the following options:\nenchated forest. Option enchated forest\nmountain summit. Option mountain summit\nYour choice (enchated forest or mountain summit): ')
   if choice.lower() == 'enchated forest':
        print('giant moss toads or frosty elk') 
        while True:
            choice =  input('Please choose one of the following options:\ngiant moss toads. Option left\nfrosty elk. Option giant moss toads\nYour choice (giant moss toads or frosty elk: ')
            if choice.lower() == 'giant moss toads':
                print('YOU GET PAST FOR YOUR NEXT CHALLENGE!!') 
                while True:
                    choice = input('Please choose one of the following options:\nmystical fawn. Option lmystical fawn\nwhispering deer. Option whispering deer\nYour choice (mystical fawn or whispering deer): ')
                    if choice.lower() == 'mystical fawn':
                       print('the fawn watches you, but you get past')
                       break
                    elif choice.lower() == 'whispering deer':
                       print ('YOU HAVE FOUND THE MOONLIT OWL; YOU WIN!!!')
                       break 
                    else:
                        print('that is an invalid choice please choose again')
                        break
                while True:
                   choice = input('Please choose one of the following options:\nmidnight sparrow. Option lfabled grizzzly\nmidnight sparrow. Option midnight sparrow\nYour choice (fabled grizzly or midnights sparrow): ')
                         if choice.lower() == 'midnight sparrow':
                               print('YOU WERE TRICKED BY THE CUNNING MIDNIGHT SPARROW; YOU LOST!!!!')
                               break
                          elif:
                                print('THE FABLED GRIZZLY PROTECTS YOU; AND HELPS YOU FIND THE MOONLIT OWL YOU WIN!!!!!!!')
                                break
                           else:
                              print('THAT IS AN INVALID ANSWER; PLEASE TRY AGAIN.')
                              break
                  elif choice.lower() == 'frosty elk':
                     print ('THE ELK FELT THREATENED AND ATTACKED YOU, YOU LOSE!!!')
                     break
            elif choice.lower() == 'mountain summit':
                while True:
                    choice = input('Please choose one of the following options:\nvolcano. Option volcano\n. Option glacial caves\nYour choice (volcano or glacial caves): ')
                    if choice.lower() == 'volcano':
                          print('YOU FOUND THE SECRET CAVE!!! YOU WIN!!!')
                           break  # Exit the outer loop after handling Option 2.
             elif choice.lower() == 'glacial caves':
                print ('YOU MEET A BEAR, YOU LOST!!!')
                 break
       else:
            print('that is an invalid choice, please choose again')
            break
          
              


