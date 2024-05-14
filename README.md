# MediCare

MediCare is a web-based healthcare platform that aims to provide a centralized system for managing healthcare services across multiple hospitals. The platform has different modules for different types of users, such as patients, doctors, hospital administrators, lab workers, and pharmacists. The platform allows users to perform various tasks related to their healthcare needs, such as accessing information, booking appointments, purchasing medicines, paying for tests, and communicating with each other. The platform also allows users to access and share their health records with other authorized users, such as doctors or pharmacists. This way, the platform helps users to manage their healthcare needs more easily and conveniently, while also reducing the workload and costs for healthcare providers.

## Screenshots
Home Page
![Screenshot 2023-11-24 200118](https://github.com/Heartsx12/JobFinder/assets/120915164/103ee706-782d-44e4-a769-af9b55c00ab7)
Jobs Page
![Screenshot 2023-11-24 200138](https://github.com/Heartsx12/JobFinder/assets/120915164/6be19d37-dd50-49f9-9926-8782bf1e9b03)
Employee Registration Page
![Screenshot 2023-11-24 200213](https://github.com/Heartsx12/JobFinder/assets/120915164/b31ea8f9-422f-4282-a856-ed8aa68b649c)
Employers Registration Page
![Screenshot 2023-11-24 200224](https://github.com/Heartsx12/JobFinder/assets/120915164/e27a070a-b139-4eae-b2a0-dcd2437f4ada)
Wish List Page (Employee)
![Screenshot 2023-11-24 200636](https://github.com/Heartsx12/JobFinder/assets/120915164/d0d294ad-2b1d-4eb6-8f3e-347a47362dbb)
Applied Jobs Page (Employee)
![Screenshot 2023-11-24 200648](https://github.com/Heartsx12/JobFinder/assets/120915164/29c43313-347a-4ead-8d47-1a3900efabd5)
Dashboard Page (Employer)
![Screenshot 2023-11-24 200734](https://github.com/Heartsx12/JobFinder/assets/120915164/0f92111a-79c6-4936-8e8f-064e167d6ebf)
Applicants who Applied Jobs Page (Employer)
![Screenshot 2023-11-24 200745](https://github.com/Heartsx12/JobFinder/assets/120915164/88a45c23-56fa-4a23-af4c-e86b30cde950)
Login Page
![Screenshot 2023-11-24 212725](https://github.com/Heartsx12/JobFinder/assets/120915164/7f0693a5-6d09-40cd-a0cc-38c3e13f47ab)
Forgot Password Page
![Screenshot 2023-11-24 212747](https://github.com/Heartsx12/JobFinder/assets/120915164/45edaa8d-22fe-4da4-ab80-508f809c5b03)

## Local Environment Setup
#### Create a virtual environment:
```bash
# Using virtualenv
virtualenv virtualenv

# Using Python 3.8
python3.8 -m venv virtualenv
```
#### Activate the virtual environment:
```bash 
source virtualenv/bin/activate
```
#### Clone the repository and install the required packages:
```bash
pip install -r requirements.txt
```
## Running the Project
#### Collect Static (Optional)
```bash
Note: Only necessary when debug is False (in production mode).
python manage.py collectstatic
```
#### Create Initial Database:
```bash
python manage.py migrate
```
#### Run Server:
```bash
python manage.py runserver
```
#### Default Django Admin Credentials:
```bash
Email: MediCare
Password: MediCare
```
## Support the Project
If you find this project useful, show your support by starring it! 🌟
