<div align="center">
  <img src="./cobalt_logo.png" alt="Cobalt Logo" width="100%"/>
  <h1>Cobalt Programming Language</h1>
  <p><b>Скорость Rust. Элегантность Python. Никакой боли с Borrow Checker.</b></p>
  <p><b>Rust's speed. Python's elegance. No more Borrow Checker pain.</b></p>

  [![Version](https://img.shields.io/badge/version-0.1.0_alpha-blue.svg)]()
  [![License](https://img.shields.io/badge/license-Apache-green.svg)](LICENSE)
  [![YouTube](https://img.shields.io/badge/YouTube-Devlog-red.svg)](https://www.youtube.com/@Rizor1x)
</div>

---

## 🚀 About / О проекте

**Cobalt** — это строго типизированный, компилируемый язык программирования следующего поколения.
**Cobalt** is a statically typed, compiled programming language of the next generation.

Под капотом Cobalt является **source-to-source транслятором**. Он берет ваш код на `.co`, интеллектуально анализирует его и генерирует высокооптимизированный код на Rust.
Under the hood, Cobalt is a **source-to-source transpiler**. It takes your `.co` code, intelligently analyzes it, and generates highly optimized Rust code.

---

## 🗺️ Roadmap / Дорожная карта

#### `v0.1.0` — The Foundation (Фундамент)
- [ ] **Lexer & Parser:** Создание грамматики и дерева (AST) на `Lark`.
- [ ] **AST & IR:** Проектирование промежуточного представления кода.
- [ ] **Code Gen:** Трансляция в базовый синтаксис Rust (переменные, `print`, типы).
- [ ] **Build Pipeline:** Прямая интеграция с `cargo` для автоматической сборки бинарных файлов.

#### `v0.2.0` — Logic & Flow (Логика и Потоки)
- [ ] **Control Flow:** Условные операторы (`if / else`).
- [ ] **Loops:** Реализация циклов (`for`, `while`).
- [ ] **Functions:** Функции с аргументами и возвратом значений.
- [ ] **Operators:** Полный набор арифметических и логических операций.

#### `v0.3.0` — Data & Safety (Структуры и Безопасность)
- [ ] **Object Model:** Реализация `class` с авто-генерацией `struct` и `impl` в Rust.
- [ ] **Memory Safety:** Умная авто-расстановка ссылок и `.clone()` (избавление от боли с Borrow Checker).
- [ ] **Error Handling:** Безопасная обработка ошибок через `Result` и оператор `?`.

#### `v0.4.0` — Developer Experience (CLI & Tooling)
- [ ] **CLI Tool:** Создание команды `cobalt` (аналог `cargo` или `go`).
- [ ] **Project Management:** Реализация `cobalt init` для создания проектов и `cobalt run file.co` для быстрого запуска.
- [ ] **Package System:** Базовое управление модулями и зависимостями.

#### `v1.0.0` — Self-Hosting (Стабильный релиз)
- [ ] **Standard Library:** Написание базовой стандартной библиотеки на Cobalt.
- [ ] **Compiler Rewrite:** Переписывание компилятора с Python на самом Cobalt.
- [ ] **Final Polish:** Стабилизация API, покрытие тестами и подготовка к первому стабильному релизу.

---

## 💡 Code Example / Пример кода

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

## 🤝 Community / Сообщество

Язык разрабатывается публично.
The language is developed in public.

**YouTube** — следите за процессом разработки / follow the dev process.

**Issues** — предлагайте фичи / suggest new features.

Поставьте ⭐️ этому репозиторию, если ждете релиза!

**Built with ❤️ by Rizor1x**