# Automated_website_testing

# Automated Website Testing Project

This is an automated testing project using Selenium WebDriver and Python's unittest framework. The project is designed to test functionalities such as login, adding items to the cart, and validating cart contents on [the Sauce Demo](https://www.saucedemo.com/) e-commerce website.

# Table of Contents
1. Project Overview
2. Technologies Used
3. Setup
4. Running Tests
5. Test Structure
6. Contributing
7. License

# 1. Project Overview
This project automates various flows of an e-commerce website such as:
1. Logging in with valid credentials.
2. Searching for and adding specific products to the shopping cart.
3. Verifying that the selected products are successfully added to the cart.
The project follows the Page Object Model (POM) design pattern for better readability, maintainability, and scalability.

# 2. Technologies Used
1. Python 3.x
2. Selenium WebDriver
3. unittest (for structuring and running tests)
4. Google Chrome (browser used for testing)
5. PyCharm (as the development environment)

# 3. Setup
Prerequisites
1. Python 3.x should be installed on your system. [Download Python](https://www.python.org/downloads/)
2. Install Google Chrome browser.
3. Install ChromeDriver and ensure it is added to your system's PATH.

Installing Dependencies
1. Clone the repository to your local machine:
(bash)
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2. Create and activate a virtual environment (optional but recommended):
(bash)
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows

3. Install the required packages:
(bash)
pip install -r requirements.txt

Setting Up WebDriver
Download the ChromeDriver version compatible with your installed Chrome browser. Add the ChromeDriver to your PATH so Selenium can use it.

# 4. Running Tests
Start by ensuring that the WebDriver (e.g., ChromeDriver) is available in your PATH or in the project directory.

To run the tests, simply execute the following command:
(bash)
python -m unittest discover -s tests
This will run all the test cases defined in the tests directory.

# 5. Test Structure
Login Tests
The login tests validate that a user can successfully log into the SauceDemo site with valid credentials.

Cart Tests
The cart tests check whether users can add items to their shopping cart and verify that the selected items are correctly listed in the cart.

Example Test Workflow
1. Open the SauceDemo website.
2. Log in using valid credentials (standard_user / secret_sauce).
3. Search for products such as Sauce Labs Bike Light and Sauce Labs Onesie.
4. Add the items to the cart.
5. Go to the cart and verify the items have been added.

# 6. Contributing
Feel free to fork this repository and make your own contributions. When submitting a pull request, make sure to include clear commit messages and ensure that all tests pass.

# 7. License
This project is licensed under the MIT License - see [LICENSE](https://docs.github.com/de/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository#disclaimer) for details.
