from os import system
from shutil import copyfile

system("curl -o jamnik1.png https://szmatoland.github.io/haha.png")

for i in range(2,101):
    copyfile("jamnik1.png", f"jamnik{i}.png")