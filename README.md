# Serpent Cipher Web Application

This project is a web-based implementation of a custom symmetric block cipher, the "Serpent Cipher." Built with Python and the Flask framework, it provides an interactive and user-friendly interface for key generation, encryption, and decryption. The application is designed as an educational tool to demonstrate cryptographic principles with a unique and visually appealing "Teal and Orange Sunset" theme.



## 🔑 Key Features

-   **Custom Cipher Algorithm:** Implements a unique symmetric block cipher operating on 16-byte blocks with a 256-bit key.
-   **Single-Round Transformation:** Utilizes custom, efficient encryption steps for clarity and educational demonstration.
-   **Interactive Web Interface:** Allows users to easily generate keys, encrypt plaintext, and decrypt ciphertext through a web browser.
-   **Distinct Visual Design:** Features a "Teal and Orange Sunset" color scheme for a professional and unique user experience.
-   **Educational Tool:** Perfectly suited for demonstrating cryptographic principles in classrooms or workshops.

## ⚙️ The Serpent Cipher Algorithm

The Serpent Cipher is a custom symmetric block cipher with the following specifications:

-   **Key Size:** 256-bit (32 bytes).
-   **Block Size:** 16 bytes.
-   **Padding:** Uses PKCS#7 padding to ensure the plaintext is a multiple of the block size.
-   **Transformation (Encryption):** For each byte `Bi` in a block and corresponding key byte `Ki`, the transformation `Ci` is:
    1.  `T1 = Bi ⊕ Ki` (Bitwise XOR)
    2.  `T2 = (T1 + 7) mod 256` (Addition and Modulo)
    3.  `Ci = LeftRotate(T2, 2)` (Bitwise Left Rotation)
-   **Inverse Transformation (Decryption):** The operations are reversed to get the original byte `Bi` from a ciphertext byte `Ci`:
    1.  `T2 = RightRotate(Ci, 2)` (Bitwise Right Rotation)
    2.  `T1 = (T2 - 7) mod 256` (Subtraction and Modulo)
    3.  `Bi = T1 ⊕ Ki` (Bitwise XOR)
-   **Serialization:** Encrypted blocks are converted to a comma-separated hexadecimal string for easy display and transmission.

## 📁 Project Structure

The project follows a standard Flask application structure:

-   `app.py`: The main Flask file that handles routing, request handling, and integrates the cryptographic logic.
-   `cerpent.py`: A dedicated module containing the core cryptographic logic for the Serpent Cipher (key generation, padding, transformation, etc.).
-   `templates/`: Contains all Jinja2 HTML files (`base.html`, `home.html`, `index.html`, `decrypt.html`, `result.html`).
-   `static/`: Contains the `style.css` file, which defines the custom "Teal and Orange Sunset" theme and other styling rules.

## 🚀 How to Run Locally

Follow these steps to set up and run the project on your local machine.

### Prerequisites

-   Python 3.x
-   `pip` (Python package installer)

### Installation and Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/NoorMustafa4556/Serpent-Cipher-Flask-App-.git
    cd Serpent-Cipher-Flask-App-
    ```

2.  **Create and activate a virtual environment (Recommended):**
    ```bash
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required packages:**
    ```bash
    pip install Flask
    ```

