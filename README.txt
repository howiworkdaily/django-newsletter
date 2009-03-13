Django-Newsletter
=================

This is a simple newsletter opt-in/opt-out reusable application for your Django powered web app.

Many projects I develop need basic "newsletter" opt-in/out functionality on their site with the ability to export subscriptions to CSV files for uploading to newsletter management solutions like Campaign Monitor.

So instead of reinventing the wheel each time I've selected the features most share and created this reusable Django app. I also provided basic example app to get you started.

This app follows several "best practices" for reusable apps by allowing for template overrides and extra_context 
arguments and such.

This is not a newsletter mailing application. The Django-Mailer application is the one you're looking for if you need a mail queuing and management, and possible Django-Notification depending on your needs.

Features
===================

1. allow user to opt-in.
2. allow user to opt-out.
3. export subscribed users to a CSV file via the admin.

Installation
============

1. add 'newsletter' directory to your Python path.
2. add 'newsletter' to your INSTALLED_APPS tuple found in your settings file.
3. execute ./manage.py syncdb to created database tables
4. Log into your admin and enjoy!
5. To customize the templates add a "newsletter" directory to your project's templates dir.

Example Site
============

I included an example site in the /example directory. You should be able to
simply execute './manage.py syncdb' and then './manage.py runserver' and have
the example site up and running. I assume your system has sqlite3 available -
it is set as the default database with the DATABASE_NAME = 'dev.db'

1. From the repository root directory execute "cd example" to jump into the example dir.

2. Execute './manage.py syncdb' (This assumes that sqlite3 is available as it is set as the default database with th DATABASE_NAME = 'dev.db'.)

3. Executing '/manage.py loaddata fixtures/newsletter_initial.json' will load initial data for you for testing purposes.

4. Execute './manage.py runserver' and you will have the example site up and running. The home page will have links to get to the available views.

5. The admin is available at "/admin". Feel free to play around with it!
