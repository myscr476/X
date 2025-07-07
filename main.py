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
answerrepo = "local-repo"
userid = "ID001"
history = []
url = ""
pkginstaller = "no"
pkginstallera = "segfault"
repos = [
    "sysrep",
    "termux-official-repo",
    "x-repo",
    "locate.repo.all.90repo",
    "local-repo"
]
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
    "cat [path] [file name]",
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
    "bash"
]
xstatus = "NO"
windai = "soxca"
aliases = {}
verapt = False
cdirectory = "C:\\Users" if os.name == 'nt' else "/storage/emulated/0/X#init"
prootname = "root"
canloginasroot = False
loadingspinner = ['\\', '-', '/', '|']
offline_mode = False
prootuser = "local"
start_time = time.time()

os.chdir(cdirectory)

print("Welcome to X# Interpreter.")
print("Type 'help' for help.")

while True:
    try:
        default_home = "/storage/emulated/0/X#init"

        if cdirectory == default_home:
            prompt_path = "~"
        elif cdirectory.startswith(default_home):
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

    if command in aliases:
        aliased_command = aliases[command]
        history.append(aliased_command)
        command = aliased_command
        continue
        
    elif command == "exit":
        break

    elif command == "joingr":
        webbrowser.open("https://chat.whatsapp.com/FzudiFhaocT4vXHmxVks1N")

    elif command == "information":
        print("X# is a programming language that allows you to make an app or game (or another software). This language is built with Python, in 2006.")

    elif command.startswith("mkdir"):
        try:
            path = "C:\\" if os.name == 'nt' else "/storage/emulated/0"
            os.chdir(path)
            partmkdir = command[len("mkdir "):].strip()
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

    elif command.startswith("w/"):
        search_query = command[2:].strip()
        if search_query:
            url = f"https://www.google.com/search?q={quote(search_query)}"
            print("Please wait...")
            time.sleep(2)
            webbrowser.open(url)
        else:
            print("Failed to fetch")

    elif command.startswith("s/"):
        search_term = command[2:].strip().lower()
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

    elif command.startswith("echo"):
        print(command[len("echo"):].strip())

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

    elif command.startswith("setname"):
        new_name = command[len("setname"):].strip()
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

    elif command.startswith("pkg install"):
        if offline_mode:
            print("Can't install package. Check your internet connection.")
        else:
            pkg_name = command[len("pkg install"):].strip().lower()
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

    elif command.startswith("alias"):
        parts = command.split(" ", 2)
        if len(parts) < 3:
            print("Usage: alias [name] [real command]")
        else:
            aliases[parts[1]] = parts[2]
            print(f"Alias '{parts[1]}' set to '{parts[2]}'")

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
                        printedtext = code[len("nugget('", "')"):].strip()
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
        while True:
            print("y")

    elif command == "ver":
        print("Version 2.5.1.")

    elif command == "apt update":
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

    elif command.startswith("mkfl"):
        try:
            path = "C:\\" if os.name == 'nt' else "/storage/emulated/0"
            os.chdir(path)
            filename = command[len("mkfl "):].strip()
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

    elif command.startswith("cat"):
        parts = command.strip().split(" ", 2)
        if len(parts) < 3:
            print("Type a path and filename to read the file.")
        else:
            catpath = parts[1]
            catname = parts[2]
            fullpath = os.path.join(catpath, catname)
            if os.path.exists(catpath) and os.path.isfile(fullpath):
                try:
                    with open(fullpath, "r") as f:
                        print(f.read())
                except Exception as e:
                    print(e)
            else:
                print(f"File not found in path {catpath}")

    elif command.startswith("pip install"):
        piptarget = command[len("pip install "):].strip()
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

    elif command.startswith("tree"):
        target_path = command[len("tree"):].strip()
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
                    prootname = input("Enter new username (this is required if you not need root for user):  ")
                    if not prootname:
                        prootname = "localroot"
                    prootpassword = input(f"Enter password for {prootname}:  ")
                    print("Please wait...")
                    time.sleep(random.randint(2, 5))
                    print(f"{prootname} is succesfully created!")
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
                    
    elif command.startswith("/rm"):
        parts = command.split(" ")
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
                
    elif command.startswith("pkg uninstall"):
        pkg_name_that_to_uninstall = command[len("pkg uninstall "):].strip()
        
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
            new_path = command[len("cd"):].strip()
            dangerous_paths = ["/", "/storage", "/storage/emulated"]

            if new_path.startswith("$HOME"):
                new_path = new_path.replace("$HOME", "/storage/emulated/0/X#init")
            if new_path.startswith("~"):
                new_path = new_path.replace("~", "/storage/emulated/0/X#init")

            if not os.path.isabs(new_path):
                target = os.path.join(cdirectory, new_path)
            else:
                target = new_path

            if os.path.abspath(target) in [os.path.abspath(p) for p in dangerous_paths]:
                print("Access denied.")
                continue

            if not os.path.exists(target):
                print("Path not found.")
                continue

            os.chdir(target)
            cdirectory = target

        except Exception as e:
            print(f"{type(e).__name__}: {e}")
    
            
    elif command == "pwd":
        print(os.getcwd())
     
    elif command.startswith("math"):
        expr = command[len("math"):].strip().replace(" ", "")
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
            
    elif command.startswith("nano "):
        filename = command[len("nano "):].strip()
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
                subprocess.run(shell_cmd, shell=True)
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
                subprocess.run(shell_cmd, shell=True)
            except Exception as e:
                print("bash error:", e)
        
    else:
        closest = difflib.get_close_matches(command, commands, n=3, cutoff=0.4)
        if closest:
            print("Unknown command. Did you mean:")
            for cmd in closest:
                print(f" - {cmd}")
        else:
            print(f"'{command}' is not recognized as an internal or external command,\noperable program or batch file.")
            
# End of File (EOF)