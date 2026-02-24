import hashlib
import os
import sys
from colorama import Fore, Style, init

# Colorama'yı başlat (Windows'ta renklerin düzgün çalışması için)
init(autoreset=True)

def display_banner():
    """Program başladığında gösterilecek BERITAN Hash Cracker banner'ını görüntüler."""
    banner = f"""
{Fore.CYAN}{Style.BRIGHT}

{Fore.YELLOW}
⠀⠀⠀⠀⠀⢀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠐⡈⠐⠠⢁⠂⠐⢀⣾⣿⡿⠿⠿⠿⣿⣿⣿⣿⣿⡿⠟⠛⠛⠿⣷⡄⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠐⠠⢁⠂⠄⠀⣛⠀⡟⢁⣠⣄⠀⠀⠀⠙⢻⡟⠉⠀⠀⢀⣴⣦⣬⠃⣬⣅⠀⢂⠐⡀⢂⠐⠠⠀⠄⠠⠀⠄⠠⢀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡁⢂⠈⠀⠾⡛⢱⡿⢿⣿⣿⣿⣦⣄⣠⣼⣷⣤⣤⣶⠿⠿⢿⣟⠆⢉⡛⠆⠀⢂⠐⠠⠈⠄⠡⠈⠄⠡⢈⠐⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡐⢀⠂⢠⣾⡟⣸⣰⡿⠁⠄⠀⠙⣿⡇⣿⣿⠸⣿⠁⢀⣀⣀⣙⡸⠎⢿⡆⠀⠂⠌⠠⠁⠌⠠⠁⠌⡐⢀⠂⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠠⠀⠄⠀⠟⡸⢛⣤⣼⣿⣿⣿⣤⣼⠇⣿⣿⠀⢧⣿⣿⣿⣿⣿⣿⣧⣄⠃⠀⢃⠘⡀⢃⠘⡀⠃⠄⠠⢀⠘⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢂⠡⠈⠄⢈⡾⠋⢹⣿⣿⣿⣿⡟⢡⣴⣿⣿⣷⣦⡙⢿⣿⣿⣿⣿⠀⠙⠀⠈⡀⢂⠐⡀⠂⠄⠡⢈⠐⡀⠂⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠄⢂⠡⠀⢸⠀⠀⢸⣿⣿⣿⣿⡀⣿⣿⣿⣿⣿⣿⡇⠸⢿⣿⣿⡟⠀⠀⠀⠀⡐⢀⠂⠅⠡⢈⠐⡀⢂⠐⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠄⡐⠠⠀⠀⠀⠀⠙⠋⠉⠀⠀⠉⠉⠙⠛⠋⠉⠀⠀⠀⠀⠁⠀⠀⠀⠀⢀⠐⠠⠈⠆⡁⢂⡐⡀⠂⠄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢈⠐⠠⠁⠄⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⢀⣀⠀⠀⢀⠂⠌⠠⢁⠆⡐⢀⠆⠄⠡⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠠⠈⠄⠡⢈⠐⡀⠸⣿⣦⡀⠀⠀⠛⠒⠚⠛⠛⠛⠛⠀⢀⣴⣿⠃⠀⠌⡀⠂⠌⡐⢀⠂⡐⠠⡈⠄⡁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠡⢈⠐⡀⠂⠄⠀⢻⣿⣿⣷⣶⣦⣤⣤⣤⣤⣤⣶⣾⣿⣿⡿⠀⠐⠠⢀⠁⢂⠐⡀⠂⠄⠡⢈⠐⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⡐⢀⠂⠄⠡⠈⠄⠘⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⡿⠃⠀⠌⡐⠠⠈⠄⠂⠄⠡⢈⠐⠠⠈⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡐⠠⠈⠄⠡⢈⠐⠀⠀⠙⠃⣿⣿⣿⣿⣿⣿⣿⣿⡗⠋⠀⣤⠀⠀⠀⠡⠈⠄⠡⢈⠑⠠⠈⠌⡁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠄⠡⠈⠄⡁⠂⠀⠀⣤⡀⠀⢻⣿⣿⣿⣿⣿⣿⣿⠇⣠⣾⣿⠀⣰⠀⠀⠀⣈⡀⠀⠈⠀⠁⠢⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡈⠄⠁⠂⠀⠀⠀⠀⢻⣿⣷⠬⠉⠉⠉⠉⠉⠉⠀⠚⢿⣿⣿⢀⣿⡀⠀⠀⢹⣿⣿⣿⣿⣶⡶⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⢸⣧⠘⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⣾⣿⡇⠀⠁⠀⢻⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⣟⡿⠀⠀⠀⠀⣿⣿⣦⠘⣿⣶⠖⣠⠆⠀⠀⢳⣤⡙⢿⣟⣼⣿⣿⡇⠀⠐⡀⠈⣿⣿⣿⣿⠀⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⣿⠃⠀⠀⠀⠀⢿⣿⣿⣷⣌⣿⣾⠏⠀⡀⠀⠸⡿⠿⠾⠿⠿⠿⠿⠷⠀⠀⠄⠀⠸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢠⠀⠀⠈⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⢠⠀⡄⣴⠀⠀⡄⠐⠀⠀⢻⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠠⠀⠀⠀⠀⢀⠀⠠⠀⠄⢂⠐⠠⢈⠐⡈⠐⡀⢂⠐⠘⢷⡭⠂⠄⡁⢂⠀⠈⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠡⠐⠠⠈⡐⠠⠈⠄⠡⠈⠄⡈⠐⡀⠂⠄⠡⠐⠠⠨⠄⠆⠠⠌⠠⠐⠠⢀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀

██████╗░███████╗██████╗░██╗████████╗░█████╗░███╗░░██╗
██╔══██╗██╔════╝██╔══██╗██║╚══██╔══╝██╔══██╗████╗░██║
██████╦╝█████╗░░██████╔╝██║░░░██║░░░███████║██╔██╗██║
██╔══██╗██╔══╝░░██╔══██╗██║░░░██║░░░██╔══██║██║╚████║
██████╦╝███████╗██║░░██║██║░░░██║░░░██║░░██║██║░╚███║
╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{Fore.MAGENTA}{Style.BRIGHT}
         >> ETHICAL HASH CRACKING TOOLBOX <<
         Oluşturan: BERITAN AYDIN
{Style.RESET_ALL}
"""
    print(banner)

