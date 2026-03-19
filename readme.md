<div align="center">
  <img src="cobalt_logo.png" alt="Cobalt Logo" width="100%"/>
  <h1>Cobalt Programming Language</h1>
  <p><b>Скорость Rust. Элегантность Python. Никакой боли с Borrow Checker.</b></p>

  [![Version](https://img.shields.io/badge/version-0.1.0_alpha-blue.svg)]()
  [![License](https://img.shields.io/badge/license-Apache-green.svg)](LICENSE)
  [![YouTube](https://img.shields.io/badge/YouTube-Devlog-red.svg)](ТВОЯ_ССЫЛКА_НА_КАНАЛ)
</div>

---

## 🚀 Что такое Cobalt?
**Cobalt** — это строго типизированный, компилируемый язык программирования следующего поколения. 
Он создается для тех, кто любит минималистичный и читаемый синтаксис (как в Python), но нуждается в бескомпромиссной производительности и безопасности (как в Rust или C++).

Под капотом Cobalt является **source-to-source транслятором (transpiler)**. Он берет ваш красивый код на `.co`, интеллектуально анализирует его и генерирует высокооптимизированный код на Rust, который затем компилируется в бинарник.

### 🔥 Философия языка:
1. **Developer Experience (DX) на первом месте:** Никаких точек с запятой, сложного управления временем жизни (lifetimes) и визуального шума.
2. **Нулевой оверхед:** Вы получаете скорость C/Rust без использования тяжелого Garbage Collector'а.
3. **Web-Native:** Встроенная поддержка создания API и компиляции в WebAssembly (в разработке).

---

## 💡 Как выглядит код? (Концепт)

Забудьте про ручное разделение на `struct` и `impl` или мучения с макросами. Пишите логику:

```Cobalt
use std::io
use std::fs::File

// Все данные и методы в одном понятном блоке
class Task {
    val id: int
    val title: string
    var is_done: bool = false

    // Метод, изменяющий состояние
    fn complete(var self) {
        self.is_done = true
    }
}

fn main() {
    var tasks =[
        Task(1, "Создать лексер"),
        Task(2, "Написать парсер")
    ]

    for task in tasks {
        if not task.is_done {
            print("В процессе: {task.title}")
        }
    }
}
```

🗺️ Дорожная карта (Roadmap)

Проект находится на стадии зарождения. Весь процесс создания языка я документирую на своем YouTube-канале!

    v0.1 (Bootstrap): Базовый транслятор на Python (Лексер, Парсер, AST).

    v0.2: Классы, ООП и умный анализатор для автогенерации кода Rust (избавление от боли с Borrow Checker).

    v0.3: Web-Native фичи (создание бекенда одним словом api fn).

    v1.0 (Self-Hosting): Переписывание компилятора Cobalt на самом Cobalt! 🚀

🤝 Как поучаствовать?

Язык разрабатывается публично. Если у вас есть идеи по синтаксису, фичам или вы хотите помочь с парсером на Python — открывайте Issues или присылайте Pull Requests!

    Подпишитесь на YouTube-канал, чтобы следить за архитектурными решениями.

    Поставьте ⭐️ этому репозиторию, если ждете релиза!

Built with ❤️ for developers who value their time.