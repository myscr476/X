#pylint:disable=W0311
'''
A interactive termination for Android and Windows.
Created by Athaya.
'''
#pylint:disable=C0302
#pylint:disable=C0103
# Setup
# Built in Python

import webbrowser
import time
import datetime
import os
from urllib.parse import urlparse, quote, urlencode
import platform
import requests
import random
import re
from datetime import datetime
import subprocess
import sys
import difflib
from importlib.metadata import distributions

username = "local"
cdirectory = "C:\\Users" if os.name == 'nt' else "/storage/emulated/0/X#init"
default_home = "/storage/emulated/0/X#init" if os.name != 'nt' else r"C:\Users"
answerrepo = "local-repo"
userid = "ID001"
repos = [
    "sysrep",
    "termux-official-repo",
    "x-repo",
    "locate.repo.all.90repo",
    "local-repo"
]
prompt = "$"
history = []
url = ""
last_command = ""
pkginstaller = "no"
pkginstallera = "segfault"
available_package = ["sys", "pyrun", "lv", "x#builder", "xpackage", "$pkg", "pip"]
commands = [
    ".",
    ".safe",
    "exit",
    "joingr",
    "information",
    "mkdir",
    "dir",
    "help",
    "w/",
    "s/",
    "c-repo",
    "reposhow",
    "id",
    "history",
    "insta",
    "clear",
    "whoami",
    "setname",
    "pkg install",
    "alias",
    "xeditor",
    "windai",
    "sys(info)",
    "lang",
    "yes",
    "ver",
    "apt update",
    "apt",
    "mkfl",
    "cat",
    "pip install",
    "pyrun",
    "tree",
    "login",
    "/rm -rf [path]",
    "selfdestruct",
    "login --as [proot name]",
    "pkg uninstall [pkg name]",
    "repo",
    "cd ",
    "pwd",
    "math",
    "nano",
    "uptime",
    "sh",
    "bash",
    "update",
    "update --force",
    "dirsmake",
    "ls [-la] (dir)",
    "mv",
    "cowsay [message]",
    "env",
    "man",
    "source",
    "ls",
    "rename",
    "unalias",
    "alias -l",
    "unalias -a",
    "python",
    "find [ext]",
    "df -h",
    "stat",
    "figlet",
    "jvrun",
    "setprompt",
    "error",
    "error -l",
    "error -man",
    "prjctline",
    "about",
    "about -v",
    "cal",
    "pigsay",
    "passwordgen",
    "passrate",
    "help()",
    "fortune",
    "funfacts",
    "party",
    "nyancat",
    "hack",
    "rave",
    "sneksay",
    "which",
    "catsay",
    "lolcat",
    "hashgen",
    "base64gen",
    "base64decode",
    "uuidgen",
    "settings",
    "clock",
    "expand",
    "rev",
    "wc",
    "rot13",
    "8ball",
    "bulldoiser",
    "chmod",
    "chroot",
    "unchroot",
    "checkperm",
    "top",
    "logout",
    "htop",
    "top --simple",
    "pycheck",
    "du -h"
]
env_vars = {
    "USER": username,
    "ID": userid,
    "REPO": answerrepo,
    "DIR": cdirectory,
    "OS": platform.system(),
    "SYSTEM": os.name,
    "PS1": prompt,
    "CMDLIST": ", ".join(commands),
    "HOME": default_home,
    "PATH": f"/{default_home}/;/homefolder" if os.name != "nt" else "C:\\Users;C:\\",
    "SHELL": "/sdcard/X#init/home/local/xshell" if os.name != 'nt' else "C:\\Users\\xshell",
    "PS2": ">",
    "FILERC": "config.py"
}
xstatus = "NO"
windai = "soxca"
aliases = {}
verapt = False
need_update = random.choice([True, False, "Needed but not updating all package"])
filename = "main.py"
os.makedirs("/storage/emulated/0/X#init/homefolder", exist_ok=True)
os.makedirs("/storage/emulated/0/X#init/home/local", exist_ok=True)
try:
    os.chdir("/storage/emulated/0/X#init/home/local")
    content = '''
    content/xshell:XSH.RUN={simple,xsh,subprocess}
id%XSH.Shell.CONTENT * 4
                     xshell"ID001"
username%XSH.Shell.CONTENT * 5
                     xshell"local"
get={content,dispatcher}
get.Viewer{
    viewer: dispatcher
}.element{}
XSH.RUN{
 xsh.information.about("--help {args.strip()})
 xsh.command("main.py")
}
.script {
    xsh.enable(whenStart=true)
}
'''
    with open("xshell", "w") as xshell:
        xshell.write(content)
        os.chdir(default_home)
except BaseException:
    pass        

try:
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

except FileNotFoundError:
    pass
except BaseException as e:
    pass
    
prootname = "root"
canloginasroot = False
loadingspinner = ['\\', '-', '/', '|']
colors = {
    "-g": "\033[92m",  # Green
    "-r": "\033[91m",  # Red
    "-b": "\033[94m",  # Blue
    "-w": "\033[97m",  # White
    "-p": "\033[95m",  # Purple
}
reset = "\033[0m"
offline_mode = False
prootuser = "local"
start_time = time.time()
import math

termux_detected = "com.termux" in sys.executable or os.getenv("PREFIX") == "/data/data/com.termux/files/usr"
if termux_detected:
    print("WARNING: Some feature may not working properly in Termux. Like 'sh'.")
    print("Try for run in Python Terminal/Pydroid 3/Ubuntu/WSL.\n")

os.chdir(cdirectory)


has_checked_update = False
need_update = False
help_dict = {
    "math": "Usage: math <expression>\nExample: math 3+5*2-1\nPerforms math operations using +, -, *, /.",
    "mkdir": "Usage: mkdir [folder_name]\nCreates a single directory in the root path.",
    "dirsmake": "Usage: dirsmake [nested/folder/path]\nCreates nested folders recursively.",
    "cat": "Usage: cat [filename]\nDisplays the content of the specified file.",
    "cd": "Usage: cd [path]\nChanges current working directory. Accepts ~ and $HOME.",
    "pwd": "Shows the current directory you're in.",
    "xeditor": "Launches X# Code Editor for writing simple nugget() or echothis commands.",
    "pyrun": "Starts an interactive Python interpreter session.",
    "windai": "Talk to the AI assistant called WindAI. (mostly for fun)",
    "uptime": "Displays how long the terminal has been running.",
    "pkg install": "Usage: pkg install [package_name]\nInstalls a built-in or pip package.",
    "pkg uninstall": "Usage: pkg uninstall [package_name]\nRemoves a previously installed package.",
    "alias": "Usage: alias [name] [command]\nCreates a shortcut (alias) for a longer command.",
    "unalias": "Usage: unalias [name]\nRemoves an existing alias.",
    "repo": "Shows the current selected repository.",
    "reposhow": "Displays available repositories you can switch to.",
    "echo": "Prints text with environment variable support. Example: echo $USER",
    "help": "Shows all available built-in commands.",
    "help()": "Starts interactive help tutorial with fun facts and guidance.",
    "ls": "Lists files in the current directory. Add -la for more details.",
    "mv": "Usage: mv [source] [target]\nMoves or renames files.",
    "nano": "Usage: nano [filename]\nOpen file editor with save/remove/list options.",
    "fortune": "Displays a random funny or wise quote.",
    "cowsay": "Displays your message with an ASCII cow. Example: cowsay Hello!",
    "pigsay": "Same as cowsay, but with a pig.",
    "nyancat": "Launches NYANCAT animation in terminal 🌈🐱",
    "party": "🎉 Celebrates your coding with flashy effects.",
    "hashgen": "Generates hash (md5, sha1, sha256) from text input.",
    "passrate": "Rates the strength of a password.",
    "passwordgen": "Generates a random password with custom options.",
    "lolcat": "Displays text with rainbow colors.",
    "tree": "Draws directory tree of current or specified path.",
    "env": "Lists environment variables used by X# interpreter.",
    "find": "Usage: find [ext]\nSearches files with specific extension (e.g. .txt).",
    "df": "Disk usage info. Run as: df -h",
    "stat": "Shows RAM and memory stats. Requires psutil.",
    "figlet": "Usage: figlet [text]\nShows ASCII art banner (requires pyfiglet).",
    "setprompt": "Changes the prompt symbol or color. Use setprompt -d to reset.",
    "bash": "Launches interactive bash shell mode.",
    "sh": "Launches interactive sh shell mode.",
    "update": "Checks and updates installed packages if needed.",
    "update --force": "Force-update all packages, even if not recommended.",
    "about": "Displays basic info about X# CLI.",
    "about -v": "Verbose mode: show developer, Python version, prompt, etc.",
    "clock": "Real-time clock.",
    "base64gen": "Base64 Generator.",
    "base64decode": "Base64 decode tools.",
    "expand": "Like in unix.",
    "rev": "Reverse a text; auto detection for empty text.",
    "wc": "wc = Word Count. count a word, line and more in file.",
    "rot13": "Applies ROT13 encryption/decryption to args.",
    "chmod": "Usage: chmod [mode] [filename]\nExample: chmod 755 file.txt\nChange file permission using octal format like in UNIX.",
    "chroot": "Usage: chroot [dir]\nChange current root directory like in BASH.",
    "unchroot": "Change current root directory to default.",
    "checkperm": "Usage: checkperm [filename]. Check permission for a file.\nExample: checkperm main.py",
    "logout": "logout for this session.",
    "top": "Like in UNIX.",
    "top --simple": "Simple top. Just show for one time.",
    "htop": "Like in UNIX again. But this is improved top.",
    "pycheck": "Check syntax of a code.",
}
if os.path.isfile("config.py"):
    with open("config.py", "r") as xsharp:
        try:
            execute = xsharp.read()
            exec(execute, globals())
        except BaseException:
            print("Welcome to X# Interpreter!")
            print("Type 'help' for help.")
else: 
    print("Welcome to X# Interpreter!")
    print("Type 'help' for help.")

