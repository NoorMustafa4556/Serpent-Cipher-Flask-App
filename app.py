from flask import Flask, render_template, request, jsonify, redirect, url_for

# Import the cerpent cipher functions
# Ensure you have a file named cerpent.py in the same directory
try:
    from cerpent import generate_key, encrypt, decrypt
except ImportError:
    print("Error: cerpent.py not found. Please make sure cerpent.py is in the same directory as App.py")
    print("You can use the cerpent.py code provided below.")
    exit() # Exit if the crypto module can't be imported


app = Flask(__name__)

@app.route("/")
def home():
    """Renders the home/landing page."""
    # The home page now contains introductory text and relies on the navbar for navigation
    return render_template("home.html")

@app.route("/encrypt", methods=["GET", "POST"])
def encrypt_page():
    """
    Renders the encryption form on GET request.
    Handles encryption on POST request and redirects to the result page.
    """
    if request.method == "GET":
        return render_template("index.html") # index.html now serves as the encryption page

    # Handle POST request from the encryption form
    try:
        message = request.form.get("message", "").strip()
        if not message:
            raise ValueError("Message cannot be empty!")
        key = request.form.get("key", "").strip()
        if not key:
            raise ValueError("Secret key is required for encryption!")
        ciphertext = encrypt(message, key)
        # Redirect to result page after successful encryption
        # Pass result details as query parameters
        return redirect(url_for('result_page', operation="Encryption", result=ciphertext, success=True))
    except Exception as e:
        # Redirect to result page with error on failure
        return redirect(url_for('result_page', operation="Encryption", result=str(e), success=False))


@app.route("/decrypt", methods=["GET", "POST"])
def decrypt_page():
    """
    Renders the decryption form on GET request.
    Handles decryption on POST request and redirects to the result page.
    """
    if request.method == "GET":
        return render_template("decrypt.html") # decrypt.html serves as the decryption page

    # Handle POST request from the decryption form
    try:
        ciphertext = request.form.get("ciphertext", "").strip()
        if not ciphertext:
            raise ValueError("Ciphertext cannot be empty!")
        key = request.form.get("key", "").strip()
        if not key:
            raise ValueError("Secret key is required for decryption!")
        plaintext = decrypt(ciphertext, key)
        # Redirect to result page after successful decryption
        # Pass result details as query parameters
        return redirect(url_for('result_page', operation="Decryption", result=plaintext, success=True))
    except Exception as e:
        # Redirect to result page with error on failure
        return redirect(url_for('result_page', operation="Decryption", result=str(e), success=False))

# New route for displaying results - uses query parameters passed from redirects
@app.route("/result")
def result_page():
    """Renders the result page displaying the outcome of encrypt/decrypt operations."""
    operation = request.args.get('operation', 'Operation')
    result = request.args.get('result', 'No result available.')
    # Get success status, default to False if not provided or not 'true' case-insensitive
    success = request.args.get('success', 'False').lower() == 'true'

    # Basic check to prevent displaying very long error messages directly in the URL
    # This is a simplification; for real apps, pass an error ID or use flash messages
    if len(result) > 500 and not success:
        result = "An unexpected error occurred. Please check your input or key."

    return render_template("result.html", operation=operation, result=result, success=success)


@app.route("/generate_key", methods=["GET"])
def generate_key_route():
    """
    Generates a new secret key.
    Intended to be called via AJAX from the frontend.
    """
    # Ensure this is an AJAX request if possible, though not strictly required by Flask
    if not request.headers.get("X-Requested-With") == "XMLHttpRequest":
         # Optional: Return an error or redirect if not AJAX
         # return jsonify({"error": "AJAX request expected"}), 400
         pass # Allow non-AJAX GET for simple testing

    try:
        key = generate_key()
        # Always return JSON response containing the key
        return jsonify({"key": key})
    except Exception as e:
        error_msg = str(e)
        # Return JSON response with error message and 500 status code
        return jsonify({"error": error_msg}), 500


if __name__ == "__main__":
    # Ensure the static and templates directories exist before running
    import os
    os.makedirs('static', exist_ok=True)
    os.makedirs('templates', exist_ok=True)
    # Use a more robust server like Waitress in production instead of debug=True
    app.run(debug=True)