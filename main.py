#Resibo Maker
from pyscript import document, display

def create_order(e):
    document.getElementById("receipt_output").innerHTML = ""

    drink1 = document.getElementById("Matcha1")
    drink2 = document.getElementById("Matcha2")
    drink3 = document.getElementById("Matcha3")
    drink4 = document.getElementById("Matcha4")
    drink5 = document.getElementById("Matcha5")

# Total Calculate:
    subtotal = (
        (float(drink1.value) * drink1.checked) +
        (float(drink2.value) * drink2.checked) +
        (float(drink3.value) * drink3.checked) +
        (float(drink4.value) * drink4.checked) +
        (float(drink5.value) * drink5.checked)
    )

# VAT
    vat = subtotal * 0.12
    total = subtotal + vat

    divider = "------ Receipt ------"
    subtotal_str = f"Subtotal: ₱{subtotal:.2f}"
    vat_str = f"Tax: ₱{vat:.2f}"
    total_str = f"Total: ₱{total:.2f}"

    display(divider, target="receipt_output", append=True)
    display(subtotal_str, target="receipt_output", append=True)
    display(vat_str, target="receipt_output", append=True)
    display(total_str, target="receipt_output", append=True)

#Buttons
    order_button = document.getElementById("place_order_btn")
    order_button.style.display = "inline-block"

def place_order(e):
    display("Order successfully placed!", target="receipt_output", append=True)