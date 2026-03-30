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
### `v0.1.0` — The Foundation
- [x] **Lexer & Parser:** Generates EBNF grammars and tree (AST) using `Lark`.
- [x] **Code Gen:** Translates to basic Rust syntax (variables, `print`, `int/float/str/bool` types).
- [x] **Build Pipeline:** Integration with the `rustc` compiler for automatic building and running.

### `v0.2.0` — Logic & Flow
- [x] **Control Flow:** Conditional statements (`if / else`).
- [x] **Loops:** Implements loops (`for .. in`, `while`).
- [x] **Functions:** `fn` declaration, function calls, arguments, and `return`.
- [x] **Operators:** A full set of arithmetic and logical (`and`, `or`) operations.

### `v0.3.0` — Data Structures
- [x] **Arrays & Lists:** Creation of `[1, 2, 3]` lists, indexing with `arr[0]`, and casting to `Vec<T>`.
- [x] **Dictionaries:** Basic support for key-value pairs (casting to `HashMap`).
- [ ] **String Manipulation:** Built-in string methods (concatenation, interpolation).

### `v0.4.0` — Architecture & OOP
- [x] **Object Model:** `class` implementation with transparent auto-generation of `struct` and `impl` in Rust.
- [ ] **Methods & `self`:** Dotted method invocation (`obj.method()`) and state mutation.
- [ ] **Traits (Interfaces):** Interface support for implementing polymorphism.

### `v0.5.0` — Safety & Error Handling
- [ ] **Error Handling:** Typed `Result[T, E]` error system and `?` early return operator.
- [ ] **Option Type:** Null-Reference Exception avoidance via the `Option` type (Some/None).
- [ ] **Memory Management:** A "smart" generator that automatically places `.clone()`, hiding the pain of `Borrow Checker` from the user.

### `v0.6.0` — Ecosystem & CLI (Ecosystem)
- [ ] **Modularity:** The `use ./module.crs` import system and file separation.
- [x] **CLI Tool:** A full-fledged `crest` application (`init`, `run`, `build` commands).
- [ ] **Package System:** Basic dependency management.

### `v0.7.0` — System Level (Preparing for OS creation)
- [ ] **Bare Metal:** The `[no_std]` flag to disable the Rust standard library.
- [ ] **Unsafe Memory:** `unsafe { ... }` blocks for directly working with pointers and hardware.
- [ ] **FFI (C-Interop):** The `extern` keyword for calling C/Rust drivers.

### `v1.0.0` — Self-Hosting (Stable Release)
- [ ] **Standard Library:** Writing a library (`std::io`, `std::fs`) on Crest itself.
- [ ] **Compiler Rewrite:** Rewriting the entire compiler from Python to Crest.
- [ ] **Stable API:** Final polishing and release candidate.

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

## Community

The language is developed in public.

- [YouTube](https://www.youtube.com/@Rizor1x) - follow the dev process.

- [Issues](https://github.com/Rizor1x/Crest/issues) - suggest new features.

Put ⭐️ to this repository if you are waiting for a release!

---

**Built with ❤️ by Rizor1x**
