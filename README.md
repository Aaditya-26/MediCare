# MediCare

MediCare is a web-based healthcare platform that aims to provide a centralized system for managing healthcare services across multiple hospitals. The platform has different modules for different types of users, such as patients, doctors, hospital administrators, lab workers, and pharmacists. The platform allows users to perform various tasks related to their healthcare needs, such as accessing information, booking appointments, purchasing medicines, paying for tests, and communicating with each other. The platform also allows users to access and share their health records with other authorized users, such as doctors or pharmacists. This way, the platform helps users to manage their healthcare needs more easily and conveniently, while also reducing the workload and costs for healthcare providers.

## Screenshots
Home Page
![image](https://github.com/Aaditya-26/MediCare/assets/120915164/21c51444-b183-434c-8951-b85308d1c9e2)
Login Page (Patient)
![image](https://github.com/Aaditya-26/MediCare/assets/120915164/a10f66ff-22c7-46d5-ab60-ba49502a453e)
Registration Page (Doctor)
![image](https://github.com/Aaditya-26/MediCare/assets/120915164/172f62d9-fce1-4127-b8bb-dcef3120591a)
Hospital Administrator Login Page
![image](https://github.com/Aaditya-26/MediCare/assets/120915164/a4abefa6-a4d0-4f2a-8f9d-dc09d6c8cd4e)
Hospital Administrator Registration Page
![image](https://github.com/Aaditya-26/MediCare/assets/120915164/988b3b2f-3d78-4469-8c1c-fcc05cc4aa6e)
Dashboard Page (Patient)
![image](https://github.com/Aaditya-26/MediCare/assets/120915164/a4e3bccb-b06a-48c4-bbfd-29987ef3b597)
Medical Shop Page
![image](https://github.com/Aaditya-26/MediCare/assets/120915164/c96136f6-3399-4654-b0cb-49b0be406a2f)
Profile Page (Doctor)
![image](https://github.com/Aaditya-26/MediCare/assets/120915164/e7cdaaba-191b-458b-9d64-bc43ecd5e0c5)
Chat Page (Doctor)
![image](https://github.com/Aaditya-26/MediCare/assets/120915164/4a8210c5-c060-4e71-bdca-89f45bebd9fc)
Hospital Administrator Dashboard Page
![image](https://github.com/Aaditya-26/MediCare/assets/120915164/1b5aaca0-17ee-415b-9eeb-ef2462ba1294)

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
python manage.py makemigrations
python manage.py migrate
```
#### Run Server:
```bash
python manage.py runserver
```
#### Default Django Admin Credentials:
```bash
Username: MediCare
Password: MediCare
```
## Support the Project
If you find this project useful, show your support by starring it! 🌟
