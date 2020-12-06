# Teal CRM
Teal CRM is a CRM made in Django. It has a teal color Dashboard.
A Django CRM in which you can create, update or delete Product, Orders and Contacts. You can also filter and search. You can also add task for reminder.

+  Create, update or delete Product, Orders and Contacts.
+  Search and filter.
+  Add todo tasks for reminder.

### Screenshots

<table>
  <tr>
  <td align="center">
      <a href="https://raw.githubusercontent.com/masoodmomin/teal-crm/main/screenshots/login.png">
        <img src="screenshots/login.png" alt="Login Page">
      </a>
      <br />
      <p>Login Page</p>
    </td>
    <td align="center">
      <a href="https://raw.githubusercontent.com/masoodmomin/teal-crm/main/screenshots/dashboard.png">
        <img src="screenshots/dashboard.png" alt="Dashboard">
      </a>
      <br />
      <p>Dashboard</p>
    </td>
    <td align="center">
      <a href="https://raw.githubusercontent.com/masoodmomin/teal-crm/main/screenshots/contacts.png">
        <img src="screenshots/contacts.png" alt="Contacts">
      </a>
      <br />
      <p>Contacts</p>
    </td>
    <td align="center">
      <a href="https://raw.githubusercontent.com/masoodmomin/teal-crm/main/screenshots/product.png">
        <img src="screenshots/product.png" alt="Products">
      </a>
      <br />
      <p>Products</p>
    </td>
    <td align="center">
      <a href="https://raw.githubusercontent.com/masoodmomin/teal-crm/main/screenshots/tasks.png">
        <img src="screenshots/tasks.png" alt="Tasks">
      </a>
      <br />
      <p>Tasks</p>
    </td>
    </tr>
</table>

### Clone this repository

```
git clone https://github.com/masoodmomin/teal-crm.git
```

### Dependencies
```
django-filter=2.4.0
```
### Run the following commands to get started:

```
pip install django django-filter
python manage.py makemigrations crm tasks
python manage.py migrate
python manage.py runserver
```
