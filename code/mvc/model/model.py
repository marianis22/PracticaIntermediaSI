from mysql import connector

class Model:
    def __init__(self,config_db_file = 'config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connect_to_db()
    
    def read_config_db(self):
        d ={}
        
        with open(self.config_db_file) as f_r:
            for line in f_r:
                (key, val) = line.strip().split(':')
                d[key] = val
        return d

    def connect_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor()

    def close_db(self):
        self.cnx.close() 
    """
    Modelo cliente:
    """                   
    def create_cliente(self,nombre,apellido_p, apellido_m,edad,correo,tel, usuario,contrasena,admin):
        try:
            sql = 'INSERT INTO clientes(nombre,apellido_p, apellido_m,edad,correo,tel, usuario,contrasena,admin) VALUES(%s, %s,%s,%s,%s,%s,%s,%s,%s)'
            values = (nombre,apellido_p, apellido_m,edad,correo,tel, usuario,contrasena,admin)

            self.cursor.execute(sql, values)
            self.cnx.commit()

            return True
        except connector.Error as err:
            self.cnx.rollback()
            return(err)

    def read_cliente(self, id):
        try:
            sql = 'SELECT * FROM clientes WHERE idcliente = %s'
            values = (id,)
            self.cursor.execute(sql, values)
            cliente = self.cursor.fetchone()

            return cliente
        except connector.Error as err:
            return (err)
            
    def leer_correo_clientes(self, correo):        
        try:
            sql = "SELECT * FROM clientes WHERE correo = " + "'" + correo + "';"
            self.cursor.execute(sql)
            cliente = self.cursor.fetchone()
            print(cliente)
            return cliente
        except connector.Error as err:
            return (err)         

    def read_all_clientes(self):
        try:
            sql = 'SELECT * FROM clientes'
            self.cursor.execute(sql)
            cliente = self.cursor.fetchall()

            return cliente
        except connector.Error as err:
            return (err) 


    def update_cliente(self, idcliente, nombre = '', apellido_p = '', apellido_m = '', edad = '', correo = '',tel = '', usuario= '',contrasena = '',admin = ''):
        fields = []
        val = []

        if nombre !='':
            val.append(nombre)
            fields.append('nombre = %s')
        if apellido_p !='':
            val.append(apellido_p)
            fields.append('apellido_p = %s')
        if apellido_m !='':
            val.append(apellido_m)
            fields.append('apellido_m = %s')    
        if edad != '':
            val.append(edad)
            fields.append('edad = %s')
        if correo != '':
            val.append(correo)
            fields.append('correo = %s')
        if tel != '':
            val.append(tel)
            fields.append('tel = %s')   
        if usuario != '':
            val.append(usuario)
            fields.append('usuario = %s')
        if contrasena != '':
            val.append(contrasena)
            fields.append('contrasena = %s')    
        if admin != '':
            val.append(admin)
            fields.append('admin = %s')    
               

        val.append(idcliente)
        val = tuple(val)         
        try:
            sql = 'UPDATE clientes SET ' + ','.join(fields) +' WHERE idcliente =%s'

            self.cursor.execute(sql,val)
            self.cnx.commit()

            return self.cursor.rowcount > 0

        except connector.Error as err:
            self.cnx.rollback()
            return(err)

    def delete_cliente(self, id):
        try:
            sql = 'DELETE  FROM clientes WHERE idcliente = %s'
            values = (id,)

            self.cursor.execute(sql, values)
            self.cnx.commit()

            return self.cursor.rowcount > 0
        except connector.Error as err:
            self.cnx.rollback()
            return (err)
    """
    Modelo peliculas:
    """              
    def create_pelicula(self,nombre,duracion, sinopsis,clasificacion,generos_idgenero):
        try:
            sql = 'INSERT INTO peliculas(nombre,duracion, sinopsis,clasificacion,generos_idgenero) VALUES(%s, %s,%s,%s,%s)'
            values = (nombre,duracion, sinopsis,clasificacion,generos_idgenero)

            self.cursor.execute(sql, values)
            self.cnx.commit()

            return True
        except connector.Error as err:
            self.cnx.rollback()
            return(err)

    def read_pelicula(self, id):
        try:
            sql = 'SELECT idpelicula, nombre, duracion, sinopsis, clasificacion, genero FROM peliculas JOIN generos ON peliculas.generos_idgenero = generos.idgenero WHERE idpelicula = %s'
            values = (id,)

            self.cursor.execute(sql, values)
            pelicula = self.cursor.fetchone()

            return pelicula
        except connector.Error as err:
            return (err) 

    def leer_nombre_pendiente(self, correo):        
        try:
            sql = 'SELECT * FROM clientes WHERE correo = %s'
            values = (correo,)
            self.cursor.execute(sql, values)
            cliente = self.cursor.fetchone()

            return cliente
        except connector.Error as err:
            return (err)         

    def read_all_peliculas(self):
        try:
            sql = 'SELECT idpelicula, nombre, duracion, sinopsis, clasificacion, genero FROM peliculas JOIN generos ON peliculas.generos_idgenero = generos.idgenero'
            self.cursor.execute(sql)
            pelicula = self.cursor.fetchall()

            return pelicula
        except connector.Error as err:
            return (err) 


    def update_pelicula(self, idpelicula, nombre = '', duracion = '', sinopsis = '', clasificacion = '',generos_idgenero = ''):
        fields = []
        val = []

        if nombre !='':
            val.append(nombre)
            fields.append('nombre = %s')
        if duracion !='':
            val.append(duracion)
            fields.append('duracion = %s')
        if sinopsis !='':
            val.append(sinopsis)
            fields.append('sinopsis = %s')    
        if clasificacion != '':
            val.append(clasificacion)
            fields.append('clasificacion = %s')
        if generos_idgenero != '':
            val.append(generos_idgenero)
            fields.append('generos_idgenero = %s')    
           
        val.append(idpelicula)
        val = tuple(val)         
        try:
            sql = 'UPDATE peliculas SET ' + ','.join(fields) +' WHERE idpelicula = %s'

            self.cursor.execute(sql,val)
            self.cnx.commit()

            return self.cursor.rowcount > 0

        except connector.Error as err:
            self.cnx.rollback()
            return(err)

    def delete_pelicula(self, id):
        try:
            sql = 'DELETE  FROM peliculas WHERE idpelicula = %s'
            values = (id,)

            self.cursor.execute(sql, values)
            self.cnx.commit()

            return self.cursor.rowcount > 0
        except connector.Error as err:
            self.cnx.rollback()
            return (err) 
    """
    Modelo salas:
    """  
    def create_sala(self,num_asientos,numero_sala,tipo_sala):
        try:
            sql = 'INSERT INTO salas(num_asientos,numero_sala,tipo_sala) VALUES(%s, %s,%s)'
            values = (num_asientos,numero_sala,tipo_sala)

            self.cursor.execute(sql, values)
            self.cnx.commit()

            return True
        except connector.Error as err:
            self.cnx.rollback()
            return(err)

    def read_sala(self, id):
        try:
            sql = 'SELECT * FROM salas WHERE idsala = %s'
            values = (id,)
            self.cursor.execute(sql, values)
            sala = self.cursor.fetchone()

            return sala
        except connector.Error as err:
            return (err) 
        

    def read_all_salas(self):
        try:
            sql = 'SELECT * FROM salas'
            self.cursor.execute(sql)
            sala = self.cursor.fetchall()

            return sala
        except connector.Error as err:
            return (err) 


    def update_sala(self, idsala, num_asientos = '', numero_sala = '',  tipo_sala= ''):
        fields = []
        val = []

        if num_asientos !='':
            val.append(num_asientos)
            fields.append('num_asientos = %s')
        if numero_sala !='':
            val.append(numero_sala)
            fields.append('numero_sala = %s')
        if tipo_sala !='':
            val.append(tipo_sala)
            fields.append('tipo_sala = %s')    
           
        val.append(idsala)
        val = tuple(val)         
        try:
            sql = 'UPDATE salas SET ' + ','.join(fields) +' WHERE idsala = %s'

            self.cursor.execute(sql,val)
            self.cnx.commit()

            return self.cursor.rowcount > 0

        except connector.Error as err:
            self.cnx.rollback()
            return(err)

    def delete_sala(self, id):
        try:
            sql = 'DELETE  FROM salas WHERE idsala = %s'
            values = (id,)

            self.cursor.execute(sql, values)
            self.cnx.commit()

            return self.cursor.rowcount > 0
        except connector.Error as err:
            self.cnx.rollback()
            return (err) 
    """
    Modelo asientos:
    """ 
    def create_asiento(self,asiento, fila, salas_idsala):
        try:
            sql = 'INSERT INTO asientos(asiento, fila,salas_idsala) VALUES(%s, %s,%s)'
            values = (asiento, fila,salas_idsala)

            self.cursor.execute(sql, values)
            self.cnx.commit()

            return True
        except connector.Error as err:
            self.cnx.rollback()
            return(err)

    def read_asiento(self, id):
        try:
            sql = 'SELECT * FROM asientos WHERE idasiento = %s'
            values = (id,)
            self.cursor.execute(sql, values)
            sala = self.cursor.fetchone()

            return sala
        except connector.Error as err:
            return (err) 
        

    def read_all_asientos(self):
        try:
            sql = 'SELECT * FROM asientos'
            self.cursor.execute(sql)
            asiento = self.cursor.fetchall()

            return asiento
        except connector.Error as err:
            return (err) 

    def read_all_asientos_por_sala(self, idsala):
        try:
            sql = 'SELECT * FROM asientos WHERE salas_idsala = %s'
            values = (idsala,)

            self.cursor.execute(sql, values)
            asientos = self.cursor.fetchall()

            return asientos
        except connector.Error as err:
            return (err) 

    def obtener_asientos_ocupados(self, idfuncion):
        try:
            sql = 'SELECT asientos_idasiento FROM boletos WHERE id_funciones = %s'
            values = (idfuncion,)

            self.cursor.execute(sql, values)
            asientos = self.cursor.fetchall()

            ids = []

            for a in asientos:
                ids.append(a[0])

            return ids
        except connector.Error as err:
            return (err) 

    def update_asientos(self, idasiento, asiento = '', fila = '', salas_idsala = ''):
        fields = []
        val = []

        if asiento !='':
            val.append(asiento)
            fields.append('asiento = %s')
        if fila !='':
            val.append(fila)
            fields.append('fila = %s')
        if salas_idsala !='':
            val.append(salas_idsala)
            fields.append('salas_idsala = %s')         
           
        val.append(idasiento)
        val = tuple(val)         
        try:
            sql = 'UPDATE asientos SET ' + ','.join(fields) +' WHERE idasiento = %s'

            self.cursor.execute(sql,val)
            self.cnx.commit()

            return self.cursor.rowcount > 0

        except connector.Error as err:
            self.cnx.rollback()
            return(err)

    def delete_asiento(self, id):
        try:
            sql = 'DELETE  FROM asientos WHERE idasiento = %s'
            values = (id,)

            self.cursor.execute(sql, values)
            self.cnx.commit()

            return self.cursor.rowcount > 0
        except connector.Error as err:
            self.cnx.rollback()
            return (err) 
    """
    Modelo boletos:
    """   
    def create_boleto(self,id_funciones,id_salas_asientos, clientes_idcliente,asientos_idasiento):
        try:
            sql = 'INSERT INTO boletos(id_funciones,id_salas_asientos, clientes_idcliente,asientos_idasiento) VALUES(%s, %s,%s,%s)'
            values = (id_funciones,id_salas_asientos, clientes_idcliente,asientos_idasiento)

            self.cursor.execute(sql, values)
            self.cnx.commit()

            return True
        except connector.Error as err:
            self.cnx.rollback()
            return(err)

    def read_boleto(self, id):
        try:
            sql = 'SELECT peliculas.nombre, funciones.fecha, funciones.hora,funciones.salas_idsala, salas.tipo_sala, asientos.asiento FROM boletos JOIN funciones ON boletos.id_funciones = funciones.id_funciones JOIN salas ON boletos.id_salas_asientos = salas.idsala JOIN peliculas ON funciones.idpelicula = peliculas.idpelicula JOIN asientos ON boletos.asientos_idasiento = asientos.idasiento WHERE idboleto = %s'
            values = (id,)
            self.cursor.execute(sql, values)
            boleto = self.cursor.fetchone()

            return boleto
        except connector.Error as err:
            return (err) 
        

    def read_all_boletos(self):
        try:
            sql = 'SELECT  peliculas.nombre, funciones.fecha, funciones.hora,funciones.salas_idsala, salas.tipo_sala, asientos.asiento FROM boletos JOIN funciones ON boletos.id_funciones = funciones.id_funciones JOIN salas ON boletos.id_salas_asientos = salas.idsala JOIN peliculas ON funciones.idpelicula = peliculas.idpelicula JOIN asientos ON boletos.asientos_idasiento = asientos.idasiento'
            self.cursor.execute(sql)
            boleto = self.cursor.fetchall()

            return boleto
        except connector.Error as err:
            return (err) 

    def update_boleto(self, idboleto, id_funciones = '', id_salas_asientos = '', clientes_idcliente = '', asientos_idasiento= ''):
        fields = []
        val = []

        if id_funciones !='':
            val.append(id_funciones)
            fields.append('id_funciones = %s')
        if id_salas_asientos !='':
            val.append(id_salas_asientos)
            fields.append('id_salas_asientos = %s')
        if clientes_idcliente !='':
            val.append(clientes_idcliente)
            fields.append('clientes_idcliente = %s')
        if asientos_idasiento !='':
            val.append(asientos_idasiento)
            fields.append('asientos_idasiento = %s')         
           
        val.append(idboleto)
        val = tuple(val)         
        try:
            sql = 'UPDATE boletos SET ' + ','.join(fields) +' WHERE idboleto = %s'

            self.cursor.execute(sql,val)
            self.cnx.commit()

            return self.cursor.rowcount > 0

        except connector.Error as err:
            self.cnx.rollback()
            return(err)

    def delete_boleto(self, id):
        try:
            sql = 'DELETE  FROM boletos WHERE idboleto = %s'
            values = (id,)

            self.cursor.execute(sql, values)
            self.cnx.commit()

            return self.cursor.rowcount > 0
        except connector.Error as err:
            self.cnx.rollback()
            return (err)  
    """
    Metodo funciones
    """
    def create_funcion(self,idpelicula,fecha, hora, salas_idsala, precio):
        try:
            sql = 'INSERT INTO funciones(idpelicula,fecha, hora, salas_idsala, precio) VALUES(%s, %s,%s,%s,%s)'
            values = (idpelicula,fecha, hora, salas_idsala,precio)

            self.cursor.execute(sql, values)
            self.cnx.commit()

            return True
        except connector.Error as err:
            self.cnx.rollback()
            return(err)

    def read_funcion(self, id):
        try:
            sql = 'SELECT * FROM funciones WHERE id_funciones = %s'
            values = (id,)
            self.cursor.execute(sql, values)
            funcion = self.cursor.fetchone()

            return funcion
        except connector.Error as err:
            return (err) 
        

    def read_all_funciones(self):
        try:
            sql = 'SELECT  id_funciones,nombre,fecha,hora,duracion,sinopsis,clasificacion,genero FROM funciones JOIN peliculas ON funciones.idpelicula = peliculas.idpelicula JOIN generos ON peliculas.generos_idgenero = generos.idgenero'
            self.cursor.execute(sql)
            funcion = self.cursor.fetchall()

            return funcion
        except connector.Error as err:
            return (err)

    def read_all_funciones_por_fecha(self, fecha):
        try:
            sql = 'SELECT  id_funciones,nombre,fecha,hora,duracion,sinopsis,clasificacion,genero FROM funciones JOIN peliculas ON funciones.idpelicula = peliculas.idpelicula JOIN generos ON peliculas.generos_idgenero = generos.idgenero WHERE fecha = %s'
            values = (fecha,)
            
            self.cursor.execute(sql, values)
            funcion = self.cursor.fetchall()

            return funcion
        except connector.Error as err:
            return (err) 

    def read_all_funciones_por_pelicula(self, idpelicula):
        try:
            sql = 'SELECT  id_funciones,nombre,fecha,hora,duracion,sinopsis,clasificacion,genero FROM funciones JOIN peliculas ON funciones.idpelicula = peliculas.idpelicula JOIN generos ON peliculas.generos_idgenero = generos.idgenero WHERE peliculas.idpelicula = %s'
            values = (idpelicula,)
            
            self.cursor.execute(sql, values)
            funcion = self.cursor.fetchall()

            return funcion
        except connector.Error as err:
            return (err) 

    def update_funcion(self, id_funciones, idpelicula = '', fecha = '', hora = '', salas_idsala = '',precio = ''):
        fields = []
        val = []

        if idpelicula !='':
            val.append(idpelicula)
            fields.append('idpelicula = %s')
        if fecha !='':
            val.append(fecha)
            fields.append('fecha = %s')
        if hora !='':
            val.append(hora)
            fields.append('hora = %s')
        if salas_idsala!='':
            val.append(salas_idsala)
            fields.append('salas_idsala = %s')
        if precio!='':
            val.append(precio)
            fields.append('precio = %s')          
           
        val.append(id_funciones)
        val = tuple(val)         
        try:
            sql = 'UPDATE funciones SET ' + ','.join(fields) +' WHERE id_funciones = %s'

            self.cursor.execute(sql,val)
            self.cnx.commit()

            return self.cursor.rowcount > 0

        except connector.Error as err:
            self.cnx.rollback()
            return(err)

    def delete_funcion(self, id):
        try:
            sql = 'DELETE  FROM funciones WHERE id_funciones = %s'
            values = (id,)

            self.cursor.execute(sql, values)
            self.cnx.commit()

            return self.cursor.rowcount > 0
        except connector.Error as err:
            self.cnx.rollback()
            return (err)  

    """
    modelo login iniciar sesion
    """              
    def read_login(self, usuario, contrasena):
        try:
            sql = 'SELECT * FROM clientes WHERE usuario =%s AND contrasena =%s'
            values = (usuario, contrasena)
            
            self.cursor.execute(sql, values)
            funcion = self.cursor.fetchone()

            return funcion
        except connector.Error as err:
            return (err)
