# Gym Website


![Main image](documentation/home_header.png)

Admin login Information:

        Username: admin
        password: admin


Welcome to our Gym Website! This platform is designed to provide a seamless experience for both members and staff, offering a range of features to enhance your fitness journey. Whether you're a fitness enthusiast looking for classes or a staff member managing the gym operations, this platform has you covered. make this a bit longer.

## How this website will be used and future development for this project

### Membership Process:
User Registration:

Users can register on the website, providing necessary details to create an account.
Membership Activation:

Only staff members have the authority to create user profiles with memberships.
This typically happens when a user physically attends the gym, completes the required paperwork, and makes a payment.
Choosing Memberships:

During the physical registration process, users can pick the membership plan that suits them best.
### Future Features:

In future updates, we plan to introduce online payment methods, providing users with the convenience of selecting a membership and making payments directly on the website. This streamlined process will automatically create a user profile with an active membership.

Our goal is to enhance the user experience, making it easier for members to manage their memberships and enjoy the full range of classes offered by the gym 
## UX

This website is designed to be user-friendly for both staff and members. Members can easily browse, book, and cancel classes, as well as access detailed information about instructors to find the best fit for their needs. On the staff side, the interface allows seamless editing of user information, creation of user and instructor profiles, and addition of new classes. The straightforward design ensures a smooth experience for both users and staff, emphasizing simplicity and functionality.

### Target Audience

This website is meant for fitness enthusiasts of all levels, seeking a convenient and engaging platform to enhance their fitness journey. Members who value ease of use, accessibility, and a variety of class options will find our website tailored to their preferences. Whether you're a beginner exploring fitness classes or an experienced gym-goer looking for specific instructors, our platform caters to a diverse range of needs.



## Technologies Used

