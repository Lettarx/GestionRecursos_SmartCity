from skfuzzy import control as ctrl
import skfuzzy as fuzz
import numpy as np
import matplotlib.pyplot as plt

def logica_difusa():
    #Definicion de variables
    hora_dia = ctrl.Antecedent(np.arange(0,24,1),"Hora_dia")
    cant_trafico = ctrl.Antecedent(np.arange(0,11,1),"Cant_trafico")
    clima = ctrl.Antecedent(np.arange(0,11,1), "Clima")
    intensidad = ctrl.Consequent(np.arange(0,101,1),"Intensidad_luces")

    #Definicion de funciones de membresia
    #Hora del dia
    hora_dia['madrugada'] = fuzz.trimf(hora_dia.universe,[0,3,6])
    hora_dia['mañana'] = fuzz.trimf(hora_dia.universe,[5,9,12])
    hora_dia['tarde'] = fuzz.trimf(hora_dia.universe,[12,15,19])
    hora_dia['noche'] = fuzz.trimf(hora_dia.universe,[17,21,23])

    #Cantida de trafico
    cant_trafico['bajo'] = fuzz.trimf(cant_trafico.universe,[0,2,4])
    cant_trafico['medio'] = fuzz.trimf(cant_trafico.universe,[3,5,7])
    cant_trafico['alto'] = fuzz.trimf(cant_trafico.universe,[6,8,10])

    #Clima
    clima['buen'] = fuzz.trimf(clima.universe,[0,2,4])
    clima['normal'] = fuzz.trimf(clima.universe,[3,5,7])
    clima['malo'] = fuzz.trimf(clima.universe,[6,8,10])

    #intensidad
    intensidad['baja']  = fuzz.trimf(intensidad.universe, [0, 25, 50])
    intensidad['media'] = fuzz.trimf(intensidad.universe, [30, 50, 70])
    intensidad['alta']  = fuzz.trimf(intensidad.universe, [60, 80, 100])

    #Definicion de reglas difusas
    reglas = [
        ctrl.Rule(hora_dia['madrugada'] & cant_trafico['bajo'] & clima['buen'], intensidad['baja']),
        ctrl.Rule(hora_dia['madrugada'] & cant_trafico['medio'] & clima['normal'], intensidad['media']),
        ctrl.Rule(hora_dia['madrugada'] & cant_trafico['alto'] & clima['malo'], intensidad['alta']),
        
        ctrl.Rule(hora_dia['mañana'] & cant_trafico['bajo'] & clima['buen'], intensidad['baja']),
        ctrl.Rule(hora_dia['mañana'] & cant_trafico['medio'] & clima['normal'], intensidad['media']),
        ctrl.Rule(hora_dia['mañana'] & cant_trafico['alto'] & clima['malo'], intensidad['alta']),
        
        ctrl.Rule(hora_dia['tarde'] & cant_trafico['bajo'] & clima['buen'], intensidad['baja']),
        ctrl.Rule(hora_dia['tarde'] & cant_trafico['medio'] & clima['normal'], intensidad['media']),
        ctrl.Rule(hora_dia['tarde'] & cant_trafico['alto'] & clima['malo'], intensidad['alta']),
        
        ctrl.Rule(hora_dia['noche'] & cant_trafico['bajo'] & clima['buen'], intensidad['baja']),
        ctrl.Rule(hora_dia['noche'] & cant_trafico['medio'] & clima['normal'], intensidad['media']),
        ctrl.Rule(hora_dia['noche'] & cant_trafico['alto'] & clima['malo'], intensidad['alta']),

        ctrl.Rule(clima['malo'], intensidad['alta']),

        ctrl.Rule(cant_trafico['alto'] & clima['normal'],intensidad['media']),

        ctrl.Rule(hora_dia['mañana'] & clima['buen'], intensidad['baja']),
        ctrl.Rule(hora_dia['tarde'] & clima['malo'], intensidad['media']),
        ctrl.Rule(hora_dia['noche'] & cant_trafico['medio'],intensidad['alta']),
    ]

    sistema_ctrl = ctrl.ControlSystem(reglas)
    sistema = ctrl.ControlSystemSimulation(sistema_ctrl)

    return sistema, intensidad

def calcular_intensidad(sistema, hora, trafico, clima):
    # Asignar valores a las variables de entrada
    sistema.input['Hora_dia'] = hora
    sistema.input['Cant_trafico'] = trafico
    sistema.input['Clima'] = clima

    # Calcular la salida
    sistema.compute()

    return sistema

def observar_intensidad(sistema, intensidad):
    # Configurar el estilo de matplotlib
    plt.style.use('default')
    
    # Crear una nueva figura
    fig = plt.figure(figsize=(8, 4))
    
    # Crear el gráfico
    ax = intensidad.view(sim=sistema)
    
    # Configurar título y etiquetas
    plt.title('Función de membresía de intensidad de luz')
    plt.xlabel('Intensidad (%)')
    plt.ylabel('Grado de membresía')
    
    return plt.gcf()
