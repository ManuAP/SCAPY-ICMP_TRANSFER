<!DOCTYPE html>
<html>
<body>
	<h1>ICMP Sniffer y Sender en Python y Bash</h1>
	<p>Este proyecto incluye dos scripts: <code>sniffer.py</code> y <code>sender.sh</code>.</p>
  <h2>Instalación</h2>
<p>Para ejecutar el script de sniffer, se necesitan las siguientes dependencias de Python:</p>
<ul>
	<li>Scapy: <code>pip install scapy</code></li>
</ul>
<p>Para ejecutar el script de sender, no se necesitan dependencias adicionales.</p>

<h2>Uso</h2>
<h3>Sniffer</h3>
<p>El script de sniffer se puede ejecutar de la siguiente manera:</p>
<code>sudo python sniffer.py</code>
<p>El script escuchará en la interfaz de red <code>tun0</code> y buscará paquetes ICMP que contengan una carga útil de 4 bytes.</p>
<p>Una vez que se detecta un paquete válido, el script imprimirá la carga útil descifrada en la consola.</p>

<h3>Sender</h3>
<p>El script de sender se puede ejecutar de la siguiente manera:</p>
<code>./sender.sh [datos]</code>
<p>Este script acepta un argumento de entrada (los datos que se deben enviar) y luego divide los datos en fragmentos de dos bytes y los envía como una carga útil en paquetes ICMP usando el comando <code>ping</code>. Cada paquete ICMP contiene solo una parte de los datos y, por lo tanto, se envían múltiples paquetes para enviar los datos completos.</p>
<p>Nota: Asegúrese de reemplazar <code>[DESTINATION_IP]</code> con la dirección IP del destino en el archivo <code>sender.sh</code>.</p>

<h2>Consideraciones adicionales</h2>
<p>Este proyecto es solo un ejemplo de cómo se pueden enviar y recibir datos a través del protocolo ICMP utilizando scripts en Python y Bash. Tenga en cuenta que el uso de ICMP para transmitir datos no es una práctica recomendada y puede ser detectado por sistemas de seguridad y firewalls.</p>
</body>
</html>
