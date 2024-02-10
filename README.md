# project-III



VIERNES NOCHE: Funcion que extrae de FourSquare
                Funcion que guarda en DB que voy a crear
                Funcion que extrae de DataBase compañias 


SABADO 20:00 -- tener los mini radios definidos -- TODA LA PARTE 1
DOMINGO -- 




For this project we need to find a suitable place to our company. 

In the company there is : 

People want:

----------------------------------  PARTE 1  ---------------------------------------------

- APROACH: Que cumplan todas estas - quiza dentro de cada una podemos decir que umplan 1 o otra 

**MAINTENANCE**
- 1. buscar los estadios deportes en general 
     10051	Arts and Entertainment > Stadium
          
**DOG PARK**
    - Dog park
        16033	Landmarks and Outdoors > Park > Dog Park
**CEO**
    - Vegan o X restaurant (Opciones)
        13377	Dining and Drinking > Restaurant > Vegan and Vegetarian Restaurant

**PARTY**

   10032	Arts and Entertainment > Night Club
   13003	Dining and Drinking > Bar


***METEMOS UN CUANTAS EMPRESAS DE LA DB EMPRESAS HAY AQUI?¿** 

--------------------------- PARTE 2 --------------------------------------------------

4. De los hot spots hemos hecho una lista de posibles sitios. 

    - Algo tengo que hacer para generar radios mas pequeños dentro de cada uno de ellos y quiza hacer el analisis aqui en plan o quiza con el de los hot spot ya esta - a esto datle una vuelta 

5. Con mis X radios ya mas pequeñitos - estraer todos los (de abajo) para cada uno de los puntos: 

    veremos cuantos de cada hay en cada sector -- generamos un mapa de calor
    
    - Companies Data base: 
    
          - Design Companies 
          - Tech startups raised at least 1M
          
    - API FourSquare: 
    
           - Airpot or Trainstation
           - Starbuks near 
           
           
6. Seleccionamos 1 y justificamos

Si te quieres poner super creativa - como ultimo cirterio hacer un mapa de SOL y la decision definitiva sera el que tenga mas areas de sol 


1. Extraer la informacion que queremos de Foursquare - crear una funcion que la extraiga
  - Extraer todos los estadios de basket --> analizar que campos
2. Crear una funcion que los meta en Mongo

3. Extraer todos los MUST a partir de 



--------PARTE 1 un poco liosa --------------------------------------------

Fist we have identify the conditions that MUST. The Indispensable ones: 

-  basketball stadium < 10 km
-  At least 1 vegan restaurant? change to other food? sushi? 
-  Somethig for a Dog - una carniceria? - 
-  At least one party club 

Fist we will filter locations that meet all 4 

- Encontrar areas que cumplan estos 4 criterios en un radio de X . Como el estadio de basket es el mas restictivo quiza podemos empezar por 

- 1. Encontrar estadios de basket, a partir de ahi en un radio de 10km que esten los otros tres 

- Find all -- basket stadiums - point del basket stadium - to list o to iterable
- for all elements in the iterable list of basket stadiums - check if in a circle of 10k of this point there is :



    *Keep in mind that i only have X requests for FourSquare so i nedd to think what do i really need so may be is beter no limit the busqueda to a given area/city
    
    
    ** TAMBIEN va a ser imporante guardar toda la info que cojamos de foursquares para asi luego referirnis a la base de datos en lugar de hacer requests a la API, la cosa es primero determinar que vamos a pedir y luego como y como guardarlas 
    
    Lo de mirar el link que decia leo es buena, bueno no se para que sirve pero lo veremos 
    
    - We are limiting the busqueda to X City/Country? 
    Quiza podemos limitar la busqueda despues de esto: 
    
    Empezamos con estadios porque es de lo que menos hay 

First dorm FourSquares 

    - Buscar (TODOS?) los estadios? y descargarlos? cuidado-- quiza hay que limitar 

    1. Find Baskeball stadiums - grupo de estadios - Tenemos una lista de estadios
    
        10061	Arts and Entertainment > Stadium > Basketball Stadium
        
    2. Por cada punto de estados vamos a definir un radio de 10km donde donde miraremos si estan estas tres condiciones: 
    
    SACAME de este punto con radio X todos los --- vegano 
    
    2. Por cada punto de estadios, chekea si --> Tienen las tres condiciones. la cosa es como quremos los 3 puntos que esten de cerca? Como sacamos la info para luego ir analizandola? 
    
   **España**

Quiza no hay que generar los espacios como tal sino simplementemente ir a four square y en la busqueda pedir con este punto [El estadio] a un ratio de X km buscame ---
             
DRAMA: No quiero solo que haya estas tres cosas sino que estas tres cosas no esten locamente separadas, quiero decir que si cada cosa esta en una punta luego no podre decir que lo tienen cerca - bueno a ver si que puedo pero no se yo... 
            
    
    - Condition1 and Condition2 and Condition 3
 
 If they evaluate to true -- save them into SUITABLE if not - nothing (fuera ) 
 
 Form our SUITABLE selecction:
 
 For remaining company employees: 
 
     - 25% [Designers] --> Other Design Companies 
     - 25% [A.M] --> Need to travel (Airpot or Trainstation)
     - 18% [Data Analist] --> Nothing? 
     - 18% [Developers Front/Back] --> tech startups raised at least 1M
     - 13% [Executives] --> Starbuks near 
     
HOW we are gona meet this conditions : 

    - Companies Data base: 
    
          - Design Companies 
          - Tech startups raised at least 1M
          
    - API FourSquare: 
    
           - Airpot or Trainstation
           - Starbuks near 




- Hemos encontrado X areas que cumplen estos cuatro criterios 
