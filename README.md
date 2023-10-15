# Preface

> This project is clone project of the `AirBnB` platform, built by `Python` programming language


---


# AirBnB

  **AirBnB is an online platform that allows property owners to list their place as holiday accommodation and allows travellers to find a place to stay while they are away from home**.

---

# What is AirBnB - The Console:


**AirBnb Console is a command line interpreter that works in the server side to mange and control the platform componants, which build on `python3`**.


**AirBnB Console provides a bunch of services, descriped below**


## Serives:

- Create a new object(ex: a new User or a new Place)
- Retrive an object from a file, database etc...
- Do operations on object(count, compute stats, etc..)
- Update attributes of an object
- Destroy an object

<sub>Those Seriives will be discussed more below</sub>


---


## How to Use:


### Installing and Runing the Console:


**first**:  clone the project repository


> git clone <project_url>


**then*:  from the root of the project, run the `console.py` file


> python3 console.py


<sub>This will run interactive session for you</sub>


> echo "command | script" | ./console.py


<sub>For the non-interactive session</sub>


---


### Services:


**The Console provides a bunch of services which ca be used to manage the server side of the projects and for the testing and debuging perposes. Each service of the following can be run by a `ClassName.service(attrs)` way or by `service ClaseName attrs. more inforamtion on the help bage of each service**


- **Create:**


Creates a new instance of the provided class name.


> create User


for example will creates a new instances of the `User` object and prints its `id`.


- **Retrive an object information:**


Display the provided BnB object instance inforamtions, there are two services for this process, `show` and `all`


**show** will display information about specific BnB object instance, for example:


> show User <user_id>


> User.show(<user_id>)


will dispaly the information on the `user` that has the is `user_id`


on the other hande **all** will dispaly the information about all the instance of the BnB objects or a specific object name, see example below:


> all


> all Place


> Place.all()


The first one will shows all the information about BnB objects instance regurdless of thier class name, the last tow will do the same except for the instance of the `Place` object



- **Operate on objects:**


The oprations provided by `The Console` are:


**count**: calcuate the number of instances of given BnB object


> City.count()


Will dispaly the current number of the instance of the `City` object


**update**: updates the provided instance information, there are couple of ways to update instance information by `The Console`:


1. One attribute ber time


> update User <user_id > <attribute> <value>


This will updates the instance of the `User` by the new <value> of the <attribute>


2. Update using key:value pair


> User.update(<user_id>, {key:value})


**destroy**: to delete an instance


> destroy Review <review_id>


This will delete the review that has the id <review_id> from the BnB object Review.



For more inforamtion and excplanation you do the help function


> help


to see all the services


> help <service_name>


to see the information about specific one.