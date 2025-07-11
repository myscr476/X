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
answerrepo = "local-repo"
userid = "ID001"
repos = [
    "sysrep",
    "termux-official-repo",
    "x-repo",
    "locate.repo.all.90repo",
    "local-repo"
]
env_vars = {
    "USER": username,
    "ID": userid,
    "REPO": answerrepo,
    "CDIR": cdirectory,
}
history = []
url = ""
pkginstaller = "no"
pkginstallera = "segfault"
available_package = ["sys", "pyrun", "lv", "x#builder", "xpackage", "$pkg", "pip"]
commands = [
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
    "stat"
]
xstatus = "NO"
windai = "soxca"
aliases = {}
verapt = False
need_update = random.choice([True, False, "Needed but not updating all package"])
prootname = "root"
canloginasroot = False
loadingspinner = ['\\', '-', '/', '|']
offline_mode = False
prootuser = "local"
start_time = time.time()

termux_detected = "com.termux" in sys.executable or os.getenv("PREFIX") == "/data/data/com.termux/files/usr"
if termux_detected:
    print("WARNING: Some feature may not working properly in Termux. Like 'sh', 'joingr'.")
    print("Try for run in Python REPL/Pydroid 3/Ubuntu/WSL.\n")

os.chdir(cdirectory)
user_input = ""

has_checked_update = False
need_update = False

print("Welcome to X# Interpreter!")
print("Type 'help' for help.")

