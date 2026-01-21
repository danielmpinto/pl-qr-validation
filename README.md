# classroom-qr-checkin

A Python-based automation tool designed to integrate with **PrairieLearn**. This project validates student submissions for labs and generates a cryptographically signed **QR Code** as proof of completion.

* **Secure Validation:** Generates a unique hash upon successful test completion.
* **Visual Proof:** Renders a "Validated" QR Code in instuctors smartphone, that can be scanned by students.


## Docker Build

Need to updt with --platform linux/amd64 for working with PrairieLearn.

docker build --platform linux/amd64 -t your_user/your_image:latest .

docker push your_username/image:latest 