# Texas DPS Appointment Finder

This is a Python script that automates the process of finding and booking earlier appointments for Texas Department of Public Safety (DPS) services.

## Installation

To use this script, you need to have [Python 3](https://www.python.org/downloads/) installed on your computer. You also need to install the following Python packages:

- `selenium`
- `webdriver_manager`

You can install these packages by running the following command:

`pip install selenium`

You also need to download the [ChromeDriver executable](https://chromedriver.chromium.org/downloads) and add it to your system path.

## Usage

1. Open `config.py` and edit the following variables with your personal information:

   - `APPLICANT_FIRST_NAME`
   - `APPLICANT_LAST_NAME`
   - `DOB` (in the format `MM/DD/YYYY`)
   - `LAST_FOUR_SSN`
   - `POSTAL_CODE`
   - `IDEAL_DATE` (the earliest date you want to schedule the appointment)

2. Run the script by executing the following command in your terminal:

`python main.py`


3. The script will automatically open a Chrome browser window and navigate to the Texas DPS appointment scheduler website. It will then search for earlier appointments and book them if available.

## Notes

- This script is for educational purposes only. Use it at your own risk, as the Texas DPS may have policies against automated appointment scheduling.
- The script was last tested in September 2021. If the Texas DPS website has changed since then, the script may not work properly.
- If you encounter any issues or errors while using the script, please create an issue in this repository and provide as much detail as possible.
