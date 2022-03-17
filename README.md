# Furman Flask Serial Server 

This project creates a simple web application with Flask to allow a user to control the status of A/V equipment through web endpoints.

This project complements the [Furman-Node-Server](https://github.com/brandonlavello/Furman-Node-Server) project to control AV equiptment throughout the building.  


## Description

This Flask web application offers user control and status data for multiple Furman Power conditiors through URL endpoints.

Example: http://<ip_address>/<deviceName>/<command>
  
When the user accesses the endpoint, the server parses the data in the URL and triggers the relays through a serial interface on the server.
  
