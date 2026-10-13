import tkinter as tk
from tkinter import simpledialog, messagebox

# تعداد فرآیندها و منابع مشخص شده
p = 5
r = 3

def get_user_input():
    def submit_data():
        try:
            allocation = [list(map(int, row.split(','))) for row in allocation_text.get("1.0", "end-1c").split('\n')]
            max_matrix = [list(map(int, row.split(','))) for row in max_text.get("1.0", "end-1c").split('\n')]

            if len(allocation) != p or any(len(row) != r for row in allocation):
                messagebox.showerror("Error", "Allocation matrix dimensions must match the number of processes and resources.")
                return

            if len(max_matrix) != p or any(len(row) != r for row in max_matrix):
                messagebox.showerror("Error", "Max matrix dimensions must match the number of processes and resources.")
                return

            root.quit()
            root.destroy()

            display_result(p, r, available, allocation, max_matrix)

        except ValueError:
            messagebox.showerror("Error", "Please enter valid data.")

    root = tk.Tk()
    root.title("Banker's Algorithm Input Form")

    tk.Label(root, text="Number of Processes:").grid(row=0, column=0)
    tk.Label(root, text=str(p)).grid(row=0, column=1)

    tk.Label(root, text="Number of Resources:").grid(row=1, column=0)
    tk.Label(root, text=str(r)).grid(row=1, column=1)

    tk.Label(root, text="Available Resources (comma-separated):").grid(row=2, column=0)
    available_entry = tk.Entry(root)
    available_entry.insert(0, "2,1,0")
    available_entry.grid(row=2, column=1)

    tk.Label(root, text="Allocation Matrix (comma-separated rows):").grid(row=3, column=0)
    allocation_text = tk.Text(root, height=p, width=30)
    allocation_text.grid(row=3, column=1)

    tk.Label(root, text="Max Matrix (comma-separated rows):").grid(row=4, column=0)
    max_text = tk.Text(root, height=p, width=30)
    max_text.grid(row=4, column=1)

    submit_button = tk.Button(root, text="Submit", command=submit_data)
    submit_button.grid(row=5, columnspan=2)

    root.mainloop()

def display_result(processes, resources, available, allocation, max_matrix):
    result_root = tk.Tk()
    result_root.title("Banker's Algorithm Input Result")

    result_text = f"""
    Number of Processes: {processes}
    Number of Resources: {resources}
    Available Resources: {available}
    Allocation Matrix: {allocation}
    Max Matrix: {max_matrix}
    """

    tk.Label(result_root, text=result_text, justify=tk.LEFT).pack()
    result_root.mainloop()

# Run the form to get user input
get_user_input()
