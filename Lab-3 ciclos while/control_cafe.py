# CONFIGURACIÓN Y CONSTANTES INICIALES
CODIGO_SUPERVISOR = "CAFE2026" 
MAX_INTENTOS = 3 
PESO_OBJETIVO = 500       # Gramos      
TOLERANCIA = 10           # Gramos          
MAX_CONSECUTIVAS = 3      # Defectuosas seguidas que detienen la línea

# ACCESO DEL SUPERVISOR
intentos = 0 
acceso_concedido = False

while intentos < MAX_INTENTOS and not acceso_concedido: 
    codigo = input("Código de supervisor: ") 
    intentos += 1 
    if codigo == CODIGO_SUPERVISOR: 
        acceso_concedido = True 
    else: 
        restantes = MAX_INTENTOS - intentos 
        print(f"Código incorrecto. Intentos restantes: {restantes}") 

if not acceso_concedido: 
    print("Acceso bloqueado. Avise al jefe de planta.") 
else: 
    print("Acceso concedido. Inicie el registro (0 para terminar).") 
    
    # Variables registro de bolsas 
    total_bolsas = 0 
    aceptadas = 0            
    defectuosas = 0          
    peso_acumulado = 0       
    terminar = False 
    consecutivas = 0         
    linea_detenida = False   
    peso_minimo = 0          
    peso_maximo = 0         

    # CICLO DE REGISTRO Y VALIDACIÓN
    while not terminar and not linea_detenida: 
        peso = float(input(f"Peso de la bolsa {total_bolsas + 1} (g): "))
        
        # Validar que el peso no sea negativo
        while peso < 0: 
            print("Peso inválido. Ingrese un valor positivo.") 
            peso = float(input(f"Peso de la bolsa {total_bolsas + 1} (g): ")) 
            
        if peso == 0: 
            terminar = True 
        else: 
            total_bolsas += 1 
            
            # PESO MÍNIMO Y MÁXIMO
            if total_bolsas == 1:
                peso_minimo = peso
                peso_maximo = peso
            else:
                if peso < peso_minimo:
                    peso_minimo = peso
                if peso > peso_maximo:
                    peso_maximo = peso
            
            # CLASIFICAR Y ACUMULAR
            peso_acumulado += peso 
            diferencia = peso - PESO_OBJETIVO
            if diferencia < 0:
                diferencia = -diferencia
                
            if diferencia <= TOLERANCIA:
                aceptadas += 1
                consecutivas = 0  # Reinicia la racha
                print("  OK")
            else:
                defectuosas += 1
                consecutivas += 1 
                print(f"  DEFECTUOSA ({consecutivas} seguidas)") 
                
                if consecutivas == MAX_CONSECUTIVAS:
                    linea_detenida = True

    # REPORTE DEL TURNO
    print("\n--- Reporte del turno ---")
    print(f"Bolsas revisadas: {total_bolsas}")
    print(f"Aceptadas: {aceptadas}")
    print(f"Defectuosas: {defectuosas}")
    

    if total_bolsas > 0:
        porcentaje_defectuosas = (defectuosas / total_bolsas) * 100
        peso_promedio = peso_acumulado / total_bolsas
        
        print(f"Porcentaje de defectuosas: {porcentaje_defectuosas:.1f}%")
        print(f"Peso promedio: {peso_promedio:.1f} g")
        print(f"Peso más bajo: {peso_minimo:.1f} g")  
        print(f"Peso más alto: {peso_maximo:.1f} g")  

    if linea_detenida:
        print("ALERTA: La línea fue detenida.")