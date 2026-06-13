CliniCata - Medical Appointment Management System

CliniCata is a modern web application designed to digitalize medical services, allowing patients to manage their doctor appointments in a secure, intuitive, and responsive environment. The project is built using the **Django** framework and is fully deployed in production on the **Railway** cloud platform, utilizing a **PostgreSQL** database and third-party cloud APIs for enhanced security and automated notifications.

Key Features

* **Advanced Authentication & Security:**
    * Full user registration and secure login flow for patients.
    * **Two-Factor Authentication (2FA):** Extra account protection using a Time-Based One-Time Password (TOTP) system compatible with mobile authenticator apps like Google Authenticator.
* **Medical Appointment System:**
    * Interactive directory of doctors displayed via modern UI cards, including profile pictures, professional descriptions, and specialties.
    * Real-time appointment booking with chosen medical specialists.
    * Comprehensive patient dashboard to view personal appointment history.
    * Instant appointment cancellation management.
* **Automated Email Notification System:**
    * Automated "Welcome Email" sent instantly upon successful account registration.
    * Confirmation emails containing full appointment details (date, time, and doctor) sent upon booking.
    * Immediate email alerts triggered automatically if an appointment is canceled.

 Technical Details & Architecture

###  Data Management & Password Security
The application relies on a robust **PostgreSQL** relational database hosted as a dedicated instance on **Railway**. 

Data security is a top priority; therefore, user passwords are **never stored in plain text**. Django utilizes a secure **Password Hashing** architecture. Upon registration, the plain-text password undergoes a one-way cryptographic hashing algorithm (specifically **PBKDF2 with a SHA-256 hash** and a unique per-user *salt*). This ensures that even in the unlikely event of unauthorized database access, the passwords cannot be reversed or decoded, maintaining absolute user privacy.

###  Email Infrastructure (Automated Notifications)
To guarantee lightning-fast email delivery and bypass spam filters, the application is integrated with the **Resend API**, a developer-focused transactional email service. Communication between the Django backend and Resend's servers is fully secured via production API keys, triggering dynamic HTML email templates (Welcome, Confirmation, and Cancellation) seamlessly through Django backend signals.

###  Deployment & Cloud Infrastructure
* **Hosting Platform:** Railway (PaaS).
* **Database:** PostgreSQL (Cloud Instance).
* **Domain:** Fully deployed with a custom domain name, making the application live and accessible from any smartphone, tablet, or desktop.

## Tech Stack

* **Backend:** Python 3.x, Django Framework
* **Security:** Django OTP / Formtools (2FA Core), PBKDF2 (Cryptographic Password Hashing)
* **Database:** PostgreSQL
* **External Services:** Resend API (Transactional Email Engine)
* **Frontend:** HTML5, CSS3, Bootstrap 5 (Modern & Fully Responsive Design)
* **Deployment:** Railway Cloud Infrastructure

## Images

**Home page**

Desktop

<img width="917" height="365" alt="image" src="https://github.com/user-attachments/assets/ae7cde23-eb4f-4268-9fb1-f0044803e97f" />
<img width="945" height="380" alt="image" src="https://github.com/user-attachments/assets/960057b6-ef0c-4dd6-8f46-d83448a0105c" />

Mobile

<img width="345" height="647" alt="image" src="https://github.com/user-attachments/assets/7fac52f5-dc52-4acb-bda0-4397efc9a42f" />
<img width="328" height="647" alt="image" src="https://github.com/user-attachments/assets/955e9734-e68b-4c73-b94e-1bc7796f3158" />

**Doctors list**

<img width="945" height="449" alt="image" src="https://github.com/user-attachments/assets/8cf835c0-998d-4325-b62b-7d950008753d" />

<img width="945" height="455" alt="image" src="https://github.com/user-attachments/assets/90310f46-06e7-460c-9f4d-7288dc37b783" />

**Login and register pages**

<img width="945" height="380" alt="image" src="https://github.com/user-attachments/assets/56cc1345-52b5-4635-af8d-c231f2f5eaf0" />
<img width="945" height="450" alt="image" src="https://github.com/user-attachments/assets/ee0c0c74-6e90-4431-b48a-9b7b2c923cd9" />

**Mail after register**

<img width="945" height="493" alt="image" src="https://github.com/user-attachments/assets/ca962439-cfec-45c3-9901-5bb3a3911a8a" />

**Apponintment system**

<img width="945" height="433" alt="image" src="https://github.com/user-attachments/assets/36f56a92-d71c-42fd-84b4-fefb0968694f" />

<img width="945" height="405" alt="image" src="https://github.com/user-attachments/assets/f4550462-79c1-453c-af27-0884776f912b" />

<img width="945" height="407" alt="image" src="https://github.com/user-attachments/assets/a601cf9a-0a3c-4995-92bd-46d342598179" />

<img width="923" height="436" alt="image" src="https://github.com/user-attachments/assets/bacb1345-57c5-4f7e-a769-df3077a06212" />

<img width="923" height="436" alt="image" src="https://github.com/user-attachments/assets/06b566d0-bd4d-4944-9878-ffec9b3e6ada" />

**2FA**

<img width="956" height="354" alt="image" src="https://github.com/user-attachments/assets/3cc6b59c-5283-4f88-b124-c5041a61b8f8" />

<img width="850" height="361" alt="image" src="https://github.com/user-attachments/assets/e8aeb2b2-504b-4ad3-bdd9-404cb53d95a9" />

<img width="883" height="343" alt="image" src="https://github.com/user-attachments/assets/f5a00df9-ad19-4a71-bbba-eacbc687a392" />

<img width="858" height="348" alt="image" src="https://github.com/user-attachments/assets/10f79aa6-68c7-4bc0-a371-22ae4703972b" />

<img width="945" height="451" alt="image" src="https://github.com/user-attachments/assets/ac68694f-475b-443d-b1b9-4865f843c974" />


















