# Django Job Board API
    A RESTful API built with Django and Django REST Framework (DRF) for a simple job board application. Users can register as employers or job seekers, post jobs, manage skills, and apply to jobs. Authentication is JWT-based using Simple JWT for token management.

## Features

    User Roles: Employers (post jobs) and Seekers (apply to jobs with skills).
    Custom User Model: Uses email as the username, with role-based validation (e.g., employers can't have skills).
    Models:

    CustomUser: Core user with profile details.
    Profile: One-to-one extension of user (note: currently empty in provided code; extend as needed).
    Skill: Reusable skills for seekers and jobs.
    Job: Posted by employers, with skills, location, and salary.
    Application: Links seekers to jobs.

    API Endpoints: Managed via DRF ViewSets for CRUD operations on Users, Jobs, Skills, and Applications. Additional endpoints for authentication and profile management.
    Authentication: JWT-based (access and refresh tokens). Protected endpoints require Authorization: Bearer <access_token> header.
    Permissions: Assume role-based checks in views (e.g., only employers can create jobs; implement in ViewSets permissions).

## Prerequisites

    Python 3.8+
    Django 4.x+
    Django REST Framework
    djangorestframework-simplejwt
    A database (default SQLite for development; configure PostgreSQL for production)

## Installation
 1. Clone the Repository:
    git clone https://github.com/AmanT776/Job-board-api.git
    cd <project-directory>

 2. Setup virtual environment
    python -m venv venv
    source venv/bin/activate  
    On Windows: venv\Scripts\activate
 3. Install Dependencies:
    pip install django djangorestframework djangorestframework-simplejwt

## Project Structure

    - apps/users/models.py: Defines CustomUser, Role, and related logic.
    - apps/users/views.py: Likely contains UserViewSet, CustomTokenObtainPairView (custom login), ProfileView.
    - apps/job_application/models.py: Defines Skill, Job, Application, and Profile.
    - apps/job_application/views.py: ViewSets for Jobs, Skills, Applications (e.g., JobViewsets, SkillViewSets, ApplicationViewSets).
    - apps/users/urls.py: Handles user-related routes (registration, login, profile).
    - apps/job_application/urls.py: Handles job-related routes.
    Mount apps in project urls.py, e.g.:
## Models Overview

### CustomUser (users app)

    Fields: first_name, last_name, phone, email (unique, login field), role (employer/seeker), skill (ManyToMany for seekers only), timestamps.
    Validation: Employers cannot have skills.
    Manager: CustomUserManager (custom creation logic assumed).
    String representation: First name.

### Profile (job_application app)
    OneToOne with CustomUser. Currently empty; add fields like bio or resume URL.

### Skill (job_application app)
    Fields: name, timestamps.
    Used by seekers and jobs.

### Job (job_application app)
    Fields: title, description, employer (FK to CustomUser), skill (ManyToMany), location, salary, timestamps.
    Posted only by employers.

### Application (job_application app)
    Fields: seeker (FK to CustomUser), job (FK), timestamps.
    Represents job applications.

## API Endpoints
### User Management (Base: /api/users/)
#### Uses DRF routers and paths:
##### Users (/users/):
    GET: List all users / Retrieve a user (admin or self).
    POST: Register a new user (provide email, password, role, etc.).
    PUT/PATCH: Update user.
    DELETE: Delete user.

##### Login (/login):
    POST: Obtain JWT tokens. Body: {"email": "...", "password": "..."}. Returns access and refresh tokens.


##### Token Refresh (/refresh):
    POST: Refresh access token. Body: {"refresh": "<refresh_token>"}.
##### Profile (/profile):
    GET/PUT: View or update own profile (authenticated).

#### Job Board (Base: /api/jobs/)
Uses DRF routers for automatic CRUD:

##### Jobs (/jobs/):
    GET: List all jobs / Retrieve a job.
    POST: Create a job (employer only).
    PUT/PATCH: Update a job.
    DELETE: Delete a job.
    Example: GET /jobs/ – Returns paginated list of jobs.


##### Skills (/skills/):
    GET: List / Retrieve skills.
    POST: Create skill (admin or authenticated).
    PUT/PATCH/DELETE: Update/Delete.
##### Applications (/apply/):
    GET: List applications (own or employer's jobs).
    POST: Apply to a job (seeker provides job ID).
    etc.