def get_hash_type(hash_string):
    """Hash string'inin türünü (MD5, SHA1, SHA256) tahmin eder."""
    hash_length = len(hash_string)
    if hash_length == 32:
        return "md5"
    elif hash_length == 40:
        return "sha1"
    elif hash_length == 64:
        return "sha256"
    else:
        return None

def crack_hash(target_hash, wordlist_path):
    """Verilen hash'i bir kelime listesi kullanarak kırmaya çalışır."""
    hash_type = get_hash_type(target_hash)

    if not hash_type:
        print(f"{Fore.RED}[-] Desteklenmeyen veya geçersiz hash formatı: {target_hash}{Style.RESET_ALL}")
        return

    if not os.path.exists(wordlist_path):
        print(f"{Fore.RED}[-] Kelime listesi bulunamadı: {wordlist_path}{Style.RESET_ALL}")
        return

    print(f"{Fore.YELLOW}[*] Hedef Hash: {target_hash}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}[*] Tahmin Edilen Hash Türü: {hash_type.upper()}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}[*] Kelime Listesi Yolu: {wordlist_path}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}[*] Kırma işlemi başlatılıyor...{Style.RESET_ALL}\n")

    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
            for i, line in enumerate(f):
                password = line.strip()
                if not password: # Boş satırları atla
                    continue

                if hash_type == "md5":
                    hashed_password = hashlib.md5(password.encode('utf-8')).hexdigest()
                elif hash_type == "sha1":
                    hashed_password = hashlib.sha1(password.encode('utf-8')).hexdigest()
                elif hash_type == "sha256":
                    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
                
                # Her 1000 denemede bir ilerleme göster
                if (i + 1) % 1000 == 0:
                    sys.stdout.write(f"\r{Fore.BLUE}[>] {i + 1} kelime denendi...{Style.RESET_ALL}")
                    sys.stdout.flush()

                if hashed_password == target_hash:
                    sys.stdout.write(f"\r{Fore.GREEN}[+] Şifre bulundu! -> {password}{' ' * 20}\n{Style.RESET_ALL}")
                    return password
            
        print(f"\n{Fore.RED}[-] Kelime listesi içerisinde şifre bulunamadı.{Style.RESET_ALL}")
        return None

    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[-] Kullanıcı tarafından durduruldu.{Style.RESET_ALL}")
        return None
    except Exception as e:
        print(f"{Fore.RED}[-] Bir hata oluştu: {e}{Style.RESET_ALL}")
        return None

def main():
    display_banner()

    if len(sys.argv) < 3:
        print(f"{Fore.WHITE}{Style.BRIGHT}Kullanım:{Style.RESET_ALL} python beritan_hash_cracker.py <hedef_hash> <kelime_listesi_yolu>")
        print(f"{Fore.WHITE}{Style.BRIGHT}Örnek:{Style.RESET_ALL} python beritan_hash_cracker.py 5d41402abc4b2a76b9719d911017c592 wordlist.txt")
        sys.exit(1)

    target_hash = sys.argv[1].lower() # Hash'i küçük harfe çevir
    wordlist_path = sys.argv[2]

    found_password = crack_hash(target_hash, wordlist_path)

    if found_password:
        print(f"\n{Fore.GREEN}{Style.BRIGHT}[*] Kırma işlemi başarıyla tamamlandı.{Style.RESET_ALL}")
    else:
        print(f"\n{Fore.RED}{Style.BRIGHT}[*] Kırma işlemi tamamlandı ancak şifre bulunamadı.{Style.RESET_ALL}")
    print(f"\n{Fore.WHITE}{Style.BRIGHT}Oluşturan:{Style.RESET_ALL} BERITAN AYDIN\n")

if __name__ == "__main__":
    main()
