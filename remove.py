import shutil
import argparse
import os
userhome = os.path.expanduser("~")
parser = argparse.ArgumentParser(description='Fully purges an installed VM.')
parser.add_argument('name', help="name of virtual machine")

args = parser.parse_args()

env_dir = f"{userhome}/PyVM/Virtual Machines/{args.name}"

if not os.path.isdir(env_dir):
  print("ERROR: No such VM.")
  exit(1)
print("NOTE: Would uninstall apps you installed on your VM. Continue?")
conf_uninstall = False
while not conf_uninstall:
  conf_uninst_opt = input("Confirm [y/n]:").lower()
  if conf_uninst_opt == "y":
    conf_uninstall == True
  elif conf_uninst_opt == "n":
    exit()
  else:
    print(f"{conf_uninst_opt} is not a valid option. Choose y or n (case insensitive).")
print("Uninstalling...")
shutil.rmtree(env_dir)
