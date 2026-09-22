
# AWS 3-Tier Web Application Architecture

A scalable and secure Python web application deployed on Amazon Web Services (AWS) using a 3-tier architecture.

##  Project Overview

This project implements a 3-tier web application architecture on AWS consisting of:

- Web Tier – Nginx running on Amazon EC2
- Application Tier – Python Flask application running on Amazon EC2
- Database Tier – Amazon RDS MySQL

The architecture uses Amazon VPC, Application Load Balancers, Internet Gateway, NAT Gateway, Security Groups, and private/public subnets to provide secure communication between the different application layers.

The application allows users to submit feedback through a web interface. The request is processed by the Flask backend and the submitted feedback is stored in Amazon RDS MySQL.

## Architecture


                         Internet
                            │
                            ▼
                 ┌─────────────────────┐
                 │  Public ALB :80     │
                 │  GUVI-Public-ALB    │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   Web EC2           │
                 │   Nginx             │
                 │   Public Subnet     │
                 └──────────┬──────────┘
                            │
                     /api/ :5000
                            │
                            ▼
                 ┌─────────────────────┐
                 │  Internal ALB       │
                 │  Port 5000          │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   App EC2           │
                 │   Python + Flask    │
                 │   Private Subnet    │
                 └──────────┬──────────┘
                            │
                         :3306
                            │
                            ▼
                 ┌─────────────────────┐
                 │   Amazon RDS        │
                 │   MySQL             │
                 │   feedbackdb        │
                 └─────────────────────┘

## AWS Services Used:

-Amazon VPC
-Amazon EC2
-Amazon RDS MySQL
-Application Load Balancer (ALB)
-Internet Gateway
-NAT Gateway
-Security Groups
-Route Tables
-Amazon EC2 Systems Manager (Session Manager)
-Nginx
-Python Flask

## VPC

VPC Name: GUVI-3Tier

CIDR: 10.0.0.0/16

The VPC is distributed across two Availability Zones in the Mumbai region:

Region: ap-south-1

## SUBNETS:

| Tier        | Availability Zone | CIDR        | Type    |
| ----------- | ----------------- | ----------- | ------- |
| Web         | ap-south-1a       | 10.0.1.0/24 | Public  |
| Web         | ap-south-1b       | 10.0.2.0/24 | Public  |
| Application | ap-south-1a       | 10.0.3.0/24 | Private |
| Application | ap-south-1b       | 10.0.4.0/24 | Private |
| Database    | ap-south-1a       | 10.0.5.0/24 | Private |
| Database    | ap-south-1b       | 10.0.6.0/24 | Private |

## Security

Security Groups are configured to restrict traffic between the application tiers.

Load Balancer Security Group

GUVI-LB-SG

HTTP (80) from the Internet
TCP (5000) for communication with the Application Tier
Web Security Group

GUVI-Web-SG

HTTP (80)
SSH/Instance Connect access as required
Application Security Group

GUVI-App-SG

TCP (5000) from the Web/Load Balancer tier
Database Security Group

GUVI-DB-SG

MySQL/Aurora (3306) from the Application Tier

Only the required traffic is permitted between the application layers.

## Application Components

#Web Tier

The Web Tier uses an Amazon EC2 instance running Nginx.

Nginx:

Serves the frontend HTML page
Handles incoming HTTP requests
Acts as a reverse proxy for /api/ requests
Forwards API requests to the Internal Application Load Balancer

#Application Tier

The Application Tier runs a Python Flask application on port 5000.

The Flask application:

Receives feedback requests
Processes user input
Connects to Amazon RDS MySQL
Stores submitted feedback

#Database Tier

Amazon RDS MySQL is used as the database layer.

Database:
 Database: feedbackdb
 Table: feedback

The feedback table stores:

-ID
-Name
-Email
-Feedback
-Created timestamp

## Validation

The application was validated through the following workflow:

-Accessed the application through the Public ALB.
-Loaded the feedback form.
-Submitted feedback through the web interface.
-Nginx forwarded the API request to the Internal ALB.
-The Internal ALB forwarded the request to the Flask application.
-Flask processed the request.
-Flask connected to Amazon RDS MySQL.
-Feedback was successfully stored in the feedback table.
-SQL queries were used to verify the stored records

## Architecture Diagram

Architecture/AWS-3TIER-ARCHITECTURE.drawio.png
