# SpendWise — Personal Finance Tracker

SpendWise is a desktop-based expense tracking application built using **Python** and **Tkinter** that helps users manage daily expenses, monitor spending habits, and organize financial records through a clean and interactive interface.

Designed as a lightweight personal finance assistant, the application allows users to track expenses without relying on spreadsheets or external tools.

---

## Overview

Managing daily expenses often becomes difficult when transactions are scattered across notes, apps, or memory.

SpendWise solves this by providing a simple desktop application where users can:

* Record expenses instantly
* Categorize spending habits
* View expense history
* Delete incorrect entries
* Monitor total spending
* Analyze category-wise expenses

The goal of the project was to build a practical finance management tool while applying core Python concepts to a real-world problem.

---

## Features

### Add Expense

Users can add an expense by entering:

* Amount spent
* Expense category
* Expense description

Example:

```text
₹450 | Food | Pizza
₹120 | Travel | Bus Ticket
₹899 | Shopping | Shoes
```

---

### Expense History

Displays all previously recorded expenses inside the application.

Every expense is automatically saved and reloaded whenever the application starts.

---

### Persistent Data Storage

Expense records are stored locally using file handling.

This allows the application to preserve data even after closing the program.

---

### Delete Expense

Users can remove any selected expense entry from the expense history.

Useful for correcting accidental entries.

---

### Total Spending Tracker

Automatically calculates total money spent across all recorded expenses.

Example:

```text
Total Spending: ₹4580
```

---

### Category Summary

Generates category-wise expense distribution.

Example:

```text
Food → ₹1600
Travel → ₹500
Shopping → ₹2100
Bills → ₹380
```

This helps users understand where most spending occurs.

---

## Tech Stack

Built entirely using:

* Python
* Tkinter (GUI Development)
* File Handling
* Lists and Dictionaries
* Functions and Modular Logic

No external libraries or frameworks were used.

---

## Why I Built This

The objective behind SpendWise was to build a practical application that solves an everyday problem while strengthening problem-solving skills in Python.

Instead of creating tutorial-based beginner projects, this project focuses on building a utility that has actual real-world use.

The project helped in understanding:

* Desktop application development
* State management
* File persistence
* CRUD operations (Create, Read, Delete)
* User interface design in Python

---

## Future Improvements

Planned upgrades for future versions:

* Dropdown category selector
* Monthly budget limits
* Search and filter expenses
* Expense analytics dashboard
* Export records to CSV
* Graph-based spending visualization
* Dark/Light mode themes

---


## Current Version

Version 1 — Functional Desktop MVP

A fully working desktop expense tracker capable of storing and managing personal expense records locally.

---

## Author

Built as a portfolio project focused on practical Python development and solving real-world productivity problems.

