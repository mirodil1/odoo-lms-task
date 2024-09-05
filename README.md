# Odoo Custom Modules

This repository contains custom modules for managing learning center system, including teachers, students, payments, groups, and courses.

## Modules Included

- **Teacher**: Manages teacher information.
- **Student**: Handles student records.
- **Payments**: Manages payment transactions and history.
- **Group**: Organizes students and teachers into groups.
- **Course**: Manages course information.

## Getting Started

### Prerequisites

- Python 3.10
- Odoo 17.0
- PostgreSQL

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/mirodil1/odoo-lms-task.git
   cd odoo-lms-task
   ```
2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Running locally**
    ```bash
    python3 odoo-bin --addons-path=addons,odoo/addons,project_addons

### Initial Setup

Upon first-time setup, activate all custom modules by navigating to the Odoo Apps menu and installing them. This will ensure all modules are properly loaded and configured.


### User Roles

Roles and permissions for users can be controlled when creating or managing users within the Odoo interface. Assign appropriate roles to users to grant access to different functionalities provided by the custom modules.