while True:
    try:
        default_home = "/storage/emulated/0/X#init" if os.name != 'nt' else r"C:\Users"

        if cdirectory == default_home:
            prompt_path = "~"
        elif default_home and cdirectory.startswith(default_home + "/"):
           prompt_path = cdirectory.replace(default_home, "~", 1)
        else:
            parts = cdirectory.strip("/").split("/")
            if len(parts) >= 2:
                prompt_path = ".../" + "/".join(parts[-2:])
            else:
                prompt_path = cdirectory
                
        command = input(f"\033[93m{prompt_path} $\033[0m").strip()
        
    except EOFError:
        print("Exiting...")
        break
    except KeyboardInterrupt:
        print("Exiting...")
        break
    except BaseException as e:
        print(e)

    history.append(command)
    try:
        with open("datahistory.txt", "a") as f:
            f.write(f"{command}\n")
    except Exception as e:
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
        
    if command == "exit":
        break

    elif command == "joingr":
        webbrowser.open("https://chat.whatsapp.com/FzudiFhaocT4vXHmxVks1N")

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
        except IOError as e:
            print(f"IOError: {e}")
        except Exception as e:
            print(f"{type(e).__name__}: {e}")
        finally:
            os.chdir(cdirectory)

    elif command == "dir":
        os.chdir('C:/' if os.name == 'nt' else '/storage/emulated/0')
        print(os.listdir())
        os.chdir(cdirectory)

    elif command == "help":
        print("Built-in commands:\n----------------\n[.[[", ", ".join(commands), "\n------------------")

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
            print("Error:", e)

    elif command == "clear":
        os.system("cls" if os.name == "nt" else "clear")
        print("Welcome to X# Interpreter.")
        print("Type 'help' for help.")

    elif command == "setname":
        new_name = args.strip()
        if new_name:
            try:
                if os.path.isfile("datalog.txt"):
                    with open("datalog.txt", "a") as f:
                        f.write(f"[LOG DATA] {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: {new_name}\n")
                    username = new_name
                    print("Username changed!")
                else:
                    with open("datalog.txt", "w") as f:
                        f.write(f"[LOG DATA] {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: {new_name}\n")
                        username = new_name
                        print("Username changed!")
            except Exception as e:
                print(e)
        else:
            print("Type a username.")

    elif command == "pkg" and args.strip() == "install":
        if offline_mode:
            print("Can't install package. Check your internet connection.")
        else:
            pkg_name = args.strip().lower()
            if not pkg_name:
                print("Please provide a pkg name.")
                continue
            if not re.match(r'^[a-zA-Z0-9\-_]+$', pkg_name):
                print("Invalid package name.")
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
        parts = args.strip().split(" ", 1)
        if len(parts) < 2:
            print("Usage: alias [name] [real command]")
        else:
            alias_name = parts[0]
            alias_value = parts[1]
            aliases[alias_name] = alias_value
            print(f"Alias '{alias_name}' set to '{alias_value}'")

    elif command == "whoami":
        print(f"User: {username}\nID: {userid}")

    elif command == "xeditor":
        if xstatus == "NO":
            print("Cannot access X# Editor")
        else:
            print("Welcome to X# Editor!")
            print("Starts with new code or set id?")
            sub = input(">>>  ")
            if sub == "Starts with new code":
                code_lines = []
                while True:
                    code = input("~  ")
                    if code == "exit":
                        break
                    elif code.startswith("nugget('") and code.endswith("')"):
                        printedtext = code[8:-2]
                        code_lines.append(f"nugget('{printedtext}'")
                    elif code.startswith("echothis "):
                        echothistext = code[len("echothis "):].strip()
                        code_lines.append(f"echothis {echothistext}")
                    elif code.startswith("save "):
                        filename = code[len("save "):].strip()
                        if not filename:
                            print("File Empty!")
                        else:
                            with open(f"{filename}.xpf", "w") as f:
                                for line in code_lines:
                                    f.write(line + "\n")
                            print(f"File '{filename}' saved in directory {cdirectory}.")
                    else:
                        code_lines.append(code)
            elif sub == "Set id":
                stepcode = input("---  ")
                if re.match(r"^ID{6}$", stepcode):
                	print("Checking ID format...")
                	time.sleep(2)
                	print("The ID is valid!")
                	time.sleep(1)
                	print("nugget('Hello!')")
                	print("```Hello!")
                	
                	while True:
                	    code = input(">>>")
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
        if not args.strip():
            while True:
                print("y")
        else:
            while True:
                print(message)

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
        parts = args.strip().split(" ", 1)
        if len(parts) < 2:
            print("Type a path and filename to read the file.")
        else:
            catpath = parts[0]
            catname = parts[1]
            fullpath = os.path.join(catpath, catname)
            if os.path.exists(catpath) and os.path.isfile(fullpath):
                try:
                    with open(fullpath, "r") as f:
                        print(f.read())
                except Exception as e:
                    print(e)
            else:
                print(f"File not found in path {catpath}")

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
                            while True:
                                sublogin = input(f"{prootname}@localhost:~$ ")
                                if sublogin == "exit":
                                    print("logout")
                                    break
                                else:
                                    print("[Error] Unknown command.")
                            break
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
            print("No such file or directory.")
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
            print("Permission denied.")
        except Exception as e:
            print("Error:", e)
            
    elif command == "selfdestruct":
        print("[WARNING] Initiating self-destruction sequence...")
        for i in range(1, 6, +1):
            print(f"Self-destruct in {i}...")
            time.sleep(1)
        print("BOOM. X# Interpreter terminated.")
        break
        
    elif command == f"login --as {prootuser}":
        while True:
            proot = input(f"{prootuser}@localhost:~$ ")
            if proot == "exit":
                print("logout")
                break
            else:
                print("[Error] Unknown command.")
                
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
            print("Error: Division by zero is not allowed.")
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
    Displays all built-in commands in X# Interpreter."""
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

        show_detail = False
        target_dir = cdirectory

        if "-la" in args:
            show_detail = True
            args = args.replace("-la", "").strip()

        if args:
            if args.startswith("~"):
                args = args.replace("~", "/storage/emulated/0/X#init")
            target_dir = os.path.abspath(os.path.join(cdirectory, args))

        try:
            files = os.listdir(target_dir)
            if not show_detail:
                for f in files:
                    print(f)
            else:
                print(f"{'Name':<30} {'Size':>10}  {'Modified Time'}")
                print("-" * 60)
                for f in files:
                    path = os.path.join(target_dir, f)
                    size = os.path.getsize(path)
                    mtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(path)))
                    print(f"{f:<30} {size:>10}  {mtime}")
        except Exception as e:
            print("Error:", e)
            
    elif command.startswith("mv "):
        args = command[len("mv "):].strip().split()

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
                    
    elif command.startswith("cowsay"):
        text = args.strip()
        if not text:
            print("Usage: cowsay <your message>")
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
                 print("Format: rename [old_name] [new_name]")
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
            print("Usage: find [ext] (tanpa titik)")
        else:
            matches = []
            for root, dirs, files in os.walk(cdirectory):
                for file in files:
                    if file.lower().endswith(f".{ext}"):
                        relative_path = os.path.relpath(os.path.join(root, file), cdirectory)
                        matches.append(relative_path)
            if matches:
                print(f"Found {len(matches)} file(s) with extension '.{ext}':")
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
            
        
    else:
        closest = difflib.get_close_matches(command, commands, n=3, cutoff=0.4)
        if closest:
            print("Unknown command. Did you mean:")
            for cmd in closest:
                print(f" - {cmd}")
        else:
            print(f"'{command}' is not recognized as an internal or external command,\noperable program or batch file.")
            
# End of File (EOF)