# brug routeren som bridge

På routeren

# nulstil IP på portene
ip addr flush dev eth0   
ip addr flush dev eth1   

# lav bro og tilføj porte
ip link add br0 type bridge   
ip link set eth0 master br0   
ip link set eth1 master br0   

# giv broen en management-IP i samme subnet (valgfrit)
ip addr add 10.0.1.1/24 dev br0   

# tænd alt
ip link set eth0 up   
ip link set eth1 up   
ip link set br0 up   

# routing er ikke nødvendig
sysctl -w net.ipv4.ip_forward=0

På PC1

ip addr add 10.0.1.10/24 dev <pc1_if>   
ip link set <pc1_if> up   
ip route add default via 10.0.1.1   # kun hvis routeren også skal være gateway

På PC2

ip addr add 10.0.1.20/24 dev <pc2_if>   
ip link set <pc2_if> up   
ip route add default via 10.0.1.1   # kun hvis gateway ønskes

Test

# fra PC1
ping 10.0.1.20
# fra PC2
ping 10.0.1.10

Note: Lad ikke begge router-interfaces have IP i samme subnet uden bridge. Det giver ARP-problemer. Proxy ARP virker, men er unødigt bøvlet her.
