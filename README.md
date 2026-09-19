#​ MultiCode

**MultiCode** es un proyecto de Python que comenzó con una idea simple:

> *"¿Y si hago un programa que convierta texto entre diferentes formatos de codificación?"* 🤔

Y bueno... terminó creciendo más de lo esperado. 😂

MultiCode es un conjunto de herramientas de línea de comandos para codificar y decodificar texto usando diferentes formatos como **ASCII, Binario, Hexadecimal, Unicode y Base64**.

El proyecto se está desarrollando actualmente con una arquitectura más modular y escalable, lo que hace que sea más fácil agregar nuevas funciones sin convertir la base de código en un desastre.

> 🚧 **Status:** Active development

---

## ⚡ ¿Qué puede hacer MultiCode?

Actualmente, MultiCode soporta:

* 🔤 **ASCII** — Encode and decode text
* 🔢 **Binary** — Convert text to binary and back
* 🔷 **Hexadecimal** — Encode and decode hexadecimal
* 🌐 **Unicode** — Work with Unicode representations
* 🔐 **Base64** — Encode and decode Base64
* 📋 **Clipboard support** — Copia resultados directamente
* 🖥️ **Terminal interface** —Todo se ejecuta desde la CLI
* 🧩 **Modular architecture** — Cada componente tiene su propio trabajo

Y hay un par de experimentos en trabajo:

* 🔎 **Detector de Lenguaje** — *In development*
* 🤖 **Chatbot** — *In development*

---

## Preview:

<img width="1107" height="500" alt="MultiCode terminal interface" src="https://github.com/user-attachments/assets/f8fbc90f-4247-4491-a15d-3e3e5ed78eff" />

---

## 🏗️ Estructura del proyecto:

Uno de los mayores cambios en esta versión fue pasar de un enfoque de programa único a una estructura de paquetes más organizada.
```
MultiCode/
│
├── src/
│   └── multicode/
│       ├── codecs/
│       ├── cli/
│       ├── core/
│       └── ...
│
├── tests/
├── main.py
├── pyproject.toml
└── README.md
```

La idea es simple:

**Cada parte de MultiCode debería tener su propio lugar**
---

## 🛠️ Constrido con:

* 🐍 Python 3.10+
* 📋 Pyperclip
* 🧠 Standard Python libraries
* 💻 A suspicious amount of terminal usage

---

## 🚀 Arrancando:

### 1. Clone the repository

```bash
git clone https://github.com/MMLabsDev/Multicode-system
```

### 2. Enter the project

```bash
cd Multicode-system
```

### 3. Install it in editable mode

```bash
pip install -e .
```

### 4. Run MultiCode

```bash
python main.py
```

Y eso es todo

Bienvenido a Multicode
---

## 🧪 ¿Por qué hice esto?

MultiCode comenzó como un pequeño proyecto en Python mientras aprendía a programar.
Al inicio, la meta era básicamente:

**"Quiero entender cómo funciona la codificación y hacer algo genial con ello"**

Pero a medida que aprendía más sobre Python, el proyecto comenzó a convertirse en un lugar para experimentar con:

* Modular Programmig
* Python packages
* Command-line interfaces
* String manipulation
* Encoding systems
* Testing
* Project architecture
* Dependency management
* Git and GitHub

Así que MultiCode ya no se trata solo de convertir texto.

También es mi pequeño laboratorio para aprender cómo se construye el software real🐍
---

## 🗺️ Ruta

Cosas que me gustaría añadir o mejorar:

* [ ] `multicode` terminal command
* [ ] Better language detection
* [ ] More encoding formats
* [ ] More advanced chatbot
* [ ] Better CLI experience
* [ ] More automated tests
* [ ] Better documentation
* [ ] More modular tools
* [ ] Keep cleaning up the code

Esta ruta puede cambiar a medida que el proyecto evoluciona. Eso es parte de la diversión.
---

## ☕ Hecho por MMLabs

MultiCode se desarrolla como parte de **MMLabs**, mi espacio personal para crear proyectos en Python y experimentar con el desarrollo de software.
Hecho con Python, curiosidad, muchas sesiones de terminal, y probablemente más café del necesario☕🐍

---

## 📄 License

MultiCode is licensed under the **MIT License**.
