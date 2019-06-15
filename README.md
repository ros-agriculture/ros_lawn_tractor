# ROS sobre Minitractor Corta Cesped
Este repositorio tiene como objetivo contener el software, hardware, esquemas del proceso de desarrollo y la experiencia misma de la implementación ROS en un minitractor corta cesped (pasto).

![Tractor que presento Matt en la AgBot 2019](https://github.com/ros-agriculture/ros_lawn_tractor/blob/master/ros_lawn_tractor.png)

https://youtu.be/MUbRY6LcDrI

## Contexto.
Durante los últimos tres años he asistido a la AgBot, pude constatar personalmente el crecimiento de ROS en la escena de robotización de agro y en estas reuniones conocí a Matt Droter. Como una cosa lleva a la otra Matt se ofreció a darnos una mano en el desarrollo de un prototipo y los que participamos en este proyecto creemos que es algo muy importante para el sector agropecuario y digno de dedicar tiempo. Claramente como objetivo principal es todos los documentos queden en español y posteriormente si nos da tiempo la vida en portugués (brasilero).

## Herramientas.
Para facilitar el trabajo en grupo y a distancia trabajamos en las siguientes plataformas:
Grupo Whatsapp ROS Agricultura Argentina.
https://chat.whatsapp.com/FK1hUuH3ac3ExXbGrR0gs1
Grupo SLACK ROS Agricultura Argentina.


## Como usar el simulador?
El simulador usa ROS Navigation y TEB Planner: https://youtu.be/JuZ8gpx9oO4

## Simulación en la nueve
Tutorial sobre utilizacion del simulador de la cortadora de pasto: https://www.loom.com/share/c9868920819a466d827d522a2aa76c8e  
Archivo ROSJect con el simulador ya cargado:  http://www.rosject.io/l/8e95478/

## Instalación local
Si Usted no tiene Ubuntu 16.04 instalado en su comutadora corriendo ROS Kinetic.  Este código https://github.com/linorobot/rosme de LinoRobot (https://linorobot.org/) instalará ROS por usted.

Este simulador corre en Ubuntu 16.04 y ROS Kinetic.

<pre>

prompt$ cd catkin_ws/src
prompt/catkin_ws/src$ git clone https://github.com/ros-agriculture/ros_lawn_tractor.git
prompt/catkin_ws/src$ git clone https://github.com/bsb808/geonav_transform.git
prompt/catkin_ws/src$ cd ..
prompt/catkin_ws$ rosdep update
prompt/catkin_ws$ rosdep install -y --from-paths . --ignore-src --rosdistro ${ROS_DISTRO}
prompt/catkin_ws$ sudo apt-get install python-catkin-tools
prompt/catkin_ws$ catkin build
prompt/catkin_ws$ source devel/setup.bash
#Add new catkin build source to your startup script.
prompt/catkin_ws$ echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
prompt/catkin_ws$ roslaunch lawn_tractor_sim lawn_tractor_sim.launch
</pre>

## Docker
If you have docker installed skip to Download Start File.<br />
<br />
**Install Docker** <br />
Docker install instructions - https://docs.docker.com/install/ <br />
<br />

**Download Start File**<br />
<pre>
prompt$ wget https://raw.githubusercontent.com/ros-agriculture/ros_lawn_tractor/master/docker/start.sh
prompt$ chmod +x start.sh
prompt$ ./start.sh
</pre>
..... wait for image to download ......
<pre>
docker/prompt$ roslaunch lawn_tractor_sim lawn_tractor_sim.launch
</pre>

<br /><br />
<br /><br />

## Licenciamiento
ros_lawn_tractor esta bajo licencia MIT.

Todo usuario de este software deberá indemnify y mantener libre de daño y responsabilidad ROS Agriculture O&Uuml;. y sus directores, oficiales, empleado, accionistas, afiliados, sub-contratistas, y clientes de y contra todo tipo de alegatos, reclamos, acciones legales, petición, demandas, daños, reclamos, obligaciones, perdidas, acuerdo, juicios, costos, expensas (incluidas comisiones y costos de abogados) que se pudieran generar de forma directa o indirecta del uso de este software por el usuario o quien fuera.

ESTO ES SOFTWARE DE CALIDAD ALFA PARA USO EN INVESTIGACIÓN SOLAMENTE. ESTO NO ES UN PRODUCTO. USTED ES RESPONSABLE DE CUMPLIMENTAR LAS LEYES LOCALES Y REGULACIONES APLICABLES. NO HAY GARANTÍA DE NINGÚN TIPO SOBRE ESTOS PRODUCTOS.
