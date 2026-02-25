**GLC Graduation Requirement Validation System**

_Overview_

This project was developed during a 2023 hackathon hosted by the Applied Information Engineering department.
The goal of the project was to build a system that allows students to easily check whether they meet the graduation requirements for the Global Leaders College (GLC) at Yonsei University.

Students upload their academic records as a CSV file, and the system analyzes the data to determine whether graduation requirements are satisfied and what remains.


_Features_

ㅇ CSV file input processing

ㅇ Automatic major classification based on student data

ㅇ Graduation requirement validation logic

ㅇ Support for multiple majors with different requirement criteria



_My Contribution_

I was responsible for the backend logic, specifically:
  1. Designing and implementing CSV data preprocessing
  2. Building the graduation requirement validation logic
  3. Structuring the data flow so it integrates smoothly with the Streamlit frontend
  4. Handling inconsistencies in input data (e.g., formatting differences, unnecessary spaces)

I focused on ensuring that the system produces reliable and consistent results even when input data is not perfectly structured.


_How It Works_

  1. The user uploads a CSV file containing their academic records
  2. The system reads and preprocesses the data
  3. The student’s major is identified
  4. Based on the major, the corresponding graduation requirements are applied
  5. The system outputs whether the student meets the requirements and what is missing


_Tech Stack_

ㅇ Python

ㅇ Pandas (for data processing)

ㅇ Streamlit (for frontend integration, 3 man team project)



_Scope of This Repository_

This repository focuses on the backend logic that I implemented during the hackathon.
It includes:

  ㅇ CSV preprocessing code 
  
  ㅇ Graduation requirement validation logic for:
  
    - Applied Information Engineering
    
    - Bio & Living Engineering
    
    - Korean Language & Culture Education
    
    - International Commerce

    - General Education requirements
    
The full system (including frontend UI and full integration) was developed as a team project.
Only my contribution has been refactored and uploaded here for clarity.


_What I Learned_

Through this project, I learned that data quality is just as important as implementing logic. Even small inconsistencies in data can significantly affect results, and backend systems must be designed to handle real-world variability.

This experience led me to develop a strong interest in data-centric problem solving, where improving data quality and structure plays a critical role in building reliable systems.





Backend logic must be designed with real-world input variability in mind

This experience made me more interested in data-focused problem solving, where improving data quality and structure plays a key role in building reliable systems.
