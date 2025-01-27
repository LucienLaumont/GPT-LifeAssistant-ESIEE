import subprocess
import os

def run_vite_dev():
    # Set the path to the project directory
    project_dir = r"C:\Theo\School\ESIEE\Annee\E5\LLM\GPT-LifeAssistant-ESIEE\DailyAssistant\app\project"
    
    # Change the working directory to the project folder
    os.chdir(project_dir)

    try:
        # Run the 'npm run dev' command using the shell
        subprocess.run("npm run dev", shell=True, check=True)
    except FileNotFoundError as e:
        print(f"Error: {e}. This could mean that 'npm' is not installed or not in the system's PATH.")
    except subprocess.CalledProcessError as e:
        print(f"Error while running the command: {e}")

if __name__ == "__main__":
    run_vite_dev()

