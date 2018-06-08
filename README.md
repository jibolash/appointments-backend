# appointments-backend

Backend for an appointment scheduling app built with Perl and CGI

## Local Setup
This app was built and tested on a macOs High Sierra, Version 10.13.4

- Download or clone this repo into the `cgi-bin` folder of your apache webserver.
- Run the command `sudo chmod 755 /path-to/cgi-bin/appointments-backend`. This makes the Perl scripts executable.
Notice that `path-to` indicates the path to the `appointments-backend` folder inside `cgi-bin` where you cloned or downloaded the repo in the step above
- If you haven't already done so, download or clone the frontend for this application (https://github.com/jibolash/appointments-frontend) into the document root of your apache webserver. Depending on your apache setup or operating system, this could be named `www`, `Sites` or `htdocs`
- Start apache
- Vist the app in your browser at `http://localhost/appointments-frontend`
