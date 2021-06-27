print("Bienvenido, aquí puede consultar por un contacto de su agenda");
            
            def validar(contactos):
                try:
                    (contactos)
                    return True
                                        
                except ValueError:
                    return False 
            
            contacto                = contact()
            contacto.ID             = input("Ingrese un identificador al nuevo contacto:  ");
            contacto.NOMBRE_CONTACT = input("Ingrese el nombre al nuevo contacto:         ");
            contacto.TELEFONO       = input("Ingrese el telefono al nuevo contacto:       ");
            contacto.DIRECCION      = input("Ingrese la dirección al nuevo contacto:      ");
            contactos.append(contacto)
            

