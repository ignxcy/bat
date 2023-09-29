#!/usr/bin/python3 
import os
import sys
import subprocess

def rootcheck():
    if os.geteuid() == 0:
        print("E: Please do not run this script as root!")
        sys.exit(1)

def install(package):
    try:
        user_home = os.path.expanduser("~")
        package_directory = f"{user_home}/bat/{package}"

        if os.path.exists(package_directory):
            print(f"The package directory '{package_directory}' already exists. Updating...")
            os.chdir(package_directory)  # Change the current working directory here
            subprocess.run("git pull", shell=True, check=True)
        else:
            clone_command = f"git clone https://aur.archlinux.org/{package}.git {package_directory}"
            subprocess.run(clone_command, shell=True, check=True)

        pkgbuild_found = False
        for root, dirs, files in os.walk(package_directory):
            if 'PKGBUILD' in files:
                pkgbuild_found = True
                break

        if not pkgbuild_found:
            print("Error: PKGBUILD file does not exist.")
            sys.exit(1)

        print("Running makepkg -sri...")
        subprocess.run("makepkg -sri", shell=True, check=True)

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print("Something went wrong during package installation.")
        sys.exit(1)

if __name__ == "__main__":
    rootcheck()

    if sys.argv[1] == "":
        print("Usage: bat-install {package}")
        sys.exit(1)

    package = sys.argv[1]
    install(package)
