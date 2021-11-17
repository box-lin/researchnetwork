# Design Document

## Research Network Platform 
--------
Prepared by:

* `<Yi Chou>`
* `<Boxiang Lin>`
* `<Shutian Wang>`
* `<Wanting Wu>`

---

**Course** : CptS 322 - Software Engineering Principles I

**Instructor**: Sakire Arslan Ay

---

## Table of Contents
- [Design Document](#design-document)
  - [Research Network Platform](#research-network-platform)
  - [Table of Contents](#table-of-contents)
  - [Document Revision History](#document-revision-history)
- [1. Introduction](#1-introduction)
- [2.	Architectural and Component-level Design](#2architectural-and-component-level-design)
  - [2.1 System Structure](#21-system-structure)
  - [2.2 Subsystem Design](#22-subsystem-design)
    - [2.2.1 Model](#221-model)
    - [2.2.2 Controller](#222-controller)
    - [2.2.3 View and User Interface Design](#223-view-and-user-interface-design)
- [3. Progress Report](#3-progress-report)
- [4. Testing Plan](#4-testing-plan)
- [5. References](#5-references)
- [Appendix: Grading Rubric](#appendix-grading-rubric)

<a name="revision-history"> </a>

## Document Revision History

| Name | Date | Changes | Version |
| ------ | ------ | --------- | --------- |
|Revision 1 |2021-10-27 |Initial draft | 1.0        |
|      |      |         |         |
|      |      |         |         |

# 1. Introduction

**Iteration 1:**

The purpose of the Software Design Document is to provide a description of the design of a system fully enough to allow for software development to proceed with an understanding of what is to be built and how it is expected to built. The Software Design Document provides information necessary to provide description of the details for the software and system to be built.

The project is to built a platform for the students and the faculty members in WSU. The Goal of this project is to provides smooth connections to research opportunities for students. professors or faculties can present their research opportunities on this platform. Students will be able to apply see all currently available research opportunities and be able to apply for them.

Overview of the document outlie: First, System Structure will talk about the major subsystem and how they fit together. Second, Subsystem design will talk about how are we going to design Model, Controller and View subsystems. Third, we will have a program progress section, when we finish one iteration we will update the what did we finish in the iteration. This will help us keep in track of our project. Last, we will have a testing part for the document. We will planning how to test each iteration on this part.



# 2.	Architectural and Component-level Design
## 2.1 System Structure

**Iteration 1 section (MVC Pattern):**

 * Provide a UML component diagram that illustrates the architecture of your software.

   ![](https://github.com/boxianglin/Storage/blob/main/ResearchNetworkImages/UMLite1.drawio.png?raw=true)

 * **Model:** The component that responsible for types of object (data in certain category) will be stored in the database. In our first iteration we need data for User and data for Research Position Post. 

   **View:** The component that responsible for graphical outputs. Triggered by the routes and does also redirect to the routes (as needed). In our MVC, htmls are mainly to render the FlaskForm attributes. We does also set the redirect to `routes.delete` in _post.html to enable a button for faculty to delete their research position post.

   **Controller:** The component that responsible for the operations on database and serve as a transition in between Model and View component. In this Controller, the Flaskform serve as a container that provided a space to receive inputs in HTML stage; route hence retrieve those inputs from Flaskform and do the operations to the database.

 * **Intention:** Cohesion represents the functional strength of modules and coupling represents the independence among modules. So our goal is to make the system have a strong functional strength and also make sure between each strong functional strength modules they have enough independence.

 * **Conclusion:** Hence a Controller component that contains FlaskForm and Flask Route is very cohesive, since they are highly related and being use interchangeably; Letting htmls in View component and db.Models in Models component bringing us a low coupling structure, so that changes in one component does not really gonna influences the other.

## 2.2 Subsystem Design 

(Note: This is just a suggested template. If you adopted a pattern other than MVC, you should revise this template and the list the major subsystems in your architectural design.)

### 2.2.1 Model

|                     | Table 1                                           |                                                   |      |      |
| ------------------- | ------------------------------------------------- | ------------------------------------------------- | ---- | ---- |
| Name:               | User                                              |                                                   |      |      |
| Role:               | *Store user infomation, both student and faculty* |                                                   |      |      |
|                     | *Table contain follow columns:*                   |                                                   |      |      |
| id                  | Integer, primary_key                              | User ID                                           |      |      |
| username            | String(64), unique, index                         | Username                                          |      |      |
| password_hash       | String(128)                                       | Hashed password                                   |      |      |
| lastname            | String(20)                                        | User lastname                                     |      |      |
| firstname           | String(30)                                        | User firstname                                    |      |      |
| wsuid               | Integer, unique                                   | User WSUID                                        |      |      |
| phone               | String(20)                                        | User phone number                                 |      |      |
| email               | String(120), unique, index                        | User email address                                |      |      |
| major               | String(20)                                        | Student major                                     |      |      |
| GPA                 | String(5)                                         | Student GPA                                       |      |      |
| gradulationdate     | String(10)                                        | Student graduate date                             |      |      |
| elective            | String(300)                                       | Student elective class                            |      |      |
| researchtopic       | String(30)                                        | Student interested research topic                 |      |      |
| office              | String(1024)                                      | Office Location                                   |      |      |
| research_experience | String(200)                                       | Student Research Experience                       |      |      |
| usertype            | Integer                                           | Determine User Type: 0 for student, 1 for faculty |      |      |
| elective            | relationship                                      | Retrieve StudentElectives Associate Table         |      |      |
| researchtopic       | relationship                                      | Retrieve ResearchTopics Associate Table           |      |      |
| programming         | relationship                                      | Retrieve ProgrammingLanaguages Associate Table    |      |      |
| repr                | method                                            | Use to Print Information                          |      |      |
| set_password        | method                                            | Generate Password                                 |      |      |
| get_password        | method                                            | Check Password                                    |      |      |
| is_student          | method                                            | Check User Type                                   |      |      |
| is_faculty          | method                                            | Check User Type                                   |      |      |
| is_applied          | method                                            | Check Application Status                          |      |      |
| apply               | method                                            | Use to Apply Application                          |      |      |
| withdraw            | method                                            | User to Withdraw Application                      |      |      |
| get_faculty_posts   | method                                            | Return Post Position                              |      |      |
| get_electives       | method                                            | Return User Elective                              |      |      |
| get_researchtopic   | method                                            | Return Research Topic                             |      |      |
| get_programming     | method                                            | Return Programming Language                       |      |      |

|                         | Table 2                               |                                      |      |      |
| ----------------------- | ------------------------------------- | ------------------------------------ | ---- | ---- |
| Name:                   | Position                              |                                      |      |      |
| Role:                   | *Store Research Position Information* |                                      |      |      |
|                         | *Table contain follow columns:*       |                                      |      |      |
| id                      | Integer, primary_key                  | Position ID                          |      |      |
| title                   | String(2048)                          | Position title                       |      |      |
| desc                    | String(2048)                          | Position description                 |      |      |
| start_date              | String(128)                           | Position start date                  |      |      |
| end_date                | String(128)                           | Position end date                    |      |      |
| time_commitment         | String(128)                           | Time commitment                      |      |      |
| research_field          | String(128)                           | Research field this position related |      |      |
| applicant_qualification | String(1024)                          | User email address                   |      |      |
| user_id                 | Integer                               | User assigned to this position       |      |      |
| roster                  | Relationship                          | User retrieved applied application   |      |      |

|                    | Table 3                                        |                         |
| :----------------- | ---------------------------------------------- | ----------------------- |
| Name               | Apply                                          |                         |
| Role               | *Association Object between User and Position* |                         |
|                    | *Table contain follow columns:*                |                         |
| studentid          | Integer                                        | User ID                 |
| positionid         | Integer                                        | Position ID             |
| applydate          | DateTime                                       | Apply Date              |
| status             | Integer                                        | Application Status      |
| studentapplied     | Relationship                                   | Retrieved User Data     |
| applicationapplied | Relationship                                   | Retrieved Position Data |
|                    |                                                |                         |

|      | Table 4                                   |      |
| ---- | ----------------------------------------- | ---- |
| Name | ResearchTopics                            |      |
| Role | Associate Table for Reasearch Topic       |      |
| Name | TechnicalElectives                        |      |
| Role | Associate Table for Technical Electives   |      |
| Name | ProgrammingLanguages                      |      |
| Role | Associate Table for Programming Languages |      |



### 2.2.2 Controller

|      | Methods   | URL Path             | Description                                          |
| :--- | :-------- | :------------------- | :--------------------------------------------------- |
| 1.   | GET       | faculty_index        | Retrieve all research position for faculty to manage |
| 2.   | GET       | student_index        | Retrieve all research position for student to apply  |
| 3.   | GET, POST | newPost              | Faculty create new position                          |
| 4.   | GET, POST | delete/<position_id> | Faculty delete created position                      |
| 5.   | GET, POST | login                | Let user login the system                            |
| 6.   | GET       | logout               | Let user logout the system                           |
| 7.   | GET, POST | faculty_register     | Let faculty register into the system                 |
| 8.   | GET, POST | student_register     | Let student register into the system                 |
| 9.   | GET, POST | register             | Let user register into the system                    |

### 2.2.3 View and User Interface Design

**Iteration 1:**

In this iteration user interfaces of `1. login`, `2. student registration and 3. faculty registration`,`4 Faculty Homepage and 5 Faculty Delete Post`, `6. Faculty Post Position`, and `7. Student homepage` have been implemented. We use generic HTML CSS to custom the style and layout for the Flaskform element generated by the Jinjia Template engine.

- **User interface for `1. Login`:**

  1. Use case #2 with additional use case #14 in iteration 2
  2. This is a generic login page, user types their username and password and selects the corresponding role they are to log in. If the role does not matches, will pop a message with an invalid username or password.

  <img src="https://github.com/wantingw/Storage/blob/master/Screen%20Shot%202021-11-16%20at%2012.03.18%20AM.png?raw=true" style="zoom:67%;" />

- **User interface for `2. student registration and 3. faculty registration`:**

  1. Use case #1 with additional use case #12 in iteration 2
  2. Both student and faculty registrations are shown in this route, we added a JavaScript function to dynamically show the corresponding student flaskform and faculty flaskform whenever the radio button get selected.

  <img src="https://github.com/wantingw/Storage/blob/master/Screen%20Shot%202021-11-16%20at%2012.07.42%20AM.png?raw=true" alt="img" style="zoom: 87%;" />

- **User Interface` 4 Faculty Homepage and 5 Faculty Delete Post`**

  1. Use case #5
  2. The home page will display all the research positions. Faculty can only delete their own post.

  [![img](https://github.com/boxianglin/Storage/raw/main/ResearchNetworkImages/faculty_homepage.png?raw=true)](https://github.com/boxianglin/Storage/blob/main/ResearchNetworkImages/faculty_homepage.png?raw=true)

- **User interface `6. Faculty Post Position`:**

  1. Use case #4
  2. This route will be called when faculty click the "Post New Position". Faculty can fill the research position formation. These information will add into the database and display in the Homepage.

  [![img](https://github.com/boxianglin/Storage/raw/main/ResearchNetworkImages/faculty_post.png?raw=true)](https://github.com/boxianglin/Storage/blob/main/ResearchNetworkImages/faculty_post.png?raw=true)

- **User interface `7.student homepage`**

  1. Student Homepage corresponding to the `Use Case #7` in **Iteration 2**, we structure it in advance but more styling work will be perform in Iteration 2.

  [![img](https://github.com/boxianglin/Storage/raw/main/ResearchNetworkImages/student_homepage.png?raw=true)](https://github.com/boxianglin/Storage/blob/main/ResearchNetworkImages/student_homepage.png?raw=true)

# 3. Progress Report

In iteration 1, we implement the basic features of the platform: create an account, log in, log out, post the research position, and delete the position post. The Users can create an account and assign it as Faculty or Student. The Student User can log into the student page and view all the posted research positions. The Faculty Users can log into the faculty page and post the research position by entering detailed descriptions. The research position posts can be deleted by the poster faculty user. 

# 4. Testing Plan

(***in iteration 1***)
Don't include this section.

(***in iteration 2***)
  * *Unit Testing*: Explain for what modules you plan to write unit tests, and what framework you plan to use.  (Each team should write automated tests (at least) for testing the API routes)
  * *Functional Testing*: How will you test your system to verify that the use cases are implemented correctly? (Manual tests are OK)
  * *UI Testing*: How do you plan to test the user interface?  (Manual tests are OK)

Iteration 2 testing plan, to test the project we will be implementing a mix of manual and automatic testing. For model.py we can write automated tests but it is optional, and we will also test API routes using automates testing except login and register routes. we will implement test cases that are fail and succeed to make sure the surve is responding correctly to the request. we will try to test login and register routes manually and we already finish testing login and register routes is working completely, we try plenty cases to make sure it actually work. For the rest of the routes we will write the tests and test it. we will test functionality manually, we will go through the use cases we write and check it one by one make sure it is operating as expected and do not crash the system when user have some extraordinary behavior. we will also test the user interface manually, to make sure it can display information correctly and trying to make it look more beautiful and simple because we do not want to misleading user. for the user interface we already finish testing so far and it displaying information correctly.



# 5. References

N/A


----
# Appendix: Grading Rubric

