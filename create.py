import venv
import platform
import argparse
import os
userhome = os.path.expanduser("~")
parser = argparse.ArgumentParser(description='Create a new VM for running easily on your system.')
parser.add_argument('name', help="name of virtual machine")
parser.add_argument('--minimal', help="do not install pip CLI installer", action="store_true")

args = parser.parse_args()

env_dir = f"{userhome}/PyVM/Virtual Machines/{args.name}"

print(f"Setting up {platform.system()} VM as {args.name}...")
venv.create(env_dir, system_site_packages=False, clear=False, symlinks=False, with_pip=not args.minimal, prompt="[Virtual Machine] ", upgrade_deps=False)
print(f"Installed: {platform.system()} -> {env_dir}")
if os.name == "nt":
   print(f"""To start:
   - Command Prompt: run {env_dir}\\Scripts\\activate.bat (deactivate.bat to go back to host)
   - PowerShell: run {env_dir}\\Scripts\\activate.ps1 (deactivate.ps1 to go back to host)

To install programs, copy them to {env_dir}\\Scripts.""")
else:
   print(f"To start, run: bash --rcfile {env_dir}/Scripts/activate.sh\nTo go back to host, run deactivate.sh.\nTo install programs, copy them to {env_dir}\\Scripts.")
