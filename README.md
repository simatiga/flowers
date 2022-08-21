# flowers

설치방법, 소스코드 설명, 이슈 등을 간단하게 기록.

![image](https://user-images.githubusercontent.com/111373093/185776046-91924d82-8dab-48b0-9cf9-3255c67eedbc.png)



Getting started
The app consists of a client using React.js frontend, Node.js is used as a backend server with Express for REST APIs and MySQL db.

The React client sends HTTP Requests and retrieves HTTP Responses using Axios, consume data on the components. React Router is used for navigating to pages. The Node.js Express exports REST APIs and interacts with MySQL Database.

diagram.png
Picture source: Building Data Science Web Application with React, NodeJS, and MySQL



To run our app, we have to do the following:

install node, for mac, brew install node
clone a repo
install packages under server directory, npm install
docker-compose up

Let's start!


Clone repo:

$ git clone https://github.com/Einsteinish/react-nodejs-mysql-docker-compose.git    

$ cd react-nodejs-mysql-docker-compose    

Install the dependencies:

$ npm version
{
  'web-samples': '1.0.0',
  npm: '6.14.5',
  ares: '1.16.0',
  brotli: '1.0.7',
  cldr: '37.0',
  icu: '67.1',
  llhttp: '2.0.4',
  modules: '83',
  napi: '6',
  nghttp2: '1.41.0',
  node: '14.5.0',
  openssl: '1.1.1g',
  tz: '2019c',
  unicode: '13.0',
  uv: '1.38.0',
  v8: '8.3.110.9-node.23',
  zlib: '1.2.11'
}

$ cd server 

$ npm install  

The npm (node package manager) is a dependency/package manager we get out of the box when we install Node.js. It provides a way for developers to install packages both globally and locally.

Note that npm by itself doesn't run any packages. If we want to run a package using npm, we must specify that package in our package.json file.

When executables are installed via npm packages, npm creates links to them:

local installs have links created at the ./node_modules/.bin/ directory.
global installs have links created from the global bin/ directory, for example: /usr/local/bin on Linux.






Services
We'll be using 4 services: mysql, phpmyadmin, server, and client:

mysql will use the extension fields declared for host, database, user and password (and a root password of its own just in case) to enable connections for the other services. The port 3306 is exposed as the default port.
phpmyadmin is to view the databases and manually edit if needed. It will depend on the mysql service so this service will run before it upon start, and it is linked to it to enable use of the credentials defined (host, database, user, password) when navigating to http://localhost:8080 to access the database. The PMA_HOST defines the address of the mysql server.
server refers to the nodeJS app. It will be built with its own Dockerfile, and it will run before the mysql service. It will expose the port 8000 and use a variable, REACT_APP_SERVER_PORT, to allow the express server to work. MYSQL_HOST_IP allows us to resolve the mysql service's host IP address to map it to the mysql connection.
client refers to the React app. Its build attribute will search for a Dockerfile inside the client folder. The NODE_PATH environment variable allows for the app to recognize its src folder as the start point for aliases to work. It also makes of the extension fields, but only to use REACT_APP_SERVER_PORT. Since the default port in a react app done with CRA is 3000 , this port will be exposed. We provide volumes for the src folder to store codes.
