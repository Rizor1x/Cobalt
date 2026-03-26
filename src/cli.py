import sys
import os
import subprocess
from .parser import parse_code
from .generator import RustGen
from .error import CrestError

def build_and_run(file_path, run_after_build=True):
    if not os.path.exists(file_path):
        print(f"❌ Ошибка: файл '{file_path}' не найден.")
        return
    
    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()

    try:
        ast_tree = parse_code(code)
        rust_generator = RustGen(code, file_path)
        rust_code = rust_generator.transform(ast_tree) 

        file_dir = os.path.dirname(file_path)
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        build_dir = os.path.join(file_dir, ".crest_temp")
        os.makedirs(build_dir, exist_ok=True)

        rs_file_path = os.path.join(build_dir, f"{base_name}.rs")
        exe_file_path = os.path.join(build_dir, f"{base_name}")

        with open(rs_file_path, "w", encoding="utf-8") as f:
            f.write(rust_code)

        compile_process = subprocess.run(["rustc", rs_file_path, "-o", exe_file_path], capture_output=True, text=True)

        if compile_process.returncode != 0:
            print("❌ Ошибка компиляции Rust:")
            print(compile_process.stderr)
            return
        
        if run_after_build:
            subprocess.run([exe_file_path])
        else:
            print(f"✅ Успешно скомпилировано: {exe_file_path}")

    except CrestError as e:
        print(e)
    except Exception as e:
        print(f"Системная ошибка: {e}")

def main():
    # Если пользователь написал просто `crest`
    if len(sys.argv) < 2:
        print("\033[31m Crest Programming Language v0.3.0 \033[0m")
        print("Использование:")
        print("  crest run <файл.crs>   - Скомпилировать и запустить")
        print("  crest build <файл.crs> - Только скомпилировать")
        return

    command = sys.argv[1]

    if command == "run":
        if len(sys.argv) < 3:
            print("❌ Укажите файл: crest run <файл.crs>")
            return
        build_and_run(sys.argv[2], run_after_build=True)
        
    elif command == "build":
        if len(sys.argv) < 3:
            print("❌ Укажите файл: crest build <файл.crs>")
            return
        build_and_run(sys.argv[2], run_after_build=False)
        
    else:
        print(f"❌ Неизвестная команда: '{command}'")

if __name__ == "__main__":
    main()