# Magnet2Torrent
Script para convertir de enlace Magnet a archivo .torrent a través de magnet-to-torrent.com
*No tengo afiliación con el sitio.*

El script funciona con `./magnet.py -m [enlace magnet]` y descarga el archivo .torrent en la carpeta donde se encuentra el script.

La implementación es pobre y tiene muchas dependencias para lo que hace, pero busco simplificarlo a futuro. Mis disculpas también a magnet-to-torrent.com y agradecimientos pues sin ellos no funcionaría.

Actualmente utiliza las dependencias de **pip**:
- wget
- requests
- urllib2
- argparse

Algunas de las cosas que planeo hacer son:
- Eliminar las dependencias de wget y requests haciendo uso único de urllib2.
- Permitir elegir el directorio donde se descarga el archivo .torrent
