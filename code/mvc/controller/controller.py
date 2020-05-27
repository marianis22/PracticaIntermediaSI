from model.model import Model
from view.view import View
from datetime import date

class Controller:

    def __init__(self):
        self.view = View()
        self.model = Model()
        self.cliente_iniciado = None
        
    def start(self):
        self.view.start()  
        self.menu_principal_login()

    def menu_principal_login(self): 
        option = None
        
        while option != '0':
            self.view.menu_principal_login()
            self.view.select_opcion()

            option = input()

            if option == '1':
                self.menu_registrarse()
            elif option == '2':
                self.menu_iniciar_sesion()             
            elif option == '0':
                self.view.end()
            else:
                self.view.opcion_invalid()
    """
    controlador 
    """    
    def menu_registrarse(self):
        self.view.ask('Nombre: ')
        nombre = input()
        self.view.ask('Apellido Paterno: ')
        apellido_p = input()
        self.view.ask('Apellido Materno: ')
        apellido_m = input()
        self.view.ask('Edad: ')
        edad = input()
        self.view.ask('Correo: ')
        correo = input()
        self.view.ask('Teléfono: ')
        tel = input()
        self.view.ask('Usuario: ')
        usuario = input()
        self.view.ask('Contraseña: ')
        contrasena = input()
        admin = 0

        registro = self.model.create_cliente(nombre,apellido_p,apellido_m,edad, correo,tel,usuario,contrasena,admin)

        if registro == True:

            self.view.success()
        else:
            self.view.error()

        
    def menu_iniciar_sesion(self):    
        self.view.ask('Nombre de usuario: ')
        usuario = input()
        self.view.ask('Contraseña: ')
        contrasena = input()

        cliente = self.model.read_login(usuario, contrasena)

        if type(cliente) == tuple:
            self.cliente_iniciado = cliente
            self.menu_principal_clientes()
        elif cliente ==  None:
            self.view.datos_incorrectos()
        else:
            self.view.error()


    """
    Controlador menu principal admin
    """

    def menu_principal(self): 
        option = None
        
        while option != '0':
            self.view.menu_principal()
            self.view.select_opcion()

            option = input()

            if option == '1':
                self.menu_cliente()
            elif option == '2':
                self.pelicula_menu()
            elif option == '3':
                self.funciones_menu()
            elif option == '4':
                self.salas_menu()
            elif option == '5':
                self.asientos_menu() 
            elif option == '6':
                self.boletos_menu()          
            elif option == '0':
                self.view.end()
            else:
                self.view.opcion_invalid() 
    """
    controlador clientes
    """
    def menu_cliente(self): 
        option = None
        
        while option != '0':
            self.view.menu_cliente()
            self.view.select_opcion()

            option = input()

            if option == '1':
                self.agregar_cliente()
            elif option == '2':
                self.read_cliente()
            elif option == '3':
                self.read_all_clientes()
            elif option == '4':
                self.update_cliente()     
            elif option == '5':
                self.delete_cliente()          
            elif option == '0':
                self.view.end()
            else:
                self.view.opcion_invalid() 

    def agregar_cliente(self):
        self.view.ask('Nombre:')
        nombre = input()
        self.view.ask('Apellido Paterno: ') 
        apellido_p = input()
        self.view.ask(' Apellido Materno: ')
        apellido_m = input()
        self.view.ask('Edad: ')
        edad = input()
        self.view.ask('Correo: ')
        correo = input()
        self.view.ask('Teléfono: ')
        tel = input()
        self.view.ask('Usuario: ')
        usuario = input()
        self.view.ask('Contraseña: ')
        contrasena = input()
        self.view.ask('Admin: ')
        admin = input()
        

        crear = self.model.create_cliente(nombre, apellido_p,apellido_m, edad,correo,tel,usuario,contrasena,admin)  
        if crear == True:

            self.view.success()
        else:
            self.view.error()

    def read_cliente(self):
        self.view.ask("ID Cliente: ")
        idcliente = input()

        cliente =  self.model.read_cliente(idcliente)

        if type(cliente) == tuple:
            self.view.mostrar_cliente(cliente)
        elif cliente ==  None:
            self.view.id_invalido()
        else:
            self.view.error()

    def read_all_clientes(self):
        clientes = self.model.read_all_clientes()

        if type(clientes) == list:
            self.view.mostrar_clientes(clientes)
        else:
            self.view.error()        

    def read_correo_cliente(self):
        self.view.ask("Correo: ")
        correo = input()

        cliente = self.model.leer_correo_clientes(correo)
        if type(cliente) == tuple:
            
            self.view.mostrar_clientes(cliente)
        elif cliente ==  None:
            self.view.id_invalido()        

        else:
            self.view.error()

    def update_cliente(self):
      
        self.view.mostrar_update()
        self.view.ask('ID:')
        idcliente = input()    
        self.view.ask('Nombre:')
        nombre = input()
        self.view.ask('Apellido Paterno: ') 
        apellido_p = input()
        self.view.ask(' Apellido Materno: ')
        apellido_m = input()
        self.view.ask('Edad: ')
        edad = input()
        self.view.ask('Correo: ')
        correo = input()
        self.view.ask('Teléfono: ')
        tel = input()
        self.view.ask('Usuario: ')
        usuario = input()
        self.view.ask('Contraseña: ')
        contrasena = input()
        self.view.ask('Admin: ')
        admin = input()
        

        result = self.model.update_cliente(idcliente, nombre,apellido_p, apellido_m,edad,correo,tel, usuario,contrasena,admin)
        
        if result == True:
            self.view.success()
        elif result == False: 
            self.view.id_invalido()   
        else:
            self.view.error() 

    def delete_cliente(self):
        self.view.ask("ID: ")
        idcliente = input()

        result = self.model.delete_cliente(idcliente)

        if result == True:
            self.view.success()
        elif  result == False:
            self.view.id_invalido()
        else:    
            self.view.error()
    """
    controlador peliculas
    """        

    def pelicula_menu(self): 
        option = None
        
        while option != '0':
            self.view.pelicula_menu()
            self.view.select_opcion()
            option = input()
            if option == '1':
                self.agregar_pelicula()
            elif option == '2':
                self.read_pelicula()
            elif option == '3':
                self.read_all_peliculas()
            elif option == '4':
                self.update_pelicula()
            elif option == '5':
                self.delete_peliculas()                  
            elif option == '0':
                self.view.end()
            else:
                self.view.opcion_invalid() 

    def agregar_pelicula(self):
        self.view.ask('Nombre:')
        nombre = input()
        self.view.ask('Duración: ') 
        duracion = input()
        self.view.ask('Sinopsis: ')
        sinopsis = input()
        self.view.ask('Clasificación: ')
        clasificacion= input()
        self.view.ask('Genero: ')
        generos_idgenero = input()
        
        crear = self.model.create_pelicula(nombre, duracion,sinopsis,clasificacion,generos_idgenero)  
        if crear == True:

            self.view.success()
        else:
            self.view.error()

    def read_pelicula(self):
        self.view.ask("ID pelicula: ")
        idpelicula = input()

        pelicula =  self.model.read_pelicula(idpelicula)

        if type(pelicula) == tuple:
            self.view.mostrar_pelicula(pelicula)
        elif pelicula ==  None:
            self.view.id_invalido()

    def read_all_peliculas(self):
        pelicula = self.model.read_all_peliculas()

        if type(pelicula) == list:
            self.view.mostrar_peliculas(pelicula)
        else:
            self.view.error()

    def update_pelicula(self):
      
        self.view.mostrar_update()
        self.view.ask('ID:')
        idpelicula = input()    
        self.view.ask('Nombre:')
        nombre = input()
        self.view.ask('Duración: ') 
        duracion = input()
        self.view.ask('sinopsis: ')
        sinopsis = input()
        self.view.ask('Clasificación: ')
        clasificacion= input()
        self.view.ask('Genero: ')
        generos_idgenero = input()
        
        result = self.model.update_pelicula(idpelicula, nombre,duracion, sinopsis,clasificacion,generos_idgenero)
        
        if result == True:
            self.view.success()
        elif result == False: 
            self.view.id_invalido()   
        else:
            self.view.error()

    def delete_peliculas(self):
        self.view.ask("ID: ")
        idpelicula = input()

        result = self.model.delete_pelicula(idpelicula)

        if result == True:
            self.view.success()
        elif  result == False:
            self.view.id_invalido()
        else:    
            self.view.error() 
    """
    controlador salas
    """        
    def salas_menu(self): 
        option = None
        
        while option != '0':
            self.view.salas_menu()
            self.view.select_opcion()
            option = input()
            if option == '1':
                self.agregar_sala()
            elif option == '2':
                self.read_sala()
            elif option == '3':
                self.read_all_salas()
            elif option == '4':
                self.update_sala()
            elif option == '5':
                self.delete_sala()                  
            elif option == '0':
                self.view.end()
            else:
                self.view.opcion_invalid()

    def agregar_sala(self):
        self.view.ask('Número de asientos:')
        num_asientos = input()
        self.view.ask('Número de sala: ') 
        numero_sala = input()
        self.view.ask('Tipo de sala: ')
        tipo_sala = input()
        
        crear = self.model.create_sala(num_asientos,numero_sala,tipo_sala)  
        if crear == True:

            self.view.success()
        else:
            self.view.error()

    def read_sala(self):
        self.view.ask("ID Sala: ")
        idsala = input()

        sala =  self.model.read_sala(idsala)

        if type(sala) == tuple:
            self.view.mostrar_sala(sala)
        elif sala ==  None:
            self.view.id_invalido()

    def read_all_salas(self):
        sala = self.model.read_all_salas()

        if type(sala) == list:
            self.view.mostrar_salas(sala)
        else:
            self.view.error() 

    def update_sala(self):
      
        self.view.mostrar_update()
        self.view.ask('ID:')
        idsala = input()    
        self.view.ask('Número de asientos :')
        num_asientos = input()
        self.view.ask('Número de sala: ') 
        numero_sala = input()
        self.view.ask('Tipo de sala: ')
        tipo_sala = input()
        
        result = self.model.update_sala(idsala,num_asientos,numero_sala,tipo_sala)
        
        if result == True:
            self.view.success()
        elif result == False: 
            self.view.id_invalido()   
        else:
            self.view.error() 

    def delete_sala(self):
        self.view.ask("ID: ")
        idsala = input()

        result = self.model.delete_sala(idsala)

        if result == True:
            self.view.success()
        elif  result == False:
            self.view.id_invalido()
        else:    
            self.view.error() 
    """
    controlador asientos
    """                                                 
    def asientos_menu(self): 
        option = None
        
        while option != '0':
            self.view.asientos_menu()
            self.view.select_opcion()
            option = input()
            if option == '1':
                self.agregar_asiento()
            elif option == '2':
                self.read_asiento()
            elif option == '3':
                self.read_all_asientos()
            elif option == '4':
                self.update_asiento()
            elif option == '5':
                self.delete_asiento()                  
            elif option == '0':
                self.view.end()
            else:
                self.view.opcion_invalid()

    def agregar_asiento(self):
        self.view.ask('Ingrese asiento: ')
        asiento = input()
        self.view.ask('Ingrese fila: ') 
        fila = input()
        self.view.ask('ID Sala: ')
        salas_idsala = input()
        
        crear = self.model.create_asiento(asiento,fila,salas_idsala)  
        if crear == True:

            self.view.success()
        else:
            self.view.error() 

    def read_asiento(self):
        self.view.ask("ID Asiento: ")
        idasiento = input()

        asiento =  self.model.read_asiento(idasiento)

        if type(asiento) == tuple:
            self.view.mostrar_asiento(asiento)
        elif asiento ==  None:
            self.view.id_invalido()

    def read_all_asientos(self):
        asiento = self.model.read_all_asientos()

        if type(asiento) == list:
            self.view.mostrar_asientos(asiento)
        else:
            self.view.error()

    def update_asiento(self):
      
        self.view.mostrar_update()
        self.view.ask('ID:')
        idasiento = input()    
        self.view.ask('Nombre asiento :')
        asiento = input()
        self.view.ask('Número fila: ') 
        fila = input()
        self.view.ask('ID Sala: ')
        salas_idsala = input()
        
        result = self.model.update_asientos(idasiento,asiento,fila,salas_idsala)
        
        if result == True:
            self.view.success()
        elif result == False: 
            self.view.id_invalido()   
        else:
            self.view.error()

    def delete_asiento(self):
        self.view.ask("ID: ")
        idasiento = input()

        result = self.model.delete_asiento(idasiento)

        if result == True:
            self.view.success()
        elif  result == False:
            self.view.id_invalido()
        else:    
            self.view.error() 
    """
    controlador funciones
    """                                                 
    def funciones_menu(self): 
        option = None
        
        while option != '0':
            self.view.funciones_menu()
            self.view.select_opcion()
            option = input()
            if option == '1':
                self.agregar_funcion()
            elif option == '2':
                self.read_funcion()
            elif option == '3':
                self.read_all_funciones()
            elif option == '4':
                self.update_funcion()
            elif option == '5':
                self.delete_fucion()                  
            elif option == '0':
                self.view.end()
            else:
                self.view.opcion_invalid()

    def agregar_funcion(self):
        self.view.ask('ID Pelicula: ')
        idpelicula = input()
        self.view.ask('Fecha: ') 
        fecha = input()
        self.view.ask('Hora: ')
        hora = input()
        self.view.ask('ID Sala: ')
        salas_idsala = input()
        self.view.ask('Precio: ')
        precio = input()
        
        crear = self.model.create_funcion(idpelicula,fecha,hora,salas_idsala,precio)  
        if crear == True:

            self.view.success()
        else:
            self.view.error() 

    def read_funcion(self):
        self.view.ask("ID Función: ")
        idfuncion = input()

        funcion =  self.model.read_funcion(idfuncion)

        if type(funcion) == tuple:
            self.view.mostrar_funcion(funcion)
        elif funcion ==  None:
            self.view.id_invalido()
        else:
            self.view.error()

    def read_all_funciones(self):
        funcion = self.model.read_all_funciones()

        if type(funcion) == list:
            self.view.mostrar_funciones(funcion)
        else:
            self.view.error()

    def update_funcion(self):
      
        self.view.ask('ID Función:')
        id_funciones = input()
        self.view.mostrar_update()
        self.view.ask('ID Pelicula:')
        idpelicula = input()    
        self.view.ask('Fecha :')
        fecha = input()
        self.view.ask('Hora: ') 
        hora = input()
        self.view.ask('ID Sala: ')
        salas_idsala = input()
        self.view.ask('Precio: ')
        precio = input()
        
        result = self.model.update_funcion(id_funciones,idpelicula,fecha,hora,salas_idsala,precio)

        print(result)
        
        if result == True:
            self.view.success()
        elif result == False: 
            self.view.id_invalido()   
        else:
            self.view.error()

    def delete_fucion(self):
        self.view.ask("ID: ")
        idfuncion = input()

        result = self.model.delete_funcion(idfuncion)

        if result == True:
            self.view.success()
        elif  result == False:
            self.view.id_invalido()
        else:    
            self.view.error()

    """
    controlador boletos admin
    """  
    def boletos_menu(self): 
        option = None
        
        while option != '0':
            self.view.boletos_menu()
            self.view.select_opcion()

            option = input()

            if option == '1':
                self.read_boleto()
            elif option == '2':
                self.read_all_boletos()
            elif option == '3':
                self.delete_boleto()              
            elif option == '0':
                self.view.end()
            else:
                self.view.opcion_invalid()   

    def read_boleto(self):
        self.view.ask("ID Boleto: ")
        idboleto = input()

        boleto =  self.model.read_boleto(idboleto)

        if type(boleto) == tuple:
            self.view.mostrar_boleto(boleto)
        elif boleto ==  None:
            self.view.id_invalido()
        else:
            self.view.error()

    def read_all_boletos(self):
        boleto = self.model.read_all_boletos()

        if type(boleto) == list:
            self.view.mostrar_boletos(boleto)
        else:
            self.view.error()

    def delete_boleto(self):
        self.view.ask("ID Boleto: ")
        boleto = input()

        result = self.model.delete_boleto(boleto)

        if result == True:
            self.view.success()
        elif  result == False:
            self.view.id_invalido()
        else:    
            self.view.error()        

    """
    Controlador clientes
    """         
    def menu_principal_clientes(self): 
        option = None
        
        while option != '0':
            self.view.menu_principal_clientes()
            self.view.select_opcion()

            option = input()

            if option == '1':
                self.read_all_peliculas()
            elif option == '2':
                self.read_all_funciones()
            elif option == '3':
                self.comprar_boletos()
            elif option == '4':
                self.comprar_boletos_por_pelicula()
            elif option == '5':
                self.ver_mis_boletos() 
            elif option == '6':
                self.menu_administrador()             
            elif option == '0':
                self.view.end()
            else:
                self.view.opcion_invalid() 

    def menu_administrador(self): 
        es_admin = self.cliente_iniciado[9]

        if es_admin:
            self.menu_principal()
        else:
            self.view.no_admin()

    def comprar_boletos(self):
        self.view.ask('Fecha (AAAA/MM/DD): ')
        fecha = input()

        if fecha == '':
            fecha = date.today().isoformat()

        funciones = self.model.read_all_funciones_por_fecha(fecha)

        self.view.mostrar_funciones(funciones)

        self.view.ask('ID Funciones: ')
        id_funciones = input()

        funcion = self.model.read_funcion(id_funciones)

        id_salas_asientos = funcion[4]
        clientes_idcliente = self.cliente_iniciado[0]

        asientos = self.model.read_all_asientos_por_sala(id_salas_asientos)
        asientos_ocupados_id = self.model.obtener_asientos_ocupados(id_funciones)

        asientos_disponibles = []

        for a in asientos:
            if a[0] not in asientos_ocupados_id:
                asientos_disponibles.append(a)

        self.view.mostrar_asientos(asientos_disponibles)
        
        self.view.ask('ID Asiento: ')
        asientos_idasiento = input()

        if int(asientos_idasiento) in asientos_ocupados_id:
            self.view.imprimir_asiento_ocupado()
            return
        
        crear = self.model.create_boleto(id_funciones,id_salas_asientos,clientes_idcliente,asientos_idasiento)  
        if crear == True:

            self.view.success()
        else:
            self.view.error() 
    
    def comprar_boletos_por_pelicula(self):
        self.read_all_peliculas()

        self.view.ask('ID pelicula: ')
        idpelicula = input()

        funciones = self.model.read_all_funciones_por_pelicula(idpelicula)

        self.view.mostrar_funciones(funciones)

        self.view.ask('ID Funciones: ')
        id_funciones = input()

        funcion = self.model.read_funcion(id_funciones)

        id_salas_asientos = funcion[4]
        clientes_idcliente = self.cliente_iniciado[0]

        asientos = self.model.read_all_asientos_por_sala(id_salas_asientos)
        asientos_ocupados_id = self.model.obtener_asientos_ocupados(id_funciones)

        asientos_disponibles = []

        for a in asientos:
            if a[0] not in asientos_ocupados_id:
                asientos_disponibles.append(a)

        self.view.mostrar_asientos(asientos_disponibles)
        
        self.view.ask('ID Asiento: ')
        asientos_idasiento = input()

        if int(asientos_idasiento) in asientos_ocupados_id:
            self.view.imprimir_asiento_ocupado()
            return
        
        crear = self.model.create_boleto(id_funciones,id_salas_asientos,clientes_idcliente,asientos_idasiento)  
        if crear == True:

            self.view.success()
        else:
            self.view.error() 

    def ver_mis_boletos(self):
        boletos = self.model.read_all_boletos()

        if type(boletos) == list:
            self.view.mostrar_boletos(boletos)
        else:
            self.view.error() 

    

        


   