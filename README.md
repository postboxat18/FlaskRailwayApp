# Flask App Hosting on Railway via GitHub

This repository demonstrates how to host a Flask application on [Railway](https://railway.app) using GitHub. Follow the steps below to deploy and run the application successfully.

---

## Prerequisites

1. **Railway Account**: Sign up or log in to [Railway](https://railway.app).
2. **GitHub Repository**: Clone or fork this repository.
3. **Python Installed**: Ensure Python (>= 3.7) is installed on your local machine.
4. **Gunicorn Installed**: Install Gunicorn for production:

   ```bash
   pip install gunicorn
   ```

---

## Local Setup

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/postboxat18/FlaskRailwayApp.git
   cd FlaskRailwayApp
   ```

2. **Install Dependencies**:

   Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

   Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask App Locally**:

   ```bash
   gunicorn -b :8000 app:app
   ```

   Open your browser and visit [http://localhost:8000](http://localhost:8000) to see the app running.

---

## Deploying to Railway

1. **Connect GitHub to Railway**:
   - Go to [Railway](https://railway.app) and log in.
   - Create a new project and select "Deploy from GitHub."
   - Link your repository (`FlaskRailwayApp`).

2. **Configure Environment Variables**:
   - In the Railway dashboard, go to the "Variables" section.
   - Add any required environment variables your Flask app needs (e.g., `FLASK_ENV`, `SECRET_KEY`).

3. **Set Up the Gunicorn Command**:
   - In the Railway project settings, configure the start command:

     ```bash
     gunicorn -b :$PORT app:app
     ```

   Railway will automatically set the `$PORT` environment variable.

4. **Deploy**:
   - Railway will build and deploy your application automatically.

5. **Access Your App**:
   - After deployment, you’ll be provided with a public URL to access your app.

---

## Additional Configuration Files

### Procfile

```
web: gunicorn app:app
```

### railway.json

```json
{
    "$schema": "https://railway.app/railway.schema.json",
    "build": {
        "builder": "NIXPACKS"
    },
    "deploy": {
        "startCommand": "gunicorn app:app",
        "restartPolicyType": "ON_FAILURE",
        "restartPolicyMaxRetries": 10
    }
}
```

### nixpacks.toml

```
# nixpacks.toml

[start]
cmd = "gunicorn app:app"
```

---

## Notes

- Ensure your `requirements.txt` includes all dependencies, including `gunicorn`.
- If you encounter issues, check Railway’s logs for debugging.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

