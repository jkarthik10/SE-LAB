# LAB 3 – Component Modelling & Architectural Pattern Selection

## Faculty Research Grant & Publication Tracker

**Problem Statement #09**

- **Name:** J Karthik
- **SRN:** PES1UG25AM804
- **Section:** B

## Objective

To select a suitable architectural pattern and create a UML Component Diagram showing components, interfaces, and dependencies.

## Selected Architecture

### Layered Architecture

The system is divided into three layers:

- **Presentation Layer:** Web Portal UI
- **Business Layer:** Grant & Expense Manager, Publication Manager, Approval Workflow, Analytics Service
- **Data Layer:** Database Repository, Audit Ledger

## Main Interfaces

- `IGrantService`
- `IPublicationService`
- `IApprovalReview`
- `IAnalyticsService`
- `IApprovalRequest`
- `IDataAccess`
- `IAuditLog`

## Architectural Justification

Layered Architecture provides clear separation of concerns, easier maintenance, and organized component interaction. The Immutable Audit Ledger provides tamper-evident logging for security, while separation of layers supports responsive system performance.

## Requirements Covered

- FR-001: Grant Management
- FR-002: Expense & Budget Management
- FR-003: Publication Tracking
- FR-004: Approval Workflow
- FR-005: Research & Fund Analytics
- NFR-001: Audit Ledger
- NFR-002: Responsive Access

## Deliverables

- UML Component Diagram
- Architectural Pattern Selection
- Component and Interface Identification
- Architectural Justification
