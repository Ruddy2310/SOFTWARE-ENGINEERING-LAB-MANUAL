# Practical 3 - Live Testing Tools Project

A small, real, runnable project used to demonstrate different categories of
software testing tools in action, instead of only describing them.

## Structure
```
Practical-3-Testing-Tools/
├── src/
│   ├── calculator.py       # app under test (unit testing demo)
│   └── api_server.py       # app under test (API/performance testing demo)
├── tests/
│   ├── test_calculator.py  # Unit Testing tool demo (unittest / JUnit / PyTest style)
│   └── test_api.py         # API Testing tool demo (Postman / RestAssured style)
├── selenium_test.py        # Automation Testing tool demo (Selenium)
├── postman_collection.json # Real Postman collection - importable into Postman
├── load_test.jmx           # Real JMeter test plan - importable into JMeter
├── .github/workflows/ci.yml# Live CI pipeline - runs tests on every push (GitHub Actions)
└── README.md
```

## How each tool is demonstrated

| Category | Tool represented | File | How to run |
|---|---|---|---|
| Unit Testing | JUnit / PyTest | `tests/test_calculator.py` | `python -m unittest tests.test_calculator -v` |
| API Testing | Postman / RestAssured | `tests/test_api.py`, `postman_collection.json` | `python -m unittest tests.test_api -v` (or import the JSON into Postman while `src/api_server.py` is running) |
| Performance Testing | Apache JMeter | `load_test.jmx` | Start `src/api_server.py`, then open `load_test.jmx` in JMeter and hit Run |
| Automation Testing | Selenium | `selenium_test.py` | `pip install selenium`, install ChromeDriver, then `python selenium_test.py` |
| CI / Continuous Testing | Jenkins / GitHub Actions | `.github/workflows/ci.yml` | Runs automatically on every `git push` - check the **Actions** tab on GitHub |

## Run everything locally
```bash
cd Practical-3-Testing-Tools
python -m unittest discover -s tests -v
```

## Live CI
Once this folder is pushed to GitHub, open the **Actions** tab of the
repository. The `Practical 3 - Live Testing Tools CI` workflow will run
automatically and show a green checkmark (or red, if a test fails) directly
on the commit - a live, continuously running demonstration of the Unit
Testing and API Testing tools on real GitHub infrastructure.
