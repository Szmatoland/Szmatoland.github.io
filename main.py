import subprocess
import shutil
import os

# Get the path to the current user's desktop
desktop = os.path.join(os.environ['USERPROFILE'], 'Desktop')
target_base = os.path.join(desktop, "jamnik")

try:
    # Download the first image directly to the desktop
    first_image = f"{target_base}1.png"
    subprocess.run(["curl", "-s", "-o", first_image, "https://szmatoland.github.io/haha.png"], check=True)
    
    # Create 99 copies on the desktop
    for i in range(2, 101):
        shutil.copyfile(first_image, f"{target_base}{i}.png")
        
except Exception as e:
    # This helps you debug if something goes wrong
    with open(os.path.join(desktop, "error_log.txt"), "w") as f:
        f.write(str(e))
