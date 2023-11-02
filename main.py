import logico_text
import logico_tkinter

#If you fail because of a negation, try putting the negation and what it is negating in another layer of parenthesis
#   IE: ¬(p∧q) → q fails, but (¬(p∧q)) → q does not.
#Just run and so long as tkinter_mode = True, you should be able to run program from the start.
#The following text shortcuts replace a keyword in the input with a logical operator:
#   IE: p.and.q is the same as saying p∧q
#→ .so.
#∧ .and.
#∨ .or.
#¬ .not.
#↔ .eq.
#⊕ .xor.
#≡ .is.
#≡ .isnt.
#≡ ≢
#↑ .nand.
#↓ .nor.


if __name__ == '__main__':
    #logico_text.run()
    logico_tkinter.LogicoGUI().run()