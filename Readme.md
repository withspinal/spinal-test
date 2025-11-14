# Contract Evidence Tool - Technical Assessment

Welcome! This technical assessment challenges you to build a **Contract Evidence Tool** that extracts invoice-related information from contract documents using OCR and displays the results in an interactive frontend application.

## Overview

Your task is to create a full-stack application that:
1. **Processes contract documents** using OCR to extract key information
2. **Identifies and stores bounding box coordinates** for each extracted field
3. **Visualizes the extracted data** in an interactive frontend with document highlighting

Look at [Reducto.ai](https://reducto.ai/) - where you can upload a document and see highlighted regions showing where specific information was extracted from. Your solution should provide a similar experience.

Please use AI Assistant coding tools.

---

## What You Need to Extract

From the sample contracts in the `/contracts` folder, extract **ALL** information that would typically appear on an invoice:

- Customer & Client Name
- Payment Terms (Things like when is the invoice due after payment)
- Payment Schedule (frequency - annually, monthly, etc.)
- Payment Amounts (total value, installments, etc.)
- Contract Start Date
- Contract Sign/Execution Date
- Any other invoice-relevant details you identify

For each extracted field, you must also capture the **bounding box coordinates** so the frontend can highlight where that information appears in the original document.
PyMuPDF with tesseract OCR is probably your best combination to tackle this task. This combination allows both document extraction through OCR and PDF annotations.


## What's Already Set Up

We've provided a solid backend foundation to save you time:

### Backend Infrastructure
- **FastAPI** application
- **PostgreSQL 18** database
- **SQLAlchemy** ORM with proper session management
- **Alembic** for database migrations
- **Docker Compose** setup for local development
- Example models and API endpoints to guide you

### Database
- Configured and ready to use
- Example model showing best practices
- Migration system ready for your schema changes

### Development Environment
- Fully containerized with Docker
- Automatic database initialization
- Development seed data
- All dependencies managed with `uv`

---

## Your Challenge

### Backend Tasks

1. **OCR Integration**
2. **Data Models**
3. **API Endpoints**
4. **File Storage**
5. We do NOT expect tests to be written

### Frontend Tasks

**Framework Choice:** You may use any frontend framework or library you're comfortable with. The best library for loading in PDFs and navigating them is probably PDF.js

## Getting Started

### Prerequisites
- Docker and Docker Compose installed
- Your preferred code editor

### Setup Instructions

1. **Start the application:**
   ```bash
   docker-compose up --build
   ```

2. **Access the backend:**
   - API: http://localhost:8000

3. **Database:**
   - PostgreSQL is accessible on `localhost:5434`
   - Credentials: `postgres` / `password`
   - Database name: `spinal`

4. **Sample contracts:**
   - Located in the `/contracts` folder
   - Use these for testing your OCR extraction

## Evaluation Criteria

Your submission will be evaluated on a few factors. The most important being, does the application work.
Other factors could include:

#### Data Modeling 
- Appropriate database schema design
- Proper relationships between entities

#### Frontend Implementation
- Highlighting accuracy and clarity
- Intuitive user interface

## Submission Instructions

- Clone spinal-test repository
- Commit all your changes to git
- Ensure the application runs with `docker-compose up --build`
- Send link to repo in email

### Time Expectation

This assessment is designed to take **6 hours**. We value:
- **Working software** over perfect code
- **Core functionality** over additional features
- **Clear thinking** over complex solutions
