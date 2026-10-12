# fullstack_developer_capstone

## Cars Dealership — Full-Stack Development Capstone

**Repository Name:** `xrwvm-fullstack_developer_capstone`  
**Project Name:** `fullstack_developer_capstone`  
**Application:** Cars Dealership Review Platform  
**Project Type:** Full-Stack Web Application

---

## 1. Project Overview

The Cars Dealership Full-Stack Development Capstone is a web application that allows users to explore car dealerships, view dealership information, read customer reviews, and submit their own reviews.

The application demonstrates full-stack development using Django, Python, React, HTML, CSS, JavaScript, REST-style API endpoints, database integration, authentication, sentiment analysis, Docker, and GitHub Actions.

The project follows a modular application structure with frontend components, backend functionality, dealership data, customer reviews, and administrative management.

## 2. Project Objectives

- Display dealership information and dealership locations.
- Retrieve dealership records through API endpoints.
- Filter dealerships by state.
- Display individual dealership details.
- Support user registration, login, and logout.
- Retrieve customer reviews for individual dealerships.
- Allow authenticated users to submit reviews.
- Analyze review text to identify sentiment.
- Display car makes and associated models.
- Provide an administrative interface using Django Admin.
- Support application containerization with Docker.
- Automate configured checks and tests through GitHub Actions.
- Prepare the application for deployment to a cloud environment.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web framework and request handling |
| Django Admin | Administrative interface |
| React | Frontend registration component |
| HTML5 | Webpage structure |
| CSS3 | Styling and responsive layouts |
| JavaScript | Frontend interaction |
| REST-style APIs | Communication between application components |
| SQLite | Local development database |
| Git and GitHub | Version control and source-code hosting |
| GitHub Actions | CI/CD workflow automation |
| Docker | Application containerization |
| Cloud deployment | Hosting the application |

The technologies listed above describe the intended project stack. Optional components and deployment services must be configured and verified in the actual environment.

## 4. Main Application Features

### Dealership Directory
- Retrieve dealership records.
- Display dealership names, locations, addresses, and other available details.
- Filter dealerships by state.
- Open an individual dealership details page.

### User Authentication
- Register a user with a username, first name, last name, email address, and password.
- Log in using valid credentials.
- Log out of an authenticated session.
- Display the logged-in user's identity where required.

### Customer Reviews
- Retrieve reviews associated with a dealership.
- Submit reviews through the application.
- Include purchase date and vehicle details where supported.
- Display posted reviews on the dealership details page.

### Sentiment Analysis
Analyze review text and classify its sentiment according to the configured analysis implementation.

Example input:

`Fantastic services`

The expected interpretation is positive sentiment. The actual API response depends on the configured implementation.

### Car Makes and Models
Retrieve available car makes and their associated models through the configured car-data endpoint.

### Administrative Management
Use Django Admin to manage supported application records and administrative data.

## 5. Repository Structure

The repository is organized around the Django application, frontend resources, configuration files, and submission evidence.

```text
xrwvm-fullstack_developer_capstone/
├── manage.py
├── README.md
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── DEPLOYMENT.md
├── .github/
│   └── workflows/
├── server/
│   └── frontend/
│       ├── static/
│       │   ├── About.html
│       │   ├── Contact.html
│       │   └── css/
│       └── src/
│           └── components/
│               └── Register/
│                   └── Register.jsx
└── submission/
    ├── evidence_checklist.md
    └── deploymentURL
```

This is a reference structure. The actual repository may contain additional application modules, migrations, database files, templates, and tests.

## 6. Installation Requirements

Install the following software before running the project:

- Python 3.11 or a compatible supported Python version.
- pip.
- Git.
- Node.js 18 or a compatible version if building the React component separately.
- Docker, if using the containerized setup.

## 7. Run the Application Locally

### Step 1: Clone the repository

```bash
git clone https://github.com/vikas-dangi07/xrwvm-fullstack_developer_capstone.git
cd xrwvm-fullstack_developer_capstone
```

### Step 2: Create a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4: Apply database migrations

```bash
python manage.py migrate
```

### Step 5: Create an administrative user

```bash
python manage.py createsuperuser
```

Follow the prompts to create your own administrative account.

### Step 6: Load demonstration data

If the repository includes the `seed_demo` management command, run:

```bash
python manage.py seed_demo
```

### Step 7: Start the Django development server

```bash
python manage.py runserver
```

Open the following URLs in your browser:

- Application: http://127.0.0.1:8000/
- Django Admin: http://127.0.0.1:8000/admin/

These URLs apply to local development. A cloud deployment will have a different URL.

## 8. API Endpoints

