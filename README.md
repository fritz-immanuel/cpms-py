# **Client - Project Management System**

## Preface

The **Client - Project Management System (CPMS)** is a terminal-based project management tool designed as a learning exercise for Python programming. It was created as part of the requirements for Purwadhika's Data Science & Machine Learning Course. This program demonstrates the basics of Python while providing practical functionality for managing client and project data.

---

## Introduction

The CPMS is ideal for professionals working on a client-project basis, helping them efficiently manage and track their projects. Users can perform essential operations such as creating, updating, viewing, and deleting both client and project records.

---

## Features

| Feature    | Clients | Projects                       |
| ---------- | ------- | ------------------------------ |
| **View**   | ✅      | ✅                             |
| **Create** | ✅      | ✅                             |
| **Update** | ✅      | ✅                             |
| **Delete** | ✅      | ✅ (by Project ID & Client ID) |

### View

Both modules (client and project) can be viewed directly in a table view. Upon entering the program, the user is presented with a choice of the 2 modules. After selecting the desired module, the user is presented with a list of data of that module.

### Create

Upon selecting the desired module, the user is presented with a list of data of that module. Alongside that, a menu of actions is displayed. The user may choose the "Add a new <module_name>" menu and the user will be taken into the data creation page. In the creation page, the user will be prompted text space for the input of the specific column asked. When all is done, the user will now be asked if they want to create another data input or no. If yes, then the user shall be starting the create data procedure again. If no, then they will be asked if they are sure to input the data.

### Update

This feature has the same flow as "Create". What makes this different is the fact that the user has to first input the <module> Code that they want to update. Only then the user will be prompted into updating the existing data.

### Delete

The 'Delete' feature is, as the name suggests, to delete data. This feature allows user to delete data by the module code. For example, if the user is in the `Client` Module, then they will be deleting by the `Client Code`. Both the `Client` and `Project` has this feature. However, the `Project` module has 2 extra delete features. Which are:

1. Delete by Client Code
2. Delete by Status

---

## Technology

- [Python](https://www.python.org/) – The only technology used for this program.

---

## Installation

1. Ensure you have [Python](https://www.python.org/) installed on your device.
2. Clone this repository:
   ```bash
   git clone https://github.com/fritz-immanuel/cpms-py
   ```
3. Navigate to the project directory and run the program using:
   ```bash
   python <file_name>.py
   ```
