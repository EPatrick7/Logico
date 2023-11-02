import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

import logico

class LogicoGUI:
    def __init__(self):
        self.binary_only = False
        self.root = tk.Tk()
        self.root.title("Logico.py")

        self.details_frame = tk.Frame(self.root)
        self.details_frame.pack(side = tk.LEFT, fill = tk.X, expand = False)

        self.output = tk.Text(self.root)
        self.output.pack(side = tk.RIGHT, fill = tk.X, expand = False)

        self.details_label = tk.Label(self.details_frame, text = "Logical Expression")
        self.details_label.pack()

        self.details_entry = ScrolledText(self.details_frame, wrap = tk.WORD)
        self.details_entry.pack()

        self.evaluate = tk.Button(self.details_frame, text = "Evaluate", state = tk.NORMAL,
                                  command = self.evaluate)
        self.evaluate.pack(side = tk.LEFT, fill = tk.X, expand = True)

        self.command_text = tk.Entry(self.details_frame)

        self.refresh_toggle = tk.Checkbutton(self.details_frame, text = "Refresh",
                                             command = self.refresh)
        self.refresh_toggle.pack(side = tk.RIGHT)
        # → .so.
        # ∧ .and.
        # ∨ .or.
        # ¬ .not.
        # ↔ .eq.
        # ⊕ .xor.
        # ≡ .is.
        # ≡ .isnt.
        # ≡ ≢
        # ↑ .nand.
        # ↓ .nor.
        self.command_text.insert(0, "→∧∨¬↔⊕≡↑↓")
        self.command_text["state"] = "readonly"
        self.command_text.pack(side = tk.RIGHT)

        self.binary_button = tk.Checkbutton(self.details_frame, text = "Binary Only",
                                            command = self.toggle_binary)
        self.binary_button.pack(side = tk.RIGHT)

    def evaluate(self):
        statement = self.details_entry.get("1.0", tk.END).replace("\n", "")
        try:
            out = (logico.crunch(logico.input_statement(statement), self.binary_only))
            self.output.insert(tk.END, out + "\n")
        except Exception as e:
            messagebox.showerror("Logical Evaluation Failed:", str(e))

    def run(self):
        self.root.mainloop()

    def toggle_binary(self):
        self.binary_only = not self.binary_only

    def refresh(self):
        self.output.delete(1.0, tk.END)
        self.refresh_toggle.toggle()


if __name__ == "__main__":
    LogicoGUI().run()