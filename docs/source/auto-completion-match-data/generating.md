## Generating Auto Completion Match Data

### Overview

To generate completion data, there are two available methods:

1. **QR Code Generation** – Suitable when scouting devices have internet access.
2. **Match Data File Generation** – Useful when scouting devices do not have reliable internet access. The data is transferred manually via USB drives or similar methods.

### Method 1: Generating a QR Code

This method allows scouting devices to receive match data through a QR code.

#### Steps:

1. Navigate to the `parsing` directory:
   ```sh
   cd parsing
   ```
2. Run the match data script:
   ```sh
   python GetMatchData.py
   ```
3. Select **Method 1** (Use of QR Codes).
4. Enter the **event key** when prompted.
5. Enter the **TBA API key** when prompted.
6. A link to the generated QR code will be provided. Open the link and save the QR code onto your device.
7. Transfer the QR code to a mobile device for easy scanning.
8. Scan the QR code using the app on scouting devices.
   - Refer to [Inputting Auto Completion Match Data](inputting.md#using-qr-codes) for more details.

### Method 2: Generating a File with Match Data

This method generates a JSON file with match data that can be transferred manually.

#### Steps:

1. Navigate to the `parsing` directory:
   ```sh
   cd parsing
   ```
2. Run the match data script:
   ```sh
   python GetMatchData.py
   ```
3. Select **Method 2** (Generate File with Match Data).
4. Enter the **event key** when prompted.
5. Enter the **TBA API key** when prompted.
6. The match data file will be generated and saved on your computer.
7. Transfer the file to scouting devices using a USB drive or another method.
8. Load the file into the website.
   - Refer to [Inputting Auto Completion Match Data](inputting.md#manually-inputting-a-match-data-file) for more details.
     for more details.
