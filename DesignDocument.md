# Design Document

## Your Project Title
--------
Prepared by:

* `<author1>`,`<organization>`
* `<author1>`,`<organization>`
* `<author1>`,`<organization>`
* `<author1>`,`<organization>`

---

**Course** : CptS 322 - Software Engineering Principles I

**Instructor**: Sakire Arslan Ay

---

## Table of Contents
- [Design Document](#design-document)
  - [## Your Project Title](#-your-project-title)
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
|Revision 1 |2021-10-05 |Initial draft | 1.0        |
|      |      |         |         |
|      |      |         |         |


# 1. Introduction

Explain the purpose for providing this design document. If this is a revision of an earlier document, please make sure to summarize what changes have been made during the revision (keep this discussion brief). 

Then provide a brief description of your project and state your project goal.

At the end of the introduction, provide an overview of the document outline.

Section II includes …

Section III includes …

# 2.	Architectural and Component-level Design
## 2.1 System Structure

This section should describe the high-level architecture of your software:  i.e., the major subsystems and how they fit together. 
If you adopted the application structure we used in the Smile App, your application would have the Model-View-Controller (MVC) pattern. If you adopted a different architectural pattern, mention the pattern you adopted in your software and briefly discuss the rationale for using the proposed architecture (i.e., why that pattern fits well for your system).

In this section:
 * Provide a UML component diagram that illustrates the architecture of your software.
 * Briefly explain the role of each subsystem in your architectural design and explain the dependencies between them. 
 * Discuss the rationale for the proposed decomposition in terms of cohesion and coupling.

## 2.2 Subsystem Design 

(Note: This is just a suggested template. If you adopted a pattern other than MVC, you should revise this template and the list the major subsystems in your architectural design.)

### 2.2.1 Model

|Table 1|||
------------- | --------------|--------------|
Name:         | User ||
Role:         | *Store user infomation, both student and faculty* |
|*Table contain follow columns:*|
id            |Integer, primary_key|User ID|
username      |String(64), unique, index|Username|
password_hash |String(128)              |Hashed password|
lastname      |String(20)               |User lastname|
firstname     |String(30)               |User firstname|
wsuid         |Integer, unique          |User WSUID|
phone         |String(20)               |User phone number|
email         |String(120), unique, index|User email address|
major         |String(20)               |Student major|
GPA           |String(5)                |Student GPA|
gradulation   |String(10)               |Student graduate date|
elective      |String(300)              |Student elective class|
researchtopic |String(30)               |Student interested research topic|
programming   |String(30)               |Student programming language|
experience    |String(200)              |Student experience and brief introduction|
role          |String(20)               |Determine the user role is faculty or student|

|Table 2|||
------------- | --------------|--------------|
Name:         | User ||
Role:         | *Store user infomation, both student and faculty* |
|*Table contain follow columns:*|
id            |Integer, primary_key     |Position ID|
title         |String(2048)             |Position title|
desc          |String(2048)             |Position description|
start_date    |String(128)              |Position start date|
end_date      |String(128)              |Position end date|
time_commitment|String(128)             |Time commitment|
research_field |String(128)             |Research field this position related|
applicant_qualification|String(1024)    |User email address|
user_id       |Integer                  |User assigned to this position|

### 2.2.2 Controller

|   | Methods           | URL Path        | Description  |
|:--|:------------------|:----------------|:-------------|
|1. |GET                |faculty_index    |Retrieve all research position for faculty to manage              |
|2. |GET                |student_index    |Retrieve all research position for student to apply              |
|3. |GET, POST          |newPost          |Faculty create new position              |
|4. |GET, POST          |delete/<position_id>|Faculty delete created position              |
|5. |GET, POST          |login            |Let user login the system              |
|6. |GET                |logout           |Let user logout the system              |
|7. |GET, POST          |faculty_register |Let faculty register into the system              |
|8. |GET, POST          |student_register |Let student register into the system              |
|9. |GET, POST          |register         |Let user register into the system              |


### 2.2.3 View and User Interface Design 

Briefly explain the role of the view. Explain how you will build the user interfaces. Mention the frameworks or the libraries you plan to use.  

Provide a detailed description of user interface you have built so far. The information in this section should be accompanied with proper images of your screenshots.  Make sure to mention which use-cases in your “Requirements Specification” document will utilize these interfaces for user interaction. 


# 3. Progress Report

Write a short paragraph summarizing your progress in iteration1.

# 4. Testing Plan

(***in iteration 1***)
Don't include this section.

(***in iteration 2***)
In this section , provide a brief description of how you plan to test the system. Thought should be given to  mostly how automatic testing can be carried out, so as to maximize the limited number of human hours you will have for testing your system. Consider the following kinds of testing:
  * *Unit Testing*: Explain for what modules you plan to write unit tests, and what framework you plan to use.  (Each team should write automated tests (at least) for testing the API routes)
  * *Functional Testing*: How will you test your system to verify that the use cases are implemented correctly? (Manual tests are OK)
  * *UI Testing*: How do you plan to test the user interface?  (Manual tests are OK)



# 5. References

Cite your references here.

For the papers you cite give the authors, the title of the article, the journal name, journal volume number, date of publication and inclusive page numbers. Giving only the URL for the journal is not appropriate.

For the websites, give the title, author (if applicable) and the website URL.


----
# Appendix: Grading Rubric
(Please remove this part in your final submission)

These is the grading rubric that we will use to evaluate your document. 


|**MaxPoints**| **Design** |
|:---------:|:-------------------------------------------------------------------------|
|           | Are all parts of the document in agreement with the product requirements? |
| 10        | Is the architecture of the system described well, with the major components and their interfaces?  Is the rationale for the proposed decomposition in terms of cohesion and coupling explained well? |
| 15        | Is the document making good use of semi-formal notation (i.e., UML diagrams)? Does the document provide a clear and complete UML component diagram illustrating the architecture of the system? |
| 15        | Is the model (i.e., “database model”) explained well with sufficient detail? | 
| 10        | Is the controller explained in sufficient detail?  |
| 20        | Are all major interfaces (i.e., the routes) listed? Are the routes explained in sufficient detail? |
| 10        | Is the view and the user interfaces explained well? Did the team provide the screenshots of the interfaces they built so far.   |
| 5         | Is there sufficient detail in the design to start Iteration 2?   |
| 5         | Progress report  |
|           |   |
|           | **Clarity** |
| 5         | Is the solution at a fairly consistent and appropriate level of detail? Is the solution clear enough to be turned over to an independent group for implementation and still be understood? |
| 5         | Is the document carefully written, without typos and grammatical errors?  |
|           |  |
|           | **Total** |
|           |  |