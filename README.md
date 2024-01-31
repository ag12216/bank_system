1. Clone the project 
2. Create the virtual env -> python3 -m venv venv
3. Activate the virtual environment -> source venv/bin/activate
4. Install the requirements.txt file -> pip3 install -r requirements.txt
5. Collect all the static files -> python3 manage.py collectstatic
6. Migrate all the basic tables -> python3 manage.py migrate app
7. Run the test cases: python3 manage.py test app.tests.BankingSystemTestCase

(Note: above cmd is as per linux)
