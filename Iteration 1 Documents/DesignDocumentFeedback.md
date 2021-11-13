# Design Document Feedback

## System Structure

 - Your diagram is for the most part correct put there's a lot of associations that make it very hard to read. I'd suggest revising it for cleanliness and readability next time around.

## Model

### User model
 - electives, research topics, and programming should probably not be strings. It's possible for a student to have more than one of each of those. Consider making them models as well and having these be relationships.
 - User model needs relationship to applications (students) and posts (faculty)

### Position
 - Missing relation to user who created the position.
 - Missing relation to applications for the position

### Missing application model
 - You need some way to store the applications students have submitted to a position, as well as the status of each application.

## Controller
 - Does not explain what the controller does in the relevant section
### Missing routes
 - index (landing for either faculty or student)
 - withdraw application
 - Apply for position
 - Edit profile
 - Update application status