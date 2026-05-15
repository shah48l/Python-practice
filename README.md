# 🐍 Python Interview Prep

A hands-on collection of **Design Patterns**, **SOLID Principles**, **Python Core Concepts**, and **Daily Practice Problems** — built for interview preparation and quick revision.

---

## 📁 Repository Structure

```
├── design_pattern/        # Classic GoF design patterns in Python
├── design_principles/     # SOLID principles with examples
├── Python_core/           # Core Python concepts & daily problems
│   ├── day-1/             # Lists, strings, dicts, file I/O
│   ├── day-2/             # *args, **kwargs, map/filter, closures
│   ├── day-3/OOPS/        # OOP fundamentals — classes, inheritance, polymorphism
│   └── day-4/             # Abstract classes, dunder methods, properties, MRO
└── sqlalchemy/            # SQLAlchemy ORM basics
```

---

## 🏗️ Design Patterns

| File | Pattern | Description |
|------|---------|-------------|
| [design_pattern/STP.py](design_pattern/STP.py) | **Singleton** | Three implementations — `__new__`, thread-safe with `Lock`, and decorator-based |
| [design_pattern/FTP.py](design_pattern/FTP.py) | **Factory** | `PaymentFactory` with a registry to create payment objects from a string key |
| [design_pattern/BP.py](design_pattern/BP.py) | **Builder** | Step-by-step `User` construction with method chaining (`.set_name().set_email().build()`) |
| [design_pattern/AP.py](design_pattern/AP.py) | **Adapter** | Wraps `VLCPlayer`/`MP4Player` behind a common `MediaPlayer` interface |
| [design_pattern/DP.py](design_pattern/DP.py) | **Decorator** | Coffee shop example — dynamically adds cost/description via `MilkDecorator`, `SugarDecorator` |

---

## 📐 Design Principles

| File | Principle | Description |
|------|-----------|-------------|
| [design_principles/LSP.py](design_principles/LSP.py) | **Liskov Substitution** | Shows the violation (`Penguin.fly()` raises exception) and the fix using separate `Bird`/`FlyingBird` hierarchies |

---

## 🧠 Python Core Concepts

| File | Topic | Description |
|------|-------|-------------|
| [Python_core/closure.py](Python_core/closure.py) | **Closures** | Inner function capturing variables from the enclosing scope |
| [Python_core/dict.py](Python_core/dict.py) | **Dictionaries** | Iterating over nested dictionaries |
| [Python_core/encasulation.py](Python_core/encasulation.py) | **Encapsulation** | Name mangling, `@property` getter/setter with validation |
| [Python_core/iterators.py](Python_core/iterators.py) | **Iterators** | `iter()` / `next()` protocol |
| [Python_core/lambda.py](Python_core/lambda.py) | **Lambdas** | Lambda basics, `map()` with lambda, storing lambdas in collections |
| [Python_core/Python.py](Python_core/Python.py) | **Collections** | `analyze_collection()` utility, recursive `flatten_and_filter()`, list comprehension |

---

## 📝 Daily Practice Problems

### Day 1 — Lists, Strings & Dicts

| # | Problem | Key Concept |
|---|---------|-------------|
| 1 | [Filter even numbers](Python_core/day-1/problem-1.py) | List comprehension |
| 2 | [Character frequency](Python_core/day-1/problem-2.py) | `dict.get()` |
| 3 | [List union](Python_core/day-1/problem-3.py) | Sets |
| 4 | [Read file safely](Python_core/day-1/problem-4.py) | File I/O, `try/except` |
| 5 | [Reverse string in-place](Python_core/day-1/problem-5.py) | Two pointers |
| 6 | [Palindrome check](Python_core/day-1/problem-6.py) | Two pointers, case-insensitive |
| 7 | [Remove duplicates (preserve order)](Python_core/day-1/problem_7.py) | Seen-list technique |
| 8 | [Most frequent word](Python_core/day-1/problem-8.py) | `max()` with lambda key |

### Day 2 — Functions, Lambdas & Closures

| # | Problem | Key Concept |
|---|---------|-------------|
| 1 | [Variadic sum](Python_core/day-2/problem-1.py) | `*args` |
| 2 | [Print keyword args](Python_core/day-2/problem-2.py) | `**kwargs` |
| 3 | [Merge dictionaries](Python_core/day-2/problem-3.py) | `*args` with `dict.update()` |
| 4 | [Square elements](Python_core/day-2/problem-4.py) | `map()` + lambda |
| 5 | [Filter long words](Python_core/day-2/problem-5.py) | `filter()` + lambda |
| 6 | [Custom max](Python_core/day-2/problem-6.py) | Lambda with ternary |
| 7 | [Multiplier factory](Python_core/day-2/problem-7.py) | Closures |
| 8 | [Counter with state](Python_core/day-2/problem-8.py) | `nonlocal` |
| 9 | [Greeting builder](Python_core/day-2/problem-9.py) | Closures |

### Day 3 — OOP Fundamentals

| # | Problem | Key Concept |
|---|---------|-------------|
| 1 | [BankAccount class](Python_core/day-3/OOPS/problem-1.py) | Classes, methods, `__str__` |
| 2 | [Student class](Python_core/day-3/OOPS/problem-2.py) | Class variables, `promote()` |
| 3 | [Rectangle class](Python_core/day-3/OOPS/problem-3.py) | `area()`, `perimeter()`, `is_square()` |
| 4 | [Animal / Dog inheritance](Python_core/day-3/OOPS/problem-4.py) | Inheritance, method overriding |
| 5 | [Shape / Circle inheritance](Python_core/day-3/OOPS/problem-5.py) | Polymorphism, `area()` via subclass |
| 6 | [Employee / Manager inheritance](Python_core/day-3/OOPS/problem-6.py) | `super()`, method overriding |

### Day 4 — Advanced OOP

| # | Problem | Key Concept |
|---|---------|-------------|
| — | [Abstract classes + Polymorphism](Python_core/day-4/Abstract-class.py) | ABC, `@abstractmethod`, concrete method in abstract class |
| 1 | [Dunder methods (BankAccount)](Python_core/day-4/problem-1.py) | `__str__`, `__repr__`, `__add__`, `__eq__`, `__len__` |
| 2 | [Employee class methods](Python_core/day-4/problem-2.py) | `@classmethod` (`from_string`), `@staticmethod` (`is_valid_salary`) |
| 3 | [Circle with properties](Python_core/day-4/problem-3.py) | `@property`, getter/setter, validation, read-only properties |
| 4 | [Vehicle hierarchy](Python_core/day-4/problem-4.py) | Inheritance, `super()`, MRO, name mangling (`__engine`) |

---

## 🗄️ SQLAlchemy

| File | Description |
|------|-------------|
| [sqlalchemy/books_app.py](sqlalchemy/books_app.py) | ORM basics — define a `Book` model, create a SQLite DB, perform CRUD operations using `sessionmaker` |

---

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/shah48l/Python-practice.git
cd Python-practice

# (Optional) Create a virtual environment
python -m venv .venv
.venv\Scripts\activate   # Windows

# Run any file
python design_pattern/STP.py
python Python_core/day-1/problem-1.py
```

---

## 🤝 Contributing

Found a bug or want to add more patterns/problems? Feel free to open a PR or raise an issue.

## 📄 License

This project is open-source and available for personal and educational use.
