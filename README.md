# aws-3-tier-architecture
AWS 3-Tier Web Application using EC2, RDS MySQL, Application Load Balancers, Nginx, and Flask.

# AWS 3-Tier Web Application Architecture

A scalable and secure Python web application deployed on Amazon Web Services (AWS) using a 3-tier architecture.

## 📌 Project Overview

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

                 