4.  **Run the Flask application:**
    ```bash

# 👋 Hi, I'm Noor Mustafa

A passionate and results-driven **Flutter Developer** from **Bahawalpur, Pakistan**, specializing in building elegant, scalable, and high-performance cross-platform mobile applications using **Flutter** and **Dart**.

With a strong understanding of **UI/UX principles**, **state management**, and **API integration**, I aim to deliver apps that are not only functional but also user-centric and visually compelling. My development approach emphasizes clean code, reusability, and performance.

---

## 🚀 What I Do

- 🧑‍💻 **Flutter App Development** – I build cross-platform apps for Android, iOS, and the web using Flutter.
- 🔗 **API Integration** – I connect apps to powerful RESTful APIs and third-party services.
- 🎨 **UI/UX Design** – I craft responsive and animated interfaces that elevate the user experience.
- 🔐 **Authentication & Firebase** – I implement secure login systems and integrate Firebase services.
- ⚙️ **State Management** – I use Provider, setState, and Riverpod (in-progress) for scalable app architecture.
- 🧠 **Clean Architecture** – I follow MVVM and MVC patterns for maintainable code.

---


## 🌟 Projects I'm Proud Of

- 🌤️ **[Live Weather Check App](https://github.com/NoorMustafa4556/Live-Weather-Check-App)** – Real-time weather forecast using OpenWeatherMap API  
- 🤖 **[AI Chatbot (Gemini)](https://github.com/NoorMustafa4556/Ai-ChatBot)** – Conversational AI chatbot powered by Google’s Gemini  

- 🍔 **[Recipe App](https://github.com/NoorMustafa4556/Recipe-App)** – Discover recipes with images, categories, and step-by-step instructions  

- 📚 **[Palindrome Checker](https://github.com/NoorMustafa4556/Palindrome-Checker-App)** – A Theory of Automata-based project to identify palindromic strings  

> 🎯 Check out all my repositories on [github.com/NoorMustafa4556](https://github.com/NoorMustafa4556?tab=repositories)

---

## 🛠️ Tech Stack & Tools

| Area                | Tools/Technologies |
|---------------------|--------------------|
| **Languages**       | Dart, JavaScript, Python (basic) |
| **Mobile Framework**| Flutter            |
| **Backend/Cloud**   | Firebase (Auth, Realtime DB, Storage), Django, Flask |
| **Frontend (Web)**  | React.js (basic), HTML, CSS, Bootstrap |
| **State Management**| Provider, setState, Riverpod (learning) |
| **API & Storage**   | REST APIs, HTTP, Shared Preferences, SQLite |
| **Design**          | Material, Cupertino, Lottie Animations, Gradient UI |
| **Version Control** | Git, GitHub        |
| **Tools**           | Android Studio, VS Code, Postman, Figma (basic) |

---

## 🧰 Tech Toolbox

<p align="left">
  <img src="https://img.shields.io/badge/Dart-0175C2?style=for-the-badge&logo=dart&logoColor=white"/>
  <img src="https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=flutter&logoColor=white"/>
  <img src="https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white"/>
  <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB"/>
  <img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white"/>
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white"/>
</p>

---

## 📈 Current Focus

- 💡 Enhancing Flutter animations and transitions
- 🤖 Implementing AI-based logic with Google Gemini API
- 📲 Building portfolio-level applications using full-stack Django & Flutter

---

## 📫 Let's Connect!

<p align="left">
  <a href="https://x.com/NoorMustafa4556" target="blank">
    <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="X / Twitter" height="30" width="40" />
  </a>
  <a href="https://www.linkedin.com/in/noormustafa4556/" target="blank">
    <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="LinkedIn" height="30" width="40" />
  </a>
  <a href="https://www.facebook.com/NoorMustafa4556" target="blank">
    <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/facebook.svg" alt="Facebook" height="30" width="40" />
  </a>
  <a href="https://instagram.com/noormustafa4556" target="blank">
    <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="Instagram" height="30" width="40" />
  </a>
  <a href="https://wa.me/923087655076" target="blank">
    <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/whatsapp.svg" alt="WhatsApp" height="30" width="40" />
  </a>
  <a href="https://www.tiktok.com/@noormustafa4556" target="blank">
    <img src="https://cdn-icons-png.flaticon.com/512/3046/3046122.png" alt="TikTok" height="30" width="30" />
  </a>
</p>

- 📍 **Location:** Bahawalpur, Punjab, Pakistan

---

> _“Learning never stops. Every app I build makes me a better developer — one widget at a time.”_

---


    python app.py 
    ```

5.  **Open in your browser:**
    Navigate to `http://127.0.0.1:5000` to access the application.

---
