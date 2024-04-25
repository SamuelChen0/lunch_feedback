# Lunch Feedback WebApp

## Description

The Lunch Feedback WebApp is a Python-based application designed to collect feedback on daily lunches at Hsinchu American School.

## Technology Stack

- **Backend**: Flask (Python)
- **Database**: SQLAlchemy (SQLite for development, PostgreSQL for production)
- **Frontend**: HTML, CSS
- **Version Control**: Git

## Setting up the Development Environment

### Prerequisites

- Python 3.8 or newer
- Pip (Python package installer)
- Virtual environment (recommended)

### Getting the Java Commmand
1. Clone this repository:
  ```sh
   git clone https://github.com/rentsdue/PlatformGameProject.git
   ```
2. Go to the "lunch_feedback_edition" branch of the repository.
3. Click "run" on Visual Studio Code.
4. Copy the command that is used to run the game, and then format it like this:
  ```sh
   command = [
    r'C:\Program Files\Eclipse Adoptium\jdk-21.0.2.13-hotspot\bin\java.exe',
    # Java VM Option
    '-XX:+ShowCodeDetailsInExceptionMessages',
    # Classpath Option
    '-cp',
    # Classpath Value
    r'C:\Users\admin\PlatformGameProject\bin',
    # Main Class to Run
    'main.java.com.example.Main'
]
   ```
5. Go to the .env file and copy the command into "JAVA_COMMAND"

### Installation Steps

1. Clone the repository:
   ```sh
   git clone https://github.com/SamuelChen0/lunch_feedback.git
   ```
   
2. Navigate to the project directory:
   ```sh
   cd lunch_feedback
   ```pip install -r requirements.txt

3. Create a virtual environment and activate it:
   ```sh
   python3 -m venv env
   env\Scripts\activate # On Mac IOS, use ` source env/bin/activate`
   ```

4. Install the necessary packages:
   ```sh
   pip install -r requirements.txt
   ```    

6. Run the application:
   ```sh
   python main.py
   ```

7. Open your browser and visit `http://127.0.0.1:8080` to access the application.

## Support

For support, please create an issue on the GitHub issue tracker or contact the maintainers directly.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
