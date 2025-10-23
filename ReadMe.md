# TypeKadeh Signup Automation 🚀

## Overview

This Python script automates the signup process on [TypeKadeh](https://typekadeh.com) using Selenium. It navigates to the signup page, fills in the required fields (email, username, password), and submits the form.

## Features

*   Automates account creation on TypeKadeh.
*   Uses Selenium to interact with the website.
*   Configurable with your desired email, username, and password.

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

*   **Credentials:** Modify the email, username, and password directly in the script.
*   **XPath Selectors:** If TypeKadeh changes its website structure, you'll need to update the XPath selectors in the script to match the new structure.  Inspect the elements in your browser's developer tools to get the correct XPaths.
*   **Browser:**  The script currently uses Chrome.  You can adapt it to other browsers supported by Selenium (e.g., Firefox) by changing the `webdriver.Chrome()` line.  You'll also need the appropriate WebDriver for that browser.

## Disclaimer

This script is intended for educational purposes and personal use. Automating account creation may violate the terms of service of TypeKadeh. Use responsibly and at your own risk.  The author is not responsible for any consequences of using this script.

## License

MIT License