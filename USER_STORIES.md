# Bella Vista Salon – User Stories and Acceptance Criteria

**Course:** EGN 475 – Software Prototyping  
**Assignment:** Week 2 – Assignment 2.1  
**Project:** Bella Vista Salon – Option B  
**Location:** Coral Gables, Florida  
**Developer:** Waqar Javed

## 1. Introduction

This backlog defines user stories and testable acceptance criteria for the Bella Vista Salon appointment-booking prototype. It covers the two primary user groups: salon clients and salon staff. Each story is prioritized as Must, Should, or Could.

**Prototype assumptions:** The salon's exact operating hours, address, service durations, and current booking procedures have not been provided. The prototype will use configurable sample data for business hours, service durations, and location details; these values are not presented as verified salon policies. The first version supports one service per appointment, does not require clients to select a stylist, and uses the salon's local time.

## 2. Client User Stories

### US-01: Browse Salon Services

**Priority:** Must

As a salon client, I want to view active salon services and their descriptions, so that I can choose a service that meets my needs.

**Acceptance Criteria**

1. **Given** one or more active services have a name and description, **when** the client opens the services page, **then** the application displays each active service with its name and description.
2. **Given** no active services are available, **when** the client opens the services page, **then** the application displays a message that no services are currently available and does not display inactive or incomplete entries.

### US-02: View Available Appointment Times

**Priority:** Must

As a salon client, I want to view available appointment times for a selected service and date, so that I can choose a time that fits my schedule.

**Acceptance Criteria**

1. **Given** the client selects an active service and a future date, **when** the application checks configured salon hours, the service's configured duration, and existing Pending or Confirmed appointments, **then** it displays only start times that fit within those hours and do not overlap an active appointment.
2. **Given** the selected date is in the past, is a configured closed day, or has no remaining appointment times, **when** the client requests availability, **then** the application displays no bookable times and explains that no availability exists for that date. Canceled appointments do not block a time slot.

### US-03: Book an Appointment

**Priority:** Must

As a salon client, I want to book one service by choosing a date and available time and entering my contact information, so that I can request a salon visit.

**Acceptance Criteria**

1. **Given** the client selects an active service, an available future date and time, enters a name, and provides at least one valid contact method (email address or phone number), **when** the client submits the booking, **then** the application creates one appointment with Pending status and displays the booking details.
2. **Given** a required field is empty, the name is missing, both contact methods are missing or invalid, the service is inactive, or the selected time is no longer available, **when** the client submits the booking, **then** the application rejects the request, identifies the validation problem, and does not create an appointment.

### US-04: View My Appointments

**Priority:** Must

As a salon client, I want to find my appointments using the contact information provided when booking, so that I can keep track of my scheduled salon visits.

**Acceptance Criteria**

1. **Given** the client supplies the email address or phone number used for a booking, **when** the client requests their appointment list, **then** the application displays only matching appointments with their date, time, and selected service.
2. **Given** no appointments match the supplied contact information or the contact field is empty, **when** the client requests the list, **then** the application displays an appropriate message and does not reveal another client's appointments.

### US-05: View Appointment Status

**Priority:** Should

As a salon client, I want to view the status of one of my appointments, so that I know whether the booking is pending, confirmed, completed, or canceled.

**Acceptance Criteria**

1. **Given** an appointment matches the client's supplied booking contact information, **when** the client opens that appointment's details, **then** the application displays its current status as Pending, Confirmed, Completed, or Canceled.
2. **Given** an appointment does not exist or does not match the client's supplied booking contact information, **when** the client attempts to view it, **then** the application displays a not-found or unavailable message and does not disclose the appointment's details or status.

### US-10: View Salon Location and Parking Information

**Priority:** Could

As a salon client, I want to view the salon's published location and parking information, so that I can plan my visit.

**Acceptance Criteria**

1. **Given** the salon address and/or parking information has been configured, **when** the client opens the location section, **then** the application displays the published address and any available parking details.
2. **Given** the address or parking details have not been provided, **when** the client opens the location section, **then** the application identifies the missing information and does not invent or display unverified details.

## 3. Staff User Stories

### US-06: View Daily Appointment Schedule

**Priority:** Must

As a salon receptionist, I want to view appointments for a selected salon-local date, so that I can organize the day's activities.

**Acceptance Criteria**