- ### Languages:

    - [Python 3.9.5](https://www.python.org/downloads/release/python-395/): The primary language used to develop the server-side of the website.
    - [JS](https://www.javascript.com/): The primary language used to develop interactive components of the website.
    - [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML): The markup language used to create the website.
    - [CSS](https://developer.mozilla.org/en-US/docs/Web/css): The styling language used to style the website.

- ### Frameworks and libraries:

    - [Django](https://www.djangoproject.com/): python framework used to create all the logic.
    - [Bootstrap](https://getbootstrap.com/): Bootstrap framework used is a css framework developing responsive and mobile-first websites.
    - [Pillow](https://pypi.org/project/pillow/): Pillow is used for processing images.


- ### Other tools:

    - [Git](https://git-scm.com/): The version control system used to manage the code.
    - [Pip3](https://pypi.org/project/pip/): the package manager used to install the dependencies.
    - [Gunicorn](https://gunicorn.org/): The web server used to run the website.
    - [Psycopg2](https://www.psycopg.org/): The database driver used to connect to the database.
    - [Django-allauth](https://django-allauth.readthedocs.io/en/latest/): The authentication library used to create the user accounts.
    - [GitHub](https://github.com/): Used to host the website's source code.
    - [VSCode](https://code.visualstudio.com/): The IDE used to develop the website.
    - [Chrome DevTools](https://developer.chrome.com/docs/devtools/open/): was used to debug the website.
    - [Font Awesome](https://fontawesome.com/): was used to create the icons used in the website.
    - [W3C Validator](https://validator.w3.org/): was used to validate HTML5 code for the website.
    - [W3C CSS validator](https://jigsaw.w3.org/css-validator/): was used to validate CSS code for the website.
    - [JShint](https://jshint.com/): was used to validate JS code for the website.
    - [JShint](https://jshint.com/): was used to validate JS code for the website.


## Features (Regular User)

### Desktop

1. Landing page
    - When a first time user visits the website they will be welcomed with landing page which will have a nav bar which the user will be able to visit all the pages, login and sign up, testimonials and opening times.

    ![landing page](documentation/website_screenshots/landing_page.png)


2. Register
    - When a first time user clicks Register which is located in the 
    the nav bar they are redirected to the Register page 
    - The new user will then be able to input a username, email and password; then clicking the "Sign up" button to create the account.

    ![register page](documentation/website_screenshots/register.png)

3. Login

    - When a user already has an account they would click the login button which located in the nav bar they are then redirected to the login page.
    - The user then will be able to input there email and password then click login and if the information the user inputted is correct then they will be redirected to the home screen.
    - If the user inputted the wrong details they will be asked to input the email and password again.
    
    ![login page](documentation/website_screenshots/login.png)

4. Log Out 

    - When the user wants to log out of their account they would click the "Log Out" link in the nav bar they will be directed to the sign out page.

    ![LogOut page](documentation/website_screenshots/logout.png)

    - Once they are directed to the sign out page they would click the sign out button to confirm that they want to sign out. 

    - Once they click the sign out button they will directed back to the home page.

5. Instructors

    - Whether the user has an account or no account they will be able to access the instructor page by clicking the instructor tab in the nav bar which will redirect the user to the instructor page.
    - The instructor page has cards of all the instructor that are in the database displayed next to each other.
    - The cards contain an images of each instructor with their name, what they coach, and there certification.

    ![Instructor page](documentation/website_screenshots/instructors.png)

6. Classes
    - Whether the user has an account or no account they will be able to see all the classes the gym has to offer in a card layout.
    - The information in the cards for everyone who accesses the page will be an image of the class, description of the class, max capacity, room number and the specific coach that will be coaching the class.
    - Under the instructor text there will either be a text saying:
        - "you need to be logged in" if the user is not logged in.
        - "no membership" if the user has no membership.
        -"Join Class(button)"  if the user has a membership and the class is not full.
        - "class is full" if the the class is full
        - "Cancel Class(button)" if the user is a member and has joined a class he will be able to cancel the class.

    ![Classes page](documentation/website_screenshots/classes.png)


    - If the user has no membership it will show "No Membership" under the instructor

    ![No membership](documentation/website_screenshots/no_memberhsip.png)

    - If the user has a membership a "Join Class" button will appear 

    ![They have membership ](documentation/website_screenshots/member_join_class.png)


    - When user clicks join class They will be added to the class

    - When user wants to cancel class the button will turn red and have the text "cancel class"

    ![cancel class button](documentation/website_screenshots/cancel_class.png)

    - When the user clicks cancel class a pop will appear so the user can confirm the action

    ![Cancel Class pop up ](documentation/website_screenshots/cancel_class_pop.png)


    - Once the user confirms the action they will directed to a page showing the user that the action has been successful.


    ![Cancel Class Confirmation ](documentation/website_screenshots/cancel_class_confirmation.png)


7. Profile

    - When the user logs in to there account a profile tab will appear in the nav bar 
    - When the user clicks the profile tab they will be directed to a profile page where the user will be able to see:
        - The users Username.
        - The Users Membership.
        - The users Join Date.

    ![User profile information ](documentation/website_screenshots/user_profile_info.png)


## Features (Staff)

1. Staff Area

    - When the user who has staff access a staff tab will appear in the nav bar.

    ![Instructor page](documentation/website_screenshots/navbar_staff.png)

    - When the user clicks the staff area they will be redirected to the staff area page.

    ![Instructor page](documentation/website_screenshots/staff_area.png)

    - The staff area has 6 buttons:
        - 3 blue buttons which when clicked shows:
            - All the users.
            - All the classes.
            - All the instructors.
        - 3 green buttons which when clicked shows:
            - Create new instructor profile.
            - Create new user profile.
            - Create new class.


2. Show Users 

    - When the staff clicks the Show users button all the users will appear in a table with each user having their own row.

    ![Instructor page](documentation/website_screenshots/show_users.png)

    - Each row has this information about the user:

                - Username
                - Email
                - Registration Date
                - User Type

    ![Instructor page](documentation/website_screenshots/show_user_row.png)

    - Each row also has 5 different button:

                - Delete 
                - Edit Membership
                - Classes Joined 
                - Add To A Class
                - Edit User

    

    - Delete Button

        - When the staff clicks the delete button of a user a pop up will appear to confirm if the staff wants to delete the user.

        ![Instructor page](documentation/website_screenshots/delete_button.png)

         ![Instructor page](documentation/website_screenshots/delete_user_pop.png)


        - Once the staff confirms the deletion of the staff will be redirected to a confirmation page to let the staff know the user has been deleted successfully and a button to go back to the staff area.

        ![Instructor page](documentation/website_screenshots/delete_user_confirm.png)


    - Edit Membership

        - When the staff clicks edit membership they will be redirected to the edit membership page (only if the user has a user profile)

         ![Instructor page](documentation/website_screenshots/edit_memberhsip_button.png)

        ![Instructor page](documentation/website_screenshots/edit_membership.png)

        - The edit membership page will show the staff the current membership of the user and then a membership choice dropdown that will allow the staff to pick a new membership type for the user.

        - Once the staff clicks save changes they will be redirected to the confirmation page so the staff knows the membership has successfully been changed.

        ![membership edited confirm](documentation/website_screenshots/membership_edited_confirm.png)


    - Classes Joined

        - When the staff clicks the classes joined they will be redirected to classes user joined page where the staff will be able to see:


        ![Classes joined ](documentation/website_screenshots/classes_joined_button.png)

                - The classes the use joined.
                - The room number.

        ![classes joined table](documentation/website_screenshots/classes_joined_table.png)

    - Add To Class

        - When the user clicks the "Add to Class" button they will be directed to add user to class page.


        ![Instructor page](documentation/website_screenshots/add_to_class_button.png)

        ![Instructor page](documentation/website_screenshots/add_user_to_class.png)

        - Once they add a user to a class and click save changes they will be directed to a confirmation page.

        ![Instructor page](documentation/website_screenshots/add_user_to_class_confirm.png)
        



    - Edit User

        - When the user clicks the edit user they will be directed to a page where they will be able to update the users profile, the information they will be able to update information like:

        ![Instructor page](documentation/website_screenshots/edit_user_button.png)

                - Username
                - Email Address
                - First Name
                - Last Name 
        
        ![Instructor page](documentation/website_screenshots/edit_user_form.png)

        - Once the staff finished updating the users information they will click save changes and a pop up will appear for the staff member to confirm the save.

        ![Instructor page](documentation/website_screenshots/edit_user_popup.png)

        - Once clicked they will be be redirected to the confirmation page so the staff will be able to know that the change was successful.

        ![Instructor page](documentation/website_screenshots/edit_user_confirmation.png)

3. Show Classes

    - When the staff clicks the show class button a table will appear with each class in their own row; each row has three button:

            - Edit Class
            - Show Users
            - Delete Class

    ![Show Classes](documentation/website_screenshots/show_classes_.png)

    - Edit Class

        - When the staff member clicks the "Edit Class" button they will redirected to a page to update the class information; the information that will be able to edited will be:

        ![Edit Class button](documentation/website_screenshots/edit_class_button.png)


                - Class Name
                - Room Number
                - Description
                - Max Capacity
                - Class Image
                - Change
                - Instructors

        ![Edit Class form](documentation/website_screenshots/edit_class_form.png)

        - Once the staff is done updating the classes information they will click the "Edit The Class" button and will be presented with a pop up to confirm the staff wants to confirm this update.

        ![Edit class pop up](documentation/website_screenshots/edit_class_popup.png)

        - When the Staff confirms the update they will be redirected to a confirmation page.

        ![Edit class confirmation](documentation/website_screenshots/edit_class_confirmation.png)

    
    - Show Users

        - When the staff member clicks the "Show Users" button all the usernames who have joined the class will appear.

        ![Show User Button](documentation/website_screenshots/show_users_button.png)


        ![Show Users in class](documentation/website_screenshots/show_users_in_class.png)


    - Delete Class

        - When the user clicks the "Delete Class" button they will be presented with a pop up for the staff to confirm the action of deleting the class.

        ![Delete class button](documentation/website_screenshots/delete_class_button.png)

        ![Delete class pop up](documentation/website_screenshots/delete_class_pop_up.png)

        - Once the user deletes confirms the deletion they will be directed to the confirmation page.

        ![Instructor page](documentation/website_screenshots/delete_class_confirmation.png)

4. Show Instructors

    - When the staff clicks the "Show instructors" button a table with appear with all the instructor profiles that will be shown in the instructors page of the website.

    ![Instructor page](documentation/website_screenshots/show_instructors.png)



    - In each row there will be two buttons:


    ![Show instructor row](documentation/website_screenshots/show_instructor_row.png)

            - Edit Profile
            - Delete 
    
    - Edit Profile 

        ![edit_profile button](documentation/website_screenshots/edit_profile_button.png)

        - When the staff click edit profile they will be redirected to the the edit instructor profile page.

        ![Edit Profile Form](documentation/website_screenshots/edit_profile_form.png)

            - Specialization
            - Certification
            - Display name
            - Instructor image
            
        - Once the staff is happy with the changes and click save changes a pop up will appear for the staff to confirm the action.

         ![edit instructor popup](documentation/website_screenshots/edit_instructor_popup.png)

         - Once they staff confirms the action they will directed to a confirmation page.
        
        ![instructor profile edit confirmation](documentation/website_screenshots/instructor_profile_edit_confirmation.png)


    - Delete 

        ![Delete](documentation/website_screenshots/delete_button.png)

        - When the staff clicks the delete button a pop up will appear asking the staff if they want to go ahead with the deletion.

        ![Delete instructor popup](documentation/website_screenshots/delete_instructor_popup.png)

        - Once the staff confirms the deletion they will be directed to the confirmation page.

        ![Delete instructor confirmation](documentation/website_screenshots/delete_instructor_confirmatiion.png)
    

5. Create New Instructor Profile

    - When the staff clicks "Create New Instructor Profile" button they will be directed to a page with an empty form for the staff to fill in which will then appear in the instructor page of the website for everyone to see.

    ![Create new instructor button](documentation/website_screenshots/create_new_instructor_profile_button.png)

    ![Create new instructor form](documentation/website_screenshots/create_new_instructor_profile_form.png)

    - The information that the staff would need to fill in would be:

            - Instructor User
            - Specialization
            - Certification
            - Display Name
            - Instructor Image

    - Once the staff adds all the required information and clicks the "Create Profile" a pop up will appear asking the staff if they want to go ahead with creating the profile.

    ![Create new instructor profile pop up ](documentation/website_screenshots/create_instructor_profile_popup.png)

    
    - Once the staff confirms the creation of the profile they  will directed to a confirmation page to let the staff know that the new instructor profile has been successfully created.

    ![Create new instructor profile confirmation](documentation/website_screenshots/create_new_instructor_confirmation.png)  


6. Create New User profile

    - When the staff click the "Create New User Profile" button they will be directed to a page with an empty form for the staff to fill in to create a user profile for every user in order to be able to get a membership.

    ![Create new user profile button](documentation/website_screenshots/create_new_user_profile_button.png)

    ![Create new user profile confirmation](documentation/website_screenshots/create_new_user_profile_form.png)

    - The information that the staff would need to fill in would be: 
    
            - User
            - Membership Choices
            - Join Date
            - New Membership purchase

    - Once the staff adds all the required information and clicks the "Create Profile" button a pop up will appear asking the staff if they want to go ahead with creating the profile. 

    ![Create new user profile pop up](documentation/website_screenshots/create_new_user_profile_popup.png)
    
     - Once the staff confirms the creation of the profile they  will directed to a confirmation page to let the staff know that the new user profile has been successfully created.
    
    ![Instructor page](documentation/website_screenshots/create_new_user_profile_confirmation.png)


7. Create New Class

    - When the staff clicks "Create New Class" button they will directed to a page with an empty form for the staff to fill in. This will then to create a new class that will be visible in the classes page of the website.


    ![create new class button](documentation/website_screenshots/create_new_class_button.png)
    
    ![Create new class button](documentation/website_screenshots/create_new_class_form.png)

    - The information that the staff would need to fill in would be:

            - Class Name
            - Room number
            - Description
            - Max capacity
            - Class image
            - Instructors

    - Once the staff adds all the required information and clicks the "Create New Class" button a pop up will appear asking the staff if they want to go ahead with creating the profile. 

    ![Create new class pop up](documentation/website_screenshots/create_new_class_popup.png)

    - Once the staff adds all the required information and clicks "Create New Class" button they will be directed to a confirmation page to let the staff member knows that new class has been successfully been created.

    ![Instructor page](documentation/website_screenshots/create_new_class_confirmation.png)

---

## Design

- The design for our gym website, we have chosen a  combination of white and dark grey. This minimalist palette not only exudes elegance but also aligns seamlessly with the essence of our fitness platform.

White: The predominant use of white signifies purity, clarity, and a sense of openness. It reflects the clean and fresh environment one seeks in a fitness space, creating a visually appealing interface.

![White](documentation/white.png)

Dark Grey: The incorporation of dark grey adds depth and a touch of modernity. It provides a strong contrast to white, emphasizing essential elements and enhancing readability. Dark grey instills a sense of strength and stability, resonating with the robust nature of fitness.

![Grey](documentation/grey.png)

Together, this color scheme aims to create a user-friendly, sleek, and motivating atmosphere for our users, reinforcing the commitment to their health and well-being.

### Wire Frames

Home Page

![home page wire frames](documentation/wireframes/homepage.png)

Instructor Page 

![Instructor page wire frame](documentation/wireframes/instructors.png)

Classes Page

![Classes page wire frame](documentation/wireframes/classes.png)

Profile Page 

![Profile wire frame](documentation/wireframes/profile.png)

Staff Area Page

![Staff Area page wire frame](documentation/wireframes/staff_area.png)

---

## Agile Methodology

### GitHub Project Management

- GitHub Project Management was essential for overseeing the project's development. It enabled efficient task prioritization and tracking, making it a crucial tool for successfully managing the application's progress.

### Process of using Git Hub Project Management

    The Beginning of using GitHub Project Management before using the badges 

 ![GitHub Project Management](documentation/aglie/before_badges.png)

    After adding the badges

![GitHub Project Management](documentation/aglie/after_badges.png)

    Around half way through the project moving the task in Todo column to the Done column

![GitHub Project Management](documentation/aglie/mid_way.png)
 
    At the end when all the tasks are in Done column

![GitHub Project Management](documentation/aglie/done_tasks.png)


---

## Information Architecture

### Database

- The project is using PostgreSQL as the database engine.
- The specific PostgreSQL instance is hosted on ElephantSQL.
- The dj_database_url package is helping parse the DATABASE_URL from the environment variables.

## Entity-Relationship Diagram
   
![GitHub Project Management](documentation/erd.png)


## Data Modeling

### Gym Classes Model

| Name          | Database Key  | Field Type    | Validation       |
| ------------- | ------------- | ------------- | ---------------- |
| class_id      | class_id      | AutoField     | primary_key=True |
| class_name    | class_name    | CharField     | max_length=100   |
| room_number   | room_number   | CharField     | max_length=5     |
| description   | description   | TextField     | default="Your default description goes here"|
| max_capacity  | max_capacity  | IntegerField  |                  |
| users         | users         | ManyToManyField | User           |
| class_image   | class_image   | ImageField    | upload_to='class_images', null=True, blank=True |
| instructors   | instructors   | ManyToManyField | ManyToManyField |


### InstructorProfile Model

| Name          | Database Key  | Field Type    | Validation       |
| ------------- | ------------- | ------------- | ---------------- |
| instructor    | instructor  | OneToOneField    | User, on_delete=models.CASCADE |
| specialization | specialization  | CharField | max_length=50 |
| certification    | certification   | TextField  |       |
| display_name    | display_name   | CharField  | max_length=100, default='Default Display Name'  |
| instructor_image  | instructor_image   | ImageField          | upload_to='images/', null=True, blank=True   |


### MembershipType Model

| Name          | Database Key  | Field Type    | Validation       |
| ------------- | ------------- | ------------- | ---------------- |
| membership_type_id |  membership_type_id  | AutoField| primary_key=True |
| membership_type_name   | membership_type_name  | CharField  | max_length=100      |


### UserProfile Model

| Name          | Database Key  | Field Type    | Validation       |
| ------------- | ------------- | ------------- | ---------------- |
| user          | user          | OneToOneField     | User, on_delete=models.CASCADE |
| membership_choices     | membership_choices | CharField      | choices=MEMBERSHIP_CHOICES, default='None'         |
| join_date      | join_date     | DateField         | default=timezone.now   |
| new_membership_purchase | new_membership_purchase | BooleanField | default=False  |

---
# Testing

## Manual Testing

### User(Customer)
| Page    | User Actions           | Expected Results | Y/N |
|-------------|------------------------|------------------|------|
| Register     |                        |                  |      |
| 1           | Click on Register button | Redirection to Register page | Y |         
| 2   |  Click on sign in link                     | Redirects user to sign in page                |    Y  |
|  3    |  Input correct details (including email)  and click sign up                  |    Redirects user to home page since meaning user has made an account         |   Y   |
|   Log Out    |                         |                  |      |
|   1   |    User clicks the sign out button |       Redirects user sign out page |   Y   |
|   2  |        User click sign out button                 |     User gets signed out              |   Y   |
|   Log In   |                      |             |    Y  |
|   1   |      User clicks login button                   |   Redirects user to login  page                 |  Y    |
|   2   |       User inputs  information  and clicks sign in button               |       user is redirected to home page being logged in           |   Y   |
|    3  |      User input wrong information and clicks sign in                  |  Message appears letting user the information inputted is wrong        |  Y    |
|   4   |         clicks text link in the sign in page                | Redirects user to sign in page                |    Y  |
|  Home page    |                        |                  |      |
|   1   |       Click explore classes button in hero section            |    Redirects user to classes page              |   Y   |
|    NavBar(Not Staff)  |   |  |      |
|   1   |   Click Home button     |  Redirects user to home page                |   Y   |
|   2   |   Click Instructors button   |     Redirects user to     Instructors    page     |   Y   |
|   3   |  Click  Classes button                    |     Redirects user to classes page             |   Y   |
| 4     |    Click Profile button                    |   Redirects user to profile page               |  Y    |
|  Instructor Page    |                        |                  |      |
|   1   |  User goes to Instructor Page   |     Shows all information on instructors             |  Y    |
|  Classes Page(No Membership)    |                        |                  |      |
|    1  | User goes to classes page                        |  Shows all information on classes                |   Y   |
|   2   |   User has no membership                     |  No Membership appears in bold at the bottom of the each card            |  Y    |
|   Classes Page(Has Membership)   |                        |                  |      |
|  1    |     User has membership                 |    Instead of "No membership" a button with the text "Join Class" will show              |    Y  |
|  2    | User clicks join class                       |  Pop up appears asking the user to confirm the joining of class            |   Y   |
|   3   |   User clicks ok                     |   Redirects user to confirmation page               |   Y   |
|  4    |  User joined class and goes back to classes page                     |  The classes the user joined button turns into "Cancel Class" button              |    Y  |
|  5    |  User clicks "Cancel Class" Button"                     |    Pop up appears asking user to confirm the canceling of the class          |  Y    |
|   6   |   User clicks ok                      | Redirects user to confirmation page                 |   Y   |
|  7     |    user clicks "back to classes" button in confirmation page                |   Redirects user back to classes page               | Y     |
|  Profile Page    |                        |                  |      |
|  1    |   User goes to Profile page                    |   Users Information appears on the page                |  Y    |

### User(Staff)

| Page    | User Actions           | Expected Results | Y/N |
|-------------|------------------------|------------------|------|
| NavBar     |                        |                  |      |
| 1         | Staff has admin access | Staff button appears on NavBar | Y |         
|  2    |      Staff clicks staff button                  |     User is redirected to staff area page             |  Y    |
|   Show Users Button   |                        |                  |      |
|  1    | Staff clicks show user button                       |     All users appear in a table             |    Y  |
|   2   |      Staff clicks Delete button for one of the users             |   Pop up appears           |   Y   |
|  3    |     staff clicks "ok" in the pop up                   | User    redirected to confirmation page             |   Y   |
|   4   |    Staff clicks"back to staff area" button  in the confirmation page             |     Redirected to Staff area            | Y     |
|   5   |  Staff clicks "Edit Membership" Button                       |        Redirected to  edit membership page if user has a user profile |  Y    |
|    6   | Pick a different type of membership and click save changes   | Staff is redirected to membership changed confirmation page                  |    Y  |
|    7   |  Staff clicks "Back to staff area" button in confirmation page   |    Staff is redirected to staff area              |    Y |
|   8    |  Staff clicks "Classes Joined" button   | Staff is redirected to classes joined page where they can see all the classes the user specific user has joined                  |  Y   |
|   9   |  Click "Add To Class" Button    |  Staff is redirected to add to class page                |  Y    |
|    10     |  Pick a class for specific user to join and click "Add To Class" Button  | Staff is redirected to user added to class confirmation page               |  Y  |
|   11    |   Staff clicks "Back to staff area" button   |    Staff is redirected to staff area              |   Y   |
|    12   |   Staff clicks "Edit User" button  |  Staff is redirected to edit user page                |   Y   |
|   13    |  Staff adds information about  the user and click save changes   |      Pop up appears for the staff to confirm the action            |   Y    |
|   14    |  Staff clicks "ok"  |   Staff is redirected to user edited confirmation page               |  Y    |
|  15     |  Staff clicks "back to staff area" button   |   Staff is redirected back to the staff area               |   Y   |
|    Show Classes   |     |                  |      |
|     1  |  Staff clicks "Show classes button"   |   Classes table is displayed               |   Y   |
|   2    |  Staff clicks "Edit Class" Button   | Staff is redirected to edit class page                 |   Y   |
|     3  |  Staff updates Information and clicks "Edit Class" button   | Pop up appears for the staff to confirm the action   |   Y   |
|   4    |  Staff clicks "ok"  | staff is redirected to class edited confirmation page|   Y   |
| 5      |   Staff clicks "back to staff area" Button  |   Staff is redirected to staff area               |   Y   |
|   6    |   Staff Clicks "Show Users" button in the specific class row  |    Small table of users who has joined the class appears in that specific class row next to the "Show users" button      |   Y   |
|  7      |  Staff clicks "Delete Class" Button    |  Pop up appears for the staff to confirm the action               |  Y    |
|    8   |  Staff Clicks "ok"   |  Staff Iis redirected to class deleted confirmation page               |   Y   |
|    9   |  Staff Clicks "Back to staff area" in class deleted confirmation page   |   Staff is directed to the staff area               |   Y  |
|   Show Instructors    |     |                 |      |
|    1   |  Staff clicks "Show Instructors" button   |    Table of instructors is displayed            |  Y    |
|    2   |  Staff clicks "edit profile" button   |    Staff is redirected to edit instructor profile page            |    Y  |
|    3   |  Staff updates instructors profile and clicks save changes    |  Pop up appears for the staff to confirm the action              |    Y  |
|  4     | Staff clicks "ok"    |   Staff is redirected to instructor edited confirmation page              |    Y  |
|   5    |  Staff clicks "back to staff area" button   |    Staff is redirected to staff area   |  Y    |
|  Create New Instructor Profile     |     |                 |      |
|    1   |  Staff clicks "Create New Instructor Profile Button     |    Staff is redirected to          Create New instructor Profile page   |   Y   |
|   2    |  Staff Create a new instructor profile and clicks save changes  |   Pop up appears for the staff to confirm the action               |   Y   |
|    3   |  Staff Clicks "ok"   |  Staff is redirected to Instructor Profile Created confirmation page               |   Y   |
|    4  | Staff click "Back to staff area" button    |  Staff is redirected to staff area               |  Y    |
|     Create New User Profile  |     |                 |      |
|    1   |  Staff clicks "Create New User Profile"   |   Staff is directed to Create new user Profile Page              |   Y   |
|    2   |   Staff creates a new profile and clicks save changes  |    Pop up appears for the staff to confirm the action             |   Y   |
|   3    |  Staff clicks "ok"   |  Staff is redirected to user profile created confirmation page                |   Y   |
|     4  |  Staff clicks "Back To Staff Area" button   |   Staff is redirected by to the staff area              |   Y   |
|   Create New Class    |     |                 |      |
|    1   | Staff clicks "Create New Class" button    |   Staff is redirected to create new class page              |  Y    |
|   2    |  Staff creates new class and clicks "create new class" button  |   Pop up appears for the staff to confirm the action               | Y     |
|    3   |  Staff clicks "ok"   |  Staff is redirected to class created confirmation page               |    Y  |
|    4   |  Staff Click "Back to staff area" button    |    Staff is redirected back to staff area             |    Y  |



### User Stories Check

#### First Time Visitor

 |User Story    | 
|-------------|
| As a First Time Visitor, I want a straightforward and intuitive sign-up process to create my account on FlexGym. |
|  As a First Time Visitor, I want the option to explore the available classes without committing to a login. |
| As a First Time Visitor, I want to see a diverse range of classes with brief descriptions, so I can quickly identify those that match my interests. |
 | As a First Time Visitor, I want to be able to find the app useful, so that I can use it according to my needs. |
 | As a First Time Visitor, I want to learn more about the instructors, including their expertise and teaching styles, to make informed decisions about the classes I might join. |
 | As a First Time Visitor, I want to be able to see the list of products, so that I can learn the benefits of the app as a user. |
 | As a First Time Visitor, I want access to testimonials from previous learners to gain insights into their experiences and the value they derived from the classes. |
 | As a First Time Visitor, I want the website to provide clear navigation and a visually appealing layout to enhance my overall user experience. |

#### Regular User (Customer)

 |User Story    | 
|-------------|
 |As a regular user, I want a quick and secure login process to access my FlexGym account efficiently. |
| As a regular user, I want a easy way to see what classes i have joined. |
 |As a regular user, I want to be able to cancel any class that i have joined. |
 |As a regular user, I want a to confirm if i want to cancel my class or join the class so i wont be able to do it by mistake. |
 |As a regular user, I want to be able to see if the class if full. |
 |As a regular user, I want a to be able to see the room number and instructor for the class incase it changes. |


#### Admin(Staff)
|  User Story   | 
|-------------|
||As a Admin, I want to be able be able to delete Users. |
|As a Admin, I want to be able to edit the membership type of any user. |
|As a Admin, I want to be able to look at all the classes the user has joined. |
|As a Admin, I want to be able to edit the users profile, such as username, email and name. |
 |As a Admin, I Want to be to Add any user to any class,so that if a member asks (through email or reception desk) to be added to a class maybe because they have no access to the website, the admin will be able to. |
 |As a Admin, I want to be to edit any of classes, so that i can be able to update the class name, room number, description, max capacity, class image, and coach. |
 |As a Admin, I want to be able to look at all the users in each class, so that if member asks if they are enrolled into the class i would be able to check and confirm with them. |
 |As a Admin, I want to be able delete any of the classes, so that if the gym no longer has the class i can remove it from the website. |
 |As a Admin, I want to be able to edit the the profile of all instructor profiles, so that i can update the Specialization, Certification, Display name and Image. |
|As a Admin, I want to be able to delete any of the instructor profiles, so that if a instructor is no longer with the gym i can remove them from the website. |
 |As a Admin, I want to be able to create a new instructor profile to be added the website, so that when a new instructor join the gym i can add a instructor profile to the user account of the instructor to be displayed on the website. |
 |As a Admin, I want to be able to create a user profile for a user, so that when a user creates an account the admin will be able to add the users membership choice, join date and if its a new membership purchase when the new member speaks to the reception at the gym to pay(Until Future Development When user can pay online).|
 |As a Admin, I want to be able to create a new class, so that when the gym has a new class to offer i will be able to create a new class to be added to the website. 

All user stories has been accomplished for this project.


## Validation

- ### HTML

    - HTML validator was not working because of the django


- ### CSS Validation:
    No errors or warnings were found when passing through the official W3C jigsaw validator
    ![Css](documentation/css_test.png)

---

- ### JsHint
    No errors or warnings were found when passing through the official  JsHint validator



## Solved bugs 

    - When user has none membership join class btn was still showing.
    - Staff area edit instructor profile takes two clicks to work.
    - When user profile created membership choice empty needed to be none membership.

    

## Unsolved Bugs

    - The javascript file is not to working with the in the staff area section so i had to add the code to the staff area html and classes html to work.

    - The 404 and 500 page was was not working it kept giving and error stating "a server error occurred. please contact the administrator"


# Deployment

## Deployment instructions for the project


*Note:*

    - This project requires the installation of all requirements:
    - Open the terminal window and type

First step is to create a local copy of the GitHub repository by following one of these ways :

- Download the Zip file:

  1. Go to the Github repository for this project which is !
    [GitHub Project Management](documentation/deployment/github_repo.png)

  2. Click the Code button and download the ZIP file containing the project.
    ![GitHub Project Management](documentation/deployment/download_zip.png)

  3. Unzip the downloaded file and save it to a location on your computer.

- Clone the repository

    1. Open a code editor
    ![GitHub Project Management](documentation/deployment/open_vscode.png)

    2. Open a folder in VScode

    ![GitHub Project Management](documentation/deployment/open_folder.png)

    3. Open the terminal

    ![GitHub Project Management](documentation/deployment/open_terminal.png)

    4. Run the clone command

    git clone https://github.com/yousefalm1/gym_management

    ![GitHub Project Management](documentation/deployment/run_clone_command.png)

    5. Navigate to the Cloned Repository:

    cd gym_management

    ![Navigate to Repo](documentation/deployment/navigate_repo.png)

   

## Local Deployment

1. Clone the repository.

    - ```git clone https://github.com/yousefalm1/gym_management```

        ![clone Repo](documentation/deployment/run_clone_command.png)

2.  2. Go to the ```gym_management``` directory.

    - ```cd gym_management```

        ![Navigate to Repo](documentation/deployment/navigate_repo.png)

3. Create a virtual environment.

    - ```python3 -m venv venv```

        ![Create Virtual Environment](documentation/deployment/create_virtual.png)

    - ```source venv/bin/activate```

        ![Activate Virtual Environment](documentation/deployment/activate_virtual_env.png)

4. Install Dependencies

    - ```pip install -r requirements.txt```

        ![Install all dependencies](documentation/deployment/install_dependencies.png)


5. Create an env.py File

    - ```touch env.py```

        ![Create env file](documentation/deployment/create_env_file.png)

6. Add the following lines to ```env.py```:

    - ```import os ```
    - ```os.environ.setdefault("DATABASE_URL",  "postgres://ehdeynzy:jdfrGgSKurLeCnfJoRUgUs7a5gqkO28L@flora.db.elephantsql.com/ehdeynzy")```

    ![Add to env file](documentation/deployment/add_to_env.png)

 7. Create Database Tables

    - ```python manage.py makemigrations```

    - This command will analyze your Django models and create migration files in the migrations directory.

    ![Create Database Tables](documentation/deployment/create_database_tables.png)

8. Apply Migrations

    - ```python manage.py migrate```

    ![apply migrations](documentation/deployment/apply_migrations.png)

    - This command will execute the SQL statements defined in the migration files and create the necessary tables in your database.



9. Create a Superuser

    - ```python manage.py createsuperuser```

    ![Create super user](documentation/deployment/create_super_user.png)

10. Run the Development Server

    - ```python manage.py runserver```

    ![Run server](documentation/deployment/run_server.png)

11. Access the website by the link provided in terminal. Add ```/admin/``` at the end of the link to access the admin panel.

    ![Admin Panel](documentation/deployment/run_server.png)

## Heroku Deployment

1. Create a Heroku account if you don't already have one.

2. Create a new app on Heroku.

    - Click the "New" button.
        ![New button](documentation/deployment/click_new.png)

    - Click on the "Create new app" button.
        ![create app](documentation/deployment/click_create_new_app.png)

    - Choose a name for your app and region.
     ![pick name and region](documentation/deployment/choose_name.png)

     - Click on the "Create app" button.

     ![click create app](documentation/deployment/click_create_app.png)

3. Go to settings tab

    ![settings on heroku](documentation/deployment/heroku_settings.png)

4. click revel config vars and add these vars make sure to make debug false when done.

    ![Add vars](documentation/deployment/config_vars.png)    



### Create Database on ElephantSQL

1. Go to [ElephantSQL](https://www.elephantsql.com/) and create a new account or login.

2. Create a new instance of the database.

    ![Create a new instance ](documentation/deployment/create_new_instance.png)

3. Create name and select the free plan named tiny turtle.

    ![select name and plan](documentation/deployment/select_name_and_plan.png)

4. Click "Select Region"

    ![select region ](documentation/deployment/select_region.png)

5. Choose a region near you

    ![choose a region ](documentation/deployment/pick_region.png)

6. Click "Review"

    ![review button](documentation/deployment/click_review_button.png)
    

7. Click "Create Instance"

    ![Create instance](documentation/deployment/create_instance.png)



8. Click the name of the the database

    ![Click name](documentation/deployment/click_databse.png)


9. Once clicked you will see all the information of the database, in order to connect the project to this database.

---

## Credits

    Bootstrap
    Django
    Github
    Unsplash
    heroku
    ElephantSQL

    Used this for hero section https://library.livecanvas.com/sections/hero-with-glassmorphism/
    Used this to help with loops thttps://stackoverflow.com/questions/6998366/django-templates-forloop-first-and-forloop-last




---

### Acknowledgments

I extend heartfelt gratitude to my mentor, Julia, for their invaluable guidance and unwavering support. Their mentorship has been a catalyst for my growth, both professionally and personally. I appreciate the wisdom, encouragement, and inspiration they have shared, making this journey an enriching experience.


























    



















    















      

























