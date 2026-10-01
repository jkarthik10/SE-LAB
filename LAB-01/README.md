# SE Lab – Requirements Engineering & UML

## Lab 1: Requirements Engineering & UML Use-Case Modelling

### Problem Statement #09
**Faculty Research Grant & Publication Tracker**

## Student Details

- **Name:** J Karthik
- **SRN:** PES1UG25AM804
- **Section:** B

## Objective

The objective of this lab is to perform Requirements Engineering and UML Use-Case Modelling for a Faculty Research Grant & Publication Tracker system.

## System Overview

The Faculty Research Grant & Publication Tracker is designed to help Faculty Researchers manage research grants, research expenses, publications, co-author approvals, and research performance.

The Research Dean can monitor grant utilization and research/publication performance.

## Functional Requirements

The system supports:

- Managing research grant records and approved funding limits.
- Recording research expenses.
- Calculating the remaining grant balance.
- Preventing expenses that exceed the available grant amount.
- Managing publication records.
- Maintaining indexing and citation information.
- Supporting co-author approval workflows.
- Providing fund burn-up and research/publication analytics.

## Non-Functional Requirements

The system includes:

- Immutable and tamper-evident audit records.
- Traceability of financial approvals and publication status changes.
- Responsive access during expected peak usage.

## Actors

The UML Use-Case Diagram contains two main actors:

1. Faculty Researcher
2. Research Dean

## Use Cases

### Faculty Researcher

- UC-01 – Manage Grant
- UC-02 – Record Research Expense
- UC-03 – Update Remaining Budget
- UC-04 – Manage Publication
- UC-05 – Request Co-author Approval
- UC-06 – Track Publication Metrics

### Research Dean

- UC-07 – View Fund Analytics
- UC-08 – View Research Metrics
- UC-09 – Review Approval

## Core Use Case

### Record Research Expense

The Faculty Researcher selects an active research grant and enters the expense details.

The system validates the expense and checks whether the amount is within the available grant balance.

If the expense is valid:

- The expense is recorded.
- Total expenditure is updated.
- Remaining grant balance is recalculated.
- The updated balance is displayed.

If the expense exceeds the available grant balance, the system rejects the expense and informs the researcher.

## UML Relationships

The use-case diagram contains:

- `<<include>>` relationships for mandatory supporting functionality.
- `<<extend>>` relationship for the co-author approval workflow.

## Deliverable

This repository contains the complete Lab 1 submission, including:

- Requirements Table
- UML Use-Case Diagram
- Use-Case Descriptions
- Core Use-Case Flow
- Alternate Flow

## File

`PES1UG25AM804_LAB01.pdf`

---

**PES University – CSE (AIML)**  
**Software Engineering Lab**