1. **Given** appointments exist for the selected date, **when** authorized staff opens the daily schedule, **then** the application displays each appointment in time order with its time, service, customer name and contact details, and current status.
2. **Given** no appointments exist for the selected date, **when** authorized staff opens the schedule, **then** the application displays an empty-schedule message; a user without staff authorization cannot access customer schedule details.

### US-07: Confirm Appointment Requests

**Priority:** Must

As a salon receptionist, I want to confirm pending appointment requests, so that clients know their bookings have been accepted.

**Acceptance Criteria**

1. **Given** an appointment has Pending status, **when** authorized staff confirms it, **then** the application changes its status to Confirmed and the updated status is available for the client to view.
2. **Given** the appointment does not exist, is already Canceled or Completed, or the requester is not authorized staff, **when** a confirmation is attempted, **then** the application rejects the action and leaves the appointment unchanged.

### US-08: Mark Appointments as Completed

**Priority:** Must

As a salon receptionist, I want to mark a confirmed appointment as completed, so that the salon maintains accurate appointment records.

**Acceptance Criteria**

1. **Given** an appointment has Confirmed status, **when** authorized staff marks it as completed, **then** the application changes its status to Completed.
2. **Given** the appointment does not exist, is not Confirmed, or the requester is not authorized staff, **when** completion is attempted, **then** the application rejects the action and leaves the status unchanged.

### US-09: Cancel Appointments

**Priority:** Must

As a salon receptionist, I want to cancel a pending or confirmed appointment, so that the schedule reflects appointments that will no longer take place.

**Acceptance Criteria**

1. **Given** an appointment has Pending or Confirmed status, **when** authorized staff cancels it, **then** the application changes its status to Canceled and the canceled appointment no longer blocks that time slot in availability results.
2. **Given** the appointment does not exist, is already Completed or Canceled, or the requester is not authorized staff, **when** cancellation is attempted, **then** the application rejects the action and leaves the appointment unchanged.

## 4. Service Administration User Stories

### US-11: Add Salon Services

**Priority:** Should

As an authorized salon staff member, I want to add a salon service with its name, description, and duration, so that clients can see services offered by the salon.

**Acceptance Criteria**

1. **Given** authorized staff enters a non-empty service name and description and a positive service duration, **when** the staff member saves the service, **then** the application adds it as an active service in the service listing.
2. **Given** a required field is empty, the duration is zero or negative, or the requester is not authorized staff, **when** the service is submitted, **then** the application rejects the entry and displays a validation or authorization message.

### US-12: Update Salon Services

**Priority:** Should

As an authorized salon staff member, I want to update an existing service's details, so that the service listing remains accurate.

**Acceptance Criteria**

1. **Given** an active service exists and authorized staff enters a valid name, description, and positive duration, **when** the staff member saves the changes, **then** the application stores the updated details and displays the updated service in the listing.
2. **Given** the service does not exist, required details are invalid, or the requester is not authorized staff, **when** an update is submitted, **then** the application rejects the update and preserves the existing service details.

### US-13: Deactivate Salon Services

**Priority:** Should

As an authorized salon staff member, I want to deactivate a service that is no longer offered, so that clients cannot book an unavailable service.

**Acceptance Criteria**

1. **Given** an active service exists, **when** authorized staff deactivates it, **then** the service no longer appears as bookable in the client service listing and existing appointment records remain intact.
2. **Given** the service does not exist or the requester is not authorized staff, **when** deactivation is attempted, **then** the application rejects the action and makes no changes.

## 5. Priority Summary

| Priority | Story IDs | Total |
|---|---|---:|
| Must | US-01, US-02, US-03, US-04, US-06, US-07, US-08, US-09 | 8 |
| Should | US-05, US-11, US-12, US-13 | 4 |
| Could | US-10 | 1 |
| **Total** | **US-01 to US-13** | **13** |

## 6. Assignment Reflection Questions

### Question 1: Which story did you split into smaller stories, and why?

I split the appointment-booking process into two stories: US-02 (View Available Appointment Times) and US-03 (Book an Appointment). These represent different client activities. Viewing availability lets a client inspect possible times, while booking submits a request and validates the client's information. Separating them makes each activity easier to understand, implement, and test independently.

I also split the original staff status-management story into US-08 (Mark Appointments as Completed) and US-09 (Cancel Appointments), because completion and cancellation have different conditions and outcomes. I separated the original service-administration story into US-11 (Add), US-12 (Update), and US-13 (Deactivate) so that each operation can be tested independently.

