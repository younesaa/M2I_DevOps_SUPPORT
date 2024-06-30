import subprocess
import platform
import datetime

def update_software():
    """ Vérifie et installe les dernières mises à jour pour les logiciels installés. """
    if platform.system() == "Windows":
        result = subprocess.run(["powershell", "-Command", "Get-WindowsUpdate"], capture_output=True, text=True)
        if "UpdatesAvailable: False" not in result.stdout:
            subprocess.run(["powershell", "-Command", "Update-Module"], check=True)
            subprocess.run(["powershell", "-Command", "Install-Module -Name PSWindowsUpdate; Get-WindowsUpdate -Install"], check=True)
        else:
            print("Le système d'exploitation est déjà à jour.")
    if platform.system() == "Linux":
        result = subprocess.run(["sudo", "apt-get", "upgrade", "--dry-run"], capture_output=True,text=True)
        if "0 mis à jour" not in result.stdout:
            subprocess.run(["sudo", "apt-get", "update"], check=True)
            subprocess.run(["sudo", "apt-get", "upgrade", "-y"], check=True)
        else:
            print("Le système d'exploitation est déjà à jour.")

def clean_temp_files():
    """ Supprime les fichiers temporaires qui ne sont plus nécessaires. """
    if platform.system() == "Windows":
        #subprocess.run(["del", "/f", "/s", "/q", "%temp%\\*"], shell=True, check=True)
        pass
    elif platform.system() == "Linux":
        subprocess.run(["sudo", "rm", "-rf", "/tmp/*"], check=True)

def check_system_integrity():
    """ Exécute des outils de vérification du système pour détecter et réparer les problèmes potentiels. """
    if platform.system() == "Windows":
        subprocess.run(["sfc", "/scannow"], shell=True, check=True)
    elif platform.system() == "Linux":
        subprocess.run(["sudo", "touch", "/forcefsck"], check=True)
        subprocess.run(["sudo", "reboot"], check=True)

def main():
    report_file = "maintenance_report.txt"
    with open(report_file, "w") as file:
        file.write("Début de la maintenance: " + str(datetime.datetime.now()) + "\n")

        try:
            file.write("\nMise à jour des logiciels...\n")
            update_software()
            file.write("Mise à jour des logiciels effectuée.\n")
        except subprocess.CalledProcessError as e:
            file.write(f"Erreur lors de la mise à jour des logiciels: {e}\n")

        try:
            file.write("\nNettoyage des fichiers temporaires...\n")
            clean_temp_files()
            file.write("Nettoyage des fichiers temporaires effectué.\n")
        except subprocess.CalledProcessError as e:
            file.write(f"Erreur lors du nettoyage des fichiers temporaires: {e}\n")

        try:
            file.write("\nVérification de l'intégrité du système...\n")
            check_system_integrity()
            file.write("Vérification de l'intégrité du système effectuée.\n")
        except subprocess.CalledProcessError as e:
            file.write(f"Erreur lors de la vérification de l'intégrité du système: {e}\n")

        file.write("\nFin de la maintenance: " + str(datetime.datetime.now()) + "\n")

    print(f"La maintenance est terminée. Veuillez consulter le fichier '{report_file}' pour les détails.")

if __name__ == "__main__":
    main()
