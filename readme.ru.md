<div align="center">
  <img src="https://raw.githubusercontent.com/Rizor1x/Cobalt/main/cobalt_logo.png" alt="Cobalt Logo" width="100%"/>
  <h1>Cobalt Programming Language</h1>
  <p><b>Скорость Rust. Элегантность Python. Никакой боли с Borrow Checker.</b></p>

  [![Version](https://img.shields.io/badge/version-0.1.0_alpha-blue.svg)]()
  [![License](https://img.shields.io/badge/license-Apache-green.svg)](LICENSE)
  [![YouTube](https://img.shields.io/badge/YouTube-Devlog-red.svg)](https://www.youtube.com/@Rizor1x)
</div>

🇬🇧 [Read in English](README.md)

---

## 🚀 О проекте
**Cobalt** — это строго типизированный, компилируемый язык программирования следующего поколения. Под капотом Cobalt является **source-to-source транслятором**. Он берет ваш код на `.co`, интеллектуально анализирует его и генерирует высокооптимизированный код на Rust.

## 🗺️ Дорожная карта

#### `v0.1.0` — Фундамент
- [ ] **Лексер и Парсер:** Создание грамматики и дерева (AST) на `Lark`.
- [ ] **AST и IR:** Проектирование промежуточного представления кода.
- [ ] **Генерация кода:** Трансляция в базовый синтаксис Rust (переменные, `print`, типы).
- [ ] **Сборка:** Прямая интеграция с `cargo` для автоматической сборки бинарных файлов.

#### `v0.2.0` — Логика и Потоки
- [ ] **Условия:** Условные операторы (`if / else`).
- [ ] **Циклы:** Реализация циклов (`for`, `while`).
- [ ] **Функции:** Функции с аргументами и возвратом значений.
- [ ] **Операторы:** Полный набор арифметических и логических операций.

#### `v0.3.0` — Структуры и Безопасность
- [ ] **Объекты:** Реализация `class` с авто-генерацией `struct` и `impl` в Rust.
- [ ] **Безопасность памяти:** Умная авто-расстановка ссылок и `.clone()`.
- [ ] **Обработка ошибок:** Безопасная обработка через `Result` и оператор `?`.

#### `v0.4.0` — CLI и инструменты
- [ ] **CLI Tool:** Создание команды `cobalt`.
- [ ] **Управление проектами:** Реализация `cobalt init` и `cobalt run file.co`.
- [ ] **Система пакетов:** Базовое управление модулями и зависимостями.

#### `v1.0.0` — Стабильный релиз (Self-Hosting)
- [ ] **Стандартная библиотека:** Написание базовой библиотеки на Cobalt.
- [ ] **Переписывание компилятора:** Переписывание компилятора с Python на самом Cobalt.
- [ ] **Финальная полировка:** Стабилизация API, покрытие тестами и подготовка к релизу.

## 💡 Пример кода
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

## 🤝 Сообщество
Язык разрабатывается публично.
- [YouTube](https://www.youtube.com/@Rizor1x) — следите за процессом разработки.
- [Issues](https://github.com/Rizor1x/Cobalt/issues) — предлагайте фичи.

Поставьте ⭐️ этому репозиторию, если ждете релиза!
**Built with ❤️ by Rizor1x**