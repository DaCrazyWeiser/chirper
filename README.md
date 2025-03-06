# CHIRPER
This project is a Social media messaging app similar to Twitter. On our app you will be able to do the following things:
1. Make a chirp that is up to 255 characters
2. Create and sign into an account
3. Like other peoples chirps
4. Reply to other chirps
5. Follow other users
6. create a unique profile

# USAGE
1. Download our code and install the following dependecies: Pillow
2. run the server using: `python manage.py runserver` or if running on a virutal enviorment you may need to run `uv run python manage.py runserver`
3. go to http://127.0.0.1:8000/
4. Chirp away

## Editing the database
If you want to edit the raw database or remove certain chirps using admin privileges to forcibly delete them from the database.
To do this you simply need to create a superuser in your terminal window using: `python manage.py createsuperuser`.
It will prompt you for a username and password so set these to something you remeber as you will need them to login
navigate to http://127.0.0.1:8000/admin/ on your browser.
Next login on this page:

![image](https://github.com/user-attachments/assets/91d7a7b7-7df9-42ba-9496-2f72c647f5df)

After you login you can add delete or manage any of your tables:

![image](https://github.com/user-attachments/assets/512865b7-3b84-47a8-a00b-9ca123f43083)

# Contact Us
If you have an issue with your code just submit an issue and we will try to fix that as soon as we can otherwise you can reach out to us at:
- Noah Leeper: noah.leeper@student.cune.edu
- Ethan L'Heureux: ethan.lheureux@student.cune.edu
- Isaac Dawson: isaac.dawson@student.cune.edu

# Work Distribution
- Ethan L'Heureux: Wrote the entire front end html and some of the form stuff to help work on comments. Did all the buttons on the front end and wrote some views.
- Noah Leeper: Wrote backend models tried to help figure out how the database stores comments and also the README.
- Isaac Dawson: Wrote some forms
