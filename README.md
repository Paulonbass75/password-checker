# Password Checker

This project allows users to check if their passwords have been compromised using the "Have I Been Pwned" API.

## Project Structure

- `templates/index.html`: Contains the HTML form for submitting a password.
- `checkmypass.py`: Python script that checks if the submitted password has been compromised.
- `requirements.txt`: Lists the dependencies required for the project.
- `README.md`: Documentation for the project.

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd password-checker
   ```

2. **Install dependencies**:
   Make sure you have Python installed, then run:
   ```
   pip install -r requirements.txt
   ```

3. **Run the application**:
   Execute the Python script:
   ```
   python checkmypass.py
   ```

4. **Access the application**:
   Open your web browser and navigate to `http://localhost:5000` (or the appropriate URL if using a web framework).

## Usage

- Enter your password in the input field and click the submit button.
- The application will check if the password has been found in any data breaches and display the result.

## License

This project is licensed under the MIT License.