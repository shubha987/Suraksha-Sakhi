![image-banner](surakshasakhi.png)

# Suraksha Sakhi

Suraksha Sakhi is a project aimed at creating a safe and supportive environment for women. It provides a platform for women to connect with trusted individuals who can offer assistance and support in times of need.

## Getting Started

To run Suraksha Sakhi on your localhost, follow these steps:

1. Fork this repository by clicking `fork` button in upper-right corner

2. Clone the repository:
```bash
git clone https://github.com/your-username/SurakshaSakhi.git
```

3. Navigate to the project directory:
```bash
cd SurakshaSakhi/mysite
```

4. Install the dependencies:
```bash
pip install -r requirements.txt
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Open your web browser and visit `http://localhost:8000` to access Suraksha Sakhi.


## Sending Mail through SMTP server
To send mail through an SMTP server in your application, you need to follow these steps:
1.Create an app in your Gmail account:
<ul>
  <li>Go to your Google Account settings</li>
  <li>Click on "Security" in the left sidebar.</li>
  <li>Scroll down to the "Third-party apps with account access" section and click on "Manage third-party access".</li>
  <li>Click on "Add app" or "Manage apps"</li>
  <li>Search for "Suraksha Sakhi" or enter a custom name for your app</li>
  <li>Click on "Create" or "Next" to generate an app password.</li>
</ul>
2.Generate an app password:
<ul>
  <li>After creating the app, you will be provided with an app password</li>
  <li>Copy the generated app password as you will need it to authenticate your application</li>
</ul>

3.Configure your application to use the app password:
In the `mail.py` file do necessary changes:
```bash
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
```
Replace `'your-email@gmail.com'` with your Gmail account email address and `'your-app-password'` with the app password you generated.

## Contributing

We welcome contributions from the community to make Suraksha Sakhi even better. To contribute, please follow these steps:

1. Fork the repository on GitHub.

2. Clone your forked repository:
    ```bash
    git clone https://github.com/your-username/SurakshaSakhi.git
    ```

3. Create a new branch for your feature or bug fix:
    ```bash
    git checkout -b feature/your-feature-name
    ```

4. Make your changes and commit them:
    ```bash
    git commit -m "Add your commit message here"
    ```

5. Push your changes to your forked repository:
    ```bash
    git push origin feature/your-feature-name
    ```

6. Open a pull request on the original repository.

Please ensure that your contributions adhere to our [code of conduct](CONTRIBUTING.md) and [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).