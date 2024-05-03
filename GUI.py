import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox


class EventManagementSystem(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Event Management System")

        # Create notebook
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(pady=10, expand=True, fill="both")

        # Employee tab
        self.employee_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.employee_frame, text="Employees")
        self.create_employee_widgets()

        # Event tab
        self.event_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.event_frame, text="Events")
        self.create_event_widgets()

        # Client tab
        self.client_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.client_frame, text="Clients")
        self.create_client_widgets()

        # Guest tab
        self.guest_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.guest_frame, text="Guests")
        self.create_guest_widgets()

        # Venue tab
        self.venue_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.venue_frame, text="Venues")
        self.create_venue_widgets()

        # Supplier tab
        self.supplier_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.supplier_frame, text="Suppliers")
        self.create_supplier_widgets()

    # Employee methods
    def create_employee_widgets(self):
        self.employee_label = ttk.Label(self.employee_frame, text="Employee ID:")
        self.employee_label.grid(row=0, column=0, padx=10, pady=5)

        self.employee_id_entry = ttk.Entry(self.employee_frame)
        self.employee_id_entry.grid(row=0, column=1, padx=10, pady=5)

        self.employee_button = ttk.Button(self.employee_frame, text="Display Details", command=self.display_employee_details)
        self.employee_button.grid(row=0, column=2, padx=10, pady=5)

        # Add/Delete/Modify buttons
        self.add_employee_button = ttk.Button(self.employee_frame, text="Add", command=self.add_employee)
        self.add_employee_button.grid(row=2, column=0, padx=10, pady=5)

        self.delete_employee_button = ttk.Button(self.employee_frame, text="Delete", command=self.delete_employee)
        self.delete_employee_button.grid(row=2, column=1, padx=10, pady=5)

        self.modify_employee_button = ttk.Button(self.employee_frame, text="Modify", command=self.modify_employee)
        self.modify_employee_button.grid(row=2, column=2, padx=10, pady=5)

        self.employee_details_text = tk.Text(self.employee_frame, width=50, height=10)
        self.employee_details_text.grid(row=1, columnspan=3, padx=10, pady=5)

    def display_employee_details(self):
        employee_id = self.employee_id_entry.get()
        employee_details = {
            "Name": "Susan Meyers", "Employee ID": "47899", "Department": "Sales Manager", "Job Title": "Sales Manager","Basic Salary": 37500, "Age": 35, "Date of Birth": "01-01-1989", "Passport Details": "XX1234567",
            "Name": "Shyam Sundar", "Employee ID": "11234", "Department": "Sales ", "Job Title": "Salesperson","Basic Salary": 20000, "Age": 28, "Date of Birth": "15-05-1996", "Passport Details": "YY2345678",
            "Name": "Salma J Sam", "Employee ID": "98637", "Department": "Sales ", "Job Title": "Salesperson","Basic Salary": 20000, "Age": 30, "Date of Birth": "20-07-1994", "Passport Details": "ZZ3456789",
            "Name": "Joy Rogers", "Employee ID": "81774", "Department": "Sales ", "Job Title": "Sales Manager","Basic Salary": 24000, "Age": 40, "Date of Birth": "10-10-1984", "Passport Details": "AA4567890",
            "Name": "Mariam Khalid", "Employee ID": "98394", "Department": "Sales ", "Job Title": "Salesperson","Basic Salary": 20000, "Age": 27, "Date of Birth": "25-12-1997", "Passport Details": "BB5678901"
        }
        self.display_details(employee_details, self.employee_details_text)

    def add_employee(self):
        # Implement add employee functionality
        # Create a dialog box to input new employee details
        add_dialog = tk.Toplevel()
        self.employee_details = {}
        add_dialog.title("Add Employee")

        # Employee details entry fields
        ttk.Label(add_dialog, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        name_entry = ttk.Entry(add_dialog)
        name_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(add_dialog, text="Employee ID:").grid(row=1, column=0, padx=5, pady=5)
        id_entry = ttk.Entry(add_dialog)
        id_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(add_dialog, text="Department:").grid(row=2, column=0, padx=5, pady=5)
        department_entry = ttk.Entry(add_dialog)
        department_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(add_dialog, text="Job Title:").grid(row=3, column=0, padx=5, pady=5)
        job_title_entry = ttk.Entry(add_dialog)
        job_title_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(add_dialog, text="Basic Salary:").grid(row=4, column=0, padx=5, pady=5)
        salary_entry = ttk.Entry(add_dialog)
        salary_entry.grid(row=4, column=1, padx=5, pady=5)

        ttk.Label(add_dialog, text="Age:").grid(row=5, column=0, padx=5, pady=5)
        age_entry = ttk.Entry(add_dialog)
        age_entry.grid(row=5, column=1, padx=5, pady=5)

        ttk.Label(add_dialog, text="Date of Birth:").grid(row=6, column=0, padx=5, pady=5)
        dob_entry = ttk.Entry(add_dialog)
        dob_entry.grid(row=6, column=1, padx=5, pady=5)

        ttk.Label(add_dialog, text="Passport Details:").grid(row=7, column=0, padx=5, pady=5)
        passport_entry = ttk.Entry(add_dialog)
        passport_entry.grid(row=7, column=1, padx=5, pady=5)

        # Function to add the new employee
        def add_employee_confirm():
            new_employee_details = {
                "Name": name_entry.get(),
                "Employee ID": id_entry.get(),
                "Department": department_entry.get(),
                "Job Title": job_title_entry.get(),
                "Basic Salary": int(salary_entry.get()),
                "Age": int(age_entry.get()),
                "Date of Birth": dob_entry.get(),
                "Passport Details": passport_entry.get()
            }

            # Save the new employee details
            self.employee_details[new_employee_details["Employee ID"]] = new_employee_details

            # Update display
            self.display_details(self.employee_details, self.employee_details_text)

            add_dialog.destroy()

        # Button to confirm adding employee
        ttk.Button(add_dialog, text="Add Employee", command=add_employee_confirm).grid(row=8, columnspan=2, padx=5,pady=10)

    def delete_employee(self):
        # Create a dialog box to input the employee ID to be deleted
        self.employee_details = {}  # Define it here
        delete_dialog = tk.Toplevel()
        delete_dialog.title("Delete Employee")

        ttk.Label(delete_dialog, text="Enter Employee ID to delete:").grid(row=0, column=0, padx=5, pady=5)
        id_entry = ttk.Entry(delete_dialog)
        id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Function to confirm deletion
        def delete_confirm():
            employee_id = id_entry.get()
            if employee_id in self.employee_details:
                del self.employee_details[employee_id]
                self.display_details(self.employee_details, self.employee_details_text)
                delete_dialog.destroy()
            else:
                messagebox.showerror("Error", "Employee ID not found")

        # Button to confirm deletion
        ttk.Button(delete_dialog, text="Delete Employee", command=delete_confirm).grid(row=1, columnspan=2, padx=5,pady=10)

    def modify_employee(self):
        # Create a dialog box to input the employee ID to be modified
        modify_dialog = tk.Toplevel()
        self.employee_details = {}
        modify_dialog.title("Modify Employee")

        ttk.Label(modify_dialog, text="Enter Employee ID to modify:").grid(row=0, column=0, padx=5, pady=5)
        id_entry = ttk.Entry(modify_dialog)
        id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Employee details entry fields
        ttk.Label(modify_dialog, text="New Name:").grid(row=1, column=0, padx=5, pady=5)
        new_name_entry = ttk.Entry(modify_dialog)
        new_name_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(modify_dialog, text="New Department:").grid(row=2, column=0, padx=5, pady=5)
        new_department_entry = ttk.Entry(modify_dialog)
        new_department_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(modify_dialog, text="New Job Title:").grid(row=3, column=0, padx=5, pady=5)
        new_job_title_entry = ttk.Entry(modify_dialog)
        new_job_title_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(modify_dialog, text="New Basic Salary:").grid(row=4, column=0, padx=5, pady=5)
        new_salary_entry = ttk.Entry(modify_dialog)
        new_salary_entry.grid(row=4, column=1, padx=5, pady=5)

        ttk.Label(modify_dialog, text="New Age:").grid(row=5, column=0, padx=5, pady=5)
        new_age_entry = ttk.Entry(modify_dialog)
        new_age_entry.grid(row=5, column=1, padx=5, pady=5)

        ttk.Label(modify_dialog, text="New Date of Birth:").grid(row=6, column=0, padx=5, pady=5)
        new_dob_entry = ttk.Entry(modify_dialog)
        new_dob_entry.grid(row=6, column=1, padx=5, pady=5)

        ttk.Label(modify_dialog, text="New Passport Details:").grid(row=7, column=0, padx=5, pady=5)
        new_passport_entry = ttk.Entry(modify_dialog)
        new_passport_entry.grid(row=7, column=1, padx=5, pady=5)

        # Function to confirm modification
        def modify_confirm():
            employee_id = id_entry.get()
            if employee_id in self.employee_details:
                # Update employee details
                self.employee_details[employee_id]["Name"] = new_name_entry.get()
                self.employee_details[employee_id]["Department"] = new_department_entry.get()
                self.employee_details[employee_id]["Job Title"] = new_job_title_entry.get()
                self.employee_details[employee_id]["Basic Salary"] = int(new_salary_entry.get())
                self.employee_details[employee_id]["Age"] = int(new_age_entry.get())
                self.employee_details[employee_id]["Date of Birth"] = new_dob_entry.get()
                self.employee_details[employee_id]["Passport Details"] = new_passport_entry.get()

                # Update display
                self.display_details(self.employee_details, self.employee_details_text)
                modify_dialog.destroy()
            else:
                messagebox.showerror("Error", "Employee ID not found")

        # Button to confirm modification
        ttk.Button(modify_dialog, text="Modify Employee", command=modify_confirm).grid(row=8, columnspan=2, padx=5,pady=10)

    # Event methods
    def create_event_widgets(self):
        # Similar to create_employee_widgets, you can add widgets for events here
        self.event_label = ttk.Label(self.event_frame, text="Event ID:")
        self.event_label.grid(row=0, column=0, padx=10, pady=5)

        self.event_id_entry = ttk.Entry(self.event_frame)
        self.event_id_entry.grid(row=0, column=1, padx=10, pady=5)

        self.event_button = ttk.Button(self.event_frame, text="Display Details", command=self.display_event_details)
        self.event_button.grid(row=0, column=2, padx=10, pady=5)

        # Add/Delete/Modify buttons
        self.add_event_button = ttk.Button(self.event_frame, text="Add", command=self.add_event)
        self.add_event_button.grid(row=2, column=0, padx=10, pady=5)

        self.delete_event_button = ttk.Button(self.event_frame, text="Delete", command=self.delete_event)
        self.delete_event_button.grid(row=2, column=1, padx=10, pady=5)

        self.modify_event_button = ttk.Button(self.event_frame, text="Modify", command=self.modify_event)
        self.modify_event_button.grid(row=2, column=2, padx=10, pady=5)

        self.event_details_text = tk.Text(self.event_frame, width=50, height=10)
        self.event_details_text.grid(row=1, columnspan=3, padx=10, pady=5)
    def display_event_details(self):
        event_id = self.event_id_entry.get()
        # Fetch details from database or the created objects
        event_details = {
            "Event": "EV001","Type": "Wedding","Theme": "Traditional","Date": "2024-06-15","Time":  "18:00","Duration": "5 hours", "Venue address": "123 Main St","Client ID":  "C001","Guest list": ("G001", "G002"),"Invoice": "INV001"}

        self.display_details(event_details, self.event_details_text)

    def add_event(self):
        # Create a dialog box to input new event details
        add_dialog = tk.Toplevel()
        self.event_details = {}
        add_dialog.title("Add Event")

        # Event details entry fields
        ttk.Label(add_dialog, text="Event ID:").grid(row=0, column=0, padx=5, pady=5)
        event_id_entry = ttk.Entry(add_dialog)
        event_id_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(add_dialog, text="Event Type:").grid(row=1, column=0, padx=5, pady=5)
        event_type_entry = ttk.Entry(add_dialog)
        event_type_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(add_dialog, text="Event Theme:").grid(row=2, column=0, padx=5, pady=5)
        event_theme_entry = ttk.Entry(add_dialog)
        event_theme_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(add_dialog, text="Event Date:").grid(row=3, column=0, padx=5, pady=5)
        event_date_entry = ttk.Entry(add_dialog)
        event_date_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(add_dialog, text="Event Time:").grid(row=4, column=0, padx=5, pady=5)
        event_time_entry = ttk.Entry(add_dialog)
        event_time_entry.grid(row=4, column=1, padx=5, pady=5)

        ttk.Label(add_dialog, text="Event Duration:").grid(row=5, column=0, padx=5, pady=5)
        event_duration_entry = ttk.Entry(add_dialog)
        event_duration_entry.grid(row=5, column=1, padx=5, pady=5)

        ttk.Label(add_dialog, text="Venue Address:").grid(row=6, column=0, padx=5, pady=5)
        venue_address_entry = ttk.Entry(add_dialog)
        venue_address_entry.grid(row=6, column=1, padx=5, pady=5)

        ttk.Label(add_dialog, text="Client ID:").grid(row=7, column=0, padx=5, pady=5)
        client_id_entry = ttk.Entry(add_dialog)
        client_id_entry.grid(row=7, column=1, padx=5, pady=5)

        ttk.Label(add_dialog, text="Guest List:").grid(row=8, column=0, padx=5, pady=5)
        guest_list_entry = ttk.Entry(add_dialog)
        guest_list_entry.grid(row=8, column=1, padx=5, pady=5)

        ttk.Label(add_dialog, text="Invoice:").grid(row=9, column=0, padx=5, pady=5)
        invoice_entry = ttk.Entry(add_dialog)
        invoice_entry.grid(row=9, column=1, padx=5, pady=5)

        # Function to add the new event
        def add_event_confirm():
            new_event_details = {
                "Event": event_id_entry.get(),
                "Type": event_type_entry.get(),
                "Theme": event_theme_entry.get(),
                "Date": event_date_entry.get(),
                "Time": event_time_entry.get(),
                "Duration": event_duration_entry.get(),
                "Venue address": venue_address_entry.get(),
                "Client ID": client_id_entry.get(),
                "Guest list": tuple(guest_list_entry.get().split(',')),
                "Invoice": invoice_entry.get()
            }
            # Here you can add code to save the new event details
            # For now, just print the details
            print("New Event Details:", new_event_details)
            add_dialog.destroy()

        # Button to confirm adding event
        ttk.Button(add_dialog, text="Add Event", command=add_event_confirm).grid(row=10, columnspan=2, padx=5, pady=10)

    def delete_event(self):
        # Create a dialog box to input the event ID to be deleted
        delete_dialog = tk.Toplevel()
        self.event_details = {}
        delete_dialog.title("Delete Event")

        ttk.Label(delete_dialog, text="Enter Event ID to delete:").grid(row=0, column=0, padx=5, pady=5)
        id_entry = ttk.Entry(delete_dialog)
        id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Function to confirm deletion
        def delete_confirm():
            event_id = id_entry.get()
            if event_id in self.event_details:
                del self.event_details[event_id]
                self.display_details(self.event_details, self.event_details_text)
                delete_dialog.destroy()
            else:
                messagebox.showerror("Error", "Event ID not found")

        # Button to confirm deletion
        ttk.Button(delete_dialog, text="Delete Event", command=delete_confirm).grid(row=1, columnspan=2, padx=5,
                                                                                    pady=10)

    def modify_event(self):
        # Create a dialog box to input the event ID to be modified
        modify_dialog = tk.Toplevel()
        self.event_details = {}
        modify_dialog.title("Modify Event")

        ttk.Label(modify_dialog, text="Enter Event ID to modify:").grid(row=0, column=0, padx=5, pady=5)
        id_entry = ttk.Entry(modify_dialog)
        id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Event details entry fields
        ttk.Label(modify_dialog, text="New Event Type:").grid(row=1, column=0, padx=5, pady=5)
        new_type_entry = ttk.Entry(modify_dialog)
        new_type_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(modify_dialog, text="New Event Theme:").grid(row=2, column=0, padx=5, pady=5)
        new_theme_entry = ttk.Entry(modify_dialog)
        new_theme_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(modify_dialog, text="New Event Date:").grid(row=3, column=0, padx=5, pady=5)
        new_date_entry = ttk.Entry(modify_dialog)
        new_date_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(modify_dialog, text="New Event Time:").grid(row=4, column=0, padx=5, pady=5)
        new_time_entry = ttk.Entry(modify_dialog)
        new_time_entry.grid(row=4, column=1, padx=5, pady=5)

        ttk.Label(modify_dialog, text="New Event Duration:").grid(row=5, column=0, padx=5, pady=5)
        new_duration_entry = ttk.Entry(modify_dialog)
        new_duration_entry.grid(row=5, column=1, padx=5, pady=5)

        ttk.Label(modify_dialog, text="New Venue Address:").grid(row=6, column=0, padx=5, pady=5)
        new_address_entry = ttk.Entry(modify_dialog)
        new_address_entry.grid(row=6, column=1, padx=5, pady=5)

        ttk.Label(modify_dialog, text="New Client ID:").grid(row=7, column=0, padx=5, pady=5)
        new_client_entry = ttk.Entry(modify_dialog)
        new_client_entry.grid(row=7, column=1, padx=5, pady=5)

        ttk.Label(modify_dialog, text="New Guest List:").grid(row=8, column=0, padx=5, pady=5)
        new_guest_entry = ttk.Entry(modify_dialog)
        new_guest_entry.grid(row=8, column=1, padx=5, pady=5)

        ttk.Label(modify_dialog, text="New Invoice:").grid(row=9, column=0, padx=5, pady=5)
        new_invoice_entry = ttk.Entry(modify_dialog)
        new_invoice_entry.grid(row=9, column=1, padx=5, pady=5)

        # Function to confirm modification
        def modify_confirm():
            event_id = id_entry.get()
            if event_id in self.event_details:
                # Update event details
                self.event_details[event_id]["Type"] = new_type_entry.get()
                self.event_details[event_id]["Theme"] = new_theme_entry.get()
                self.event_details[event_id]["Date"] = new_date_entry.get()
                self.event_details[event_id]["Time"] = new_time_entry.get()
                self.event_details[event_id]["Duration"] = new_duration_entry.get()
                self.event_details[event_id]["Venue address"] = new_address_entry.get()
                self.event_details[event_id]["Client ID"] = new_client_entry.get()
                self.event_details[event_id]["Guest list"] = tuple(new_guest_entry.get().split(','))
                self.event_details[event_id]["Invoice"] = new_invoice_entry.get()

                # Update display
                self.display_details(self.event_details, self.event_details_text)
                modify_dialog.destroy()
            else:
                messagebox.showerror("Error", "Event ID not found")

        # Button to confirm modification
        ttk.Button(modify_dialog, text="Modify Event", command=modify_confirm).grid(row=10, columnspan=2, padx=5,
                                                                                    pady=10)

    # Client methods
    def create_client_widgets(self):
        # Similar to create_employee_widgets, you can add widgets for clients here
        self.client_label = ttk.Label(self.client_frame, text="Client ID:")
        self.client_label.grid(row=0, column=0, padx=10, pady=5)

        self.client_id_entry = ttk.Entry(self.client_frame)
        self.client_id_entry.grid(row=0, column=1, padx=10, pady=5)

        self.client_button = ttk.Button(self.client_frame, text="Display Details", command=self.display_client_details)
        self.client_button.grid(row=0, column=2, padx=10, pady=5)

        # Add/Delete/Modify buttons
        self.add_client_button = ttk.Button(self.client_frame, text="Add", command=self.add_client)
        self.add_client_button.grid(row=2, column=0, padx=10, pady=5)

        self.delete_client_button = ttk.Button(self.client_frame, text="Delete", command=self.delete_client)
        self.delete_client_button.grid(row=2, column=1, padx=10, pady=5)

        self.modify_client_button = ttk.Button(self.client_frame, text="Modify", command=self.modify_client)
        self.modify_client_button.grid(row=2, column=2, padx=10, pady=5)

        self.client_details_text = tk.Text(self.client_frame, width=50, height=10)
        self.client_details_text.grid(row=1, columnspan=3, padx=10, pady=5)
        #pass

    def display_client_details(self):
        client_id = self.client_id_entry.get()
        client_details = {
            "Client ID": "C001", "Name": "Dana Ali", "Address": "456 Elm St", "Contact details": "050-456-7890", "Budget": 20000}
        self.display_details(client_details, self.client_details_text)

    def add_client(self):
        # Create a dialog box to input new client details
        add_dialog = tk.Toplevel()
        self.client_details = {}
        add_dialog.title("Add Client")

        # Client details entry fields
        ttk.Label(add_dialog, text="Client ID:").grid(row=0, column=0, padx=5, pady=5)
        client_id_entry = ttk.Entry(add_dialog)
        client_id_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(add_dialog, text="Name:").grid(row=1, column=0, padx=5, pady=5)
        name_entry = ttk.Entry(add_dialog)
        name_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(add_dialog, text="Address:").grid(row=2, column=0, padx=5, pady=5)
        address_entry = ttk.Entry(add_dialog)
        address_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(add_dialog, text="Contact details:").grid(row=3, column=0, padx=5, pady=5)
        contact_entry = ttk.Entry(add_dialog)
        contact_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(add_dialog, text="Budget:").grid(row=4, column=0, padx=5, pady=5)
        budget_entry = ttk.Entry(add_dialog)
        budget_entry.grid(row=4, column=1, padx=5, pady=5)

        # Function to add the new client
        def add_client_confirm():
            new_client_details = {
                "Client ID": client_id_entry.get(),
                "Name": name_entry.get(),
                "Address": address_entry.get(),
                "Contact details": contact_entry.get(),
                "Budget": int(budget_entry.get())
            }
            print("New Client Details:", new_client_details)
            add_dialog.destroy()

        # Button to confirm adding client
        ttk.Button(add_dialog, text="Add Client", command=add_client_confirm).grid(row=5, columnspan=2, padx=5, pady=10)

    def delete_client(self):
        # Create a dialog box to input the client ID to be deleted
        delete_dialog = tk.Toplevel()
        self.client_details = {}
        delete_dialog.title("Delete Client")

        ttk.Label(delete_dialog, text="Enter Client ID to delete:").grid(row=0, column=0, padx=5, pady=5)
        id_entry = ttk.Entry(delete_dialog)
        id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Function to confirm deletion
        def delete_confirm():
            client_id = id_entry.get()
            if client_id in self.client_details:
                del self.client_details[client_id]
                self.display_details(self.client_details, self.client_details_text)
                delete_dialog.destroy()
            else:
                messagebox.showerror("Error", "Client ID not found")

        # Button to confirm deletion
        ttk.Button(delete_dialog, text="Delete Client", command=delete_confirm).grid(row=1, columnspan=2, padx=5,
                                                                                     pady=10)

    def modify_client(self):
        # Create a dialog box to input the client ID to be modified
        modify_dialog = tk.Toplevel()
        self.client_details = {}
        modify_dialog.title("Modify Client")

        ttk.Label(modify_dialog, text="Enter Client ID to modify:").grid(row=0, column=0, padx=5, pady=5)
        id_entry = ttk.Entry(modify_dialog)
        id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Client details entry fields
        ttk.Label(modify_dialog, text="New Name:").grid(row=1, column=0, padx=5, pady=5)
        new_name_entry = ttk.Entry(modify_dialog)
        new_name_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(modify_dialog, text="New Address:").grid(row=2, column=0, padx=5, pady=5)
        new_address_entry = ttk.Entry(modify_dialog)
        new_address_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(modify_dialog, text="New Contact details:").grid(row=3, column=0, padx=5, pady=5)
        new_contact_entry = ttk.Entry(modify_dialog)
        new_contact_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(modify_dialog, text="New Budget:").grid(row=4, column=0, padx=5, pady=5)
        new_budget_entry = ttk.Entry(modify_dialog)
        new_budget_entry.grid(row=4, column=1, padx=5, pady=5)

        # Function to confirm modification
        def modify_confirm():
            client_id = id_entry.get()
            if client_id in self.client_details:
                # Update client details
                self.client_details[client_id]["Name"] = new_name_entry.get()
                self.client_details[client_id]["Address"] = new_address_entry.get()
                self.client_details[client_id]["Contact details"] = new_contact_entry.get()
                self.client_details[client_id]["Budget"] = int(new_budget_entry.get())

                # Update display
                self.display_details(self.client_details, self.client_details_text)
                modify_dialog.destroy()
            else:
                messagebox.showerror("Error", "Client ID not found")

        # Button to confirm modification
        ttk.Button(modify_dialog, text="Modify Client", command=modify_confirm).grid(row=5, columnspan=2, padx=5,
                                                                                     pady=10)

    # Guest methods
    def create_guest_widgets(self):
        self.guest_label = ttk.Label(self.guest_frame, text="Guest ID:")
        self.guest_label.grid(row=0, column=0, padx=10, pady=5)

        self.guest_id_entry = ttk.Entry(self.guest_frame)
        self.guest_id_entry.grid(row=0, column=1, padx=10, pady=5)

        self.guest_button = ttk.Button(self.guest_frame, text="Display Details", command=self.display_guest_details)
        self.guest_button.grid(row=0, column=2, padx=10, pady=5)

        # Add/Delete/Modify buttons
        self.add_guest_button = ttk.Button(self.guest_frame, text="Add", command=self.add_guest)
        self.add_guest_button.grid(row=2, column=0, padx=10, pady=5)

        self.delete_guest_button = ttk.Button(self.guest_frame, text="Delete", command=self.delete_guest)
        self.delete_guest_button.grid(row=2, column=1, padx=10, pady=5)

        self.modify_guest_button = ttk.Button(self.guest_frame, text="Modify", command=self.modify_guest)
        self.modify_guest_button.grid(row=2, column=2, padx=10, pady=5)

        self.guest_details_text = tk.Text(self.guest_frame, width=50, height=10)
        self.guest_details_text.grid(row=1, columnspan=3, padx=10, pady=5)
        # pass

    def display_guest_details(self):
        guest_id = self.guest_id_entry.get()
        guest_details = {
            "Guest ID": "G001", "Name": "Alia", "Address": "457 Elm St", "Contact details": "052-222-3333",
            "Guest ID": "G002", "Name": "Khalid", "Address": "458 Elm St", "Contact details": "055-555-6666"
        }
        self.display_details(guest_details, self.guest_details_text)

    def add_guest(self):
        # Create a dialog box to input new guest details
        add_dialog = tk.Toplevel()
        self.guest_details = {}
        add_dialog.title("Add Guest")

        # Guest details entry fields
        ttk.Label(add_dialog, text="Guest ID:").grid(row=0, column=0, padx=5, pady=5)
        guest_id_entry = ttk.Entry(add_dialog)
        guest_id_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(add_dialog, text="Name:").grid(row=1, column=0, padx=5, pady=5)
        name_entry = ttk.Entry(add_dialog)
        name_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(add_dialog, text="Address:").grid(row=2, column=0, padx=5, pady=5)
        address_entry = ttk.Entry(add_dialog)
        address_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(add_dialog, text="Contact details:").grid(row=3, column=0, padx=5, pady=5)
        contact_entry = ttk.Entry(add_dialog)
        contact_entry.grid(row=3, column=1, padx=5, pady=5)

        # Function to add the new guest
        def add_guest_confirm():
            new_guest_details = {
                "Guest ID": guest_id_entry.get(),
                "Name": name_entry.get(),
                "Address": address_entry.get(),
                "Contact details": contact_entry.get()
            }
            print("New Guest Details:", new_guest_details)
            add_dialog.destroy()

        # Button to confirm adding guest
        ttk.Button(add_dialog, text="Add Guest", command=add_guest_confirm).grid(row=4, columnspan=2, padx=5, pady=10)

    def delete_guest(self):
        # Create a dialog box to input the guest ID to be deleted
        delete_dialog = tk.Toplevel()
        self.guest_details = {}
        delete_dialog.title("Delete Guest")

        ttk.Label(delete_dialog, text="Enter Guest ID to delete:").grid(row=0, column=0, padx=5, pady=5)
        id_entry = ttk.Entry(delete_dialog)
        id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Function to confirm deletion
        def delete_confirm():
            guest_id = id_entry.get()

            delete_dialog.destroy()

        # Button to confirm deletion
        ttk.Button(delete_dialog, text="Delete Guest", command=delete_confirm).grid(row=1, columnspan=2, padx=5,
                                                                                    pady=10)

    def modify_guest(self):
        # Create a dialog box to input the guest ID to be modified
        modify_dialog = tk.Toplevel()
        self.guest_details = {}
        modify_dialog.title("Modify Guest")

        ttk.Label(modify_dialog, text="Enter Guest ID to modify:").grid(row=0, column=0, padx=5, pady=5)
        id_entry = ttk.Entry(modify_dialog)
        id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Guest details entry fields
        ttk.Label(modify_dialog, text="New Name:").grid(row=1, column=0, padx=5, pady=5)
        new_name_entry = ttk.Entry(modify_dialog)
        new_name_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(modify_dialog, text="New Address:").grid(row=2, column=0, padx=5, pady=5)
        new_address_entry = ttk.Entry(modify_dialog)
        new_address_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(modify_dialog, text="New Contact details:").grid(row=3, column=0, padx=5, pady=5)
        new_contact_entry = ttk.Entry(modify_dialog)
        new_contact_entry.grid(row=3, column=1, padx=5, pady=5)

        # Function to confirm modification
        def modify_confirm():
            guest_id = id_entry.get()
            modify_dialog.destroy()

        # Button to confirm modification
        ttk.Button(modify_dialog, text="Modify Guest", command=modify_confirm).grid(row=4, columnspan=2, padx=5,
                                                                                    pady=10)

    # Venue methods
    def create_venue_widgets(self):
        self.venue_label = ttk.Label(self.venue_frame, text="Venue ID:")
        self.venue_label.grid(row=0, column=0, padx=10, pady=5)

        self.venue_id_entry = ttk.Entry(self.venue_frame)
        self.venue_id_entry.grid(row=0, column=1, padx=10, pady=5)

        self.venue_button = ttk.Button(self.venue_frame, text="Display Details", command=self.display_venue_details)
        self.venue_button.grid(row=0, column=2, padx=10, pady=5)

        # Add/Delete/Modify buttons
        self.add_venue_button = ttk.Button(self.venue_frame, text="Add", command=self.add_venue)
        self.add_venue_button.grid(row=2, column=0, padx=10, pady=5)

        self.delete_venue_button = ttk.Button(self.venue_frame, text="Delete", command=self.delete_venue)
        self.delete_venue_button.grid(row=2, column=1, padx=10, pady=5)

        self.modify_venue_button = ttk.Button(self.venue_frame, text="Modify", command=self.modify_venue)
        self.modify_venue_button.grid(row=2, column=2, padx=10, pady=5)

        self.venue_details_text = tk.Text(self.venue_frame, width=50, height=10)
        self.venue_details_text.grid(row=1, columnspan=3, padx=10, pady=5)

    def display_venue_details(self):
        venue_id = self.venue_id_entry.get()
        venue_details = {
            "Venue ID": "V001", "Name": "Grand Hall", "Address": "789 Maple St", "Contact details": "056-012-3456",
            "Min guest": 50, "Max guest": 200}
        self.display_details(venue_details, self.venue_details_text)

    def add_venue(self):
        # Create a dialog box to input new venue details
        add_dialog = tk.Toplevel()
        self.venue_details = {}
        add_dialog.title("Add Venue")

        # Venue details entry fields
        ttk.Label(add_dialog, text="Venue ID:").grid(row=0, column=0, padx=5, pady=5)
        venue_id_entry = ttk.Entry(add_dialog)
        venue_id_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(add_dialog, text="Name:").grid(row=1, column=0, padx=5, pady=5)
        name_entry = ttk.Entry(add_dialog)
        name_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(add_dialog, text="Address:").grid(row=2, column=0, padx=5, pady=5)
        address_entry = ttk.Entry(add_dialog)
        address_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(add_dialog, text="Contact details:").grid(row=3, column=0, padx=5, pady=5)
        contact_entry = ttk.Entry(add_dialog)
        contact_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(add_dialog, text="Min guests:").grid(row=4, column=0, padx=5, pady=5)
        min_guests_entry = ttk.Entry(add_dialog)
        min_guests_entry.grid(row=4, column=1, padx=5, pady=5)

        ttk.Label(add_dialog, text="Max guests:").grid(row=5, column=0, padx=5, pady=5)
        max_guests_entry = ttk.Entry(add_dialog)
        max_guests_entry.grid(row=5, column=1, padx=5, pady=5)

        # Function to add the new venue
        def add_venue_confirm():
            new_venue_details = {
                "Venue ID": venue_id_entry.get(),
                "Name": name_entry.get(),
                "Address": address_entry.get(),
                "Contact details": contact_entry.get(),
                "Min guest": int(min_guests_entry.get()),
                "Max guest": int(max_guests_entry.get())
            }
            print("New Venue Details:", new_venue_details)
            add_dialog.destroy()

        # Button to confirm adding venue
        ttk.Button(add_dialog, text="Add Venue", command=add_venue_confirm).grid(row=6, columnspan=2, padx=5, pady=10)

    def delete_venue(self):
        # Create a dialog box to input the venue ID to be deleted
        delete_dialog = tk.Toplevel()
        self.venue_details = {}
        delete_dialog.title("Delete Venue")

        ttk.Label(delete_dialog, text="Enter Venue ID to delete:").grid(row=0, column=0, padx=5, pady=5)
        id_entry = ttk.Entry(delete_dialog)
        id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Function to confirm deletion
        def delete_confirm():
            venue_id = id_entry.get()
            delete_dialog.destroy()

        # Button to confirm deletion
        ttk.Button(delete_dialog, text="Delete Venue", command=delete_confirm).grid(row=1, columnspan=2, padx=5,
                                                                                    pady=10)

    def modify_venue(self):
        # Create a dialog box to input the venue ID to be modified
        modify_dialog = tk.Toplevel()
        self.venue_details = {}
        modify_dialog.title("Modify Venue")

        ttk.Label(modify_dialog, text="Enter Venue ID to modify:").grid(row=0, column=0, padx=5, pady=5)
        id_entry = ttk.Entry(modify_dialog)
        id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Venue details entry fields
        ttk.Label(modify_dialog, text="New Name:").grid(row=1, column=0, padx=5, pady=5)
        new_name_entry = ttk.Entry(modify_dialog)
        new_name_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(modify_dialog, text="New Address:").grid(row=2, column=0, padx=5, pady=5)
        new_address_entry = ttk.Entry(modify_dialog)
        new_address_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(modify_dialog, text="New Contact details:").grid(row=3, column=0, padx=5, pady=5)
        new_contact_entry = ttk.Entry(modify_dialog)
        new_contact_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(modify_dialog, text="New Min guests:").grid(row=4, column=0, padx=5, pady=5)
        new_min_guests_entry = ttk.Entry(modify_dialog)
        new_min_guests_entry.grid(row=4, column=1, padx=5, pady=5)

        ttk.Label(modify_dialog, text="New Max guests:").grid(row=5, column=0, padx=5, pady=5)
        new_max_guests_entry = ttk.Entry(modify_dialog)
        new_max_guests_entry.grid(row=5, column=1, padx=5, pady=5)

        # Function to confirm modification
        def modify_confirm():
            venue_id = id_entry.get()
            modify_dialog.destroy()

        # Button to confirm modification
        ttk.Button(modify_dialog, text="Modify Venue", command=modify_confirm).grid(row=6, columnspan=2, padx=5,
                                                                                    pady=10)

    # Supplier methods
    def create_supplier_widgets(self):
        self.supplier_label = ttk.Label(self.supplier_frame, text="Supplier ID:")
        self.supplier_label.grid(row=0, column=0, padx=10, pady=5)

        self.supplier_id_entry = ttk.Entry(self.supplier_frame)
        self.supplier_id_entry.grid(row=0, column=1, padx=10, pady=5)

        self.supplier_button = ttk.Button(self.supplier_frame, text="Display Details", command=self.display_supplier_details)
        self.supplier_button.grid(row=0, column=2, padx=10, pady=5)

        # Add/Delete/Modify buttons
        self.add_supplier_button = ttk.Button(self.supplier_frame, text="Add", command=self.add_supplier)
        self.add_supplier_button.grid(row=2, column=0, padx=10, pady=5)

        self.delete_supplier_button = ttk.Button(self.supplier_frame, text="Delete", command=self.delete_supplier)
        self.delete_supplier_button.grid(row=2, column=1, padx=10, pady=5)

        self.modify_supplier_button = ttk.Button(self.supplier_frame, text="Modify", command=self.modify_supplier)
        self.modify_supplier_button.grid(row=2, column=2, padx=10, pady=5)

        self.supplier_details_text = tk.Text(self.supplier_frame, width=50, height=10)
        self.supplier_details_text.grid(row=1, columnspan=3, padx=10, pady=5)
        # pass

    def display_supplier_details(self):
        supplier_id = self.supplier_id_entry.get()
        supplier_details = {
            "SUpplier ID": "S001", "Name": "ABC Catering", "Address": "101 Oak St", "Contact details": "050-234-5678",
            "Menu": "Buffet", "Min guest": 50, "Max guest": 200}
        self.display_details(supplier_details, self.supplier_details_text)

    def add_supplier(self):
        # Create a dialog box to input new supplier details
        add_dialog = tk.Toplevel()
        self.supplier_details = {}
        add_dialog.title("Add Supplier")

        # Supplier details entry fields
        ttk.Label(add_dialog, text="Supplier ID:").grid(row=0, column=0, padx=5, pady=5)
        supplier_id_entry = ttk.Entry(add_dialog)
        supplier_id_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(add_dialog, text="Name:").grid(row=1, column=0, padx=5, pady=5)
        name_entry = ttk.Entry(add_dialog)
        name_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(add_dialog, text="Address:").grid(row=2, column=0, padx=5, pady=5)
        address_entry = ttk.Entry(add_dialog)
        address_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(add_dialog, text="Contact details:").grid(row=3, column=0, padx=5, pady=5)
        contact_entry = ttk.Entry(add_dialog)
        contact_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(add_dialog, text="Menu:").grid(row=4, column=0, padx=5, pady=5)
        menu_entry = ttk.Entry(add_dialog)
        menu_entry.grid(row=4, column=1, padx=5, pady=5)

        ttk.Label(add_dialog, text="Min guests:").grid(row=5, column=0, padx=5, pady=5)
        min_guests_entry = ttk.Entry(add_dialog)
        min_guests_entry.grid(row=5, column=1, padx=5, pady=5)

        ttk.Label(add_dialog, text="Max guests:").grid(row=6, column=0, padx=5, pady=5)
        max_guests_entry = ttk.Entry(add_dialog)
        max_guests_entry.grid(row=6, column=1, padx=5, pady=5)

        # Function to add the new supplier
        def add_supplier_confirm():
            new_supplier_details = {
                "Supplier ID": supplier_id_entry.get(),
                "Name": name_entry.get(),
                "Address": address_entry.get(),
                "Contact details": contact_entry.get(),
                "Menu": menu_entry.get(),
                "Min guest": int(min_guests_entry.get()),
                "Max guest": int(max_guests_entry.get())
            }
            print("New Supplier Details:", new_supplier_details)
            add_dialog.destroy()

        # Button to confirm adding supplier
        ttk.Button(add_dialog, text="Add Supplier", command=add_supplier_confirm).grid(row=7, columnspan=2, padx=5,
                                                                                       pady=10)

    def delete_supplier(self):
        # Create a dialog box to input the supplier ID to be deleted
        delete_dialog = tk.Toplevel()
        self.supplier_details = {}
        delete_dialog.title("Delete Supplier")

        ttk.Label(delete_dialog, text="Enter Supplier ID to delete:").grid(row=0, column=0, padx=5, pady=5)
        id_entry = ttk.Entry(delete_dialog)
        id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Function to confirm deletion
        def delete_confirm():
            supplier_id = id_entry.get()
            delete_dialog.destroy()

        # Button to confirm deletion
        ttk.Button(delete_dialog, text="Delete Supplier", command=delete_confirm).grid(row=1, columnspan=2, padx=5,
                                                                                       pady=10)

    def modify_supplier(self):
        # Create a dialog box to input the supplier ID to be modified
        modify_dialog = tk.Toplevel()
        self.supplier_details = {}
        modify_dialog.title("Modify Supplier")

        ttk.Label(modify_dialog, text="Enter Supplier ID to modify:").grid(row=0, column=0, padx=5, pady=5)
        id_entry = ttk.Entry(modify_dialog)
        id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Supplier details entry fields
        ttk.Label(modify_dialog, text="New Name:").grid(row=1, column=0, padx=5, pady=5)
        new_name_entry = ttk.Entry(modify_dialog)
        new_name_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(modify_dialog, text="New Address:").grid(row=2, column=0, padx=5, pady=5)
        new_address_entry = ttk.Entry(modify_dialog)
        new_address_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(modify_dialog, text="New Contact details:").grid(row=3, column=0, padx=5, pady=5)
        new_contact_entry = ttk.Entry(modify_dialog)
        new_contact_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(modify_dialog, text="New Menu:").grid(row=4, column=0, padx=5, pady=5)
        new_menu_entry = ttk.Entry(modify_dialog)
        new_menu_entry.grid(row=4, column=1, padx=5, pady=5)

        ttk.Label(modify_dialog, text="New Min guests:").grid(row=5, column=0, padx=5, pady=5)
        new_min_guests_entry = ttk.Entry(modify_dialog)
        new_min_guests_entry.grid(row=5, column=1, padx=5, pady=5)

        ttk.Label(modify_dialog, text="New Max guests:").grid(row=6, column=0, padx=5, pady=5)
        new_max_guests_entry = ttk.Entry(modify_dialog)
        new_max_guests_entry.grid(row=6, column=1, padx=5, pady=5)

        # Function to confirm modification
        def modify_confirm():
            supplier_id = id_entry.get()
            modify_dialog.destroy()

        # Button to confirm modification
        ttk.Button(modify_dialog, text="Modify Supplier", command=modify_confirm).grid(row=7, columnspan=2, padx=5,
                                                                                       pady=10)

    def display_details(self, details, text_widget):
        text_widget.delete(1.0, tk.END)
        for key, value in details.items():
            text_widget.insert(tk.END, f"{key}: {value}\n")

if __name__ == "__main__":
    app = EventManagementSystem()
    app.mainloop()
