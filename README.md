# A&GBusinessesPromotions

[![Logo](https://i.imgur.com/glNeRC8.png "Logo")](https://i.imgur.com/glNeRC8.png "Logo")

[![GitHub pull-requests](https://img.shields.io/github/issues-pr/avivz450/A-GBusinessesPromotions.svg)](https://github.com/avivz450/A-GBusinessesPromotions/pulls)
[![GitHub issues](https://img.shields.io/github/issues/avivz450/A-GBusinessesPromotions.svg)](https://github.com/avivz450/A-GBusinessesPromotions/issues/)

## Product :
A web application whose purpose is to advertise businesses whose type is determined according to the site from which we came to the application

## Goals :
1. To give the user an easy experience of viewing businesses according to his request.
2. Helping business owners to market their business.
3. Make a profit to the app owners by premium packages.

## Users :
Site manager - will accept/ignore businesses to his own web, will inspect the content of the business.
Business owners - will open their business on a suitable page.
Premium users will have additional benefits.
Guests - will be able to watch the content only.

## Features :
1. Adding business/sales. (V)
2. Filter and sort businesses/sales by specific criteria.
3. Editing an existing business/sale page. (V)
4. View sales/businesses for each user/guest. (V)
5. Charging for premium services. (V)
6. Connect Sale/Business to other website efficiently.
7. Host the website in AWS + edit our URLs. (V)
8. Registration and login. (V)
9. User notification. (V)
10. Edit admin section.
11. Add website. (V)

## Nice to have features
1. Adding a category for each business for filter while the user using the searching bar.
2. Extending opening hours for each business.
3. Adding reviews to the businesses
4. Adding "ask to connect to my site"
5. Add block users feature.
6. Edit website to admins only

##  Technology Stack :
- Client side : Html, CSS, JavaScript .
- Server side :  Django, Python
- Database : SQLite
- SCM: Git and GitHub
- Testing: Pytest
- Virtualization: Vagrant and VirtualBox
- AWS ec2 instance: host our website on the cloud
- AWS route 53: adding our DOMAIN to the instance path

## Dependencies
The dependencies that must be installed for this software to work are:
* [Vagrant](https://www.vagrantup.com/downloads)
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

## Installation

To install make sure you have Git installed already and all the dependencies mentioned above.

Enter in the Command Line: 
```
git clone https://github.com/avivz450/A-GBusinessesPromotions.git
```
## Getting Started
In your local git repository you made, enter the command:
```
vagrant up
```
Afterwards vagrant will boot up, configure, download and install all the needed additional dependencies.
A script will launch the app and you can access it in: http://127.0.0.1:8000/

## The public website url
- If you want to visit our wesite go to: agbusinessespromotions.com

## Instrutor :
Amir Kirsh

## Team members:
- Aviv Zafrani
- Gideon Schachar

## License

Distributed under the MIT License. See `LICENSE` for more information.
