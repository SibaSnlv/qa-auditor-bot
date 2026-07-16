# Automated QA Auditor

An automated, headless testing script built with Python and Selenium to monitor the uptime and functional integrity of production web applications.

## Practical System Example: The 24/7 Auditor
Imagine a FinTech company with a critical online banking portal. This script acts as an automated auditor. 

Instead of paying a human to click through the website every day, this script can be scheduled to run silently in the background every hour. It opens a hidden browser, navigates to the "Client Login" and "Fund Transfer" pages, and verifies that the critical buttons actually exist and are clickable. If an overnight code update accidentally breaks the site, this auditor catches the error immediately and can alert the engineering team before any real customers are affected.

## Project Overview
This was originally used to test my web apps and see how if it's accessible and if all components work. This is for quality assurance before deployment.

## Tech Stack
* **Python 3**
* **Selenium WebDriver** (Headless Chrome execution)

## Setup
\`\`\`bash
pip install -r requirements.txt
python qa_auditor.py
\`\`\`