while True:
    try:
        

    
        if prompt.startswith("[chroot]"):
                prompt_path = "/"
        elif cdirectory == default_home:
                prompt_path = "~"
        elif default_home and cdirectory.startswith(default_home + "/"):
           prompt_path = cdirectory.replace(default_home, "~", 1)
        else:
           parts = cdirectory.strip("/").split("/")
           if len(parts) > 35:
               prompt_path = ".../" + "/".join(parts[-2:])
           else:
               prompt_path = cdirectory
                
        command = input(f"\033[93m{prompt_path} {prompt} \033[0m").strip()
        if command.strip() == ".safe":
            if history:
                last_command = history[-1]
                if last_command in commands:
                    print(f"(safe re-running: {last_command})")
                    command = last_command
                else:
                    print("Previous command failed. Nothing to repeat safely.")
                    continue
            else:
                print("No previous command to run safely.")
                continue
        if command.strip() == ".":
            if history:
                last_command = history[-1]
                print(f"(re-running: {last_command})")
                command = last_command
            else:
                print("No previous command to run.")
                continue
        
    except EOFError:
        print("\nlogout\n")
        print("[1] No input detected.")
        sys.exit()
    except KeyboardInterrupt:
        print("logout\n")
        print("[130] Program disabled due to KeyboardInterrupt.")
        sys.exit()
    except BaseException as e:
        print(e)

    history.append(command)
    try:
        if os.path.isfile("datahistory.txt"):
            with open("datahistory.txt", "a") as f:
                f.write(f"{command}\n")
        else:
            with open("datahistory.txt", "w") as f:
                f.write(f"{command}\n")
    except BaseException as e:
        print(e)
        
    split = command.strip().split(" ", 1)
    command = split[0]
    args = split[1] if len(split) > 1 else ""

    if command in aliases:
        alias_expansion = aliases[command]
        combined = alias_expansion + (" " + args if args else "")

        command_parts = combined.strip().split(" ", 1)
        command = command_parts[0]
        args = command_parts[1] if len(command_parts) > 1 else ""
        
    if not command:
        continue
        
    elif command == "exit":
        print("logout\n")
        print("[0] Exited with a normal code.")
        sys.exit(0)
        
    elif command == "--help":
        help_command = args.strip()
        if not help_command:
            print("Usage: --help [command]\nExample: --help math")
        else:
            if help_command in help_dict:
                print(help_dict[help_command])
            elif help_command == "--list":
                print("Current help value dictionary:")
                for key, value in help_dict.items():
                    print(f"{key}: {value}")
            else:
                print(f"{help_command}: not found (not in documentation)")
                
    elif command == "logout":
        print("logout")
        while True:
            subcommand = input("[username]~$  ")
            if subcommand == "%EXIT":
                break
            if subcommand == "%HELP":
                print("%help[%EXIT,%HELP")
        

    elif command == "joingr":
        url = "https://chat.whatsapp.com/FzudiFhaocT4vXHmxVks1N"
        if "com.termux" in os.environ.get("PREFIX", ""):
            os.system(f"termux-open-url '{url}'")
        else:
            webbrowser.open(url)
        

    elif command == "information":
        print("X# is a programming language that allows you to make an app or game (or another software). This language is built with Python, in 2006.")

    elif command == "mkdir":
        try:
            path = "C:\\" if os.name == 'nt' else "/storage/emulated/0"
            os.chdir(path)
            partmkdir = args.strip()
            os.mkdir(partmkdir)
            print("Directory succesfully created in:", os.path.join(path, partmkdir))
            time.sleep(2)
        except OSError as e:
            print(f"OSError: {e}")
        except Exception as e:
            print(f"{type(e).__name__}: {e}")
        finally:
            os.chdir(cdirectory)

    elif command == "dir":
        os.chdir('C:\\' if os.name == 'nt' else '/storage/emulated/0')
        print(os.listdir())
        os.chdir(cdirectory)
        
    elif command == "help()":
        print("Welcome to interactive help!")
        print("If you want to tutorial, type 'tutorial'.")
        print("For quit, type 'quit'.")
        while True:
            subcommand = input("help $   ")
            if subcommand == "quit":
                print("Now you quiting Help Utilities.")
                break
            elif subcommand == "tutorial":
                print("Welcome to tutorial!")
                print("This tutorial will get you a learn of a feature of help().")
                tutorialmap = [
                    "X# is created by Athaya.",
                    "Athaya is indonesia people.",
                    "This X# is created in Jakarta.",
                    "Did you know, X# have so much commands!",
                    "Did you know, X# built in Python."
                ]
                print(random.choice(tutorialmap))
                print("loading...")
                time.sleep(7)
                print("Welcome to X#!")
                print("help() is a interactive help for user.\nNot like help, this is a interactive help.")

    elif command == "help":
        print("Built-in commands:\n----------------\n", ", ".join(commands), "\n------------------", "\nTotal commands:", len(commands))

    elif command == "w/":
        if not args.strip():
            print("Usage: w/ <search query>")
        else:
            query = args.strip().replace(" ", "+")
            url = f"https://www.google.com/search?q={query}"
            print(f"Searching for: {args.strip()}")
            try:
                if "com.termux" in os.environ.get("PREFIX", ""):
                    os.system(f"termux-open-url '{url}'")
                else:
                    webbrowser.open(url)
            except Exception as e:
                print(f"Failed to open browser: {e}")

    elif command == "s/":
        search_term = args.strip().lower()
        matched = [pkg for pkg in available_package if search_term in pkg.lower()]
        if matched:
            print("Packages found:")
            for m in matched:
                print(f" - {m}")
        else:
            print("\033[1;41mModuleNotFoundError: No module found\033[0m")

    elif command == "c-repo":
        repo = input("Type repo name or type 'reposhow' to show repo...  ")
        if repo == "reposhow":
            print("Available repos:", ", ".join(repos))
        elif repo in repos:
            answerrepo = repo
            print("Current repo:", answerrepo)
        else:
            suggestions = [r for r in repos if repo in r]
            if suggestions:
                print("Unknown repo. Did you mean:")
                for s in suggestions:
                    print(f" - {s}")
            else:
                print("Unknown repo in suggestions.")

    elif command == "echo":
        echo_text = args.strip()
        
        if not echo_text:
            print("Usage: echo [text]")
            continue

        # Get all $VARNAME in text
        for key, value in env_vars.items():
            echo_text = echo_text.replace(f"${key}", value)

        print(echo_text)

    elif command == "reposhow":
        print(", ".join(repos))

    elif command == "id":
        print(userid)

    elif command == "history":
        for i, cmd in enumerate(history, 1):
            print(f"{i}. {cmd}")

    elif command == "insta":
        urlin = input("Type URL...  ")
        savefile = input("Save as...  ")
        try:
            r = requests.get(urlin)
            with open(savefile, "wb") as f:
                f.write(r.content)
            print("File installed!")
        except Exception as e:
            print("error when installing:", e)

    elif command == "clear":
        os.system("cls" if os.name == "nt" else "clear")
        if os.path.isfile("config.py"):
            with open("config.py", "r") as xsharp:
                try:
                    execute = xsharp.read()
                    exec(execute, globals())
                except BaseException:
                    print("Welcome to X# Interpreter!")
                    print("Type 'help' for help.")
        else: 
               print("Welcome to X# Interpreter!")
               print("Type 'help' for help.")

    elif command == "setname":
        new_name = args.strip()
        if new_name:
            try:
                if os.path.isfile("datalog.txt"):
                    with open("datalog.txt", "a") as f:
                        f.write(f"[LOG DATA] {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: {new_name}\n")
                    username = new_name
                    env_vars["USER"] = new_name
                    print("Username changed!")
                else:
                    with open("datalog.txt", "w") as f:
                        f.write(f"[LOG DATA] {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: {new_name}\n")
                        username = new_name
                        env_vars["USER"] = new_name
                        print("Username changed!")
            except Exception as e:
                print(e)
        else:
            print("Type a username.")

    elif command == "pkg" and args.strip().startswith("install "):
        if offline_mode:
            print("Can't install package. Check your internet connection.")
        else:
            pkg_name = args.strip()[len("install "):].strip()
            if not pkg_name:
                print("Please provide a pkg name.")
                continue
            if not re.match(r'^[a-zA-Z0-9\-_]+$', pkg_name):
                print("Invalid package name. Avoid special character for security.")
                continue

            # --- internal pseudo packages ---
            if pkg_name == "jvrun":
                if pkginstaller == "yes":
                    print("jvrun is installed.")
                else:
                    print("Installing jvrun...")
                    time.sleep(random.randint(2, 5))
                    pkginstaller = "yes"
                    print("Succesfully installed jvrun!")
                    available_package.append("jvrun")

            elif pkg_name == "jvscrrun":
                if pkginstallera == "true":
                    print("jvscrrun is installed.")
                else:
                    print("Installing jvscrrun...")
                    time.sleep(random.randint(2, 5))
                    pkginstallera = "true"
                    print("Succesfully installed jvscrrun!")
                    available_package.append("jvscrrun")

            elif pkg_name == "xeditor":
                if xstatus == "True":
                    print("xeditor is installed.")
                else:
                    print("Installing xeditor...")
                    time.sleep(random.randint(2, 5))
                    xstatus = "True"
                    print("Succesfully installed xeditor!")
                    available_package.append("xeditor")

            elif pkg_name == "windai":
                if windai == "SOYES":
                    print("windai is installed.")
                else:
                    print("Installing windai...")
                    time.sleep(random.randint(2, 5))
                    windai = "SOYES"
                    print("Succesfully installed windai!")
                    available_package.append("windai")

            elif pkg_name == "proot-xlogin":
                if canloginasroot:
                    print("proot-xlogin is installed.")
                else:
                    spinner_msg = "\tInstalling build dependencies for proot-xlogin..."
                    print("Installing proot-xlogin...")
                    time.sleep(random.randint(2, 5))
                    print("Installing build requirements for proot-data...")
                    for _ in range(10):
                        for frame in loadingspinner:
                            sys.stdout.write(f"\r{spinner_msg} {frame}")
                            sys.stdout.flush()
                            time.sleep(0.25)
                    sys.stdout.write("\r" + " " * (len(spinner_msg) + 2) + "\r")
                    sys.stdout.flush()

                    print("Installing build for proot-xdistro...")
                    time.sleep(random.randint(2, 5))
                    canloginasroot = True
                    print("Succesfully installing proot-xlogin!")
                    available_package.append("proot-xlogin")

            # --- pip packages ---
            else:
                print(f"Installing {pkg_name} via pip...")
                try:
                    subprocess.check_call([sys.executable, "-m", "pip", "install", pkg_name])
                    print(f"{pkg_name} is installed succesfully!")
                except subprocess.CalledProcessError as e:
                    print(f"Failed to install package {pkg_name}: {e}")
                    
    elif command == "alias" and args.strip() == "-l":
        if aliases:
            print("Active aliases:")
            for name, value in aliases.items():
                print(f" - {name}: {value}")
        else:
            print("No aliases found.")

    elif command == "alias":
        parts = args.strip().split("=", 1)
        if len(parts) < 2:
            print("Usage: alias [name] [real command]")
        elif parts[0] in commands:
            print(f"[500] Cannot add alias '{parts[0]}': it's in command lists")
        else:
            alias_name = parts[0]
            alias_value = parts[1]
            aliases[alias_name] = alias_value
            print(f"Alias '{alias_name}' set to '{alias_value}'")

    elif command == "whoami":
        print(f"{username}")

    elif command == "xeditor":
        if xstatus == "NO":
            print("Cannot access X# Editor")
        else:
            print("Welcome to X# Editor!")
            print("Starts with new code or set id?")
            sub = input(">>>  ")
            if sub == "Starts with new code":
                code_lines = []
                output = None
                while True:
                    code = input("~  ")
                    if code == "exit":
                        break
                    elif code.startswith("nugget('") and code.endswith("')"):
                        printedtext = code[8:-2]
                        code_lines.append(f"nugget('{printedtext}'")
                        output.append(printedtext)
                    elif code.startswith("echothis "):
                        echothistext = code[len("echothis "):].strip()
                        code_lines.append(f"echothis {echothistext}")
                        output.append(echothistext)
                        
                    elif code == "run":
                        print(f"{output}")
                        
                    elif code.startswith("save "):
                        filename = code[len("save "):].strip()
                        if not filename:
                            print("File Empty!")
                        else:
                            import zipfile
                            import json
                            
                            xrc_path = "/storage/emulated/0/X#init/.xrc"
                            if not os.path.isfile(xrc_path):
                                print("Cannot make file: .xrc not found.")
                                content = f'''[APP]
name = {filename}
package = {filename.lower()}
package_name = com.{filename.lower()}
source_dir = .
app_xicy.required = false

[REQUIREMENTS]
runtime = 
requirements = xsharp

[ASSETS]
include = 

[BUILD]
# WPA SDK requirements
wpa.sdk_development.versions = 31 


[PERMISSIONS]
permissions = A:ENTRY(windpow,INTERNET)

[DEVICE]
# Supported device
supported = windpow,posix,dmu,nt
convert_to = .wpa

[RESOURCE]
# Change this to your resource
resource.get_module = xpm 

[UI]
# Splash screen, default is ok for Xicy App
ui.splash_screen = 

# Fullscreen config, 1 for fullscreen
fullscreen = 0

[PYTHON]
# Are this from python?
python.are_this.from_python = False

[PROFILE]
# Profile of author
author_name = yourname
Copyright (c) [Years] yourname

[CONVERT]
# WPA SDK converted (not required)
wpa.sdk_convert = *
'''
                                print("Make a new .xrc file.")
                                with open(".xrc", "w") as f:
                                    f.write(content
                                    )
                                continue
                            else:
                                try:
                                    with open(xrc_path, "r") as f:
                                        xrc_content = f.read()
                                except Exception as e:
                                    print("Error when make file:", e)
                                    continue
                                projects_metadata = {
                                    "project_name": filename,
                                    "author": username,
                                    "languange": "xython",
                                    "version": "0.1",
                                    "contains": ["__main__", ".xrc", "project.json"]
                                }
                                
                                path = os.path.join(cdirectory, f"{filename}.xpf")
                                
                                try:
                                    with zipfile.ZipFile(path, "w") as x:
                                        x.writestr("__main__", "\n".join(code_lines))
                                        x.writestr(".xrc", xrc_content)
                                        x.writestr("project.json", json.dumps(projects_metadata, indent=4))
                                    print(f"The file is saved to {cdirectory}!")
                                except Exception as e:
                                    print(e)
                                
                    else:
                        code_lines.append(code)
                    
            elif sub == "Set id":
                stepcode = input("---  ")
                if re.match(r"^ID\d{6}$", stepcode):
                	print("Checking ID format...")
                	time.sleep(2)
                	print("The ID is valid!")
                	time.sleep(1)
                	print("nugget('Hello!')")
                	print("\n\n\nOutput: Hello!")
                	
                	
                	while True:
                	    code = input("~  ")
                	    if code == "exit":
                	    	break
                else:
                    print("Please start with 'ID' and six (6) digit to check your ID.")

    elif command == "windai":
        if windai == "soxca":
            print("Can't access WindAI 1.2.0.1.")
        else:
            print("Welcome to WindAI!")
            while True:
                ai = input(f"{username}: ")
                if ai.lower() == "hello":
                    print("WindAI: Hello! What can I help you with?")
                elif ai == "exit":
                    break
                elif ai.lower() == "who is the real dev":
                    print("WindAI: The real dev is Athaya.")
                else:
                    print("WindAI: Sorry, I can't help with that yet.")

    elif command == "sys(info)":
        info = platform.uname()
        print("OS:", info.system)
        print("VER:", info.version)
        print("NODE NAME:", info.node)
        print("MACHINE NAME:", info.machine)
        print("RELEASE VERSION:", info.release)

    elif command == "lang":
        print("Current language: English")

    elif command == "yes":
        message = args.strip()
        if not message:
                while True:
                    try:
                        print("y")
                    except KeyboardInterrupt:
                        break
        else:
            while True:
                try:
                    print(message)
                except KeyboardInterrupt:
                    break

    elif command == "ver":
        print("Version", "3.0.0" if need_update else "2.5.1")

    elif command == "apt" and args.strip() == "update":
        if verapt:
            print("Apt is updated to new version.")
        else:
            print("Building dependency tree...")
            time.sleep(2)
            print("Updating packages...")
            time.sleep(1)
            print("Packages that can updated: pip, lv, pyrun")
            tryinput = input("Update? (y/n)  ")
            if tryinput.lower() == "y":
                print("Updating pip...")
                time.sleep(random.randint(1, 5))
                print("Updating lv, pyrun...")
                time.sleep(random.randint(1, 5))
                print("Done.")
                verapt = True
            else:
                print("Building new update...")
                time.sleep(2)
                print("Cannot updating apt: lv is deprecated and not supported again.")
                print("\033[91mERROR: cannot find lv-2.0.0. APT needs lv-2.0.0 to upgrade.\033[0m")
                time.sleep(0.1)
                print("\033[91mERROR: cannot find lv-builder\033[0m")
                verapt = False
                continue

    elif command == "apt":
        print("APT status:", "2.0.1" if verapt else "2.0.0")

    elif command == "mkfl":
        try:
            path = "C:\\" if os.name == 'nt' else "/storage/emulated/0"
            os.chdir(path)
            filename = args.strip()
            if not filename:
                print("\033[1;41mFileEmptyError:\033[0m\033[91mThe filename is empty\033[0m")
            else:
                ext = input("Add file extension (e.g. .txt, .py)? Press enter to skip: ")
                
                if ext and not filename.endswith(ext):
                    filename += ext
                    
                content = input("File content (press Enter to leave blank): ")
                with open(filename, "w") as f:
                    f.write(content)
                
                print(f"File created: {os.path.join(path, filename)}")
        
        except IOError as e:
            print(e)
        except Exception as e:
            print(e)
        finally:
            os.chdir(cdirectory)

    elif command == "cat":
        catfile = args.strip()
        try:
            if os.path.isfile(catfile):
                with open(catfile, "r", encoding="utf-8") as rfile:
                    print(rfile.read())
            else:
                print("Not a file.")
                
        except Exception as e:
           print(e)

    elif command == "pip" and args.strip().startswith("install "):
        piptarget = args.strip()[len("install "):].strip()
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", piptarget])
            print(f"{piptarget} succesfully installed.")
        except subprocess.CalledProcessError as e:
            print(f"Error during installing: {e}")
        except Exception as e:
            print(e)

    elif command == "pyrun":
        try:
            print("Running python...")
            time.sleep(2)
            print("Executing command...")
            time.sleep(1)
            os.system("cls" if os.name == 'nt' else "clear")
            subprocess.call([sys.executable])
            os.system("cls" if os.name == 'nt' else "clear")
            print("Welcome to X# Interpreter.")
            print("Type help for 'help'.")
            print("Returned from python interpreter")
        except KeyboardInterrupt:
            os.system("cls" if os.name == 'nt' else "clear")
            print("Keyboard interrupt. Returning to X# Interpreter..")
            continue
        except BaseException as e:
            print(f"Error when running python: {e}")
            continue

    elif command == "tree":
        target_path = args.strip()
        if not target_path:
            target_path = os.getcwd()
        elif not os.path.exists(target_path):
            print("Directory does not exist.")
            continue

        print("Tree of:", target_path)
        dirs = [(target_path, "", True)]

        while dirs:
            current_path, prefix, _ = dirs.pop(0)
            try:
                items = sorted(os.listdir(current_path))
                for i, item in enumerate(items):
                    full_path = os.path.join(current_path, item)
                    is_last = (i == len(items) - 1)
                    connector = "└── " if is_last else "├── "
                    print(prefix + connector + item)
                    if os.path.isdir(full_path):
                        new_prefix = prefix + ("    " if is_last else "│   ")
                        dirs.insert(0, (full_path, new_prefix, is_last))
            except PermissionError:
                print(prefix + "└── [Permission Denied]")
            except Exception as e:
                print(prefix + "└── ", e)

    elif command == "login":
        if not canloginasroot:
            print("You can't login to root because you don't have: proot-xlogin")
        else:
            info = platform.uname()
            while True:
                root = input(f"{prootname}@{info.machine}:~#   ")
                if root == "mkuser":
                    temp_prootname = input("Enter new username (this is required if you not need root for user):  ")
                    if not prootname:
                        temp_prootname = "localroot"
                    attempt = 0
                    max_attempts = 4
                    while attempt < max_attempts:
                        prootpassword = input(f"Enter password for {temp_prootname}:  ").strip()
                        if prootpassword:
                            print("Please wait...")
                            time.sleep(random.randint(2, 5))
                            print(f"{temp_prootname} is succesfully created!")
                            prootname = temp_prootname
                            print(f"Switching to user '{prootname}'...")
                            root = input(f"{prootname}@localhost:~$  ")
                        else:
                            attempt += 1
                            if attempt < max_attempts:
                                print(f"[!] Password cannot be empty. Attempts left: {max_attempts - attempt}")
                            else:
                                print("Maximum attempts reached. User creation canceled.")
                                break
                elif root == "exit":
                    print("logout")
                    break
                elif root.startswith("sudo "):
                    sudo = root[len("sudo "):].strip()
                    if sudo == "apt update":
                        print("Updating packages...")
                        time.sleep(1)
                        print("Done!")
                elif root == "whoami":
                    print(f"Name: {prootname}")
                else:
                    print("Unknown command.")
                    
    elif command == "/rm":
        parts = args.strip().split(" ")
        if len(parts) < 2:
            print("Usage: /rm [-rf] <path>")
            continue

        force = False
        path = parts[-1]
        if "-rf" in parts:
            force = True

        dangerous_paths = ["/", "/storage", "/storage/emulated", "/storage/emulated/0"]
        if os.path.abspath(path) in [os.path.abspath(p) for p in dangerous_paths]:
            print("Access denied. Are you crazy?")
            continue

        if not os.path.exists(path):
            print("[404] No such file or directory.")
            continue

        try:
            if os.path.isfile(path):
                os.remove(path)
                print(f"File '{path}' deleted.")
            elif os.path.isdir(path):
                if force:
                    import shutil
                    shutil.rmtree(path)
                    print(f"Directory '{path}' and all contents removed.")
                else:
                    os.rmdir(path)
                    print(f"Directory '{path}' removed.")
        except PermissionError:
            print("[403] Permission denied.")
        except Exception as e:
            print("Error:", e)
            
    elif command == "selfdestruct":
        print("[WARNING] Initiating self-destruction sequence...")
        for i in range(1, 6, +1):
            print(f"Self-destruct in {i}...")
            time.sleep(1)
        print("BOOM. X# Interpreter terminated.")
        break
        
    elif command == "login" and args.startswith("--as "):
        target_user = args[6:].strip()
        if target_user == prootuser:
            while True:
                proot = input(f"{prootuser}@localhost:~$ ")
                if proot == "exit":
                    print("logout")
                    break
                elif proot == "whoami":
                    print(f"User: {prootuser}")
                elif proot.startswith("sudo "):
                    sudo_cmd = proot[5:].strip()
                    if sudo_cmd == "apt update":
                        print("Running sudo apt update...")
                        time.sleep(1)
                        print("Update finished (simulated).")
                    else:
                        print(f"[sudo] Unknown command: {sudo_cmd}")
                else:
                    print("[Error] Unknown command.")
        else:
            print(f"Access denied for user '{target_user}'")
                
    elif command == "pkg" and args.startswith("uninstall "):
        pkg_name_that_to_uninstall = args[len("uninstall "):].strip()
        
        if pkg_name_that_to_uninstall == "lv":
            spinner_msg = "Deleting lv-setuptools..."
            print("Uninstalling lv...")
            for _ in range(5):
                for frame in loadingspinner:
                    sys.stdout.write(f"\r{spinner_msg} {frame}")
                    sys.stdout.flush()
                    time.sleep(0.25)
                    
                    sys.stdout.write("\r" + " " * (len(spinner_msg) + 2) + "\r")
                    sys.stdout.flush()
            print("Succesfully uninstalling lv!")
            time.sleep(0.2)
            print(f"\033[91mNotSuchAModuleError: {', '.join(available_package)} not such a module\033[0m")
            print(f"lv not detected.")
            break
        
        try:
            installed = {dist.metadata['Name'].lower() for dist in distributions()}
            if pkg_name_that_to_uninstall.lower() in installed:
                subprocess.run(f"pip uninstall {pkg_name_that_to_uninstall} -y", shell=True)
                print(f"{pkg_name_that_to_uninstall} has deleted succesfully!")
            else:
                print("The package name is not available in index.")
        except BaseException as e:
            print(f"Error when deleting {pkg_name_that_to_uninstall}: {e}")
            
    elif command == "repo":
        print(answerrepo)
   
    elif command.startswith("cd"):
        try:

            parts = command.strip().split(maxsplit=1)
            new_path = args.strip()

            dangerous_paths = ["/", "/storage", "/storage/emulated"]
            home_path = "/storage/emulated/0/X#init"

            if not new_path:
                new_path = home_path

            if new_path.startswith("$HOME"):
                new_path = new_path.replace("$HOME", home_path)
            elif new_path.startswith("~"):
                new_path = new_path.replace("~", home_path)

            if not os.path.isabs(new_path):
                target = os.path.abspath(os.path.join(cdirectory, new_path))
            else:
                target = os.path.abspath(new_path)


            if os.path.abspath(target) in [os.path.abspath(p) for p in dangerous_paths]:
                print("Access denied.")
                continue

            if not os.path.exists(target):
                print(f"Path not found: {target}")
                continue

            os.chdir(target)
            cdirectory = target
            print(f"Succesfully changing directory!")

        except Exception as e:
            print(f"{type(e).__name__}: {e}")
    
            
    elif command == "pwd":
        print(os.getcwd())
     
    elif command == "math":
        expr = args.strip().replace(" ", "")
        expr = expr.replace("x", "*").replace("×", "*")

        numbers = []
        operators = []
        i = 0
        num = ""
        last_char_was_op = True  # For read negative number

        try:
            while i < len(expr):
                char = expr[i]

                if char.isdigit() or char == "." or (char == "-" and last_char_was_op):
                    num += char
                    last_char_was_op = False
                elif char in "+-*/":
                    if num == "":
                        raise ValueError("Invalid format.")
                    numbers.append(float(num))
                    num = ""
                    while (operators and
                        ((operators[-1] in "*/" and char in "+-") or
                         (operators[-1] in "*/" and char in "*/"))):
                        b = numbers.pop()
                        a = numbers.pop()
                        op = operators.pop()
                        if op == "+":
                            numbers.append(a + b)
                        elif op == "-":
                            numbers.append(a - b)
                        elif op == "*":
                            numbers.append(a * b)
                        elif op == "/":
                            if b == 0:
                                raise ZeroDivisionError
                            numbers.append(a / b)
                    operators.append(char)
                    last_char_was_op = True
                else:
                    raise ValueError("Invalid character.")
                i += 1

            if num != "":
                numbers.append(float(num))

            while operators:
                b = numbers.pop()
                a = numbers.pop()
                op = operators.pop()
                if op == "+":
                    numbers.append(a + b)
                elif op == "-":
                    numbers.append(a - b)
                elif op == "*":
                    numbers.append(a * b)
                elif op == "/":
                    if b == 0:
                        raise ZeroDivisionError
                    numbers.append(a / b)

            result = numbers[0]
            print(f"Result: {result}")
        
        # --- except ---
        
        except ZeroDivisionError:
            print("[417] Error: Division by zero is not allowed.")
        except Exception as e:
            print("Invalid input. Use proper math expression like '3+4*2-1'.")
            
    elif command == "nano":
        filename = args.strip()
        filepath = os.path.join(cdirectory, filename)
        code_lines = []

        if os.path.exists(filepath):
            try:
                with open(filepath, "r") as f:
                    code_lines = f.read().splitlines()
                print(f"Opened existing file: {filename}")
            except Exception as e:
                print(f"Error reading file: {e}")
                continue
        else:
            print(f"Creating new file: {filename}")

        print("\n--- X# Nano Editor ---")
        print("Type new lines. Special commands:")
        print("  :wq       → save & quit")
        print("  :q        → quit without saving")
        print("  :rm [n]   → remove line number n")
        print("  :list     → show current content\n")

        while True:
            line = input("~nano> ").strip()

            if line == ":wq":
                try:
                    with open(filepath, "w") as f:
                        for cl in code_lines:
                            f.write(cl + "\n")
                    print(f"File '{filename}' saved successfully.")
                except Exception as e:
                    print(f"Failed to save file: {e}")
                break

            elif line == ":q":
                print("Exited without saving.")
                break

            elif line.startswith(":rm "):
                try:
                    index = int(line.split()[1]) - 1
                    if 0 <= index < len(code_lines):
                        deleted = code_lines.pop(index)
                        print(f"Line {index + 1} ('{deleted}') removed.")
                    else:
                        print("Invalid line number.")
                except Exception:
                    print("Wrong format. Use :rm [line number]")

            elif line == ":list":
                print("\n--- Current Content ---")
                for i, l in enumerate(code_lines, 1):
                    print(f"{i:>2}. {l}")
                print("------------------------\n")

            else:
                code_lines.append(line)
                
    elif command == "uptime":
        uptime_seconds = int(time.time() - start_time)
        minutes, seconds = divmod(uptime_seconds, 60)
        hours, minutes = divmod(minutes, 60)

        uptime_str = []

        if hours > 0:
            if hours == 1:
                uptime_str.append("1 hour")
            else:
                uptime_str.append(f"{hours} hours")

        if minutes > 0:
            if minutes == 1:
                uptime_str.append("1 minute")
            else:
                uptime_str.append(f"{minutes} minutes")

        if seconds == 1:
            uptime_str.append("1 second")
        else:
            uptime_str.append(f"{seconds} seconds")

        print("X# Interpreter running for " + ", ".join(uptime_str) + ".")
        
    elif command == "sh":
        print("Entering sh shell mode. Type 'exit' to return.")
        while True:
            try:
                shell_cmd = input("$ ").strip()
                if shell_cmd.lower() == "exit":
                    break
                if shell_cmd == "":
                    continue
                subprocess.run(["sh", "-i", "-c", shell_cmd], bufsize=0)
            except Exception as e:
                print("sh error:", e)

    elif command == "bash":
        print("Entering bash shell mode. Type 'exit' to return.")
        while True:
            try:
                shell_cmd = input("~$ ").strip()
                if shell_cmd.lower() == "exit":
                    break
                if shell_cmd == "":
                    continue
                subprocess.run(["bash", "-i", "-c", shell_cmd], bufsize=0)
            except Exception as e:
                print("bash error:", e)
                
    elif command == "update" and args.strip() == "--force":
        if not has_checked_update:
            tryinput = input("This action not recommended because this will force upgrading all package (and all package that not want to updating). Continue? (y/N)  ")
            if tryinput.upper() == "N":
                print("Canceled.")
            elif tryinput == "y":
                print("Updating lv...")
                time.sleep(2)
                print("lv cannot updated.\nNo update required.")
                need_update = False
                has_checked_update = True
        else:
            print("No force update needed.")
                
    elif command == "update":
        if not has_checked_update:
            print("Checking for updates...")
            time.sleep(1)
            has_checked_update = True

            if need_update:
                print("Update available: X# Interpreter v3.0.0")
                spinner = ['\\', '-', '|', '/']
                for module in available_package:
                    print(f"Updating {module}...")
                    for _ in range(10):
                        for frame in spinner:
                            sys.stdout.write(f"\rUpdating {module}... {frame}")
                            sys.stdout.flush()
                            time.sleep(0.1)
                    sys.stdout.write(f"\r{module} updated successfully.     \n")
                    time.sleep(0.5)
                print("All packages in available_package have been updated.")
                print("Status: Interpreter successfully updated to v3.0.0")
                
            elif need_update == "Needed but not updating all package":
                print("Updating package: pip...")
                time.sleep(2)
                print("Done!")
            else:
                print("You're already using the latest version.")
                print("Status: No update needed.")

        else:
            if need_update:
                print("You're already on v3.0.0. No need to update again.")
            else:
                print("No updates available. Stop checking.")
            
    elif command == "dirsmake":
        try:
            path = "C:\\" if os.name == 'nt' else "/storage/emulated/0"
            os.chdir(path)
            folderpath = args.strip()
            if not folderpath:
                print("\033[91mFolder path can't be empty!\033[0m")
            else:
                os.makedirs(folderpath, exist_ok=True)
                print("Nested directories created at:", os.path.join(path, folderpath))
        except IOError as e:
            print(f"IOError: {e}")
        except Exception as e:
            print(f"{type(e).__name__}: {e}")
        finally:
            os.chdir(cdirectory)       
            
    elif command == "man":
        man_cmd = args.strip()
        man_pages = {
            "dirsmake": """\
NAME
    dirsmake - create nested directories recursively

SYNOPSIS
    dirsmake [folder path]

DESCRIPTION
    Creates all folders along the specified path, including nested ones.
    It uses os.makedirs() with exist_ok=True, so it won't error if folders already exist.

EXAMPLES
    dirsmake folder1/folder2/folder3""",

            "mkdir": """\
NAME
    mkdir - create a directory

SYNOPSIS
    mkdir [folder name]

DESCRIPTION
    Creates a single folder in root storage.
    This command uses os.mkdir() and does not create nested folders.""",

            "help": """\
NAME
    help - show available commands

SYNOPSIS
    help

DESCRIPTION
    Displays all built-in commands in X# Interpreter.""",
             
            "cd": """\
NAME
     cd - changing current directory
     
SYNOPSIS
     cd [directory name]
     
DESCRIPTION
     Changing current working directory (cwd).
     It have a protection for /, /storage, and more.
     
EXAMPLES
     cd /sdcard"""  
        }

        if not man_cmd:
            print("Usage: man [command name]. Example: man help")
        elif man_cmd == "--list":
            print("Available manual pages:")
            for cmd in man_pages:
                print(f" - {cmd}")
        elif man_cmd in man_pages:
            print(man_pages[man_cmd])
        else:
            print(f"\033[91mNo manual entry for '{man_cmd}'\033[0m")
            
    elif command == "ls":
        import stat

        show_detail = "-la" in args or "-lah" in args
        show_perm = "-la" in args or "-lah" in args
        recursive = "-R" in args
        target_dir = cdirectory

        if "-lah" in args:
            args = args.replace("-lah", "").strip()
        elif "-la" in args:
            args = args.replace("-la", "").strip()
        if "-R" in args:
            args = args.replace("-R", "").strip()

        if args:
            if args.startswith("~"):
                args = args.replace("~", default_home)
            target_dir = os.path.abspath(os.path.join(cdirectory, args))

        def list_dir(path, prefix=""):
            ''' I dont know why i make a function... :| '''
            try:
                files = os.listdir(path)
                if prefix:
                    print(f"{prefix}:")
                if not show_detail:
                    for f in files:
                        full_path = os.path.join(path, f)
                        mode = os.stat(full_path).st_mode
                        if stat.S_ISDIR(mode):
                            color = "\033[94m"
                        elif os.access(full_path, os.X_OK):
                            color = "\033[92m"
                        elif f.startswith("."):
                            color = "\033[90m"
                        else:
                            color = "\033[97m"
                        print(f"{color}{f}\033[0m")
                else:
                    print(f"{'Permissions':<11} {'Size':>10}  {'Modified Time':<20} {'Name'}")
                    print("-" * 70)
                    for f in files:
                        full_path = os.path.join(path, f)
                        try:
                            mode = os.stat(full_path).st_mode
                            perms = stat.filemode(mode) if show_perm else "-"
                            size = os.path.getsize(full_path)
                            mtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(full_path)))
                            if stat.S_ISDIR(mode):
                                color = "\033[94m"
                            elif os.access(full_path, os.X_OK):
                                color = "\033[92m"
                            elif f.startswith("."):
                                color = "\033[90m"
                            else:
                                color = "\033[97m"
                            print(f"{perms:<11} {size:>10}  {mtime:<20} {color}{f}\033[0m")
                        except Exception as e:
                            print(f"Error reading '{f}': {e}")
                if recursive:
                    for f in files:
                        full_path = os.path.join(path, f)
                        if os.path.isdir(full_path):
                            list_dir(full_path, prefix=full_path)
            except Exception as e:
                print("Error:", e)

        list_dir(target_dir, prefix=target_dir)
            
    elif command == "mv":
        args = args.strip().split()

        if len(args) != 2:
            print("Usage: mv [source] [destination]")
        else:
            src = os.path.join(cdirectory, args[0])
            dest = os.path.join(cdirectory, args[1])

            if not os.path.exists(src):
                print(f"mv: source '{args[0]}' does not exist.")
            else:
                try:
                    os.rename(src, dest)
                    print(f"Moved/Renamed '{args[0]}' to '{args[1]}'")
                except BaseException as e:
                    print(f"mv error: {e}")
                    
    elif command == "cowsay":
        text = args.strip()
        if not text:
            print("Usage: cowsay <your message>")
        elif text.startswith('"'):
            while True:
                ps2 = input("> ")
                if ps2.startswith('cowsay "') and ps2.endswith('"'):
                    break
                
        elif text.startswith('"') and text.endswith('"'):
            replaced = text.replace('"', '').strip()
            bubble = f'   \"{replaced}"\n'
            cow = r"""
         \   ^__^
          \  (oo)\_______
             (__)\       )\/\
                 ||----w |
                 ||     ||
            """
            print(bubble + cow)
        else:
            bubble = f"  \"{text}\"\n"
            cow = r"""
         \   ^__^
          \  (oo)\_______
             (__)\       )\/\
                 ||----w |
                 ||     ||
            """
            print(bubble + cow)
            
    elif command == "env":
        for key, value in env_vars.items():
            print(f"{key}={value}")
            
    elif command == "source":
        filepath = args.strip()
        if not filepath:
            print("Usage: source <filename>")
        elif not os.path.isfile(filepath):
            print(f"File '{filepath}' not found.")
        else:
            _, ext = os.path.splitext(filepath)
            print(f"Sourcing file '{filepath}'...")

            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    lines = f.read().splitlines()

                for line in lines:
                    line = line.strip()
                    if not line:
                        continue
                    print(f"{line}")
                    history.append(line)

                if ext == ".py":
                    try:
                        exec(line, globals())
                    except BaseException as e:
                        print(f"python error: {e}")

                else:
                    if line in aliases:
                        line = aliases[line]
                    if line.startswith("echo"):
                        for key, value in env_vars.items():
                            line = line.replace(f"${key}", value)
                        print(line[5:].strip())
                    elif line.startswith("cd "):
                        try:
                            new_path = line[3:].strip()
                            if not os.path.isabs(new_path):
                                new_path = os.path.join(cdirectory, new_path)
                            os.chdir(new_path)
                            cdirectory = new_path
                        except Exception as e:
                            print(f"cd error: {e}")
                    elif line.startswith("mkdir "):
                        try:
                            os.mkdir(line[6:].strip())
                        except Exception as e:
                            print(f"mkdir error: {e}")
                    else:
                        print(f"line: {line}")

            except Exception as e:
               print(f"source error: {e}")
               
               
               
    elif command == "rename":
         try:
             split_args = args.strip().split()
             if len(split_args) != 2:
                 print("Usage: rename [old_name] [new_name]")
             else:
                 old_path = os.path.join(cdirectory, split_args[0])
                 new_path = os.path.join(cdirectory, split_args[1])
                 os.rename(old_path, new_path)
                 print(f"Renamed '{split_args[0]}' to '{split_args[1]}'")
         except Exception as e:
             print(f"Error: {e}")
             
    elif command == "unalias" and args.strip() == "-a":
        if aliases:
            aliases.clear()
            print("All alias cleared.")
        else:
            print("No alias detected.")
             
    elif command == "unalias":
        alias_name = args.strip()
        if not alias_name:
            print("Usage: unalias [name]")
        elif alias_name not in aliases:
            print(f"Alias '{alias_name}' does not exist.")
        else:
            del aliases[alias_name]
            print(f"Alias '{alias_name}' has been removed.")
            
        
    elif command == "python":
        filename = args.strip()

        if not filename:
            print("Usage: python [file.py]")
        else:
            filepath = os.path.join(cdirectory, filename)
            if not os.path.isfile(filepath):
                print(f"File '{filename}' not found in current directory.")
            else:
                try:
                    with open(filepath, "r") as f:
                        code = f.read()
                        exec(code, globals())
                except Exception as e:
                    print(f"RuntimeError: {e}")
                    
    elif command == "find":
        ext = args.strip().lower().lstrip(".")
        if not ext:
            print("Usage: find [ext]")
        else:
            matches = []
            for root, dirs, files in os.walk(cdirectory):
                for file in files:
                    if file.lower().endswith(f".{ext}"):
                        relative_path = os.path.relpath(os.path.join(root, file), cdirectory)
                        matches.append(relative_path)
            if matches:
                print(f"Found {len(matches)} file{'(s)' if len(matches) > 1 else ''} with extension '.{ext}':")
                for f in matches:
                    print(f" - {f}")
            else:
                print(f"No file with extension '.{ext}' found.")
                
    elif command == "df" and args.strip() == "-h":
        try:
            import shutil
            total, used, free = shutil.disk_usage(cdirectory)
            total_gb = round(total / (1024 ** 3), 2)
            used_gb = round(used / (1024 ** 3), 2)
            free_gb = round(free / (1024 ** 3), 2)
            percent_used = round((used / total) * 100, 1)
            
            print("DISK STATUS (df -h style)")
            print("-------------------------")
            print(f"Total : {total_gb} GB")
            print(f"Used  : {used_gb} GB")
            print(f"Free  : {free_gb} GB")
            print(f"Usage : {percent_used}%")
        except Exception as e:
            print(f"Error reading disk status: {e}")
            
    elif command == "stat":
        try:
            import psutil
            mem = psutil.virtual_memory()
            total_ram = round(mem.total / (1024 ** 3), 2)
            used_ram = round(mem.used / (1024 ** 3), 2)
            free_ram = round(mem.available / (1024 ** 3), 2)
            percent_ram = round(mem.percent, 1)

            print("SYSTEM STATUS")
            print("-------------")
            print(f"Total RAM : {total_ram} GB")
            print(f"Used RAM  : {used_ram} GB")
            print(f"Free RAM  : {free_ram} GB")
            print(f"Usage     : {percent_ram}%")
        except ImportError:
            print("Missing required module: psutil\nTry: pip install psutil")
        except Exception as e:
            print("Error fetching memory stats:", e)
            
    elif command == "figlet":
        try:
            from pyfiglet import Figlet
        except ImportError:
            print("Missing module 'pyfiglet'. Installing via pip...")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", "pyfiglet"])
                from pyfiglet import Figlet
            except Exception as e:
                print("Failed to install pyfiglet:", e)
                continue

        text = args.strip()
        if not text:
            print("Usage: figlet [your text]")
        else:
            fig = Figlet()
            print(fig.renderText(text))
            
    elif command == "setprompt":
        
        
        split_args = args.strip().split(" ", 1)
        flag = split_args[0] if len(split_args) >= 1 else ""
        prompt_text = split_args[1] if len(split_args) == 2 else ""

        if flag == "-d":
            prompt = "$"
            print("Prompt successfully changed to default.")
        elif flag in colors and prompt_text:
            prompt = f"{colors[flag]}{prompt_text}{reset}"
            print(f"Prompt successfully changed to: {prompt_text} (with color)")
        elif args.strip():
            prompt = args.strip()
            print(f"Prompt successfully changed to: {prompt}")
        else:
            print("Usage:")
            print(" setprompt [prompt]")
            print(" setprompt -d                  # reset")
            print(" setprompt -g GreenPrompt      # green")
            print(" setprompt -r RedPrompt        # red")
            print(" setprompt -b BluePrompt       # blue")
            print(" setprompt -w WhitePrompt      # white")
            print(" setprompt -p PurplePrompt     # purple")
            
    elif command == "error" and args.strip() == "-l":
        print("Known error codes:")
        print(" [0]    Normal exit")
        print(" [1]    General error")
        print(" [127]  Command not found")
        print(" [403]  Permission denied")
        print(" [404]  File or directory not found")
        print(" [417]  Math: Division by zero")
        print(" [130]  Interrupted (Ctrl+C)")
        print(" [999]  Unknown or custom error")

    elif command == "error" and args.strip().startswith("-man"):
        parts = args.strip().split()
        if len(parts) != 2:
            print("Usage: error -man [error_code]")
        else:
            code = parts[1]
            errdesc = {
                "0": "Normal program exit. Everything's fine.",
                "1": "General catch-all error.",
                "127": "Command not found. Typo or command does not exist.",
                "403": "Permission denied. You don't have access.",
                "404": "File or directory not found.",
                "417": "You tried dividing by zero. Not allowed.",
                "130": "You interrupted the program (KeyboardInterrupt).",
                "999": "Custom/unknown error."
            }
            print(f"[{code}] {errdesc.get(code, 'No manual entry for this error code.')}")
            
    elif command == "error":
        print("Error command usage:")
        print("  error -l        → list all known error codes")
        print("  error -man [n]  → explain error code [n]")
        print("Example:")
        print("  error -man 127")
        
    elif command == "prjctline":
        
        total_lines = 0
        target_files = [sys.argv[0]]

        for filename in target_files:
            if os.path.exists(filename):
                with open(filename, "r", encoding="utf-8") as f:
                    line_count = sum(1 for _ in f)
                    total_lines += line_count
                    

        print(f"Total lines of code in your X# CLI Project: {total_lines} lines.")
        if total_lines < 200:
            print("Still a mini project. But a cool one to begin with.")
        elif total_lines < 1000:
            print("It's getting serious. You're building something real.")
        elif total_lines < 2000:
            print("Your CLI is on par with a mini kernel. Massive respect.")
        else:
            print("Is this a terminal or a parallel universe simulator?! 😭")
            
    elif command == "about" and args.strip() == "-v":
        
        system_info = platform.system() + " " + platform.release()
        cwd = os.getcwd()
        file_size = os.path.getsize("main.py")
        total_commands = 0
        with open(sys.argv[0], "r", encoding="utf-8") as f:
            for line in f:
                if "elif command ==" and "if command ==" and "else:" in line:
                    total_commands += 1

        print("╔════════════════════════════════════════════╗")
        print("║           X# TERMINAL - VERBOSE MODE       ║")
        print("╠════════════════════════════════════════════╣")
        print(f"║ Developer      : Nara Athaya Tito Lubis    ║")
        print("║ Python Version : 3.13.2               ║")
        print(f"║ System         : {system_info:<30}║")
        print(f"║ Prompt Mode    : {prompt.replace(chr(27) + '[0m',''):<30}║")
        print(f"║ Total Commands : {line:<30}║")
        print(f"║ File Size      : {file_size} bytes{'':<20}║")
        print(f"║ Working Dir    : {cwd:<30}║")
        print("╚════════════════════════════════════════════╝")
        print("Full detail mode active.")
            
    elif command == "about":
        import datetime

        build_date = "9-3-2025"
        cli_version = "4.0"
        developer = "Nara Athaya Tito Lubis"
        prompt_clean = prompt.replace("\033[0m", " ")

        print("╔════════════════════════════════════════╗")
        print("║           X# TERMINAL SYSTEM           ║")
        print("╠════════════════════════════════════════╣")
        print(f"║ Developer   : {developer:<28}║")
        print(f"║ Version     : {cli_version:<28}║")
        print(f"║ Prompt Mode : {prompt_clean:<28}║")
        print(f"║ Lines of Code : {1471:>24}║")
        print(f"║ Build Date  : {build_date:<28}║")
        print("╚════════════════════════════════════════╝")
        print("Built with passion. Fueled by cowsay and chaos.")
        
    elif command == "cal":
        cal = __import__("calendar")
        now = datetime.now()
        year = now.year
        month = now.month

        try:
            cal_lines = cal.month(year, month).splitlines()
            header = f"╔════ {cal.month_name[month].upper()} {year} ════╗"
            print(header)
            for line in cal_lines[1:]:
                print("║ " + line.ljust(len(header) - 4) + " ║")
            print("╚" + "═" * (len(header) - 2) + "╝")
        except Exception as e:
            print("Calendar error:", e)
            
    elif command == "pigsay":
        text = args.strip()
        if not text:
            print("Usage: pigsay <your message>")
        else:
            bubble = f'  <"{text}">\n'
            pig = r"""
         (\____/)
         ( ͡ ° ͜ʖ ͡ °)   oink.
        (  >•<  )  ~~~
         ^^    ^^
            """
            print(bubble + pig)
            
    elif command == "passwordgen":
        import string

        try:
            length_input = input("Password length? (default: 12): ").strip()
            length = int(length_input) if length_input else 12

            digits_input = input("Use digits (0-9)? [y/N]: ").strip().lower()
            upper_input = input("Use uppercase letters (A-Z)? [y/N]: ").strip().lower()
            symbols_input = input("Use symbols (!@#$%)? [y/N]: ").strip().lower()

            use_digits = digits_input in ["y", "yes", "1"]
            use_upper = upper_input in ["y", "yes", "1"]
            use_symbols = symbols_input in ["y", "yes", "1"]

            all_chars = string.ascii_lowercase
            password_chars = []

            if use_digits:
                all_chars += string.digits
                password_chars.append(random.choice(string.digits))
            if use_upper:
                all_chars += string.ascii_uppercase
                password_chars.append(random.choice(string.ascii_uppercase))
            if use_symbols:
                symbols = "!@#$%^&*()-_=+"
                all_chars += symbols
                password_chars.append(random.choice(symbols))

            # Fill remaining length
            while len(password_chars) < length:
                password_chars.append(random.choice(all_chars))

            random.shuffle(password_chars)
            password = ''.join(password_chars)

            print(f"Generated password: {password}")

        except ValueError:
            print("Invalid input. Please enter a number for the length.")
            
            
    elif command == "party":
        print("🎉🎉🎉 PARTY MODE ACTIVATED 🎉🎉🎉")
        print(f"YOU WROTE {len(lines)} LINES OF CODE!!")
        print("Terminal going full HYPE in 3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        print("SYSTEM OVERLOAD! Initiating confetti.exe")
        for _ in range(100):
            print("✨✨✨✨✨✨✨✨✨✨")
            time.sleep(0.1)
            
    elif command == "passrate":
        import string

        password = input("Enter password to rate: ").strip()
        length = len(password)

        has_upper = any(c in string.ascii_uppercase for c in password)
        has_lower = any(c in string.ascii_lowercase for c in password)
        has_digit = any(c in string.digits for c in password)
        has_symbol = any(c in "!@#$%^&*()-_=+[]{};:,<.>/?\\|`~" for c in password)

        score = 0
        if length >= 8:
            score += 1
        if length >= 12:
            score += 1
        if has_upper:
            score += 1
        if has_lower:
            score += 1
        if has_digit:
            score += 1
        if has_symbol:
            score += 1

        print("\nPassword Analysis Result:")
        print(f" - Length: {length}")
        print(f" - Contains uppercase: {'Yes' if has_upper else 'No'}")
        print(f" - Contains lowercase: {'Yes' if has_lower else 'No'}")
        print(f" - Contains digits   : {'Yes' if has_digit else 'No'}")
        print(f" - Contains symbols  : {'Yes' if has_symbol else 'No'}")

        print("\nPassword Strength:", end=" ")
        if score <= 2:
            print("Very Weak")
        elif score <= 3:
            print("Weak")
        elif score <= 4:
            print("Moderate")
        elif score <= 5:
            print("Strong")
        else:
            print("Ultra Secure")
            
            
    elif command == "fortune":
        fortunes = [
            "'The road to success is always under construction.' — Unknown",
            "'You can't fix stupid. But you can vote it out.'",
            "'Life is just a game... with really bad graphics sometimes.'",
            "'Don't worry, nobody gets out of life alive anyway.'",
            "'You will find a chicken in your next meal.'",
            "'If you think education is expensive, try ignorance.'",
            "'Error 417: Fortune overload. Try again.'",
            "'Take a break from your screen. Except this one.'",
            "'Your future holds... more coding bugs.'",
            "'404: Fortune not found. Try again tomorrow.'",
            "'Try for make you are happy today. All problems can be empty.'",
            "'Ok.' — Developer of X#",
            "'School is best than phone.'"
        ]
        print(random.choice(fortunes))
        
    elif command == "funfacts":
        facts = [
            "Fun Fact: Cats have fewer toes on their back paws.",
            "Fun Fact: A day on Venus is longer than a year on Venus.",
            "Fun Fact: Water can boil and freeze at the same time.",
            "Fun Fact: The brain named itself.",
            "Fun Fact: The Eiffel Tower can grow over 15 cm in summer.",
            "Fun Fact: The first webcam watched a coffee pot.",
            "Fun Fact: Octopuses have three hearts.",
            "Fun Fact: Chicken is the closest living relative to the T-Rex.",
            "Fun Fact: Humans are the only animals that blush.",
            "Fun Fact: Space smells like seared steak (according to astronauts)."
        ]
        print(random.choice(facts))
        
    elif command == "nyancat":
        import itertools

        frames = [
            "\033[95m=^.^=   🌈🌈🌈🌈🌈🌈🌈\033[0m",
            "\033[94m=^.^=   🌈🌈🌈🌈🌈🌈🌈\033[0m",
            "\033[96m=^.^=   🌈🌈🌈🌈🌈🌈🌈\033[0m",
            "\033[92m=^.^=   🌈🌈🌈🌈🌈🌈🌈\033[0m",
            "\033[93m=^.^=   🌈🌈🌈🌈🌈🌈🌈\033[0m",
            "\033[91m=^.^=   🌈🌈🌈🌈🌈🌈🌈\033[0m"
        ]

        print("🌈 NYANCAT MODE ENABLED. CTRL+C to stop.")
        time.sleep(1)
        try:
            for frame in itertools.cycle(frames):
                print(frame)
                time.sleep(0.0)
        except KeyboardInterrupt:
            print("\n😸 Nyan Cat ESCAPED! You're safe for now.")
            
    elif command == "rave":
        import itertools
        colors = ["\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m", "\033[96m"]
        texts = ["RAVE MODE!", "🎵 DROP THE BASS 🎶", "💃🕺", "X# PARTY TIME", "🌈🌈🌈", "TERMINAL DANCE FLOOR", "🔥🔥🔥"]
        
        print("🚨 Entering RAVE MODE. Press CTRL+C to escape the party.")
        time.sleep(1)

        try:
            while True:
                color = random.choice(colors)
                text = random.choice(texts)
                print(f"{color}{text.center(50)}\033[0m")
                time.sleep(0.05)
        except KeyboardInterrupt:
            print("\nRave ended. Terminal cooling down...")
    


    elif command == "hack":
        import itertools
        import time
        import os
        import random

        green = '\033[92m'
        reset = '\033[0m'

        os.system("cls" if os.name == "nt" else "clear")

        lines = [
            "root@X# ~ $ ping 192.168.0.1",
            "[+] Port 22 open",
            "[+] Injecting payload...",
            "[!] Bypassing firewall...",
            ">>> ACCESS GRANTED <<<",
            "root@X# ~ $ ping windpowos.com",
            "PORT 8080 — STATUS: OPEN",
            "[x] Proxy tunnel established",
            "[+] Dumping credentials...",
            ">> decrypting firewall rules...",
            "AUTH TOKEN: 0x4f2a3d... VERIFIED",
            "[+] Admin cookie injected",
            "TRACE: 172.16.254.1 → 8.8.8.8 via 10.0.0.1",
            "SYSTEM BREACH DETECTED!",
            "[+] Injecting chaos.dll into kernel.sys",
            f"[!] Tracking user: {username}",
            "[+] Brute-forcing password... success!",
            "root@localhost:~# sudo windai --override-mode",
            f"[!] ROOTING DEVICE {os.name}, USERNAME DETECTED!"
            f"PING: 8.8.8.8",
            "[+] ROOTING USER..."
        ]

        try:
            for i in itertools.cycle(lines):
                print(green + random.choice(lines) + reset)
                time.sleep(0.03)
        except KeyboardInterrupt:
            print(reset + "\nHack teminated.")
            
    elif command == "sneksay":
        snake = args.strip()
        if not snake:
            print("Usage: sneksay <your message>")
        else:
            print(f'  "{snake}"')
            print("   \\")
            print("    ~~~~~")
            print("   ( u.u )")
            print("    )   )>  ssssss...")
            print("   (   (")
            
    elif command == "which":
        cmdname = args.strip()
        if not cmdname:
            print("Usage: which [cmd] or which [pkg]")
        elif cmdname in commands:
            print(f"{cmdname}: built-in command")
        elif cmdname in available_package:
            print(f"{cmdname}: built-in pkg")
        else:
            print(f"{cmdname}: command not found")
            
    elif command == "catsay":
        text = args.strip()
        if not text:
            print("Usage: catsay [text]")
        else:
            cat = r'''
  ／＞　 フ
 | 　_　_| 
／` ミwノ
/　　　　 |
(　 ヽ＿ヽ_)__)
＼二つ
'''
            bubble = f"-------\n{text}\n-------"
            print(bubble + "\n" + cat)
            
    elif command == "lolcat":
          loltext = args.strip()
          

          colored_text = ""

          for i, c in enumerate(loltext):
                # Hue calculation with sin wave formula
                r = int(math.sin(0.1 * i + 0) * 127 + 128)
                g = int(math.sin(0.3 * i + 2) * 127 + 128)
                b = int(math.sin(0.2 * i + 4) * 127 + 128)


                r_ansi = int(r / 51)
                g_ansi = int(g / 51)
                b_ansi = int(b / 51)
                color_code = 16 + 36 * r_ansi + 6 * g_ansi + b_ansi

                colored_text += f"\033[38;5;{color_code}m{c}"

          colored_text += "\033[0m\n"  # reset color
          sys.stdout.write(colored_text)
          sys.stdout.flush()
          
    elif command == "hashgen":
       import hashlib
       
       hash_type = input("Enter type of hash: ").strip().lower()
       
       if hash_type not in ["md5", "sha1", "sha256"]:
           print("Invalid hash type. Abort.")
       else:
           text = input("Some text for hashing:  ").strip().lower()
           if not text:
               print("Abort.")
           else:
               if hash_type == "md5":
                   result = hashlib.md5(text.encode()).hexdigest()
               elif hash_type == "sha1":
                   result = hashlib.sha1(text.encode()).hexdigest()
               elif hash_type == "sha256":
                   result = hashlib.sha256(text.encode()).hexdigest()
               
               print("Result:", result)
               
    elif command == "base64gen":
        import base64
        text = input("Text to encode (Base64): ").strip()
        if not text:
            print("No text given.")
        else:
            encoded = base64.b64encode(text.encode("utf-8")).decode("utf-8")
            print(f"Base64 encoded result: {encoded}")
            
    elif command == "base64decode":
        import base64
        text = input("Base64 text to decode: ").strip()
        if not text:
            print("No text given.")
        else:
            try:
                decoded = base64.b64decode(text.encode("utf-8")).decode("utf-8")
                print(f"Decoded result: {decoded}")
            except Exception as e:
                print("Invalid Base64 input.")
                
    elif command == "uuidgen":
        import uuid
        parts = args.strip().split()
        if not args:
            print("Generated UUID (v4):")
            print(str(uuid.uuid4()))
        elif len(parts) == 2 and parts[0] == "-n" and parts[1].isdigit():
            count = int(parts[1])
            print(f"Generating {count} UUID(s):")
            for _ in range(count):
                print(str(uuid.uuid4()))
        else:
            print("Usage: uuidgen    OR    uuidgen -n <number>")
            
    elif command == "settings":
        while True:
            print("\n--- X# Settings Menu ---")
            print("1. Change Prompt")
            print("2. Change Username")
            print("3. Change Prompt Color")
            print("4. Reset to Default")
            print("5. Exit Settings")

            choice = input("Choose an option (1-5): ").strip()

            if choice == "1":
                new_prompt = input("Enter new prompt symbol (e.g. $, >>>, >): ").strip()
                if new_prompt:
                    prompt = new_prompt
                    print(f"Prompt set to: {prompt}")
            elif choice == "2":
                new_user = input("Enter new username: ").strip()
                if new_user:
                    username = new_user
                    env_vars["USER"] = new_user
                    print(f"Username changed to: {username}")
            elif choice == "3":
                print("Available colors: -g (green), -r (red), -b (blue), -p (purple), -w (white)")
                flag = input("Enter color flag (e.g. -g): ").strip()
                new_prompt_text = input("Prompt text: ").strip()
                if flag in colors and new_prompt_text:
                    prompt = f"{colors[flag]}{new_prompt_text}{reset}"
                    print("Prompt updated with color.")
                else:
                    print("Invalid color or prompt.")
            elif choice == "4":
                username = "local"
                env_vars["USER"] = username
                prompt = "$"
                print("Settings reset to default.")
            elif choice == "5":
                print("Exiting settings.")
                break
            else:
                print("Invalid choice.")
                
    elif command == "clock":
        try:
            print("Press Ctrl+C to stop.")
            while True:
                now = time.strftime("%H:%M:%S")
                print(f"\r{now}", end="", flush=True)
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nClock stopped.")
            

    elif command == "expand":
        filename = args.strip()
        if not filename:
            print("Usage: expand [filename]")
        elif not os.path.isfile(filename):
            print(f"File '{filename}' not found.")
        else:
            try:
                with open(filename, "r") as f:
                    lines = f.readlines()
                expanded_lines = [line.expandtabs(4) for line in lines]
                for line in expanded_lines:
                    print(line)
            except Exception as e:
                print(f"Error: {e}")
                
    elif command == "rev":
        text = args.strip()
        if not text:
            print("Usage: rev [text]")
        else:
            print(text[::-1])
            
    elif command == "wc":
        filename = args.strip()
        if not filename:
            print("Usage: wc [filename]")
        elif not os.path.isfile(filename):
            print(f"File '{filename}' not found.")
        else:
            try:
                with open(filename, "r", encoding="utf-8") as f:
                    content = f.read()
                lines = content.splitlines()
                words = content.split()
                chars = len(content)
                print(f"Lines: {len(lines)}, Words: {len(words)}, Characters: {chars}")
            except Exception as e:
                print(f"Error reading file: {e}")
                
    elif command == "rot13":
        text = args.strip()
        if not text:
            print("Usage: rot13 [text]")
        else:
            result = ""
            for c in text:
                if "a" <= c <= "z":
                    result += chr((ord(c) - ord("a") + 13) % 26 + ord("a"))
                elif "A" <= c <= "Z":
                    result += chr((ord(c) - ord("A") + 13) % 26 + ord("A"))
                else:
                    result += c
            print(result)
            
    elif command == "rps":
        options = ["rock", "paper", "scissors"]
        user_choice = args.strip().lower()

        if user_choice not in options:
            print("Usage: rps [rock|paper|scissors]")
        else:
            computer_choice = random.choice(options)
            print(f"You: {user_choice}")
            print(f"Computer: {computer_choice}")

            if user_choice == computer_choice:
                print("Result: It's a tie!")
            elif (
                (user_choice == "rock" and computer_choice == "scissors") or
                (user_choice == "paper" and computer_choice == "rock") or
                (user_choice == "scissors" and computer_choice == "paper")
            ):
                print("Result: You win!")
            else:
                print("Result: You lose!")
                
    elif command == "8ball":
        question = args.strip()
        if not question.endswith("?") or not question:
            print("Usage: 8ball [your question?]")
        else:
            responses = [
                "Yes, definitely.",
                "Nope, never.",
                "Ask again later.",
                "Maybe yes, maybe no.",
                "100% YES.",
                "Are you kidding me?",
                "No comment.",
                "Trust me, you don't want to know.",
                "For sure!",
                "Hmm... highly unlikely.",
                "Just believe.",
                "Absolutely not.",
                "The stars say yes.",
                "Try again when you're serious.",
                "Absolutely i dont know.",
                "404 Brain Not Found. Try again later."
            ]
            print(f"You asked: {question}")
            print("8ball says:", random.choice(responses))
            
    elif command == "debunix":
        if args.strip() == "--run":
            print("Launching DebUnix shell...")
            try:
                subprocess.Popen(["sh", "-i"] if not termux_detected else ["bash", "-i"]).wait()
            except Exception as e:
                print("Failed to launch DebUnix shell.", end=" ")
                print(str(e))
        elif args.strip() == "--about":
            print("DebUnix v1.0.")
            print("A minimalist shell that use sh/bash for running.")
            print("shell = sh\nsh = bourne shell")
            help_reference = input("help> ")
            if help_reference == "sh":
                subprocess.Popen(["sh", "-i"] if not termux_detected else ["bash", "-i"]).wait()
                
        else:
            print("Usage: debunix --run or debunix --about")
            
    elif command == "bulldoiser":
        bulldoiser = args.strip()
        appname = random.choice(["newfile", "wpa", "batch", "debug"])

        if bulldoiser == "init":
            desc = """ [App]
name =
version =
main =
author =
description =
icon =

[Build]
entry =
onefile =
windowed =
compress =
optimize =
target_os =

[Dependency]
require_runtime =
xsharp_version =
sdk_path =

[Output]
dir =
filename =
history_tracking =
"""
            try:
                if os.path.exists("bulldoiser.spec"):
                    print("E: File Exists!")
                else:
                    with open("bulldoiser.spec", "w") as f:
                        f.write(desc)
                    print("bulldoiser.spec is successfully created, ready to customize!")
            except BaseException as e:
                print("E: Cannot create!", e)

        elif bulldoiser == "windpow debug":
            try:
                if not os.path.exists("bulldoiser.spec"):
                    print("E: bulldoiser.spec is not available!")
                else:
                    with open(f"{appname}.wpa", "wb") as f:
                        f.write(b"\x57\x50\x41\x01")
            except BaseException as e:
                print(f"E: {e}")
                
        else:
            print("Usage: bulldoiser windpow debug or bulldoiser init")
            
    elif command == "chmod":
        args_parts = args.strip().split()
        if len(args_parts) != 2:
            print("Usage: chmod [mode: like 755] [filename]")
        else:
            mode_str, filename = args_parts
            filepath = os.path.join(cdirectory, filename)

            try:
                mode = int(mode_str, 8)  # 755 (string) -> 0o755 (octal)
                os.chmod(filepath, mode)
                print(f"Permissions of '{filename}' changed to {mode_str}.")
            except ValueError:
                print("Invalid mode. Use numbers like 755, 644, 600, etc.")
            except FileNotFoundError:
                print(f"File '{filename}' not found.")
            except PermissionError:
                print("Permission denied.")
            except Exception as e:
                print(f"chmod error: {e}")
                
    elif command == "chroot":
        target = args.strip()
        if not target:
            print("Usage: chroot [path]")
        elif not os.path.isdir(target):
            print("Not a directory.")
        else:
            try:
                os.chdir(target)
                cdirectory = target
                default_home = target
                env_vars["HOME"] = target
                prompt = "[chroot] $"
                print(f"Changed root directory to '{target}'.")
            except Exception as e:
                print(f"Failed to chroot: {e}")
            continue
            
    elif command == "unchroot":
        try:
            original_home = "/storage/emulated/0/X#init" if os.name != "nt" else "C:\\Users"
            os.chdir(original_home)
            cdirectory = original_home
            default_home = original_home
            env_vars["HOME"] = original_home
            prompt = "$"
            print("Returned to default root directory.")
        except Exception as e:
            print(f"Failed to unchroot: {e}")
            
    elif command == "checkperm":
        filename = args.strip()
        if not filename:
            print("Usage: checkperm [filename]")
        else:
            filepath = os.path.join(cdirectory, filename)
            if not os.path.exists(filepath):
                print(f"[404] File or directory '{filename}' not found.")
            else:
                import stat

                mode = os.stat(filepath).st_mode
                can_read = os.access(filepath, os.R_OK)
                can_write = os.access(filepath, os.W_OK)
                can_exec = os.access(filepath, os.X_OK)

                print(f"Permissions for: {filename}")
                print(f" - Raw Mode     : {oct(mode)}")
                print(f" - Readable     : {'✓' if can_read else '×'}")
                print(f" - Writable     : {'✓' if can_write else '×'}")
                print(f" - Executable   : {'✓' if can_exec else '×'}")
                
    elif command == "top" and args.strip() == "--simple":
        try:
            import psutil
            print(f"{'PID':<8} {'Name':<25} {'CPU%':<8} {'Memory%':<8}")
            print("-" * 60)
            for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
                try:
                    pid = proc.info['pid']
                    name = proc.info['name'][:24] if proc.info['name'] else "Unknown"
                    cpu = proc.info['cpu_percent']
                    mem = proc.info['memory_percent']
                    print(f"{pid:<8} {name:<25} {cpu:<8.1f} {mem:<8.1f}")
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue
        except ImportError:
            print("Missing required module: psutil\nTry: pip install psutil")
                
    elif command == "top":
        try:
            import psutil
            import os

            print("Press Ctrl+C to stop.\n")
            while True:
                os.system("cls" if os.name == "nt" else "clear")
                print(f"{'PID':<8} {'Name':<25} {'CPU%':<8} {'Memory%':<8}")
                print("*" * 60)
                for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
                    try:
                        pid = proc.info['pid']
                        name = proc.info['name'][:24] if proc.info['name'] else "Unknown"
                        cpu = proc.info['cpu_percent']
                        mem = proc.info['memory_percent']

                        if cpu > 5:
                            cpu_display = f"\033[91m{cpu:<8.1f}\033[0m"  # red
                        elif cpu >= 3:
                            cpu_display = f"\033[93m{cpu:<8.1f}\033[0m"  # yellow
                        else:
                            cpu_display = f"{cpu:<8.1f}"  # white

                        print(f"{pid:<8} {name:<25} {cpu_display} {mem:<8.1f}")
                    except (psutil.NoSuchProcess, psutil.AccessDenied):
                        continue
                time.sleep(1)
        except ImportError:
            print("Missing required module: psutil\nTry: pip install psutil")
        except KeyboardInterrupt:
            print("\nTop stopped.")
    
    elif command == "htop":
        try:
            import psutil
            import os

            def usage_bar(percent, length=20):
                filled = int(length * percent / 100)
                return "█" * filled + "░" * (length - filled)

            print("Press Ctrl+C to stop.\n")
            while True:
                os.system("cls" if os.name == "nt" else "clear")
                print(f"{'PID':<8} {'Name':<25} {'CPU%':<8} {'CPU BAR':<22} {'MEM%':<8} {'MEM BAR'}")
                print("*" * 90)

                processes = []
                for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
                    try:
                        processes.append(proc.info)
                    except (psutil.NoSuchProcess, psutil.AccessDenied):
                        continue

                
                processes.sort(key=lambda p: p['cpu_percent'], reverse=True)

                for proc in processes[:15]:
                    pid = proc['pid']
                    name = proc['name'][:24] if proc['name'] else "Unknown"
                    cpu = proc['cpu_percent']
                    mem = proc['memory_percent']

                    # Warna CPU
                    if cpu > 50:
                        cpu_str = f"\033[91m{cpu:<8.1f}\033[0m"
                    elif cpu >= 20:
                        cpu_str = f"\033[93m{cpu:<8.1f}\033[0m"
                    else:
                        cpu_str = f"{cpu:<8.1f}"

                    cpu_bar = usage_bar(cpu)
                    mem_bar = usage_bar(mem)

                    print(f"{pid:<8} {name:<25} {cpu_str} {cpu_bar:<22} {mem:<8.1f} {mem_bar}")

                time.sleep(1)

        except ImportError:
            print("Missing required module: psutil\nTry: pip install psutil")
        except KeyboardInterrupt:
            print("\nHtop stopped.")
            
    elif command == "pycheck":
        pythonchecked = args.strip()
        if not pythonchecked:
            print("Usage: pycheck [code]")
        else:
            try:
                compile(pythonchecked, "<string>", "exec")
                print("Syntax result: True")
            except BaseException as e:
                print(f"Syntax result: Error: {type(e).__name__}")
                
    elif command == "du" and args.strip() == "-h":
        target = cdirectory
        if args.strip() and args.strip() != "-h":
            target = os.path.join(cdirectory, args.strip())
        if not os.path.exists(target):
            print(f"Path '{target}' not found.")
        else:
            total = 0
            if os.path.isfile(target):
                total = os.path.getsize(target)
            else:
                for dirpath, dirnames, filenames in os.walk(target):
                    for f in filenames:
                        fp = os.path.join(dirpath, f)
                        try:
                            total += os.path.getsize(fp)
                        except FileNotFoundError:
                            pass
            size_bytes = float(total)
            for unit in ['B','KB','MB','GB','TB']:
                if size_bytes < 1024:
                    break
                size_bytes /= 1024.0
            print(f"{size_bytes:.2f} {unit}\t{target}")                
              
      
      
                      
                        

        
    else:
        closest = difflib.get_close_matches(command, commands, n=4, cutoff=0.5)
        if closest:
            print("Unknown command. Did you mean:")
            for cmd in closest:
                print(f" - {cmd}")
        else:
            print(f"[127] '{command}': not found")
            
# End of File (EOF)

