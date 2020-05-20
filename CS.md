# Computer Science

## Case Study

### Vocabulario

#### APT

-   Una amenaza persistente avanzada(por Advanced Persistent Threat)
-   conjunto de procesos informáticos
    -   sigilosos orquestados por un tercero
    -   intención y la capacidad de
        -   atacar de forma
            -   avanzada (a través de múltiples vectores de ataque) y
            -   continuada en el tiempo
    -   objetivo determinado
        -   empresa competidora
        -   estado
        -   ...
-   instalado usando exploits que aprovechan [vulnerabilidades](#vulnerabilidad) de la máquina objetivo
-   habitual aprovechar
    -   [vulnerabilidades de día cero](#ataquevulnerabilidad-de-dia-zero)
    -   ataques de abrevadero.

#### Ataques DOS/DDOS

-   un ataque de denegación de servicio
-   ataque a
    -   un sistema de computadoras o
    -   red que
-   causa servicio/recurso sea inaccesible a los usuarios legítimos.
-   provoca la pérdida de la conectividad con la red por el
    -   consumo del ancho de banda de la red de la víctima o
    -   sobrecarga de los recursos computacionales del sistema atacado.
-   Un ejemplo

    -   27 de marzo de 2013,
    -   ataque de una empresa a otra
    -   inundó la red de correos basura
    -   provocando una ralentización general de Internet
    -   llegó a afectar a puntos clave como el nodo central de Londres.

-   se generan mediante la saturación de los puertos con múltiples flujos de información,
    -   servidor se sobrecargue
    -   no pueda seguir prestando su servicio.
-   técnica es usada por
    -   crackers
    -   piratas informáticos
-   A nivel global
    -   problema ha ido creciendo
        -   mayor facilidad para crear ataques
        -   mayor cantidad de equipos disponibles
            -   mal configurados
            -   con fallos de seguridad
    -   Se ve un aumento en los ataques
        -   por reflexión
        -   amplificación por sobre el uso de [botnets](#zombisordenadores-zombis).
            -   DDoS (por sus siglas en inglés, Distributed Denial of Service)
                -   generando un gran flujo de información
                -   varios puntos de conexión
                -   hacia un mismo punto de destino
                -   más común
                    -   [red de bots](#zombisordenadores-zombis)

#### Ataques smurf

-   standard scenario

    -   host A sends an ICMP Echo (ping) request to host B,
    -   triggering an automatic response
    -   time it takes for a response to arrive is used as a measure of the virtual distance between the two hosts.

-   In an IP broadcast network

    -   an ping request is sent to every host
    -   prompting a response from each of the recipients
    -   Smurf attacks, perpetrators take advantage to amplify their attack traffic

-   A Smurf attack scenario can be broken down as follows:

    -   Smurf malware is used to generate a fake Echo request containing a spoofed source IP, which is actually the target server address.
    -   The request is sent to an intermediate IP broadcast network.
    -   The request is transmitted to all of the network hosts on the network.
    -   Each host sends an ICMP response to the spoofed source address.
    -   With enough ICMP responses forwarded, the target server is brought down.
        The amplification factor of the Smurf attack correlates to the number of the hosts on the intermediate network. For example, an IP broadcast network with 500 hosts will produce 500 responses for each fake Echo requests. Typically, each of the relies is of the same size as the original ping request.

It should be noted that, during the attack, the service on the intermediate network is likely to be degraded.

In addition to showing good internet citizenship, this should incentivize operators to prevent their networks from being unwitting Smurf attack participants.

-   To accomplish this you can:
    -   Disable IP-directed broadcasts on your router.
    -   Reconfigure your operating system to disallow ICMP responses to IP broadcast requests.
    -   Reconfigure the perimeter firewall to disallow pings originating from outside your network.

#### Ataque/Vulnerabilidad de dia zero

#### BYOD

#### Cortafuegos

#### Desbordamiento del buffer de la pila

#### Filtrado de paquetes

#### Gestión de eventos e información de seguridad

#### Gusano

#### IDS

#### IM

#### Inclusión en listas blancas

#### Intermediario

#### Inundación SYN

#### IPS

#### Panorama de amenazas

#### Redes robot

#### Robots

#### Script kiddies

#### Servidor proxy

#### Software malicioso/ malware

#### Spam

#### SSL

#### TLS

#### Toolkits

#### Vulnerabilidad

#### Zombis/ordenadores zombis

## OOP
