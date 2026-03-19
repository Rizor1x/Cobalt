<div align="center">
  <img src="https://raw.githubusercontent.com/Rizor1x/Cobalt/blob/main/cobalt_logo.png" alt="Cobalt Logo" width="100%"/>
  <h1>Cobalt Programming Language</h1>
  <p><b>Rust's speed. Python's elegance. No more Borrow Checker pain.</b></p>

  [![Version](https://img.shields.io/badge/version-0.1.0_alpha-blue.svg)]()
  [![License](https://img.shields.io/badge/license-Apache-green.svg)](LICENSE)
  [![YouTube](https://img.shields.io/badge/YouTube-Devlog-red.svg)](https://www.youtube.com/@Rizor1x)
</div>

🇷🇺 [Read in Russian](README.ru.md)

---

## 🚀 About
**Cobalt** is a statically typed, compiled programming language of the next generation. Under the hood, Cobalt is a **source-to-source transpiler**. It takes your `.co` code, intelligently analyzes it, and generates highly optimized Rust code.

## 🗺️ Roadmap
#### `v0.1.0` — The Foundation
- [ ] **Lexer & Parser:** Creating grammar and tree (AST) on `Lark`.
- [ ] **AST & IR:** Designing an intermediate representation of the code.
- [ ] **Code Gen:** Translation into the basic syntax of Rust (variables, `print`, types).
- [ ] **Build Pipeline:** Direct integration with `cargo` for automatic binary file assembly.

#### `v0.2.0` — Logic & Flow
- [ ] **Control Flow:** Conditional operators (`if / else`).
- [ ] **Loops:** Implementing cycles (`for`, `while`).
- [ ] **Functions:** Functions with arguments and return values.
- [ ] **Operators:** A full set of arithmetic and logical operations.

#### `v0.3.0` — Data & Safety
- [ ] **Object Model:** Implementing `class` with auto-generation of `struct` and `impl` in Rust.
- [ ] **Memory Safety:** Smart auto-referencing and `.clone()` management (getting rid of Borrow Checker pain).
- [ ] **Error Handling:** Safe error handling via `Result` and the `?` operator.

#### `v0.4.0` — Developer Experience (CLI)
- [ ] **CLI Tool:** Creating a `cobalt` command (analogous to `cargo` or `go`).
- [ ] **Project Management:** Implementing `cobalt init` and `cobalt run file.co`.
- [ ] **Package System:** Basic module and dependency management.

#### `v1.0.0` — Self-Hosting (Stable)
- [ ] **Standard Library:** Writing a basic standard library in Cobalt.
- [ ] **Compiler Rewrite:** Rewriting the compiler from Python to Cobalt itself.
- [ ] **Final Polish:** API stabilization, testing, and preparation for the first stable release.

## 💡 Code Example
```Cobalt
class Task {
    val id: int
    val title: string
    var is_done: bool = false

    fn complete(var self) {
        self.is_done = true
    }
}

fn main() {
    var tasks = [Task(1, "Build lexer"), Task(2, "Build parser")]
    for task in tasks {
        if not task.is_done {
            print("Processing: {task.title}")
        }
    }
}
```

---

## 🤝 Community / Сообщество

The language is developed in public.

**YouTube** — follow the dev process.

**Issues** — suggest new features.

Put ⭐️ to this repository if you are waiting for a release!
**Built with ❤️ by Rizor1x**