# classroom-qr-checkin

A Python-based automation tool designed to integrate with **PrairieLearn**. This project validates student submissions for labs and generates a cryptographically signed **QR Code** as proof of completion.

* **Secure Validation:** Generates a unique hash upon successful test completion.
* **Visual Proof:** Renders a "Validated" QR Code in instuctors smartphone, that can be scanned by students.



## How to Use

1.  **Duplicate the Template:**
    Copy the `question-example/` folder and rename it to your new question ID (e.g., `lab01_abc`).

2.  **Update Metadata (`info.json`):**
    * **UUID:** Generate a fresh UUID (crucial to avoid conflicts).
    * **Title:** Update the question title and topic tags.
    * **Image:** Update with you docker image.

3.  **Edit Content (`question.html`):**
    Modify the HTML to display the specific instructions and submission requirements for this new lab.

4.  **Configure Validation (`tests/grade.py`):**
    Update the Python logic to test the specific requirements of the new assignment.

5.  **Deploy:**
    Sync the changes to your PrairieLearn server.


### Docker Build

Build with --platform linux/amd64 for working with PrairieLearn.

1. docker build --platform linux/amd64 -t your_user/your_image:latest .

2. docker push your_username/image:latest 