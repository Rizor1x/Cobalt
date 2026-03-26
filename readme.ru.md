<div align="center">
  <img src="https://github.com/Rizor1x/Crest/blob/main/crest_logo.png" alt="Crest Logo" width="100%"/>
  <h1>Crest Programming Language</h1>
  <p><b>Скорость Rust. Элегантность Python. Никакой боли с Borrow Checker.</b></p>

  [![Version](https://img.shields.io/badge/version-0.2.0_alpha-blue.svg)]()
  [![License](https://img.shields.io/badge/license-Apache%20License%202.0-blue.svg)](LICENSE)
  [![YouTube](https://img.shields.io/badge/YouTube-Devlog-red.svg)](https://www.youtube.com/@Rizor1x)
</div>

🇬🇧 [Read in English](https://github.com/Rizor1x/Crest/blob/main/readme.md)

---

## О проекте
**Crest** — это строго типизированный, компилируемый язык программирования следующего поколения. Под капотом Crest является **source-to-source транслятором**. Он берет ваш код на `.crs`, интеллектуально анализирует его и генерирует высокооптимизированный код на Rust.

## Дорожная карта

### `v0.1.0` — The Foundation (Фундамент)
- [x] **Lexer & Parser:** Создание EBNF грамматики и дерева (AST) на `Lark`.
- [x] **Code Gen:** Трансляция в базовый синтаксис Rust (переменные, `print`, типы `int/float/str/bool`).
- [x] **Build Pipeline:** Интеграция с компилятором `rustc` для автоматической сборки и запуска.

### `v0.2.0` — Logic & Flow (Логика и Потоки)
- [x] **Control Flow:** Условные операторы (`if / else`).
- [x] **Loops:** Реализация циклов (`for .. in`, `while`).
- [x] **Functions:** Объявление `fn`, вызовы функций, аргументы и `return`.
- [x] **Operators:** Полный набор арифметических и логических (`and`, `or`) операций.

### `v0.3.0` — Data Structures (Структуры данных)
- [ ] **Arrays & Lists:** Создание списков `[1, 2, 3]`, индексация `arr[0]` и трансляция в `Vec<T>`.
- [ ] **Dictionaries:** Базовая поддержка пар ключ-значение (трансляция в `HashMap`).
- [ ] **String Manipulation:** Встроенные методы для строк (конкатенация, интерполяция).

### `v0.4.0` — Architecture & OOP (Архитектура и ООП)
- [ ] **Object Model:** Реализация `class` с прозрачной авто-генерацией `struct` и `impl` в Rust.
- [ ] **Methods & `self`:** Вызов методов через точку (`obj.method()`) и мутация состояния.
- [ ] **Traits (Interfaces):** Поддержка интерфейсов для реализации полиморфизма.

### `v0.5.0` — Safety & Error Handling (Безопасность)
- [ ] **Error Handling:** Типизированная система ошибок `Result[T, E]` и оператор раннего возврата `?`.
- [ ] **Option Type:** Избавление от Null-Reference Exception через тип `Option` (Some/None).
- [ ] **Memory Management:** "Умный" генератор, который автоматически расставляет `.clone()`, скрывая от пользователя боль `Borrow Checker`.

### `v0.6.0` — Ecosystem & CLI (Экосистема)
- [ ] **Modularity:** Система импортов `use ./module.crs` и разделение на файлы.
- [ ] **CLI Tool:** Полноценное приложение `crest` (команды `init`, `run`, `build`).
- [ ] **Package System:** Базовое управление зависимостями.

### `v0.7.0` — System Level (Подготовка к созданию ОС)
- [ ] **Bare Metal:** Флаг `[no_std]` для отключения стандартной библиотеки Rust.
- [ ] **Unsafe Memory:** Блоки `unsafe { ... }` для прямой работы с указателями и железом.
- [ ] **FFI (C-Interop):** Ключевое слово `extern` для вызова драйверов на C/Rust.

### `v1.0.0` — Self-Hosting (Стабильный релиз)
- [ ] **Standard Library:** Написание библиотеки (`std::io`, `std::fs`) на самом Crest.
- [ ] **Compiler Rewrite:** Переписывание всего компилятора с Python на Crest.
- [ ] **Stable API:** Финальная полировка и выпуск релиз-кандидата.

## Пример кода
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

## Сообщество
Язык разрабатывается публично.

- [YouTube](https://www.youtube.com/@Rizor1x) - следите за процессом разработки.
- [Issues](https://github.com/Rizor1x/Crest/issues) - предлагайте фичи.

Поставьте ⭐️ этому репозиторию, если ждете релиза!

---

**Built with ❤️ by Rizor1x**
