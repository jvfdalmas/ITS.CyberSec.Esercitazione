from scapy.all import *
from scapy.layers.http import HTTPRequest 
from scapy.layers.http import HTTPResponse

iPkt = 0

def process_packet(packet):
    global iPkt
    iPkt += 1
    print("Ho letto un pkt sulla tua macchina")
    
    if not packet.haslayer(IP):
        return
    
    ip_layer = "PKT # " + str(iPkt) + " | " + "IP_SRC: " + packet[IP].src + " | " + "IP_DST: " + packet[IP].dst +  " | " + "\n" + "PROTOCOLO: " + str(packet[IP].proto) + " | " + "LUNGHEZZA: " + str(packet[IP].len)
    #stampa i dati del layer IP
    print(ip_layer) 

    if packet[IP].proto == 6:
        ip_port = "SOURCE_PORT: " + str(packet[IP].sport) + " | " + "DEST_PORT: " + str(packet[IP].dport)
        print(ip_port)
    
    if packet[IP].dport == 80:
        print("Riconosciuto richiesta HTTP") 
        if packet.haslayer((HTTPRequest)):
            print(packet[HTTPRequest].show()) 
    elif packet[IP].sport == 80:
        print("Riconosciuto risposta HTTP")
        if packet.haslayer(HTTPResponse):
            print(packet[HTTPResponse].show())

    if packet[IP].dport  == 443 or packet[IP].sport == 443:
        print("Riconosciuto pkt TLS".upper())
    
    print("\n")

sniff(iface="enp4s0", filter="tcp", prn=process_packet)
