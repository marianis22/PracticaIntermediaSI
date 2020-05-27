class View:
    def start(self):
        print("***************************************************")
        print("    Bienvenido Al Sistema Del Cinema Salamanca:  ")
        print("***************************************************")
        
    def end(self):
        print("\n-------------------")
        print("   ¡Vuelve pronto!")
        print("---------------------")

    def menu_principal(self):
        print("---------------------")
        print("    Menú Principal:  ")
        print("---------------------") 
        
        print("1. Clientes")
        print("2. Peliculas") 
        print("3. Funciones")
        print("4. Salas")
        print("5. Asientos") 
        print("6. Boletos")
        print("\n0. Salir") 

    def select_opcion(self):
        print("Seleccione una opción: ", end = '') 

    def opcion_invalid(self):
        print("*************************************") 
        print("¡Opción incorrecta vuelva a intentar!") 
        print("*************************************") 
    
    def no_admin(self):
        print("*****************************************") 
        print("¡Solo los administradores pueden acceder!") 
        print("*****************************************") 

    def ask(self, output):
        print(output, end = '')    
        
    def success(self):    
         print(f"Los cambios se guardaron correctamente ")

    def error(self):
        print("Error: no se realizo correctamente")
    
    def id_invalido(self):
        print("Error. el id es invalido") 

    def mostrar_update(self):
        print("Actualiza los campos que sean necesarios")

    def mostrar_total(self, total):
        print("\nTotal del pedido: ", total) 

    def datos_incorrectos(self):
        print('\nUsuario o contraseña incorrectos')   
    """
    Vista admin cliente
    """
    def menu_cliente(self):
        print("---------------------")
        print("    Menú Clientes:  ")
        print("---------------------") 
        
        print("1. Agregar cliente")
        print("2. Leer cliente") 
        print("3. Leer todos los clientes")
        print("4. Actualizar cliente")
        print("5. Borrar cliente") 
        print("\n0. Salir")

    def mostrar_cliente(self, cliente):
        print('*****Información Cliente**********')
        print('ID: ', cliente[0])
        print('**********************************')
        print('Nombre: ', cliente[1])
        print('**********************************')
        print('Apellido Paterno: ', cliente[2])
        print('**********************************')
        print('Apellido Materno: ', cliente[3])
        print('**********************************')
        print('Edad: ', cliente[4])
        print('**********************************')
        print('Correo: ', cliente[5])
        print('**********************************') 
        print('Teléfono: ', cliente[6]) 
        print('**********************************')
        print('Usuario: ', cliente[7])
        print('**********************************')
        print('Contraseña: ', cliente[8])
        print('**********************************') 
        print('Admin: ', cliente[9])
        print('**********************************') 

    def mostrar_clientes(self, clientes):
        print('\n' + 'ID'.ljust(5) + '|' + 'Nombre(s)'.ljust(10) + '|' + 'Apellido Paterno'.ljust(16)+ '|'+'Apellido Materno'.ljust(16)+'|'+'Edad'.ljust(5)+'|' +' Correo'.ljust(15)+'|' +'Teléfono'.ljust(10)+'|' +' Usuario'.ljust(8)+'|'+'Contraseña'.ljust(10)+'|'+' Admin'.ljust(8))  
    
        for record in clientes:
            print(f'{record[0]:<5}|{record[1]:<10}|{record[2]:<16}|{record[3]:<16}|{record[4]:<5}|{record[5]:<15}|{record[6]:<10}|{record[7]:<8}|{record[8]:<8}|{record[9]:<8}')

    """
    Vista admin peliculas
    """

    def pelicula_menu(self):
        print("\n---------------------")
        print("    Menú Peliculas:  ")
        print("---------------------") 
        
        print("1. Agregar pelicula")
        print("2. Leer pelicula") 
        print("3. Leer todas las peliculas")
        print("4. Actualizar pelicula")
        print("5. Borrar pelicula")
        print("0. Salir")

    def mostrar_pelicula(self, pelicula):
        print('*****Información Peliculas********') 
        print('ID Boleto: ', pelicula[0])
        print('**********************************')
        print('Nombre: ', pelicula[1])
        print('**********************************') 
        print('Duración: ', pelicula[2])
        print('**********************************')
        print('Sinopsis: ', pelicula[3])
        print('**********************************') 
        print('Clasificación: ', pelicula[4])
        print('**********************************') 
        print('Genero: ', pelicula[5])
        print('**********************************')
   
    def mostrar_peliculas(self, pelicula):
        print('\n' + 'ID pelicula'.ljust(11) + '|' + 'Nombre'.ljust(20) + '|' + 'Duración'.ljust(11)+ '|'+'Sinopsis'.ljust(20)+'|'+' Clasificación'.ljust(20)+'|'+' Genero'.ljust(10))   

        for record in pelicula:
            print(f'{record[0]:<10}|{record[1]:<21}|{record[2]:<11}|{record[3]:<20}|{record[4]:<20}|{str(record[5]):<8}')   
    """
    vista admin salas
    """
    def salas_menu(self):
        print("\n---------------------")
        print("    Menú Salas:  ")
        print("---------------------") 
        
        print("1. Agregar sala")
        print("2. Leer sala") 
        print("3. Leer todas las salas")
        print("4. Actualizar sala")
        print("5. Borrar sala")
        print("0. Salir")

    def mostrar_sala(self, sala):
        print('*******Información Salas**********') 
        print('ID Sala: ', sala[0])
        print('**********************************')
        print('numero_asientos: ', sala[1])
        print('**********************************')
        print('numero_sala: ', sala[2])
        print('**********************************')
        print('tipo_sala: ', sala[3])
        print('**********************************')
        
    def mostrar_salas(self, sala):
        print('\n' + 'ID Sala'.ljust(7) + '|' + 'numero_asientos'.ljust(15) + '|' + 'numero_sala'.ljust(11)+ '|'+'tipo_sala'.ljust(9))   

        for record in sala:
            print(f'{record[0]:<7}|{record[1]:<15}|{record[2]:<11}|{record[3]:<9}') 
    """
    Vista admin asientos
    """
    def asientos_menu(self):
        print("\n---------------------")
        print("    Menú Asientos:  ")
        print("---------------------") 
        
        print("1. Agregar asiento")
        print("2. Leer asiento") 
        print("3. Leer todos los asientos")
        print("4. Actualizar asiento")
        print("5. Borrar asiento")
        print("0. Salir")

    def mostrar_asiento(self, asiento):
        print('*******Información asientos*******') 
        print('ID Asiento: ', asiento[0])
        print('**********************************')
        print('asiento: ', asiento[1])
        print('**********************************')
        print('fila: ', asiento[2])
        print('**********************************') 
        print('asiento: ', asiento[3])
        print('**********************************') 
        
    def mostrar_asientos(self, asiento):
        print('\n' + 'ID Asiento'.ljust(10) + '|' + 'asiento'.ljust(7) + '|' + 'fila'.ljust(4)+ '|'+'sala'.ljust(4))   

        for record in asiento:
            print(f'{record[0]:<10}|{record[1]:<7}|{record[2]:<4}|{record[3]:<4}') 
    """
    Vista admin funcion
    """
    def funciones_menu(self):
        print("\n---------------------")
        print("    Menú Funciones:  ")
        print("---------------------") 
        
        print("1. Agregar función")
        print("2. Leer funcion") 
        print("3. Leer todas las funciones")
        print("4. Actualizar función")
        print("5. Borrar función")
        print("0. Salir")

    def mostrar_funcion(self, funcion):
        print('******Información Función*********') 
        print('ID Función: ', funcion[0])
        print('**********************************')
        print('Pelicula: ', funcion[1])
        print('**********************************') 
        print('Fecha: ', funcion[2])
        print('**********************************') 
        print('Hora: ', funcion[3])
        print('**********************************')
    
    def mostrar_funciones(self, funcion):
        print('\n' + 'ID Función'.ljust(10) + '|' + 'Pelicula'.ljust(20) + '|' + 'Fecha'.ljust(12)+'|'+'Hora'.ljust(8)+ '|' + 'duracion'.ljust(15)+'|' + 'Sinopsis'.ljust(20) +'|' + 'Clasificacion'.ljust(15) +'|' + 'Genero'.ljust(15)) 

        for record in funcion:
            print(f'{record[0]:<10}|{record[1]:<20}|{str(record[2]):<12}|{record[3]:<8}|{record[4]:<15}|{record[5]:<20}|{record[6]:<15}|{record[7]:<15}')           
    
    """
    vista boletos admin
    """
    def boletos_menu(self):
        print("\n---------------------")
        print("    Menú Boletos:  ")
        print("---------------------") 
        
        print("1. Leer boleto") 
        print("2. Leer todol boletos")
        print("3. Borrar boleto")
        print("0. Salir")

    def mostrar_boleto(self, boleto):
        print('*******Información Salas**********') 
        print('ID Función: ', boleto[0])
        print('**********************************')
        print('ID Sala: ', boleto[1])
        print('**********************************')
        print('ID Cliente: ', boleto[2])
        print('**********************************')
        print('ID Asiento: ', boleto[3])
        print('**********************************')
        
    def mostrar_boletos(self, sala):
        print('\n' + 'ID Función'.ljust(7) + '|' + 'ID Sala'.ljust(15) + '|' + 'ID Cliente'.ljust(11)+ '|'+'ID Asiento'.ljust(9))   

        for record in sala:
            print(f'{record[0]:<7}|{record[1]:<15}|{record[2]:<11}|{record[3]:<9}') 
    
    """
    Vista login
    """
    def menu_principal_login(self):

        print("1. Registrarse")
        print("2. Iniciar Sesión") 

    
        

    """
    Vista clientes
    """     



    def menu_principal_clientes(self):
        print("---------------------")
        print("   Menú Principal:  ")
        print("---------------------") 
        
        print("1. Ver peliculas") 
        print("2. Ver funciones")
        print("3. Comprar Boletos")
        print("4. Comprar boletos de una pelicula")
        print("5. Ver mis boletos")
        print("6. Administrador")
        print("\n0. Salir")

    
    def mostrar_boleto(self, boletos):
        print('******Información Función*********') 
        print('Nombre: ', boletos[0])
        print('**********************************')
        print('Fecha: ', str(boletos[1]))
        print('**********************************') 
        print('Hora: ', boletos[2])
        print('**********************************') 
        print('Sala: ', boletos[3])
        print('**********************************')
        print('Tipo de sala: ', boletos[4])
        print('**********************************')
        print('Asiento: ', boletos[5])
        print('**********************************')
    
    def mostrar_boletos(self, boletos):
        print('\n' + 'Nombre'.ljust(15) + '|' + 'Fecha'.ljust(15) + '|' + 'Hora'.ljust(15)+'|'+'Salas'.ljust(8)+ '|' + 'Tipo de sala'.ljust(15)+'|' + 'Asiento'.ljust(7)) 

        for record in boletos:
            print(f'{record[0]:<15}|{str(record[1]):<15}|{str(record[2]):<15}|{record[3]:<8}|{record[4]:<15}|{record[5]:<7}')           
        
    def imprimir_asiento_ocupado(self):
        print('El asiento ya fue ocupado')   
    