import modules.corefile as cf

import funciones.globales as fg

import ui.uiPatient as uiPa

import ui.uispecialist as uiSp



def mainMenu(op):

    fg.borrar_pantalla()

    title ="""

    *******************

    * CLINITA PRIVADA *

    ******************* 

    """

    mainMenuOp = '1. Registro Pasiente\n2. Especialistas\n3. Agendar Cita\n4. Consultar Citas\n5 Salir'

    if (op != 5):

        print(title)

        print(mainMenuOp)

        try:

            opcion = int(input(':)_ '))

        except ValueError:

            print('Error en la opcion ingresada')

            fg.pausar_pantalla()

            mainMenu(0)

        else:

            match (opcion):

                case 1:

                    uiPa.MenuPatient(0)

                case 2:

                    uiSp.MenuSpecialist()

                case 3:

                   pass

                case 4:

                    pass

                case 5:

                    print('Regrese pronto......')

                    fg.pausar_pantalla()

                case _:

                    print('Opcion ingresada no pertenece al menu de opciones')

                    fg.pausar_pantalla()

                    mainMenu(0)

if __name__ == '__main__':

    cf.MY_DATABASE = 'data/patient.json'

    cf.checkFile(fg.clinicaSpecialist)

    mainMenu()

    main()

    
