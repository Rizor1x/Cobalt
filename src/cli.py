import sys
import os
import subprocess
from parser import parse_code

from generator import RustGen

def main():
    if len(sys.argv) < 2:
        print("Использование: python cli.py <путь_к_файлу.crs>")
        return
    
    file_path = sys.argv[1]
    
    if not os.path.exists(file_path):
        print(f"Ошибка: файл '{file_path}' не найден.")
        return
    
    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()

    try:
        ast_tree = parse_code(code)

        rust_generator = RustGen()
        rust_code = rust_generator.transform(ast_tree) 

        file_dir = os.path.dirname(file_path)
        base_name = os.path.splitext(os.path.basename(file_path))[0]

        build_dir = os.path.join(file_dir, ".crest_temp")
        os.makedirs(build_dir, exist_ok=True)

        rs_file_path = os.path.join(build_dir, f"{base_name}.rs")

        exe_ext = ""

        exe_file_path = os.path.join(build_dir, f"{base_name}{exe_ext}")

        with open(rs_file_path, "w", encoding="utf-8") as f:
            f.write(rust_code)

        compile_process = subprocess.run(["rustc", rs_file_path, "-o", exe_file_path], capture_output=True, text=True)

        if compile_process.returncode != 0:
            print(compile_process.stderr)
            return
        
        subprocess.run([exe_file_path])

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
    