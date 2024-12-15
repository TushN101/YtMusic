import os
import subprocess

# Define paths
documents_path = os.path.join(os.path.expanduser("~"), "Documents")
foldername = "YtMusic-Vault"
folder_path = os.path.join(documents_path, foldername)

RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
BLUE = "\033[34m"

def print_header():
    print(f"{CYAN}{BOLD} ========================================{RESET}")
    print(f"{CYAN}{BOLD}         ~  Welcome to YtMusic  ~        {RESET}")
    print(f"{CYAN}{BOLD} ========================================{RESET}\n")

def check_folder():
    if not os.path.exists(folder_path):
        print(f"{YELLOW} [-] Vault folder not found at {folder_path}, creating now...{RESET}")
        try:
            os.makedirs(folder_path)  # Create the folder if it doesn't exist
            print(f"{GREEN} [+] Vault folder successfully created at: {folder_path}{RESET}")
        except Exception as e:
            print(f"{RED} [CRITICAL] Failed to create vault folder: {e} | Exiting..{RESET}")
            exit(1)
    else:
        print(f"{GREEN} [+] Found the vault folder at: {folder_path}{RESET}")

def check_package(package_name, failcommand):
    print(f"{YELLOW} [?] Verifying if {package_name} is installed...{RESET}")
    result = subprocess.run(["where", package_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    if result.returncode == 0:
        print(f"{GREEN} [+] {package_name} is already installed.{RESET}")
    else:
        print(f"{RED} [CRITICAL] {package_name} not found.{RESET}")
        print(f"{RED} [CRITICAL] Install it using: {failcommand}{RESET}")
        exit(1)

def download_audio_yt(url):
    import yt_dlp
    print(f"{CYAN}\n [+] Preparing to download audio from: {url}{RESET}")
 
    ydl_opts = {
        'format': 'bestaudio/best', 
        'outtmpl': os.path.join(folder_path, '%(title)s.%(ext)s'), 
        'quiet': True,
        'ignoreerrors': True
    }
 
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            os.system("cls")
            print_header()
            print(f"{GREEN} [+] Download completed successfully!{RESET}")
        except Exception as e:
            print(f"{RED} [CRITICAL] Failed to download: {e}{RESET}")

def format_playlist_folder():
    try:
        os.system("cls")
        print_header()
        print(f"{CYAN} [+] Formatting playlist folder at: {folder_path}{RESET}")
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"{GREEN} [+] Deleted: {filename}{RESET}")
        print(f"{GREEN}\n [+] Folder {folder_path} is now empty!{RESET}")
    except Exception as e:
        print(f"{RED} [CRITICAL] Failed to format the folder: {e}{RESET}")

def show_menu():
    print(f"\n{BLUE} ===== YtMusic-Vault Menu ====={RESET}")
    print(f"{GREEN} 1.{RESET} Add music to library")
    print(f"{GREEN} 2.{RESET} Open playlist folder")
    print(f"{GREEN} 3.{RESET} Open music player")
    print(f"{GREEN} 4.{RESET} Format playlist folder (Delete all files)")
    print(f"{GREEN} 5.{RESET} Exit")
    print(f"{CYAN} ============================={RESET}")

def handle_menu_choice(choice):
    if choice == "1":
        youtube_url = input(f"{CYAN}\n [-] Enter the YouTube URL to download audio: {RESET}").strip()
        if youtube_url:
            download_audio_yt(youtube_url)
        else:
            print(f"{RED} [!] Invalid URL. Please try again.{RESET}")
    
    elif choice == "2":
        os.system("cls")
        print_header()
        print(f"{CYAN} [+] Opened the playlist folder: {folder_path}{RESET}")
        subprocess.Popen(f'start {folder_path}', shell=True)

    elif choice == "3":
        os.system("cls")
        print_header()
        print(f"{CYAN} [+] Opening VLC with the folder: {folder_path}{RESET}")
        print(f"{YELLOW} [?] Toggle playlist view using Ctrl+L{RESET}")
        try:
            subprocess.Popen(
                [r"C:\Program Files\VideoLAN\VLC\vlc.exe", "--no-play-and-exit", "--playlist-tree", folder_path],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
        except Exception as e:
            print(f"{RED} [CRITICAL] Failed to open VLC: {e}{RESET}")

    elif choice == "4":
        confirm = input(f"{YELLOW}\n [!] Are you sure you want to delete all files in the playlist folder? (y/n): {RESET}").strip().lower()
        if confirm == 'y':
            format_playlist_folder()
        else:
            print(f"{GREEN} [!] Action canceled.{RESET}")
    
    elif choice == "5":
        print(f"\n{GREEN} [+] Exiting... Thank you for using YtMusic!{RESET}\n\n")
        exit(0)

    else:
        print(f"{RED} [!] Invalid choice. Please select a valid option.{RESET}")

def main():
    os.system("cls")
    print_header()

    check_folder()

    check_package("yt-dlp", "pip install yt-dlp")

    while True:
        show_menu()
        choice = input(f"{CYAN}\n [+] Please select an option (1/2/3/4/5): {RESET}").strip()
        handle_menu_choice(choice)

if __name__ == "__main__":
    main()
