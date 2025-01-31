import re
from collections import Counter

def extract_attacking_ips(file_path, target_ip):
    ip_pattern = re.compile(r'IP (\d+\.\d+\.\d+\.\d+)\.\d+ > ' + re.escape(target_ip))
    ip_counter = Counter()
    
    with open(file_path, 'r') as file:
        for line in file:
            match = ip_pattern.search(line)
            if match:
                src_ip = match.group(1)
                if src_ip != target_ip:  # Escludi il tuo IP
                    ip_counter[src_ip] += 1
    
    return ip_counter

def main():
    file_path = "./Report/filedump.txt"  # Cambia con il tuo file
    target_ip = "10.8.0.6"  # Il tuo IP
    
    attackers = extract_attacking_ips(file_path, target_ip)
    
    print("IP attaccanti e numero di tentativi:")
    for ip, count in attackers.most_common():
        print(f"{ip}: {count} tentativi")

if __name__ == "__main__":
    main()