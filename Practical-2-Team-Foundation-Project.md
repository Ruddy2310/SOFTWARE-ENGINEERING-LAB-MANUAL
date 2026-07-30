# Practical 2: Creating a Team Foundation Project

## Aim
To study Team Foundation Server (TFS) / Azure DevOps and create a Team Foundation Project for managing a software project's source code, work items, and team collaboration.

## Theory

**Team Foundation Server (TFS)**, now evolved into **Azure DevOps Server / Azure DevOps Services**, is a Microsoft product that provides:

- **Version Control** — Team Foundation Version Control (TFVC) and Git repositories
- **Work Item Tracking** — for managing tasks, bugs, user stories, and features
- **Build Automation (CI/CD)** — automated build and release pipelines
- **Project Management** — Agile/Scrum boards, sprints, backlogs
- **Reporting & Dashboards** — progress tracking and team metrics

A **Team Project** is the basic organizational unit in TFS/Azure DevOps. It contains everything related to a software project — code repository, work items, builds, test plans, and documentation — under one collection.

## Prerequisites
- A Microsoft account
- Access to [https://dev.azure.com](https://dev.azure.com) (Azure DevOps Services — the modern, free, cloud-based version of TFS)

## Procedure

1. **Sign in** to Azure DevOps at `https://dev.azure.com` using a Microsoft account.
2. **Create an Organization** (if not already created):
   - Click **New organization**
   - Provide an organization name
   - Choose the region for hosting
3. **Create a New Team Project**:
   - Click **+ New Project**
   - Enter **Project name** (e.g., `SoftwareEngineeringLab`)
   - Add a short **Description**
   - Set **Visibility**: Private or Public
   - Choose **Version control**: Git (recommended) or TFVC
   - Choose **Work item process**: Agile, Scrum, or Basic
   - Click **Create**
4. **Explore the Team Project**:
   - **Boards** — create and track work items (Epics, User Stories, Tasks, Bugs)
   - **Repos** — clone/push code using Git
   - **Pipelines** — set up CI/CD build and release pipelines
   - **Test Plans** — plan and execute test cases
   - **Artifacts** — manage packages and dependencies
5. **Add Team Members**:
   - Go to **Project Settings → Teams**
   - Add members and assign roles (Reader, Contributor, Admin)
6. **Create Work Items**:
   - Go to **Boards → Work Items → New Work Item**
   - Add a User Story or Task with title, description, and assignee

## Conclusion
A Team Foundation Project was successfully created in Azure DevOps, demonstrating how TFS/Azure DevOps supports centralized version control, work item tracking, and team collaboration for managing a software engineering project throughout its lifecycle.
