# << Software Requirements Specification >>

## ResearchNetwork - Web App
--------
Prepared by:

* `Boxiang Lin` 
* `Shutian Wang` 
* `Yi Chou`
* `Wanting Wu`

---

**Course** : `CptS 322 - Software Engineering Principles I`

**Instructor**: `Sakire Arslan Ay`

---

## Table of Contents
- [Software Requirements Specification](#software-requirements-specification)
  - [ResearchNetwork](#ResearchNetwork)
  - [Table of Contents](#table-of-contents)
  - [Document Revision History](#document-revision-history)
- [1. Introduction](#1-introduction)
  - [1.1 Document Purpose](#11-document-purpose)
  - [1.2 Product Scope](#12-product-scope)
  - [1.3 Document Overview](#13-document-overview)
- [2. Requirements Specification](#2-requirements-specification)
  - [2.1 Customer, Users, and Stakeholders](#21-customer-users-and-stakeholders)
  - [2.2 Use Cases](#22-use-cases)
  - [2.3 Non-Functional Requirements](#23-non-functional-requirements)
- [3. User Interface](#3-user-interface)
- [4. References](#4-references)
- [Appendix: Grading Rubric](#appendix-grading-rubric)

<a name="revision-history"> </a>

## Document Revision History

| Name | Date | Changes | Version |
| ------ | ------ | --------- | --------- |
|Revision 1 |2021-10-05 |Initial draft | 1.0        |
|      |      |         |         |
|      |      |         |         |

----
# 1. Introduction

`ResearchNetwork` is a platform that provides smooth connections to research opportunities for students at Washington State University. Professors or faculties can present their research opportunities on this platform. Students will be able to see all currently available research opportunities and be able to apply for them. 

## 1.1 Document Purpose

Describe the purpose of the Software Requirement Specification (SRS) document and its intended audience.

## 1.2 Product Scope

Identify the product whose software requirements are specified in this document. Explain what the product that is covered by this SRS will do. Provide a short description of the software being specified and its purpose, including relevant benefits, objectives, and goals.

## 1.3 Document Overview

Describe what the rest of the document contains and how it is organized.

----
# 2. Requirements Specification

This section specifies the software product's requirements. Specify all of the software requirements to a level of detail sufficient to enable designers to design a software system to satisfy those requirements, and to enable testers to test that the software system satisfies those requirements.

## 2.1 Customer, Users, and Stakeholders

People that will use this platform are  `Faculty Members (Research Assistant, Professors, etc)` and `Students` from Washington State University. 


----
## 2.2 Use Cases

This section will include the specification for your project in the form of use cases. The section should start with a short description of the actors involved (e.g., regular user, administrator, etc.) and then follow with a list of the use cases.

For each use case you should have the following:

* Name,
* Actors,
* Triggers (what initiates the use case),
* Preconditions (in what system state is this use case applicable),
* Actions (what actions will the code take to implement the use case),
* Alternative paths
* Postconditions (what is the system state after the use case is done),
* Acceptance tests (list one or more acceptance tests with concrete values for the parameters, and concrete assertions that you will make to verify the postconditions).

Each use case should also have a field called "Iteration" where you specify in which iteration you plan to implement this feature.

You may use the following table template for your use cases. Copy-paste this table for each use case you will include in your document.

### Iteration 1



Boxiang Scope --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

| Use case Student 3# |   |
| ------------------ |--|
| Name              | View Open Research Positions |
| Users             | Student, Faculty |
| Rationale        | The open research positions are what users of this platform are looking for. So when students or faculty log in or click their home page, they should see a list of open research positions. |
| Triggers        | The user click the Home Page (index page) or redirect to the Home Page route. |
| Preconditions     | Student or Faculty account login |
| Actions           | 1. Home page (index page) clicked. <br/>2. Home page (index page) route directed  2. Database table query   <br/>3. HTML render the database information (Only render the Research Project Title, brief description of the required qualifications, research filed, and start and end date ) |
| Alternative paths | For step 1, when users login their account, the platform will automatically load the Home page (index page). |
| Postconditions    | All open research opportunities are shown on the Homepage (index page). |
| Acceptance tests  | Make sure total number of open research opportunities are shown on the home page. |
| Iteration         | 1 |



| Use case Student 3# |                                                              |
| ------------------- | ------------------------------------------------------------ |
| Name                | Recommended Research Positions                               |
| Users               | Student                                                      |
| Rationale           | Now students that use this platform are in different majors, and among a major, they could be interested in various fields of studies. An algorithm that filters out the matching positions to the student will significantly improve the research job look-up efficiencies for the students. |
| Triggers            | The user submit the select field form component.             |
| Preconditions       | Student account login and is on the Home Page route.         |
| Actions             | 1. Select field clicked. <br/>2. Home page (index page) route directed and select filed element retrieved  <br/>3. Database table query the corresponding positions with match tag   <br/>4. HTML render the database information |
| Alternative paths   | For step 1, the select field will always place the "All" at the first position, so it will always load the all open research position. Unless otherwise, other interest tags are selected. |
| Postconditions      | The corresponding matched research opportunities are shown on the Homepage (index page). |
| Acceptance tests    | Make sure total number of matched open research opportunities are shown on the home page. |
| Iteration           | 1                                                            |



| Use case Student 4# |                                                              |
| ------------------- | ------------------------------------------------------------ |
| Name                | Open Research Position Information Display                   |
| Users               | Student, Faculty                                             |
| Rationale           | Since users can see all the open research positions on the Home Page, displaying all information of each available position on the home page will occupy a large pixels amount of space. So, we will need a unique route that to display the information of that open position. |
| Triggers            | The user click a specific research position post.            |
| Preconditions       | Home page is loaded.                                         |
| Actions             | 1. Click on a specific research position post. <br/>2. information route directed  2. Database information query and pass to HTML <br/>3. HTML render all information for the research position post) |
| Alternative paths   | A faculty user can only display other research position posts posted by other faculty, for the post from themselves will be handled with additional functionality that provide for modifications. |
| Postconditions      | A new page that shows all the details about the research position that user clicked. |
| Acceptance tests    | Make sure all the information about the current research position is on the page. |
| Iteration           | 1                                                            |



| Use case Student 1# |                                                              |
| ------------------- | ------------------------------------------------------------ |
| Name                | Student Account Registration                                 |
| Users               | Anonymous User / Student                                     |
| Rationale           | We want students can be able to log in to this platform, view and apply for the research position. To ensure that the student account has all the necessary information, we will require students to fill out their profiles at the time of registration. |
| Triggers            | User select create student account                           |
| Preconditions       | A user has a valid wsu@edu email that is not already tied to an account in the application. |
| Actions             | 1.Click register for a student account. <br/>2. System direct to a registration route and display the form for fill out. <br/>3. The student user supplies information (email, username, password) and profile information to the system. <br/>4. The system validates the supplied email is a valid and unused email and username. <br/>5. The student user is directed into the login page |
| Alternative paths   | 1. A user is asked to enter a different email if the email is already associated with an account or the email is not from the wsu.edu domain. <br/>2. A user is asked to enter a different username if the username is already associated with an account. |
| Postconditions      | An account for the email supplied by the user has been created, storing email, username, password, and profile information. |
| Acceptance tests    | Make sure that the user account is stored by the system with identical information to what the user supplied. |
| Iteration           | 1                                                            |



| Use case Student 2# |                                                              |
| ------------------- | ------------------------------------------------------------ |
| Name                | Student Account Login                                        |
| Users               | Student User                                                 |
| Rationale           | For student to be able to access features that require a student user account |
| Triggers            | A user selects the student login page                        |
| Preconditions       | A student user already has a created account                 |
| Actions             | 1. A student user should be able to supply the information (email and password) that is associated with their account.<br/>2. The system will validate that the information given by the user is correct.<br/>3. The user will now have a validated login session created. <br/>4. The user will be directed to the home page. |
| Alternative paths   | 1. A student user is asked if they want to sign up for an account if an account does not exist with their email. <br/> 2. A student user is asked to re-enter the password if the one entered is incorrect. |
| Postconditions      | A student user successfully logs into their account and a login session is created. |
| Acceptance tests    | Make sure that student users have an established login session with validated student user capabilities. |
| Iteration           | 1                                                            |



**Include a swim-lane diagram that illustrates the message flow and activities for following scenario:**
“A student applies to a research position; initially its status will appear as “Pending”. The faculty who created that position reviews the application and updates the application status to either “Approved for Interview”, or “Hired”, or “Not hired”. The updated status of the application is displayed on the student view.
The student may delete the pending applications (i.e., whose status is still “Pending”. )”


----
## 2.3 Non-Functional Requirements

List the non-functional requirements in this section.

You may use the following template for non-functional requirements.

1. [Enter a Concise Requirement Name]:  [provide a concise description, in clear and easily understandable language to specify the requirement]

----
# 3. User Interface

Here you should include the sketches or mockups for the main parts of the interface.

----
# 4. References

Cite your references here.

For the papers you cite give the authors, the title of the article, the journal name, journal volume number, date of publication and inclusive page numbers. Giving only the URL for the journal is not appropriate.

For the websites, give the title, author (if applicable) and the website URL.

----
----
# Appendix: Grading Rubric
(Please remove this part in your final submission)

These is the grading rubric that we will use to evaluate your document. 

| Max Points  | **Content** |
| ----------- | ------- |
| 10          | Do the requirements clearly state the customers’ needs? |
| 5           | Do the requirements avoid specifying a design (note: customer-specified design elements are allowed; non-functional requirements may specify some major design requirements)? |
| | |
|    | **Completeness** |
| 25 | Are use cases written in sufficient detail to allow for design and planning? |
| 4 | Do use cases have acceptance tests? |
| 20 | Is your use case model complete? Are all major use cases included in the document? |
| 8 | Has the team provided an appropriate swim-lane diagram for the scenario where faculty reviews a student’s application? |
| 10 |  Are the User Interface Requirements given with some detail? Are there some sketches, mockups?  |
|   
|   | **Clarity** |
| 4 | Is the document carefully written, without typos and grammatical errors? |
| 2 | Is each part of the document in agreement with all other parts? |
| 2 | Are all items clear and not ambiguous? (Minor document readability issues should be handled off-line, not in the review, e.g. spelling, grammar, and organization). |
|   |   |
|    | **GitHub Issues** |
| 10 | Has the team setup their GitHub Issues page? Have they  generated the list of user stories, use-cases, created milestones, assigned use-cases (issues) to milestones?   Example GitHub repo (check the issues): https://github.com/WSU-CptS322-Fall2021/TermProjectSampleRepo/issues |

