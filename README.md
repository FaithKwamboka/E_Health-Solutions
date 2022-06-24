## E-Health Solutions

## Built by:
* Faith Okong'o
* Vonetta Orinda
* Susan Mageto
* Florence Wangechi

## Appearance

* Landing Page
![Homepage](/static/images/landingpage.png)

* Admin Dashboard
![Admin Dashboard](/static/images/admindash.png)

* Doctor Dashboard
![Admin Dashboard](/static/images/doctordash.png)



### Description
E-Health is a web application health management system that unifies the patient-doctor interactions by providing seamless flow of information and data across board.


### Technology Used

The following languages have been used on this project:

- HTML
- CSS
- Bootstrap
- Python
- Django
- PostgreSQL



- Live link to view the project <a target="_blank" href="https://ehealthsolutions.herokuapp.com/">E-Health Solutions</a>


### User Stories
These are the behaviours/features that the application implements for use by a user.
### Admin Abilities
These are the behaviours/features that the application implements for use by the admin.

Admin should:
* Sign in to the application
* Approve Doctors and Patients to the system.
* Create Appointments for patients.
* Delete, reject and revoke doctors and patients from the system.
* Discharge patients.
* Manage the entire.


Doctors should:
* Sign-up to the system and await approval.
* Login to the dashboard view appointments and assigned patients records and discharge status.

Patients should:
* Sign-up to the system and await approval.
* Login to the dashboard view appointments and.




### Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Admin Authentication | **Home Page** | Access Admin dashboard |
| Doctor Authentication| **Home page** | Access Doctor Dashboard |
| Patient Authentication| **Home page** | Access Patient Dashboard |
| To approve doctors and patients  | **Through Admin dashboard** | Redirected relevant approval page for approval |
| To add doctor or patiens | **Through Admin dashboard and** | Redirected to the add new doctors and admit new |
| To Discharge patients | **Through Admin Dashboard** | Admin discharges admitted patiens|


### Setup Installation

- Copy the github repository url
- Clone to your computer
- Open terminal and navigate to the directory of the project you just cloned to your computer
- Run the following command to start the server using virtual environment

```
python3 -m venv --without-pip virtual
```

- To activate the virtual environment

```
source virtual/bin/activate
```
```
pip install -r requirements.txt
```

- Edit the .env file and replace the values with your own Cloudinary credentials and database credentials

- To run the server

```
python manage.py runserver

```

- Open the browser and navigate to http://127.0.0.1:8000/ to see the application in action


Copyright (c) [2022] E-Health Solutions.

 

