<div align="center">
  <img src="https://github.com/Rizor1x/Crest/blob/main/crest_logo.png" alt="Crest Logo" width="100%"/>
  <h1>Crest Programming Language</h1>
  <p><b>Rust's speed. Python's elegance. No more Borrow Checker pain.</b></p>

  [![Version](https://img.shields.io/badge/version-0.2.0_alpha-blue.svg)]()
  [![License](https://img.shields.io/badge/license-Apache%20License%202.0-blue.svg)](LICENSE)
  [![YouTube](https://img.shields.io/badge/YouTube-Devlog-red.svg)](https://www.youtube.com/@Rizor1x)
</div>

🇷🇺 [Read in Russian](https://github.com/Rizor1x/Crest/blob/main/readme.ru.md)

---

## About
**Crest** is a statically typed, compiled programming language of the next generation. Under the hood, Crest is a **source-to-source transpiler**. It takes your `.crs` code, intelligently analyzes it, and generates highly optimized Rust code.

## Roadmap
#### `v0.1.0` — The Foundation
- [x] **Lexer & Parser:** Creating grammar and tree (AST) on `Lark`.
- [x] **AST & IR:** Designing an intermediate representation of the code.
- [x] **Code Gen:** Translation into the basic syntax of Rust (variables, `print`, types).
- [x] **Build Pipeline:** Direct integration with `cargo` for automatic binary file assembly.

#### `v0.2.0` — Logic & Flow
- [x] **Control Flow:** Conditional operators (`if / else`).
- [ ] **Loops:** Implementing cycles (`for`, `while`).
- [ ] **Functions:** Functions with arguments and return values.
- [ ] **Operators:** A full set of arithmetic and logical operations.

#### `v0.3.0` — Data & Safety
- [ ] **Object Model:** Implementing `class` with auto-generation of `struct` and `impl` in Rust.
- [ ] **Memory Safety:** Smart auto-referencing and `.clone()` management (getting rid of Borrow Checker pain).
- [ ] **Error Handling:** Safe error handling via `Result` and the `?` operator.

#### `v0.4.0` — Developer Experience (CLI)
- [ ] **CLI Tool:** Creating a `crest` command (analogous to `cargo` or `go`).
- [ ] **Project Management:** Implementing `crest init` and `crest run file.co`.
- [ ] **Package System:** Basic module and dependency management.

#### `v1.0.0` — Self-Hosting (Stable)
- [ ] **Standard Library:** Writing a basic standard library in Crest.
- [ ] **Compiler Rewrite:** Rewriting the compiler from Python to Crest itself.
- [ ] **Final Polish:** API stabilization, testing, and preparation for the first stable release.

## Code Example
```Crest
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

## Community / Сообщество

The language is developed in public.

- [YouTube](https://www.youtube.com/@Rizor1x) - follow the dev process.

- [Issues](https://github.com/Rizor1x/Crest/issues) - suggest new features.

Put ⭐️ to this repository if you are waiting for a release!

---

**Built with ❤️ by Rizor1x**
