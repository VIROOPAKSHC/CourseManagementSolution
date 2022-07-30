# Course Management Solution ( In Construction )
A website where students, lecturers and instructors can login and assign, access courses, submit and work in together.
<br><br>
This project uses JAM stack - Python-Flask, VueJS, HTML, Boostrap, APIs.<br>
Project has several components and requirements which are the following:<br>

## A. Logins:<br>
<ol>
<li> Student Login - takes to the Student component </li>
<li> Teacher Login - takes to the Teacher component </li>
<li> Instructor Login - takes to the Instructor component </li>
</ol>

## B. Student Component and Dashboard Requirements:<br>
<ol>
<li> A profile page to show. </li>
<li> Dashboard with all courses enrolled in and done. </li>
<li> Search option to search in courses. </li>
<li> Drop down option to have which courses displayed. (Completed and current / Current / Completed) </li>
<li> Precautions and notes for usage. (Common to all) </li>
</ol>
Each course (Enrolled or completed) is a component. <br>

## C. Course Component: <br>
<ol>
<li> Course details and Info </li>
<li> Has Expiration date (Completion of a course in a semester.) </li>
<li> Announcements. </li>
<li> Topics. </li>
<li> Assignments.  </li>
<li> Exams. </li>
<li> Instructor, Teacher for the course. </li>
<li> Peers. </li>
</ol>
<br>
Student cannot add himself to a course. <br>
As soon as the course in a semester completes, it is completed currently for students, teachers, instructors. But they can still edit. <br>

## D. Teacher Component: <br>
<ol>
<li> Can Add Students to courses. </li>
<li> Can remove Students from course. </li>
</ol>

## E. Instructor Component: (Highest Authority for a course) <br>
<ol>
<li> Can create a course (Add a new course). </li>
<li> Can Delete or Edit a course and it's contents. </li>
<li> Can Assign teachers to courses. </li>
</ol>
<br>
All Instructors are Teachers, but all teachers are not instructors.<br>
<br>
An Instructor who has a profile, creates a course and allots a (set of) teacher(s) to the course. A teacher of a particular profile accesses the alloted course and adds students to the course causing them enrolled. A student with a profile joins a course, accesses the contents throughout the semester. <br>
A student cannot add himself to a course. <br>
