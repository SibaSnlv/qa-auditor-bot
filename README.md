# Automated QA Auditor

An automated, headless testing script built with Python and Selenium to monitor the uptime and functional integrity of production web applications.

## Practical System Example: The 24/7 "Night Watchman"
Imagine a FinTech company with a critical online banking portal. This script acts as an automated night watchman. 

Instead of paying a human to click through the website every day, this script can be scheduled to run silently in the background every hour. It opens a hidden browser, navigates to the "Client Login" and "Fund Transfer" pages, and verifies that the critical buttons actually exist and are clickable. If an overnight code update accidentally breaks the site, this auditor catches the error immediately and can alert the engineering team before any real customers are affected.

## Tech Stack
* **Python 3**
* **Selenium WebDriver** (Headless Chrome execution)

## Setup
\`\`\`bash
pip install -r requirements.txt
python qa_auditor.py
\`\`\`