### Question 2: Which story was hardest to write acceptance criteria for? What made it hard?

US-02 (View Available Appointment Times) was the hardest because availability depends on the selected service's duration, the requested date, configured business hours, and existing appointments. The criteria need to prevent a client from being offered a time that is already occupied or outside the salon's configured schedule. The prototype therefore uses configurable sample scheduling data and checks for overlaps with Pending and Confirmed appointments.

## 7. AI Assistance Log – INVEST Review

**Tool:** GitHub Copilot Chat in the project workspace.

**Review prompt used:**

> Here are my user stories for a Flask prototype. Check each one against INVEST and tell me which are too big, vague or not testable. Do not rewrite them; list problems only.
>
> Review all 10 stories in my USER_STORIES.md.
>
> For each story:
> 1. Identify any INVEST principle it may violate.
> 2. Explain why the story may be too large, vague, dependent, or difficult to test.
> 3. Identify acceptance criteria that are ambiguous or missing edge cases.
> 4. Do not rewrite my stories or acceptance criteria.
>
> Return a numbered review using the story IDs US-01 through US-10.

**Copilot review findings and decisions**

The review was performed on the original ten-story draft (US-01 through US-10). The decisions below explain how that feedback was applied to the revised backlog. The story IDs in the first column refer to the original draft.

| Original story | Copilot finding | Decision and application |
|---|---|---|
| US-01 – Browse Salon Services | “Available” services and the required description were not defined; incomplete services and load failures were not addressed. | Accepted the need to distinguish active, complete services from inactive or incomplete entries. A detailed network-failure scenario was left outside the core prototype. |
| US-02 – View Available Appointment Times | Availability rules were vague; duration, business hours, closed days, canceled bookings, past dates, and simultaneous booking attempts needed consideration. | Accepted configured service duration, salon hours, closed days, past-date checks, and overlap handling. Canceled appointments are not treated as active bookings. Rejected simultaneous multi-user concurrency handling as beyond the initial prototype. |
| US-03 – Book an Appointment | Required contact fields and validation were unclear; invalid services and unavailable times were not covered. | Accepted clearer contact requirements and validation for missing or invalid contact details, inactive services, and unavailable times. Rejected advanced duplicate-submission and concurrency controls. |
| US-04 – View My Appointments | The method for identifying a client's appointments was unspecified; the story overlapped with status display. | Accepted using booking contact information to find a client's appointment list and protecting unmatched records. Separated appointment-list viewing from opening an individual appointment's status details. A full account-registration system remains outside the prototype. |
| US-05 – Check Appointment Confirmation Status | Criteria covered only Confirmed status despite listing four statuses; the story overlapped with US-04. | Accepted criteria for all four supported statuses. Kept a separate status-details story by defining US-04 as the appointment list and US-05 as the detail/status view. |
| US-06 – View Daily Appointment Schedule | Selected date, daily boundaries, displayed customer details, ordering, and access control needed clarification. | Accepted a selected salon-local date, time-ordered results, defined displayed fields, and a staff authorization condition. Rejected advanced time-zone conversion. |
| US-07 – Confirm Appointment Requests | Staff authorization and invalid status changes were not sufficiently testable. | Accepted authorization checks and rejection of invalid status transitions. |
| US-08 – Update Appointment Status | Completion and cancellation were bundled, and cancellation was not tested. | Accepted the split into US-08 (Mark Appointments as Completed) and US-09 (Cancel Appointments), each with its own valid and invalid conditions. |
| US-09 – Manage Salon Services | Add, update, and remove operations were bundled; only adding had acceptance criteria. | Accepted the split into US-11 (Add), US-12 (Update), and US-13 (Deactivate). Deactivation is used instead of permanent deletion so existing appointment records remain intact. |
| US-10 – View Salon Location and Parking Information | Required location and parking information were not defined. | Accepted criteria that display only configured information and identify missing details without inventing an address or parking policy. |

**Overall decision:** I accepted feedback that improved story size, clarity, authorization, validation, and testability. I did not add production-level functionality such as full customer account registration, complex time-zone conversion, or simultaneous-booking infrastructure because those features are outside the intended prototype scope.

## 8. Repository

GitHub: https://github.com/iamwaqarjaved/egn475-bella-vista-salon

**Author:** Waqar Javed  
**Course:** EGN 475 – Software Prototyping