The following endpoints are required by the capstone evaluation rubric. Verify that they are implemented and accessible in the actual application before using them.

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/djangoapp/login` | Authenticate a user |
| GET | `/djangoapp/logout` | Log out a user |
| GET | `/fetchDealers` | Retrieve all dealers |
| GET | `/fetchDealers/Kansas` | Retrieve dealers in Kansas |
| GET | `/fetchDealer/1` | Retrieve an individual dealer |
| GET | `/fetchReviews/dealer/1` | Retrieve reviews for a dealer |
| GET | `/djangoapp/get_cars` | Retrieve car makes and models |
| GET | `/analyze/Fantastic%20services` | Analyze the sentiment of review text |

The dealer ID `1` and the Kansas state filter are examples for testing. Other valid IDs and state values can be used where supported.

### API Testing with cURL

Retrieve all dealerships:

```bash
curl http://127.0.0.1:8000/fetchDealers
```

Retrieve Kansas dealerships:

```bash
curl http://127.0.0.1:8000/fetchDealers/Kansas
```

Retrieve an individual dealership:

```bash
curl http://127.0.0.1:8000/fetchDealer/1
```

Retrieve dealership reviews:

```bash
curl http://127.0.0.1:8000/fetchReviews/dealer/1
```

Retrieve car makes and models:

```bash
curl http://127.0.0.1:8000/djangoapp/get_cars
```

Analyze the review text:

```bash
curl "http://127.0.0.1:8000/analyze/Fantastic%20services"
```

For login and logout, use the HTTP methods and JSON fields required by the implemented API. Use the actual server responses as submission evidence rather than manually written sample output.

## 9. Frontend Pages

The frontend requirements include:

- **Home page:** Displays the dealership directory.
- **About Us:** Provides project information and team-member details.
- **Contact Us:** Displays contact information and navigation.
- **Registration page:** Includes Username, First Name, Last Name, Email, Password, and a Register button.
- **Login page:** Allows users to authenticate.
- **Dealership details page:** Displays information for a selected dealership and its reviews.
- **Review submission page:** Allows a user to enter review details.
- **Review results:** Displays the submitted review and sentiment information where implemented.

The application should use appropriate CSS and Bootstrap stylesheet links where required by the assignment.

## 10. Database and Data Management

The application uses Django's configured database to store supported application records. SQLite is intended for local development in the starter configuration.

Database migrations should be applied before the application is used.

The dealership and review records should be populated using the actual application data or supported demonstration-data commands. API output should reflect the records stored in the running application.

## 11. Testing

Before submission, verify the following:

- The Django server starts without system-check errors.
- The application home page loads.
- The dealership API returns the expected records.
- State filtering returns the correct dealerships.
- Individual dealership details can be retrieved.
- Review retrieval includes the required vehicle and purchase details.
- Registration and authentication work.
- Logout returns the required response.
- Car makes and models are returned in the expected format.
- The sentiment endpoint responds to the specified review text.
- The admin interface supports successful login and logout.
- The GitHub Actions workflow completes successfully.

Only mark a test as passed after verifying its result.

## 12. GitHub Actions and CI/CD

GitHub Actions is used to automate the configured project workflow.

The workflow should include the appropriate repository checkout, runtime setup, dependency installation, and application checks or tests. If the course workflow requires both Python and JavaScript jobs, ensure that both jobs are configured and execute successfully.

To verify a run:

1. Open the repository on GitHub.
2. Select the **Actions** tab.
3. Open a completed workflow run.
4. Inspect each required job and step.
5. Confirm that the run completed successfully.

Actual workflow logs must be used as evidence. A list of expected steps in this README does not prove that a workflow has run.

## 13. Docker

If Docker support is configured, build and start the application with:

```bash
docker compose up --build
```

Open the configured application address in your browser.

Docker configuration, environment variables, exposed ports, and database persistence should be verified before deployment.

## 14. Deployment

Refer to `DEPLOYMENT.md` for the deployment procedure supported by this repository.

The final deployment must use your own course lab or cloud environment. If the assignment requires Skills Network or IBM Cloud Code Engine, follow the environment-specific instructions provided by your course.

After a successful deployment:

1. Obtain the actual public application URL.
2. Verify that the landing page loads.
3. Test login and logout.
4. Open a dealership details page.
5. Submit and verify a customer review.
6. Capture screenshots of the deployed pages.
7. Save the real deployment URL in the required `submission/deploymentURL` file.

Do not replace the deployment URL with a placeholder or a local `127.0.0.1` address.

## 15. Final Submission Checklist

Before submitting the capstone, verify all 28 graded tasks against the course rubric.

### Repository and frontend
- [ ] Repository name is `xrwvm-fullstack_developer_capstone`.
- [ ] README identifies the project as `fullstack_developer_capstone`.
- [ ] About Us page has the required styling and team details.
- [ ] Contact Us page includes required stylesheets and images.
- [ ] Registration page contains all five input fields.

### Backend and API evidence
- [ ] Django server output is captured.
- [ ] Login cURL command and actual response are captured.
- [ ] Logout cURL command and actual response are captured.
- [ ] Dealer review output includes the required purchase and car fields.
- [ ] All 50 dealers are retrieved with the required fields.
- [ ] Individual dealer details include latitude, longitude, short name, and full name.
- [ ] Kansas filtering uses the required endpoint.
- [ ] Car makes and models use `/djangoapp/get_cars`.
- [ ] Sentiment analysis uses `/analyze/Fantastic%20services`.

### Screenshots
- [ ] Successful admin login.
- [ ] Admin logout.
- [ ] Dealer home page before login.
- [ ] Dealer home page after login.
- [ ] Kansas dealer filtering.
- [ ] Individual dealer details with reviews.
- [ ] Completed review form before submission.
- [ ] Posted review with sentiment image.

### CI/CD and deployment
- [ ] Actual successful GitHub Actions run is documented.
- [ ] Both required workflow jobs and their steps are visible.
- [ ] `submission/deploymentURL` contains the actual public deployment URL.
- [ ] Deployed landing-page screenshot is captured.
- [ ] Deployed logged-in screenshot displays the username.
- [ ] Deployed dealer details screenshot is captured.
- [ ] Deployed review screenshot is captured.

Use the exact filenames specified by the course when uploading screenshots and evidence.

## 16. Project Status

This README describes the application and the work required for the capstone. Completion of the graded assignment depends on the actual application implementation, successful tests, genuine screenshots, CI/CD results, and a working deployment.

The repository and project names are stated explicitly to match the course's naming requirements.
