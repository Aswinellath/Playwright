# Playwright Python Beginner Learning Programs

## Introduction
This repository contains beginner-friendly learning programs for using [Playwright](https://playwright.dev/python/) with Python. Playwright is a powerful automation framework for web testing, providing support for multiple browsers and platforms. These programs are designed to help new users understand and practice Playwright's features.

## Prerequisites
Before running the scripts, ensure you have the following installed:

- Python 3.7+
- Playwright
- pip (Python package manager)

## Installation
Follow these steps to set up Playwright:

1. **Clone this repository**
   ```bash
   git clone https://github.com/yourusername/playwright-python-beginner.git
   cd playwright-python-beginner
   ```

2. **Create and activate a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright and browsers**
   ```bash
   playwright install
   ```

## Contents
This repository contains the following learning modules:

1. **Basic Setup** - Installing and configuring Playwright
2. **Launching Browsers** - Opening Chromium, Firefox, and WebKit
3. **Navigating Web Pages** - Visiting websites and interacting with elements
4. **Handling Forms** - Filling forms and submitting data
5. **Assertions & Testing** - Writing basic assertions for UI testing
6. **Screenshots & Videos** - Capturing screenshots and recording videos
7. **Headless vs Headed Mode** - Running tests in headless and UI modes
8. **Using Selectors** - Finding elements using CSS, XPath, and Playwright selectors
9. **Page & Context Handling** - Managing multiple pages and browser contexts

## Running the Scripts
To run a specific script, use:

```bash
python scripts/script_name.py
```

For example:
```bash
python scripts/navigate.py
```

## Contributing
Contributions are welcome! If you find issues or want to add new learning modules, feel free to submit a pull request.

## Resources
- [Playwright Documentation](https://playwright.dev/python/)
- [Python Official Documentation](https://docs.python.org/3/)

## License
This project is licensed under the MIT License.

