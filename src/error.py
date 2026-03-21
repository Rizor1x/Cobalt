class CrestError(Exception):
    def __init__(self, message, token, code, file_path, help_msg=""):
        self.message = message
        self.token = token
        self.code = code
        self.file_path = file_path
        self.help_msg = help_msg

    def __str__(self):
        line_no = self.token.line
        col_no = self.token.column
        length = len(self.token.value)

        lines = self.code.split('\n')
        error_line = lines[line_no - 1]

        RED = "\033[91m"
        BLUE = "\033[96m"
        RESET = "\033[0m"

        out = []
        out.append(f"{RED}error{RESET}: {self.message}")
        out.append(f"  --> {self.file_path}:{line_no}:{col_no}")
        out.append(f"   |")
        out.append(f"{line_no:2} | {error_line}")
        out.append(f"   | " + " " * (col_no - 1) + f"{RED}" + "^" * length + f"{RESET}")
        
        if self.help_msg:
            out.append(f"   |")
            out.append(f"   = {BLUE}help{RESET}: {self.help_msg}")
            
        return "\n".join(out)