# BrowserStack Assignments: BrowserStack Automation Test with Selenium and Python
This project demonstrates the automation of a test scenario using Selenium and Python on BrowserStack's infrastructure. The test scenario involves navigating to flipkart.com, searching for a product ("Samsung Galaxy S10"), applying filters, sorting results, and gathering specific information about the products displayed on the first page of search results.

## Clone Repository:
```bash
git clone https://github.com/haseebhijazi/HaseebHijaziKhan_BrowserStackAssignments.git
cd HaseebHijaziKhan_BrowserStackAssignments
```
## Create virtual environment
```bash
python3 -m venv venv
```

## Activate Virtual Environment:
```bash 
source venv/bin/activate
```

## Install Dependencies:
```bash 
pip install -r requirements.txt
```

## Set BrowserStack Credentials:
```bash
export BROWSERSTACK_USERNAME=<your_username>
export BROWSERSTACK_ACCESS_KEY=<your_access_key>
```

## Local Test Execution:
```bash
python automation_test.py
```

## Configuration for GitHub Actions:
[How to create Github Secrets](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions)

## Results
Results are logged onto the terminal along with providing the url to Browser Stack dashboard 

Change
