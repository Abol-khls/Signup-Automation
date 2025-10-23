# TypeKadeh Signup Automation 🚀

## Overview

This python file automates the signup process on [TypeKadeh](https://typekadeh.com) using Selenium. It visits the signup page, fills out the necessary fields (email, username, password), and submits the form.

## Features

*   Automates account creation on TypeKadeh.
*   Uses Selenium to automate action taken on website.
*   A configuration file can be used where you can specify your email, username, and password.

## Installation

1.  Clone this repository:

    ```sh
    git clone https://github.com/Abol-khls/Signup-Automation.git
    ```

3.  Install Python virtual environment:

    ```sh
    python -m venv .venv
    ```

4.  activate Python virtual environment:

    ```sh
    .venv\Scripts\activate
    ```

2.  Install the required Python package:

    ```sh
    pip install selenium
    ```

## Usage

1.  **Configuration:**
    *   Open `1.py` and modify the `inputEmail`, `inputUsername`, and `inputPass` variables with your desired credentials.
2.  **Run the script:**

    ```sh
    python 1.py
    ```

## Code Explanation

*   **`1.py`**: The main script.
    *   Imports necessary Selenium modules.
    *   Uses `webdriver.Chrome()` to initialize the Chrome driver.
    *   Locates web elements using XPath.
    *   Sends keys (email, username, password) to the input fields.
    *   Clicks the submit button.
    *   Includes a `time.sleep(100)` at the end to keep the browser open for observation.

## Customization

*   **Credentials:** You can change the email, username, and password inside of the script.
*   **XPath Selectors:** If the website structure changes (TypeKadeh), you will have to update the XPath selectors in the script for it to work.  You can inspect the elements through your developer tools of the browser to get the correct XPaths.
*   **Browser:**  This script uses Chrome by default, but can be changed to any other browser with Selenium support, such as Firefox, by changing the line in the script where it says `webdriver.Chrome()`.  You will need the WebDriver for the browser you want to use.

## Disclaimer

The authors intention for this code is for educational purposes and personal use only.  Automating account creation can likely violate the terms of agreement for TypeKadeh. Use responsively and at your own risk, as the author takes no responsibility for any consequences that happen from running the code provided above.

## License

MIT License