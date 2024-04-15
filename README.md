The Health Umbrella Foundation is a platform designed to assist individuals who have been misled by unreliable online sources regarding their specific medical conditions. It provides access to scientifically validated data on disease treatments that have been experimentally proven effective. Additionally, the website offers information on the top hospitals specializing in each disease and provides curated YouTube and testimonial links to guide users toward better health outcomes
<br />

Initialising the project :<br />
    -> git clone https://github.com/healthumbrella/health_umbrella_foundation_backend <br />
    -> py -m venv env      -     Create a virtual environment.<br />
    -> .\env\Scripts\activate      -  Run virtual environment.<br />
    -> pip install -r requirements.txt  - Install the requirements<br />
    -> pyhton manage.py runserver   - Run the Django server<br />
<br />
In settings.py, add HOST_USER and HOST_PASSWORD to enable OTP verification
  EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
  EMAIL_HOST = 'smtp.gmail.com'
  EMAIL_PORT = 587
  EMAIL_USE_TLS = True
  EMAIL_HOST_USER = ''
  EMAIL_HOST_PASSWORD = ''
<br />
Open http://127.0.0.1:8000/ to view it in the browser.


