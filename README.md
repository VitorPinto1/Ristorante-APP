# Ristorante ilcapo Application Mobile

Prerequisites

- 	Visual Studio Code
-  	Python Extension for VS Code
-  	Git
-  	Python 3.9
-  	MySQL: The MySQL database server must be running. Filess.io

1. Installation and Deployment

Launch VSCode and install the "Python" extension published by Microsoft. After creating the 'Restaurant app' folder, open an integrated terminal in VS Code to clone the repository and execute the following commands:

  	« git clone https://github.com/VitorPinto1/Ristorante-APP.git »
  	« cd Restaurant app »
   
2. Environment Configuration

Activate the Python virtual environment in the terminal:

  	« source env/bin/activate »  # Unix ou MacOS
  	« env\Scripts\activate »    # Windows

If the virtual environment does not exist yet, you can create it with:

  	« python -m venv env » 

3. Install Dependencies

Install the necessary packages from the requirements.txt file, if available:

  	« pip install -r requirements.txt »

4. Launching the Application

Run the application in the terminal:

  	« python main.py »

5. Accessing the Application

By following these steps, you should be able to deploy the mobile application locally and test its functionalities.

# File Information

Screens Folder

Contains Python (.py) files for the different screens of the application. Each file in this folder defines the logic and specific interactions for a particular screen of the application.

- login_screen.py: Manages the logic for the login screen.
- reservation_screen.py: Manages the logic for the reservations screen.
- myreservation.py: Manages the logic for the reservation details screen.
- reservation_modification.py: Manages the modifications of reservations.

Tools Folder

Contains utilities and tools used by the application.

- database.py: Manages interactions with the database. This file provides services for connecting to the database, retrieving user data, verifying passwords, and managing reservations.

screens.kv File

Defines the styles and visual layout of the different screens of the application.

main.py File

Entry point of the application. This file initializes the application, loads the layout defined in screens.kv, and configures the ScreenManager to handle navigation between different screens. It also configures environment variables for the database, and initializes and displays the user interface.

