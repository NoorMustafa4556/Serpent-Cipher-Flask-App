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
    python app.py 
    ```

5.  **Open in your browser:**
    Navigate to `http://127.0.0.1:5000` to access the application.

---
