# ROS sobre Minitractor Corta Cesped
Software, hardware y esquemas para la construcción de un tractor con piloto automático. Uno de los principales objetivos es que este y todos los demás documentos queden en español.


![Tractor que presento Matt en la AgBot 2019](https://github.com/ros-agriculture/ros_lawn_tractor/blob/master/ros_lawn_tractor.png)

https://youtu.be/MUbRY6LcDrI

## Como usar el simulador?
El simulador usa ROS Navigation y TEB Planner: https://youtu.be/JuZ8gpx9oO4

## Simulación en la nueve
Tutorial sobre utilizacion del simulador de la cortadora de pasto: https://www.loom.com/share/c9868920819a466d827d522a2aa76c8e  
Archivo ROSJect con el simulador ya cargado:  http://www.rosject.io/l/8e95478/

## Instalación local
If you don't have a Ubuntu 16.04 computer running ROS Kinetic.  This script https://github.com/linorobot/rosme provided by LinoRobot (https://linorobot.org/) will install ROS for you.

This simulator runs on Ubuntu 16.04 and ROS Kinetic.

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

## Licensing
ros_lawn_tractor esta bajo licencia MIT.

Todo usuario de este software deberá indemnify y mantener libre de daño y responsabilidad ROS Agriculture O&Uuml;. y sus directores, oficiales, empleado, accionistas, afiliados, sub-contratistas, y clientes de y contra todo tipo de alegatos, reclamos, acciones legales, petición, demandas, daños, reclamos, obligaciones, perdidas, acuerdo, juicios, costos, expensas (incluidas comisiones y costos de abogados) que se pudieran generar de forma directa o indirecta del uso de este software por el usuario o quien fuera.

ESTO ES SOFTWARE DE CALIDAD ALFA PARA USO EN INVESTIGACIÓN SOLAMENTE. ESTO NO ES UN PRODUCTO. USTED ES RESPONSABLE DE CUMPLIMENTAR LAS LEYES LOCALES Y REGULACIONES APLICABLES. NO HAY GARANTÍA DE NINGÚN TIPO SOBRE ESTOS PRODUCTOS.
