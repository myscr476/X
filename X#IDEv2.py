from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.dialog import MDDialog
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.toolbar import MDTopAppBar
import io, contextlib, os

class XSharpExecutor:
    def desugar_condition(self, condition):
        replacements = {
            " is same with ": " == ",
            " is not ": " != ",
            " is ": " is ",
            " and ": " and ",
            " or ": " or ",
            " plus ": " + ",
            " minus ": " - ",
            " greater than ": " > ",
            " less than ": " < ",
            " greater or equal ": " >= ",
            " less or equal ": " <= "
        }
        for xsharp, python in replacements.items():
            condition = condition.replace(xsharp, python)
        return condition.strip()

    def to_python(self, line):
        line = line.strip()
        if line.startswith("if ") and "::" in line:
            cond = line[3:line.find("::")].strip()
            if not cond:
                raise SyntaxError(f"SyntaxFault: invalid syntax '{line}'")
            return f"if {self.desugar_condition(cond)}:"
        elif line.startswith("elseorif ") and "::" in line:
            cond = line[9:line.find("::")].strip()
            if not cond:
                raise SyntaxError(f"SyntaxFault: invalid syntax '{line}'")
            return f"elif {self.desugar_condition(cond)}:"
        elif line == "else::":
            return "else:"
        elif line.startswith("nugget("):
            return line.replace("nugget", "print")
        elif line.startswith("use "):
            mod = line[len("use "):].strip()
            return f"import {mod}"
        elif "get{" in line:
            return f"# Fetch variable → {line}"
        elif line.startswith("request.get("):
            return f"import requests\n{line}"
        elif line.startswith("startwith("):
            args = line[len("startwith("):-1].split(",")
            if len(args) == 2:
                return f"{args[0].strip()}.startswith({args[1].strip()})"
            raise SyntaxError(f"SyntaxFault: invalid startwith usage '{line}'")
        elif line.startswith("endwith("):
            args = line[len("endwith("):-1].split(",")
            if len(args) == 2:
                return f"{args[0].strip()}.endswith({args[1].strip()})"
            raise SyntaxError(f"SyntaxFault: invalid endwith usage '{line}'")
        elif line == "insta()":
            return "# insta() → simulated install"
        elif line.startswith("#") or line == "":
            return line
        else:
            raise SyntaxError(f"SyntaxFault: invalid syntax '{line}'")

    def run_code(self, code):
        python_code = []
        lines = code.split("\n")
        for i, line in enumerate(lines):
            try:
                python_line = self.to_python(line)
                python_code.append(python_line)
            except SyntaxError as e:
                return f"{e} (line {i+1})"

        joined_code = "\n".join(python_code)
        try:
            loc = {}
            stdout_capture = io.StringIO()
            with contextlib.redirect_stdout(stdout_capture):
                exec(joined_code, {}, loc)
            output = stdout_capture.getvalue()
            return output.strip() if output.strip() else ""
        except Exception as e:
            return f"{type(e).__name__}: {e}"

class XSharpIDEApp(MDApp):
    def build(self):
        self.executor = XSharpExecutor()
        self.xfiles_path = "/storage/emulated/0/X#init/homefolder/user/appgame"

        self.dark_mode_enabled = False
        self.font_scale = 1.0

        self.theme_cls.theme_style = "Light"

        screen = MDScreen()
        main_layout = MDBoxLayout(orientation="vertical")

        self.toolbar = MDTopAppBar(
            title="X# IDE v2",
            left_action_items=[["cog", lambda x: self.open_settings_dialog(x)]]
        )

        self.code_input = MDTextField(
            hint_text="Write X# code here...",
            multiline=True,
            mode="rectangle",
            size_hint_y=None,
            height="250dp"
        )

        self.output_label = MDLabel(
            text="Output will show there.",
            theme_text_color="Secondary",
            halign="left"
        )

        self.run_button = MDRaisedButton(
            text="▶ Run",
            on_release=self.run_code
        )

        self.save_button = MDRaisedButton(
            text="Save",
            on_release=self.save_file
        )

        self.load_button = MDRaisedButton(
            text="Load",
            on_release=self.load_file
        )

        self.clear_button = MDRaisedButton(
            text="Clear",
            on_release=self.clear_code
        )

        button_layout = MDBoxLayout(size_hint_y=None, height="40dp", spacing=5)
        button_layout.add_widget(self.run_button)
        button_layout.add_widget(self.save_button)
        button_layout.add_widget(self.load_button)
        button_layout.add_widget(self.clear_button)

        scroll_output = MDScrollView()
        scroll_output.add_widget(self.output_label)

        main_layout.add_widget(self.toolbar)
        main_layout.add_widget(self.code_input)
        main_layout.add_widget(button_layout)
        main_layout.add_widget(scroll_output)

        screen.add_widget(main_layout)
        return screen

    def run_code(self, instance):
        code = self.code_input.text
        result = self.executor.run_code(code)
        self.output_label.text = f"{result}"

    def save_file(self, instance):
        try:
            filename = os.path.join(self.xfiles_path, "newfile.xpf")
            with open(filename, "w") as f:
                f.write(self.code_input.text)
            self.output_label.text = f"[Saved to newfile.xpf]"
        except FileExistsError:
            with open(filename, "a") as f:
                f.write(self.code_input.text)
            self.output_label.text = f"[Line saved to file]"

    def load_file(self, instance):
        try:
            files = [f for f in os.listdir(self.xfiles_path) if f.endswith(".xpf")]
            if not files:
                self.output_label.text = "[No .xpf file found]"
                return
            filepath = os.path.join(self.xfiles_path, files[0])
            with open(filepath, "r") as f:
                self.code_input.text = f.read()
            self.output_label.text = f"[Loaded {files[0]}]"
        except Exception as e:
            self.output_label.text = f"[Error loading file: {e}]"

    def clear_code(self, instance):
        self.code_input.text = ""
        self.output_label.text = "[Cleared input]"

    def open_settings_dialog(self, instance):
        self.dialog = MDDialog(
            title="Settings",
            type="custom",
            content_cls=self.build_settings_content(),
            buttons=[
                MDRaisedButton(text="Save", on_release=self.on_save),
                MDRaisedButton(text="Cancel", on_release=lambda x: self.dialog.dismiss())
            ]
        )
        self.dialog.open()

    def build_settings_content(self):
        self.dark_checkbox = MDCheckbox(active=self.dark_mode_enabled)
        self.font_checkbox = MDCheckbox(active=(self.font_scale > 1.0))

        layout = MDBoxLayout(orientation="vertical", spacing=10, padding=10)

        row1 = MDBoxLayout(orientation="horizontal", spacing=10)
        row1.add_widget(MDLabel(text="Enable Dark Mode", halign="left"))
        row1.add_widget(self.dark_checkbox)

        row2 = MDBoxLayout(orientation="horizontal", spacing=10)
        row2.add_widget(MDLabel(text="Large Font", halign="left"))
        row2.add_widget(self.font_checkbox)

        layout.add_widget(row1)
        layout.add_widget(row2)
        return layout

    def on_save(self, *args):
        self.dark_mode_enabled = self.dark_checkbox.active
        self.font_scale = 1.5 if self.font_checkbox.active else 1.0
        self.code_input.font_size = 16 * self.font_scale
        self.output_label.font_size = 14 * self.font_scale
        self.theme_cls.theme_style = "Dark" if self.dark_mode_enabled else "Light"
        self.dialog.dismiss()

XSharpIDEApp().run()