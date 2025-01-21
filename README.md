# Furman Flask Serial Server

This project is a Flask-based web application designed to control the status of A/V equipment through web endpoints. It complements the [Furman Node Server](https://github.com/brandonlavello/Furman-Node-Server) project to manage A/V equipment throughout a building.

## Description

The Flask web application provides user control and status data for multiple Furman Power conditioners via URL endpoints. When a user accesses a specific endpoint, the server parses the URL data and triggers the relays through a serial interface on the server.

## Features

- **Web-Based Control**: Access endpoints to control A/V equipment status.
- **Serial Communication**: Interfaces with Furman Power conditioners through a serial connection.
- **Complementary Integration**: Works alongside the Furman Node Server for comprehensive A/V equipment management.

## Installation

1. **Clone the Repository**:

   ```bash
      git clone https://github.com/brandonlavello/Furman-Flask-Serial-Server.git
   ```

2. **Navigate to the Project Directory:**

   ```bash
      cd Furman-Flask-Serial-Server
   ```

3. **Install Dependencies:**

Ensure you have Python installed, then install the required packages:
   
   ```bash
      pip install -r requirements.txt
   ```

## Usage

Start the Flask Server:
   
   ```bash
      python app.py
   ```

Access Control Endpoints:

Open a web browser and navigate to http://<ip_address>/ to control the A/V equipment.

## License

This project is licensed under the GPL-3.0 License.

## Acknowledgments

Developed by Brandon Lavello
