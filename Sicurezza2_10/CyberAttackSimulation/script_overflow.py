import subprocess
import os

def load_ips(file_path):
    """Legge gli IP da un file di testo."""
    with open(file_path, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def run_ab_test(ip):
    """Esegue il comando ab e salva il risultato in un file separato per ogni IP."""
    command = f"ab -n 500 http://{ip}:8888/p1.html"
    output_file = f"ab_test_report_{ip}.txt"
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        with open(output_file, 'w') as f:
            f.write(f"Test per {ip}\n{'='*50}\n")
            f.write(result.stdout)
            f.write("\n" + "-"*50 + "\n")
    except Exception as e:
        print(f"Errore durante il test per {ip}: {e}")

if __name__ == "__main__":
    input_file = "./IP_List/chosen-ip.txt"  # File con gli IP
    
    ip_list = load_ips(input_file)
    
    for ip in ip_list:
        run_ab_test(ip)
    
    print("Test completati. Report salvati in file separati per ogni IP.")