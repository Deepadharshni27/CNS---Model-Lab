from scapy.all import sniff, ARP

arp_table = {}

def detect_arp_spoof(packet):
    if packet.haslayer(ARP) and packet.op == 2: 
        mac_address = packet.hwsrc
        ip_address = packet.psrc

        if ip_address in arp_table and arp_table[ip_address] != mac_address:
            print(f"⚠️ Possible ARP Spoofing detected! IP: {ip_address} is mapped to multiple MACs.")

        arp_table[ip_address] = mac_address

print("Monitoring ARP packets for spoofing...")
sniff(filter="arp", prn=detect_arp_spoof, store=False)
